# NI_LABVIEW_PROGRAMMING_REFERENCE

<!--SYSTEM_CORPUS id=NI_LABVIEW_PROGRAMMING_REFERENCE format=markdown generated=2026-07-14T12:02:18+00:00 -->
- title: LabVIEW Programming Reference Manual
- source: https://docs-be.ni.com/bundle/labview-api-ref/preprocessedpdf/enus
- source_sha256: 7a54c389b4f3d78e2215f55c9f156124d3668ce61d0d5018094e356004d895ac
- versions: 2024 Q1|2024 Q3|2025 Q1|2025 Q3|2026 Q1
- fidelity: full-text-records

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3001 ordinal=3001 -->
## Functions

Functions

Let A be an m-by-nmatrix that represents the Input Matrix, Y be the set of m
coefficients in Known Vector, and X be the set of nelements in Solution Vector that
solves the system

AX = Y

When m> n, the system has more equations than unknowns, so it is an over-
determined system. The solution that satisfies AX = Y might not exist, so the VI finds the
least-square solution X, which minimizes ||AX – Y||.

When m< n, the system has more unknowns than equations, so it is an under-
determined system. It may have infinite solutions that satisfy AX = Y. The VI finds one of
these solutions.

In the case of m= n, if A is a nonsingular matrix—no row or column is a linear
combination of any other row or column, respectively—then you can solve the system
for X by decomposing the input matrix A into its lower and upper triangular matrices, L
and U, such that

AX = LZ = Y

and

Z = UX

can be an alternate representation of the original system. Notice that Z is also an
n-element vector.

Triangular systems are easy to solve using recursive techniques. Consequently, when
you obtain the L and U matrices from A, you can find Z from the LZ = Y system and X
from the UX = Z system.

In the case of m≠ n, A can be decomposed to an orthogonal matrix Q and an upper
triangular matrix R, so that A = QR. The linear system then can be represented by QRX =
Y. You then can solve RX = QTY.

You can easily solve this triangular system to get x using recursive techniques.


                                                    © National Instruments 3001

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3001 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3002 ordinal=3002 -->
## Functions

Functions

           Note You cannot always determine beforehand whether the matrix is
                singular, especially with large systems. The Solve Linear Equations VI detects
               singular matrices and returns an error, so you do not need to verify whether
            you have a valid system before using this VI.

      The numerical implementation of the matrix inversion is numerically intensive and,
      because of its recursive nature, is also highly sensitive to round-off error introduced by
       the floating-point numeric coprocessor. Although the computations use the maximum
       possible accuracy, the VI cannot always solve the system.

      Solve Complex Linear Equations

       Let A represent the m-by-nInput Matrix, Y represent the set of melements in the
     Known Vector, and X represent the set of nelements in the Solution Vector that solves
        for the system

      AX = Y

     When m> n, the system has more equations than unknowns, so it is an over-
      determined system. Since the solution that satisfies AX = Y may not exist, the VI finds
       the least-square solution X, which minimizes ||AX – Y||.

     When m< n, the system has more unknowns than equations, so it is an under-
      determined system. It might have infinite solutions that satisfy AX = Y. The VI then
        selects one of these solutions.

     When m= n, if A is a nonsingular matrix—no row or column is a linear combination of
      any other row or column, respectively—then you can solve the system for X by
      decomposing the Input Matrix A into its lower and upper triangular matrices, L and U,
      such that

      AX = LZ = Y

      and

      Z = UX


3002   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3002 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3003 ordinal=3003 -->
## Functions

Functions

can be an alternate representation of the original system. Notice that Z is also an
n-element vector.

Triangular systems are easy to solve using recursive techniques. Consequently, when
you obtain the L and U matrices from A, you can find Z from the LZ = Y system and X
from the UX = Z system.

When m≠ n, A can be decomposed to an orthogonal matrix Q, and an upper triangular
matrix R, so that A = QR, and the linear system can be represented by QRX = Y. You then
can solve RX = QHY. You can easily solve this triangular system to get X using recursive
techniques.

      Note The numerical implementation of the matrix inversion is numerically
        intensive and, because of its recursive nature, is also highly sensitive to
        round-off error introduced by the floating-point numeric coprocessor.
       Although the computations use the maximum possible accuracy, the VI
       cannot always solve for the system.

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Mathematics\Linear Algebra\Linear
   Algebra Calculator.vi

SolveSolve ComplexComplex LinearLinear EquationsEquations (multiple(multiple rightright hand)hand) VIVI

Solves a linear system AX = Y. The data types you wire to the Input Matrix and Known
Vector inputs determine the polymorphic instance to use.


Inputs/Outputs

   •      Input Matrix —

                                                    © National Instruments 3003

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3003 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3004 ordinal=3004 -->
## Functions

Functions


            Input Matrix must be a nonsingular, square or rectangular, complex matrix. A nonsingular matrix
                is a matrix in which no row or column contains a linear combination of any other row or column,
              respectively. You cannot always determine beforehand whether the matrix is singular, especially
            with large systems.

         When Input Matrix is singular, if the matrix type is General, the VI finds the least-square solution.
            Otherwise, the VI returns an error.

               •     Known Matrix —

         Known Matrix is a matrix of known, dependent-variable values. Known Matrix must have the
          same number of rows as Input Matrix. If the number of rows in Known Matrix and Input Matrix
            are not equal, the VI sets Solution Matrix to an empty matrix and returns an error.

               •      matrix type —

            matrix type is the type of Input Matrix. Knowing the type of Input Matrix can speed up the
           computation of the Solution Matrix and can help you to avoid unnecessary computation, which
            could introduce numerical inaccuracy.

                  General           0
                     (default)
           1      Positive definite
           2     Lower triangular
           3     Upper triangular

               •      Solution Matrix —

            Solution Matrix returns the solution X to AX = Y where A is the Input Matrix and Y is the Known
             Matrix.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       Let A be an m-by-nmatrix that represents the Input Matrix, Y be the set of m
        coefficients in Known Vector, and X be the set of nelements in Solution Vector that
       solves the system


3004   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3004 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3005 ordinal=3005 -->
## Functions

Functions

AX = Y

When m> n, the system has more equations than unknowns, so it is an over-
determined system. The solution that satisfies AX = Y might not exist, so the VI finds the
least-square solution X, which minimizes ||AX – Y||.

When m< n, the system has more unknowns than equations, so it is an under-
determined system. It may have infinite solutions that satisfy AX = Y. The VI finds one of
these solutions.

In the case of m= n, if A is a nonsingular matrix—no row or column is a linear
combination of any other row or column, respectively—then you can solve the system
for X by decomposing the input matrix A into its lower and upper triangular matrices, L
and U, such that

AX = LZ = Y

and

Z = UX

can be an alternate representation of the original system. Notice that Z is also an
n-element vector.

Triangular systems are easy to solve using recursive techniques. Consequently, when
you obtain the L and U matrices from A, you can find Z from the LZ = Y system and X
from the UX = Z system.

In the case of m≠ n, A can be decomposed to an orthogonal matrix Q and an upper
triangular matrix R, so that A = QR. The linear system then can be represented by QRX =
Y. You then can solve RX = QTY.

You can easily solve this triangular system to get x using recursive techniques.

      Note You cannot always determine beforehand whether the matrix is
         singular, especially with large systems. The Solve Linear Equations VI detects
        singular matrices and returns an error, so you do not need to verify whether

                                                    © National Instruments 3005

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3005 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3006 ordinal=3006 -->
## Functions

Functions


            you have a valid system before using this VI.

      The numerical implementation of the matrix inversion is numerically intensive and,
      because of its recursive nature, is also highly sensitive to round-off error introduced by
       the floating-point numeric coprocessor. Although the computations use the maximum
       possible accuracy, the VI cannot always solve the system.

      Solve Complex Linear Equations

       Let A represent the m-by-nInput Matrix, Y represent the set of melements in the
     Known Vector, and X represent the set of nelements in the Solution Vector that solves
        for the system

      AX = Y

     When m> n, the system has more equations than unknowns, so it is an over-
      determined system. Since the solution that satisfies AX = Y may not exist, the VI finds
       the least-square solution X, which minimizes ||AX – Y||.

     When m< n, the system has more unknowns than equations, so it is an under-
      determined system. It might have infinite solutions that satisfy AX = Y. The VI then
        selects one of these solutions.

     When m= n, if A is a nonsingular matrix—no row or column is a linear combination of
      any other row or column, respectively—then you can solve the system for X by
      decomposing the Input Matrix A into its lower and upper triangular matrices, L and U,
      such that

      AX = LZ = Y

      and

      Z = UX

      can be an alternate representation of the original system. Notice that Z is also an
      n-element vector.


3006   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3006 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3007 ordinal=3007 -->
## Functions

Functions

Triangular systems are easy to solve using recursive techniques. Consequently, when
you obtain the L and U matrices from A, you can find Z from the LZ = Y system and X
from the UX = Z system.

When m≠ n, A can be decomposed to an orthogonal matrix Q, and an upper triangular
matrix R, so that A = QR, and the linear system can be represented by QRX = Y. You then
can solve RX = QHY. You can easily solve this triangular system to get X using recursive
techniques.

      Note The numerical implementation of the matrix inversion is numerically
        intensive and, because of its recursive nature, is also highly sensitive to
        round-off error introduced by the floating-point numeric coprocessor.
       Although the computations use the maximum possible accuracy, the VI
       cannot always solve for the system.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Linear Algebra\Linear
   Algebra Calculator.vi

DotDot ProductProduct

Computes the dot product of X Vector and Y Vector. The data types you wire to the X
Vector and Y Vector inputs determine the polymorphic instance to use.


  • Real Dot Product VI
  • Complex Dot Product VI

Let Xrepresent the input sequence X Vector and Yrepresent the input sequence Y
Vector. The VI calculates the dot product X * Y using the following equation.


                                                    © National Instruments 3007

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3007 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3008 ordinal=3008 -->
## Functions

Functions


      where nis the number of data points and yi* is the complex conjugate of yi. Notice
       that the output value X * Y is a scalar value.

      RealReal DotDot ProductProduct VIVI

      Computes the dot product of X Vector and Y Vector. The data types you wire to the X
       Vector and Y Vector inputs determine the polymorphic instance to use.


      Inputs/Outputs

               •     X Vector —

          X Vector is the first input vector. The number of elements in X Vector must be equal to the
          number of elements in Y Vector. If the number of elements in the X Vector is zero or is different
           from the number of elements in Y Vector, the dot product is undefined and is set to NaN.

               •      Y Vector —

           Y Vector is the second input vector. If Y Vector is an empty array, the dot product is NaN.

               •     X * Y —

          X * Y is the dot product.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       Let Xrepresent the input sequence X Vector and Yrepresent the input sequence Y
       Vector. The VI calculates the dot product X * Y using the following equation.


3008   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3008 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3009 ordinal=3009 -->
## Functions

Functions

where nis the number of data points and yi* is the complex conjugate of yi. Notice
that the output value X * Y is a scalar value.

ComplexComplex DotDot ProductProduct VIVI

Computes the dot product of X Vector and Y Vector. The data types you wire to the X
Vector and Y Vector inputs determine the polymorphic instance to use.


Inputs/Outputs

   •     X Vector —

    X Vector is the first input vector. The number of elements in X Vector must be equal to the
   number of elements in Y Vector. If the number of elements in X Vector is zero or is different from
    the number of elements in Y Vector, the dot product is undefined and is set to NaN.

   •      Y Vector —

    Y Vector is the second input vector. If Y Vector is an empty array, the dot product is NaN.

   •     X * Y —

    X * Y is the dot product.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Let Xrepresent the input sequence X Vector and Yrepresent the input sequence Y
Vector. The VI calculates the dot product X * Y using the following equation.


where nis the number of data points and yi* is the complex conjugate of yi. Notice


                                                    © National Instruments 3009

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3009 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3010 ordinal=3010 -->
## Functions

Functions

       that the output value X * Y is a scalar value.

     OuterOuter ProductProduct

      Computes the outer product of X Vector and Y Vector. The data types you wire to the X
       Vector and Y Vector inputs determine the polymorphic instance to use.


            • Real Outer Product VI
            • Complex Outer Product VI

       Let xrepresent the input sequence X Vector and yrepresent the input sequence Y
       Vector. The VI calculates Outer Product using the following equation.


      where arepresents the 2D output sequence Outer Product, nis the number of
      elements in the input sequence X Vector, and mis the number of elements in the
       input sequence Y Vector.

      RealReal OuterOuter ProductProduct VIVI

      Computes the outer product of X Vector and Y Vector. The data types you wire to the X
       Vector and Y Vector inputs determine the polymorphic instance to use.


      Inputs/Outputs

               •     X Vector —

          X Vector is the first input vector.

               •      Y Vector —


3010   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3010 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3011 ordinal=3011 -->
## Functions

Functions


    Y Vector is the second input vector.

   •      Outer Product —

    Outer Product is the outer product. If one of the input sequences is an empty array, Outer
    Product is an empty array.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Let xrepresent the input sequence X Vector and yrepresent the input sequence Y
Vector. The VI calculates Outer Product using the following equation.


where arepresents the 2D output sequence Outer Product, nis the number of
elements in the input sequence X Vector, and mis the number of elements in the
input sequence Y Vector.

ComplexComplex OuterOuter ProductProduct VIVI

Computes the outer product of X Vector and Y Vector. The data types you wire to the X
Vector and Y Vector inputs determine the polymorphic instance to use.


Inputs/Outputs

   •     X Vector —

    X Vector is the first input vector

   •      Y Vector —


                                                    © National Instruments 3011

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3011 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3012 ordinal=3012 -->
## Functions

Functions


           Y Vector is the second input vector.

               •      Outer Product —

           Outer Product is the complex outer product. If one of the input sequences is an empty array, the
           Outer Product is an empty array.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       Let xrepresent the input sequence X Vector and yrepresent the input sequence Y
       Vector. The VI calculates Outer Product using the following equation.


      where arepresents the 2D output sequence Outer Product, nis the number of
      elements in the input sequence X Vector, and mis the number of elements in the
       input sequence Y Vector.

     AA xx BB

      Performs the multiplication of two input matrices or an input matrix and an input
        vector. The data types you wire to the A and B inputs determine the polymorphic
       instance to use.

      (FPGA Module) To multiply a matrix by a vector on an FPGA, use the Matrix*Vector
       Express VI.


            • Real A x B VI
            • Complex A x B VI
            • A x Vector VI
            • Complex A x Vector VI

3012   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3012 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3013 ordinal=3013 -->
## Functions

Functions

  • Vector x A VI
  • Complex Vector x A VI

If A is an n-by-kmatrix and B is a k-by-mmatrix, the matrix multiplication of A and B,
C = AB, results in a matrix, C, whose dimensions are n-by-m. Let A represent the 2D
input array A, B represent the 2D input array B, and C represent the 2D output array A x
B. The VI calculates the elements of C using the following equation.


where nis the number of rows in A, kis the number of columns in A and the number of
rows in B, and mis the number of columns in B.

      Note The A x B VI performs a strict matrix multiplication and not an element-
       by-element 2D multiplication. To perform an element-by-element
        multiplication, you must use the Multiply function. In general, AB ≠ BA.

A x Vector

If A is an n-by-kmatrix, and X is a vector with kelements, the multiplication of A and X,
Y = AX, results in a vector Y with nelements. The VI calculates the elements of Y using
the following equation.


where Y is the output A x Vector, A is the input matrix A, X is the input Vector, nis the
number of rows in A, and kis the number of columns in A and the number of elements
in Vector.

Vector x A

If X′ is a row vector with nelements and A is an n-by-kmatrix, the multiplication of X′
and A, Y = X′A, results in a row vector Y′ with kelements. The VI calculates the elements
of Y′ using the following equations.

                                                    © National Instruments 3013

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3013 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3014 ordinal=3014 -->
## Functions

Functions


      and

       X'=[x0 x1 … xn–1] Y'=[y0 y1 … yk–1]

      where Y′ is the output V′ x A, X′ is the input Vector V′, A is the input matrix A, nis the
      number of elements in Vector V′ and the number of rows in A, and kis the number of
      columns in A.

      RealReal AA xx BB VIVI

      Performs the multiplication of two input matrices or an input matrix and an input
        vector. The data types you wire to the A and B inputs determine the polymorphic
       instance to use.

      (FPGA Module) To multiply a matrix by a vector on an FPGA, use the Matrix*Vector
       Express VI.


      Inputs/Outputs

               •     A —

          A is the first matrix. The number of columns in A must match the number of rows in B and must
          be greater than zero: k>0. If the number of columns in A does not match the number of rows in B,
            the VI sets A x B to an empty array and returns an error.

               •     B —

         B is the second matrix. If the number of rows in B does not match the number of columns in A,
            the VI sets A x B to an empty array and returns an error.

               •     A x B —

          A x B is the matrix containing the result of the matrix multiplication A x B.


3014   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3014 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3015 ordinal=3015 -->
## Functions

Functions

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If A is an n-by-kmatrix and B is a k-by-mmatrix, the matrix multiplication of A and B,
C = AB, results in a matrix, C, whose dimensions are n-by-m. Let A represent the 2D
input array A, B represent the 2D input array B, and C represent the 2D output array A x
B. The VI calculates the elements of C using the following equation.


where nis the number of rows in A, kis the number of columns in A and the number of
rows in B, and mis the number of columns in B.

      Note The A x B VI performs a strict matrix multiplication and not an element-
       by-element 2D multiplication. To perform an element-by-element
        multiplication, you must use the Multiply function. In general, AB ≠ BA.

A x Vector

If A is an n-by-kmatrix, and X is a vector with kelements, the multiplication of A and X,
Y = AX, results in a vector Y with nelements. The VI calculates the elements of Y using
the following equation.


where Y is the output A x Vector, A is the input matrix A, X is the input Vector, nis the
number of rows in A, and kis the number of columns in A and the number of elements
in Vector.

Vector x A

If X′ is a row vector with nelements and A is an n-by-kmatrix, the multiplication of X′

                                                    © National Instruments 3015

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3015 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3016 ordinal=3016 -->
## Functions

Functions

      and A, Y = X′A, results in a row vector Y′ with kelements. The VI calculates the elements
       of Y′ using the following equations.


      and

       X'=[x0 x1 … xn–1] Y'=[y0 y1 … yk–1]

      where Y′ is the output V′ x A, X′ is the input Vector V′, A is the input matrix A, nis the
      number of elements in Vector V′ and the number of rows in A, and kis the number of
      columns in A.

     ComplexComplex AA xx BB VIVI

      Performs the multiplication of two input matrices or an input matrix and an input
        vector. The data types you wire to the A and B inputs determine the polymorphic
       instance to use.

      (FPGA Module) To multiply a matrix by a vector on an FPGA, use the Matrix*Vector
       Express VI.


      Inputs/Outputs

               •     A —

          A is the first matrix. The number of columns in A must match the number of rows in B and must
          be greater than zero. If the number of columns in A does not match the number of rows in B, the
              VI sets A x B to an empty array and returns an error.

               •     B —

         B is the second matrix. If the number of rows in B does not match the number of columns in A,
            the VI sets A x B to an empty array and returns an error.


3016   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3016 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3017 ordinal=3017 -->
## Functions

Functions

   •     A x B —

   A x B is the matrix containing the result of the matrix multiplication A x B.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If A is an n-by-kmatrix and B is a k-by-mmatrix, the matrix multiplication of A and B,
C = AB, results in a matrix, C, whose dimensions are n-by-m. Let A represent the 2D
input array A, B represent the 2D input array B, and C represent the 2D output array A x
B. The VI calculates the elements of C using the following equation.


where nis the number of rows in A, kis the number of columns in A and the number of
rows in B, and mis the number of columns in B.

      Note The A x B VI performs a strict matrix multiplication and not an element-
       by-element 2D multiplication. To perform an element-by-element
        multiplication, you must use the Multiply function. In general, AB ≠ BA.

A x Vector

If A is an n-by-kmatrix, and X is a vector with kelements, the multiplication of A and X,
Y = AX, results in a vector Y with nelements. The VI calculates the elements of Y using
the following equation.


where Y is the output A x Vector, A is the input matrix A, X is the input Vector, nis the
number of rows in A, and kis the number of columns in A and the number of elements
in Vector.


                                                    © National Instruments 3017

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3017 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3018 ordinal=3018 -->
## Functions

Functions

      Vector x A

           If X′ is a row vector with nelements and A is an n-by-kmatrix, the multiplication of X′
      and A, Y = X′A, results in a row vector Y′ with kelements. The VI calculates the elements
       of Y′ using the following equations.


      and

       X'=[x0 x1 … xn–1] Y'=[y0 y1 … yk–1]

      where Y′ is the output V′ x A, X′ is the input Vector V′, A is the input matrix A, nis the
      number of elements in Vector V′ and the number of rows in A, and kis the number of
      columns in A.

     AA xx VectorVector VIVI

      Performs the multiplication of two input matrices or an input matrix and an input
        vector. The data types you wire to the A and B inputs determine the polymorphic
       instance to use.

      (FPGA Module) To multiply a matrix by a vector on an FPGA, use the Matrix*Vector
       Express VI.


      Inputs/Outputs

               •     A —

          A is the input matrix. The number of columns in A must match the number of elements in Vector
          and must be greater than zero. If the number of columns in A does not match the number of
           elements in Vector, the VI sets A x Vector to an empty array and returns an error.

               •      Vector —


3018   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3018 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3019 ordinal=3019 -->
## Functions

Functions


    Vector is the input vector.

   •     A x Vector —

   A x Vector is the output vector containing the result of A multiplied by Vector.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If A is an n-by-kmatrix and B is a k-by-mmatrix, the matrix multiplication of A and B,
C = AB, results in a matrix, C, whose dimensions are n-by-m. Let A represent the 2D
input array A, B represent the 2D input array B, and C represent the 2D output array A x
B. The VI calculates the elements of C using the following equation.


where nis the number of rows in A, kis the number of columns in A and the number of
rows in B, and mis the number of columns in B.

      Note The A x B VI performs a strict matrix multiplication and not an element-
       by-element 2D multiplication. To perform an element-by-element
        multiplication, you must use the Multiply function. In general, AB ≠ BA.

A x Vector

If A is an n-by-kmatrix, and X is a vector with kelements, the multiplication of A and X,
Y = AX, results in a vector Y with nelements. The VI calculates the elements of Y using
the following equation.


where Y is the output A x Vector, A is the input matrix A, X is the input Vector, nis the


                                                    © National Instruments 3019

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3019 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3020 ordinal=3020 -->
## Functions

Functions

      number of rows in A, and kis the number of columns in A and the number of elements
        in Vector.

      Vector x A

           If X′ is a row vector with nelements and A is an n-by-kmatrix, the multiplication of X′
      and A, Y = X′A, results in a row vector Y′ with kelements. The VI calculates the elements
       of Y′ using the following equations.


      and

       X'=[x0 x1 … xn–1] Y'=[y0 y1 … yk–1]

      where Y′ is the output V′ x A, X′ is the input Vector V′, A is the input matrix A, nis the
      number of elements in Vector V′ and the number of rows in A, and kis the number of
      columns in A.

     ComplexComplex AA xx VectorVector VIVI

      Performs the multiplication of two input matrices or an input matrix and an input
        vector. The data types you wire to the A and B inputs determine the polymorphic
       instance to use.

      (FPGA Module) To multiply a matrix by a vector on an FPGA, use the Matrix*Vector
       Express VI.


      Inputs/Outputs

               •     A —

          A is the input matrix. The number of columns in A must match the number of elements in Vector


3020   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3020 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3021 ordinal=3021 -->
## Functions

Functions


    and must be greater than zero. If the number of columns in A does not match the number of
    elements in Vector, the VI sets A x Vector to an empty array and returns an error.

   •      Vector —

    Vector is the input vector.

   •     A x Vector —

   A x Vector is the output vector containing the result of A multiplied by Vector.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If A is an n-by-kmatrix and B is a k-by-mmatrix, the matrix multiplication of A and B,
C = AB, results in a matrix, C, whose dimensions are n-by-m. Let A represent the 2D
input array A, B represent the 2D input array B, and C represent the 2D output array A x
B. The VI calculates the elements of C using the following equation.


where nis the number of rows in A, kis the number of columns in A and the number of
rows in B, and mis the number of columns in B.

      Note The A x B VI performs a strict matrix multiplication and not an element-
       by-element 2D multiplication. To perform an element-by-element
        multiplication, you must use the Multiply function. In general, AB ≠ BA.

A x Vector

If A is an n-by-kmatrix, and X is a vector with kelements, the multiplication of A and X,
Y = AX, results in a vector Y with nelements. The VI calculates the elements of Y using
the following equation.


                                                    © National Instruments 3021

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3021 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3022 ordinal=3022 -->
## Functions

Functions


      where Y is the output A x Vector, A is the input matrix A, X is the input Vector, nis the
      number of rows in A, and kis the number of columns in A and the number of elements
        in Vector.

      Vector x A

           If X′ is a row vector with nelements and A is an n-by-kmatrix, the multiplication of X′
      and A, Y = X′A, results in a row vector Y′ with kelements. The VI calculates the elements
       of Y′ using the following equations.


      and

       X'=[x0 x1 … xn–1] Y'=[y0 y1 … yk–1]

      where Y′ is the output V′ x A, X′ is the input Vector V′, A is the input matrix A, nis the
      number of elements in Vector V′ and the number of rows in A, and kis the number of
      columns in A.

      VectorVector xx AA VIVI

      Performs the multiplication of two input matrices or an input matrix and an input
        vector. The data types you wire to the A and B inputs determine the polymorphic
       instance to use.

      (FPGA Module) To multiply a matrix by a vector on an FPGA, use the Matrix*Vector
       Express VI.


3022   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3022 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3023 ordinal=3023 -->
## Functions

Functions

Inputs/Outputs

   •      Vector V' —

    Vector V' is the input vector.

   •      Matrix A —

    Matrix A is the input matrix. The number of rows in Matrix A must match the number of elements
     in Vector V' and must be greater than zero.

       If the number of rows in Matrix A does not match the number of elements in Vector V', the VI sets
     V' x A to an empty array and returns an error.

   •       V' x A —

     V' x A is the output vector containing the result of Vector V' multiplied by Matrix A.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If A is an n-by-kmatrix and B is a k-by-mmatrix, the matrix multiplication of A and B,
C = AB, results in a matrix, C, whose dimensions are n-by-m. Let A represent the 2D
input array A, B represent the 2D input array B, and C represent the 2D output array A x
B. The VI calculates the elements of C using the following equation.


where nis the number of rows in A, kis the number of columns in A and the number of
rows in B, and mis the number of columns in B.

      Note The A x B VI performs a strict matrix multiplication and not an element-
       by-element 2D multiplication. To perform an element-by-element
        multiplication, you must use the Multiply function. In general, AB ≠ BA.


                                                    © National Instruments 3023

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3023 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3024 ordinal=3024 -->
## Functions

Functions

     A x Vector

           If A is an n-by-kmatrix, and X is a vector with kelements, the multiplication of A and X,
      Y = AX, results in a vector Y with nelements. The VI calculates the elements of Y using
       the following equation.


      where Y is the output A x Vector, A is the input matrix A, X is the input Vector, nis the
      number of rows in A, and kis the number of columns in A and the number of elements
        in Vector.

      Vector x A

           If X′ is a row vector with nelements and A is an n-by-kmatrix, the multiplication of X′
      and A, Y = X′A, results in a row vector Y′ with kelements. The VI calculates the elements
       of Y′ using the following equations.


      and

       X'=[x0 x1 … xn–1] Y'=[y0 y1 … yk–1]

      where Y′ is the output V′ x A, X′ is the input Vector V′, A is the input matrix A, nis the
      number of elements in Vector V′ and the number of rows in A, and kis the number of
      columns in A.

     ComplexComplex VectorVector xx AA VIVI

      Performs the multiplication of two input matrices or an input matrix and an input
        vector. The data types you wire to the A and B inputs determine the polymorphic
       instance to use.

      (FPGA Module) To multiply a matrix by a vector on an FPGA, use the Matrix*Vector

3024   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3024 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3025 ordinal=3025 -->
## Functions

Functions

Express VI.


Inputs/Outputs

   •      Vector V' —

    Vector V' is the input vector.

   •      Matrix A —

    Matrix A is the input matrix. The number of rows in Matrix A must match the number of elements
     in Vector V' and must be greater than zero.

       If the number of rows in Matrix A does not match the number of elements in Vector V', the VI sets
     V' x A to an empty array and returns an error.

   •       V' x A —

     V' x A is the output vector containing the result of Vector V' multiplied by Matrix A.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If A is an n-by-kmatrix and B is a k-by-mmatrix, the matrix multiplication of A and B,
C = AB, results in a matrix, C, whose dimensions are n-by-m. Let A represent the 2D
input array A, B represent the 2D input array B, and C represent the 2D output array A x
B. The VI calculates the elements of C using the following equation.


where nis the number of rows in A, kis the number of columns in A and the number of
rows in B, and mis the number of columns in B.


                                                    © National Instruments 3025

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3025 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3026 ordinal=3026 -->
## Functions

Functions

           Note The A x B VI performs a strict matrix multiplication and not an element-
             by-element 2D multiplication. To perform an element-by-element
                multiplication, you must use the Multiply function. In general, AB ≠ BA.

     A x Vector

           If A is an n-by-kmatrix, and X is a vector with kelements, the multiplication of A and X,
      Y = AX, results in a vector Y with nelements. The VI calculates the elements of Y using
       the following equation.


      where Y is the output A x Vector, A is the input matrix A, X is the input Vector, nis the
      number of rows in A, and kis the number of columns in A and the number of elements
        in Vector.

      Vector x A

           If X′ is a row vector with nelements and A is an n-by-kmatrix, the multiplication of X′
      and A, Y = X′A, results in a row vector Y′ with kelements. The VI calculates the elements
       of Y′ using the following equations.


      and

       X'=[x0 x1 … xn–1] Y'=[y0 y1 … yk–1]

      where Y′ is the output V′ x A, X′ is the input Vector V′, A is the input matrix A, nis the
      number of elements in Vector V′ and the number of rows in A, and kis the number of
      columns in A.


3026   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3026 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3027 ordinal=3027 -->
## Functions

Functions

KroneckerKronecker ProductProduct

Calculates the Kronecker product of the input matrices A and B. The data types you
wire to the A and B inputs determine the polymorphic instance to use.


  • Real Kronecker Product VI
  • Complex Kronecker Product VI

If A is an n-by-mmatrix and B is a k-by-lmatrix, the Kronecker product of A and B


results in a matrix C, with dimensions nk-by-ml. The VI calculates the Kronecker
product using the following equation:


For example, if


                 then

RealReal KroneckerKronecker ProductProduct VIVI

Calculates the Kronecker product of the input matrices A and B. The data types you
wire to the A and B inputs determine the polymorphic instance to use.


                                                    © National Instruments 3027

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3027 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3028 ordinal=3028 -->
## Functions

Functions

      Inputs/Outputs

               •     A —

          A is the first input real matrix for computing the Kronecker product.

               •     B —

         B is the second input real matrix for computing the Kronecker product.

               •      Kronecker Product —

           Kronecker Product is the matrix that contains the resulting Kronecker product of matrices A and
             B. The number of rows in Kronecker Product is the product of the number of rows in A and B.
          The number of columns in Kronecker Product is the product of the number of columns in A and
             B.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


           If A is an n-by-mmatrix and B is a k-by-lmatrix, the Kronecker product of A and B


        results in a matrix C, with dimensions nk-by-ml. The VI calculates the Kronecker
      product using the following equation:


       For example, if


                       then


3028   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3028 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3029 ordinal=3029 -->
## Functions

Functions

ComplexComplex KroneckerKronecker ProductProduct VIVI

Calculates the Kronecker product of the input matrices A and B. The data types you
wire to the A and B inputs determine the polymorphic instance to use.


Inputs/Outputs

   •     A —

   A is the first input complex matrix for computing the Kronecker product.

   •     B —

   B is the second input complex matrix for computing the Kronecker product.

   •      Kronecker Product —

    Kronecker Product is the matrix that contains the resulting Kronecker product of matrices A and
     B. The number of rows in Kronecker Product is the product of the number of rows in A and B.
    The number of columns in Kronecker Product is the product of the number of columns in A and
     B.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If A is an n-by-mmatrix and B is a k-by-lmatrix, the Kronecker product of A and B


results in a matrix C, with dimensions nk-by-ml. The VI calculates the Kronecker
product using the following equation:


                                                    © National Instruments 3029

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3029 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3030 ordinal=3030 -->
## Functions

Functions


       For example, if


                       then

     SubspacesSubspaces AngleAngle

      Computes the angle between column spaces of two matrices.

       Wire data to the A and B inputs to determine the polymorphic instance to use or
      manually select the instance.


            • Subspaces Angle (1D) VI
            • Subspaces Angle (2D 1D) VI
            • Subspaces Angle (2D) VI

       Let U1S1V1T and U2S2V2T be the singular value decomposition of A and B,
        respectively. The following equation defines the angle between the Euclidean
      subspaces that span columns of A and B.

     angle= arccos(s)

      where sis the minimum singular value of U1TU2

           If A and B are both vectors, the previous equation equals the following equation.


3030   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3030 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3031 ordinal=3031 -->
## Functions

Functions

where the norm symbols (||.||) compute the 2-norm of the input vectors.

SubspacesSubspaces AngleAngle (1D)(1D) VIVI

Computes the angle between column spaces of two matrices.

Wire data to the A and B inputs to determine the polymorphic instance to use or
manually select the instance.


Inputs/Outputs

   •     A —

    A is a real vector.

   •     B —

   B is a real vector. The length of B must equal the length of A.

   •      angle —

    angle returns the angle (in radians) between the column subspaces of A and B.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

Let U1S1V1T and U2S2V2T be the singular value decomposition of A and B,
respectively. The following equation defines the angle between the Euclidean
subspaces that span columns of A and B.

angle= arccos(s)

where sis the minimum singular value of U1TU2


                                                    © National Instruments 3031

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3031 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3032 ordinal=3032 -->
## Functions

Functions

           If A and B are both vectors, the previous equation equals the following equation.


      where the norm symbols (||.||) compute the 2-norm of the input vectors.

      SubspacesSubspaces AngleAngle (2D(2D 1D)1D) VIVI

      Computes the angle between column spaces of two matrices.

       Wire data to the A and B inputs to determine the polymorphic instance to use or
      manually select the instance.


      Inputs/Outputs

               •     A —

          A is a real matrix.

               •     B —

         B is a real vector. The length of B must equal the number of rows in A.

               •      angle —

            angle returns the angle (in radians) between the column subspaces of A and B.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

       Let U1S1V1T and U2S2V2T be the singular value decomposition of A and B,
        respectively. The following equation defines the angle between the Euclidean
      subspaces that span columns of A and B.

3032   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3032 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3033 ordinal=3033 -->
## Functions

Functions

angle= arccos(s)

where sis the minimum singular value of U1TU2

If A and B are both vectors, the previous equation equals the following equation.


where the norm symbols (||.||) compute the 2-norm of the input vectors.

SubspacesSubspaces AngleAngle (2D)(2D) VIVI

Computes the angle between column spaces of two matrices.

Wire data to the A and B inputs to determine the polymorphic instance to use or
manually select the instance.


Inputs/Outputs

   •     A —

    A is a real matrix.

   •     B —

   B is a real matrix. The number of rows in B must equal the number of rows in A.

   •      angle —

    angle returns the angle (in radians) between the Euclidean subspaces specified in columns of A
    and B.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error


                                                    © National Instruments 3033

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3033 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3034 ordinal=3034 -->
## Functions

Functions


          Code VI to convert the error code or warning into an error cluster.

       Let U1S1V1T and U2S2V2T be the singular value decomposition of A and B,
        respectively. The following equation defines the angle between the Euclidean
      subspaces that span columns of A and B.

     angle= arccos(s)

      where sis the minimum singular value of U1TU2

           If A and B are both vectors, the previous equation equals the following equation.


      where the norm symbols (||.||) compute the 2-norm of the input vectors.

     DeterminantDeterminant

      Computes the determinant of Input Matrix. Wire data to the Input Matrix input to
      determine the polymorphic instance to use or manually select the instance.


            • Real Determinant VI
            • Complex Determinant VI

       Let Abe a square matrix that represents the Input Matrix, and let Land Urepresent
       the lower and upper triangular matrices, respectively, of Asuch that

   A= LU

      where the main diagonal elements of the lower triangular matrix Lare arbitrarily set to
       one. The VI finds the determinant of Aby the product of the main diagonal elements

3034   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3034 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3035 ordinal=3035 -->
## Functions

Functions

of the upper triangular matrix U


where |A| is the determinant of Xand nis the dimension of X.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Linear Algebra\Linear
   Algebra Calculator.vi

RealReal DeterminantDeterminant VIVI

Computes the determinant of Input Matrix. Wire data to the Input Matrix input to
determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •      Input Matrix —

    Input Matrix must be a square real matrix.

   •      matrix type —

    matrix type is the type of Input Matrix. Knowing the type of Input Matrix can speed up the
    computation of the determinant and can help you to avoid unnecessary computation, which
    could introduce numerical inaccuracy.

          General
    0
            (default)
    1      Positive definite
    2     Lower triangular


                                                    © National Instruments 3035

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3035 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3036 ordinal=3036 -->
## Functions

Functions


           3     Upper triangular

               •      determinant —

           determinant is a scalar value.

               Note The determinant of a singular matrix is zero. This is a valid result and is not an
                         error, that is, |A|=0.0 if A is singular.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       Let Abe a square matrix that represents the Input Matrix, and let Land Urepresent
       the lower and upper triangular matrices, respectively, of Asuch that

   A= LU

      where the main diagonal elements of the lower triangular matrix Lare arbitrarily set to
       one. The VI finds the determinant of Aby the product of the main diagonal elements
       of the upper triangular matrix U


      where |A| is the determinant of Xand nis the dimension of X.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Linear Algebra\Linear
        Algebra Calculator.vi


3036   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3036 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3037 ordinal=3037 -->
## Functions

Functions

ComplexComplex DeterminantDeterminant VIVI

Computes the determinant of Input Matrix. Wire data to the Input Matrix input to
determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •      Input Matrix —

    Input Matrix must be a square complex matrix.

   •      matrix type —

    matrix type is the type of Input Matrix. Knowing the type of Input Matrix can speed up the
    computation of the determinant and can help you to avoid unnecessary computation, which
    could introduce numerical inaccuracy.

          General
    0            (default)
    1      Positive definite
    2     Lower triangular
    3     Upper triangular

   •      determinant —

    determinant is a scalar value. The determinant of a singular matrix is zero. This is a valid result
    and is not an error, that is, |A| = 0.0 if A is singular.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Let Abe a square matrix that represents the Input Matrix, and let Land Urepresent
the lower and upper triangular matrices, respectively, of Asuch that


                                                    © National Instruments 3037

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3037 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3038 ordinal=3038 -->
## Functions

Functions

   A= LU

      where the main diagonal elements of the lower triangular matrix Lare arbitrarily set to
       one. The VI finds the determinant of Aby the product of the main diagonal elements
       of the upper triangular matrix U


      where |A| is the determinant of Xand nis the dimension of X.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Linear Algebra\Linear
        Algebra Calculator.vi

      VectorVector NormNorm

      Computes the norm of Input Vector. Wire data to the Input Vector input to determine
       the polymorphic instance to use or manually select the instance.

           Note You can use the Matrix Norm VI to calculate the matrix norm.


            • Real Vector Norm VI
            • Complex Vector Norm VI

       This VI calculates norm using the following equations.

        1-norm                           ||X|| = |x0| + |x1| + … + |xn– 1|
        2-norm                           ||X|| = √(|x0|² + |x1|² + … + |xn– 1|²)

3038   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3038 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3039 ordinal=3039 -->
## Functions

Functions

 Inf-norm                         ||X|| = maxi(|xi|)
 –Inf-norm                        ||X|| = mini(|xi|)
 User Defined                    ||X|| = ||x0|y + |x1|y + … + |xn– 1|y|1/y

where Xis Input Vector, yis user defined norm, and ||X|| is norm.

RealReal VectorVector NormNorm VIVI

Computes the norm of Input Vector. Wire data to the Input Vector input to determine
the polymorphic instance to use or manually select the instance.

      Note You can use the Matrix Norm VI to calculate the matrix norm.


Inputs/Outputs

   •      Input Vector —

    Input Vector is the real input vector. If Input Vector is an empty array, this VI sets norm to NaN.

   •     norm type —

   norm type indicates what type of norm you use to compute the norm. The default is 2-norm. If
   norm type is User Defined, this VI uses user defined norm as the norm type.

    1     1-norm
    2     2-norm (default)
    3     Inf-norm
    4     –Inf-norm
    5     User Defined

   •      user defined norm —


                                                    © National Instruments 3039

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3039 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3040 ordinal=3040 -->
## Functions

Functions


            user defined norm is the user defined norm type. The default is –1. This VI uses user defined
         norm as the norm type only if you set norm type to User Defined.

            user defined norm must be nonzero.

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

     ComplexComplex VectorVector NormNorm VIVI

      Computes the norm of Input Vector. Wire data to the Input Vector input to determine
       the polymorphic instance to use or manually select the instance.

           Note You can use the Matrix Norm VI to calculate the matrix norm.


3040   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3040 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3041 ordinal=3041 -->
## Functions

Functions


Inputs/Outputs

   •      Input Vector —

    Input Vector is the complex input vector. If Input Vector is an empty array, this VI sets norm to
    NaN.

   •     norm type —

   norm type indicates what type of norm you use to compute the norm. The default is 2-norm. If
   norm type is User Defined, this VI uses user defined norm as the norm type.

   •      user defined norm —

    user defined norm is the user defined norm type. The default is –1. This VI uses user defined
   norm as the norm type only if you set norm type to User Defined.

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


                                                    © National Instruments 3041

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3041 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3042 ordinal=3042 -->
## Functions

Functions

      where Xis Input Vector, yis user defined norm, and ||X|| is norm.

      MatrixMatrix NormNorm

      Computes the norm of Input Matrix. Wire data to the Input Matrix input to determine
       the polymorphic instance to use or manually select the instance.

           Note You can use the Vector Norm VI or the Unit Vector VI to calculate the
               vector norm.


            • Real Matrix Norm VI
            • Complex Matrix Norm VI

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Linear Algebra\Linear
        Algebra Calculator.vi
            • labview\examples\Mathematics\Linear Algebra\Matrix to a
        Power.vi

      RealReal MatrixMatrix NormNorm VIVI

      Computes the norm of Input Matrix. Wire data to the Input Matrix input to determine
       the polymorphic instance to use or manually select the instance.

           Note You can use the Vector Norm VI or the Unit Vector VI to calculate the
               vector norm.


3042   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3042 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3043 ordinal=3043 -->
## Functions

Functions

Inputs/Outputs

   •      Input Matrix —

    Input Matrix can be a square or rectangular, real matrix.

   •     norm type —

   norm type indicates what type of norm is used to compute the norm.

    0 2-norm—||A||2 is the largest singular value of the Input Matrix.
    1 1-norm—||A||1 is the largest absolute column sum of the Input Matrix.
      F-norm—||A||f is equal to            where diag(ATA) means the diagonal elements of
    2
      matrix ATA and AT is the transpose of A.
    3 inf-norm—||A||∞ is the largest absolute row sum of the Input Matrix.

   •     norm —

   norm is a scalar that gives some measure of the magnitude of the elements in the matrix.

    Let A represent the Input Matrix, the norm of A is represented by ||A||p, where p can be 1, 2, F, or
     infinity, indicating different types of norms that are computed.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Linear Algebra\Linear
   Algebra Calculator.vi
  • labview\examples\Mathematics\Linear Algebra\Matrix to a
   Power.vi


                                                    © National Instruments 3043

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3043 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3044 ordinal=3044 -->
## Functions

Functions

     ComplexComplex MatrixMatrix NormNorm VIVI

      Computes the norm of Input Matrix. Wire data to the Input Matrix input to determine
       the polymorphic instance to use or manually select the instance.

           Note You can use the Vector Norm VI or the Unit Vector VI to calculate the
               vector norm.


      Inputs/Outputs

               •      Input Matrix —

            Input Matrix can be a square or rectangular, complex matrix.

               •     norm type —

         norm type indicates what type of norm is used to compute the norm.

               •     norm —

         norm is a scalar that gives some measure of the magnitude of the elements in the matrix.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Linear Algebra\Linear
        Algebra Calculator.vi
            • labview\examples\Mathematics\Linear Algebra\Matrix to a
        Power.vi


3044   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3044 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3045 ordinal=3045 -->
## Functions

Functions

MatrixMatrix RankRank

Computes the rank of Input Matrix. Wire data to the Input Matrix input to determine
the polymorphic instance to use or manually select the instance.


  • Real Matrix Rank VI
  • Complex Matrix Rank VI

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Linear Algebra\Linear
   Algebra Calculator.vi

RealReal MatrixMatrix RankRank VIVI

Computes the rank of Input Matrix. Wire data to the Input Matrix input to determine
the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •      Input Matrix —

    Input Matrix must be a real matrix.

   •      tolerance —

    tolerance defines a level such that the number of singular values greater than this level is the
    rank of Input Matrix. The default is –1.

   •      rank —


                                                    © National Instruments 3045

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3045 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3046 ordinal=3046 -->
## Functions

Functions


           rank is the number of singular values in the Input Matrix that are larger than the tolerance. rank
                is the maximum number of independent rows or columns in the Input Matrix.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Linear Algebra\Linear
        Algebra Calculator.vi

     ComplexComplex MatrixMatrix RankRank VIVI

      Computes the rank of Input Matrix. Wire data to the Input Matrix input to determine
       the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •      Input Matrix —

            Input Matrix is a complex matrix.

               •      tolerance —

            tolerance defines a level such that the number of singular values greater than this level is the
            rank of Input Matrix. The default is –1.

               •      rank —

           rank is the number of singular values in the Input Matrix that are larger than the tolerance. rank
                is the maximum number of independent rows or columns in the Input Matrix.

               •       error —

3046   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3046 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3047 ordinal=3047 -->
## Functions

Functions


    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Linear Algebra\Linear
   Algebra Calculator.vi

TraceTrace

Finds the trace of Input Matrix. Wire data to the Input Matrix input to determine the
polymorphic instance to use or manually select the instance.


  • Real Matrix Trace VI
  • Complex Matrix Trace VI

The VI uses the following equation to compute the trace.


where Ais Input Matrix, tr(A) is trace, and mand nare the number of rows and the
number of columns of Input Matrix, respectively.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Linear Algebra\Linear
   Algebra Calculator.vi


                                                    © National Instruments 3047

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3047 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3048 ordinal=3048 -->
## Functions

Functions

      RealReal MatrixMatrix TraceTrace VIVI

       Finds the trace of Input Matrix. Wire data to the Input Matrix input to determine the
      polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •      Input Matrix —

            Input Matrix is a square or rectangular matrix. If Input Matrix is an empty matrix, this VI sets
             trace to NaN and returns an error.

               •       trace —

             trace is the sum of the main diagonal of Input Matrix.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The VI uses the following equation to compute the trace.


      where Ais Input Matrix, tr(A) is trace, and mand nare the number of rows and the
      number of columns of Input Matrix, respectively.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Linear Algebra\Linear
        Algebra Calculator.vi


3048   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3048 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3049 ordinal=3049 -->
## Functions

Functions

ComplexComplex MatrixMatrix TraceTrace VIVI

Finds the trace of Input Matrix. Wire data to the Input Matrix input to determine the
polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •      Input Matrix —

    Input Matrix is a square or rectangular matrix. If Input Matrix is an empty matrix, this VI sets
    trace to NaN and returns an error.

   •       trace —

    trace is the sum of the main diagonal of Input Matrix.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The VI uses the following equation to compute the trace.


where Ais Input Matrix, tr(A) is trace, and mand nare the number of rows and the
number of columns of Input Matrix, respectively.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Linear Algebra\Linear
   Algebra Calculator.vi


                                                    © National Instruments 3049

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3049 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3050 ordinal=3050 -->
## Functions

Functions

      TestTest MatrixMatrix TypeType

       Tests whether Input Matrix is a matrix of special type. Wire data to the Input Matrix
       input to determine the polymorphic instance to use or manually select the instance.


            • Test Real Matrix Type VI
            • Test Complex Matrix Type VI

      Positive Definite and Positive Semi-Definite

        In real cases, a symmetric matrix Ais positive definite if


        for any non-zero vector x. A symmetric matrix Ais positive semi-definite if


        for any non-zero vector x. In complex cases, a Hermitian matrix Ais positive definite if


        for any non-zero vector x. A Hermitian matrix Ais positive semi-definite if


        for any non-zero vector x.

       This VI first tests whether Input Matrix is symmetric (or Hermitian). If the test fails, is
      type? returns FALSE. Then, this VI tests whether the symmetric (or Hermitian) matrix is
       positive definite (or positive semi-definite) by Cholesky factorization. If a symmetric
       matrix is not positive definite (or positive semi-definite), the algorithm for Cholesky
        factorization fails when it attempts to calculate the square root of a negative number
       or divide by zero.

3050   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3050 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3051 ordinal=3051 -->
## Functions

Functions

This VI uses relative tolerance to determine whether a number is small enough that
you consider it as zero when performing Cholesky factorization. If relative tolerance is
less than zero, the tolerance in Cholesky factorization is

2.22e–16*n*maxdiag

where nis the order of Input Matrix and maxdiagis the maximum value of diagonal
elements of Input Matrix. Otherwise, the tolerance is

relative tolerance*n*maxdiag
Symmetric and Hermitian

A real or complex square matrix is symmetric if

aij = aji

A complex square matrix is Hermitian if

aij = conj(aji)

where conj is the complex conjugate function.

      Note Both instances of the VI include Symmetric and Hermitian values
         for matrix type.

This VI uses relative tolerance to determine whether the difference between two
elements in Input Matrix is small enough to consider them equal. If relative tolerance
is less than zero, the tolerance is

2.22e–16*n*max

where nis the order of Input Matrix and maxis the maximum absolute value of
elements in Input Matrix. For a complex element, maxis the maximum absolute value
of its real and imaginary parts. Otherwise, the tolerance is


                                                    © National Instruments 3051

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3051 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3052 ordinal=3052 -->
## Functions

Functions

        relative tolerance*n*max
     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Linear Algebra\Linear
        Algebra Calculator.vi

       TestTest RealReal MatrixMatrix TypeType VIVI

       Tests whether Input Matrix is a matrix of special type. Wire data to the Input Matrix
       input to determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •      Input Matrix —

            Input Matrix is the matrix which you want to test for special type.

               •      matrix type —

            matrix type specifies which type you want to test for Input Matrix.

               •       relative tolerance —

             relative tolerance specifies the relative tolerance used to test whether Input Matrix is a matrix of
             special type. The default value is –1. If relative tolerance is less than 0, this VI sets tolerance
           based on Input Matrix.

               •        is type? —

                is type? is TRUE if Input Matrix is a matrix of special type. Otherwise, is type? is FALSE.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error


3052   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3052 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3053 ordinal=3053 -->
## Functions

Functions


    Code VI to convert the error code or warning into an error cluster.


Positive Definite and Positive Semi-Definite

In real cases, a symmetric matrix Ais positive definite if


for any non-zero vector x. A symmetric matrix Ais positive semi-definite if


for any non-zero vector x. In complex cases, a Hermitian matrix Ais positive definite if


for any non-zero vector x. A Hermitian matrix Ais positive semi-definite if


for any non-zero vector x.

This VI first tests whether Input Matrix is symmetric (or Hermitian). If the test fails, is
type? returns FALSE. Then, this VI tests whether the symmetric (or Hermitian) matrix is
positive definite (or positive semi-definite) by Cholesky factorization. If a symmetric
matrix is not positive definite (or positive semi-definite), the algorithm for Cholesky
factorization fails when it attempts to calculate the square root of a negative number
or divide by zero.

This VI uses relative tolerance to determine whether a number is small enough that
you consider it as zero when performing Cholesky factorization. If relative tolerance is
less than zero, the tolerance in Cholesky factorization is

2.22e–16*n*maxdiag

where nis the order of Input Matrix and maxdiagis the maximum value of diagonal

                                                    © National Instruments 3053

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3053 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3054 ordinal=3054 -->
## Functions

Functions

      elements of Input Matrix. Otherwise, the tolerance is

        relative tolerance*n*maxdiag
     Symmetric and Hermitian

      A real or complex square matrix is symmetric if

       aij = aji

      A complex square matrix is Hermitian if

       aij = conj(aji)

      where conj is the complex conjugate function.

           Note Both instances of the VI include Symmetric and Hermitian values
                for matrix type.

       This VI uses relative tolerance to determine whether the difference between two
      elements in Input Matrix is small enough to consider them equal. If relative tolerance
         is less than zero, the tolerance is

      2.22e–16*n*max

      where nis the order of Input Matrix and maxis the maximum absolute value of
      elements in Input Matrix. For a complex element, maxis the maximum absolute value
       of its real and imaginary parts. Otherwise, the tolerance is

        relative tolerance*n*max
     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Linear Algebra\Linear
        Algebra Calculator.vi

3054   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3054 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3055 ordinal=3055 -->
## Functions

Functions

TestTest ComplexComplex MatrixMatrix TypeType VIVI

Tests whether Input Matrix is a matrix of special type. Wire data to the Input Matrix
input to determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •      Input Matrix —

    Input Matrix is the matrix which you want to test for special type.

   •      matrix type —

    matrix type specifies which type you want to test for Input Matrix.

   •       relative tolerance —

     relative tolerance specifies the relative tolerance used to test whether Input Matrix is a matrix of
     special type. The default value is –1. If relative tolerance is less than 0, this VI sets tolerance
    based on Input Matrix.

   •        is type? —

      is type? is TRUE if Input Matrix is a matrix of special type. Otherwise, is type? is FALSE.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Positive Definite and Positive Semi-Definite

In real cases, a symmetric matrix Ais positive definite if


                                                    © National Instruments 3055

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3055 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3056 ordinal=3056 -->
## Functions

Functions

        for any non-zero vector x. A symmetric matrix Ais positive semi-definite if


        for any non-zero vector x. In complex cases, a Hermitian matrix Ais positive definite if


        for any non-zero vector x. A Hermitian matrix Ais positive semi-definite if


        for any non-zero vector x.

       This VI first tests whether Input Matrix is symmetric (or Hermitian). If the test fails, is
      type? returns FALSE. Then, this VI tests whether the symmetric (or Hermitian) matrix is
       positive definite (or positive semi-definite) by Cholesky factorization. If a symmetric
       matrix is not positive definite (or positive semi-definite), the algorithm for Cholesky
        factorization fails when it attempts to calculate the square root of a negative number
       or divide by zero.

       This VI uses relative tolerance to determine whether a number is small enough that
      you consider it as zero when performing Cholesky factorization. If relative tolerance is
        less than zero, the tolerance in Cholesky factorization is

      2.22e–16*n*maxdiag

      where nis the order of Input Matrix and maxdiagis the maximum value of diagonal
      elements of Input Matrix. Otherwise, the tolerance is

        relative tolerance*n*maxdiag
     Symmetric and Hermitian

      A real or complex square matrix is symmetric if

       aij = aji


3056   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3056 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3057 ordinal=3057 -->
## Functions

Functions

A complex square matrix is Hermitian if

aij = conj(aji)

where conj is the complex conjugate function.

      Note Both instances of the VI include Symmetric and Hermitian values
         for matrix type.

This VI uses relative tolerance to determine whether the difference between two
elements in Input Matrix is small enough to consider them equal. If relative tolerance
is less than zero, the tolerance is

2.22e–16*n*max

where nis the order of Input Matrix and maxis the maximum absolute value of
elements in Input Matrix. For a complex element, maxis the maximum absolute value
of its real and imaginary parts. Otherwise, the tolerance is

relative tolerance*n*max
Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Mathematics\Linear Algebra\Linear
   Algebra Calculator.vi

MatrixMatrix ConditionCondition NumberNumber

Computes the condition number of Input Matrix. Wire data to the Input Matrix input
to determine the polymorphic instance to use or manually select the instance.


                                                    © National Instruments 3057

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3057 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3058 ordinal=3058 -->
## Functions

Functions

            • Real Matrix Condition Number VI
            • Complex Matrix Condition Number VI

       condition number defines cas the following equation:

    c= ||A||p||A–1||p

      where ||A||p is the norm of Input Matrix. Different values of pdefine the different types
       of norms, therefore pdefines different types of computations of condition numbers.

       For the 2-norm condition number, cis the ratio of the largest, singular value of Ato the
       smallest, singular value of A.

      The condition number of a matrix measures the sensitivity of a system solution of
        linear equations to errors in the data. It gives an indication of the accuracy of the
        results from a matrix inversion and a linear equation solution.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Linear Algebra\Linear
        Algebra Calculator.vi

      RealReal MatrixMatrix ConditionCondition NumberNumber VIVI

      Computes the condition number of Input Matrix. Wire data to the Input Matrix input
       to determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •      Input Matrix —

            Input Matrix can be a rectangular matrix when norm type is 2-norm. If norm type is not 2-norm,


3058   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3058 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3059 ordinal=3059 -->
## Functions

Functions


    Input Matrix must be a square matrix.

   •     norm type —

   norm type indicates what type of norm is used to compute the condition number.

   •      condition number —

    condition number is the calculated condition number for a given norm. For the 2-norm, the
    condition number is the ratio of the largest singular value of Input Matrix to the smallest
     singular value of Input Matrix.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


condition number defines cas the following equation:

c= ||A||p||A–1||p

where ||A||p is the norm of Input Matrix. Different values of pdefine the different types
of norms, therefore pdefines different types of computations of condition numbers.

For the 2-norm condition number, cis the ratio of the largest, singular value of Ato the
smallest, singular value of A.

The condition number of a matrix measures the sensitivity of a system solution of
linear equations to errors in the data. It gives an indication of the accuracy of the
results from a matrix inversion and a linear equation solution.

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Mathematics\Linear Algebra\Linear
   Algebra Calculator.vi


                                                    © National Instruments 3059

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3059 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3060 ordinal=3060 -->
## Functions

Functions

     ComplexComplex MatrixMatrix ConditionCondition NumberNumber VIVI

      Computes the condition number of Input Matrix. Wire data to the Input Matrix input
       to determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •      Input Matrix —

            Input Matrix can be a rectangular matrix when norm type is 2-norm. If norm type is not 2-norm,
            Input Matrix must be a square matrix.

               •     norm type —

         norm type indicates what type of norm is used to compute the condition number.

               •      condition number —

            condition number is the calculated condition number for a given norm. For the 2-norm, the
            condition number is the ratio of the largest singular value of Input Matrix to the smallest
             singular value of Input Matrix.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       condition number defines cas the following equation:

    c= ||A||p||A–1||p

      where ||A||p is the norm of Input Matrix. Different values of pdefine the different types
       of norms, therefore pdefines different types of computations of condition numbers.

       For the 2-norm condition number, cis the ratio of the largest, singular value of Ato the
       smallest, singular value of A.

3060   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3060 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3061 ordinal=3061 -->
## Functions

Functions

The condition number of a matrix measures the sensitivity of a system solution of
linear equations to errors in the data. It gives an indication of the accuracy of the
results from a matrix inversion and a linear equation solution.

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Mathematics\Linear Algebra\Linear
   Algebra Calculator.vi

InverseInverse MatrixMatrix

Finds Inverse Matrix, if it exists, of Input Matrix. Wire data to the Input Matrix input to
determine the polymorphic instance to use or manually select the instance.


   • Real Inverse Matrix VI
   • Complex Inverse Matrix VI

If Input Matrix is nonsingular, you can find Inverse Matrix by solving the linear system
given by the following equation.

AB= I,

where Ais the Input Matrix, Bis the Inverse Matrix, and Iis the identity matrix.

If Ais a nonsingular matrix, you can show that the solution to the preceding system is
unique and that it corresponds to the Inverse Matrix of A, given by the following
equation.

B= A–1

Therefore, Bis an Inverse Matrix.


                                                    © National Instruments 3061

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3061 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3062 ordinal=3062 -->
## Functions

Functions

           Note The numerical implementation of the matrix inversion is not only
              numerically intensive but, because of its recursive nature, is also highly
                sensitive to round-off errors introduced by the floating-point numeric
               coprocessor. Although the computations use the maximum possible
               accuracy, the VI cannot always solve for the system.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Linear Algebra\Linear
        Algebra Calculator.vi
            • labview\examples\Mathematics\Linear Algebra\Matrix to a
        Power.vi

      RealReal InverseInverse MatrixMatrix VIVI

       Finds Inverse Matrix, if it exists, of Input Matrix. Wire data to the Input Matrix input to
      determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •      Input Matrix —

            Input Matrix must be nonsingular and must have as many rows as columns. If Input Matrix is
             singular or is not square, the VI sets Inverse Matrix to an empty array and returns an error.

          A nonsingular matrix is a matrix in which no row or column contains a linear combination of any
            other row or column, respectively. You cannot always determine beforehand whether the matrix
                is singular, especially with large systems. The Inverse Matrix VI detects singular matrices and
             returns an error, so you do not need to verify whether you have a valid system before using this
                VI.

               •      matrix type —


3062   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3062 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3063 ordinal=3063 -->
## Functions

Functions


    matrix type is the type of Input Matrix. Knowing the type of Input Matrix can speed up the
    computation of the Inverse Matrix and can help you to avoid unnecessary computation, which
    could introduce numerical inaccuracy.

           General    0            (default)
    1      Positive definite
    2     Lower triangular
    3     Upper triangular

   •      Inverse Matrix —

    Inverse Matrix is the inverse matrix of the Input Matrix.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If Input Matrix is nonsingular, you can find Inverse Matrix by solving the linear system
given by the following equation.

AB= I,

where Ais the Input Matrix, Bis the Inverse Matrix, and Iis the identity matrix.

If Ais a nonsingular matrix, you can show that the solution to the preceding system is
unique and that it corresponds to the Inverse Matrix of A, given by the following
equation.

B= A–1

Therefore, Bis an Inverse Matrix.

      Note The numerical implementation of the matrix inversion is not only
        numerically intensive but, because of its recursive nature, is also highly


                                                    © National Instruments 3063

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3063 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3064 ordinal=3064 -->
## Functions

Functions


                sensitive to round-off errors introduced by the floating-point numeric
               coprocessor. Although the computations use the maximum possible
               accuracy, the VI cannot always solve for the system.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Linear Algebra\Linear
        Algebra Calculator.vi
            • labview\examples\Mathematics\Linear Algebra\Matrix to a
        Power.vi

     ComplexComplex InverseInverse MatrixMatrix VIVI

       Finds Inverse Matrix, if it exists, of Input Matrix. Wire data to the Input Matrix input to
      determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •      Input Matrix —

            Input Matrix must be a nonsingular, square matrix. If the Input Matrix is singular or is not
            square, the VI sets the Inverse Matrix to an empty array and returns an error.

          A nonsingular matrix is a matrix in which no row or column contains a linear combination of any
            other row or column, respectively. You cannot always determine beforehand whether the matrix
                is singular, especially with large systems. The Complex Inverse Matrix VI detects singular
            matrices and returns an error, so you do not need to verify whether you have a valid system
            before using this VI.

               •      matrix type —

            matrix type is the type of Input Matrix. Knowing the type of Input Matrix can speed up the
           computation of the Inverse Matrix and can help you to avoid unnecessary computation, which
            could introduce numerical inaccuracy.


3064   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3064 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3065 ordinal=3065 -->
## Functions

Functions


           General    0
            (default)
    1      Positive definite
    2     Lower triangular
    3     Upper triangular

   •      Inverse Matrix —

    Inverse Matrix is the inverse matrix of the Input Matrix.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If Input Matrix is nonsingular, you can find Inverse Matrix by solving the linear system
given by the following equation.

AB= I,

where Ais the Input Matrix, Bis the Inverse Matrix, and Iis the identity matrix.

If Ais a nonsingular matrix, you can show that the solution to the preceding system is
unique and that it corresponds to the Inverse Matrix of A, given by the following
equation.

B= A–1

Therefore, Bis an Inverse Matrix.

      Note The numerical implementation of the matrix inversion is not only
        numerically intensive but, because of its recursive nature, is also highly
        sensitive to round-off errors introduced by the floating-point numeric
        coprocessor. Although the computations use the maximum possible
        accuracy, the VI cannot always solve for the system.


                                                    © National Instruments 3065

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3065 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3066 ordinal=3066 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Linear Algebra\Linear
        Algebra Calculator.vi
            • labview\examples\Mathematics\Linear Algebra\Matrix to a
        Power.vi

     PseudoInversePseudoInverse MatrixMatrix

       Finds the PseudoInverse Matrix of Input Matrix. Wire data to the Input Matrix input to
      determine the polymorphic instance to use or manually select the instance.


            • Real PseudoInverse Matrix VI
            • Complex Pseudoinverse Matrix VI

      The m-by-nmatrix A+ is called the pseudoinverse of matrix A if A+ satisfies the
       following four Moore-Penrose conditions:

            • A A+ A = A.
            • A+ A A+ = A+.
            • A A+ is a symmetric matrix.
            • A+ A is a symmetric matrix.

      The VI computes PseudoInverse Matrix A+ using the SVD algorithm. For example,
      assume the singular value decomposition of Aequals USV*. Then A+ = VS+U*. You can
       calculate the pseudoinverse matrix of a diagonal matrix Sby taking the reciprocal of
      each element on the diagonal. When the elements are smaller than the tolerance, this
        VI sets the reciprocals to zero.

      The pseudoinverse provides a least-squares solution to a system of linear equations.


3066   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3066 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3067 ordinal=3067 -->
## Functions

Functions

For example, for a linear system Ax= b, the following equation is the least-squares
solution: x= A+b.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Linear Algebra\Linear
   Algebra Calculator.vi

RealReal PseudoInversePseudoInverse MatrixMatrix VIVI

Finds the PseudoInverse Matrix of Input Matrix. Wire data to the Input Matrix input to
determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •      Input Matrix —

    Input Matrix is a rectangular, real matrix. When Input Matrix is not a square matrix, or when
    Input Matrix is singular, the inverse of Input Matrix does not exist. You can compute the
    pseudoinverse of Input Matrix instead.

   •      tolerance —

    tolerance defines a level such that the number of singular values greater than this level is the
    rank of Input Matrix. The default is –1.

   •      PseudoInverse Matrix —

    PseudoInverse Matrix is the pseudoinverse matrix of the Input Matrix. If Input Matrix A is square
    and not singular, then the pseudoinverse is the same as the inverse of a matrix, and the Inverse
    Matrix VI should be used as a more efficient method of computing the inverse of the Input
    Matrix.

   •       error —


                                                    © National Instruments 3067

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3067 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3068 ordinal=3068 -->
## Functions

Functions


             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The m-by-nmatrix A+ is called the pseudoinverse of matrix A if A+ satisfies the
       following four Moore-Penrose conditions:

            • A A+ A = A.
            • A+ A A+ = A+.
            • A A+ is a symmetric matrix.
            • A+ A is a symmetric matrix.

      The VI computes PseudoInverse Matrix A+ using the SVD algorithm. For example,
      assume the singular value decomposition of Aequals USV*. Then A+ = VS+U*. You can
       calculate the pseudoinverse matrix of a diagonal matrix Sby taking the reciprocal of
      each element on the diagonal. When the elements are smaller than the tolerance, this
        VI sets the reciprocals to zero.

      The pseudoinverse provides a least-squares solution to a system of linear equations.
       For example, for a linear system Ax= b, the following equation is the least-squares
       solution: x= A+b.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Linear Algebra\Linear
        Algebra Calculator.vi

     ComplexComplex PseudoinversePseudoinverse MatrixMatrix VIVI

       Finds the PseudoInverse Matrix of Input Matrix. Wire data to the Input Matrix input to
      determine the polymorphic instance to use or manually select the instance.


3068   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3068 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3069 ordinal=3069 -->
## Functions

Functions


Inputs/Outputs

   •      Input Matrix —

    Input Matrix is usually a rectangular complex matrix. When Input Matrix is not a square matrix,
    or when Input Matrix is singular, the inverse of Input Matrix does not exist. You can compute the
    pseudoinverse of Input Matrix instead.

   •      tolerance —

    tolerance defines a level such that the number of singular values greater than this level is the
    rank of Input Matrix. The default is –1.

   •      PseudoInverse Matrix —

    PseudoInverse Matrix is the pseudoinverse matrix of Input Matrix. If Input Matrix is square and
    not singular, then the pseudoinverse is the same as the inverse of a matrix, and the Inverse
    Matrix VI should be used as a more efficient method of computing the inverse of the Input
    Matrix.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The m-by-nmatrix A+ is called the pseudoinverse of matrix A if A+ satisfies the
following four Moore-Penrose conditions:

  • A A+ A = A.
  • A+ A A+ = A+.
  • A A+ is a symmetric matrix.
  • A+ A is a symmetric matrix.

The VI computes PseudoInverse Matrix A+ using the SVD algorithm. For example,
assume the singular value decomposition of Aequals USV*. Then A+ = VS+U*. You can
calculate the pseudoinverse matrix of a diagonal matrix Sby taking the reciprocal of


                                                    © National Instruments 3069

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3069 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3070 ordinal=3070 -->
## Functions

Functions

      each element on the diagonal. When the elements are smaller than the tolerance, this
        VI sets the reciprocals to zero.

      The pseudoinverse provides a least-squares solution to a system of linear equations.
       For example, for a linear system Ax= b, the following equation is the least-squares
       solution: x= A+b.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Linear Algebra\Linear
        Algebra Calculator.vi

     TransposeTranspose MatrixMatrix

       Transposes Input Matrix. If Input Matrix is a complex matrix, the VI performs conjugate
       transposition. Wire data to the Input Matrix input to determine the polymorphic
       instance to use or manually select the instance.


            • Real Transpose Matrix VI
            • Complex Conjugate Transpose Matrix VI

      RealReal TransposeTranspose MatrixMatrix VIVI

       Transposes Input Matrix. If Input Matrix is a complex matrix, the VI performs conjugate
       transposition. Wire data to the Input Matrix input to determine the polymorphic
       instance to use or manually select the instance.


3070   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3070 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3071 ordinal=3071 -->
## Functions

Functions

Inputs/Outputs

   •      Input Matrix —

    Input Matrix is the input matrix for the transposition operation.

   •      Matrix Transpose —

    Matrix Transpose returns the transpose of Input Matrix.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


ComplexComplex ConjugateConjugate TransposeTranspose MatrixMatrix VIVI

Transposes Input Matrix. If Input Matrix is a complex matrix, the VI performs conjugate
transposition. Wire data to the Input Matrix input to determine the polymorphic
instance to use or manually select the instance.


Inputs/Outputs

   •      Input Matrix —

    Input Matrix is the input matrix for the complex conjugate transposition operation.

   •      Matrix Conjugate Transpose —

    Matrix Conjugate Transpose returns the complex conjugate transpose of Input Matrix.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


                                                    © National Instruments 3071

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3071 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3072 ordinal=3072 -->
## Functions

Functions

      MatrixMatrix SquareSquare RootRoot

      Computes the square root of Input Matrix. Wire data to the Input Matrix input to
      determine the polymorphic instance to use or manually select the instance.


            • Real Matrix Square Root VI
            • Complex Matrix Square Root VI

      RealReal MatrixMatrix SquareSquare RootRoot VIVI

      Computes the square root of Input Matrix. Wire data to the Input Matrix input to
      determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •      Input Matrix —

            Input Matrix is the real matrix for which you want to compute the square root.

               •      Matrix Square Root —

            Matrix Square Root returns the square root of Input Matrix.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     ComplexComplex MatrixMatrix SquareSquare RootRoot VIVI

      Computes the square root of Input Matrix. Wire data to the Input Matrix input to
      determine the polymorphic instance to use or manually select the instance.


3072   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3072 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3073 ordinal=3073 -->
## Functions

Functions


Inputs/Outputs

   •      Input Matrix —

    Input Matrix is the complex matrix for which you want to compute the square root.

   •      Matrix Square Root —

    Matrix Square Root returns the square root of Input Matrix.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

MatrixMatrix ExpExp

Computes the exponential of a square Input Matrix. Wire data to the Input Matrix
input to determine the polymorphic instance to use or manually select the instance.


  • Real Matrix Exp VI
  • Complex Matrix Exp VI

The following equation defines the exponential of a matrix:


where Iis the identity matrix.

This VI uses the Pade Approximation method to calculate the exponential.


                                                    © National Instruments 3073

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3073 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3074 ordinal=3074 -->
## Functions

Functions

      The matrix exponential plays a key role in solving linear differential equations. For
      example, consider the linear differential equation y'(x) = Ay(x), where y(x) equals the
       following vector:


      The solution to this linear differential equation is y(x) = eAxy(0).

      RealReal MatrixMatrix ExpExp VIVI

      Computes the exponential of a square Input Matrix. Wire data to the Input Matrix
       input to determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •      Input Matrix —

            Input Matrix is the real square matrix for which you want the exponential.

               •      Matrix Exp —

            Matrix Exp returns the exponential of Input Matrix.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The following equation defines the exponential of a matrix:


      where Iis the identity matrix.

3074   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3074 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3075 ordinal=3075 -->
## Functions

Functions

This VI uses the Pade Approximation method to calculate the exponential.

The matrix exponential plays a key role in solving linear differential equations. For
example, consider the linear differential equation y'(x) = Ay(x), where y(x) equals the
following vector:


The solution to this linear differential equation is y(x) = eAxy(0).

ComplexComplex MatrixMatrix ExpExp VIVI

Computes the exponential of a square Input Matrix. Wire data to the Input Matrix
input to determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •      Input Matrix —

    Input Matrix is the complex square matrix for which you want the exponential.

   •      Matrix Exp —

    Matrix Exp returns the exponential of Input Matrix.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The following equation defines the exponential of a matrix:


                                                    © National Instruments 3075

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3075 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3076 ordinal=3076 -->
## Functions

Functions

      where Iis the identity matrix.

       This VI uses the Pade Approximation method to calculate the exponential.

      The matrix exponential plays a key role in solving linear differential equations. For
      example, consider the linear differential equation y'(x) = Ay(x), where y(x) equals the
       following vector:


      The solution to this linear differential equation is y(x) = eAxy(0).

      MatrixMatrix PowerPower

      Computes the nth power of Input Matrix. Wire data to the Input Matrix input to
      determine the polymorphic instance to use or manually select the instance.


            • Real Matrix Power VI
            • Complex Matrix Power VI

      RealReal MatrixMatrix PowerPower VIVI

      Computes the nth power of Input Matrix. Wire data to the Input Matrix input to
      determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •      Input Matrix —


3076   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3076 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3077 ordinal=3077 -->
## Functions

Functions


    Input Matrix is the matrix for which you want to compute the nth power.

   •     n —

   n specifies the order of the power operation.

   •      Matrix Power —

    Matrix Power returns the nth power of Input Matrix

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


ComplexComplex MatrixMatrix PowerPower VIVI

Computes the nth power of Input Matrix. Wire data to the Input Matrix input to
determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •      Input Matrix —

    Input Matrix is the matrix for which you want to compute the nth power.

   •     n —

   n specifies the order of the power operation.

   •      Matrix Power —

    Matrix Power returns the nth power of Input Matrix

   •       error —


                                                    © National Instruments 3077

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3077 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3078 ordinal=3078 -->
## Functions

Functions


             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

      MatrixMatrix LogarithmLogarithm

      Computes the natural logarithm of a square Input Matrix. Wire data to the Input
       Matrix input to determine the polymorphic instance to use or manually select the
       instance.


            • Real Matrix Logarithm VI
            • Complex Matrix Logarithm VI

      The natural logarithm is the inverse operation of the exponential. The following
       equation defines the natural logarithm of a matrix A: eB = A, where matrix Bis the
       logarithm of matrix A. A matrix has a logarithm if and only if its inverse matrix exists.
       For a real matrix A, its logarithm matrix Bcan be complex, and the conjugate of matrix
   Bis also the natural logarithm of A.

      A real matrix Ais normal if AAT = ATA. For a non-singular normal matrix, if each
       negative eigenvalues of Aoccur an even number of times, Ahas a real logarithm. Note
       that this does not guarantee the uniqueness of the real logarithm.

      RealReal MatrixMatrix LogarithmLogarithm VIVI

      Computes the natural logarithm of a square Input Matrix. Wire data to the Input
       Matrix input to determine the polymorphic instance to use or manually select the
       instance.


3078   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3078 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3079 ordinal=3079 -->
## Functions

Functions

Inputs/Outputs

   •      Input Matrix —

    Input Matrix is the real square matrix for which you want the natural logarithm.

   •      logarithm option —

    logarithm option specifies the option for the logarithm that this VI returns.

    0 General (default)– Specifies that Input Matrix is regarded as a complex matrix.
     Real– Returns an exact real logarithm when Input Matrix is a non-singular normal matrix and
     each of the negative eigenvalues occur an even number of times. When Input Matrix is not    1     normal or one of its negative eigenvalues occurs an odd number of times, LabVIEW returns
      Matrix Logarithm as if logarithm option was General.

   •      Matrix Logarithm —

    Matrix Logarithm returns the natural logarithm of Input Matrix.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The natural logarithm is the inverse operation of the exponential. The following
equation defines the natural logarithm of a matrix A: eB = A, where matrix Bis the
logarithm of matrix A. A matrix has a logarithm if and only if its inverse matrix exists.
For a real matrix A, its logarithm matrix Bcan be complex, and the conjugate of matrix
Bis also the natural logarithm of A.

A real matrix Ais normal if AAT = ATA. For a non-singular normal matrix, if each
negative eigenvalues of Aoccur an even number of times, Ahas a real logarithm. Note
that this does not guarantee the uniqueness of the real logarithm.

ComplexComplex MatrixMatrix LogarithmLogarithm VIVI

Computes the natural logarithm of a square Input Matrix. Wire data to the Input
Matrix input to determine the polymorphic instance to use or manually select the

                                                    © National Instruments 3079

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3079 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3080 ordinal=3080 -->
## Functions

Functions

       instance.


      Inputs/Outputs

               •      Input Matrix —

            Input Matrix is the complex square matrix for which you want the natural logarithm.

               •      Matrix Logarithm —

            Matrix Logarithm returns the natural logarithm of Input Matrix.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The natural logarithm is the inverse operation of the exponential. The following
       equation defines the natural logarithm of a matrix A: eB = A, where matrix Bis the
       logarithm of matrix A. A matrix has a logarithm if and only if its inverse matrix exists.
       For a real matrix A, its logarithm matrix Bcan be complex, and the conjugate of matrix
   Bis also the natural logarithm of A.

      A real matrix Ais normal if AAT = ATA. For a non-singular normal matrix, if each
       negative eigenvalues of Aoccur an even number of times, Ahas a real logarithm. Note
       that this does not guarantee the uniqueness of the real logarithm.

    LULU FactorizationFactorization

      Performs the LU factorization of A so that PA = LU. Wire data to the A input to
      determine the polymorphic instance to use or manually select the instance.


3080   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3080 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3081 ordinal=3081 -->
## Functions

Functions

  • Real LU Factorization VI
  • Complex LU Factorization VI

The LU Factorization VI factors an m× nmatrix A into the following types of matrices
so that PA = LU:

  • L is an m× min(m, n) matrix. When m≤ n, L is a lower triangular matrix with ones
   on the diagonal. When m> n, L is a lower trapezoidal matrix with ones on the
    diagonal.
  • U is a min(m, n) × nmatrix. When m≥ n, U is an upper triangular matrix. When m
   < n, U is an upper trapezoidal matrix.
  • P is an m× mpermutation matrix, which serves as the identity matrix with some
   rows exchanged.

For a singular matrix, the VI completes the factorization and returns a warning, and
there is at least one zero at the diagonal of U.

The following equation illustrates one useful property of LU factorization when A is a
square matrix:


where det(A) is the determinant of A.

LU factorization serves as a key step for inverting a matrix, computing the determinant
of a matrix, and solving a linear equation.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Linear Algebra\Linear
   Algebra Calculator.vi


                                                    © National Instruments 3081

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3081 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3082 ordinal=3082 -->
## Functions

Functions

      RealReal LULU FactorizationFactorization VIVI

      Performs the LU factorization of A so that PA = LU. Wire data to the A input to
      determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •     A —

          A is a real matrix.

               •      L —

           L is a lower triangular matrix with ones on the diagonal.

               •    U —

        U is an upper triangular matrix.

               •     P —

         P is a permutation matrix.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The LU Factorization VI factors an m× nmatrix A into the following types of matrices
      so that PA = LU:

            • L is an m× min(m, n) matrix. When m≤ n, L is a lower triangular matrix with ones
         on the diagonal. When m> n, L is a lower trapezoidal matrix with ones on the
           diagonal.
            • U is a min(m, n) × nmatrix. When m≥ n, U is an upper triangular matrix. When m


3082   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3082 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3083 ordinal=3083 -->
## Functions

Functions

   < n, U is an upper trapezoidal matrix.
  • P is an m× mpermutation matrix, which serves as the identity matrix with some
   rows exchanged.

For a singular matrix, the VI completes the factorization and returns a warning, and
there is at least one zero at the diagonal of U.

The following equation illustrates one useful property of LU factorization when A is a
square matrix:


where det(A) is the determinant of A.

LU factorization serves as a key step for inverting a matrix, computing the determinant
of a matrix, and solving a linear equation.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Linear Algebra\Linear
   Algebra Calculator.vi

ComplexComplex LULU FactorizationFactorization VIVI

Performs the LU factorization of A so that PA = LU. Wire data to the A input to
determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     A —


                                                    © National Instruments 3083

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3083 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3084 ordinal=3084 -->
## Functions

Functions


          A is a complex matrix.

               •      L —

           L is a complex, lower triangular matrix with 1+0ion the diagonal.

               •    U —

        U is a complex, upper triangular matrix.

               •     P —

         P is a permutation matrix.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The LU Factorization VI factors an m× nmatrix A into the following types of matrices
      so that PA = LU:

            • L is an m× min(m, n) matrix. When m≤ n, L is a lower triangular matrix with ones
         on the diagonal. When m> n, L is a lower trapezoidal matrix with ones on the
           diagonal.
            • U is a min(m, n) × nmatrix. When m≥ n, U is an upper triangular matrix. When m
         < n, U is an upper trapezoidal matrix.
            • P is an m× mpermutation matrix, which serves as the identity matrix with some
         rows exchanged.

       For a singular matrix, the VI completes the factorization and returns a warning, and
       there is at least one zero at the diagonal of U.

      The following equation illustrates one useful property of LU factorization when A is a
      square matrix:


3084   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3084 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3085 ordinal=3085 -->
## Functions

Functions

where det(A) is the determinant of A.

LU factorization serves as a key step for inverting a matrix, computing the determinant
of a matrix, and solving a linear equation.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Linear Algebra\Linear
   Algebra Calculator.vi

CholeskyCholesky FactorizationFactorization

Performs Cholesky factorization on a symmetric or Hermitian positive definite matrix.
Wire data to the A input to determine the polymorphic instance to use or manually
select the instance.


  • Real Cholesky Factorization VI
  • Complex Cholesky Factorization VI

The following equations show the factorization of A for real cases and complex cases,
respectively:

A = RTRA = RHR

where Ris an upper triangular matrix, and all the diagonal elements of Rare positive.

The Cholesky factorization exists only if the matrix A is positive definite and either
symmetric or Hermitian. If A is not symmetric or Hermitian, this VI uses only the upper
triangular portion of A. If A is not positive definite, this VI returns an error.

You can use Cholesky factorization to solve linear equations. For example, to solve the
linear equation Ax= b, where Ais a positive symmetric matrix and A= RTR, you can

                                                    © National Instruments 3085

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3085 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3086 ordinal=3086 -->
## Functions

Functions

       derive the following equations: Rx= h, and h= R–Tb. Then you can use the triangular
       property of matrix Rto solve the equations.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Linear Algebra\Linear
        Algebra Calculator.vi

      RealReal CholeskyCholesky FactorizationFactorization VIVI

      Performs Cholesky factorization on a symmetric or Hermitian positive definite matrix.
       Wire data to the A input to determine the polymorphic instance to use or manually
        select the instance.


      Inputs/Outputs

               •     A —

          A is a symmetric positive definite matrix.

                    If A is not symmetric, this VI uses only the upper triangular portion of A.

               •      Cholesky —

           Cholesky contains the factored, upper triangular matrix R.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The following equations show the factorization of A for real cases and complex cases,
        respectively:


3086   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3086 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3087 ordinal=3087 -->
## Functions

Functions

A = RTRA = RHR

where Ris an upper triangular matrix, and all the diagonal elements of Rare positive.

The Cholesky factorization exists only if the matrix A is positive definite and either
symmetric or Hermitian. If A is not symmetric or Hermitian, this VI uses only the upper
triangular portion of A. If A is not positive definite, this VI returns an error.

You can use Cholesky factorization to solve linear equations. For example, to solve the
linear equation Ax= b, where Ais a positive symmetric matrix and A= RTR, you can
derive the following equations: Rx= h, and h= R–Tb. Then you can use the triangular
property of matrix Rto solve the equations.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Linear Algebra\Linear
   Algebra Calculator.vi

ComplexComplex CholeskyCholesky FactorizationFactorization VIVI

Performs Cholesky factorization on a symmetric or Hermitian positive definite matrix.
Wire data to the A input to determine the polymorphic instance to use or manually
select the instance.


Inputs/Outputs

   •     A —

   A is a Hermitian positive definite matrix.

       If A is not Hermitian, this VI uses only the upper triangular portion of A.

   •      Cholesky R —

                                                    © National Instruments 3087

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3087 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3088 ordinal=3088 -->
## Functions

Functions


           Cholesky R contains the factored upper triangular matrix R.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The following equations show the factorization of A for real cases and complex cases,
        respectively:

     A = RTRA = RHR

      where Ris an upper triangular matrix, and all the diagonal elements of Rare positive.

      The Cholesky factorization exists only if the matrix A is positive definite and either
      symmetric or Hermitian. If A is not symmetric or Hermitian, this VI uses only the upper
       triangular portion of A. If A is not positive definite, this VI returns an error.

      You can use Cholesky factorization to solve linear equations. For example, to solve the
        linear equation Ax= b, where Ais a positive symmetric matrix and A= RTR, you can
       derive the following equations: Rx= h, and h= R–Tb. Then you can use the triangular
       property of matrix Rto solve the equations.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Linear Algebra\Linear
        Algebra Calculator.vi

     CholeskyCholesky FactorizationFactorization Rank-1Rank-1 UpdateUpdate

      Performs Cholesky factorization on the rank-1 updated Cholesky matrix. The VI
      performs Cholesky factorization directly on the known factored matrix instead of the
      updated matrix.


3088   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3088 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3089 ordinal=3089 -->
## Functions

Functions

Wire data to the R or X inputs to determine the polymorphic instance to use or
manually select the instance.


  • Cholesky Factorization Rank-1 Update (DBL) VI
  • Cholesky Factorization Rank-1 Update (CDB) VI

CholeskyCholesky FactorizationFactorization Rank-1Rank-1 UpdateUpdate (DBL)(DBL) VIVI

Performs Cholesky factorization on the rank-1 updated Cholesky matrix. The VI
performs Cholesky factorization directly on the known factored matrix instead of the
updated matrix.

Wire data to the R or X inputs to determine the polymorphic instance to use or
manually select the instance.


Inputs/Outputs

   •     R —

   R is a real factored matrix of a known Cholesky factorization. R must be square. This VI uses only
    the upper triangular matrix of R.

   •     X —

    X is a vector that updates R'R. The length of X must equal the number of columns in R.

   •     method —

   method specifies whether to perform the rank-1 Cholesky update or downdate.

    0 Update (default)—Computes the Cholesky factorization of R'R+XX'.
    1 Downdate—Computes the Cholesky factorization of R'R-XX'. When method is Downdate, R'R


                                                    © National Instruments 3089

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3089 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3090 ordinal=3090 -->
## Functions

Functions


           and R'R-XX' must be positive definite.

               •     Updated R —

          Updated R returns the factored upper triangular matrix of the rank-1 updated Cholesky
              factorization.

         When method is Downdate, if R'R and R''-XX' are not positive definite, this VI returns a warning
          and Updated R returns the upper triangular matrix of R.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      CholeskyCholesky FactorizationFactorization Rank-1Rank-1 UpdateUpdate (CDB)(CDB) VIVI

      Performs Cholesky factorization on the rank-1 updated Cholesky matrix. The VI
      performs Cholesky factorization directly on the known factored matrix instead of the
      updated matrix.

       Wire data to the R or X inputs to determine the polymorphic instance to use or
      manually select the instance.


      Inputs/Outputs

               •     R —

         R is a complex factored matrix of a known Cholesky factorization. R must be square. This VI uses
            only the upper triangular matrix of R.

               •     X —

          X is a vector that updates R'R. The length of X must equal the number of columns in R.

               •     method —

3090   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3090 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3091 ordinal=3091 -->
## Functions

Functions


   method specifies whether to perform the rank-1 Cholesky update or downdate.

    0 Update (default)—Computes the Cholesky factorization of R′R+XX′.
    Downdate—Computes the Cholesky factorization of R′R-XX′. When method is Downdate, R′R    1
     and R′R-XX′ must be positive definite.

   •     Updated R —

    Updated R returns the factored upper triangular matrix of the rank-1 updated Cholesky
     factorization.

   When method is Downdate, if R′R and R′R-XX′ are not positive definite, this VI returns a warning
    and Updated R returns the upper triangular matrix of R.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

QRQR DecompositionDecomposition

Performs the QR decomposition of A with or without column pivoting. Wire data to the
A input to determine the polymorphic instance to use or manually select the instance.


  • Real QR Decomposition VI
  • Complex QR Decomposition VI

The following equation defines the QR decomposition:


where mis the number of rows and nis the number of columns in A, Q is an m-by-m
unitary matrix, R is an m-by-nupper trapezoidal matrix, R1 is a k-by-kupper


                                                    © National Instruments 3091

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3091 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3092 ordinal=3092 -->
## Functions

Functions

       triangular matrix where kis the minimum of mand n, R2 is an m-by-(n-m) submatrix
       of R, and 0 is an (m-n)-by-nzero matrix.

      You can use QR decomposition to calculate the determinant of a square matrix. For
      example, consider the following equation: det(A) = det(Q)*det(R). Because Q is
       orthogonal, the following is true: |det(Q)| = 1. Thus, the following also is true:


      You also can use QR decomposition to solve the least-squares problem of a linear
       equation Ax= bwhen A is full rank and m≥ n. For example, consider the following
       equation:


      where the following are true:

            •

            •
            • The size of Q1 is m-by-n
            • The size of Q2 is m-by-(m-n)
            • The size of R1 is n-by-n.

      Because min(||b– Ax||2) depends on min(||Q1Tb– R1x||2), you can obtain the solution
    xby solving the following new linear equation: R1x= Q1Tb.

      RealReal QRQR DecompositionDecomposition VIVI

      Performs the QR decomposition of A with or without column pivoting. Wire data to the
     A input to determine the polymorphic instance to use or manually select the instance.


3092   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3092 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3093 ordinal=3093 -->
## Functions

Functions


Inputs/Outputs

   •     A —

   A is an m-by-nreal matrix, where mis the number of rows in A and nis the number of columns
     in A. It can be either a square or rectangular matrix.

   •       pivot? —

    pivot? specifies whether this VI decomposes A with column pivoting. When pivot? is TRUE, this VI
    decomposes A according to the following equation: AP=QR. This VI returns the absolute values
     of the diagonals of R in descending order. When pivot? is FALSE, this VI decomposes A according
    to the following equation: A=QR. The default is FALSE.

   •    Q option —

   Q option specifies how this VI generates Q.

   Q option must take one of the following values, where mis the number of rows in A, and nis the
   number of columns in A.

    0 Full Size Q (default)—The size of Q is m-by-m, and the size of R is m-by-n.
    1 Economy Size Q—The size of Q is m-by-min(m, n), and the size of R is min(m, n)-by-n.
    2 No Q—This VI does not generate Q, and the size of R is min(m, n)-by-n.

   •    Q —

   Q is the orthogonal matrix.

   •     R —

   R is the upper triangular matrix.

   •     P —

   P is the n-by-npermutation matrix, where nis the number of columns in A. P is not empty only if
    pivot? is TRUE.

   •       error —

                                                    © National Instruments 3093

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3093 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3094 ordinal=3094 -->
## Functions

Functions


             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The following equation defines the QR decomposition:


      where mis the number of rows and nis the number of columns in A, Q is an m-by-m
       unitary matrix, R is an m-by-nupper trapezoidal matrix, R1 is a k-by-kupper
       triangular matrix where kis the minimum of mand n, R2 is an m-by-(n-m) submatrix
       of R, and 0 is an (m-n)-by-nzero matrix.

      You can use QR decomposition to calculate the determinant of a square matrix. For
      example, consider the following equation: det(A) = det(Q)*det(R). Because Q is
       orthogonal, the following is true: |det(Q)| = 1. Thus, the following also is true:


      You also can use QR decomposition to solve the least-squares problem of a linear
       equation Ax= bwhen A is full rank and m≥ n. For example, consider the following
       equation:


      where the following are true:

            •

            •
            • The size of Q1 is m-by-n
            • The size of Q2 is m-by-(m-n)

3094   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3094 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3095 ordinal=3095 -->
## Functions

Functions

   • The size of R1 is n-by-n.

Because min(||b– Ax||2) depends on min(||Q1Tb– R1x||2), you can obtain the solution
xby solving the following new linear equation: R1x= Q1Tb.

ComplexComplex QRQR DecompositionDecomposition VIVI

Performs the QR decomposition of A with or without column pivoting. Wire data to the
A input to determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     A —

    A is an m-by-ncomplex matrix, where mis the number of rows in A and nis the number of
    columns in A. It can be either a square or rectangular matrix.

   •       pivot? —

     pivot? specifies whether this VI decomposes A with column pivoting. When pivot? is TRUE, this VI
    decomposes A according to the following equation: AP=QR. This VI returns the absolute values
     of the diagonals of R in descending order. When pivot? is FALSE, this VI decomposes A according
     to the following equation: A=QR. The default is FALSE.

   •    Q option —

   Q option specifies how this VI generates Q.

   Q option must take one of the following values, where mis the number of rows in A, and nis the
    number of columns in A.

    0 Full Size Q (default)—The size of Q is m-by-m, and the size of R is m-by-n.
    1 Economy Size Q—The size of Q is m-by-min(m, n), and the size of R is min(m, n)-by-n.
    2 No Q—This VI does not generate Q, and the size of R is min(m, n)-by-n.


                                                    © National Instruments 3095

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3095 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3096 ordinal=3096 -->
## Functions

Functions

               •    Q —

        Q is the orthogonal matrix.

               •     R —

         R is the upper triangular matrix.

               •     P —

         P is the n-by-npermutation matrix, where nis the number of columns in A. P is not empty only if
             pivot? is TRUE.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The following equation defines the QR decomposition:


      where mis the number of rows and nis the number of columns in A, Q is an m-by-m
       unitary matrix, R is an m-by-nupper trapezoidal matrix, R1 is a k-by-kupper
       triangular matrix where kis the minimum of mand n, R2 is an m-by-(n-m) submatrix
       of R, and 0 is an (m-n)-by-nzero matrix.

      You can use QR decomposition to calculate the determinant of a square matrix. For
      example, consider the following equation: det(A) = det(Q)*det(R). Because Q is
       orthogonal, the following is true: |det(Q)| = 1. Thus, the following also is true:


      You also can use QR decomposition to solve the least-squares problem of a linear
       equation Ax= bwhen A is full rank and m≥ n. For example, consider the following
       equation:


3096   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3096 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3097 ordinal=3097 -->
## Functions

Functions


where the following are true:

   •

   •
   • The size of Q1 is m-by-n
   • The size of Q2 is m-by-(m-n)
   • The size of R1 is n-by-n.

Because min(||b– Ax||2) depends on min(||Q1Tb– R1x||2), you can obtain the solution
xby solving the following new linear equation: R1x= Q1Tb.

SVDSVD DecompositionDecomposition

Computes the singular value decomposition (SVD) of the m× nmatrix A. Wire data to
the A input to determine the polymorphic instance to use or manually select the
instance.


   • Real SVD Decomposition VI
   • Complex SVD Decomposition VI

The following equation defines the singular value decomposition of matrix A for real
cases:

A = USVT

The following equation defines the singular value decomposition of matrix A for
complex cases:


                                                    © National Instruments 3097

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3097 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3098 ordinal=3098 -->
## Functions

Functions

     A = USVH

        In the previous two equations, the columns in U and V are orthogonal, and S is a
       diagonal matrix whose diagonal elements are the singular values of A in descending
       order.

      Because the singular values of matrix A are the nonnegative square roots of the
       eigenvalues of AHA, they all are nonnegative. The diagonal matrix S is unique for a
       given matrix.

           If rrepresents the rank of A, the number of nonzero singular values of A is r, the first r
      columns in U are the normal orthogonal bases of the column space of A, and the first r
      columns in V are the normal orthogonal bases of the row space of A.

      You can use SVD decomposition to solve linear algebra problems, such as the
       pseudoinverse of a matrix, total least-squares minimization, and matrix
       approximation. SVD factorization also is useful in image processing applications, such
       as image compression.

      RealReal SVDSVD DecompositionDecomposition VIVI

      Computes the singular value decomposition (SVD) of the m× nmatrix A. Wire data to
       the A input to determine the polymorphic instance to use or manually select the
       instance.


      Inputs/Outputs

               •     A —

          A is an m× nmatrix with mrows and ncolumns.

               •       singular values only? —


3098   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3098 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3099 ordinal=3099 -->
## Functions

Functions


    singular values only? specifies whether to compute only the singular values. The default is
    FALSE. When singular values only? is TRUE, the VI does not compute Matrix U and Matrix V.

   •     SVD option —

   SVD Option specifies how the VI performs the decomposition.

     Thin (default)—Decomposes an m× nmatrix as the multiplication of matrix U(m× min(m,n)),    0
   S(min(m,n) × min(m,n)), and conjugated transpose of V (n× min(m,n)).
     Full—Decomposes an m× nmatrix as the multiplication of matrix U(m× m), S(m× n), and    1
     conjugated transpose of V(n× n).

   •      Vector S —

    Vector S returns the singular values of A in descending order. The values in Vector S are the
    diagonal elements of Matrix S.

   •      Matrix U —

    Matrix U returns the Umatrix of the SVD results. The columns of Matrix U compose an
    orthogonal set.

   •      Matrix S —

    Matrix S returns the Smatrix of the SVD results. Matrix S is a diagonal matrix whose diagonal
    elements are the values from Vector S, or the singular values of A in descending order.

   •      Matrix V —

    Matrix V returns the Vmatrix of the SVD results. The columns of Matrix V compose an orthogonal
     set.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The following equation defines the singular value decomposition of matrix A for real
cases:


                                                    © National Instruments 3099

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3099 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3100 ordinal=3100 -->
## Functions

Functions

     A = USVT

      The following equation defines the singular value decomposition of matrix A for
      complex cases:

     A = USVH

        In the previous two equations, the columns in U and V are orthogonal, and S is a
       diagonal matrix whose diagonal elements are the singular values of A in descending
       order.

      Because the singular values of matrix A are the nonnegative square roots of the
       eigenvalues of AHA, they all are nonnegative. The diagonal matrix S is unique for a
       given matrix.

           If rrepresents the rank of A, the number of nonzero singular values of A is r, the first r
      columns in U are the normal orthogonal bases of the column space of A, and the first r
      columns in V are the normal orthogonal bases of the row space of A.

      You can use SVD decomposition to solve linear algebra problems, such as the
       pseudoinverse of a matrix, total least-squares minimization, and matrix
       approximation. SVD factorization also is useful in image processing applications, such
       as image compression.

     ComplexComplex SVDSVD DecompositionDecomposition VIVI

      Computes the singular value decomposition (SVD) of the m× nmatrix A. Wire data to
       the A input to determine the polymorphic instance to use or manually select the
       instance.


3100   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3100 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3101 ordinal=3101 -->
## Functions

Functions

Inputs/Outputs

   •     A —

   A is an m× nmatrix with mrows and ncolumns.

   •       singular values only? —

    singular values only? specifies whether to compute only the singular values. The default is
    FALSE. When singular values only? is TRUE, the VI does not compute Matrix U and Matrix V.

   •     SVD option —

   SVD Option specifies how the VI performs the decomposition.

     Thin (default)—Decomposes an m× nmatrix as the multiplication of matrix U(m× min(m,n)),    0
   S(min(m,n) × min(m,n)), and conjugated transpose of V (n× min(m,n)).
     Full—Decomposes an m× nmatrix as the multiplication of matrix U(m× m), S(m× n), and
    1
     conjugated transpose of V(n× n).

   •      Vector S —

    Vector S returns the singular values of A in descending order. The values in Vector S are the
    diagonal elements of Matrix S.

   •      Matrix U —

    Matrix U returns the Umatrix of the SVD results. The columns of Matrix U compose an
    orthogonal set.

   •      Matrix S —

    Matrix S returns the Smatrix of the SVD results. Matrix S is a diagonal matrix whose diagonal
    elements are the values from Vector S, or the singular values of A in descending order.

   •      Matrix V —

    Matrix V returns the Vmatrix of the SVD results. The columns of Matrix V compose an orthogonal
     set.

   •       error —


                                                    © National Instruments 3101

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3101 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3102 ordinal=3102 -->
## Functions

Functions


             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The following equation defines the singular value decomposition of matrix A for real
       cases:

     A = USVT

      The following equation defines the singular value decomposition of matrix A for
      complex cases:

     A = USVH

        In the previous two equations, the columns in U and V are orthogonal, and S is a
       diagonal matrix whose diagonal elements are the singular values of A in descending
       order.

      Because the singular values of matrix A are the nonnegative square roots of the
       eigenvalues of AHA, they all are nonnegative. The diagonal matrix S is unique for a
       given matrix.

           If rrepresents the rank of A, the number of nonzero singular values of A is r, the first r
      columns in U are the normal orthogonal bases of the column space of A, and the first r
      columns in V are the normal orthogonal bases of the row space of A.

      You can use SVD decomposition to solve linear algebra problems, such as the
       pseudoinverse of a matrix, total least-squares minimization, and matrix
       approximation. SVD factorization also is useful in image processing applications, such
       as image compression.

      GeneralizedGeneralized SVDSVD DecompositionDecomposition

      Computes the generalized singular value decomposition (GSVD) of a matrix pair (A,B).
      The data types you wire to the A and B inputs determine the polymorphic instance to
       use.

3102   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3102 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3103 ordinal=3103 -->
## Functions

Functions


   • Real Generalized SVD Decomposition VI
   • Complex Generalized SVD Decomposition VI

The following expressions define the generalized singular value decomposition of a
matrix pair (A,B).

A= UCR′ B= VSR′

where Uand Vare orthogonal matrices, and Ris a square matrix.

When you let kbe the rank of matrix     , then the first kdiagonal elements of matrix
C′C+ S′Sare ones and all of the other elements are zeros. The square roots of the first
kdiagonal elements of C′Cand S′Sdetermine the numerators and denominators of
the generalized singular values, respectively.

RealReal GeneralizedGeneralized SVDSVD DecompositionDecomposition VIVI

Computes the generalized singular value decomposition (GSVD) of a matrix pair (A,B).
The data types you wire to the A and B inputs determine the polymorphic instance to
use.


Inputs/Outputs

   •     A —

    A is a matrix with mrows and pcolumns.

   •     B —

                                                    © National Instruments 3103

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3103 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3104 ordinal=3104 -->
## Functions

Functions


         B is a matrix with nrows and pcolumns.

               •       singular values only? —

             singular values only? specifies whether to compute only the generalized singular values. The
             default is FALSE. When singular values only? is TRUE, the VI computes only Singular Values.

               •     SVD option —

          SVD Option specifies how the VI performs the decomposition.

             Thin (default)—Decomposes matrix Aas the multiplication of matrix U(mx min(m,p)), C
           0 (min(m,p) x p) and transpose of R(px p). Decomposes matrix Bas the multiplication of
              matrix V(nx min(n,p)), S(min(n,p) x p) and transpose of R(px p).
            Full—Decomposes matrix Aas the multiplication of matrix U(mx m), C(mx p) and transpose
           1 of R(px p). Decomposes matrix Bas the multiplication of matrix V(nx n), S(nx p) and
             transpose of R(px p).

               •      Singular Values —

            Singular Values returns the generalized singular values of matrix pair (A,B).

               •      Matrix U —

            Matrix U returns the Umatrix of the GSVD results.

               •      Matrix V —

            Matrix V returns the Vmatrix of the GSVD results.

               •      Matrix C —

            Matrix C returns the Cmatrix of the GSVD results.

               •      Matrix S —

            Matrix S returns the Smatrix of the GSVD results.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error


3104   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3104 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3105 ordinal=3105 -->
## Functions

Functions


    Code VI to convert the error code or warning into an error cluster.

   •      Matrix R —

    Matrix R returns the Rmatrix of the GSVD results.


The following expressions define the generalized singular value decomposition of a
matrix pair (A,B).

A= UCR′ B= VSR′

where Uand Vare orthogonal matrices, and Ris a square matrix.

When you let kbe the rank of matrix     , then the first kdiagonal elements of matrix
C′C+ S′Sare ones and all of the other elements are zeros. The square roots of the first
kdiagonal elements of C′Cand S′Sdetermine the numerators and denominators of
the generalized singular values, respectively.

ComplexComplex GeneralizedGeneralized SVDSVD DecompositionDecomposition VIVI

Computes the generalized singular value decomposition (GSVD) of a matrix pair (A,B).
The data types you wire to the A and B inputs determine the polymorphic instance to
use.


Inputs/Outputs

   •     A —

    A is a matrix with mrows and pcolumns.


                                                    © National Instruments 3105

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3105 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3106 ordinal=3106 -->
## Functions

Functions

               •     B —

         B is a matrix with nrows and pcolumns.

               •       singular values only? —

             singular values only? specifies whether to compute only the generalized singular values. The
             default is FALSE. When singular values only? is TRUE, the VI computes only Singular Values.

               •     SVD option —

          SVD Option specifies how the VI performs the decomposition.

             Thin (default)—Decomposes matrix Aas the multiplication of matrix U(mx min(m,p)), C
           0 (min(m,p) x p) and transpose of R(px p). Decomposes matrix Bas the multiplication of
              matrix V(nx min(n,p)), S(min(n,p) x p) and transpose of R(px p).
            Full—Decomposes matrix Aas the multiplication of matrix U(mx m), C(mx p) and transpose
           1 of R(px p). Decomposes matrix Bas the multiplication of matrix V(nx n), S(nx p) and
             transpose of R(px p).

               •      Singular Values —

            Singular Values returns the generalized singular values of matrix pair (A,B).

               •      Matrix U —

            Matrix U returns the Umatrix of the GSVD results.

               •      Matrix V —

            Matrix V returns the Vmatrix of the GSVD results.

               •      Matrix C —

            Matrix C returns the Cmatrix of the GSVD results.

               •      Matrix S —

            Matrix S returns the Smatrix of the GSVD results.

               •       error —


3106   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3106 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3107 ordinal=3107 -->
## Functions

Functions


     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

   •      Matrix R —

    Matrix R returns the Rmatrix of the GSVD results.


The following expressions define the generalized singular value decomposition of a
matrix pair (A,B).

A= UCR′ B= VSR′

where Uand Vare orthogonal matrices, and Ris a square matrix.

When you let kbe the rank of matrix     , then the first kdiagonal elements of matrix
C′C+ S′Sare ones and all of the other elements are zeros. The square roots of the first
kdiagonal elements of C′Cand S′Sdetermine the numerators and denominators of
the generalized singular values, respectively.

SchurSchur DecompositionDecomposition

Performs the Schur decomposition of a square matrix. Wire data to the Input Matrix
input to determine the polymorphic instance to use or manually select the instance.


   • Real Schur Decomposition VI
   • Complex Schur Decomposition VI

The following expression defines the Schur decomposition of a square n× nmatrix A.

A= QSQH

where Sis in Schur form, and QH is the conjugate transpose of matrix Q.

                                                    © National Instruments 3107

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3107 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3108 ordinal=3108 -->
## Functions

Functions

      Real Matrix

       For a real matrix A, Qis an n× northogonal matrix. Sis a block upper triangular
       matrix in real Schur form, whose elements on the main diagonal are all 1 × 1 or 2 × 2
       blocks, as shown in the following matrix.


      where Sii are square blocks of dimension 1 or 2, and i= 1, 2, …, m.

     Complex Matrix

       For a complex matrix A, Qis an n× nunitary matrix. Sis an upper triangular matrix in
      complex Schur form.

      RealReal SchurSchur DecompositionDecomposition VIVI

      Performs the Schur decomposition of a square matrix. Wire data to the Input Matrix
       input to determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •      Input Matrix —

            Input Matrix must be a square real matrix.

               •     compute Schur vectors? —

          compute Schur vectors? specifies whether the VI calculates Schur Vectors. The default is FALSE.


3108   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3108 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3109 ordinal=3109 -->
## Functions

Functions

   •      order —

    order specifies how to order the Eigenvalues and the corresponding Schur Form and Schur
     Vectors.

    0 No Reorder (default)—Does not change the order of the Eigenvalues.
    1 Real Ascending—Lists the Eigenvalues in ascending order according to their real parts.
    2 Real Descending—Lists the Eigenvalues in descending order according to their real parts.
     Magnitude Ascending—Lists the Eigenvalues in ascending order according to their    3     magnitudes.
     Magnitude Descending—Lists the Eigenvalues in descending order according to their    4     magnitudes.

   •      Schur Form —

    Schur Form returns the block upper triangular matrix in real Schur form.

   •      Schur Vectors —

    Schur Vectors returns the orthogonal matrix.

   •      Eigenvalues —

    Eigenvalues returns a complex vector that contains all the computed eigenvalues of Input
     Matrix.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The following expression defines the Schur decomposition of a square n× nmatrix A.

A= QSQH

where Sis in Schur form, and QH is the conjugate transpose of matrix Q.

Real Matrix

For a real matrix A, Qis an n× northogonal matrix. Sis a block upper triangular

                                                    © National Instruments 3109

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3109 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3110 ordinal=3110 -->
## Functions

Functions

       matrix in real Schur form, whose elements on the main diagonal are all 1 × 1 or 2 × 2
       blocks, as shown in the following matrix.


      where Sii are square blocks of dimension 1 or 2, and i= 1, 2, …, m.

     Complex Matrix

       For a complex matrix A, Qis an n× nunitary matrix. Sis an upper triangular matrix in
      complex Schur form.

     ComplexComplex SchurSchur DecompositionDecomposition VIVI

      Performs the Schur decomposition of a square matrix. Wire data to the Input Matrix
       input to determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •      Input Matrix —

            Input Matrix must be a square complex matrix.

               •     compute Schur vectors? —

          compute Schur vectors? specifies whether the VI calculates Schur Vectors. The default is FALSE.

               •      order —

            order specifies how to order the Eigenvalues and the corresponding Schur Form and Schur


3110   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3110 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3111 ordinal=3111 -->
## Functions

Functions


     Vectors.

    0 No Reorder (default)—Does not change the order of the Eigenvalues.
    1 Real Ascending—Lists the Eigenvalues in ascending order according to their real parts.
    2 Real Descending—Lists the Eigenvalues in descending order according to their real parts.
     Magnitude Ascending—Lists the Eigenvalues in ascending order according to their    3     magnitudes.
     Magnitude Descending—Lists the Eigenvalues in descending order according to their    4     magnitudes.

   •      Schur Form —

    Schur Form returns the upper triangular matrix.

   •      Schur Vectors —

    Schur Vectors returns the unitary matrix.

   •      Eigenvalues —

    Eigenvalues returns a complex vector that contains all the computed eigenvalues of Input
     Matrix.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The following expression defines the Schur decomposition of a square n× nmatrix A.

A= QSQH

where Sis in Schur form, and QH is the conjugate transpose of matrix Q.

Real Matrix

For a real matrix A, Qis an n× northogonal matrix. Sis a block upper triangular
matrix in real Schur form, whose elements on the main diagonal are all 1 × 1 or 2 × 2
blocks, as shown in the following matrix.

                                                    © National Instruments 3111

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3111 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3112 ordinal=3112 -->
## Functions

Functions


      where Sii are square blocks of dimension 1 or 2, and i= 1, 2, …, m.

     Complex Matrix

       For a complex matrix A, Qis an n× nunitary matrix. Sis an upper triangular matrix in
      complex Schur form.

     HessenbergHessenberg DecompositionDecomposition

      Performs the Hessenberg decomposition of Input Matrix. Wire data to the Input Matrix
       input to determine the polymorphic instance to use or manually select the instance.


            • Real Hessenberg Decomposition VI
            • Complex Hessenberg Decomposition VI

      The following expression defines the Hessenberg decomposition of an n× nmatrix A:

   A= QHQH

      where Qis an orthogonal matrix when matrix Ais a real matrix and a unitary matrix
     when matrix Ais a complex matrix, QH is the conjugate transpose of matrix Q, and His
      a Hessenberg matrix.

      By definition, a Hessenberg matrix is a matrix with zeros under the main subdiagonal,
       as shown by the following matrix.


3112   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3112 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3113 ordinal=3113 -->
## Functions

Functions


RealReal HessenbergHessenberg DecompositionDecomposition VIVI

Performs the Hessenberg decomposition of Input Matrix. Wire data to the Input Matrix
input to determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •      Input Matrix —

    Input Matrix is an n× nreal matrix.

   •      index low —

    index low is the index low value from the Matrix Balance VI. If you balance Input Matrix with the
    Matrix Balance VI, wire the index low output of the Matrix Balance VI to this input. If the index
    low input of this VI equals –1 (default), the VI uses 0 for index low.

   •      index high —

    index high is the index high value from the Matrix Balance VI. If you balance Input Matrix with
    the Matrix Balance VI, wire the index high output of the Matrix Balance VI to this input. If the
    index high input of this VI equals –1 (default), the VI uses n– 1 for index high.

   •      Hessenberg Form H —

    Hessenberg Form H returns an n× nmatrix in Hessenberg form.


                                                    © National Instruments 3113

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3113 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3114 ordinal=3114 -->
## Functions

Functions

               •      Orthogonal Matrix Q —

           Orthogonal Matrix Q returns the n× northogonal matrix.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The following expression defines the Hessenberg decomposition of an n× nmatrix A:

   A= QHQH

      where Qis an orthogonal matrix when matrix Ais a real matrix and a unitary matrix
     when matrix Ais a complex matrix, QH is the conjugate transpose of matrix Q, and His
      a Hessenberg matrix.

      By definition, a Hessenberg matrix is a matrix with zeros under the main subdiagonal,
       as shown by the following matrix.


     ComplexComplex HessenbergHessenberg DecompositionDecomposition VIVI

      Performs the Hessenberg decomposition of Input Matrix. Wire data to the Input Matrix
       input to determine the polymorphic instance to use or manually select the instance.


3114   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3114 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3115 ordinal=3115 -->
## Functions

Functions


Inputs/Outputs

   •      Input Matrix —

    Input Matrix is an n× ncomplex matrix.

   •      index low —

    index low is the index low value from the Matrix Balance VI. If you balance Input Matrix with the
     Matrix Balance VI, wire the index low output of the Matrix Balance VI to this input. If the index
    low input of this VI equals –1 (default), the VI uses 0 for index low.

   •      index high —

    index high is the index high value from the Matrix Balance VI. If you balance Input Matrix with
    the Matrix Balance VI, wire the index high output of the Matrix Balance VI to this input. If the
    index high input of this VI equals –1 (default), the VI uses n– 1 for index high.

   •      Hessenberg Form H —

    Hessenberg Form H returns an n× nmatrix in Hessenberg form.

   •      Orthogonal Matrix Q —

    Orthogonal Matrix Q returns the n× nunitary matrix.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The following expression defines the Hessenberg decomposition of an n× nmatrix A:

A= QHQH

where Qis an orthogonal matrix when matrix Ais a real matrix and a unitary matrix
when matrix Ais a complex matrix, QH is the conjugate transpose of matrix Q, and His


                                                    © National Instruments 3115

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3115 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3116 ordinal=3116 -->
## Functions

Functions

      a Hessenberg matrix.

      By definition, a Hessenberg matrix is a matrix with zeros under the main subdiagonal,
       as shown by the following matrix.


    QZQZ DecompositionDecomposition

      Performs the QZ decomposition of a pair of square matrices. The data types you wire
       to the A and B inputs determine the polymorphic instance to use.


            • Real QZ Decomposition VI
            • Complex QZ Decomposition VI

      The following expressions define the QZ decomposition of a matrix pair (A, B).

     A = QHZH B = QTZH

      where A and B are n-by-nsquare matrices, ZH is the conjugate transpose of matrix Z,
   Tis an n-by-nupper triangular matrix, and His an n-by-nupper Hessenberg matrix if
       the decomposition type is Generalized Hessenberg or a quasi-triangular matrix with
       1-by-1 and 2-by-2 diagonal blocks if the decomposition type is Generalized Schur.
       Refer to the Hessenberg Decomposition VI for information about Hessenberg matrices.

           If B is singular, matrix pair (A, B) has an infinite generalized eigenvalue, in other words,

3116   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3116 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3117 ordinal=3117 -->
## Functions

Functions

Betai is zero. If αA–βB is singular for all α and β, matrix pair (A, B) is singular and has an
indeterminate generalized eigenvalue, in other words, both Betai and Alphai are zeros.
This VI cannot order the generalized eigenvalues if there are indeterminate generalized
eigenvalues.

RealReal QZQZ DecompositionDecomposition VIVI

Performs the QZ decomposition of a pair of square matrices. The data types you wire
to the A and B inputs determine the polymorphic instance to use.


Inputs/Outputs

   •     A —

   A is a square real matrix.

   •     B —

   B is the second square real matrix.

   •      decomposition type —

    decomposition type specifies the type of decomposition to perform.

    0  Generalized Hessenberg (default)
    1  Generalized Schur

   •      order —

    order specifies how to order the generalized eigenvalues, Alpha and Beta. order is available only
   when decomposition type is Generalized Schur. The default is No Reorder.

    0 No Reorder—Does not change the order of the generalized eigenvalues.


                                                    © National Instruments 3117

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3117 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3118 ordinal=3118 -->
## Functions

Functions


             Real Ascending—Lists the generalized eigenvalues in ascending order according to the real           1
               parts.
             Real Descending—Lists the generalized eigenvalues in descending order according to the real           2               parts.
            Magnitude Ascending—Lists the generalized eigenvalues in ascending order according to the           3
             magnitudes.
            Magnitude Descending—Lists the generalized eigenvalues in descending order according to           4             the magnitudes.

               •      Eigenvectors —

            Eigenvectors returns a complex matrix that contains the generalized eigenvectors in its columns.

               •    Q —

        Q is an orthogonal matrix.

         When trans(Q) is the transpose matrix of Q, Q satisfies the following conditions:
                     • trans(Q)AZ is an upper Hessenberg matrix if the decomposition type is Generalized
               Hessenberg or a quasi-triangular matrix with 1-by-1 and 2-by-2 diagonal blocks if the
               decomposition type is Generalized Schur.
                     • trans(Q)BZ is an upper triangular matrix.
               •     Z —

          Z is an orthogonal matrix.

         When trans(Q) is the transpose matrix of Q, Z satisfies the following conditions:
                     • trans(Q)AZ is an upper Hessenberg matrix if the decomposition type is Generalized
               Hessenberg or a quasi-triangular matrix with 1-by-1 and 2-by-2 diagonal blocks if the
               decomposition type is Generalized Schur.
                     • trans(Q)BZ is an upper triangular matrix.
               •      Alpha —

           Alpha returns the numerators of the generalized eigenvalues of matrix pair (A,B).

                    If Betai is nonzero, Alphai/Betai is a generalized eigenvalue of (A,B).

               •      Beta —

           Beta returns the denominators of the generalized eigenvalues of matrix pair (A,B).

                    If Betai is nonzero, Alphai/Betai is a generalized eigenvalue of (A,B).


3118   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3118 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3119 ordinal=3119 -->
## Functions

Functions

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The following expressions define the QZ decomposition of a matrix pair (A, B).

A = QHZH B = QTZH

where A and B are n-by-nsquare matrices, ZH is the conjugate transpose of matrix Z,
Tis an n-by-nupper triangular matrix, and His an n-by-nupper Hessenberg matrix if
the decomposition type is Generalized Hessenberg or a quasi-triangular matrix with
1-by-1 and 2-by-2 diagonal blocks if the decomposition type is Generalized Schur.
Refer to the Hessenberg Decomposition VI for information about Hessenberg matrices.

If B is singular, matrix pair (A, B) has an infinite generalized eigenvalue, in other words,
Betai is zero. If αA–βB is singular for all α and β, matrix pair (A, B) is singular and has an
indeterminate generalized eigenvalue, in other words, both Betai and Alphai are zeros.
This VI cannot order the generalized eigenvalues if there are indeterminate generalized
eigenvalues.

ComplexComplex QZQZ DecompositionDecomposition VIVI

Performs the QZ decomposition of a pair of square matrices. The data types you wire
to the A and B inputs determine the polymorphic instance to use.


Inputs/Outputs

   •     A —


                                                    © National Instruments 3119

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3119 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3120 ordinal=3120 -->
## Functions

Functions


          A is a square complex matrix.

               •     B —

         B is the second square complex matrix.

               •      decomposition type —

           decomposition type specifies the type of decomposition to perform.

           0  Generalized Hessenberg (default)
           1  Generalized Schur

               •      order —

            order specifies how to order the generalized eigenvalues, Alpha and Beta. order is available only
          when decomposition type is Generalized Schur. The default is No Reorder.

           0 No Reorder—Does not change the order of the generalized eigenvalues.
             Real Ascending—Lists the generalized eigenvalues in ascending order according to the real           1
               parts.
             Real Descending—Lists the generalized eigenvalues in descending order according to the real           2
               parts.
            Magnitude Ascending—Lists the generalized eigenvalues in ascending order according to the           3
             magnitudes.
            Magnitude Descending—Lists the generalized eigenvalues in descending order according to           4
             the magnitudes.

               •      Eigenvectors —

            Eigenvectors returns a complex matrix that contains the generalized eigenvectors in its columns.

               •    Q —

        Q is a unitary matrix.

         When trans(Q) is the conjugate transpose matrix of Q, Q satisfies the following conditions:
                     • trans(Q)AZ is an upper Hessenberg matrix if the decomposition type is Generalized
               Hessenberg or an upper triangular matrix if the decomposition type is Generalized Schur.
                     • trans(Q)BZ is an upper triangular matrix.
               •     Z —


3120   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3120 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3121 ordinal=3121 -->
## Functions

Functions


    Z is a unitary matrix.

   When trans(Q) is the conjugate transpose matrix of Q, Z satisfies the following conditions:
         • trans(Q)AZ is an upper Hessenberg matrix if the decomposition type is Generalized
        Hessenberg or an upper triangular matrix if the decomposition type is Generalized Schur.
         • trans(Q)BZ is an upper triangular matrix.
   •      Alpha —

    Alpha returns the numerators of the generalized eigenvalues of matrix pair (A,B).

       If Betai is nonzero, Alphai/Betai is a generalized eigenvalue of (A,B).

   •      Beta —

    Beta returns the denominators of the generalized eigenvalues of matrix pair (A,B).

       If Betai is nonzero, Alphai/Betai is a generalized eigenvalue of (A,B).

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The following expressions define the QZ decomposition of a matrix pair (A, B).

A = QHZH B = QTZH

where A and B are n-by-nsquare matrices, ZH is the conjugate transpose of matrix Z,
Tis an n-by-nupper triangular matrix, and His an n-by-nupper Hessenberg matrix if
the decomposition type is Generalized Hessenberg or a quasi-triangular matrix with
1-by-1 and 2-by-2 diagonal blocks if the decomposition type is Generalized Schur.
Refer to the Hessenberg Decomposition VI for information about Hessenberg matrices.

If B is singular, matrix pair (A, B) has an infinite generalized eigenvalue, in other words,
Betai is zero. If αA–βB is singular for all α and β, matrix pair (A, B) is singular and has an
indeterminate generalized eigenvalue, in other words, both Betai and Alphai are zeros.
This VI cannot order the generalized eigenvalues if there are indeterminate generalized
eigenvalues.


                                                    © National Instruments 3121

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3121 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3122 ordinal=3122 -->
## Functions

Functions

      SylvesterSylvester EquationsEquations

       Solves the Sylvester matrix equation. The data types you wire to the A, B, and C inputs
      determine the polymorphic instance to use.


            • Real Sylvester Equations VI
            • Complex Sylvester Equations VI

      The following equations define the Sylvester matrix equation:

       op(A)X + Xop(B) = aC

       or

       op(A)X – Xop(B) = aC

      where op(A) is A or the conjugate transpose of A, op(B) is B or the conjugate transpose
       of B, and ais a scaling factor to avoid overflow in X.

      The Sylvester matrix equation has a unique solution if and only if λ ± β ≠ 0, where λ and
     β are the eigenvalues of A and B, respectively, and the sign (+ or –) depends on the
       equation you want to solve. When the solution of the Sylvester matrix equation is not
       unique, this VI sets perturbed to TRUE and might not return the correct solution.

      RealReal SylvesterSylvester EquationsEquations VIVI

       Solves the Sylvester matrix equation. The data types you wire to the A, B, and C inputs
      determine the polymorphic instance to use.


3122   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3122 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3123 ordinal=3123 -->
## Functions

Functions


Inputs/Outputs

   •      operation A —

    operation A specifies the operation the VI performs on matrix Ain the Sylvester equation.

    0  not transposed (default)—op(A) = A
    1  transposed—op(A) = transpose of A

   •     A —

   A contains matrix Ain the Sylvester equation. A must be a square matrix or upper quasi-
     triangular matrix in canonical Schur form.

   •     B —

   B contains matrix Bin the Sylvester equation. B must be a square matrix or upper quasi-
     triangular matrix in canonical Schur form.

   •     C —

   C contains matrix Cin the Sylvester equation.

   •      sign —

    sign specifies the form of the Sylvester equation.

    0  plus (default)—op(A)X + Xop(B) = aC
    1  minus—op(A)X – Xop(B) = aC

   •      operation B —

    operation B specifies the operation the VI performs on matrix Bin the Sylvester equation.


                                                    © National Instruments 3123

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3123 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3124 ordinal=3124 -->
## Functions

Functions


           0  not transposed (default)—op(B) = B
           1  transposed—op(B) = transpose of B

               •      matrix type —

            matrix type is the type of A and B.

             Specify types for A and B to speed up the computation of X and avoid unnecessary computation.

           0   General
           3   Upper Triangular (default)

               •     X —

          X returns the solution of the Sylvester equation.

               •       scale —

             scale returns the scaling factor aof the Sylvester equation.

               •      perturbed —

           perturbed indicates whether the VI uses perturbed values to solve the equation. When
           perturbed is TRUE, the eigenvalues of A and B are common or close and indicate the solution of
            the Sylvester equation is not unique.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The following equations define the Sylvester matrix equation:

       op(A)X + Xop(B) = aC

       or

       op(A)X – Xop(B) = aC

      where op(A) is A or the conjugate transpose of A, op(B) is B or the conjugate transpose

3124   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3124 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3125 ordinal=3125 -->
## Functions

Functions

of B, and ais a scaling factor to avoid overflow in X.

The Sylvester matrix equation has a unique solution if and only if λ ± β ≠ 0, where λ and
β are the eigenvalues of A and B, respectively, and the sign (+ or –) depends on the
equation you want to solve. When the solution of the Sylvester matrix equation is not
unique, this VI sets perturbed to TRUE and might not return the correct solution.

ComplexComplex SylvesterSylvester EquationsEquations VIVI

Solves the Sylvester matrix equation. The data types you wire to the A, B, and C inputs
determine the polymorphic instance to use.


Inputs/Outputs

   •      operation A —

    operation A specifies the operation the VI performs on matrix Ain the Sylvester equation.

    0 not transposed (default)—op(A) = A
    1 transposed—op(A) = conjugate transpose of A

   •     A —

   A contains matrix Ain the Sylvester equation. A must be a square or upper-triangular matrix.

   •     B —

   B contains matrix Bin the Sylvester equation. B must be a square or upper-triangular matrix.

   •     C —

   C contains matrix Cin the Sylvester equation.


                                                    © National Instruments 3125

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3125 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3126 ordinal=3126 -->
## Functions

Functions

               •      sign —

            sign specifies the form of the Sylvester equation.

           0  plus (default)—op(A)X + Xop(B) = aC
           1  minus—op(A)X – Xop(B) = aC

               •      operation B —

            operation B specifies the operation the VI performs on matrix Bin the Sylvester equation.

           0 not transposed (default)—op(B) = B
           1 transposed—op(B) = conjugate transpose of B

               •      matrix type —

            matrix type is the type of A and B.

             Specify types for A and B to speed up the computation of X and avoid unnecessary computation.

           0   General
           3   Upper Triangular (default)

               •     X —

          X returns the solution of the Sylvester equation.

               •       scale —

             scale returns the scaling factor aof the Sylvester equation.

               •      perturbed —

           perturbed indicates whether the VI uses perturbed values to solve the equation. When
           perturbed is TRUE, the eigenvalues of A and B are common or close and indicate the solution of
            the Sylvester equation is not unique.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


3126   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3126 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3127 ordinal=3127 -->
## Functions

Functions

The following equations define the Sylvester matrix equation:

op(A)X + Xop(B) = aC

or

op(A)X – Xop(B) = aC

where op(A) is A or the conjugate transpose of A, op(B) is B or the conjugate transpose
of B, and ais a scaling factor to avoid overflow in X.

The Sylvester matrix equation has a unique solution if and only if λ ± β ≠ 0, where λ and
β are the eigenvalues of A and B, respectively, and the sign (+ or –) depends on the
equation you want to solve. When the solution of the Sylvester matrix equation is not
unique, this VI sets perturbed to TRUE and might not return the correct solution.

LyapunovLyapunov EquationsEquations

Solves the Lyapunov matrix equation. The data types you wire to the A and B inputs
determine the polymorphic instance to use.


  • Real Lyapunov Equations VI
  • Complex Lyapunov Equations VI

The following equation defines the continuous Lyapunov equation:

AX + XAH = αB

where AH is the conjugate transpose of A and α is a scaling factor used to avoid
overflow in X.

The continuous Lyapunov equation has a unique solution if and only if λi + λ*j ≠ 0 for
all eigenvalues of A, where λ* is the complex conjugate of λ.


                                                    © National Instruments 3127

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3127 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3128 ordinal=3128 -->
## Functions

Functions

      The following equation defines the discrete Lyapunov equation:

      AXAH – X = αB

      where AH is the conjugate transpose of A and α is a scaling factor used to avoid
       overflow in X.

      The discrete Lyapunov equation has a unique solution if and only if λiλ*j ≠ 1 for all
       eigenvalues of A, where λ* is the complex conjugate of λ.

      RealReal LyapunovLyapunov EquationsEquations VIVI

       Solves the Lyapunov matrix equation. The data types you wire to the A and B inputs
      determine the polymorphic instance to use.


      Inputs/Outputs

               •     A —

          A contains matrix A in the Lyapunov equation. A must be a square matrix or upper quasi-
             triangular matrix in canonical Schur form.

               •     B —

         B contains matrix B in the Lyapunov equation.

               •      matrix type —

            matrix type is the type of A.

            Set the type of A to speed up the computation of X and avoid unnecessary computation.

           0   General
           3   Upper Triangular (default)


3128   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3128 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3129 ordinal=3129 -->
## Functions

Functions

   •      equation type —

    equation type specifies the type of Lyapunov equation.

    0 Continuous (default)—Solves the continuous Lyapunov equation.
    1 Discrete—Solves the discrete Lyapunov equation.

   •     X —

    X returns the solution to the Lyapunov equation.

   •       scale —

    scale returns the scaling factor of the Lyapunov equation.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The following equation defines the continuous Lyapunov equation:

AX + XAH = αB

where AH is the conjugate transpose of A and α is a scaling factor used to avoid
overflow in X.

The continuous Lyapunov equation has a unique solution if and only if λi + λ*j ≠ 0 for
all eigenvalues of A, where λ* is the complex conjugate of λ.

The following equation defines the discrete Lyapunov equation:

AXAH – X = αB

where AH is the conjugate transpose of A and α is a scaling factor used to avoid
overflow in X.

The discrete Lyapunov equation has a unique solution if and only if λiλ*j ≠ 1 for all

                                                    © National Instruments 3129

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3129 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3130 ordinal=3130 -->
## Functions

Functions

       eigenvalues of A, where λ* is the complex conjugate of λ.

     ComplexComplex LyapunovLyapunov EquationsEquations VIVI

       Solves the Lyapunov matrix equation. The data types you wire to the A and B inputs
      determine the polymorphic instance to use.


      Inputs/Outputs

               •     A —

          A contains matrix A in the Lyapunov equation. A must be a square matrix or upper triangular
             matrix.

               •     B —

         B contains matrix B in the Lyapunov equation.

               •      matrix type —

            matrix type is the type of A.

            Set the type of A to speed up the computation of X and avoid unnecessary computation.

           0   General
           3   Upper Triangular (default)

               •      equation type —

           equation type specifies the type of Lyapunov equation.

           0 Continuous (default)—Solves the continuous Lyapunov equation.
           1 Discrete—Solves the discrete Lyapunov equation.

               •     X —


3130   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3130 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3131 ordinal=3131 -->
## Functions

Functions


    X returns the solution to the Lyapunov equation.

   •       scale —

    scale returns the scaling factor of the Lyapunov equation.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The following equation defines the continuous Lyapunov equation:

AX + XAH = αB

where AH is the conjugate transpose of A and α is a scaling factor used to avoid
overflow in X.

The continuous Lyapunov equation has a unique solution if and only if λi + λ*j ≠ 0 for
all eigenvalues of A, where λ* is the complex conjugate of λ.

The following equation defines the discrete Lyapunov equation:

AXAH – X = αB

where AH is the conjugate transpose of A and α is a scaling factor used to avoid
overflow in X.

The discrete Lyapunov equation has a unique solution if and only if λiλ*j ≠ 1 for all
eigenvalues of A, where λ* is the complex conjugate of λ.

EigenvaluesEigenvalues andand VectorsVectors

Finds the eigenvalues and right eigenvectors of the square Input Matrix. Wire data to
the Input Matrix input to determine the polymorphic instance to use or manually
select the instance.

                                                    © National Instruments 3131

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3131 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3132 ordinal=3132 -->
## Functions

Functions


            • Real Eigenvalues and Vectors VI
            • Complex Eigenvalues and Vectors VI

      Real

      The eigenvalue problem is to determine the nontrivial solutions to the equation:

    AX= λX

      where Ais an n-by-nInput Matrix, Xis a vector with nelements, and λ is a scalar. The
   nvalues of λ that satisfy the equation are the Eigenvalues of Aand the corresponding
       values of Xare the right Eigenvectors of A. A real, symmetric matrix always has real
       eigenvalues and eigenvectors. This VI returns the real eigenvalues in ascending order if
       the Input Matrix is a real symmetric matrix.

     Complex

      The eigenvalue problem is to determine the nontrivial solutions for the equation:

    AX= λX

      where Arepresents an n-by-nInput Matrix, Xrepresents a vector with nelements,
      and λ is a scalar. The nvalues of λ that satisfy the equation are the Eigenvalues of A
      and the corresponding values of Xare the right Eigenvectors of A. A Hermitian matrix
      always has real eigenvalues. This VI returns the real eigenvalues in ascending order if
       the Input Matrix is a Hermitian matrix.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Linear Algebra\Linear
        Algebra Calculator.vi
            • labview\examples\Mathematics\Differential Equations -

3132   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3132 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3133 ordinal=3133 -->
## Functions

Functions

   ODE\Linear Differential Equation Solving.vi

RealReal EigenvaluesEigenvalues andand VectorsVectors VIVI

Finds the eigenvalues and right eigenvectors of the square Input Matrix. Wire data to
the Input Matrix input to determine the polymorphic instance to use or manually
select the instance.


Inputs/Outputs

   •      Input Matrix —

    Input Matrix is an n-by-nsquare, real matrix, where nis the number of rows and columns of
    Input Matrix.

   •      matrix type —

    matrix type is the type of Input Matrix. A symmetric matrix needs less computation than an
    unsymmetrical matrix. A real, symmetric matrix always has real eigenvectors and eigenvalues.

    0     General (default)
    1     Symmetric

   •      output option —

    output option determines whether the VI computes Eigenvectors.

    0  eigenvalues
    1  eigenvalues and vectors (default)

   •      Eigenvalues —

    Eigenvalues is a complex vector of nelements, which contains all of the computed eigenvalues
     of the Input Matrix. The Input Matrix could have complex eigenvalues if it is not symmetric.

   •      Eigenvectors —


                                                    © National Instruments 3133

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3133 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3134 ordinal=3134 -->
## Functions

Functions


            Eigenvectors is an n-by-ncomplex matrix containing all of the computed Eigenvectors of the
            Input Matrix.

          The ith column of Eigenvectors is the eigenvector corresponding to the ith component of the
              vector, Eigenvalues. Each eigenvector is normalized so that its Euclidean norm equals 1. The
            Input Matrix could have complex Eigenvectors if it is not symmetric.

                    If output option is set to eigenvalues, the VI returns Eigenvectors as an empty array.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      Real

      The eigenvalue problem is to determine the nontrivial solutions to the equation:

    AX= λX

      where Ais an n-by-nInput Matrix, Xis a vector with nelements, and λ is a scalar. The
   nvalues of λ that satisfy the equation are the Eigenvalues of Aand the corresponding
       values of Xare the right Eigenvectors of A. A real, symmetric matrix always has real
       eigenvalues and eigenvectors. This VI returns the real eigenvalues in ascending order if
       the Input Matrix is a real symmetric matrix.

     Complex

      The eigenvalue problem is to determine the nontrivial solutions for the equation:

    AX= λX

      where Arepresents an n-by-nInput Matrix, Xrepresents a vector with nelements,
      and λ is a scalar. The nvalues of λ that satisfy the equation are the Eigenvalues of A
      and the corresponding values of Xare the right Eigenvectors of A. A Hermitian matrix
      always has real eigenvalues. This VI returns the real eigenvalues in ascending order if
       the Input Matrix is a Hermitian matrix.

3134   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3134 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3135 ordinal=3135 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Linear Algebra\Linear
   Algebra Calculator.vi
  • labview\examples\Mathematics\Differential Equations -
   ODE\Linear Differential Equation Solving.vi

ComplexComplex EigenvaluesEigenvalues andand VectorsVectors VIVI

Finds the eigenvalues and right eigenvectors of the square Input Matrix. Wire data to
the Input Matrix input to determine the polymorphic instance to use or manually
select the instance.


Inputs/Outputs

   •      Input Matrix —

    Input Matrix must be an n-by-nsquare, complex matrix, where nis the number of rows and
    columns of Input Matrix.

   •      matrix type —

    matrix type is the type of Input Matrix. A symmetric matrix needs less computation than an
    unsymmetrical matrix. A Hermitian matrix always has real eigenvalues.

    0     General (default)
    1     Hermitian

   •      output option —

    output option determines whether the VI computes Eigenvectors.

    0  eigenvalues


                                                    © National Instruments 3135

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3135 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3136 ordinal=3136 -->
## Functions

Functions


           1  eigenvalues and vectors (default)

               •      Eigenvalues —

            Eigenvalues is a complex vector of nelements, which contains all of the computed eigenvalues
             of the Input Matrix. The Input Matrix could have complex eigenvalues if it is not Hermitian.

               •      Eigenvectors —

            Eigenvectors is an n-by-ncomplex matrix containing all of the computed Eigenvectors of the
            Input Matrix.

          The ith column of Eigenvectors is the eigenvector corresponding to the ith component of the
              vector, Eigenvalues. Each eigenvector is normalized so that its Euclidean norm equals 1.

                    If output option is set to eigenvalues, the VI returns Eigenvectors as an empty array.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      Real

      The eigenvalue problem is to determine the nontrivial solutions to the equation:

    AX= λX

      where Ais an n-by-nInput Matrix, Xis a vector with nelements, and λ is a scalar. The
   nvalues of λ that satisfy the equation are the Eigenvalues of Aand the corresponding
       values of Xare the right Eigenvectors of A. A real, symmetric matrix always has real
       eigenvalues and eigenvectors. This VI returns the real eigenvalues in ascending order if
       the Input Matrix is a real symmetric matrix.

     Complex

      The eigenvalue problem is to determine the nontrivial solutions for the equation:


3136   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3136 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3137 ordinal=3137 -->
## Functions

Functions

AX= λX

where Arepresents an n-by-nInput Matrix, Xrepresents a vector with nelements,
and λ is a scalar. The nvalues of λ that satisfy the equation are the Eigenvalues of A
and the corresponding values of Xare the right Eigenvectors of A. A Hermitian matrix
always has real eigenvalues. This VI returns the real eigenvalues in ascending order if
the Input Matrix is a Hermitian matrix.

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Mathematics\Linear Algebra\Linear
   Algebra Calculator.vi
   • labview\examples\Mathematics\Differential Equations -
   ODE\Linear Differential Equation Solving.vi

GeneralizedGeneralized EigenvaluesEigenvalues andand VectorsVectors

Computes the generalized right eigenvalues and eigenvectors of the matrix pair A and
B. The data types you wire to the A and B inputs determine the polymorphic instance
to use.


   • Real Generalized Eigenvalues and Vectors VI
   • Complex Generalized Eigenvalues and Vectors VI

RealReal GeneralizedGeneralized EigenvaluesEigenvalues andand VectorsVectors VIVI

Computes the generalized right eigenvalues and eigenvectors of the matrix pair A and
B. The data types you wire to the A and B inputs determine the polymorphic instance
to use.


                                                    © National Instruments 3137

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3137 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3138 ordinal=3138 -->
## Functions

Functions


      Inputs/Outputs

               •     A —

          A is a square real matrix.

               •     B —

         B is the second square real matrix.

               •      output option —

           output option determines whether the VI computes Eigenvectors.

           0  eigenvalues
           1  eigenvalues and vectors (default)

               •      Eigenvalues —

            Eigenvalues returns the generalized right eigenvalues of the matrix pair A and B.

               •      Eigenvectors —

            Eigenvectors returns generalized right eigenvectors of the matrix pair A and B.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     ComplexComplex GeneralizedGeneralized EigenvaluesEigenvalues andand VectorsVectors VIVI

      Computes the generalized right eigenvalues and eigenvectors of the matrix pair A and
       B. The data types you wire to the A and B inputs determine the polymorphic instance
       to use.


3138   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3138 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3139 ordinal=3139 -->
## Functions

Functions


Inputs/Outputs

   •     A —

   A is a square complex matrix.

   •     B —

   B is the second square complex matrix.

   •      output option —

    output option determines whether the VI computes Eigenvectors.

    0  eigenvalues
    1  eigenvalues and vectors (default)

   •      Eigenvalues —

    Eigenvalues returns the generalized right eigenvalues of the matrix pair A and B.

   •      Eigenvectors —

    Eigenvectors returns generalized right eigenvectors of the matrix pair A and B.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

MatrixMatrix BalanceBalance

Balances the general matrix Input Matrix to improve the accuracy of computed
eigenvalues and eigenvectors. Wire data to the Input Matrix input to determine the
polymorphic instance to use or manually select the instance.

You can use the Eigenvalues and Vectors VI to obtain the eigenvalues and eigenvectors
of Balanced Matrix.

                                                    © National Instruments 3139

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3139 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3140 ordinal=3140 -->
## Functions

Functions


            • Real Matrix Balance VI
            • Complex Matrix Balance VI

      You can use one or both of the following similarity transformations to balance a matrix
   Aand improve the accuracy of computed eigenvalues and eigenvectors:

            • Permute matrix Ato block upper triangular form.
            • Scale matrix A' to reduce the norm of matrix A'22.

     Permuting Matrix A

      The following expression defines the permutation of matrix Ato block upper
       triangular form.


      where Pis a permutation matrix, A'11 and A'33 are upper triangular, and PT is the
       transpose of matrix P.

      The diagonal elements of A'11 and A'33 are eigenvalues of A. The central diagonal
       block A'22 starts from column(row) index low and ends in column(row) index high of
        A'. If no suitable permutation of Aexists, the following conditions are true:

            • A'22 is the whole of A.
            • index low = 0.
            • index high = n– 1.

      Scaling Matrix A'

      The following expression defines the scaling of matrix A' to reduce the norm of matrix


3140   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3140 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3141 ordinal=3141 -->
## Functions

Functions

A'22.


so that ||A"22|| < ||A'22||, which reduces the effect of rounding errors on the accuracy of
computed eigenvalues and eigenvectors.

The following block diagram illustrates using the Matrix Balance VI and the Back
Transform Eigenvectors VI in a VI that computes the eigenvalues and eigenvectors of
matrix A.


RealReal MatrixMatrix BalanceBalance VIVI

Balances the general matrix Input Matrix to improve the accuracy of computed
eigenvalues and eigenvectors. Wire data to the Input Matrix input to determine the
polymorphic instance to use or manually select the instance.

You can use the Eigenvalues and Vectors VI to obtain the eigenvalues and eigenvectors
of Balanced Matrix.


                                                    © National Instruments 3141

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3141 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3142 ordinal=3142 -->
## Functions

Functions

      Inputs/Outputs

               •      Input Matrix —

            Input Matrix is the real general matrix to balance.

               •      job —

            job specifies the type of matrix balance operation.

           0  Neither Permuted nor Scaled
           1  Permuted but not Scaled
           2  Scaled but not Permuted
           3  Both Permuted and Scaled (default)

               •      Balanced Matrix —

           Balanced Matrix contains the same eigenvalues as Input Matrix.

               •      index low —

            index low indicates the form of Balanced Matrix.

           Balanced Matrix(i, j) = 0 if i> jand 0 ≤ j< index low. If you set job to neither permuted
         nor scaled or scaled but not permuted, index low equals 0.

               •      index high —

            index high indicates the form of Balanced Matrix.

           Balanced Matrix(i, j) = 0 if i> jand index high < i≤ n– 1. If you set job to neither permuted
         nor scaled or scaled but not permuted, index high equals n– 1.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

               •      Scale —

            Scale returns details about the permutations and scaling factors.

                    If p_jis the index of the row and column interchanged with row and column jand d_jis the


3142   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3142 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3143 ordinal=3143 -->
## Functions

Functions


     scaling factor used to balance row and column j, the following equations define how the VI
    computes the values of Scale. Scalej = pj for j= 0, 1, …, ilo – 1, ihi + 1, …, n– 1 Scalej = dj for j=
      ilo, ilo + 1, …, ihi where ilo is index low and ihi is index high.


You can use one or both of the following similarity transformations to balance a matrix
Aand improve the accuracy of computed eigenvalues and eigenvectors:

   • Permute matrix Ato block upper triangular form.
   • Scale matrix A' to reduce the norm of matrix A'22.

Permuting Matrix A

The following expression defines the permutation of matrix Ato block upper
triangular form.


where Pis a permutation matrix, A'11 and A'33 are upper triangular, and PT is the
transpose of matrix P.

The diagonal elements of A'11 and A'33 are eigenvalues of A. The central diagonal
block A'22 starts from column(row) index low and ends in column(row) index high of
A'. If no suitable permutation of Aexists, the following conditions are true:

   • A'22 is the whole of A.
   • index low = 0.
   • index high = n– 1.

Scaling Matrix A'

The following expression defines the scaling of matrix A' to reduce the norm of matrix
A'22.

                                                    © National Instruments 3143

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3143 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3144 ordinal=3144 -->
## Functions

Functions


      so that ||A"22|| < ||A'22||, which reduces the effect of rounding errors on the accuracy of
      computed eigenvalues and eigenvectors.

      The following block diagram illustrates using the Matrix Balance VI and the Back
      Transform Eigenvectors VI in a VI that computes the eigenvalues and eigenvectors of
       matrix A.


     ComplexComplex MatrixMatrix BalanceBalance VIVI

       Balances the general matrix Input Matrix to improve the accuracy of computed
       eigenvalues and eigenvectors. Wire data to the Input Matrix input to determine the
      polymorphic instance to use or manually select the instance.

      You can use the Eigenvalues and Vectors VI to obtain the eigenvalues and eigenvectors
       of Balanced Matrix.


      Inputs/Outputs

               •      Input Matrix —


3144   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3144 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3145 ordinal=3145 -->
## Functions

Functions


  Input Matrix is the complex general matrix to balance.

•      job —

  job specifies the type of matrix balance operation.

  0  Neither Permuted nor Scaled
  1  Permuted but not Scaled
  2  Scaled but not Permuted
  3  Both Permuted and Scaled (default)

•      Balanced Matrix —

  Balanced Matrix contains the same eigenvalues as Input Matrix.

•      index low —

  index low indicates the form of Balanced Matrix.

  Balanced Matrix(i, j) = 0 if i> jand 0 ≤ j< index low. If you set job to neither permuted
  nor scaled or scaled but not permuted, index low equals 0.

•      index high —

  index high indicates the form of Balanced Matrix.

  Balanced Matrix(i, j) = 0 if i> jand index high < i≤ n– 1. If you set job to neither permuted
  nor scaled or scaled but not permuted, index high equals n– 1.

•       error —

  error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
  Code VI to convert the error code or warning into an error cluster.

•      Scale —

  Scale returns details about the permutations and scaling factors.

   If p_jis the index of the row and column interchanged with row and column jand d_jis the
  scaling factor used to balance row and column j, the following equations define how the VI
  computes the values of Scale. Scalej = pj for j= 0, 1, …, ilo – 1, ihi + 1, …, n– 1 Scalej = dj for j=


                                                   © National Instruments 3145

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3145 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3146 ordinal=3146 -->
## Functions

Functions


                 ilo, ilo + 1, …, ihi where ilo is index low and ihi is index high.


      You can use one or both of the following similarity transformations to balance a matrix
   Aand improve the accuracy of computed eigenvalues and eigenvectors:

            • Permute matrix Ato block upper triangular form.
            • Scale matrix A' to reduce the norm of matrix A'22.

     Permuting Matrix A

      The following expression defines the permutation of matrix Ato block upper
       triangular form.


      where Pis a permutation matrix, A'11 and A'33 are upper triangular, and PT is the
       transpose of matrix P.

      The diagonal elements of A'11 and A'33 are eigenvalues of A. The central diagonal
       block A'22 starts from column(row) index low and ends in column(row) index high of
        A'. If no suitable permutation of Aexists, the following conditions are true:

            • A'22 is the whole of A.
            • index low = 0.
            • index high = n– 1.

      Scaling Matrix A'

      The following expression defines the scaling of matrix A' to reduce the norm of matrix
       A'22.


3146   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3146 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3147 ordinal=3147 -->
## Functions

Functions


so that ||A"22|| < ||A'22||, which reduces the effect of rounding errors on the accuracy of
computed eigenvalues and eigenvectors.

The following block diagram illustrates using the Matrix Balance VI and the Back
Transform Eigenvectors VI in a VI that computes the eigenvalues and eigenvectors of
matrix A.


BackBack TransformTransform EigenvectorsEigenvectors

Transforms the eigenvectors of a balanced matrix to those of the original matrix. Wire
data to the Eigenvectors input to determine the polymorphic instance to use or
manually select the instance.

Use this VI after balancing a matrix with the Matrix Balance VI and computing the
eigenvectors of the balanced matrix with the Eigenvalues and Vectors VI.


  • Real Back Transform Eigenvectors VI
  • Complex Back Transform Eigenvectors VI

The following block diagram illustrates using the Matrix Balance VI and the Back
Transform Eigenvectors VI in a VI that computes the eigenvalues and eigenvectors of
matrix A.

                                                    © National Instruments 3147

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3147 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3148 ordinal=3148 -->
## Functions

Functions


      RealReal BackBack TransformTransform EigenvectorsEigenvectors VIVI

       Transforms the eigenvectors of a balanced matrix to those of the original matrix. Wire
       data to the Eigenvectors input to determine the polymorphic instance to use or
      manually select the instance.

      Use this VI after balancing a matrix with the Matrix Balance VI and computing the
       eigenvectors of the balanced matrix with the Eigenvalues and Vectors VI.


      Inputs/Outputs

               •      job —

            job specifies the type of matrix balance operation.

           0  Neither Permuted nor Scaled
           1  Permuted but not Scaled
           2  Scaled but not Permuted
           3  Both Permuted and Scaled (default)

               •      Eigenvectors —

            Eigenvectors contains the eigenvectors to transform in the columns of the matrix. Obtain
            Eigenvectors from the Eigenvalues and Vectors VI.


3148   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3148 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3149 ordinal=3149 -->
## Functions

Functions

   •      index low —

    index low specifies the form of the balanced matrix. Obtain index low from the Matrix Balance
      VI.

   •      index high —

    index high specifies the form of the balanced matrix. Obtain index high from the Matrix Balance
      VI.

   •       side —

    side specifies the side of Eigenvectors.

    0   Right eigenvectors (default)
    1   Left eigenvectors

   •      Scale —

    Scale contains details about the permutations and/or scaling factors used to balance the
     original general matrix. Obtain Scale from the Matrix Balance VI.

   •      Transformed Eigenvectors —

    Transformed Eigenvectors returns the transformed eigenvectors.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The following block diagram illustrates using the Matrix Balance VI and the Back
Transform Eigenvectors VI in a VI that computes the eigenvalues and eigenvectors of
matrix A.


                                                    © National Instruments 3149

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3149 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3150 ordinal=3150 -->
## Functions

Functions


     ComplexComplex BackBack TransformTransform EigenvectorsEigenvectors VIVI

       Transforms the eigenvectors of a balanced matrix to those of the original matrix. Wire
       data to the Eigenvectors input to determine the polymorphic instance to use or
      manually select the instance.

      Use this VI after balancing a matrix with the Matrix Balance VI and computing the
       eigenvectors of the balanced matrix with the Eigenvalues and Vectors VI.


      Inputs/Outputs

               •      job —

            job specifies the type of matrix balance operation.

           0  Neither Permuted nor Scaled
           1  Permuted but not Scaled
           2  Scaled but not Permuted
           3  Both Permuted and Scaled (default)

               •      Eigenvectors —

            Eigenvectors contains the eigenvectors to transform in the columns of the matrix. Obtain
            Eigenvectors from the Eigenvalues and Vectors VI.


3150   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3150 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3151 ordinal=3151 -->
## Functions

Functions

   •      index low —

    index low specifies the form of the balanced matrix. Obtain index low from the Matrix Balance
      VI.

   •      index high —

    index high specifies the form of the balanced matrix. Obtain index high from the Matrix Balance
      VI.

   •       side —

    side specifies the side of Eigenvectors.

    0   Right eigenvectors (default)
    1   Left eigenvectors

   •      Scale —

    Scale contains details about the permutations and/or scaling factors used to balance the
     original general matrix. Obtain Scale from the Matrix Balance VI.

   •      Transformed Eigenvectors —

    Transformed Eigenvectors returns the transformed eigenvectors.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The following block diagram illustrates using the Matrix Balance VI and the Back
Transform Eigenvectors VI in a VI that computes the eigenvalues and eigenvectors of
matrix A.


                                                    © National Instruments 3151

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3151 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3152 ordinal=3152 -->
## Functions

Functions


      MatrixMatrix CharacteristicCharacteristic PolynomialPolynomial

      Computes the characteristic polynomial of Input Matrix. Wire data to the Input Matrix
       input to determine the polymorphic instance to use or manually select the instance.


            • Real Characteristic Polynomial VI
            • Complex Characteristic Polynomial VI

      The characteristic polynomial of Input Matrix Ais defined as p(λ) = det(λI– A), where
     det denotes the matrix determinant. If Ais a square matrix of order n, the order of its
        characteristic polynomials is n. Moreover, the nroots of the characteristic polynomial
       are the eigenvalues of A.
      RealReal CharacteristicCharacteristic PolynomialPolynomial VIVI

      Computes the characteristic polynomial of Input Matrix. Wire data to the Input Matrix
       input to determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •      Input Matrix —


3152   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3152 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3153 ordinal=3153 -->
## Functions

Functions


    Input Matrix is the matrix for which you want to compute the characteristic polynomial. Input
    Matrix must be a square matrix.

   •       Characteristic Polynomial —

    Characteristic Polynomial returns the coefficients of the characteristic polynomial of Input
    Matrix in ascending order.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The characteristic polynomial of Input Matrix Ais defined as p(λ) = det(λI– A), where
det denotes the matrix determinant. If Ais a square matrix of order n, the order of its
characteristic polynomials is n. Moreover, the nroots of the characteristic polynomial
are the eigenvalues of A.
ComplexComplex CharacteristicCharacteristic PolynomialPolynomial VIVI

Computes the characteristic polynomial of Input Matrix. Wire data to the Input Matrix
input to determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •      Input Matrix —

    Input Matrix is the matrix for which you want to compute the characteristic polynomial. Input
    Matrix must be a square matrix.

   •       Characteristic Polynomial —

    Characteristic Polynomial returns the coefficients of the characteristic polynomial of Input
    Matrix in ascending order.

   •       error —


                                                    © National Instruments 3153

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3153 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3154 ordinal=3154 -->
## Functions

Functions


             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The characteristic polynomial of Input Matrix Ais defined as p(λ) = det(λI– A), where
     det denotes the matrix determinant. If Ais a square matrix of order n, the order of its
        characteristic polynomials is n. Moreover, the nroots of the characteristic polynomial
       are the eigenvalues of A.
      BasicBasic LinearLinear AlgebraAlgebra SubroutinesSubroutines

      Use the Basic Linear Algebra Subroutines VIs to perform standard functions for basic
       vector and matrix operations.

      The VIs on this palette can return mathematics error codes.


         Palette Object        Description

        ddot - Dot Product
                               Calculates the dot product of two real vectors.         (DBL)

        zdotu - Dot Product                               Calculates the unconjugated dot product of two complex vectors.        (CDB)

         zdotc - Dot Product
        with Conjugation     Calculates the conjugated dot product of two complex vectors.
        (CDB)

        axpy - Scalar-Vector
                               Calculates the product of a scalar and a vector.
        Product

       nrm2 - Vector
                               Calculates the Euclidean norm of a vector.
       2-Norm


3154   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3154 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3155 ordinal=3155 -->
## Functions

Functions


Palette Object        Description

                      Calculates the sum of the absolute values of elements in a vector. For
asum - Absolute                   complex vectors, the VI calculates the sum of the absolute values of the realValues Sum                  and imaginary parts of elements in a vector.


copy - Vector Copy    Replaces elements in y with elements in x.


swap - Vector Swap   Swaps elements between two vectors.


                     Rotates a set of two-element vectors based on the original x-componentsdrotm - Fast Givens
                  and y-components and on the Rotation Matrix and related parameters thatRotation (DBL)                     the drotmg - Fast Givens Rotation Parameters VI calculates.


drotmg - Fast Givens  Calculates a fast Givens rotation matrix that zeros the y component of a two-
Rotation Parameters  element real vector and calculates the related parameters. You can use the
(DBL)               output parameters in the drotm - Fast Givens Rotation (DBL) VI.


rot - Givens Rotation  Applies a Givens rotation to a set of points.


rotg - Givens                     Creates the parameters used in the rot - Givens Rotation VI.Rotation Parameters


                     For real vectors, returns the index of the element that has the maximum
amax - Max Element
                     absolute value. For complex vectors, the VI returns the index of the element
Index
                      that has the maximum sum of absolute real and imaginary parts.


                     For real vectors, returns the index of the element that has the minimum
amin - Min Element
                     absolute value. For complex vectors, the VI returns the index of the element
Index
                      that has the minimum sum of absolute real and imaginary parts.


                                                    © National Instruments 3155

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3155 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3156 ordinal=3156 -->
## Functions

Functions


         Palette Object        Description

       gemv - General
         Matrix-Vector         Calculates the product of a general matrix and a vector.
        Product

       dsymv - Symmetric
         Matrix-Vector         Calculates the product of a symmetric matrix and a vector.
        Product (DBL)

       zhemv - Hermitian
         Matrix-Vector         Calculates the product of a Hermitian matrix and a vector.
        Product (CDB)

        trmv - Triangle
         Matrix-Vector         Calculates the product of a triangular matrix and a vector.
        Product

         dsyr - Symmetric                               Calculates the rank–1 update of the upper or lower triangular component of         Matrix Rank-1
                          a symmetric matrix.        Update (DBL)

         dsyr2 - Symmetric                               Calculates the rank–2 update of the upper or lower triangular component of         Matrix Rank-2                          a symmetric matrix.
        Update (DBL)

         zher - Hermitian                               Calculates the rank–1 update of the upper or lower triangular component of         Matrix Rank-1
                          a Hermitian matrix.        Update (CDB)

        zher2 - Hermitian                               Calculates the rank–2 update of the upper or lower triangular component of         Matrix Rank-2                          a Hermitian matrix.
        Update (CDB)

        dger - General Matrix
                               Calculates the rank–1 update of a general matrix.
        Rank-1 Update (DBL)

         zgeru - General
         Matrix Rank-1         Calculates the rank–1 update of a general matrix.
        Update (CDB)

         zgerc - General
         Matrix Rank-1
                               Calculates the rank–1 conjugated update of a general matrix.
        Update with
        Conjugation (CDB)

3156   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3156 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3157 ordinal=3157 -->
## Functions

Functions


 Palette Object        Description

 trsv - Solve Linear                      Solves the linear equation op(A)*trsv = x for trsv.
 Eqs (Triangle, single)

 gemm - General
 Matrix-Matrix         Calculates the product of two general matrices.
 Product

 symm - Symmetric
 Matrix-Matrix         Calculates the product of a symmetric matrix and another matrix.
 Product

 zhemm - Hermitian
 Matrix-Matrix         Calculates the product of a Hermitian matrix and another matrix.
 Product (CDB)

 trmm - Triangle
 Matrix-Matrix         Calculates the product of a triangular matrix and another matrix.
 Product

 syrk - Symmetric                       Calculates the rank–k update of the upper or lower triangular component of
 Matrix Rank-k                   a symmetric matrix. Update

 syr2k - Symmetric
 Matrix Rank-2k        Calculates the rank–2k update of a symmetric matrix.
 Update

 zherk - Hermitian                       Calculates the rank–k update of the upper or lower triangular component of Matrix Rank-k                   a Hermitian matrix. Update (CDB)

 zher2k - Hermitian
                       Calculates the rank–2k update of the upper or lower triangular component
 Matrix Rank-2k
                       of a Hermitian matrix.
 Update (CDB)

 trsm - Solve Linear
 Eqs (Triangle,        Solves either op(A)*trsm = alpha*x or trsm*op(A) = alpha*x for trsm.
 multiple)

ddotddot -- DotDot ProductProduct (DBL)(DBL)

Calculates the dot product of two real vectors.

                                                    © National Instruments 3157

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3157 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3158 ordinal=3158 -->
## Functions

Functions


      Inputs/Outputs

               •      yInc —

            yInc determines whether the VI skips elements in y for the calculation. The default is 1, meaning
            the VI does not skip any elements in y. yInc is an optional input.

               Note If you wire a value other than the default to yInc, the VI skips elements that
                   have indexes that are multiples of the value you wire. If you wire a value that is
                      greater than or equal to the number of elements in y, the VI uses only the first
                   element in y for the calculation. If you wire a value that is less than 0, the VI reverses
                     the order of the elements before it calculates the result.

               •      xInc —

            xInc determines whether the VI skips elements in x for the calculation. The default is 1, meaning
            the VI does not skip any elements in x. xInc is an optional input.

               Note If you wire a value other than the default to xInc, the VI skips elements that
                   have indexes that are multiples of the value you wire. If you wire a value that is
                      greater than or equal to the number of elements in x, the VI uses only the first
                   element in x for the calculation. If you wire a value that is less than 0, the VI reverses
                     the order of the elements before it calculates the result.

               •      x —

           x is a real vector.

               •      y —

           y is a real vector. y must be the same size as x.

               •      ddot —

           ddot is a real scalar that returns the dot product of x and y.

               •       error —


3158   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3158 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3159 ordinal=3159 -->
## Functions

Functions


    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Linear Algebra\Comparison of
   BLAS and linear algebra VIs.vi

zdotuzdotu -- DotDot ProductProduct (CDB)(CDB)

Calculates the unconjugated dot product of two complex vectors.


Inputs/Outputs

   •      yInc —

    yInc determines whether the VI skips elements in y for the calculation. The default is 1, meaning
    the VI does not skip any elements in y. yInc is an optional input.

          Note If you wire a value other than the default to yInc, the VI skips elements that
            have indexes that are multiples of the value you wire. If you wire a value that is
              greater than or equal to the number of elements in y, the VI uses only the first
            element in y for the calculation. If you wire a value that is less than 0, the VI reverses
             the order of the elements before it calculates the result.

   •      xInc —


                                                    © National Instruments 3159

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3159 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3160 ordinal=3160 -->
## Functions

Functions


            xInc determines whether the VI skips elements in x for the calculation. The default is 1, meaning
            the VI does not skip any elements in x. xInc is an optional input.

               Note If you wire a value other than the default to xInc, the VI skips elements that
                   have indexes that are multiples of the value you wire. If you wire a value that is
                      greater than or equal to the number of elements in x, the VI uses only the first
                   element in x for the calculation. If you wire a value that is less than 0, the VI reverses
                     the order of the elements before it calculates the result.

               •      x —

           x is a complex vector.

               •      y —

           y is a complex vector. y must be the same size as x.

               •      zdotu —

           zdotu is a complex scalar that returns the unconjugated dot product of x and x.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
      more information on BLAS functions.

      zdotczdotc -- DotDot ProductProduct withwith ConjugationConjugation (CDB)(CDB)

       Calculates the conjugated dot product of two complex vectors.


3160   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3160 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3161 ordinal=3161 -->
## Functions

Functions

Inputs/Outputs

   •      yInc —

    yInc determines whether the VI skips elements in y for the calculation. The default is 1, meaning
    the VI does not skip any elements in y. yInc is an optional input.

          Note If you wire a value other than the default to yInc, the VI skips elements that
            have indexes that are multiples of the value you wire. If you wire a value that is
              greater than or equal to the number of elements in y, the VI uses only the first
            element in y for the calculation. If you wire a value that is less than 0, the VI reverses
             the order of the elements before it calculates the result.

   •      xInc —

    xInc determines whether the VI skips elements in x for the calculation. The default is 1, meaning
    the VI does not skip any elements in x. xInc is an optional input.

          Note If you wire a value other than the default to xInc, the VI skips elements that
            have indexes that are multiples of the value you wire. If you wire a value that is
              greater than or equal to the number of elements in x, the VI uses only the first
            element in x for the calculation. If you wire a value that is less than 0, the VI reverses
             the order of the elements before it calculates the result.

   •      x —

    x is a complex vector.

   •      y —

    y is a complex vector. y must be the same size as x.

   •      zdotc —

    zdotc is a complex scalar that returns the conjugated dot product of x and y.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for

                                                    © National Instruments 3161

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3161 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3162 ordinal=3162 -->
## Functions

Functions

      more information on BLAS functions.

      axpyaxpy -- Scalar-VectorScalar-Vector ProductProduct

       Calculates the product of a scalar and a vector.

      The data types you wire to the alpha, X, and Y inputs determine the polymorphic
       instance to use.


            • daxpy - Scalar-Vector Product (DBL) VI
            • zaxpy - Scalar-Vector Product (CDB) VI

       Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
      more information on BLAS functions.
   daxpydaxpy -- Scalar-VectorScalar-Vector ProductProduct (DBL)(DBL) VIVI

       Calculates the product of a scalar and a vector.

      The data types you wire to the alpha, X, and Y inputs determine the polymorphic
       instance to use.


      Inputs/Outputs

               •      yInc —

            yInc determines whether the VI skips elements in y for the calculation. The default is 1, meaning
            the VI does not skip any elements in y. yInc is an optional input.


3162   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3162 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3163 ordinal=3163 -->
## Functions

Functions


        Note If you wire a value other than the default to yInc, the VI skips elements that
          have indexes that are multiples of the value you wire. If you wire a value that is
            greater than or equal to the number of elements in y, the VI uses only the first
          element in y for the calculation. If you wire a value that is less than 0, the VI reverses
           the order of the elements before it calculates the result.

•      xInc —

  xInc determines whether the VI skips elements in x for the calculation. The default is 1, meaning
  the VI does not skip any elements in x. xInc is an optional input.

        Note If you wire a value other than the default to xInc, the VI skips elements that
          have indexes that are multiples of the value you wire. If you wire a value that is
            greater than or equal to the number of elements in x, the VI uses only the first
          element in x for the calculation. If you wire a value that is less than 0, the VI reverses
           the order of the elements before it calculates the result.

•      x —

  x is a real vector.

•      y —

  y is a real vector.

  The default is a vector with all elements equal to 0.

•      alpha —

  alpha is a real scalar that scales x.

  The default is 1.

•     daxpy —

  daxpy is a real vector of the same size as y that returns the result of alpha*x + y.

•       error —

  error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
  Code VI to convert the error code or warning into an error cluster.


                                                   © National Instruments 3163

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3163 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3164 ordinal=3164 -->
## Functions

Functions

       Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
      more information on BLAS functions.
   zaxpyzaxpy -- Scalar-VectorScalar-Vector ProductProduct (CDB)(CDB) VIVI

       Calculates the product of a scalar and a vector.

      The data types you wire to the alpha, X, and Y inputs determine the polymorphic
       instance to use.


      Inputs/Outputs

               •      yInc —

            yInc determines whether the VI skips elements in y for the calculation. The default is 1, meaning
            the VI does not skip any elements in y. yInc is an optional input.

               Note If you wire a value other than the default to yInc, the VI skips elements that
                   have indexes that are multiples of the value you wire. If you wire a value that is
                      greater than or equal to the number of elements in y, the VI uses only the first
                   element in y for the calculation. If you wire a value that is less than 0, the VI reverses
                     the order of the elements before it calculates the result.

               •      xInc —

            xInc determines whether the VI skips elements in x for the calculation. The default is 1, meaning
            the VI does not skip any elements in x. xInc is an optional input.

               Note If you wire a value other than the default to xInc, the VI skips elements that
                   have indexes that are multiples of the value you wire. If you wire a value that is
                      greater than or equal to the number of elements in x, the VI uses only the first
                   element in x for the calculation. If you wire a value that is less than 0, the VI reverses
                     the order of the elements before it calculates the result.


3164   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3164 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3165 ordinal=3165 -->
## Functions

Functions

   •      x —

    x is a complex vector.

   •      y —

    y is a complex vector.

    The default is a vector with all elements equal to 0.

   •      alpha —

    alpha is a complex scalar that scales X.

    The default is 0.

   •      zaxpy —

    zaxpy is a real vector of the same size as y that returns the result of alpha*x + y.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.

nrm2nrm2 -- VectorVector 2-Norm2-Norm

Calculates the Euclidean norm of a vector.

Wire data to the x input to determine the polymorphic instance to use or manually
select the instance.


  • dnrm2 - Vector 2-Norm (DBL) VI
  • dznrm2 - Vector 2-Norm (CDB) VI


                                                    © National Instruments 3165

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3165 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3166 ordinal=3166 -->
## Functions

Functions

       Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
      more information on BLAS functions.
   dnrm2dnrm2 -- VectorVector 2-Norm2-Norm (DBL)(DBL) VIVI

       Calculates the Euclidean norm of a vector.

       Wire data to the x input to determine the polymorphic instance to use or manually
        select the instance.


      Inputs/Outputs

               •      xInc —

            xInc determines whether the VI skips elements in x for the calculation. The default is 1, meaning
            the VI does not skip any elements in x. xInc is an optional input.

               Note If you wire a value other than the default to xInc, the VI skips elements that
                   have indexes that are multiples of the value you wire. If you wire a value that is
                      greater than or equal to the number of elements in x, the VI uses only the first
                   element in x for the calculation. If you wire a value that is less than 0, the VI reverses
                     the order of the elements before it calculates the result.

               •      x —

           x is a real vector.

               •     dnrm2 —

          dnrm2 is the Euclidean norm of x.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


3166   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3166 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3167 ordinal=3167 -->
## Functions

Functions

Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.
dznrm2dznrm2 -- VectorVector 2-Norm2-Norm (CDB)(CDB) VIVI

Calculates the Euclidean norm of a vector.

Wire data to the x input to determine the polymorphic instance to use or manually
select the instance.


Inputs/Outputs

   •      xInc —

    xInc determines whether the VI skips elements in x for the calculation. The default is 1, meaning
    the VI does not skip any elements in x. xInc is an optional input.

          Note If you wire a value other than the default to xInc, the VI skips elements that
            have indexes that are multiples of the value you wire. If you wire a value that is
              greater than or equal to the number of elements in x, the VI uses only the first
            element in x for the calculation. If you wire a value that is less than 0, the VI reverses
             the order of the elements before it calculates the result.

   •      x —

    x is a complex vector.

   •     dznrm2 —

   dznrm2 is the Euclidean norm of x.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


                                                    © National Instruments 3167

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3167 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3168 ordinal=3168 -->
## Functions

Functions

       Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
      more information on BLAS functions.

     asumasum -- AbsoluteAbsolute ValuesValues SumSum

       Calculates the sum of the absolute values of elements in a vector. For complex vectors,
       the VI calculates the sum of the absolute values of the real and imaginary parts of
      elements in a vector.

       Wire data to the x input to determine the polymorphic instance to use or manually
        select the instance.


            • dasum - Absolute Values Sum (DBL) VI
            • dzasum - Absolute Values Sum (CDB) VI

       Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
      more information on BLAS functions.
   dasumdasum -- AbsoluteAbsolute ValuesValues SumSum (DBL)(DBL) VIVI

       Calculates the sum of the absolute values of elements in a vector. For complex vectors,
       the VI calculates the sum of the absolute values of the real and imaginary parts of
      elements in a vector.

       Wire data to the x input to determine the polymorphic instance to use or manually
        select the instance.


      Inputs/Outputs

               •      xInc —

3168   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3168 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3169 ordinal=3169 -->
## Functions

Functions


    xInc determines whether the VI skips elements in x for the calculation. The default is 1, meaning
    the VI does not skip any elements in x. xInc is an optional input.

    xInc must be greater than zero.

          Note If you wire a value other than the default to xInc, the VI skips elements that
            have indexes that are multiples of the value you wire. If you wire a value that is
              greater than or equal to the number of elements in x, the VI uses only the first
            element in x for the calculation.

   •      x —

    x is a real vector.

   •     dasum —

   dasum is a real scalar that returns the sum of the absolute values of elements in x.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.
dzasumdzasum -- AbsoluteAbsolute ValuesValues SumSum (CDB)(CDB) VIVI

Calculates the sum of the absolute values of elements in a vector. For complex vectors,
the VI calculates the sum of the absolute values of the real and imaginary parts of
elements in a vector.

Wire data to the x input to determine the polymorphic instance to use or manually
select the instance.


                                                    © National Instruments 3169

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3169 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3170 ordinal=3170 -->
## Functions

Functions

      Inputs/Outputs

               •      xInc —

            xInc determines whether the VI skips elements in x for the calculation. The default is 1, meaning
            the VI does not skip any elements in x. xInc is an optional input.

            xInc must be greater than zero.

               Note If you wire a value other than the default to xInc, the VI skips elements that
                   have indexes that are multiples of the value you wire. If you wire a value that is
                      greater than or equal to the number of elements in x, the VI uses only the first
                   element in x for the calculation.

               •      x —

           x is a complex vector.

               •     dzasum —

          dzasum is a complex scalar that returns the sum of the absolute values of the real and imaginary
             parts of elements in x.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
      more information on BLAS functions.

      copycopy -- VectorVector CopyCopy

       Replaces elements in y with elements in x.

      The data types you wire to x and y determine the polymorphic instance to use.


            • dcopy - Vector Copy (DBL) VI

3170   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3170 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3171 ordinal=3171 -->
## Functions

Functions

  • zcopy - Vector Copy (CDB) VI

Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.
dcopydcopy -- VectorVector CopyCopy (DBL)(DBL) VIVI

Replaces elements in y with elements in x.

The data types you wire to x and y determine the polymorphic instance to use.


Inputs/Outputs

   •      yInc —

    yInc determines whether the VI skips elements in y for the calculation. The default is 1, meaning
    the VI does not skip any elements in y. yInc is an optional input.

          Note If you wire a value other than the default to yInc, the VI skips elements that
            have indexes that are multiples of the value you wire. If you wire a value that is
              greater than or equal to the number of elements in y, the VI uses only the first
            element in y for the calculation. If you wire a value that is less than 0, the VI reverses
             the order of the elements before it calculates the result.

   •      xInc —

    xInc determines whether the VI skips elements in x for the calculation. The default is 1, meaning
    the VI does not skip any elements in x. xInc is an optional input.

          Note If you wire a value other than the default to xInc, the VI skips elements that
            have indexes that are multiples of the value you wire. If you wire a value that is
              greater than or equal to the number of elements in x, the VI uses only the first
            element in x for the calculation. If you wire a value that is less than 0, the VI reverses


                                                    © National Instruments 3171

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3171 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3172 ordinal=3172 -->
## Functions

Functions


                     the order of the elements before it calculates the result.

               •      x —

           x is the real source vector.

               •      y —

           y is a real vector that supplies the default values for dcopy.

          The default is a vector with all elements equal to 0.

               •      dcopy —

           dcopy is a real vector of the same size as y. dcopy returns the result from copying elements of x
             to y.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
      more information on BLAS functions.
   zcopyzcopy -- VectorVector CopyCopy (CDB)(CDB) VIVI

       Replaces elements in y with elements in x.

      The data types you wire to x and y determine the polymorphic instance to use.


      Inputs/Outputs

               •      yInc —

3172   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3172 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3173 ordinal=3173 -->
## Functions

Functions


    yInc determines whether the VI skips elements in y for the calculation. The default is 1, meaning
    the VI does not skip any elements in y. yInc is an optional input.

          Note If you wire a value other than the default to yInc, the VI skips elements that
            have indexes that are multiples of the value you wire. If you wire a value that is
              greater than or equal to the number of elements in y, the VI uses only the first
            element in y for the calculation. If you wire a value that is less than 0, the VI reverses
             the order of the elements before it calculates the result.

   •      xInc —

    xInc determines whether the VI skips elements in x for the calculation. The default is 1, meaning
    the VI does not skip any elements in x. xInc is an optional input.

          Note If you wire a value other than the default to xInc, the VI skips elements that
            have indexes that are multiples of the value you wire. If you wire a value that is
              greater than or equal to the number of elements in x, the VI uses only the first
            element in x for the calculation. If you wire a value that is less than 0, the VI reverses
             the order of the elements before it calculates the result.

   •      x —

    x is the complex source vector.

   •      y —

    y is a complex vector that supplies the default values for dcopy.

    The default is a vector with all elements equal to 0.

   •      zcopy —

    zcopy is a real vector of the same size as y. zcopy returns the result from copying elements of x
    to y.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for

                                                    © National Instruments 3173

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3173 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3174 ordinal=3174 -->
## Functions

Functions

      more information on BLAS functions.

     swapswap -- VectorVector SwapSwap

      Swaps elements between two vectors.

      The data types you wire to the x and y inputs determine the polymorphic instance to
       use.


            • dswap - Vector Swap (DBL) VI
            • zswap - Vector Swap (CDB) VI

       Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
      more information on BLAS functions.
   dswapdswap -- VectorVector SwapSwap (DBL)(DBL) VIVI

      Swaps elements between two vectors.

      The data types you wire to the x and y inputs determine the polymorphic instance to
       use.


      Inputs/Outputs

               •      yInc —

            yInc determines whether the VI skips elements in y for the calculation. The default is 1, meaning
            the VI does not skip any elements in y. yInc is an optional input.


3174   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3174 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3175 ordinal=3175 -->
## Functions

Functions


          Note If you wire a value other than the default to yInc, the VI skips elements that
            have indexes that are multiples of the value you wire. If you wire a value that is
              greater than or equal to the number of elements in y, the VI uses only the first
            element in y for the calculation. If you wire a value that is less than 0, the VI reverses
             the order of the elements before it calculates the result.

   •      xInc —

    xInc determines whether the VI skips elements in x for the calculation. The default is 1, meaning
    the VI does not skip any elements in x. xInc is an optional input.

          Note If you wire a value other than the default to xInc, the VI skips elements that
            have indexes that are multiples of the value you wire. If you wire a value that is
              greater than or equal to the number of elements in x, the VI uses only the first
            element in x for the calculation. If you wire a value that is less than 0, the VI reverses
             the order of the elements before it calculates the result.

   •      x —

    x is a real vector.

   •      y —

    y is a real vector.

   •     dswap x —

   dswap x returns a real vector in which elements of y replace elements of x.

   •     dswap y —

   dswap y returns a real vector in which elements of x replace elements of y.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.


                                                    © National Instruments 3175

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3175 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3176 ordinal=3176 -->
## Functions

Functions

   zswapzswap -- VectorVector SwapSwap (CDB)(CDB) VIVI

      Swaps elements between two vectors.

      The data types you wire to the x and y inputs determine the polymorphic instance to
       use.


      Inputs/Outputs

               •      yInc —

            yInc determines whether the VI skips elements in y for the calculation. The default is 1, meaning
            the VI does not skip any elements in y. yInc is an optional input.

               Note If you wire a value other than the default to yInc, the VI skips elements that
                   have indexes that are multiples of the value you wire. If you wire a value that is
                      greater than or equal to the number of elements in y, the VI uses only the first
                   element in y for the calculation. If you wire a value that is less than 0, the VI reverses
                     the order of the elements before it calculates the result.

               •      xInc —

            xInc determines whether the VI skips elements in x for the calculation. The default is 1, meaning
            the VI does not skip any elements in x. xInc is an optional input.

               Note If you wire a value other than the default to xInc, the VI skips elements that
                   have indexes that are multiples of the value you wire. If you wire a value that is
                      greater than or equal to the number of elements in x, the VI uses only the first
                   element in x for the calculation. If you wire a value that is less than 0, the VI reverses
                     the order of the elements before it calculates the result.

               •      x —

           x is a complex vector.


3176   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3176 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3177 ordinal=3177 -->
## Functions

Functions

   •      y —

    y is a complex vector.

   •     zswap x —

    zswap x returns a complex vector in which elements of y replace elements of x.

   •     zswap y —

    zswap y returns a complex vector in which elements of x replace elements of y.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.

drotmdrotm -- FastFast GivensGivens RotationRotation (DBL)(DBL)

Rotates a set of two-element vectors based on the original x-components and y-
components and on the Rotation Matrix and related parameters that the drotmg - Fast
Givens Rotation Parameters VI calculates.


Inputs/Outputs

   •      yInc —

    yInc determines whether the VI skips elements in y in. The default is 1, meaning the VI does not
    skip any elements in y in.


                                                    © National Instruments 3177

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3177 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3178 ordinal=3178 -->
## Functions

Functions


               Note If you wire a value besides 1 to yInc, the VI uses only the elements that have
                     indexes that are multiples of the number you wire. If yInc is less than 0, the VI
                      reverses the order of the elements in y in. yInc cannot be 0.

               •      xInc —

            xInc determines whether the VI skips elements in x in. The default is 1, meaning the VI does not
             skip any elements in x in.

               Note If you wire a value besides 1 to xInc, the VI uses only the elements that have
                     indexes that are multiples of the number you wire. If xInc is less than 0, the VI
                      reverses the order of the elements in x in. xInc cannot be 0.

               •      x in —

           x in is a real vector that contains the x-components of a set of two-element vectors.

               •      y in —

           y in is a real vector that contains the y-components of a set of two-element vectors.

               •       rotation matrix flag —

             rotation matrix flag specifies the flag that determines the structure for certain elements in
            Rotation Matrix.

               •      Rotation Matrix —

            Rotation Matrix is the 2 × 2 fast Givens rotation matrix.

               •      x out —

           x out is a real vector that contains the x-components of the set of two-element vectors after the
              rotation.

               •      y out —

           y out is a real vector that contains the y-components of the set of two-element vectors after the
              rotation.

               •       error —


3178   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3178 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3179 ordinal=3179 -->
## Functions

Functions


    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Linear Algebra\QR
   decomposition update by Givens rotation.vi

drotmgdrotmg -- FastFast GivensGivens RotationRotation ParametersParameters (DBL)(DBL)

Calculates a fast Givens rotation matrix that zeros the y component of a two-element
real vector and calculates the related parameters. You can use the output parameters
in the drotm - Fast Givens Rotation (DBL) VI.


Inputs/Outputs

   •      x —

    x is the real input x-component for the two-element vector.

   •      y —

    y is the real input y-component for the two-element vector.

   •     d1 in —

    d1 in is the real scale factor for x.


                                                    © National Instruments 3179

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3179 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3180 ordinal=3180 -->
## Functions

Functions

               •     d2 in —

          d2 in is the real scale factor for y.

               •       rotation matrix flag —

             rotation matrix flag returns the flag that describes the form of Rotation Matrix.

             rotation matrix flag returns –2, –1, 0, or 1.

               •        r —

               r returns the x-component after the Givens rotation.

               •     d1 out —

          d1 out returns the updated scale factor of the x-component.

               •     d2 out —

          d2 out returns the updated scale factor of the y-component.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

               •      Rotation Matrix —

            Rotation Matrix returns the 2 × 2 fast Givens rotation matrix.


      The VI calculates the fast Givens rotation parameters using the following equation:


      where His the fast Givens rotation matrix.

      The fast Givens rotation matrix and scale parameters must satisfy the following
       equation:


3180   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3180 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3181 ordinal=3181 -->
## Functions

Functions

The rotation matrix flag determines the structure and value of certain elements in
Rotation Matrix Has follows:


 If rotation matrix flag is 1, H=

 If rotation matrix flag is 0, H=

 If rotation matrix flag is –1, H=

 If rotation matrix flag is –2, H=

where h11,h12,h21,and h22 are elements in Rotation Matrix.

Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Linear Algebra\QR
   decomposition update by Givens rotation.vi

rotrot -- GivensGivens RotationRotation

Applies a Givens rotation to a set of points.

The data types you wire to x in and y in determine the polymorphic instance to use.


  • drot - Givens Rotation (DBL) VI
  • zdrot - Givens Rotation (CDB) VI


                                                    © National Instruments 3181

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3181 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3182 ordinal=3182 -->
## Functions

Functions

            Tip When performing a series of Givens rotation operations, consider using
              the fast Givens rotation instead of the Givens Rotation for better
              performance. You also can use the fast Givens rotation to compute the QR
              Decomposition.

       Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
      more information on BLAS functions.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Linear Algebra\QR
        decomposition update by Givens rotation.vi
    drotdrot -- GivensGivens RotationRotation (DBL)(DBL) VIVI

       Applies a Givens rotation to a set of points.

      The data types you wire to x in and y in determine the polymorphic instance to use.


      Inputs/Outputs

               •      yInc —

            yInc determines whether the VI skips elements in y in. The default is 1, meaning the VI does not
             skip any elements in y in.

               Note If you wire a value besides 1 to yInc, the VI uses only the elements that have
                     indexes that are multiples of the number you wire. If yInc is less than 0, the VI


3182   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3182 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3183 ordinal=3183 -->
## Functions

Functions


           reverses the order of the elements in y in. yInc cannot be 0.

•      xInc —

  xInc determines whether the VI skips elements in x in. The default is 1, meaning the VI does not
  skip any elements in x in.

        Note If you wire a value besides 1 to xInc, the VI uses only the elements that have
           indexes that are multiples of the number you wire. If xInc is less than 0, the VI
           reverses the order of the elements in x in. xInc cannot be 0.

•      x in —

  x in is a real vector that contains the x-components of a set of two-element vectors.

•      y in —

  y in is a real vector that contains the y-components of a set of two-element vectors.

•      c —

  c specifies the cparameter of the Givens rotation.

  You can use the rotg – Givens Rotation Parameters VI to obtain the value for c.

•       s —

  s specifies the sparameter of the Givens rotation.

  You can use the rotg – Givens Rotation Parameters VI to obtain the value for s.

•      x out —

  x out is a real vector that contains the x-components of the set of two-element vectors after the
  rotation.

•      y out —

  y out is a real vector that contains the y-components of the set of two-element vectors after the
  rotation.

•       error —


                                                   © National Instruments 3183

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3183 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3184 ordinal=3184 -->
## Functions

Functions


             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


            Tip When performing a series of Givens rotation operations, consider using
              the fast Givens rotation instead of the Givens Rotation for better
              performance. You also can use the fast Givens rotation to compute the QR
              Decomposition.

       Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
      more information on BLAS functions.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Linear Algebra\QR
        decomposition update by Givens rotation.vi
    zdrotzdrot -- GivensGivens RotationRotation (CDB)(CDB) VIVI

       Applies a Givens rotation to a set of points.

      The data types you wire to x in and y in determine the polymorphic instance to use.


      Inputs/Outputs

               •      yInc —


3184   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3184 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3185 ordinal=3185 -->
## Functions

Functions


  yInc determines whether the VI skips elements in y in. The default is 1, meaning the VI does not
  skip any elements in y in.

        Note If you wire a value besides 1 to yInc, the VI uses only the elements that have
           indexes that are multiples of the number you wire. If yInc is less than 0, the VI
           reverses the order of the elements in y in. yInc cannot be 0.

•      xInc —

  xInc determines whether the VI skips elements in x in. The default is 1, meaning the VI does not
  skip any elements in x in.

        Note If you wire a value besides 1 to xInc, the VI uses only the elements that have
           indexes that are multiples of the number you wire. If xInc is less than 0, the VI
           reverses the order of the elements in x in. xInc cannot be 0.

•      x in —

  x in is a complex vector that contains the x-components of a set of two-element vectors.

•      y in —

  y in is a complex vector that contains the y-components of a set of two-element vectors.

•      c —

  c specifies the cparameter of the Givens rotation.

  You can use the rotg – Givens Rotation Parameters VI to obtain the value for c.

•       s —

  s specifies the sparameter of the Givens rotation.

  You can use the rotg – Givens Rotation Parameters VI to obtain the value for s.

•      x out —

  x out is a complex vector that contains the x-components of the set of two-element vectors after
  the rotation.

•      y out —


                                                   © National Instruments 3185

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3185 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3186 ordinal=3186 -->
## Functions

Functions


           y out is a complex vector that contains the y-components of the set of two-element vectors after
            the rotation.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


            Tip When performing a series of Givens rotation operations, consider using
              the fast Givens rotation instead of the Givens Rotation for better
              performance. You also can use the fast Givens rotation to compute the QR
              Decomposition.

       Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
      more information on BLAS functions.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Linear Algebra\QR
        decomposition update by Givens rotation.vi

       rotgrotg -- GivensGivens RotationRotation ParametersParameters

       Creates the parameters used in the rot - Givens Rotation VI.

      You can use a Givens rotation to zero the input y-component. The data types you wire
       to the x and y inputs determine the polymorphic instance to use.


            • drotg - Givens Rotation Parameters (DBL) VI
            • zrotg - Givens Rotation Parameters (CDB) VI


3186   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3186 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3187 ordinal=3187 -->
## Functions

Functions

Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Linear Algebra\QR
   decomposition update by Givens rotation.vi
drotgdrotg -- GivensGivens RotationRotation ParametersParameters (DBL)(DBL) VIVI

Creates the parameters used in the rot - Givens Rotation VI.

You can use a Givens rotation to zero the input y-component. The data types you wire
to the x and y inputs determine the polymorphic instance to use.


Inputs/Outputs

   •      x —

    x is the real input x-component for the two-element vector.

   •      y —

    y is the real input y-component for the two-element vector.

   •        r —

     r returns the x-component after the Givens rotation.

   •      c —

    c returns the cparameter of the Givens rotation.


                                                    © National Instruments 3187

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3187 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3188 ordinal=3188 -->
## Functions

Functions

               •       s —

             s returns the sparameter of the Givens rotation.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

               •      z —

            z returns the zparameter of the Givens rotation.

               Note You can use z to reconstruct Givens rotation parameters c and s.


       Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
      more information on BLAS functions.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Linear Algebra\QR
        decomposition update by Givens rotation.vi
    zrotgzrotg -- GivensGivens RotationRotation ParametersParameters (CDB)(CDB) VIVI

       Creates the parameters used in the rot - Givens Rotation VI.

      You can use a Givens rotation to zero the input y-component. The data types you wire
       to the x and y inputs determine the polymorphic instance to use.


3188   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3188 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3189 ordinal=3189 -->
## Functions

Functions

Inputs/Outputs

   •      x —

    x is the complex input x-component for the two-element vector.

   •      y —

    y is the complex input y-coordinate for the two-element vector.

   •        r —

     r returns the x-coordinate after the Givens rotation.

   •      c —

    c returns the cparameter of the Givens rotation.

   •       s —

    s returns the sparameter of the Givens rotation.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

   •      z —

    z returns the zparameter of the Givens rotation.

          Note You can use z to reconstruct Givens rotation parameters c and s.


Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Linear Algebra\QR


                                                    © National Instruments 3189

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3189 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3190 ordinal=3190 -->
## Functions

Functions

        decomposition update by Givens rotation.vi

     amaxamax -- MaxMax ElementElement IndexIndex

       For real vectors, returns the index of the element that has the maximum absolute
       value. For complex vectors, the VI returns the index of the element that has the
     maximum sum of absolute real and imaginary parts.

       Wire data to the x input to determine the polymorphic instance to use or manually
        select the instance.


            • idamax - Max Element Index (DBL) VI
            • izamax - Max Element Index (CDB) VI

       Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
      more information on BLAS functions.
   idamaxidamax -- MaxMax ElementElement IndexIndex (DBL)(DBL) VIVI

       For real vectors, returns the index of the element that has the maximum absolute
       value. For complex vectors, the VI returns the index of the element that has the
     maximum sum of absolute real and imaginary parts.

       Wire data to the x input to determine the polymorphic instance to use or manually
        select the instance.


      Inputs/Outputs

               •      xInc —


3190   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3190 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3191 ordinal=3191 -->
## Functions

Functions


    xInc determines whether the VI skips elements in x for the calculation. The default is 1, meaning
    the VI does not skip any elements in x. xInc is an optional input.

    xInc must be greater than zero.

          Note If you wire a value other than the default to xInc, the VI skips elements that
            have indexes that are multiples of the value you wire. If you wire a value that is
              greater than or equal to the number of elements in x, the VI uses only the first
            element in x for the calculation.

   •      x —

    x is a real vector.

   •     idamax —

    idamax returns the index of the element in x that has the maximum absolute value.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.
izamaxizamax -- MaxMax ElementElement IndexIndex (CDB)(CDB) VIVI

For real vectors, returns the index of the element that has the maximum absolute
value. For complex vectors, the VI returns the index of the element that has the
maximum sum of absolute real and imaginary parts.

Wire data to the x input to determine the polymorphic instance to use or manually
select the instance.


                                                    © National Instruments 3191

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3191 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3192 ordinal=3192 -->
## Functions

Functions

      Inputs/Outputs

               •      xInc —

            xInc determines whether the VI skips elements in x for the calculation. The default is 1, meaning
            the VI does not skip any elements in x. xInc is an optional input.

            xInc must be greater than zero.

               Note If you wire a value other than the default to xInc, the VI skips elements that
                   have indexes that are multiples of the value you wire. If you wire a value that is
                      greater than or equal to the number of elements in x, the VI uses only the first
                   element in x for the calculation.

               •      x —

           x is a complex vector.

               •      izamax —

           izamax returns the index of the element in x that has the maximum sum of absolute real and
            imaginary parts.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
      more information on BLAS functions.

     aminamin -- MinMin ElementElement IndexIndex

       For real vectors, returns the index of the element that has the minimum absolute
       value. For complex vectors, the VI returns the index of the element that has the
     minimum sum of absolute real and imaginary parts.

       Wire data to the x input to determine the polymorphic instance to use or manually
        select the instance.


3192   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3192 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3193 ordinal=3193 -->
## Functions

Functions


  • idamin - Min Element Index (DBL) VI
  • izamin - Min Element Index (CDB) VI

Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.
idaminidamin -- MinMin ElementElement IndexIndex (DBL)(DBL) VIVI

For real vectors, returns the index of the element that has the minimum absolute
value. For complex vectors, the VI returns the index of the element that has the
minimum sum of absolute real and imaginary parts.

Wire data to the x input to determine the polymorphic instance to use or manually
select the instance.


Inputs/Outputs

   •      xInc —

    xInc determines whether the VI skips elements in x for the calculation. The default is 1, meaning
    the VI does not skip any elements in x. xInc is an optional input.

    xInc must be greater than zero.

          Note If you wire a value other than the default to xInc, the VI skips elements that
            have indexes that are multiples of the value you wire. If you wire a value that is
              greater than or equal to the number of elements in x, the VI uses only the first
            element in x for the calculation.

   •      x —

    x is a real vector.


                                                    © National Instruments 3193

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3193 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3194 ordinal=3194 -->
## Functions

Functions

               •      idamin —

           idamin returns the index of the element in x that has the minimum absolute value.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
      more information on BLAS functions.
   izaminizamin -- MinMin ElementElement IndexIndex (CDB)(CDB) VIVI

       For real vectors, returns the index of the element that has the minimum absolute
       value. For complex vectors, the VI returns the index of the element that has the
     minimum sum of absolute real and imaginary parts.

       Wire data to the x input to determine the polymorphic instance to use or manually
        select the instance.


      Inputs/Outputs

               •      xInc —

            xInc determines whether the VI skips elements in x for the calculation. The default is 1, meaning
            the VI does not skip any elements in x. xInc is an optional input.

            xInc must be greater than zero.

               Note If you wire a value other than the default to xInc, the VI skips elements that
                   have indexes that are multiples of the value you wire. If you wire a value that is
                      greater than or equal to the number of elements in x, the VI uses only the first
                   element in x for the calculation.


3194   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3194 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3195 ordinal=3195 -->
## Functions

Functions

   •      x —

    x is a complex vector.

   •      izamin —

    izamin returns the index of the element in x that has the minimum sum of absolute real and
    imaginary parts.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.

gemvgemv -- GeneralGeneral Matrix-VectorMatrix-Vector ProductProduct

Calculates the product of a general matrix and a vector.

The data types you wire to the A, x, and y inputs determine the polymorphic instance
to use.


  • dgemv - General Matrix-Vector Product (DBL) VI
  • zgemv - General Matrix-Vector Product (CDB) VI

Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Linear Algebra\Comparison of
   BLAS and linear algebra VIs.vi

                                                    © National Instruments 3195

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3195 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3196 ordinal=3196 -->
## Functions

Functions

   dgemvdgemv -- GeneralGeneral Matrix-VectorMatrix-Vector ProductProduct (DBL)(DBL)
    VIVI

       Calculates the product of a general matrix and a vector.

      The data types you wire to the A, x, and y inputs determine the polymorphic instance
       to use.


      Inputs/Outputs

               •      operation A —

            operation A specifies the operation the VI performs on matrix A, resulting in matrix op(A).

           0   Direct (default)
           1   Conjugated & Transposed
           2   Transposed

               •     A —

          A is a real matrix such that op(A) has dimensions N× M.

               •      x —

           x is a real vector.

          The VI multiplies the first Melements in x by op(A). x must have at least Melements.

               •      y —

           y is a real vector.


3196   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3196 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3197 ordinal=3197 -->
## Functions

Functions


    y must have at least as many elements as op(A)*x. The default is an N-element vector with all
    elements equal to 0.

   •      alpha —

    alpha is a real scalar that scales op(A)*x. The default is 1.

   •      beta —

    beta is a real scalar that scales y. The default is 1.

   •     dgemv —

   dgemv is a real vector of the same size as y.

    For the first Nelements, the VI returns the results of alpha*op(A)*x + beta*y. For any remaining
    elements, the VI returns the value of the element in y with the same index.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Linear Algebra\Comparison of
   BLAS and linear algebra VIs.vi
zgemvzgemv -- GeneralGeneral Matrix-VectorMatrix-Vector ProductProduct (CDB)(CDB)
VIVI

Calculates the product of a general matrix and a vector.


                                                    © National Instruments 3197

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3197 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3198 ordinal=3198 -->
## Functions

Functions

      The data types you wire to the A, x, and y inputs determine the polymorphic instance
       to use.


      Inputs/Outputs

               •      operation A —

            operation A specifies the operation the VI performs on matrix A, resulting in matrix op(A).

           0   Direct (default)
           1   Conjugated & Transposed
           2   Transposed

               •     A —

          A is a complex matrix such that op(A) has dimensions N× M.

               •      x —

           x is a complex vector.

          The VI multiplies the first Melements in x by op(A). x must have at least Melements.

               •      y —

           y is a complex vector.

           y must have at least as many elements as op(A)*x. The default is an N-element vector with all
           elements equal to 0.

               •      alpha —

           alpha is a complex scalar that scales op(A)*x. The default is 1.

               •      beta —


3198   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3198 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3199 ordinal=3199 -->
## Functions

Functions


    beta is a complex scalar that scales y.

    The default is 1.

   •     zgemv —

   zgemv is a complex vector of the same size as y.

    For the first Nelements, the VI returns the results of alpha*op(A)*x + beta*y. For any remaining
    elements, the VI returns the value of the element in y with the same index.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Linear Algebra\Comparison of
   BLAS and linear algebra VIs.vi

dsymvdsymv -- SymmetricSymmetric Matrix-VectorMatrix-Vector ProductProduct (DBL)(DBL)

Calculates the product of a symmetric matrix and a vector.


Inputs/Outputs

   •     A —

                                                    © National Instruments 3199

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3199 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3200 ordinal=3200 -->
## Functions

Functions


          A is a real symmetric matrix.

          The VI multiplies the first Nrows and Ncolumns of the triangular component of A that you
             select for matrix A type by X, where Nis the number of elements in X. A must have at least N
           rows and Ncolumns.

               •      x —

           x is an N–element real vector.

               •      y —

           y is a real vector with at least Nelements.

          The default is a vector with Nelements, all equal to 0.

               •      matrix A type —

            matrix A type specifies whether the VI uses the upper or lower triangular component of A for the
              calculation.

           2 Lower Triangular—The VI uses the lower triangular component of A for the calculation.
           Upper Triangular (default)—The VI uses the upper triangular component of A for the           3               calculation.

               •      alpha —

           alpha is a real scalar that scales A*x. The default is 1.

               •      beta —

           beta is a real scalar that scales y. The default is 1.

               •     dsymv —

          dsymv is a real vector of the same size as y.

            For the first Nelements, dsymv returns the result of alpha*A*x + beta*y. For any remaining
            elements, dsymv returns the value of the element in y with the same index.

               •       error —


3200   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3200 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3201 ordinal=3201 -->
## Functions

Functions


    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.

zhemvzhemv -- HermitianHermitian Matrix-VectorMatrix-Vector ProductProduct (CDB)(CDB)

Calculates the product of a Hermitian matrix and a vector.


Inputs/Outputs

   •     A —

   A is a Hermitian matrix.

    The VI multiplies the first Nrows and the first Ncolumns of the upper or lower triangular
    component of A by X, where Nis the number of elements in X. The number of rows and columns
     in A must be greater than or equal to N.

   •      x —

    x is an N–element complex vector.

   •      y —

    y is a complex vector of at least as many elements as x.

    The default is a vector with Nelements, all equal to 0.

   •      matrix A type —

    matrix A type specifies whether the VI uses the upper or lower triangular part of A for the


                                                    © National Instruments 3201

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3201 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3202 ordinal=3202 -->
## Functions

Functions


              calculation.

           Lower Triangular—The VI uses only the lower triangular component of the input matrix for the
           2               calculation.
           Upper Triangular (default)—The VI uses only the upper triangular component of the input           3              matrix for the calculation.

               •      alpha —

           alpha is a complex scalar that scales A*x. The default is 1.

               •      beta —

           beta is a complex scale that scales y. The default is 1.

               •     zhemv —

          zhemv is a complex vector with the same number of elements as y that returns the result of
           alpha*A*x + beta*y.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
      more information on BLAS functions.

      trmvtrmv -- TriangleTriangle Matrix-VectorMatrix-Vector ProductProduct

       Calculates the product of a triangular matrix and a vector.

      The data types you wire to the A and x inputs determine the polymorphic instance to
       use.


            • dtrmv - Triangle Matrix-Vector Product (DBL) VI

3202   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3202 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3203 ordinal=3203 -->
## Functions

Functions

  • ztrmv - Triangle Matrix-Vector Product (CDB) VI

Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.
dtrmvdtrmv -- TriangleTriangle Matrix-VectorMatrix-Vector ProductProduct (DBL)(DBL)
VIVI

Calculates the product of a triangular matrix and a vector.

The data types you wire to the A and x inputs determine the polymorphic instance to
use.


Inputs/Outputs

   •      operation A —

    operation A specifies the operation the VI performs on matrix A, resulting in matrix op(A).

    0   Direct (default)
    1   Conjugated & Transposed
    2   Transposed

   •     A —

   A is a real triangular matrix.

    The VI multiplies the first Nrows and the first Ncolumns of op(A) by x, where Nequals the
   number of elements in x. The number of rows and columns in op(A) must be greater than or
    equal to N.

   •      x —


                                                    © National Instruments 3203

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3203 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3204 ordinal=3204 -->
## Functions

Functions


           x is an N–element real vector.

               •      matrix A type —

            matrix A type specifies whether A is an upper or lower triangular matrix.

           2 Lower Triangular—A is a lower triangular matrix.
           3 Upper Triangular (default)—A is an upper triangular matrix.

               •      diagonal —

            diagonal specifies the value of the diagonal elements of A.

           0 Non-unit (default)—The VI uses the original diagonal elements of A.
           1 Unit—The VI uses a value of 1 for all diagonal elements of A.

               •     dtrmv —

          dtrmv is a real vector of the same size as x that returns the result of op(A)*x.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
      more information on BLAS functions.
   ztrmvztrmv -- TriangleTriangle Matrix-VectorMatrix-Vector ProductProduct (CDB)(CDB)
    VIVI

       Calculates the product of a triangular matrix and a vector.

      The data types you wire to the A and x inputs determine the polymorphic instance to
       use.


3204   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3204 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3205 ordinal=3205 -->
## Functions

Functions


Inputs/Outputs

   •      operation A —

    operation A specifies the operation the VI performs on matrix A, resulting in matrix op(A).

    0   Direct (default)
    1   Conjugated & Transposed
    2   Transposed

   •     A —

   A is a complex triangular matrix.

    The VI multiplies the first Nrows and the first Ncolumns of op(A) by x, where Nequals the
   number of elements in x. The number of rows and columns in op(A) must be greater than or
    equal to N.

   •      x —

    x is an N–element complex vector.

   •      matrix A type —

    matrix A type specifies whether A is an upper or lower triangular matrix.

    2 Lower Triangular—A is a lower triangular matrix.
    3 Upper Triangular (default)—A is an upper triangular matrix.

   •      diagonal —

    diagonal specifies the value of the diagonal elements of A.

    0 Non-unit (default)—The VI uses the original diagonal elements of A.
    1 Unit—The VI uses a value of 1 for all diagonal elements of A.

   •      ztrmv —

                                                    © National Instruments 3205

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3205 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3206 ordinal=3206 -->
## Functions

Functions


           ztrmv is a complex vector of the same size as x that returns the result of op(A)*x.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
      more information on BLAS functions.

      dsyrdsyr -- SymmetricSymmetric MatrixMatrix Rank-1Rank-1 UpdateUpdate (DBL)(DBL)

       Calculates the rank–1 update of the upper or lower triangular component of a
      symmetric matrix.


      Inputs/Outputs

               •      x —

           x is an N–element real vector.

               •     A —

          A is a real symmetric matrix.

          The VI updates only the upper or lower triangular component of A, depending on what you
             select for matrix A type. A must have at least Nrows and Ncolumns. The default is an N× N
            matrix with zero values for all elements.

               •      matrix A type —

            matrix A type specifies whether to update the upper or lower triangular component of A.

           2 Lower Triangular—The VI uses only the lower triangular component of A to calculate the


3206   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3206 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3207 ordinal=3207 -->
## Functions

Functions


     update.
     Upper Triangular (default)—The VI uses only the upper triangular component of A to calculate    3     the update.

   •      alpha —

    alpha is a real scalar that scales x*x^T, where x^T is the same as x transposed.

   •      dsyr —

    dsyr is a real matrix of the same dimensions as A.

    For the elements in the first Nrows and Ncolumns of the triangular component you select for
    matrix A type, dsyr returns the results of the calculation. For any remaining elements, dsyr
    returns the value of the element in A with the same index.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.

dsyr2dsyr2 -- SymmetricSymmetric MatrixMatrix Rank-2Rank-2 UpdateUpdate (DBL)(DBL)

Calculates the rank–2 update of the upper or lower triangular component of a
symmetric matrix.


Inputs/Outputs

   •      x —


                                                    © National Instruments 3207

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3207 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3208 ordinal=3208 -->
## Functions

Functions


           x is an N-element real vector.

               •      y —

           y is an N-element real vector.

               •     A —

          A is a real symmetric matrix of at least Nrows and Ncolumns.

          The VI updates either the upper or lower triangular component of A, depending on what you
             select for matrix A type. The default is an N×Nmatrix with all elements equal to 0.

               •      matrix A type —

            matrix A type specifies whether to update the upper or lower triangular component of A.

           Lower Triangular—The VI uses only the lower triangular component of A to calculate the
           2             update.
           Upper Triangular (default)—The VI uses only the upper triangular component of A to calculate
           3             the update.

               •      alpha —

           alpha is the real scale factor for x*y^T and y*x^T, where x^T is the same as x transposed. The
             default is 1.

               •      dsyr2 —

            dsyr2 is a real matrix of the same dimensions as A.

            For the elements in the first Nrows and Ncolumns of the triangular component you select for
            matrix A type, dsyr2 returns the results of the calculation. For any remaining elements, dsyr2
             returns the value of the element in A with the same index.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for

3208   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3208 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3209 ordinal=3209 -->
## Functions

Functions

more information on BLAS functions.

zherzher -- HermitianHermitian MatrixMatrix Rank-1Rank-1 UpdateUpdate (CDB)(CDB)

Calculates the rank–1 update of the upper or lower triangular component of a
Hermitian matrix.


Inputs/Outputs

   •      x —

    x is an N–element complex vector.

   •     A —

   A is a Hermitian matrix of dimensions N× N.

   •      matrix A type —

    matrix A type specifies whether to update the upper or lower triangular component of A.

     Lower Triangular—The VI uses only the lower triangular component of A to calculate the
    2     update.
     Upper Triangular (default)—The VI uses only the upper triangular component of A to calculate
    3
     the update.

   •      alpha —

    alpha is a real scalar that scales x*x^H, where x^H represents the conjugate transpose of x. The
     default is 1.

   •      zher —

    zher is a complex matrix of the same dimensions as A.

    For the elements in the first Nrows and Ncolumns of the triangular component you select for


                                                    © National Instruments 3209

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3209 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3210 ordinal=3210 -->
## Functions

Functions


            matrix A type, zher returns the results of the calculation. For any remaining elements, zher
             returns the value of the element in A with the same index.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
      more information on BLAS functions.

      zher2zher2 -- HermitianHermitian MatrixMatrix Rank-2Rank-2 UpdateUpdate (CDB)(CDB)

       Calculates the rank–2 update of the upper or lower triangular component of a
       Hermitian matrix.


      Inputs/Outputs

               •      x —

           x is an N–element vector.

               •      y —

           y is an N–element vector.

               •     A —

          A is a Hermitian matrix of at least Nrows and Ncolumns.

          The default is an N×Nmatrix with all elements equal to 0.

               •      matrix A type —


3210   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3210 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3211 ordinal=3211 -->
## Functions

Functions


    matrix A type specifies whether to update the upper or lower triangular component of A.

     Lower Triangular—The VI uses only the lower triangular component of A to calculate the
    2     update.
     Upper Triangular (default)—The VI uses only the upper triangular component of A to calculate    3     the update.

   •      alpha —

    alpha is a real scalar that scales x*y^H and y*x^H, where x^H is the same as conj(x'). The default
      is 1.

   •      zher2 —

    zher2 is a complex matrix of the same dimensions as A.

    For the elements of the first Nrows and Ncolumns of the triangular component you select for
    matrix A type, zher2 returns the results of the calculation. For any remaining elements, zher2
    returns the value of the element in A with the same index.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.

dgerdger -- GeneralGeneral MatrixMatrix Rank-1Rank-1 UpdateUpdate (DBL)(DBL)

Calculates the rank–1 update of a general matrix.


Inputs/Outputs

   •      x —

                                                    © National Instruments 3211

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3211 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3212 ordinal=3212 -->
## Functions

Functions


           x is an M–element real vector.

               •      y —

           y is an N–element real vector.

               •     A —

          A is a real general matrix of dimensions greater than or equal to M× N.

          The default is an M× Nmatrix with all elements equal to 0.

               •      alpha —

           alpha is a real scalar that scales x*y^T, where y^T is the same as y transposed.

          The default is 1.

               •      dger —

           dger is a real matrix of the same dimensions as A.

            For the elements of the first Mrows and Ncolumns of dger, the VI returns the results of the
              calculation. For any remaining elements, the VI returns the value of the element with the same
            index in A.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
      more information on BLAS functions.

      zgeruzgeru -- GeneralGeneral MatrixMatrix Rank-1Rank-1 UpdateUpdate (CDB)(CDB)

       Calculates the rank–1 update of a general matrix.


3212   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3212 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3213 ordinal=3213 -->
## Functions

Functions


Inputs/Outputs

   •      x —

    x is a complex vector.

   •      y —

    y is an M–element complex vector.

   •     A —

   A is a complex general matrix.

    The number of rows in A must be greater than or equal to Nand the number of columns in A
    must be greater than or equal to M. The default is an N×Mmatrix with all elements equal to 0.

   •      alpha —

    alpha is a complex scalar that scales x*y^T, where y^T represents y transposed. The default is 1.

   •      zgeru —

    zgeru is a complex matrix of the same dimensions as A.

    For the elements in the first Nrows and Mcolumns of zgeru, the VI returns the results of the
     calculation. For any remaining elements, the VI returns the value of the element in A with the
   same index.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.


                                                    © National Instruments 3213

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3213 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3214 ordinal=3214 -->
## Functions

Functions

      zgerczgerc -- GeneralGeneral MatrixMatrix Rank-1Rank-1 UpdateUpdate withwith ConjugationConjugation (CDB)(CDB)

       Calculates the rank–1 conjugated update of a general matrix.


      Inputs/Outputs

               •      x —

           x is a complex vector.

               •      y —

           y is an M–element complex vector.

               •     A —

          A is a complex general matrix.

          The number of rows in A must be greater than or equal to Nand the number of columns in A
          must be greater than or equal to M. The default is an N×Mmatrix with all elements equal to 0.

               •      alpha —

           alpha is a complex scalar that scales x*y^H, where y^H is the same as the conjugate transpose of
               y. The default is 1.

               •      zgerc —

            zgerc is a complex matrix of the same dimensions as A.

            For the elements in the first Nrows and Mcolumns of zgerc, the VI returns the results of the
             calculations. For any remaining elements, the VI returns the value of the element in A with the
          same index.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error


3214   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3214 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3215 ordinal=3215 -->
## Functions

Functions


    Code VI to convert the error code or warning into an error cluster.


Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.

trsvtrsv -- SolveSolve LinearLinear EqsEqs (Triangle,(Triangle, single)single)

Solves the linear equation op(A)*trsv = x for trsv.

The data types you wire to the A and x inputs determine the polymorphic instance to
use.


  • dtrsv - Solve Linear Eqs (Triangle, single) (DBL) VI
  • ztrsv - Solve Linear Eqs (Triangle, single) (CDB) VI

Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.
dtrsvdtrsv -- SolveSolve LinearLinear EqsEqs (Triangle,(Triangle, single)single)
(DBL)(DBL) VIVI

Solves the linear equation op(A)*trsv = x for trsv.

The data types you wire to the A and x inputs determine the polymorphic instance to
use.


                                                    © National Instruments 3215

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3215 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3216 ordinal=3216 -->
## Functions

Functions

      Inputs/Outputs

               •      operation A —

            operation A specifies the operation the VI performs on matrix A, resulting in matrix op(A).

           0   Direct (default)
           1   Conjugated & Transposed
           2   Transposed

               •     A —

          A is a real triangular matrix.

          The VI uses the first Nrows and columns in op(A) to solve the linear equations, where Nequals
            the number of elements in x. The number of rows and columns in A must be greater than or
            equal to N.

               •      x —

           x is a real vector.

               •      matrix A type —

            matrix A type specifies whether A is an upper or lower triangular matrix.

           2 Lower Triangular—A is a lower triangular matrix.
           3 Upper Triangular (default)—A is an upper triangular matrix.

               •      diagonal —

            diagonal specifies the value of the diagonal elements of A.

           0 Non-unit (default)—The VI uses the original diagonal elements of A.
           1 Unit—The VI uses a value of 1 for all diagonal elements of A.

               •      dtrsv —

            dtrsv is a real vector of the same size as x that returns the result of op(A)*dtsrv = x, solved for
             dtrsv.

               •       error —


3216   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3216 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3217 ordinal=3217 -->
## Functions

Functions


    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.
ztrsvztrsv -- SolveSolve LinearLinear EqsEqs (Triangle,(Triangle, single)single)
(CDB)(CDB) VIVI

Solves the linear equation op(A)*trsv = x for trsv.

The data types you wire to the A and x inputs determine the polymorphic instance to
use.


Inputs/Outputs

   •      operation A —

    operation A specifies the operation the VI performs on matrix A, resulting in matrix op(A).

    0   Direct (default)
    1   Conjugated & Transposed
    2   Transposed

   •     A —

   A is a complex triangular matrix.

    The VI uses the first Nrows and columns in op(A) to solve the linear equations, where Nequals
    the number of elements in x. The number of rows and columns in A must be greater than or


                                                    © National Instruments 3217

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3217 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3218 ordinal=3218 -->
## Functions

Functions


            equal to N.

               •      x —

           x is a complex vector.

               •      matrix A type —

            matrix A type specifies whether A is an upper or lower triangular matrix.

           2 Lower Triangular—A is a lower triangular matrix.
           3 Upper Triangular (default)—A is an upper triangular matrix.

               •      diagonal —

            diagonal specifies the value of the diagonal elements of A.

           0 Non-unit (default)—The VI uses the original diagonal elements of A.
           1 Unit—The VI uses a value of 1 for all diagonal elements of A.

               •       ztrsv —

            dtrsv is a complex vector of the same size as x that returns the result of op(A)*ztsrv = x, solved
              for ztrsv.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
      more information on BLAS functions.

    gemmgemm -- GeneralGeneral Matrix-MatrixMatrix-Matrix ProductProduct

       Calculates the product of two general matrices.

      The data types you wire to A, B, and C determine the polymorphic instance to use.


3218   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3218 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3219 ordinal=3219 -->
## Functions

Functions


  • dgemm - General Matrix-Matrix Product (DBL) VI
  • zgemm - General Matrix-Matrix Product (CDB) VI

Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Linear Algebra\Comparison of
   BLAS and linear algebra VIs.vi
dgemmdgemm -- GeneralGeneral Matrix-MatrixMatrix-Matrix ProductProduct
(DBL)(DBL) VIVI

Calculates the product of two general matrices.

The data types you wire to A, B, and C determine the polymorphic instance to use.


Inputs/Outputs

   •      operation B —

    operation B specifies the operation the VI performs on matrix B, resulting in matrix op(B).

    0   Direct (default)


                                                    © National Instruments 3219

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3219 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3220 ordinal=3220 -->
## Functions

Functions


           1   Conjugated & Transposed
           2   Transposed

               •      operation A —

            operation A specifies the operation the VI performs on matrix A, resulting in matrix op(A).

           0   Direct (default)
           1   Conjugated & Transposed
           2   Transposed

               •     A —

          A is a real matrix of dimensions such that op(A) is an M× Kmatrix.

               •     B —

         B is a real matrix such that op(B) is a K× Nmatrix.

               •     C —

          C is a real matrix of dimensions greater than or equal to M× N.

               •      alpha —

           alpha is a real scalar that scales op(A)*op(B).

          The default is 1.

               •      beta —

           beta is a real scalar that scales C.

          The default is 1.

               •    dgemm —

        dgemm is a real matrix of the same dimensions as C.

            For elements of the first Mrows and Ncolumns, dgemm returns the result of alpha*op(A) *op(B)
           + beta*C. For any remaining elements, dgemm returns the value of the element in C with the
          same index.


3220   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3220 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3221 ordinal=3221 -->
## Functions

Functions

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Linear Algebra\Comparison of
   BLAS and linear algebra VIs.vi
zgemmzgemm -- GeneralGeneral Matrix-MatrixMatrix-Matrix ProductProduct
(CDB)(CDB) VIVI

Calculates the product of two general matrices.

The data types you wire to A, B, and C determine the polymorphic instance to use.


Inputs/Outputs

   •      operation B —

    operation B specifies the operation the VI performs on matrix B, resulting in matrix op(B).


                                                    © National Instruments 3221

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3221 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3222 ordinal=3222 -->
## Functions

Functions


           0   Direct (default)
           1   Conjugated & Transposed
           2   Transposed

               •      operation A —

            operation A specifies the operation the VI performs on matrix A, resulting in matrix op(A).

           0   Direct (default)
           1   Conjugated & Transposed
           2   Transposed

               •     A —

          A is a complex matrix of dimensions such that op(A) is an M× Kmatrix.

               •     B —

         B is a complex matrix such that op(B) is a K× Nmatrix.

               •     C —

          C is a complex matrix of dimensions greater than or equal to M× N.

               •      alpha —

           alpha is a complex scalar that scales op(A)*op(B). The default is 1.

               •      beta —

           beta is a complex scalar that scales C.

          The default is 1.

               •     zgemm —

         zgemm is a complex matrix of the same dimensions as C.

            For elements of the first Mrows and Ncolumns, zgemm returns the result of alpha*op(A) *op(B)
           + beta*C. For any remaining elements, zgemm returns the value of the element in C with the
          same index.


3222   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3222 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3223 ordinal=3223 -->
## Functions

Functions

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Linear Algebra\Comparison of
   BLAS and linear algebra VIs.vi

symmsymm -- SymmetricSymmetric Matrix-MatrixMatrix-Matrix ProductProduct

Calculates the product of a symmetric matrix and another matrix.

The data types you wire to the A, B, and C inputs determine the polymorphic instance
to use.


  • dsymm - Symmetric Matrix-Matrix Product (DBL) VI
  • zsymm - Symmetric Matrix-Matrix Product (CDB) VI

Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.
dsymmdsymm -- SymmetricSymmetric Matrix-MatrixMatrix-Matrix ProductProduct
(DBL)(DBL) VIVI

Calculates the product of a symmetric matrix and another matrix.


                                                    © National Instruments 3223

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3223 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3224 ordinal=3224 -->
## Functions

Functions

      The data types you wire to the A, B, and C inputs determine the polymorphic instance
       to use.


      Inputs/Outputs

               •       side —

            side specifies the position of A in the calculation.

           0 Right—The VI calculates the result of alpha*B*A.
           1 Left (default)—The VI calculates the result of alpha*A*B.

               •     A —

          A is a real symmetric matrix that has at least Krows and Kcolumns.

          The VI multiplies the first Krows and Kcolumns of A by B. If you set side to Left, Kequals the
          number of rows in B. If you set side to Right, Kequals the number of columns in B.

               •     B —

         B is a real matrix.

               •     C —

          C is a real matrix.

          The dimensions of C must be greater than or equal to the dimensions of B. The default is a
            matrix the same size as matrix B with all elements equal to 0.

               •      matrix A type —

            matrix A type specifies whether the VI uses the upper or lower triangular component of A for the
              calculation.


3224   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3224 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3225 ordinal=3225 -->
## Functions

Functions


    2 Lower Triangular—The VI uses the lower triangular component of A for the calculation.
     Upper Triangular (default)—The VI uses the upper triangular component of A for the    3      calculation.

   •      alpha —

    alpha is a real scalar that scales A*B and B*A. The default is 1.

   •      beta —

    beta is a real scalar that scales C.

    The default is 1.

   •     dsymm —

   dsymm is a real matrix the same size as C.

    For the elements of the first Krows and Kcolumns of triangular component you select, the VI
    returns the result of alpha*A*B + beta*C or alpha*B*A + beta*C, depending on the side you
     select. For any remaining elements, the VI returns the value of the element with the same index
     in C.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.
zsymmzsymm -- SymmetricSymmetric Matrix-MatrixMatrix-Matrix ProductProduct
(CDB)(CDB) VIVI

Calculates the product of a symmetric matrix and another matrix.

The data types you wire to the A, B, and C inputs determine the polymorphic instance
to use.

                                                    © National Instruments 3225

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3225 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3226 ordinal=3226 -->
## Functions

Functions


      Inputs/Outputs

               •       side —

            side specifies the position of A in the calculation.

           0 Right—The VI calculates the result of alpha*B*A.
           1 Left (default)—The VI calculates the result of alpha*A*B.

               •     A —

          A a complex symmetric matrix that has at least Krows and Kcolumns.

          The VI multiplies the first Krows and Kcolumns of A by B. If you set side to Left, Kequals the
          number of rows in B. If you set side to Right, Kequals the number of columns in B.

               •     B —

         B is a complex matrix.

               •     C —

          C is a complex matrix of dimensions greater than or equal to B.

          The default is a matrix the same size as matrix B with all elements equal to 0.

               •      matrix A type —

            matrix A type specifies whether the VI uses the upper or lower triangular component of A for the
              calculation.

           2 Lower Triangular—The VI uses the lower triangular component of A for the calculation.
           Upper Triangular (default)—The VI uses the upper triangular component of A for the
           3
               calculation.


3226   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3226 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3227 ordinal=3227 -->
## Functions

Functions

   •      alpha —

    alpha is a complex scalar that scales A*B or B*A. The default is 1.

   •      beta —

    beta is a complex scalar that scales C. The default is 1.

   •     zsymm —

   zsymm is a real matrix the same size as C.

    For the elements of the first Krows and Kcolumns of the triangular component you select, the
     VI returns the result of alpha*A*B + beta*C or alpha*B*A + beta*C, depending on the side you
     select. For any remaining elements, the VI returns the value of the element with the same index
     in C.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.

zhemmzhemm -- HermitianHermitian Matrix-MatrixMatrix-Matrix ProductProduct (CDB)(CDB)

Calculates the product of a Hermitian matrix and another matrix.


Inputs/Outputs

   •       side —


                                                    © National Instruments 3227

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3227 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3228 ordinal=3228 -->
## Functions

Functions


            side specifies the position of A in the product calculation. The default is Left.

           0 Right—The VI calculates the result of alpha*B*A + beta*C.
           1 Left (default)—The VI calculates the result of alpha*A*B + beta*C.

               •     A —

          A is a Hermitian matrix of dimensions greater than or equal to K× K.

          The VI multiplies the first Krows and Kcolumns of the upper or lower triangular component of A
           by B.

               •     B —

         B is a complex matrix of dimensions K× N, if you set side to Left, or N× K, if you set side to
             Right.

               •     C —

          C is a complex matrix of dimensions greater than or equal to B.

          The default is a matrix the same size as matrix B with all elements equal to 0.

               •      matrix A type —

            matrix A type specifies whether the VI uses the upper or lower triangular part of A for the
              calculation.

           Lower Triangular—The VI uses only the lower triangular component of the input matrix for the           2               calculation.
           Upper Triangular (default)—The VI uses only the upper triangular component of the input
           3
              matrix for the calculation.

               •      alpha —

           alpha is a complex scalar that scales A*B or B*A. The default is 1.

               •      beta —

           beta is a complex scalar that scales C. The default is 1.

               •    zhemm —


3228   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3228 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3229 ordinal=3229 -->
## Functions

Functions


   zhemm is a complex matrix of the same dimensions as C that returns the result of alpha*A*B +
    beta*C or alpha*B*A + beta*C.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.

trmmtrmm -- TriangleTriangle Matrix-MatrixMatrix-Matrix ProductProduct

Calculates the product of a triangular matrix and another matrix.

The data types you wire to the A and B inputs determine the polymorphic instance to
use.


  • dtrmm - Triangle Matrix-Matrix Product (DBL) VI
  • ztrmm - Triangle Matrix-Matrix Product (CDB) VI

Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.
dtrmmdtrmm -- TriangleTriangle Matrix-MatrixMatrix-Matrix ProductProduct (DBL)(DBL)
VIVI

Calculates the product of a triangular matrix and another matrix.

The data types you wire to the A and B inputs determine the polymorphic instance to
use.


                                                    © National Instruments 3229

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3229 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3230 ordinal=3230 -->
## Functions

Functions


      Inputs/Outputs

               •       side —

            side specifies the position of A in the calculation.

           0 Right—The VI calculates the result of alpha*B*A.
           1 Left (default)—The VI calculates the result of alpha*A*B.

               •      operation A —

            operation A specifies the operation the VI performs on matrix A, resulting in matrix op(A).

           0   Direct (default)
           1   Conjugated & Transposed
           2   Transposed

               •     A —

          A is a real triangular matrix.

          The VI multiplies the first Krows and the first Kcolumns of op(A) by B. If you set side to Left, K
            equals the number of rows in B. If you set side to Right, Kequals the number of columns in B.
          The number of rows and columns in A must be greater than or equal to K.

               •     B —

         B is a real matrix.

               •      matrix A type —

            matrix A type specifies whether A is an upper or lower triangular matrix.


3230   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3230 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3231 ordinal=3231 -->
## Functions

Functions


    2 Lower Triangular—A is a lower triangular matrix.
    3 Upper Triangular (default)—A is an upper triangular matrix.

   •      alpha —

    alpha ia real scalar that scales op(A)*B or B*op(A). The default is 1.

   •      diagonal —

    diagonal specifies the value of the diagonal elements of A.

    0 Non-unit (default)—The VI uses the original diagonal elements of A.
    1 Unit—The VI uses a value of 1 for all diagonal elements of A.

   •     dtrmm —

   dtrmm is a real matrix of the same dimensions as B.

   dtrmm returns the result of alpha*op(A)*B, if you set side to Left, or alpha*B*op(A), if you set
    side to Right.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.
ztrmmztrmm -- TriangleTriangle Matrix-MatrixMatrix-Matrix ProductProduct (CDB)(CDB)
VIVI

Calculates the product of a triangular matrix and another matrix.

The data types you wire to the A and B inputs determine the polymorphic instance to
use.


                                                    © National Instruments 3231

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3231 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3232 ordinal=3232 -->
## Functions

Functions


      Inputs/Outputs

               •       side —

            side specifies the position of A in the calculation.

           0 Right—The VI calculates the result of alpha*B*A.
           1 Left (default)—The VI calculates the result of alpha*A*B.

               •      operation A —

            operation A specifies the operation the VI performs on matrix A, resulting in matrix op(A).

           0   Direct (default)
           1   Conjugated & Transposed
           2   Transposed

               •     A —

          A is a complex triangular matrix.

          The VI multiplies the first Krows and the first Kcolumns in op(A) by B. If you set side to Left, K
            equals the number of rows in B. If you set side to Right, Kequals the number of columns in B.
          The number of rows and columns in A must be greater than or equal to K.

               •     B —

         B is a complex matrix.

               •      matrix A type —

            matrix A type specifies whether A is an upper or lower triangular matrix.


3232   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3232 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3233 ordinal=3233 -->
## Functions

Functions


    2 Lower Triangular—A is a lower triangular matrix.
    3 Upper Triangular (default)—A is an upper triangular matrix.

   •      alpha —

    alpha is a complex scalar that scales op(A)*B or B*op(A). The default is 1.

   •      diagonal —

    diagonal specifies the value of the diagonal elements of A.

    0 Non-unit (default)—The VI uses the original diagonal elements of A.
    1 Unit—The VI uses a value of 1 for all diagonal elements of A.

   •     ztrmm —

   ztrmm is a complex matrix of the same dimensions as B.

   ztrmm returns the result of alpha*op(A)*B, if you set side to Left, or alpha*B*op(A), if you set
    side to Right.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.

syrksyrk -- SymmetricSymmetric MatrixMatrix Rank-kRank-k UpdateUpdate

Calculates the rank–k update of the upper or lower triangular component of a
symmetric matrix.

The data types you wire to the A and C inputs determine the polymorphic instance to
use.


                                                    © National Instruments 3233

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3233 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3234 ordinal=3234 -->
## Functions

Functions

            • dsyrk - Symmetric Matrix Rank-k Update (DBL) VI
            • zsyrk - Symmetric Matrix Rank-k Update (CDB) VI

       Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
      more information on BLAS functions.
    dsyrkdsyrk -- SymmetricSymmetric MatrixMatrix Rank-kRank-k UpdateUpdate
   (DBL)(DBL) VIVI

       Calculates the rank–k update of the upper or lower triangular component of a
      symmetric matrix.

      The data types you wire to the A and C inputs determine the polymorphic instance to
       use.


      Inputs/Outputs

               •      operation A —

            operation A specifies the operation the VI performs on A to generate matrix op(A).

           0   Direct (default)
           1   Conjugated & Transposed
           2   Transposed

               •     A —

          A is a real matrix with dimensions N× K.

               •     C —


3234   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3234 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3235 ordinal=3235 -->
## Functions

Functions


   C is a real symmetric matrix of at least dimensions N× K, or K× Nif you set operation A to
    Transposed.

   •      matrix C type —

    matrix C type specifies whether to update the upper or lower triangular component of C.

     Lower Triangular—The VI uses only the lower triangular component of C to calculate the    2
     rank–k update.
     Upper Triangular (default)—The VI uses only the upper triangular component of C to calculate    3     the rank–k update.

   •      alpha —

    alpha is a real scalar that scales A*A^T or A^T*A, where A^T represents A transposed. The default
      is 1.

   •      beta —

    beta is a real scalar that scales C.

    The default is 1.

   •      dsyrk —

    dsyrk is a real matrix of the same dimensions as C.

    For the elements in the first Nrows and Ncolumns of the triangular component you select for
    matrix C type, dsyrk returns the results of the calculation. For any other elements, dsyrk returns
    the value of the element in C with the same index.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.


                                                    © National Instruments 3235

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3235 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3236 ordinal=3236 -->
## Functions

Functions

    zsyrkzsyrk -- SymmetricSymmetric MatrixMatrix Rank-kRank-k UpdateUpdate
   (CDB)(CDB) VIVI

       Calculates the rank–k update of the upper or lower triangular component of a
      symmetric matrix.

      The data types you wire to the A and C inputs determine the polymorphic instance to
       use.


      Inputs/Outputs

               •      operation A —

            operation A specifies the operation the VI performs on A to generate matrix op(A).

           0   Direct (default)
           1   Conjugated & Transposed
           2   Transposed

               •     A —

          A is a complex matrix of dimensions N× K.

               •     C —

          C is a complex symmetric matrix of at least dimensions N× K, or K× Nif you set operation A to
            Transposed.

               •      matrix C type —

            matrix C type specifies whether to update the upper or lower triangular component of C.


3236   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3236 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3237 ordinal=3237 -->
## Functions

Functions


     Lower Triangular—The VI uses only the lower triangular component of C to calculate the    2
     rank–k update.
     Upper Triangular (default)—The VI uses only the upper triangular component of C to calculate    3     the rank–k update.

   •      alpha —

    alpha is a real scalar that scales for A*A^T or A^T*A, where A^T represents A transposed.

    The default is 1.

   •      beta —

    beta is a complex scalar that scales C.

    The default is 1.

   •      zsyrk —

    zsyrk is a complex matrix of the same dimensions as C.

    For the elements in the first Nrows and Ncolumns of the triangular component you select for
    matrix C type, zsyrk returns the results of the calculation. For any other elements, zsyrk returns
    the value of the element in C with the same index.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.

syr2ksyr2k -- SymmetricSymmetric MatrixMatrix Rank-2kRank-2k UpdateUpdate

Calculates the rank–2k update of a symmetric matrix.

The data types you wire to the A, B, and C inputs determine the polymorphic instance
to use.


                                                    © National Instruments 3237

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3237 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3238 ordinal=3238 -->
## Functions

Functions


            • dsyr2k - Symmetric Matrix Rank-2k Update (DBL) VI
            • zsyr2k - Symmetric Matrix Rank-2k Update (CDB) VI

       Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
      more information on BLAS functions.
   dsyr2kdsyr2k -- SymmetricSymmetric MatrixMatrix Rank-2kRank-2k UpdateUpdate
   (DBL)(DBL) VIVI

       Calculates the rank–2k update of a symmetric matrix.

      The data types you wire to the A, B, and C inputs determine the polymorphic instance
       to use.


      Inputs/Outputs

               •      operation —

            operation specifies the operation the VI performs on matrices A and B, resulting in matrices
            op(A) and op(B).

          The default is Not Transposed.

           0    Direct (default)
           1   Conjugated & Transposed
           2   Transposed


3238   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3238 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3239 ordinal=3239 -->
## Functions

Functions

•     A —

  A is a real matrix of dimensions N× K.

•     B —

  B is a real matrix.

  op(B) must have the same dimensions as op(A).

•     C —

  C is a real symmetric matrix of at least dimensions N× K, or K× Nif you set operation to
  Transposed.

•      matrix C type —

  matrix C type specifies whether to update the upper or lower triangular component of C. The
  default is Upper Triangular.

   Lower Triangular—The VI uses only the lower triangular component of C to calculate the  2   rank–2k update.
   Upper Triangular (default)—The VI uses only the upper triangular component of C to calculate  3
   the rank–2k update.

•      alpha —

  alpha is a real scalar that scales scale factor for A*B^T + B*A^T or A^T *B + B^T*A, where A^T
  represents A transposed.

  The default is 1.

•      beta —

  beta is a real scalar that scales C.

  The default is 1.

•      dsyr2k —

  dsyr2k is a real matrix of the same dimensions as C.

  For the elements in the first Nrows and Ncolumns of the triangular component you select for


                                                   © National Instruments 3239

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3239 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3240 ordinal=3240 -->
## Functions

Functions


            matrix C type, dsyr2k returns the results of the calculation. For any other elements, dsyr2k
             returns the value of the element in C with the same index.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
      more information on BLAS functions.
    zsyr2kzsyr2k -- SymmetricSymmetric MatrixMatrix Rank-2kRank-2k UpdateUpdate
   (CDB)(CDB) VIVI

       Calculates the rank–2k update of a symmetric matrix.

      The data types you wire to the A, B, and C inputs determine the polymorphic instance
       to use.


      Inputs/Outputs

               •      operation —

            operation specifies the operation the VI performs on matrices A and B, resulting in matrices
            op(A) and op(B).

          The default is Not Transposed.

           0    Direct (default)


3240   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3240 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3241 ordinal=3241 -->
## Functions

Functions


  1   Conjugated & Transposed
  2   Transposed

•     A —

  A is a complex matrix of dimensions N× K.

•     B —

  B is a complex matrix.

  op(B) must have the same dimensions as op(A).

•     C —

  C is a complex symmetric matrix of at least dimensions N× K, or K× Nif you set operation to
  Transposed.

•      matrix C type —

  matrix C type specifies whether to update the upper or lower triangular component of C. The
  default is Upper Triangular.

   Lower Triangular—The VI uses only the lower triangular component of C to calculate the  2
   rank–2k update.
   Upper Triangular (default)—The VI uses only the upper triangular component of C to calculate  3
   the rank–2k update.

•      alpha —

  alpha is a real scalar that scales scale factor for A*B^T + B*A^T or A^T *B + B^T*A, where A^T
  represents A transposed.

  The default is 1.

•      beta —

  beta is a complex scalar that scales C.

  The default is 1.

•      zsyr2k —


                                                   © National Instruments 3241

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3241 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3242 ordinal=3242 -->
## Functions

Functions


            zsyr2k is a complex matrix of the same dimensions as C.

            For the elements in the first Nrows and Ncolumns of the triangular component you select for
            matrix C type, zsyr2k returns the results of the calculation. For any other elements, zsyr2k
             returns the value of the element in C with the same index.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
      more information on BLAS functions.

      zherkzherk -- HermitianHermitian MatrixMatrix Rank-kRank-k UpdateUpdate (CDB)(CDB)

       Calculates the rank–k update of the upper or lower triangular component of a
       Hermitian matrix.


      Inputs/Outputs

               •      operation A —

            operation A specifies the operation the VI performs on A.

           0   Direct (default)
           1   Conjugated & Transposed
           2   Transposed

               •     A —

          A is a complex matrix of dimensions N× K.


3242   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3242 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3243 ordinal=3243 -->
## Functions

Functions

•     C —

  C is a Hermitian matrix.

  The VI updates the first Nrows and columns of the upper or lower triangular component of C,
  depending on what you select for matrix C type. The number of rows and columns in input
  matrix C must be greater than or equal to N. The default is an N× Nmatrix with all elements
  equal to 0.

•      matrix C type —

  matrix C type specifies whether to update the upper or lower triangular component of C.

   Lower Triangular—The VI uses only the lower triangular component of C to calculate the
  2   update.
   Upper Triangular (default)—The VI uses only the upper triangular component of C to calculate  3   the update.

•      alpha —

  alpha is a complex scalar that scales A*A^H or A^H*A, where A^H is the same as the conjugate
  transpose of A. The default is 1.

•      beta —

  beta is a real scalar that scales C.

  The default is 1.

•      zherk —

  zherk is a complex matrix of the same dimensions as C.

  For the elements in the first Nrows and Ncolumns of the triangular component you select for
  matrix C type, zherk returns the results of the calculation. For any remaining elements, zherk
  returns the value of the element with the same index in C.

•       error —

  error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
  Code VI to convert the error code or warning into an error cluster.


                                                   © National Instruments 3243

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3243 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3244 ordinal=3244 -->
## Functions

Functions

       Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
      more information on BLAS functions.

      zher2kzher2k -- HermitianHermitian MatrixMatrix Rank-2kRank-2k UpdateUpdate (CDB)(CDB)

       Calculates the rank–2k update of the upper or lower triangular component of a
       Hermitian matrix.


      Inputs/Outputs

               •      operation —

            operation specifies the operation the VI performs on A and B, resulting in matrices op(A) and
             op(B).

           0   Direct (default)
           1   Conjugated & Transposed
           2   Transposed

               •     A —

          A is a complex matrix of dimensions N× K.

               •     B —

         B is a complex matrix.

            op(B) must have the same dimensions as op(A).

               •     C —

          C is a Hermitian matrix.

                    If you set operation to Not Transposed, the VI uses the first Nrows of C for the update. The


3244   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3244 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3245 ordinal=3245 -->
## Functions

Functions


   number of rows and columns in C must be greater than or equal to N. The default is an N× N
    matrix with all zero elements.

   •      matrix C type —

    matrix C type specifies whether to update the upper or lower triangular component of C.

     Lower Triangular—The VI uses only the lower triangular component of C to calculate the    2
     rank–2k update.
     Upper Triangular (default)—The VI uses only the upper triangular component of C to calculate    3     the rank–2k update.

   •      alpha —

    alpha is a complex scalar that scales A*B^H or A^H*B, where A^H is the same as conj(A').

    The default is 1.

   •      beta —

    beta is a real scalar that scales C.

    The default is 1.

   •      zher2k —

    zher2k is a complex matrix of the same dimensions as C.

    For the first Nrows and Ncolumns of the triangular component you select for matrix C type,
    zher2k returns the results of the calculation. For any remaining rows and columns, zher2k
    returns the element in C with the same index.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
more information on BLAS functions.


                                                    © National Instruments 3245

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3245 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3246 ordinal=3246 -->
## Functions

Functions

      trsmtrsm -- SolveSolve LinearLinear EqsEqs (Triangle,(Triangle, multiple)multiple)

       Solves either op(A)*trsm = alpha*x or trsm*op(A) = alpha*x for trsm.

      The data types you wire to A and x determine the polymorphic instance to use.


            • dtrsm - Solve Linear Eqs (Triangle, multiple) (DBL) VI
            • ztrsm - Solve Linear Eqs (Triangle, multiple) (CDB) VI

       Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
      more information on BLAS functions.
   dtrsmdtrsm -- SolveSolve LinearLinear EqsEqs (Triangle,(Triangle, multiple)multiple)
   (DBL)(DBL) VIVI

       Solves either op(A)*trsm = alpha*x or trsm*op(A) = alpha*x for trsm.

      The data types you wire to A and x determine the polymorphic instance to use.


      Inputs/Outputs

               •       side —

            side specifies the position of A in the linear equations.

           0 Right—The VI solves the linear equations dtrsm*op(A) = alpha*X.


3246   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3246 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3247 ordinal=3247 -->
## Functions

Functions


  1 Left (default)—The VI solves the linear equations op(A)*dtrsm = alpha*X.

•      operation A —

  operation A specifies the operation the VI performs on matrix A, resulting in matrix op(A).

  0   Direct (default)
  1   Conjugated & Transposed
  2   Transposed

•     A —

  A is a real triangular matrix.

  The VI uses the first Krows and columns in op(A) to solve the linear equations. If you set side to
   Left, Kequals the number of rows in x. If you set side to Right, Kequals the number of columns
  in x. The number of rows and columns in A must be greater than or equal to K.

•      x —

  x is a real matrix.

•      matrix A type —

  matrix A type specifies whether A is an upper or lower triangular matrix.

  2 Lower Triangular—A is a lower triangular matrix.
  3 Upper Triangular (default)—A is an upper triangular matrix.

•      alpha —

  alpha is the real scale factor for x.

  The default is 1.

•      diagonal —

  diagonal specifies the value of the diagonal elements of A.

  0 Non-unit (default)—The VI uses the original diagonal elements of A.


                                                   © National Instruments 3247

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3247 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3248 ordinal=3248 -->
## Functions

Functions


           1 Unit—The VI uses a value of 1 for all diagonal elements of A.

               •      dtrsm —

           dtrsm is a real matrix of the same size as x that returns the results of op(A)*dtsrm = alpha*x or
            dtsrm*op(A) = alpha*x solved for dtrsm.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
      more information on BLAS functions.
   ztrsmztrsm -- SolveSolve LinearLinear EqsEqs (Triangle,(Triangle, multiple)multiple)
   (CDB)(CDB) VIVI

       Solves either op(A)*trsm = alpha*x or trsm*op(A) = alpha*x for trsm.

      The data types you wire to A and x determine the polymorphic instance to use.


      Inputs/Outputs

               •       side —

            side specifies the position of A in the linear equations. The default is Left.

           0 Right—The VI solves the linear equations ztrsm*op(A) = alpha*X.


3248   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3248 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3249 ordinal=3249 -->
## Functions

Functions


  1 Left (default)—The VI solves the linear equations op(A)*ztrsm = alpha*X.

•      operation A —

  operation A specifies the operation the VI performs on matrix A, resulting in matrix op(A).

  0   Direct (default)
  1   Conjugated & Transposed
  2   Transposed

•     A —

  A is a complex triangular matrix.

  The VI uses the first Krows and columns in op(A) to solve the linear equations. If you set side to
   Left, Kequals the number of rows in x. If you set side to Right, Kequals the number of columns
  in x. The number of rows and columns in A must be greater than or equal to K.

•      x —

  x is a complex matrix.

•      matrix A type —

  matrix A type specifies whether A is an upper or lower triangular matrix.

  2 Lower Triangular—A is a lower triangular matrix.
  3 Upper Triangular (default)—A is an upper triangular matrix.

•      alpha —

  alpha is the real scale factor for x.

  The default is 1.

•      diagonal —

  diagonal specifies the value of the diagonal elements of A.

  0 Non-unit (default)—The VI uses the original diagonal elements of A.


                                                   © National Instruments 3249

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3249 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3250 ordinal=3250 -->
## Functions

Functions


           1 Unit—The VI uses a value of 1 for all diagonal elements of A.

               •      ztrsm —

           ztrsm is a complex matrix of the same size as x that returns the results of op(A)*ztsrm = alpha*x
            or ztsrm*op(A) = alpha*x solved for ztrsm.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for
      more information on BLAS functions.

      FittingFitting

      Use the Fitting VIs to perform curve fitting analysis or regression.

      The VIs on this palette can return mathematics error codes.


         Palette                      Description
        Object

                     Returns the linear fit of a data set (X, Y) using the Least Square, Least Absolute
         Linear Fit
                       Residual, or Bisquare method.


         Exponential  Returns the exponential fit of a data set (X, Y) using the Least Square, Least Absolute
           Fit           Residual, or Bisquare method.


                     Returns the power fit of a data set (X, Y) using the Least Square, Least Absolute
       Power Fit
                       Residual, or Bisquare method.


3250   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3250 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3251 ordinal=3251 -->
## Functions

Functions


Palette             Description
Object

Gaussian    Returns the Gaussian fit of a data set (X, Y) using the Least Square, Least Absolute
Peak Fit      Residual, or Bisquare method.


Logarithm   Returns the logarithmic fit of a data set (X, Y) using the Least Square, Least Absolute
Fit           Residual, or Bisquare method.


General
            Returns the polynomial fit of polynomial order for a data set (X, Y) using the LeastPolynomial             Square, Least Absolute Residual, or Bisquare method.Fit


             Finds the k-dimension linear curve values and the set of k-dimension linear fit
General
               coefficients, which describe the k-dimension linear curve that best represents theLinear Fit
             input data set using the Least Square, Least Absolute Residual, or Bisquare method.


Cubic       Uses cubic spline fitting to smooth a data set (X, Y) according to the balance
Spline Fit    parameter.


B-Spline Fit  Uses B-spline fitting to smooth a data set.


Fitting on a            Determines the best spherical fit on a cloud of points in 3D.
Sphere


            Uses the Levenberg-Marquardt algorithm to determine the set of parameters that
Nonlinear    best fit the set of input data points (X, Y) as expressed by a nonlinear function y=
Curve Fit      f(x,a), where ais the set of parameters. You must manually select the polymorphic
             instance to use.

            Uses either the Levenberg-Marquardt algorithm or the trust-region dogleg algorithm
Constrained             to determine the set of parameters that best fit the set of input data points (X, Y) as
Nonlinear            expressed by a nonlinear function y= f(x,a), where ais the set of parameters. YouCurve Fit
           must manually select the polymorphic instance to use.


                                                    © National Instruments 3251

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3251 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3252 ordinal=3252 -->
## Functions

Functions


         Palette                      Description
        Object

        Curve      Computes the coefficients that best represent the input data based on the chosen
          Fitting      model type.


        Advanced                   Use the Advanced Curve Fitting VIs to compute additional fit statistics and        Curve                         coefficients.
          Fitting


      Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Fitting\Fitting.lvproj

      LinearLinear FitFit

       Returns the linear fit of a data set (X, Y) using the Least Square, Least Absolute
       Residual, or Bisquare method.


      Inputs/Outputs

               •      Y —

           Y is the array of dependent values. The length of Y must be greater than or equal to the number
             of unknown parameters.

               •     X —

          X is the array of independent values. X must be the same size as Y.

               •      Weight —

3252   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3252 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3253 ordinal=3253 -->
## Functions

Functions


  Weight is the array of weights for the observations (X, Y). Weight must be the same size as Y.
  Weight also must contain non-zero elements. If an element in Weight is less than 0, the VI uses
  the absolute value of the element.

   If you do not wire an input to Weight, the VI sets all elements of Weight to 1.

•      tolerance —

  tolerance determines when to stop the iterative adjustment of slope and intercept when you
  use the Least Absolute Residual or Bisquare method. For the Least Absolute Residual method, if
  the relative difference between residue in two successive iterations is less than tolerance, this VI
  returns the resulting residue. For the Bisquare method, if any relative difference between slope
  and intercept in two successive iterations is less than tolerance, this VI returns the resulting
  slope and intercept.

   If tolerance is less than or equal to 0, this VI sets tolerance to 0.0001.

•     method —

  method specifies the fitting method.

  0    Least Square (default)
  1    Least Absolute Residual
  2   Bisquare

•      parameter bounds —

  parameter bounds contains the upper and lower constraints for the slope and intercept. If you
  know the exact value of certain parameters, you can set the lower and upper bounds of those
  parameters equal to the known values.

      •      slope min —

      slope min specifies the lower bound for the slope. The default value is -Inf, which means
     no lower bound is imposed on the slope.

      •      slope max —

      slope max specifies the upper bound for the slope. The default value is Inf, which means
     no upper bound is imposed on the slope.

      •       intercept min —


                                                   © National Instruments 3253

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3253 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3254 ordinal=3254 -->
## Functions

Functions


                 intercept min specifies the lower bound for the intercept. The default value is -Inf, which
             means no lower bound is imposed on the intercept.

                     •       intercept max —

                 intercept max specifies the upper bound for the intercept. The default value is Inf, which
             means no upper bound is imposed on the intercept.


               •      Best Linear Fit —

            Best Linear Fit returns the y-values of the fitted model.

               •      slope —

            slope returns the slope of the fitted model.

               •       intercept —

             intercept returns the intercept of the fitted model.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

               •      residue —

            residue returns the weighted mean error of the fitted model. If method is Least Absolute
          Residual, residue is the weighted mean absolute error. Otherwise, residue is the weighted
         mean square error.


       This VI uses the iterative general Least Square method and the Levenberg-Marquardt
      method to fit experimental data to a straight line of the general form described by the
       following equation:

     f= ax+ b

      where xis the input sequence X, ais slope, and bis intercept. This VI finds the values
       of aand bthat best fit the observations (X, Y).

3254   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3254 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3255 ordinal=3255 -->
## Functions

Functions

The following equation specifically describes the linear curve resulting from the linear
fit algorithm:

y[i] = ax[i] + b

If the noise of Y is Gaussian distributed, use the Least Square method. The following
illustration shows the linear fit result using this method.


When you use the Least Square method, this VI finds the slope and intercept of the
linear model by minimizing residue according to the following equation:


where Nis the length of Y, wi is the ith element of Weight, fi is the ith element of Best
Linear Fit, and yi is the ith element of Y.

The Least Absolute Residual and Bisquare methods are robust fitting methods. Use
these methods if outliers in the observations exist. The following illustration compares
the fit results of the Least Square, Least Absolute Residual, and Bisquare fitting
methods. In most cases, the Bisquare method is less sensitive to outliers than the
Least Absolute Residual method.


                                                    © National Instruments 3255

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3255 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3256 ordinal=3256 -->
## Functions

Functions


     When you use the Least Absolute Residual method, this VI finds the slope and
       intercept of the linear model by minimizing residue according to the following
       equation:


     When you use the Bisquare method, this VI obtains the slope and intercept using an
        iterative process, as shown in the following illustration, and calculates residue using
       the same formula as in the Least Square method.


3256   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3256 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3257 ordinal=3257 -->
## Functions

Functions


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Fitting\Regression Solver.vi
  • labview\examples\Mathematics\Fitting\Linear, Exp, and
   Power Fit.vi
  • labview\examples\Mathematics\Fitting\Robust linear fit.vi

ExponentialExponential FitFit

Returns the exponential fit of a data set (X, Y) using the Least Square, Least Absolute
Residual, or Bisquare method.


                                                    © National Instruments 3257

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3257 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3258 ordinal=3258 -->
## Functions

Functions


      Inputs/Outputs

               •      Y —

           Y is the array of dependent values. The length of Y must be greater than or equal to the number
             of unknown parameters.

               •     X —

          X is the array of independent values. X must be the same size as Y.

               •      Weight —

           Weight is the array of weights for the observations (X, Y). Weight must be the same size as Y.
           Weight also must contain non-zero elements. If an element in Weight is less than 0, the VI uses
            the absolute value of the element.

                    If you do not wire an input to Weight, the VI sets all elements of Weight to 1.

               •      tolerance —

            tolerance determines when to stop the iterative adjustment of amplitude, damping, and offset.
            For the Least Square and Least Absolute Residual methods, if the relative difference between
            residue in two successive iterations is less than tolerance, this VI returns the resulting residue.
            For the Bisquare method, if any relative difference between amplitude, damping, and offset in
          two successive iterations is less than tolerance, this VI returns the resulting amplitude,
           damping, and offset.

                    If tolerance is less than or equal to 0, this VI sets tolerance to 0.0001.

               •     method —

          method specifies the fitting method.

           0    Least Square (default)
           1    Least Absolute Residual
           2   Bisquare


3258   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3258 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3259 ordinal=3259 -->
## Functions

Functions

•      parameter bounds —

  parameter bounds contains the upper and lower constraints for the amplitude, damping, and
   offset. If you know the exact value of certain parameters, you can set the lower and upper
  bounds of the parameters equal to the known values.

      •    amp min —

    amp min specifies the lower bound for the amplitude. The default value is –Inf, which
     means no lower bound is imposed on the amplitude.

      •    amp max —

    amp max specifies the upper bound for the amplitude. The default value is Inf, which
     means no upper bound is imposed on the amplitude.

      •     damping min —

     damping min specifies the lower bound for the damping. The default value is –Inf, which
     means no lower bound is imposed on the damping.

      •     damping max —

     damping max specifies the upper bound for the damping. The default value is Inf, which
     means no upper bound is imposed on the damping.

      •       offset min —

       offset min specifies the lower bound for the offset. The default value is 0, which means the
       offset must be greater than or equal to 0.

      •       offset max —

       offset max specifies the upper bound for the offset. The default value is 0, which means the
       offset must be less than or equal to 0.


•      Best Exponential Fit —

  Best Exponential Fit returns the y-values of the fitted model.

•      amplitude —

  amplitude returns the amplitude of the fitted model.


                                                   © National Instruments 3259

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3259 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3260 ordinal=3260 -->
## Functions

Functions

               •     damping —

          damping returns the damping of the fitted model.

               •       offset —

             offset returns the offset of the fitted model.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

               •      residue —

            residue returns the weighted mean error of the fitted model. If method is Least Absolute
          Residual, residue is the weighted mean absolute error. Otherwise, residue is the weighted
         mean square error.


       This VI uses the iterative general Least Square method and the Levenberg-Marquardt
      method to fit data to an exponential curve of the general form described by the
       following equation:

     f= aebx + c

      where xis the input sequence X, ais amplitude, bis damping, and cis offset. This VI
       finds the values of a, b, and cthat best fit the observations (X, Y).

      The following equation specifically describes the exponential curve resulting from the
       exponential fit algorithm:

        y[i] = aebx[i] + c

           If the noise of Y is Gaussian distributed, use the Least Square method. The following
        illustration shows the exponential fit result using this method.


3260   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3260 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3261 ordinal=3261 -->
## Functions

Functions


When you use the Least Square method, this VI finds the amplitude, damping, and
offset of the exponential model by minimizing the residue according to the following
equation:


where Nis the length of Y, wi is the ith element of Weight, fi is the ith element of Best
Exponential Fit, and yi is the ith element of Y.

The Least Absolute Residual and Bisquare methods are robust fitting methods. Use
these methods if outliers in the observations exist. The following illustration compares
the fit results of the Least Square, Least Absolute Residual, and Bisquare fitting
methods. In most cases, the Bisquare method is less sensitive to outliers than the
Least Absolute Residual method.


                                                    © National Instruments 3261

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3261 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3262 ordinal=3262 -->
## Functions

Functions


     When you use the Least Absolute Residual method, this VI finds the amplitude,
      damping, and offset of the exponential model by minimizing the residue according to
       the following equation:


     When you use the Bisquare method, this VI obtains the amplitude, damping, and
        offset using an iterative process, as shown in the following illustration, and calculates
       the residue using the same formula as the Least Square method.


3262   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3262 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3263 ordinal=3263 -->
## Functions

Functions


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Fitting\Regression Solver.vi
  • labview\examples\Mathematics\Fitting\Linear, Exp, and
   Power Fit.vi

PowerPower FitFit

Returns the power fit of a data set (X, Y) using the Least Square, Least Absolute
Residual, or Bisquare method.


                                                    © National Instruments 3263

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3263 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3264 ordinal=3264 -->
## Functions

Functions


      Inputs/Outputs

               •      Y —

           Y is the array of dependent values. The length of Y must be greater than or equal to the number
             of unknown parameters.

               •     X —

          X is the array of independent values. X must be the same size as Y.

               •      Weight —

           Weight is the array of weights for the observations (X, Y). Weight must be the same size as Y. If
           you do not wire an input to Weight, the VI sets all elements of Weight to 1. If an element in
           Weight is less than 0, the VI uses the absolute value of the element.

               •      tolerance —

            tolerance determines when to stop the iterative adjustment of amplitude, power, and offset.
            For the Least Square and Least Absolute Residual methods, if the relative difference between
            residue in two successive iterations is less than tolerance, this VI returns the resulting residue.
            For the Bisquare method, if any relative difference between amplitude, power, and offset in two
             successive iterations is less than tolerance, this VI returns the resulting amplitude, power, and
              offset.

                    If tolerance is less than or equal to 0, this VI sets tolerance to 0.0001.

               •     method —

          method specifies the fitting method.

           0    Least Square (default)
           1    Least Absolute Residual
           2   Bisquare

               •      parameter bounds —


3264   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3264 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3265 ordinal=3265 -->
## Functions

Functions


  parameter bounds contains the upper and lower constraints for the amplitude, power, and
   offset. If you know the exact value of certain parameters, you can set the lower and upper
  bounds of those parameters equal to the known values.

      •    amp min —

    amp min specifies the lower bound for the amplitude. The default value is -Inf, which
     means no lower bound is imposed on the amplitude.

      •    amp max —

    amp max specifies the upper bound for the amplitude. The default value is Inf, which
     means no upper bound is imposed on the amplitude.

      •     power min —

     power min specifies the lower bound for the power. The default value is -Inf, which means
     no lower bound is imposed on the power.

      •     power max —

     power max specifies the upper bound for the power. The default value is Inf, which means
     no upper bound is imposed on the power.

      •       offset min —

       offset min specifies the lower bound for the offset. The default value is 0, which means the
       offset must be greater than or equal to 0.

      •       offset max —

       offset max specifies the upper bound for the offset. The default value is 0, which means the
       offset must be less than or equal to 0.


•      Best Power Fit —

  Best Power Fit returns the y-values of the fitted model.

•      amplitude —

  amplitude returns the amplitude of the fitted model.

•     power —

                                                   © National Instruments 3265

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3265 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3266 ordinal=3266 -->
## Functions

Functions


          power returns the power of the fitted model.

               •       offset —

             offset returns the offset of the fitted model.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

               •      residue —

            residue returns the weighted mean error of the fitted model. If method is Least Absolute
             Residual, residue is the weighted mean absolute error. Otherwise, residue is the weighted mean
            square error.


       This VI uses the iterative general Least Square method and the Levenberg-Marquardt
      method to fit data to the power function of the general form described by the
       following equation:

     f=axb + c

      where xis the input sequence X, ais amplitude, bis power and cis offset. This VI
       finds the values of a, b, and cthat best fit the observations (X, Y).

      The following equation specifically describes the power function resulting from the
       general power fit algorithm:

        y[i] = a(x[i])b + c

           If the noise of Y is Gaussian distributed, use the Least Square method. The following
        illustration shows the power fit result using this method.


3266   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3266 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3267 ordinal=3267 -->
## Functions

Functions


When you use the Least Square method, this VI finds the amplitude, power, and offset
of the power model by minimizing residue according to the following equation:


where Nis the length of Y, wi is the ith element of Weight, fi is the ith element of Best
Power Fit, and yi is the ith element of Y.

The Least Absolute Residual and Bisquare methods are robust fitting methods. Use
these methods if outliers in the observations exist. The following illustration compares
the fit results of the Least Square, Least Absolute Residual, and Bisquare fitting
methods. In most cases, the Bisquare method is less sensitive to outliers than the
Least Absolute Residual method.


                                                    © National Instruments 3267

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3267 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3268 ordinal=3268 -->
## Functions

Functions


     When you use the Least Absolute Residual method, this VI finds the amplitude, power,
      and offset of the power model by minimizing residue according to the following
       equation:


     When you use the Bisquare method, this VI obtains the amplitude, power, and offset
       using an iterative process, as shown in the following illustration, and calculates
       residue using the same formula as the Least Square method.


3268   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3268 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3269 ordinal=3269 -->
## Functions

Functions


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Fitting\Linear, Exp, and
   Power Fit.vi

GaussianGaussian PeakPeak FitFit

Returns the Gaussian fit of a data set (X, Y) using the Least Square, Least Absolute
Residual, or Bisquare method.


                                                    © National Instruments 3269

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3269 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3270 ordinal=3270 -->
## Functions

Functions


      Inputs/Outputs

               •        initial guess —

               initial guess specifies the initial guesses of amplitude, center, standard deviation, and offset
              for use in the iterative algorithm. If initial amplitude, initial center, initial standard deviation,
            or offset is NaN, this VI calculates the initial guess automatically.

                     •        initial amplitude —

                     initial amplitude is the initial guess of amplitude.

                     •        initial center —

                     initial center is the initial guess of center.

                     •        initial standard deviation —

                     initial standard deviation is the initial guess of standard deviation.

                     •       offset —

                  offset is the initial guess of the offset this VI returns.


               •      Y —

           Y is the array of dependent values. The length of Y must be greater than or equal to the number
             of unknown parameters.

               •     X —

          X is the array of independent values. X must be the same size as Y.

               •      Weight —

           Weight is the array of weights for the observations (X, Y). Weight must be the same size as Y. If


3270   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3270 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3271 ordinal=3271 -->
## Functions

Functions


  you do not wire an input to Weight, the VI sets all elements of Weight to 1. If an element in
  Weight is less than 0, the VI uses the absolute value of the element.

•      tolerance —

  tolerance determines when to stop the iterative adjustment of amplitude, center, standard
  deviation, and offset. For the Least Square and Least Absolute Residual methods, if the relative
  difference between residue in two successive iterations is less than tolerance, this VI returns the
  resulting residue. For the Bisquare method, if any relative difference between amplitude,
  center, standard deviation, or offset in two successive iterations is less than tolerance, this VI
  returns the resulting amplitude, center, standard deviation, and offset.

   If tolerance is less than or equal to 0, this VI sets tolerance to 0.0001.

•     method —

  method specifies the fitting method.

  0    Least Square (default)
  1    Least Absolute Residual
  2   Bisquare

•      parameter bounds —

  parameter bounds contains the upper and lower constraints for the amplitude, center,
  standard deviation, and offset. If you know the exact value of certain parameters, you can set
  the lower and upper bounds of the parameters equal to the known values.

      •    amp min —

    amp min specifies the lower bound for the amplitude. The default value is -Inf, which
     means no lower bound is imposed on the amplitude.

      •    amp max —

    amp max specifies the upper bound for the amplitude. The default value is Inf, which
     means no upper bound is imposed on the amplitude.

      •      center min —

      center min specifies the lower bound for the center. The default value is -Inf, which means


                                                   © National Instruments 3271

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3271 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3272 ordinal=3272 -->
## Functions

Functions


              no lower bound is imposed on the center.

                     •      center max —

                center max specifies the upper bound for the center. The default value is Inf, which means
              no upper bound is imposed on the center.

                     •      deviation min —

                deviation min specifies the lower bound for the standard deviation. The default value is
                       -Inf, which means no lower bound is imposed on the standard deviation.

                     •      deviation max —

                deviation max specifies the upper bound for the standard deviation. The default value is
                       Inf, which means no upper bound is imposed on the standard deviation.

                     •       offset min —

                  offset min specifies the lower bound for the offset. The default value is 0, which means the
                  offset must be greater than or equal to 0.

                     •       offset max —

                  offset max specifies the upper bound for the offset. The default value is 0, which means the
                  offset must be less than or equal to 0.


               •       offset —

             offset returns the offset of the fitted model.

               •      Best Gaussian Fit —

            Best Gaussian Fit returns the y-values of the fitted model.

               •      amplitude —

           amplitude returns the amplitude of the fitted model.

               •      center —

            center returns the center of the fitted model.


3272   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3272 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3273 ordinal=3273 -->
## Functions

Functions

   •      standard deviation —

    standard deviation returns the standard deviation of the fitted model.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

   •      residue —

    residue returns the weighted mean error of the fitted model. If method is Least Absolute
    Residual, residue is the weighted mean absolute error. Otherwise, residue is the weighted mean
    square error.


This VI uses the iterative general Linear Square method and the Levenberg-Marquardt
method to fit data to a Gaussian curve in a form described by the following equation:


where xis the input sequence X, ais amplitude, µis center, σ is standard deviation,
and cis offset. This VI finds the values of a, µ, σ, and cthat best fit the observations (X,
Y).

The following equation specifically describes the Gaussian curve resulting from the
Gaussian fit algorithm:


If the noise of Y is Gaussian distributed, use the Least Square method. The following
illustration shows the Gaussian fit result using this method.


                                                    © National Instruments 3273

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3273 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3274 ordinal=3274 -->
## Functions

Functions


     When you use the Least Square method, this VI finds the amplitude, center, standard
       deviation, and offset of the Gaussian model by minimizing the residue according to
       the following equation:


      where Nis the length of Y, wi is the ith element of Weight, fi is the ith element of Best
      Gaussian Fit, and yi is the ith element of Y.

      The Least Absolute Residual and Bisquare methods are robust fitting methods. Use
       these methods if outliers in the observations exist. The following illustration compares
       the fit results of the Least Square, Least Absolute Residual, and Bisquare fitting
      methods. In most cases, the Bisquare method is less sensitive to outliers than the
       Least Absolute Residual method.


3274   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3274 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3275 ordinal=3275 -->
## Functions

Functions


When you use the Least Absolute Residual method, this VI find the amplitude, center,
standard deviation, and offset of the Gaussian model by minimizing the residue
according to the following equation:


When you use the Bisquare method, this VI obtains the amplitude, center, standard
deviation, and offset using an iterative process, as shown in the following illustration,
and calculates the residue using the same formula as the Least Square method.


                                                    © National Instruments 3275

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3275 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3276 ordinal=3276 -->
## Functions

Functions


     LogarithmLogarithm FitFit

       Returns the logarithmic fit of a data set (X, Y) using the Least Square, Least Absolute
       Residual, or Bisquare method.


      Inputs/Outputs

               •      base —

           base specifies the base of the logarithm. The default is e, or the natural logarithm.


3276   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3276 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3277 ordinal=3277 -->
## Functions

Functions

•      Y —

  Y is the array of dependent values. The length of Y must be greater than or equal to the number
  of unknown parameters.

•     X —

  X is the array of independent values. X must be the same size as Y.

•      Weight —

  Weight is the array of weights for the observations (X, Y). Weight must be the same size as Y. If
  you do not wire an input to Weight, the VI sets all elements of Weight to 1. If an element in
  Weight is less than 0, the VI uses the absolute value of the element.

•      tolerance —

  tolerance determines when to stop the iterative adjustment of amplitude and scale. For the
  Least Square and Least Absolute Residual methods, if the relative difference between residue in
  two successive iterations is less than tolerance, this VI returns the resulting residue. For the
  Bisquare method, if any relative difference between amplitude and scale in two successive
  iterations is less than tolerance, this VI returns the resulting amplitude and scale. If tolerance is
  less than or equal to 0, this VI sets tolerance to 0.0001.

•     method —

  method specifies the fitting method.

  0    Least Square (default)
  1    Least Absolute Residual
  2   Bisquare

•      parameter bounds —

  parameter bounds contains the upper and lower constraints for the amplitude and scale. If you
  know the exact value of certain parameters, you can set the lower and upper bounds of those
  parameters equal to the known values.

      •    amp min —

    amp min specifies the lower bound for the amplitude. The default value is -Inf, which
     means no lower bound is imposed on the amplitude.


                                                   © National Instruments 3277

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3277 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3278 ordinal=3278 -->
## Functions

Functions


                     •    amp max —

            amp max specifies the upper bound for the amplitude. The default value is Inf, which
             means no upper bound is imposed on the amplitude.

                     •       scale min —

                 scale min specifies the lower bound for the scale. The default value is -Inf, which means no
                lower bound is imposed on the scale.

                     •       scale max —

                 scale max specifies the upper bound for the scale. The default value is Inf, which means no
               upper bound is imposed on the scale.


               •      Best Logarithm Fit —

            Best Logarithm Fit returns the y-values of the fitted model.

               •      amplitude —

           amplitude returns the amplitude of the fitted model.

               •       scale —

             scale returns the scale of the fitted model.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

               •      residue —

            residue returns the weighted mean error of the fitted model. If method is Least Absolute
             Residual, residue is the weighted mean absolute error. Otherwise, residue is the weighted mean
            square error.


       This VI uses the iterative general Least Square method and the Levenberg-Marquardt
      method to fit data to a logarithmic function of the general form described by the
       following equation:


3278   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3278 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3279 ordinal=3279 -->
## Functions

Functions

f= alogc(bx)

where xis the input sequence X, cis base, ais amplitude, and bis scale. This VI finds
the values of aand bthat best fit the observations (X, Y).

The following equation describes the logarithm function resulting from the logarithm
fit algorithm:

y[i] = alogc(bx[i])

If the noise of Y is Gaussian distributed, use the Least Square method. The following
illustration shows the logarithm fit result using this method.


When you use the Least Square method, this VI finds the amplitude and scale of the
logarithmic model by minimizing residue according to the following equation:


where Nis the length of Y, wi is the ith element of Weight, fi is the ith element of Best
Logarithm Fit, and yi is the ith element of Y.

The Least Absolute Residual and Bisquare methods are robust fitting methods. Use

                                                    © National Instruments 3279

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3279 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3280 ordinal=3280 -->
## Functions

Functions

       these methods if outliers in the observations exist. The following illustration compares
       the fit results of the Least Square, Least Absolute Residual, and Bisquare fitting
      methods. In most cases, the Bisquare method is less sensitive to outliers than the
       Least Absolute Residual method.


     When you use the Least Absolute Residual method, this VI finds the amplitude and
       scale of the logarithmic model by minimizing residue according to the following
       equation:


     When you use the Bisquare method, this VI obtains the amplitude and scale using an
        iterative process, as shown in the following illustration, and calculates residue using
       the same formula as in the Least Square method.


3280   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3280 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3281 ordinal=3281 -->
## Functions

Functions


GeneralGeneral PolynomialPolynomial FitFit

Returns the polynomial fit of polynomial order for a data set (X, Y) using the Least
Square, Least Absolute Residual, or Bisquare method.


Inputs/Outputs

   •       Coefficient Constraint —


                                                    © National Instruments 3281

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3281 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3282 ordinal=3282 -->
## Functions

Functions


             Coefficient Constraint specifies the constraints on Polynomial Coefficients of certain orders by
             setting the coefficient of order to coefficient. Use Coefficient Constraint if you know the exact
            values of certain polynomial coefficients.

                     •      order —

                order specifies the constrained order.

                     •       coefficient —

                  coefficient sets the coefficient of the specified order.


               •      polynomial order —

           polynomial order specifies the order of the polynomial that fits to the data set. The default is 2.

           polynomial order must be greater than or equal to 0. If polynomial order is less than zero, this
              VI sets Polynomial Coefficients to an empty array and returns an error. In real applications,
           polynomial order is less than 10. If polynomial order is greater than 25, the VI sets the
              coefficients in Polynomial Coefficients to zero and returns a warning. If polynomial order is
             high, a large range of X causes the polynomial fit result to diverge.

               •      Y —

           Y is the array of dependent values. The number of sample points in Y must be greater than
           polynomial order. If the number of sample points is less than or equal to polynomial order, this
              VI sets Polynomial Coefficients to an empty array and returns an error.

               •     X —

          X is the array of independent values. The number of sample points in X must be greater than
           polynomial order. If the number of sample points is less than or equal to polynomial order, this
              VI sets Polynomial Coefficients to an empty array and returns an error. X must be the same size
            as Y.

               •      Weight —

           Weight is the array of weights for the observations (X, Y). Weight must be the same size as Y. If
           you do not wire an input to Weight, the VI sets all elements of Weight to 1.

                    If an element of Weight is less than 0, the VI uses the absolute value of the element.

               •      tolerance —

3282   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3282 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3283 ordinal=3283 -->
## Functions

Functions


  tolerance determines when to stop the iterative adjustment of Polynomial Coefficients when
  you use the Least Absolute Residual or Bisquare methods. For the Least Absolute Residual
  method, if the relative difference between residue in two successive iterations is less than
  tolerance, this VI returns the resulting Polynomial Coefficients. For the Bisquare method, if any
  relative difference between Polynomial Coefficients in two successive iterations is less than
  tolerance, this VI returns the resulting Polynomial Coefficients.

   If tolerance is less than or equal to 0, the VI sets tolerance to 0.0001.

•     method —

  method specifies the fitting method.

  0    Least Square (default)
  1    Least Absolute Residual
  2   Bisquare

•      algorithm —

  algorithm specifies the algorithm the VI uses to compute Best Polynomial Fit. Use SVD for
  Rank Deficient H if all other algorithms are unsuccessful.

  0   SVD (default)
  1   Givens
  2   Givens2
  3   Householder
  4   LU Decomposition
  5   Cholesky
  6   SVD for Rank Deficient H

•      Best Polynomial Fit —

  Best Polynomial Fit returns the y-values of the polynomial curve that best fits the input values.

•      Polynomial Coefficients —

  Polynomial Coefficients returns the coefficients of the fitted model in ascending order of power.
  The total number of elements in Polynomial Coefficients is m+ 1, where mis the polynomial
  order.

•       error —


                                                   © National Instruments 3283

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3283 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3284 ordinal=3284 -->
## Functions

Functions


             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

               •      residue —

            residue returns the weighted mean error of the fitted model. If method is Least Absolute
          Residual, residue is the weighted mean absolute error. Otherwise, residue is the weighted
         mean square error.


       This VI fits data to a polynomial function of the general form described by the
       following equation:


      where frepresents the output sequence Best Polynomial Fit, xrepresents the input
      sequence X, arepresents Polynomial Coefficients, and mrepresents polynomial
       order. This VI finds the value of athat best fits the observations (X, Y).

      The following equation specifically describes the polynomial curve resulting from the
       general polynomial fit algorithm:


           If the noise of Y is Gaussian distributed, use the Least Square method. The following
        illustration shows the general polynomial fit result using this method.


3284   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3284 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3285 ordinal=3285 -->
## Functions

Functions


When you use the Least Square method, this VI finds the Polynomial Coefficients of
the polynomial model by minimizing the residue according to the following equation:


where Nis the length of Y, wi is the ith element of Weight, fi is the ith element of Best
Polynomial Fit, and yi is the ith element of Y.

The Least Absolute Residual and Bisquare fitting methods are robust fitting methods.
Use these methods if outliers in the observations exist. The following illustration
compares the fit results of the Least Square, Least Absolute Residual, and Bisquare
fitting methods. In most cases, the Bisquare method is less sensitive to outliers than
the Least Absolute Residual method.


                                                    © National Instruments 3285

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3285 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3286 ordinal=3286 -->
## Functions

Functions


     When you use the Least Absolute Residual method, this VI finds the Polynomial
       Coefficients of the polynomial model by minimizing the residue according to the
       following equation:


     When you use the Bisquare method, this VI obtains the Polynomial Coefficients using
      an iterative process, as shown in the following illustration, and calculates the residue
       using the same formula as in the Least Square method.


3286   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3286 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3287 ordinal=3287 -->
## Functions

Functions


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Fitting\Regression Solver.vi

GeneralGeneral LinearLinear FitFit

Finds the k-dimension linear curve values and the set of k-dimension linear fit
coefficients, which describe the k-dimension linear curve that best represents the
input data set using the Least Square, Least Absolute Residual, or Bisquare method.


                                                    © National Instruments 3287

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3287 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3288 ordinal=3288 -->
## Functions

Functions

      Inputs/Outputs

               •      covariance selector —

            covariance selector indicates whether the VI computes the covariance matrix.

               •      Y —

           Y is the observed data set Y. The number of elements in Y must equal the number of rows in H.

               •    H —

        H is the matrix that represents the formula you use to fit the data set (X, Y). Hij are the function
            values of Xi.

               •      Weight —

           Weight is the array of weights for the observations Y. Weight must be the same size as Y. If you
          do not wire an input to Weight, this VI sets all elements of Weight to 1.

               •      tolerance —

            tolerance determines when to stop the iterative adjustment of Coefficients when you use the
            Least Absolute Residual or Bisquare methods. For the Least Absolute Residual method, if the
              relative difference of the weighted mean error of the polynomial fit in two successive iterations is
              less than tolerance, this VI returns the resulting Polynomial Coefficients. For the Bisquare
           method, if any relative difference between Polynomial Coefficients in two successive iterations
                is less than tolerance, this VI returns the resulting Polynomial Coefficients.

               •     method —

          method specifies the fitting method.

               •      algorithm —

            algorithm specifies the algorithm this VI uses to compute Best Fit. Use the SVD for Rank
         Deficient H algorithm only if H is rank deficient or does not have a full rank and if all other
            algorithms are unsuccessful.

               •      Best Fit —

            Best Fit is the fitted data computed by using Coefficients.

               •       Coefficients —


3288   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3288 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3289 ordinal=3289 -->
## Functions

Functions


     Coefficients is the set of coefficients that minimize chi squared.

   •      Covariance —

    Covariance is the matrix of covariance Cwith k-by-kelements.

   •      Weight Out —

    Weight Out returns the actual weight of general linear fitting if method is Bisquare. If method
      is Least Square or Least Absolute Residual, Weight Out returns the value you enter
     for Weight.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

   •      residue —

    residue returns the weighted mean error of the fitted model. If method is Least Absolute
   Residual, residue is the weighted mean absolute error. Otherwise, residue is the weighted
   mean square error.

CubicCubic SplineSpline FitFit

Uses cubic spline fitting to smooth a data set (X, Y) according to the balance
parameter.


Inputs/Outputs

   •      Y —

    Y is the array of dependent values. Y must contain at least two points.

   •     X —

                                                    © National Instruments 3289

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3289 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3290 ordinal=3290 -->
## Functions

Functions


          X is the array of independent values. X must be the same size as Y. The elements of X must be in
            ascending order.

               •      Weight —

           Weight is the array of weights for the observations (X, Y). Weight must be the same size as Y.
           Weight also must contain non-zero elements. If an element in Weight is less than 0, the VI uses
            the absolute value of the element.

                    If you do not wire an input to Weight, the VI sets all elements of Weight to 1.

               •      balance parameter —

           balance parameter specifies the balance between the smoothness of the cubic spline fit and the
            accuracy with which it fits the observations. balance parameter must fall within the range [0, 1].
                    If balance parameter is 0, the cubic spline fit is equivalent to a linear fit. If balance parameter is
               1, the cubic spline fit interpolates between the data points.

                    If balance parameter is out of the range [0, 1], this VI calculates an appropriate value for balance
           parameter automatically according to the values of X.

               •     Smoothness —

          Smoothness controls the smoothness for each interval between two contiguous data points.
          The larger the Smoothness, the smoother the curve. The number of elements in Smoothness
          must be n–1, where nis the length of Y. If Smoothness is unwired, this VI sets all elements of
          Smoothness to 1.

               •      Best Cubic Spline Fit —

            Best Cubic Spline Fit returns the y-values of the fitted model.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       This VI fits the observations (X, Y) by minimizing the following function:


3290   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3290 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3291 ordinal=3291 -->
## Functions

Functions

pis the balance parameter. wi is the ith element of Weight. yi is the ith element of Y.
xi is the ith element of X. f"(x) is the second-order derivative of the cubic spline
function, f(x). λ(x) is the piecewise constant function

λ(x) = λi, xi ≤ x< xi+1, for i= 0, 1, … , n–2

where λi is the ith element of Smoothness.

If p= 0, the fitted model is equivalent to a linear model. If p= 1, the fitting is equivalent
to cubic spline interpolation. pmust fall in the range [0, 1] to make the fitted curve
both close to the observations and smooth. The closer pis to 0, the smoother the
fitted curve. The closer pis to 1, the closer the fitted curve is to the observations. The
following front panel shows the fit results when ptakes different values.


B-SplineB-Spline FitFit

Uses B-spline fitting to smooth a data set.


                                                    © National Instruments 3291

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3291 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3292 ordinal=3292 -->
## Functions

Functions


            • 1D B-Spline Fit VI
            • nD B-Spline Fit VI

     1D B-Spline Fit VI

      The 1D B-Spline Fit VI calculates Best BSpline Fit X and Best BSpline Fit Y by
       minimizing the residue according to the following equation:


      where Nis the length of Y, wi is the ith element of Weight, (xi,yi) is the ith pair of the
       input sequences (X, Y), (x'i,y'i) is the ith pair of (Best BSpline Fit X, Best BSpline Fit Y),
      and the norm symbols (||) on both sides of the function compute the l2 norm of a
        vector. The standard B-Spline basis functions construct the B-Spline curve (x'i,y'i).

      The following illustration shows a typical B-Spline Fit result.


3292   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3292 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3293 ordinal=3293 -->
## Functions

Functions

nD B-Spline Fit VI

The nD B-Spline Fit VI calculates the Best BSpline Fit by minimizing the residue
according to the following equation:


where Di is the ith row of Data and D'i is the ith row of Best BSpline Fit.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Fitting\B Spline Fitting
   Demo.vi

1D1D B-SplineB-Spline FitFit VIVI

Uses B-spline fitting to smooth a data set.


Inputs/Outputs

   •      # of control points —

    # of control points specifies the number of control points that fit to the data set. # of control
    points must be greater than degree. The default is 10.

   •      Y —

    Y is the array of dependent values. Y must contain at least two points.

   •     X —


                                                    © National Instruments 3293

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3293 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3294 ordinal=3294 -->
## Functions

Functions


          X is the array of independent values. X must be the same size as Y.

               •      Weight —

           Weight is the array of weights for the observations (X, Y). Weight must be the same size as Y.
           Weight also must contain non-zero elements. If an element in Weight is less than 0, the VI uses
            the absolute value of the element.

                    If you do not wire an input to Weight, the VI sets all elements of Weight to 1.

               •      degree —

           degree specifies the order of polynomials that form the B-spline curve and fit to the data set.
          The default value is 3.

               •      parameter selection —

           parameter selection specifies the method that computes the interim knot vector.

           0    equally spaced
           1    chord length
           2     centripetal (default)

               •      Best BSpline Fit Y —

            Best BSpline Fit Y returns the y-values of the B-Spline curve that best fit the input data set (X, Y).

               •      Best BSpline Fit X —

            Best BSpline Fit X returns the x-values of the B-Spline curve that best fit the input data set (X, Y).

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

               •      residue —

            residue returns the weighted mean square error of the fitted model.


3294   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3294 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3295 ordinal=3295 -->
## Functions

Functions

1D B-Spline Fit VI

The 1D B-Spline Fit VI calculates Best BSpline Fit X and Best BSpline Fit Y by
minimizing the residue according to the following equation:


where Nis the length of Y, wi is the ith element of Weight, (xi,yi) is the ith pair of the
input sequences (X, Y), (x'i,y'i) is the ith pair of (Best BSpline Fit X, Best BSpline Fit Y),
and the norm symbols (||) on both sides of the function compute the l2 norm of a
vector. The standard B-Spline basis functions construct the B-Spline curve (x'i,y'i).

The following illustration shows a typical B-Spline Fit result.


nDnD B-SplineB-Spline FitFit VIVI

Uses B-spline fitting to smooth a data set.


                                                    © National Instruments 3295

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3295 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3296 ordinal=3296 -->
## Functions

Functions


      Inputs/Outputs

               •      # of control points —

           # of control points specifies the number of control points that fit to the data set. # of control
            points must be greater than degree. The default is 10.

               •      Data —

           Data specifies the multi-dimension value to fit in rows.

               •      Weight —

           Weight is the array of weights for the input data. Weight must be the same size as the number of
           rows in Data. Weight also must contain non-zero elements. If an element in Weight is less than 0,
            the VI uses the absolute value of the element.

                    If you do not wire an input to Weight, the VI sets all elements of Weight to 1.

               •      degree —

           degree specifies the order of polynomials that form the B-spline curve and fit to the data set.
          The default value is 3.

               •      parameter selection —

           parameter selection specifies the method that computes the interim knot vector.

           0    equally spaced
           1    chord length
           2     centripetal (default)

               •      Best BSpline Fit —

            Best BSpline Fit returns the B-Spline curve that best fits the input Data in rows.

               •       error —


3296   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3296 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3297 ordinal=3297 -->
## Functions

Functions


    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

   •      residue —

    residue returns the weighted mean square error of the fitted model.


nD B-Spline Fit VI

The nD B-Spline Fit VI calculates the Best BSpline Fit by minimizing the residue
according to the following equation:


where Di is the ith row of Data and D'i is the ith row of Best BSpline Fit.

FittingFitting onon aa SphereSphere

Determines the best spherical fit on a cloud of points in 3D.


Inputs/Outputs

   •     X —

    X is the x coordinates of the points of the cloud.

   •      Y —

    Y is the y coordinates of the points of the cloud.

   •     Z —

    Z is the z coordinates of the points of the cloud.


                                                    © National Instruments 3297

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3297 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3298 ordinal=3298 -->
## Functions

Functions

               •       x0, y0, z0 —

             x0, y0, z0 are the calculated midpoints of the given cloud.

               •        r —

               r is the calculated radius of the given cloud.

               •       error —

             error returns any error or warning condition from the VI. Most error situations result from
            discrepancies between the sizes of X, Y, and Z. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The min-functional is based on an uncommon idea: find x0, y0, z0, and r with


       This leads to a simple linear equation in x0, y0, z0 where (xi, yi, zi) are the given points,
        (x0, y0, z0) is the unknown midpoint, and r is the unknown radius.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Fitting\Sphere Fit.vi

     NonlinearNonlinear CurveCurve FitFit

      Uses the Levenberg-Marquardt algorithm to determine the set of parameters that best
          fit the set of input data points (X, Y) as expressed by a nonlinear function y= f(x,a),
      where ais the set of parameters. You must manually select the polymorphic instance
       to use.


3298   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3298 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3299 ordinal=3299 -->
## Functions

Functions

   • Nonlinear Curve Fit LM VI
   • Nonlinear Curve Fit LM formula string VI

This VI uses the Levenberg-Marquardt method to calculate the best fit parameters that
minimize the weighted mean square error between the observations in Y and the best
nonlinear fit. The following equation defines the curve model:

y[i] = f(x[i], a0, a1, a2, …)

where a0, a1, a2, … are the Parameters.

The Levenberg-Marquardt method does not require yto have a linear relationship with
the Parameters.

The Hessian matrix is a common matrix in numerical optimization methods, such as
the Newton method. To avoid the weakness of the singular Hessian matrix, the
Levenberg-Marquardt method adds a positive definite diagonal matrix to the Hessian
matrix. This positive definite diagonal matrix is the main difference between the
Levenberg-Marquardt method and the Gauss-Newton method. Refer to Numerical
Optimizationin the Mathematics Related Documentation topic for more information
about the Levenberg-Marquardt method.

You can use the nonlinear Levenberg-Marquardt method to fit linear or nonlinear
curves. However, when you fit a linear curve, the General Linear Fit VI is more efficient
than this VI. You must verify the results you obtain with the Levenberg-Marquardt
method because the method does not always guarantee a correct result.

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Mathematics\Fitting\Ellipse fit.vi
   • labview\examples\Mathematics\Fitting\Sum of 3 Gaussians
   with offset fit.vi
   • labview\examples\Mathematics\Fitting\Gaussian surface
   with offset fit.vi


                                                    © National Instruments 3299

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3299 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3300 ordinal=3300 -->
## Functions

Functions

      NonlinearNonlinear CurveCurve FitFit LMLM VIVI

      Uses the Levenberg-Marquardt algorithm to determine the set of parameters that best
          fit the set of input data points (X, Y) as expressed by a nonlinear function y= f(x,a),
      where ais the set of parameters. You must manually select the polymorphic instance
       to use.


      Inputs/Outputs

               •      data —

           data specifies static data that the user-defined function needs at run time.

               •        f(x,a) —

               f(x,a) is a reference to the VI that implements the fitting model. ais the set of parameters
           LabVIEW calculates.

           Use the VI template located at labview\vi.lib\gmath\NumericalOptimization\LM
         model function and gradient.vit to create the VI from a template.

               •      Y —

           Y specifies the array of dependent values, or the observations. The number of input points must
          be greater than zero.

               •     X —

          X specifies the array of independent values. The number of input points must be greater than
              zero.

               •      Weight —


3300   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3300 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3301 ordinal=3301 -->
## Functions

Functions


  Weight is the array of weights for the observations Y. If Weight is unwired, this VI sets all
  elements of Weight to 1.

   If Weight has fewer elements than Y, this VI pads the end of Weight with ones so that the length
  of Weight equals the length of Y. If Weight has more elements than Y, this VI ignores the extra
  elements at the end of Weight. If an element in Weight is less than 0, this VI uses the absolute
  value of the element.

•        initial parameters —

   initial parameters specifies the initial guess for best fit parameters. The length of initial
  parameters must equal the length of ain f(x,a).

  The success of the nonlinear curve fit depends on how close the initial parameters are to the
  best fit parameters. Therefore, use any available resources to obtain good initial guess
  parameters to the solution before you use this VI.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      termination —

  termination specifies the stopping conditions for the fitting process.

      •     max iteration —

     max iteration specifies the largest number of iterations of the fitting routine. If the number
       of iterations exceeds max iterations, the fitting process terminates.

      •      tolerance —

      tolerance specifies the relative change in the weighted distance between Y and the current
          fit. If the relative change falls below tolerance, the fitting process terminates.


•     number of function calls —

  number of function calls returns the number of times LabVIEW called f(x,a) during the fitting
  process.

•      best nonlinear fit —


                                                   © National Instruments 3301

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3301 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3302 ordinal=3302 -->
## Functions

Functions


            best nonlinear fit returns the y-values of the fitted model that correspond to the independent
            values in X.

               •      best fit parameters —

            best fit parameters returns the array of parameters that minimizes the weighted mean square
             error between the best nonlinear fit and the observations in Y.

               •      covariance —

            covariance returns the matrix of covariances.

          Cjk is the covariance between a[j] and a[k]. c[jj] is the variance of a[j]. This VI generates the
            covariance, C, according to the following equation: C= (0.5D)^–1 where Dis the Hessian of the
             function with respect to its parameters.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •      residue —

            residue returns the weighted mean square error between the best nonlinear fit and Y.


       This VI uses the Levenberg-Marquardt method to calculate the best fit parameters that
      minimize the weighted mean square error between the observations in Y and the best
       nonlinear fit. The following equation defines the curve model:

        y[i] = f(x[i], a0, a1, a2, …)

      where a0, a1, a2, … are the Parameters.

      The Levenberg-Marquardt method does not require yto have a linear relationship with
       the Parameters.

      The Hessian matrix is a common matrix in numerical optimization methods, such as
       the Newton method. To avoid the weakness of the singular Hessian matrix, the
      Levenberg-Marquardt method adds a positive definite diagonal matrix to the Hessian
       matrix. This positive definite diagonal matrix is the main difference between the


3302   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3302 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3303 ordinal=3303 -->
## Functions

Functions

Levenberg-Marquardt method and the Gauss-Newton method. Refer to Numerical
Optimizationin the Mathematics Related Documentation topic for more information
about the Levenberg-Marquardt method.

You can use the nonlinear Levenberg-Marquardt method to fit linear or nonlinear
curves. However, when you fit a linear curve, the General Linear Fit VI is more efficient
than this VI. You must verify the results you obtain with the Levenberg-Marquardt
method because the method does not always guarantee a correct result.

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Mathematics\Fitting\Ellipse fit.vi
   • labview\examples\Mathematics\Fitting\Sum of 3 Gaussians
   with offset fit.vi
   • labview\examples\Mathematics\Fitting\Gaussian surface
   with offset fit.vi

NonlinearNonlinear CurveCurve FitFit LMLM formulaformula stringstring VIVI

Uses the Levenberg-Marquardt algorithm to determine the set of parameters that best
fit the set of input data points (X, Y) as expressed by a nonlinear function y= f(x,a),
where ais the set of parameters. You must manually select the polymorphic instance
to use.


Inputs/Outputs

   •        initial parameters —


                                                    © National Instruments 3303

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3303 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3304 ordinal=3304 -->
## Functions

Functions


               initial parameters specifies the initial guess for best fit parameters. The length of initial
           parameters must equal the length of Parameters in model description.

          The success of the nonlinear curve fit depends on how close the initial parameters are to the
            best fit parameters. Therefore, use any available resources to obtain good initial guess
           parameters to the solution before you use this VI.

               •      Y —

           Y specifies the array of dependent values, or the observations. The number of input points must
          be greater than zero.

               •     X —

          X specifies the array of independent values. The number of input points must be greater than
              zero.

               •      Weight —

           Weight is the array of weights for the observations Y. If Weight is unwired, this VI sets all
           elements of Weight to 1.

                    If Weight has fewer elements than Y, this VI pads the end of Weight with ones so that the length
             of Weight equals the length of Y. If Weight has more elements than Y, this VI ignores the extra
           elements at the end of Weight. If an element in Weight is less than 0, this VI uses the absolute
            value of the element.

               •     model description —

          model description specifies the formula string description of the model to which you want to
            apply a nonlinear curve fit. Where the Formula Nodes and the parser in the Mathematics VIs
                differ, this VI uses the parser syntax. For example, for exponentiation, use the parser syntax ^
             rather than the Formula Node syntax **.

                     •     model —

              model is a string describing the model equation. The formula can contain any number of
                  valid variables.

                     •      Parameters —

               Parameters is an array of strings of the unknown parameters.


3304   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3304 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3305 ordinal=3305 -->
## Functions

Functions


      •      x —

      x specifies the independent variable.


•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      termination —

  termination specifies the stopping conditions for the fitting process.

      •     max iteration —

     max iteration specifies the largest number of iterations of the fitting routine. If the number
       of iterations exceeds max iterations, the fitting process terminates.

      •      tolerance —

      tolerance specifies the relative change in the weighted distance between Y and the current
          fit. If the relative change falls below tolerance, the fitting process terminates.


•      best nonlinear fit —

  best nonlinear fit returns the y-values of the fitted model that correspond to the independent
  values in X.

•      best fit parameters —

  best fit parameters returns the array of parameters that minimizes the weighted mean square
  error between the best nonlinear fit and the observations in Y.

•      covariance —

  covariance returns the matrix of covariances.

  Cjk is the covariance between a[j] and a[k]. c[jj] is the variance of a[j]. This VI generates the
  covariance, C, according to the following equation: C= (0.5D)^–1 where Dis the Hessian of the
  function with respect to its parameters.

•       error out —

                                                   © National Instruments 3305

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3305 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3306 ordinal=3306 -->
## Functions

Functions


             error out contains error information. This output provides standard error out functionality.

               •      residue —

            residue returns the weighted mean square error between the best nonlinear fit and Y.


       This VI uses the Levenberg-Marquardt method to calculate the best fit parameters that
      minimize the weighted mean square error between the observations in Y and the best
       nonlinear fit. The following equation defines the curve model:

        y[i] = f(x[i], a0, a1, a2, …)

      where a0, a1, a2, … are the Parameters.

      The Levenberg-Marquardt method does not require yto have a linear relationship with
       the Parameters.

      The Hessian matrix is a common matrix in numerical optimization methods, such as
       the Newton method. To avoid the weakness of the singular Hessian matrix, the
      Levenberg-Marquardt method adds a positive definite diagonal matrix to the Hessian
       matrix. This positive definite diagonal matrix is the main difference between the
      Levenberg-Marquardt method and the Gauss-Newton method. Refer to Numerical
     Optimizationin the Mathematics Related Documentation topic for more information
      about the Levenberg-Marquardt method.

      You can use the nonlinear Levenberg-Marquardt method to fit linear or nonlinear
       curves. However, when you fit a linear curve, the General Linear Fit VI is more efficient
      than this VI. You must verify the results you obtain with the Levenberg-Marquardt
      method because the method does not always guarantee a correct result.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Fitting\Ellipse fit.vi
            • labview\examples\Mathematics\Fitting\Sum of 3 Gaussians


3306   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3306 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3307 ordinal=3307 -->
## Functions

Functions

   with offset fit.vi
  • labview\examples\Mathematics\Fitting\Gaussian surface
   with offset fit.vi

ConstrainedConstrained NonlinearNonlinear CurveCurve FitFit

Uses either the Levenberg-Marquardt algorithm or the trust-region dogleg algorithm to
determine the set of parameters that best fit the set of input data points (X, Y) as
expressed by a nonlinear function y= f(x,a), where ais the set of parameters. You must
manually select the polymorphic instance to use.


  • Nonlinear Curve Fit LM bound VI
  • Nonlinear Curve Fit TRDL bound VI

NonlinearNonlinear CurveCurve FitFit LMLM boundbound VIVI

Uses either the Levenberg-Marquardt algorithm or the trust-region dogleg algorithm to
determine the set of parameters that best fit the set of input data points (X, Y) as
expressed by a nonlinear function y= f(x,a), where ais the set of parameters. You must
manually select the polymorphic instance to use.


Inputs/Outputs

   •      data —


                                                    © National Instruments 3307

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3307 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3308 ordinal=3308 -->
## Functions

Functions


           data specifies static data that the user-defined function needs at run time.

               •        f(x,a) —

               f(x,a) is a reference to the VI that implements the fitting model. ais the set of parameters
           LabVIEW calculates.

           Use the VI template located at labview\vi.lib\gmath\NumericalOptimization\LM
         model function and gradient.vit to create the VI from a template.

               •      Y —

           Y specifies the array of dependent values. The number of input points must be greater than zero
          and greater than the number of initial parameters. The number of elements in Y must be equal
             to the number of elements in X.

               •     X —

          X specifies the array of independent values. The number of input points must be greater than
            zero and greater than the number of initial parameters. The number of elements in X must be
            equal to the number of elements in Y.

               •      Weight —

           Weight is the array of weights for the observations Y. If Weight is unwired, this VI sets all
           elements of Weight to 1.

                    If Weight has fewer elements than Y, this VI pads the end of Weight with ones so that the length
             of Weight equals the length of Y. If Weight has more elements than Y, this VI ignores the extra
           elements at the end of Weight. If an element in Weight is less than 0, this VI uses the absolute
            value of the element.

               •        initial parameters —

               initial parameters specifies the initial guess for a solution. The success of the nonlinear curve fit
           depends on how close the initial parameters are to the solution. Therefore, use any available
            resources to obtain good initial guess coefficients to the solution before you use this VI.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      termination —

3308   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3308 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3309 ordinal=3309 -->
## Functions

Functions


  termination specifies the stopping conditions for the fitting process.

      •     max iteration —

     max iteration specifies the largest number of iterations of the fitting routine. If the number
       of iterations exceeds max iterations, the fitting process terminates.

      •      tolerance —

      tolerance specifies the relative change in the weighted distance between Y and the current
          fit. If the relative change falls below tolerance, the fitting process terminates.


•      parameter bounds —

  parameter bounds is a cluster that contains the upper and lower numeric limits for the
  parameters being optimized.

      •      parameter minimum —

      parameter minimum contains the lowest allowed value of the parameters being optimized.
     The array does not accept values of NaN.

     The size of this array must either equal the size of the initial parameters array or be 0.

      •      parameter maximum —

      parameter maximum contains the highest allowed value of the parameters being
      optimized. The array does not accept values of NaN.

     The size of this array must either equal the size of the initial parameters array or be 0.

      For all i, parameter maximum[i] must be greater than or equal to parameter minimum[i]. If
      parameter maximum[i] equals parameter minimum[i], LabVIEW uses that constant value
      throughout the curve fitting.


•     method —

  method specifies the fitting method.

  0    Least Square (default)


                                                   © National Instruments 3309

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3309 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3310 ordinal=3310 -->
## Functions

Functions


           1    Least Absolute Residual
           2   Bisquare

               •     number of function calls —

          number of function calls returns the number of times LabVIEW called f(x,a) during the fitting
             process.

               •      best nonlinear fit —

            best nonlinear fit returns the y-values of the fitted model that correspond to the independent
            values in X.

               •      best fit parameters —

            best fit parameters returns the array of parameters that minimizes the weighted mean square
             error between the solution vector and the observed y-values.

               •      covariance —

            covariance returns the matrix of covariances.

          Cjk is the covariance between a[j] and a[k]. c[jj] is the variance of a[j]. This VI generates the
            covariance, C, according to the following equation: C= (0.5D)^–1 where Dis the Hessian of the
             function with respect to its parameters.

               •      residue —

            residue returns the weighted mean square error between the best nonlinear fit and Y.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      NonlinearNonlinear CurveCurve FitFit TRDLTRDL boundbound VIVI

      Uses either the Levenberg-Marquardt algorithm or the trust-region dogleg algorithm to
      determine the set of parameters that best fit the set of input data points (X, Y) as
       expressed by a nonlinear function y= f(x,a), where ais the set of parameters. You must
      manually select the polymorphic instance to use.


3310   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3310 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3311 ordinal=3311 -->
## Functions

Functions

      Note Uses the trust-region dogleg algorithm to determine the set of
       parameters that best fit the set of input data points (X, Y) as expressed by a
        nonlinear function y= f(x,a), where ais the set of parameters.


Inputs/Outputs

   •      data —

    data specifies static data that the user-defined function needs at run time.

   •        f(x,a) —

     f(x,a) is a reference to the VI that implements the fitting model. ais the set of parameters
    LabVIEW calculates.

    Use the VI template located at labview\vi.lib\gmath\NumericalOptimization\LM
   model function and gradient.vit to create the VI from a template.

   •      Y —

    Y specifies the array of dependent values. The number of input points must be greater than zero
    and greater than the number of initial parameters. The number of elements in Y must be equal
    to the number of elements in X.

   •     X —

    X specifies the array of independent values. The number of input points must be greater than
    zero and greater than the number of initial parameters. The number of elements in X must be
    equal to the number of elements in Y.

   •      Weight —


                                                    © National Instruments 3311

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3311 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3312 ordinal=3312 -->
## Functions

Functions


           Weight is the array of weights for the observations Y. If Weight is unwired, this VI sets all
           elements of Weight to 1.

                    If Weight has fewer elements than Y, this VI pads the end of Weight with ones so that the length
             of Weight equals the length of Y. If Weight has more elements than Y, this VI ignores the extra
           elements at the end of Weight. If an element in Weight is less than 0, this VI uses the absolute
            value of the element.

               •        initial parameters —

               initial parameters specifies the initial guess for a solution. The success of the nonlinear curve fit
           depends on how close the initial parameters are to the solution. Therefore, use any available
            resources to obtain good initial guess coefficients to the solution before you use this VI.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      termination —

            termination specifies the stopping conditions for the fitting process.

                     •     max iteration —

            max iteration specifies the largest number of iterations of the fitting routine. If the number
                  of iterations exceeds max iterations, the fitting process terminates.

                     •      tolerance —

                tolerance specifies the relative change in the weighted distance between Y and the current
                          fit. If the relative change falls below tolerance, the fitting process terminates.


               •      parameter bounds —

           parameter bounds is a cluster that contains the upper and lower numeric limits for the
           parameters being optimized.

                     •      parameter minimum —

               parameter minimum contains the lowest allowed value of the parameters being optimized.


3312   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3312 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3313 ordinal=3313 -->
## Functions

Functions


     The array does not accept values of NaN.

     The size of this array must either equal the size of the initial parameters array or be 0.

      •      parameter maximum —

      parameter maximum contains the highest allowed value of the parameters being
      optimized. The array does not accept values of NaN.

     The size of this array must either equal the size of the initial parameters array or be 0.

      For all i, parameter maximum[i] must be greater than or equal to parameter minimum[i]. If
      parameter maximum[i] equals parameter minimum[i], LabVIEW uses that constant value
      throughout the curve fitting.


•     method —

  method specifies the fitting method.

  0    Least Square (default)
  1    Least Absolute Residual
  2   Bisquare

•     number of function calls —

  number of function calls returns the number of times LabVIEW called f(x,a) during the fitting
  process.

•      best nonlinear fit —

  best nonlinear fit returns the y-values of the fitted model that correspond to the independent
  values in X.

•      best fit parameters —

  best fit parameters returns the array of parameters that minimizes the weighted mean square
  error between the solution vector and the observed y-values.

•      covariance —


                                                   © National Instruments 3313

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3313 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3314 ordinal=3314 -->
## Functions

Functions


            covariance returns the matrix of covariances.

          Cjk is the covariance between a[j] and a[k]. c[jj] is the variance of a[j]. This VI generates the
            covariance, C, according to the following equation: C= (0.5D)^–1 where Dis the Hessian of the
             function with respect to its parameters.

               •      residue —

            residue returns the weighted mean square error between the best nonlinear fit and Y.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

     CurveCurve FittingFitting

      Computes the coefficients that best represent the input data based on the chosen
      model type.


      Dialog Box Options

        Option   Description

                  Displays the data and results according to a mathematical model type you specify.

               The model type can be any of the following options:

                             • Linear—       Model
        Type                      Finds the slope and intercept of the line that best represents the input data set in the
                       least-squares sense.

                             • Quadratic—


3314   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3314 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3315 ordinal=3315 -->
## Functions

Functions


Option   Description

             Finds the polynomial curve of order 2 that best represents the input data set in the
              least-squares sense.

                • Spline—

             Returns the spline interpolant of length n.

      ncontains the second derivatives of the spline interpolating function g(x) at the
             tabulated points ξ, where i= 0, 1, …, n– 1.

                • Polynomial—

             Finds the set of polynomial fit coefficients that best represents the input data set in
             the least-squares sense.

      ◦ Polynomial order—

                Must be greater than or equal to zero. If Polynomial order is less than zero, the
                 Express VI returns an error. The default is 5. This option is available only when
               you select the Polynomial option.

               The value of polynomial order must observe the following relationship: 0 ≤ m<
        n– 1, where nis the number of sample points, and mis Polynomial order.

                • General least squares linear—

             Finds the k-dimension linear curve values and the set of k-dimension linear fit
               coefficients that best represents the input data set using the least-squares solution.

      ◦ Models—

                   Individual functions of the independent variable. This option is available only
              when you select the General least squares linear option.

                   In the following equation, the models are the functions of x, namely f0(x), f1(x),
             …, fn – 1(x).                                           where a= {a0,

                    a1, a2, …, an – 1}

                • Current Model—


                                                    © National Instruments 3315

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3315 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3316 ordinal=3316 -->
## Functions

Functions


        Option   Description

                       Displays the formula for the currently selected Model Type. This display is available
                      only when you set Model Type to Linear, Quadratic, Spline, Polynomial, or General
                        least squares linear.

                             • Non-linear—

                    Uses the Levenberg-Marquardt algorithm to determine the set of coefficients of the
                      nonlinear model that best represents the input data set in the least-squares sense.
                   The nonlinear model is expressed by a nonlinear function y = f(x,a), where ais the set
                        of coefficients.

          ◦ Independent variable—

                            Specifies the independent variable in Non-linear model. This option is available
                          only when you select the Non-linear option.

          ◦ Maximum iterations—

                    Maximum number of executing iterations. If the Express VI reaches Maximum
                             iterations without finding a solution, the VI returns an error. You must increase
                   Maximum iterations or adjust Initial guesses to find a solution. The default is
                           500. This option is available only when you select the Non-linear option.

          ◦  Initial guesses—

                                  Initial guesses of the solution coefficients. This option is available only when you
                             select the Non-linear option.

                             • Non-linear model—

                        String that describes the model equation. This option is available only when you
                        select the Non-linear option.


                  Displays values generated for the parameters based on the options you select and values
         results
                you enter.


        Data
                  Displays the original data and the best fit.
       Graph


3316   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3316 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3317 ordinal=3317 -->
## Functions

Functions


 Option   Description

        The VI calculates best fit using the following equation. zi = f(xi)A where Ais the best fit
           coefficient.


 Residue          Displays the difference between the original data and the best fit. Graph

Inputs/Outputs

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •      Signals —

     Specifies the observed values of the dependent variable.

   •      Locations —

     Specifies the values of the independent variables.

   •      best fit —

    Returns the fitted data.

    The VI calculates best fit using the following equation. zi = f(xi)A where Ais the best fit
     coefficient.

   •      slope —

    Returns the slope of the calculated best linear fit.

   •      a0 —

    Returns the constant term of the calculated best quadratic fit.

   •      a2 —

    Returns the coefficient of the second-order term.

   •       spline interpolant —

                                                    © National Instruments 3317

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3317 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3318 ordinal=3318 -->
## Functions

Functions


            Returns the second derivative of interpolating function g(x).

             spline interpolant is the second derivative of interpolating function g(x) at points ξ, i = 0, 1,…, n
           – 1.

               •      non-linear coefficients —

            Returns the set of coefficients of the nonlinear model that best represents the input data set in
            the least-squares sense.

               •     mean squared error —

            Returns the mean square error of the best fit.

               •       intercept —

            Returns the intercept of the calculated best linear fit.

               •      polynomial coefficients —

            Returns the coefficients that describe the best polynomial fit. The total number of elements in
           polynomial coefficients is m+ 1, where mis Polynomial order.

               •       error out —

            Contains error information. This output provides standard error out functionality.

               •      a1 —

            Returns the coefficient of the first-order term.

               •      general LS coefficients —

            Returns the set of coefficients that best represent the input data set in the least-squares sense.

               •       residual —

            Returns the difference between the original data and the best fit.


     Components

       String that describes the model equation. This option is available only when you select


3318   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3318 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3319 ordinal=3319 -->
## Functions

Functions

the Non-linear option.

Individual functions of the independent variable. This option is available only when
you select the General least squares linear option.

Initial guesses of the solution coefficients. This option is available only when you
select the Non-linear option.

Uses the Levenberg-Marquardt algorithm to determine the set of coefficients of the
nonlinear model that best represents the input data set in the least-squares sense. The
nonlinear model is expressed by a nonlinear function y = f(x,a), where ais the set of
coefficients.

Finds the k-dimension linear curve values and the set of k-dimension linear fit
coefficients that best represents the input data set using the least-squares solution.

Finds the set of polynomial fit coefficients that best represents the input data set in the
least-squares sense.

Returns the spline interpolant of length n.

Finds the polynomial curve of order 2 that best represents the input data set in the
least-squares sense.

Finds the slope and intercept of the line that best represents the input data set in the
least-squares sense.

Displays the difference between the original data and the best fit.

Displays the original data and the best fit.

Maximum number of executing iterations. If the Express VI reaches Maximum
iterations without finding a solution, the VI returns an error. You must increase
Maximum iterations or adjust Initial guesses to find a solution. The default is 500. This
option is available only when you select the Non-linear option.

Specifies the independent variable in Non-linear model. This option is available only
when you select the Non-linear option.

                                                    © National Instruments 3319

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3319 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3320 ordinal=3320 -->
## Functions

Functions

       Displays the formula for the currently selected Model Type. This display is available
       only when you set Model Type to Linear, Quadratic, Spline, Polynomial, or General
       least squares linear.

       Displays values generated for the parameters based on the options you select and
       values you enter.

      Must be greater than or equal to zero. If Polynomial order is less than zero, the Express
        VI returns an error. The default is 5. This option is available only when you select the
      Polynomial option.

     AdvancedAdvanced CurveCurve FittingFitting

      Use the Advanced Curve Fitting VIs to compute additional fit statistics and coefficients.

      The VIs on this palette can return mathematics error codes.


         Palette Object    Description

                      Removes data points that fall outside a given range or within a given index array.
       Remove Outliers                        You must manually select the polymorphic instance you want to use.


                            Calculates three statistical parameters, SSE, R-square, and RMSE, that describe
        Goodness of Fit
                    how well a fitted model matches the original data set.


         Nonlinear Curve
                            Calculates statistical intervals of the best nonlinear fit for a data set (X, Y).
           Fit Intervals


         Linear Fit          Calculates statistical intervals of the best linear fit for a data set (X, Y). You must
          Intervals         manually select the polymorphic instance to use.


3320   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3320 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3321 ordinal=3321 -->
## Functions

Functions


Palette Object    Description

Exponential Fit    Calculates statistical intervals of the best exponential fit for a data set (X, Y). You
Intervals        must manually select the polymorphic instance to use.


Power Fit          Calculates statistical intervals of the best power fit for a data set (X, Y). You must
Intervals         manually select the polymorphic instance to use.


Gaussian Peak Fit  Calculates statistical intervals of the best Gaussian fit for a data set (X, Y). You
Intervals        must manually select the polymorphic instance to use.


Logarithm Fit      Calculates statistical intervals of the best logarithmic fit for a data set (X, Y). You
Intervals        must manually select the polymorphic instance to use.


Polynomial Fit                   Calculates statistical intervals of the best polynomial fit for a data set (X, Y).
Intervals


Linear Fit         Returns the slope and intercept of the linear fit for a data set (X, Y) using the
Coefficients       Least Square, Least Absolute Residual, or Bisquare method.


Exponential Fit    Returns the amplitude and damping of the exponential fit for a data set (X, Y)
Coefficients       using the Least Square, Least Absolute Residual, or Bisquare method.


Power Fit         Returns the amplitude and power of the power fit for a data set (X, Y) using the
Coefficients       Least Square, Least Absolute Residual, or Bisquare method.


Gaussian Peak Fit  Returns the amplitude, center, and standard deviation of the Gaussian fit for a
Coefficients       data set (X, Y).


Logarithm Fit
                 Returns the amplitude and scale of the logarithmic fit for a data set (X, Y).
Coefficients


                                                    © National Instruments 3321

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3321 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3322 ordinal=3322 -->
## Functions

Functions


         Palette Object    Description

        General                          Returns the Polynomial Coefficients of the general polynomial fit for a data set
        Polynomial Fit                                 (X, Y) using the Least Square, Least Absolute Residue, or Bisquare methods.          Coefficients

     RemoveRemove OutliersOutliers

      Removes data points that fall outside a given range or within a given index array. You
      must manually select the polymorphic instance you want to use.


            • Remove Outliers (Range) VI
            • Remove Outliers (Index) VI
   RemoveRemove OutliersOutliers (Range)(Range) VIVI

      Removes data points that fall outside a given range or within a given index array. You
      must manually select the polymorphic instance you want to use.


      Inputs/Outputs

               •      Y —

           Y is the array of dependent values.

               •     X —

          X is the array of independent values. X must be the same size as Y.

               •      Weight —

3322   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3322 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3323 ordinal=3323 -->
## Functions

Functions


    Weight is the array of weights for the observations (X, Y). Weight must be the same size as Y. If
    Weight is unwired, this VI sets Weight Out to an empty array.

   •      range type —

    range type specifies the axis to which the bounds in Range apply.

   •     Range —

    Range specifies the upper and lower bounds of the range. This VI removes data points that lie on
    or outside the bounds of Range.

       If range type is Y or X, this VI uses the first two elements in Range as the upper and lower
    bounds, respectively, for the given axis. If range type is X and Y, this VI uses the first and second
    elements in Range as the upper and lower bounds for the x-axis and the third and fourth
    elements in Range as the upper and lower bounds for the y-axis.

   •      Y Out —

    Y Out returns the array of dependent values with the outliers removed.

   •     X Out —

    X Out returns the array of independent values with the outliers removed.

   •      Weight Out —

    Weight Out returns the array of weights with the outliers removed.

   •       Outlier Indexes —

    Outlier Indexes returns the array indexes for the outliers of the data set.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

RemoveRemove OutliersOutliers (Index)(Index) VIVI

Removes data points that fall outside a given range or within a given index array. You


                                                    © National Instruments 3323

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3323 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3324 ordinal=3324 -->
## Functions

Functions

      must manually select the polymorphic instance you want to use.


      Inputs/Outputs

               •      Y —

           Y is the array of dependent values.

               •     X —

          X is the array of independent values. X must be the same size as Y.

               •      Weight —

           Weight is the array of weights for the observations (X, Y). Weight must be the same size as Y. If
           Weight is unwired, this VI sets Weight Out to an empty array.

               •      Index —

            Index specifies the array of indexes of the outliers to remove.

               •      Y Out —

           Y Out returns the array of dependent values with the outliers removed.

               •     X Out —

          X Out returns the array of independent values with the outliers removed.

               •      Weight Out —

           Weight Out returns the array of weights with the outliers removed.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


3324   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3324 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3325 ordinal=3325 -->
## Functions

Functions

GoodnessGoodness ofof FitFit

Calculates three statistical parameters, SSE, R-square, and RMSE, that describe how
well a fitted model matches the original data set.


Inputs/Outputs

   •      Y —

    Y is the array of dependent values of the original data set. The number of elements in Y must be
    greater than the degree of freedom.

   •      Best Fit —

    Best Fit is the array of dependent values of the fitted model. Best Fit must be the same size as Y.

   •      Weight —

    Weight is the array of weights for the observations Y. Weight must be the same size as Y. If you
   do not wire an input to Weight, this VI sets all elements of Weight to 1.

       If an element in Weight is less than 0, this VI uses the absolute value of the element.

   •      degree of freedom —

    degree of freedom is the length of Y minus the number of coefficients in the fitted model. The
     default is -1.

       If degree of freedom is less than or equal to 0, this VI sets degree of freedom to the length of Y
    minus 2.

   •     SSE —

    SSE is the summation of square error. The smaller the SSE, the better the fit.

   •      R-square —

    R-square is a normalized parameter to measure the goodness of fit. The closer to 1 the R-square,


                                                    © National Instruments 3325

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3325 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3326 ordinal=3326 -->
## Functions

Functions


            the better the fit.

               •     RMSE —

         RMSE is the root mean square error. The smaller the RMSE, the better the fit.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The statistical parameters SSE, R-square, and RMSE are defined by the following
       equations:


    wi is the ith element of Weight. yi is the ith element of Y. fi is the ith element of Best
         Fit.                            , where   is the mean value of Y. DOFis the degree of freedom.

      NonlinearNonlinear CurveCurve FitFit IntervalsIntervals

       Calculates statistical intervals of the best nonlinear fit for a data set (X, Y).


      Inputs/Outputs

               •      data —

           data specifies static data that the user-defined function needs at run time.


3326   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3326 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3327 ordinal=3327 -->
## Functions

Functions

•        f(x,a) —

   f(x,a) is a reference to the VI that implements the fitting model.

  Use the VI template located at labview\vi.lib\gmath\NumericalOptimization\LM
  model function and gradient.vit to create the VI from a template.

•      confidence level —

  confidence level specifies the level of certainty for the confidence interval. The default is 0.95,
  which means the probability that the best fit falls between Lower Bound and Upper Bound is
  95%. confidence level must be greater than 0 and less than 1.

•      Y —

  Y specifies the array of dependent values. The number of input points must be greater than zero
  and greater than the number of best fit parameters. The number of elements in Y must be equal
  to the number of elements in X.

•     X —

  X specifies the array of independent values. The number of input points must be greater than
  zero and greater than the number of best fit parameters. The number of elements in X must be
  equal to the number of elements in Y.

•      Weight —

  Weight is the array of weights for the observations Y. Weight must be the same size as Y. If you
  do not wire an input to Weight, this VI sets all elements of Weight to 1.

   If an element in Weight is less than 0, this VI uses the absolute value of the element.

•      best fit parameters —

  best fit parameters specifies the array of parameters that minimizes the weighted mean square
  error between the solution vector and the observed y-values.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•     Upper Bound —


                                                   © National Instruments 3327

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3327 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3328 ordinal=3328 -->
## Functions

Functions


          Upper Bound returns the upper bound of the confidence interval.

               •     Lower Bound —

          Lower Bound returns the lower bound of the confidence interval.

               •       delta best fit parameters —

            delta best fit parameters returns the confidence radius of best fit parameters.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


       LinearLinear FitFit IntervalsIntervals

       Calculates statistical intervals of the best linear fit for a data set (X, Y). You must
      manually select the polymorphic instance to use.


            • Confidence Interval (Linear) VI
            • Prediction Interval (Linear) VI

      Confidence Interval

        In the following illustration, the region between the upper and lower confidence
      bounds is the confidence interval.


3328   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3328 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3329 ordinal=3329 -->
## Functions

Functions


Prediction Interval

In the following illustration, the region between the upper and lower prediction
bounds is the prediction interval.


If the noise of Y is Gaussian distributed, use both instances of the polymorphic VI to
calculate the confidence interval and prediction interval. The following block diagram
illustrates the calculation of the confidence interval and the prediction interval using
the Linear Fit Intervals VI. You must fit the observations with the Linear Fit VI using the
Least Square method to obtain the slope and intercept.

                                                    © National Instruments 3329

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3329 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3330 ordinal=3330 -->
## Functions

Functions


   ConfidenceConfidence IntervalInterval (Linear)(Linear) VIVI

       Calculates statistical intervals of the best linear fit for a data set (X, Y). You must
      manually select the polymorphic instance to use.


      Inputs/Outputs

               •      confidence level —

            confidence level specifies the level of certainty for the confidence interval. The default is 0.95,
           which means the probability that the best fit falls between Lower Bound and Upper Bound is
           95%. confidence level must be greater than 0 and less than 1.

               •      Y —

           Y is the array of dependent values. Y must contain at least three points.

               •     X —

          X is the array of independent values. X must be the same size as Y.

               •      Weight —

3330   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3330 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3331 ordinal=3331 -->
## Functions

Functions


    Weight is the array of weights for the observations (X, Y). Weight must be the same size as Y.
    Weight also must contain non-zero elements. If an element in Weight is less than 0, the VI uses
    the absolute value of the element.

       If you do not wire an input to Weight, the VI sets all elements of Weight to 1.

   •      slope —

    slope specifies the slope of the fitted model.

   •       intercept —

    intercept specifies the intercept of the fitted model.

   •     Upper Bound —

    Upper Bound returns the upper bound of the confidence interval.

   •     Lower Bound —

    Lower Bound returns the lower bound of the confidence interval.

   •       delta slope —

    delta slope returns the confidence radius of slope.

   •       delta intercept —

    delta intercept returns the confidence radius of intercept.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Confidence Interval

In the following illustration, the region between the upper and lower confidence
bounds is the confidence interval.


                                                    © National Instruments 3331

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3331 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3332 ordinal=3332 -->
## Functions

Functions


      Prediction Interval

        In the following illustration, the region between the upper and lower prediction
      bounds is the prediction interval.


           If the noise of Y is Gaussian distributed, use both instances of the polymorphic VI to
       calculate the confidence interval and prediction interval. The following block diagram
        illustrates the calculation of the confidence interval and the prediction interval using
       the Linear Fit Intervals VI. You must fit the observations with the Linear Fit VI using the
       Least Square method to obtain the slope and intercept.

3332   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3332 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3333 ordinal=3333 -->
## Functions

Functions


PredictionPrediction IntervalInterval (Linear)(Linear) VIVI

Calculates statistical intervals of the best linear fit for a data set (X, Y). You must
manually select the polymorphic instance to use.


Inputs/Outputs

   •      confidence level —

    confidence level specifies the level of certainty for the prediction interval. The default is 0.95,
    which means the probability that a new dependent value falls between Lower Bound and Upper
   Bound is 95%. confidence level must be greater than 0 and less than 1.

   •      Y —

    Y is the array of dependent values. Y must contain at least three points.

   •     X —

    X is the array of independent values. X must be the same size as Y.

   •      Weight —

                                                    © National Instruments 3333

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3333 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3334 ordinal=3334 -->
## Functions

Functions


           Weight is the array of weights for the observations (X, Y). Weight must be the same size as Y.
           Weight also must contain non-zero elements. If an element in Weight is less than 0, the VI uses
            the absolute value of the element.

                    If you do not wire an input to Weight, the VI sets all elements of Weight to 1.

               •      slope —

            slope specifies the slope of the fitted model.

               •       intercept —

             intercept specifies the intercept of the fitted model.

               •     Upper Bound —

          Upper Bound returns the upper bound of the prediction interval.

               •     Lower Bound —

          Lower Bound returns the lower bound of the prediction interval.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      Confidence Interval

        In the following illustration, the region between the upper and lower confidence
      bounds is the confidence interval.


3334   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3334 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3335 ordinal=3335 -->
## Functions

Functions


Prediction Interval

In the following illustration, the region between the upper and lower prediction
bounds is the prediction interval.


If the noise of Y is Gaussian distributed, use both instances of the polymorphic VI to
calculate the confidence interval and prediction interval. The following block diagram
illustrates the calculation of the confidence interval and the prediction interval using
the Linear Fit Intervals VI. You must fit the observations with the Linear Fit VI using the
Least Square method to obtain the slope and intercept.

                                                    © National Instruments 3335

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3335 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3336 ordinal=3336 -->
## Functions

Functions


      ExponentialExponential FitFit IntervalsIntervals

       Calculates statistical intervals of the best exponential fit for a data set (X, Y). You must
      manually select the polymorphic instance to use.


            • Confidence Interval (Exp) VI
            • Prediction Interval (Exp) VI

      Confidence Interval

        In the following illustration, the region between the upper and lower confidence
      bounds is the confidence interval.


3336   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3336 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3337 ordinal=3337 -->
## Functions

Functions


Prediction Interval

In the following illustration, the region between the upper and lower prediction
bounds is the prediction interval.


If the noise of Y is Gaussian distributed, use both instances of the polymorphic VI to
calculate the confidence interval and prediction interval. The following block diagram
illustrates the calculation of the confidence interval and the prediction interval using
the Exponential Fit Intervals VI. You must fit the observations with the Exponential Fit
VI using the Least Square method to obtain the amplitude and damping.

                                                    © National Instruments 3337

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3337 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3338 ordinal=3338 -->
## Functions

Functions


   ConfidenceConfidence IntervalInterval (Exp)(Exp) VIVI

       Calculates statistical intervals of the best exponential fit for a data set (X, Y). You must
      manually select the polymorphic instance to use.


      Inputs/Outputs

               •      confidence level —

            confidence level specifies the level of certainty for the confidence interval. The default is 0.95,
           which means the probability that the best fit falls between Lower Bound and Upper Bound is
           95%. confidence level must be greater than 0 and less than 1.

               •      Y —

           Y is the array of dependent values. Y must contain at least three points.

               •     X —

          X is the array of independent values. X must be the same size as Y.

               •      Weight —

3338   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3338 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3339 ordinal=3339 -->
## Functions

Functions


    Weight is the array of weights for the observations (X, Y). Weight must be the same size as Y.
    Weight also must contain non-zero elements. If an element in Weight is less than 0, the VI uses
    the absolute value of the element.

       If you do not wire an input to Weight, the VI sets all elements of Weight to 1.

   •      amplitude —

    amplitude specifies the amplitude of the fitted model.

   •     damping —

   damping specifies the damping of the fitted model.

   •     Upper Bound —

    Upper Bound returns the upper bound of the confidence interval.

   •     Lower Bound —

    Lower Bound returns the lower bound of the confidence interval.

   •       delta amplitude —

    delta amplitude returns the confidence radius of amplitude.

   •       delta damping —

    delta damping returns the confidence radius of damping.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Confidence Interval

In the following illustration, the region between the upper and lower confidence
bounds is the confidence interval.


                                                    © National Instruments 3339

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3339 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3340 ordinal=3340 -->
## Functions

Functions


      Prediction Interval

        In the following illustration, the region between the upper and lower prediction
      bounds is the prediction interval.


           If the noise of Y is Gaussian distributed, use both instances of the polymorphic VI to
       calculate the confidence interval and prediction interval. The following block diagram
        illustrates the calculation of the confidence interval and the prediction interval using
       the Exponential Fit Intervals VI. You must fit the observations with the Exponential Fit
        VI using the Least Square method to obtain the amplitude and damping.

3340   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3340 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3341 ordinal=3341 -->
## Functions

Functions


PredictionPrediction IntervalInterval (Exp)(Exp) VIVI

Calculates statistical intervals of the best exponential fit for a data set (X, Y). You must
manually select the polymorphic instance to use.


Inputs/Outputs

   •      confidence level —

    confidence level specifies the level of certainty for the prediction interval. The default is 0.95,
    which means the probability that a new dependent value falls between Lower Bound and Upper
   Bound is 95%. confidence level must be greater than 0 and less than 1.

   •      Y —

    Y is the array of dependent values. Y must contain at least three points.

   •     X —

    X is the array of independent values. X must be the same size as Y.

   •      Weight —

                                                    © National Instruments 3341

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3341 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3342 ordinal=3342 -->
## Functions

Functions


           Weight is the array of weights for the observations (X, Y). Weight must be the same size as Y.
           Weight also must contain non-zero elements. If an element in Weight is less than 0, the VI uses
            the absolute value of the element.

                    If you do not wire an input to Weight, the VI sets all elements of Weight to 1.

               •      amplitude —

           amplitude specifies the amplitude of the fitted model.

               •     damping —

          damping specifies the damping of the fitted model.

               •     Upper Bound —

          Upper Bound returns the upper bound of the prediction interval.

               •     Lower Bound —

          Lower Bound returns the lower bound of the prediction interval.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      Confidence Interval

        In the following illustration, the region between the upper and lower confidence
      bounds is the confidence interval.


3342   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3342 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3343 ordinal=3343 -->
## Functions

Functions


Prediction Interval

In the following illustration, the region between the upper and lower prediction
bounds is the prediction interval.


If the noise of Y is Gaussian distributed, use both instances of the polymorphic VI to
calculate the confidence interval and prediction interval. The following block diagram
illustrates the calculation of the confidence interval and the prediction interval using
the Exponential Fit Intervals VI. You must fit the observations with the Exponential Fit
VI using the Least Square method to obtain the amplitude and damping.

                                                    © National Instruments 3343

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3343 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3344 ordinal=3344 -->
## Functions

Functions


     PowerPower FitFit IntervalsIntervals

       Calculates statistical intervals of the best power fit for a data set (X, Y). You must
      manually select the polymorphic instance to use.


            • Confidence Interval (Power) VI
            • Prediction Interval (Power) VI

      Confidence Interval

        In the following illustration, the region between the upper and lower confidence
      bounds is the confidence interval.


3344   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3344 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3345 ordinal=3345 -->
## Functions

Functions


Prediction Interval

In the following illustration, the region between the upper and lower prediction
bounds is the prediction interval.


If the noise of Y is Gaussian distributed, use both instances of the polymorphic VI to
calculate the confidence interval and prediction interval. The following block diagram
illustrates the calculation of the confidence interval and the prediction interval using
the Power Fit Intervals VI. You must fit the observations with the Power Fit VI using the
Least Square method to obtain the amplitude and power.

                                                    © National Instruments 3345

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3345 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3346 ordinal=3346 -->
## Functions

Functions


   ConfidenceConfidence IntervalInterval (Power)(Power) VIVI

       Calculates statistical intervals of the best power fit for a data set (X, Y). You must
      manually select the polymorphic instance to use.


      Inputs/Outputs

               •      confidence level —

            confidence level specifies the level of certainty for the confidence interval. The default is 0.95,
           which means the probability that the best fit falls between Lower Bound and Upper Bound is
           95%. confidence level must be greater than 0 and less than 1.

               •      Y —

           Y is the array of dependent values. Y must contain at least three points.

               •     X —

          X is the array of independent values. X must be the same size as Y.

               •      Weight —

3346   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3346 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3347 ordinal=3347 -->
## Functions

Functions


    Weight is the array of weights for the observations (X, Y). Weight must be the same size as Y.
    Weight also must contain non-zero elements. If an element in Weight is less than 0, the VI uses
    the absolute value of the element.

       If you do not wire an input to Weight, the VI sets all elements of Weight to 1.

   •      amplitude —

    amplitude specifies the amplitude of the fitted model.

   •     power —

   power specifies the power of the fitted model.

   •     Upper Bound —

    Upper Bound returns the upper bound of the confidence interval.

   •     Lower Bound —

    Lower Bound returns the lower bound of the confidence interval.

   •       delta amplitude —

    delta amplitude returns the confidence radius of amplitude.

   •       delta power —

    delta power returns the confidence radius of power.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Confidence Interval

In the following illustration, the region between the upper and lower confidence
bounds is the confidence interval.


                                                    © National Instruments 3347

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3347 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3348 ordinal=3348 -->
## Functions

Functions


      Prediction Interval

        In the following illustration, the region between the upper and lower prediction
      bounds is the prediction interval.


           If the noise of Y is Gaussian distributed, use both instances of the polymorphic VI to
       calculate the confidence interval and prediction interval. The following block diagram
        illustrates the calculation of the confidence interval and the prediction interval using
       the Power Fit Intervals VI. You must fit the observations with the Power Fit VI using the
       Least Square method to obtain the amplitude and power.

3348   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3348 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3349 ordinal=3349 -->
## Functions

Functions


PredictionPrediction IntervalInterval (Power)(Power) VIVI

Calculates statistical intervals of the best power fit for a data set (X, Y). You must
manually select the polymorphic instance to use.


Inputs/Outputs

   •      confidence level —

    confidence level specifies the level of certainty for the prediction interval. The default is 0.95,
    which means the probability that a new dependent value falls between Lower Bound and Upper
   Bound is 95%. confidence level must be greater than 0 and less than 1.

   •      Y —

    Y is the array of dependent values. Y must contain at least three points.

   •     X —

    X is the array of independent values. X must be the same size as Y.

   •      Weight —

                                                    © National Instruments 3349

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3349 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3350 ordinal=3350 -->
## Functions

Functions


           Weight is the array of weights for the observations (X, Y). Weight must be the same size as Y.
           Weight also must contain non-zero elements. If an element in Weight is less than 0, the VI uses
            the absolute value of the element.

                    If you do not wire an input to Weight, the VI sets all elements of Weight to 1.

               •      amplitude —

           amplitude specifies the amplitude of the fitted model.

               •     power —

          power specifies the power of the fitted model.

               •     Upper Bound —

          Upper Bound returns the upper bound of the prediction interval.

               •     Lower Bound —

          Lower Bound returns the lower bound of the prediction interval.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      Confidence Interval

        In the following illustration, the region between the upper and lower confidence
      bounds is the confidence interval.


3350   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3350 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3351 ordinal=3351 -->
## Functions

Functions


Prediction Interval

In the following illustration, the region between the upper and lower prediction
bounds is the prediction interval.


If the noise of Y is Gaussian distributed, use both instances of the polymorphic VI to
calculate the confidence interval and prediction interval. The following block diagram
illustrates the calculation of the confidence interval and the prediction interval using
the Power Fit Intervals VI. You must fit the observations with the Power Fit VI using the
Least Square method to obtain the amplitude and power.

                                                    © National Instruments 3351

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3351 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3352 ordinal=3352 -->
## Functions

Functions


      GaussianGaussian PeakPeak FitFit IntervalsIntervals

       Calculates statistical intervals of the best Gaussian fit for a data set (X, Y). You must
      manually select the polymorphic instance to use.


            • Confidence Interval (Gauss) VI
            • Prediction Interval (Gauss) VI

      Confidence Interval

        In the following illustration, the region between the upper and lower confidence
      bounds is the confidence interval.


3352   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3352 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3353 ordinal=3353 -->
## Functions

Functions


Prediction Interval

In the following illustration, the region between the upper and lower prediction
bounds is the prediction interval.


If the noise of Y is Gaussian distributed, use both instances of the polymorphic VI to
calculate the confidence interval and prediction interval. The following block diagram
illustrates the calculation of the confidence interval and the prediction interval using
the Gaussian Peak Fit Intervals VI. You must fit the observations with the Gaussian
Peak Fit VI using the Least Square method to obtain the amplitude, center, and

                                                    © National Instruments 3353

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3353 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3354 ordinal=3354 -->
## Functions

Functions

      standard deviation.


   ConfidenceConfidence IntervalInterval (Gauss)(Gauss) VIVI

       Calculates statistical intervals of the best Gaussian fit for a data set (X, Y). You must
      manually select the polymorphic instance to use.


      Inputs/Outputs

               •      confidence level —

            confidence level specifies the level of certainty for the confidence interval. The default is 0.95,
           which means the probability that the best fit falls between Lower Bound and Upper Bound is
           95%. confidence level must be greater than 0 and less than 1.

               •      Y —

           Y is the array of dependent values. Y must contain at least four points.

               •     X —

3354   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3354 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3355 ordinal=3355 -->
## Functions

Functions


  X is the array of independent values. X must be the same size as Y.

•      Weight —

  Weight is the array of weights for the observations (X, Y). Weight must be the same size as Y.
  Weight also must contain non-zero elements. If an element in Weight is less than 0, the VI uses
  the absolute value of the element.

   If you do not wire an input to Weight, the VI sets all elements of Weight to 1.

•      amplitude —

  amplitude specifies the amplitude of the fitted model.

•      center —

  center specifies the center of the fitted model.

•      standard deviation —

  standard deviation is the standard deviation of the fitted model.

•     Upper Bound —

  Upper Bound returns the upper bound of the confidence interval.

•     Lower Bound —

  Lower Bound returns the lower bound of the confidence interval.

•       delta amplitude —

  delta amplitude returns the confidence radius of amplitude.

•       delta center —

  delta center returns the confidence radius of center.

•       error —

  error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
  Code VI to convert the error code or warning into an error cluster.

•       delta standard deviation —


                                                   © National Instruments 3355

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3355 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3356 ordinal=3356 -->
## Functions

Functions


            delta standard deviation returns the confidence radius of standard deviation.


      Confidence Interval

        In the following illustration, the region between the upper and lower confidence
      bounds is the confidence interval.


      Prediction Interval

        In the following illustration, the region between the upper and lower prediction
      bounds is the prediction interval.


3356   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3356 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3357 ordinal=3357 -->
## Functions

Functions


If the noise of Y is Gaussian distributed, use both instances of the polymorphic VI to
calculate the confidence interval and prediction interval. The following block diagram
illustrates the calculation of the confidence interval and the prediction interval using
the Gaussian Peak Fit Intervals VI. You must fit the observations with the Gaussian
Peak Fit VI using the Least Square method to obtain the amplitude, center, and
standard deviation.


PredictionPrediction IntervalInterval (Gauss)(Gauss) VIVI

Calculates statistical intervals of the best Gaussian fit for a data set (X, Y). You must
manually select the polymorphic instance to use.

                                                    © National Instruments 3357

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3357 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3358 ordinal=3358 -->
## Functions

Functions


      Inputs/Outputs

               •      confidence level —

            confidence level specifies the level of certainty for the prediction interval. The default is 0.95,
           which means the probability that a new dependent value falls between Lower Bound and Upper
          Bound is 95%. confidence level must be greater than 0 and less than 1.

               •      Y —

           Y is the array of dependent values. Y must contain at least four points.

               •     X —

          X is the array of independent values. X must be the same size as Y.

               •      Weight —

           Weight is the array of weights for the observations (X, Y). Weight must be the same size as Y.
           Weight also must contain non-zero elements. If an element in Weight is less than 0, the VI uses
            the absolute value of the element.

                    If you do not wire an input to Weight, the VI sets all elements of Weight to 1.

               •      amplitude —

           amplitude specifies the amplitude of the fitted model.

               •      center —

            center specifies the center of the fitted model.

               •      standard deviation —

           standard deviation is the standard deviation of the fitted model.

               •     Upper Bound —


3358   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3358 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3359 ordinal=3359 -->
## Functions

Functions


    Upper Bound returns the upper bound of the prediction interval.

   •     Lower Bound —

    Lower Bound returns the lower bound of the prediction interval.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Confidence Interval

In the following illustration, the region between the upper and lower confidence
bounds is the confidence interval.


Prediction Interval

In the following illustration, the region between the upper and lower prediction
bounds is the prediction interval.


                                                    © National Instruments 3359

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3359 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3360 ordinal=3360 -->
## Functions

Functions


           If the noise of Y is Gaussian distributed, use both instances of the polymorphic VI to
       calculate the confidence interval and prediction interval. The following block diagram
        illustrates the calculation of the confidence interval and the prediction interval using
       the Gaussian Peak Fit Intervals VI. You must fit the observations with the Gaussian
      Peak Fit VI using the Least Square method to obtain the amplitude, center, and
      standard deviation.


      LogarithmLogarithm FitFit IntervalsIntervals

       Calculates statistical intervals of the best logarithmic fit for a data set (X, Y). You must
      manually select the polymorphic instance to use.


3360   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3360 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3361 ordinal=3361 -->
## Functions

Functions


  • Confidence Interval (Log) VI
  • Prediction Interval (Log) VI

Confidence Interval

In the following illustration, the region between the upper and lower confidence
bounds is the confidence interval.


Prediction Interval

In the following illustration, the region between the upper and lower prediction
bounds is the prediction interval.


                                                    © National Instruments 3361

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3361 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3362 ordinal=3362 -->
## Functions

Functions


           If the noise of Y is Gaussian distributed, use both instances of the polymorphic VI to
       calculate the confidence interval and prediction interval. The following block diagram
        illustrates the calculation of the confidence interval and the prediction interval using
       the Logarithm Fit Intervals VI. You must fit the observations with the Logarithm Fit VI
       using the Least Square method to obtain the amplitude and scale.


   ConfidenceConfidence IntervalInterval (Log)(Log) VIVI

       Calculates statistical intervals of the best logarithmic fit for a data set (X, Y). You must
      manually select the polymorphic instance to use.


3362   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3362 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3363 ordinal=3363 -->
## Functions

Functions


Inputs/Outputs

   •      confidence level —

    confidence level specifies the level of certainty for the confidence interval. The default is 0.95,
    which means the probability that the best fit falls between Lower Bound and Upper Bound is
    95%. confidence level must be greater than 0 and less than 1.

   •      Y —

    Y is the array of dependent values. Y must contain at least three points.

   •     X —

    X is the array of independent values. X must be the same size as Y.

   •      Weight —

    Weight is the array of weights for the observations (X, Y). Weight must be the same size as Y.
    Weight also must contain non-zero elements. If an element in Weight is less than 0, the VI uses
    the absolute value of the element.

       If you do not wire an input to Weight, the VI sets all elements of Weight to 1.

   •      amplitude —

    amplitude specifies the amplitude of the fitted model.

   •       scale —

    scale specifies the scale of the fitted model.

   •      base —

    base specifies the base of the logarithm. The default is e, or the natural logarithm.

   •     Upper Bound —

                                                    © National Instruments 3363

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3363 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3364 ordinal=3364 -->
## Functions

Functions


          Upper Bound returns the upper bound of the confidence interval.

               •     Lower Bound —

          Lower Bound returns the lower bound of the confidence interval.

               •       delta amplitude —

            delta amplitude returns the confidence radius of amplitude.

               •       delta scale —

            delta scale returns the confidence radius of scale.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      Confidence Interval

        In the following illustration, the region between the upper and lower confidence
      bounds is the confidence interval.


3364   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3364 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3365 ordinal=3365 -->
## Functions

Functions

Prediction Interval

In the following illustration, the region between the upper and lower prediction
bounds is the prediction interval.


If the noise of Y is Gaussian distributed, use both instances of the polymorphic VI to
calculate the confidence interval and prediction interval. The following block diagram
illustrates the calculation of the confidence interval and the prediction interval using
the Logarithm Fit Intervals VI. You must fit the observations with the Logarithm Fit VI
using the Least Square method to obtain the amplitude and scale.


                                                    © National Instruments 3365

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3365 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3366 ordinal=3366 -->
## Functions

Functions

    PredictionPrediction IntervalInterval (Log)(Log) VIVI

       Calculates statistical intervals of the best logarithmic fit for a data set (X, Y). You must
      manually select the polymorphic instance to use.


      Inputs/Outputs

               •      confidence level —

            confidence level specifies the level of certainty for the prediction interval. The default is 0.95,
           which means the probability that a new dependent value falls between Lower Bound and Upper
          Bound is 95%. confidence level must be greater than 0 and less than 1.

               •      Y —

           Y is the array of dependent values. Y must contain at least three points.

               •     X —

          X is the array of independent values. X must be the same size as Y.

               •      Weight —

           Weight is the array of weights for the observations (X, Y). Weight must be the same size as Y.
           Weight also must contain non-zero elements. If an element in Weight is less than 0, the VI uses
            the absolute value of the element.

                    If you do not wire an input to Weight, the VI sets all elements of Weight to 1.

               •      amplitude —

           amplitude specifies the amplitude of the fitted model.

               •       scale —


3366   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3366 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3367 ordinal=3367 -->
## Functions

Functions


    scale specifies the scale of the fitted model.

   •      base —

    base specifies the base of the logarithm. The default is e, or the natural logarithm.

   •     Upper Bound —

    Upper Bound returns the upper bound of the prediction interval.

   •     Lower Bound —

    Lower Bound returns the lower bound of the prediction interval.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Confidence Interval

In the following illustration, the region between the upper and lower confidence
bounds is the confidence interval.


                                                    © National Instruments 3367

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3367 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3368 ordinal=3368 -->
## Functions

Functions

      Prediction Interval

        In the following illustration, the region between the upper and lower prediction
      bounds is the prediction interval.


           If the noise of Y is Gaussian distributed, use both instances of the polymorphic VI to
       calculate the confidence interval and prediction interval. The following block diagram
        illustrates the calculation of the confidence interval and the prediction interval using
       the Logarithm Fit Intervals VI. You must fit the observations with the Logarithm Fit VI
       using the Least Square method to obtain the amplitude and scale.


3368   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3368 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3369 ordinal=3369 -->
## Functions

Functions

PolynomialPolynomial FitFit IntervalsIntervals

Calculates statistical intervals of the best polynomial fit for a data set (X, Y).

You must manually select the polymorphic instance to use.


  • Confidence Interval (Polynomial) VI
  • Prediction Interval (Polynomial) VI

Confidence Interval

In the following illustration, the region between the upper and lower confidence
bounds is the confidence interval.


Prediction Interval

In the following illustration, the region between the upper and lower prediction
bounds is the prediction interval.


                                                    © National Instruments 3369

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3369 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3370 ordinal=3370 -->
## Functions

Functions


           If the noise of Y is Gaussian distributed, use both instances of the polymorphic VI to
       calculate the confidence interval and prediction interval. The following block diagram
        illustrates the calculation of the confidence interval and the prediction interval using
       the Polynomial Fit Intervals VI. You must fit the observations with the General
      Polynomial Fit VI, using the Least Square method to obtain the Polynomial
       Coefficients.


   ConfidenceConfidence IntervalInterval (Polynomial)(Polynomial) VIVI

       Calculates statistical intervals of the best polynomial fit for a data set (X, Y).

      You must manually select the polymorphic instance to use.

3370   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3370 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3371 ordinal=3371 -->
## Functions

Functions


Inputs/Outputs

   •      confidence level —

    confidence level specifies the level of certainty for the confidence interval. The default is 0.95,
    which means the probability that the best fit falls between Lower Bound and Upper Bound is
    95%. confidence level must be greater than 0 and less than 1.

   •      Y —

    Y is the array of dependent values. The number of sample points in Y must be greater than the
   number of elements in Polynomial Coefficients.

   •     X —

    X is the array of independent values. X must be the same size as Y.

   •      Weight —

    Weight is the array of weights for the observations (X, Y). Weight must be the same size as Y.
    Weight also must contain non-zero elements. If an element in Weight is less than 0, the VI uses
    the absolute value of the element.

       If you do not wire an input to Weight, the VI sets all elements of Weight to 1.

   •      Polynomial Coefficients —

    Polynomial Coefficients specifies coefficients of the fitted model in ascending order of power. If
    the total number of elements in Polynomial Coefficients is m, the polynomial order is m– 1.

   •     Upper Bound —

    Upper Bound returns the upper bound of the confidence interval.

   •     Lower Bound —

    Lower Bound returns the lower bound of the confidence interval.

   •      Delta Polynomial Coefficients —

                                                    © National Instruments 3371

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3371 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3372 ordinal=3372 -->
## Functions

Functions


            Delta Polynomial Coefficients returns the confidence radius of Polynomial Coefficients.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      Confidence Interval

        In the following illustration, the region between the upper and lower confidence
      bounds is the confidence interval.


      Prediction Interval

        In the following illustration, the region between the upper and lower prediction
      bounds is the prediction interval.


3372   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3372 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3373 ordinal=3373 -->
## Functions

Functions


If the noise of Y is Gaussian distributed, use both instances of the polymorphic VI to
calculate the confidence interval and prediction interval. The following block diagram
illustrates the calculation of the confidence interval and the prediction interval using
the Polynomial Fit Intervals VI. You must fit the observations with the General
Polynomial Fit VI, using the Least Square method to obtain the Polynomial
Coefficients.


PredictionPrediction IntervalInterval (Polynomial)(Polynomial) VIVI

Calculates statistical intervals of the best polynomial fit for a data set (X, Y).

You must manually select the polymorphic instance to use.

                                                    © National Instruments 3373

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3373 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3374 ordinal=3374 -->
## Functions

Functions


      Inputs/Outputs

               •      confidence level —

            confidence level specifies the level of certainty for the prediction interval. The default is 0.95,
           which means the probability that a new dependent value falls between Lower Bound and Upper
          Bound is 95%. confidence level must be greater than 0 and less than 1.

               •      Y —

           Y is the array of dependent values. The number of sample points in Y must be greater than the
          number of elements in Polynomial Coefficients.

               •     X —

          X is the array of independent values. X must be the same size as Y.

               •      Weight —

           Weight is the array of weights for the observations (X, Y). Weight must be the same size as Y.
           Weight also must contain non-zero elements. If an element in Weight is less than 0, the VI uses
            the absolute value of the element.

                    If you do not wire an input to Weight, the VI sets all elements of Weight to 1.

               •      Polynomial Coefficients —

           Polynomial Coefficients specifies coefficients of the fitted model in ascending order of power. If
            the total number of elements in Polynomial Coefficients is m, the polynomial order is m– 1.

               •     Upper Bound —

          Upper Bound returns the upper bound of the prediction interval.

               •     Lower Bound —

          Lower Bound returns the lower bound of the prediction interval.

               •       error —

3374   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3374 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3375 ordinal=3375 -->
## Functions

Functions


    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Confidence Interval

In the following illustration, the region between the upper and lower confidence
bounds is the confidence interval.


Prediction Interval

In the following illustration, the region between the upper and lower prediction
bounds is the prediction interval.


                                                    © National Instruments 3375

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3375 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3376 ordinal=3376 -->
## Functions

Functions


           If the noise of Y is Gaussian distributed, use both instances of the polymorphic VI to
       calculate the confidence interval and prediction interval. The following block diagram
        illustrates the calculation of the confidence interval and the prediction interval using
       the Polynomial Fit Intervals VI. You must fit the observations with the General
      Polynomial Fit VI, using the Least Square method to obtain the Polynomial
       Coefficients.


       LinearLinear FitFit CoefficientsCoefficients

       Returns the slope and intercept of the linear fit for a data set (X, Y) using the Least
       Square, Least Absolute Residual, or Bisquare method.


3376   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3376 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3377 ordinal=3377 -->
## Functions

Functions


Inputs/Outputs

   •      Y —

    Y is the array of dependent values. Y must contain at least two points.

   •     X —

    X is the array of independent values. X must be the same size as Y.

   •      Weight —

    Weight is the array of weights for the observations (X, Y). Weight must be the same size as Y.
    Weight also must contain non-zero elements. If an element in Weight is less than 0, the VI uses
    the absolute value of the element.

       If you do not wire an input to Weight, the VI sets all elements of Weight to 1.

   •      tolerance —

    tolerance determines when to stop the iterative adjustment of slope and intercept when you
    use the Least Absolute Residual or Bisquare method. If the relative difference of the weighted
   mean error of the linear fit in two successive iterations is less than tolerance, this VI returns the
     resulting slope and intercept.

       If tolerance is less than or equal to 0, this VI sets tolerance to 0.0001.

   •     method —

   method specifies the fitting method.

    0    Least Square (default)
    1    Least Absolute Residual
    2   Bisquare

   •      slope —

    slope returns the slope of the fitted model.


                                                    © National Instruments 3377

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3377 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3378 ordinal=3378 -->
## Functions

Functions

               •       intercept —

             intercept returns the intercept of the fitted model.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       This VI is similar to the Linear Fit VI but does not return the y-values or weighted mean
       error of the fitted model.

      ExponentialExponential FitFit CoefficientsCoefficients

       Returns the amplitude and damping of the exponential fit for a data set (X, Y) using
       the Least Square, Least Absolute Residual, or Bisquare method.


      Inputs/Outputs

               •      Y —

           Y is the array of dependent values. Y must contain at least two points.

               •     X —

          X is the array of independent values. X must be the same size as Y.

               •      Weight —

           Weight is the array of weights for the observations (X, Y). Weight must be the same size as Y.
           Weight also must contain non-zero elements. If an element in Weight is less than 0, the VI uses
            the absolute value of the element.

                    If you do not wire an input to Weight, the VI sets all elements of Weight to 1.


3378   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3378 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3379 ordinal=3379 -->
## Functions

Functions

   •      tolerance —

    tolerance determines when to stop the iterative adjustment of amplitude and damping when
    you use the Least Square or Bisquare method. If the relative difference of the weighted mean
     error of the exponential fit in two successive iterations is less than tolerance, this VI returns the
     resulting amplitude and damping.

       If tolerance is less than or equal to 0, this VI sets tolerance to 0.0001. tolerance is invalid if
   method is Least Square and refine? is FALSE.

   •     method —

   method specifies the fitting method.

    0    Least Square (default)
    1    Least Absolute Residual
    2   Bisquare

   •       refine? —

     refine? specifies whether to further refine amplitude and damping. The computation time for
     this VI increases if refine? is TRUE. The default is FALSE.

   •      amplitude —

    amplitude returns the amplitude of the fitted model.

   •     damping —

   damping returns the damping of the fitted model.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


This VI is similar to the Exponential Fit VI but does not return the y-values or weighted
mean error of the fitted model.

PowerPower FitFit CoefficientsCoefficients

Returns the amplitude and power of the power fit for a data set (X, Y) using the Least

                                                    © National Instruments 3379

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3379 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3380 ordinal=3380 -->
## Functions

Functions

       Square, Least Absolute Residual, or Bisquare method.


      Inputs/Outputs

               •      Y —

           Y is the array of dependent values. Y must contain at least two points.

               •     X —

          X is the array of independent values. X must be the same size as Y.

               •      Weight —

           Weight is the array of weights for the observations (X, Y). Weight must be the same size as Y. If
           you do not wire an input to Weight, the VI sets all elements of Weight to 1. If an element in
           Weight is less than 0, the VI uses the absolute value of the element.

               •      tolerance —

            tolerance determines when to stop the iterative adjustment of amplitude and power when you
           use the Bisquare method. If the relative difference of the weighted mean error of the power fit in
          two successive iterations is less than tolerance, this VI returns the resulting amplitude and
           power. If tolerance is less than or equal to 0, this VI sets tolerance to 0.0001.

               •     method —

          method specifies the fitting method.

           0    Least Square (default)
           1    Least Absolute Residual
           2   Bisquare

               •      amplitude —

           amplitude returns the amplitude of the fitted model.

               •     power —

3380   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3380 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3381 ordinal=3381 -->
## Functions

Functions


   power returns the power of the fitted model.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


This VI is similar to the Power Fit VI but does not return the y-values or weighted mean
error of the fitted model.

GaussianGaussian PeakPeak FitFit CoefficientsCoefficients

Returns the amplitude, center, and standard deviation of the Gaussian fit for a data
set (X, Y).


Inputs/Outputs

   •        initial guess —

     initial guess specifies the initial guesses of amplitude, center, standard deviation, and offset
     for use in the iterative algorithm. If initial amplitude, initial center, initial standard deviation,
    or initial offset is NaN, this VI calculates the initial guess automatically.

         •        initial amplitude —

           initial amplitude is the initial guess of amplitude.

         •        initial center —

           initial center is the initial guess of center.

         •        initial standard deviation —


                                                    © National Instruments 3381

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3381 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3382 ordinal=3382 -->
## Functions

Functions


                     initial standard deviation is the initial guess of standard deviation.


               •      Y —

           Y is the array of dependent values. Y must contain at least three points.

               •     X —

          X is the array of independent values. X must be the same size as Y.

               •      Weight —

           Weight is the array of weights for the observations (X, Y). Weight must be the same size as Y.
           Weight also must contain non-zero elements. If an element in Weight is less than 0, the VI uses
            the absolute value of the element.

                    If you do not wire an input to Weight, the VI sets all elements of Weight to 1.

               •      tolerance —

            tolerance determines when to stop the iterative adjustment of amplitude, center, and standard
             deviation. If the relative difference of the weighted mean error of the Gaussian fit in two
             successive iterations is less than tolerance, this VI returns the resulting amplitude, center, and
           standard deviation.

                    If tolerance is less than or equal to 0, this VI sets tolerance to 0.0001.

               •     method —

          method specifies the fitting method.

           0    Least Square (default)
           1    Least Absolute Residual
           2   Bisquare

               •      amplitude —

           amplitude returns the amplitude of the fitted model.

               •      center —


3382   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3382 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3383 ordinal=3383 -->
## Functions

Functions


    center returns the center of the fitted model.

   •      standard deviation —

    standard deviation returns the standard deviation of the fitted model.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


This VI is similar to the Gaussian Peak Fit VI but does not return the y-values or
weighted mean error of the fitted model.

LogarithmLogarithm FitFit CoefficientsCoefficients

Returns the amplitude and scale of the logarithmic fit for a data set (X, Y).


Inputs/Outputs

   •      base —

    base specifies the base of the logarithm. The default is e, or the natural logarithm.

   •      Y —

    Y is the array of dependent values. Y must contain at least two points.

   •     X —

    X is the array of independent values. X must be the same size as Y.

   •      Weight —


                                                    © National Instruments 3383

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3383 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3384 ordinal=3384 -->
## Functions

Functions


           Weight is the array of weights for the observations (X, Y). Weight must be the same size as Y. If
           you do not wire an input to Weight, the VI sets all elements of Weight to 1. If an element in
           Weight is less than 0, the VI uses the absolute value of the element.

               •      tolerance —

            tolerance determines when to stop the iterative adjustment of amplitude and scale when you
           use the Least Absolute Residual or Bisquare method. If the relative difference of the weighted
         mean error of the logarithmic fit in two successive iterations is less than tolerance, this VI
             returns the resulting amplitude and scale. If tolerance is less than or equal to 0, this VI sets
            tolerance to 0.0001.

               •     method —

          method specifies the fitting method.

           0    Least Square (default)
           1    Least Absolute Residual
           2   Bisquare

               •      amplitude —

           amplitude returns the amplitude of the fitted model.

               •       scale —

             scale returns the scale of the fitted model.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       This VI is similar to the Logarithm Fit VI but does not return the y-values or weighted
     mean error of the fitted model.

      GeneralGeneral PolynomialPolynomial FitFit CoefficientsCoefficients

       Returns the Polynomial Coefficients of the general polynomial fit for a data set (X, Y)
       using the Least Square, Least Absolute Residue, or Bisquare methods.


3384   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3384 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3385 ordinal=3385 -->
## Functions

Functions


Inputs/Outputs

   •       Coefficient Constraint —

    Coefficient Constraint specifies the constraints on Polynomial Coefficients of certain orders by
     setting the coefficient of order to coefficient. Use Coefficient Constraint if you know the exact
    values of certain polynomial coefficients.

         •      order —

        order specifies the constrained order.

         •       coefficient —

         coefficient sets the coefficient of the specified order.


   •      polynomial order —

    polynomial order specifies the order of the polynomial to fit to the data set.

    polynomial order must be greater than or equal to 0. If polynomial order is less than zero, this
     VI sets Polynomial Coefficients to an empty array and returns an error. polynomial order must
    be less than or equal to 25. If polynomial order is greater than 25, the VI sets the coefficients in
    Polynomial Coefficients to zero and returns a warning. The default is 2.

   •      Y —

    Y is the array of dependent values. The number of sample points in Y must be greater than
    polynomial order. If the number of sample points is less than or equal to polynomial order, this
     VI sets Polynomial Coefficients to an empty array and returns an error.

   •     X —

    X is the array of independent values. The number of sample points in X must be greater than


                                                    © National Instruments 3385

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3385 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3386 ordinal=3386 -->
## Functions

Functions


           polynomial order. If the number of sample points is less than or equal to polynomial order, this
              VI sets Polynomial Coefficients to an empty array and returns an error. X must be the same size
            as Y.

               •      Weight —

           Weight is the array of weights for the observations (X, Y). Weight must be the same size as Y. If
           you do not wire an input to Weight, the VI sets all elements of Weight to 1.

                    If an element of Weight is less than 0, the VI uses the absolute value of the element.

               •      tolerance —

            tolerance determines when to stop the iterative adjustment of Polynomial Coefficients when
           you use the Least Absolute Residual or Bisquare method. For the Least Absolute Residual
           method, if the relative difference of the weighted mean error of the polynomial fit in two
             successive iterations is less than tolerance, this VI returns the resulting Polynomial Coefficients.
            For the Bisquare method, if any relative difference between Polynomial Coefficients in two
             successive iterations is less than tolerance, this VI returns the resulting Polynomial Coefficients.

                    If tolerance is less than or equal to 0, this VI sets tolerance to 0.0001.

               •     method —

          method specifies the fitting method.

           0    Least Square (default)
           1    Least Absolute Residual
           2   Bisquare

               •      algorithm —

            algorithm specifies the algorithm this VI uses to compute Polynomial Coefficients. Use SVD
         for Rank Deficient H if all other algorithms are unsuccessful.

           0   SVD (default)
           1   Givens
           2   Givens2
           3   Householder
           4   LU Decomposition
           5   Cholesky


3386   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3386 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3387 ordinal=3387 -->
## Functions

Functions


    6   SVD for Rank Deficient H

   •      Polynomial Coefficients —

    Polynomial Coefficients returns the coefficients of the fitted model in ascending order of power.
    The total number of elements in Polynomial Coefficients is m+ 1, where mis the polynomial
     order.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


This VI is similar to the General Polynomial Fit VI, but it does not return the y-values or
weighted mean error of the fitted model.

InterpolationInterpolation && ExtrapolationExtrapolation

Use the Interpolation & Extrapolation VIs to perform 1D and 2D interpolation,
piecewise interpolation, polynomial interpolation, and Fourier interpolation.


 Palette               Description Object

 Interpolate   Performs one-dimensional interpolation using a selected method based on the
 1D          lookup table defined by X and Y.


              Performs two-dimensional interpolation using a selected interpolation method
 Interpolate
             based on the lookup table defined by X, Y, and Z, where Z is a 2D array. You must
 2D
             manually select the polymorphic instance to use.


 Interpolate
              Performs two-dimensional interpolation on scattered points.
 2D Scattered


                                                    © National Instruments 3387

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3387 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3388 ordinal=3388 -->
## Functions

Functions


         Palette                       Description
        Object

                     Takes two x domain and y domain arrays and forms X and Y 2D arrays, which are         Create Mesh                          typically used to evaluate and plot functions of two variables. You must manually         Grid (2D)                         select the polymorphic instance to use.


         Spline                     Performs one-dimensional interpolation using the spline interpolation method
         Interpolation                    based on the lookup table defined by X and Y.       1D

        Hermite                     Performs one-dimensional interpolation using the cubic Hermite interpolation         Interpolation                  method based on the lookup table defined by X and Y.       1D


         Create       Takes the piecewise polynomial x locations and a 2D array of coefficients and forms
         Interpolating  the piecewise polynomial cluster for the Evaluate Interpolating Polynomial VI to
        Polynomial   use.


         Evaluate                     Takes the piecewise polynomial cluster and computes the interpolated values yi at         Interpolating                    each xi location.
        Polynomial


                     Performs interpolation by transforming the array X into the frequency domain, zero-
         Interpolate   padding and scaling appropriately for the interpolation factor you want and to
       1D Fourier    maintain correct symmetry in the frequency domain, and then transforming back
                        into the time domain to form the output interpolated array Y out.


                    Works on the assumption that ordered x array is in monotonically increasing or
                      decreasing order and can therefore efficiently search for the relative index of the
        Search
                        location of x value within the x array. The VI starts the search at the starting index
        Ordered
                   and begins by using a fast hunting phase to roughly bracket the location and then
         Table
                     narrows to the final bracket using a bisection search. The VI computes the fractional
                     index location by using linear interpolation.


3388   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3388 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3389 ordinal=3389 -->
## Functions

Functions


 Palette               Description
 Object

 Polynomial               Interpolates or extrapolates the function f at x given a set of n points (x[i]y[i]), where Interpolation                     f(x[i]) = y[i], f is any function, and given a number x value. VI

 Rational               Interpolates or extrapolates f at x value using a rational function. The rational Interpolation               function passes through all the points formed by Y and X.
 VI


 Spline        Returns an array Interpolant of length n, which contains the second derivatives of
 Interpolant   the spline interpolating function g(x) at the tabulated points x[i], where i = 0, 1, …,
 VI            n–1.


 Spline        Returns a spline interpolated value at x value given the tabulated values (x[i], y[i])
 Interpolation and the second derivatives Interpolant that the VI obtains from the Spline
 VI             Interpolant VI.


InterpolateInterpolate 1D1D

Performs one-dimensional interpolation using a selected method based on the lookup
table defined by X and Y.


Inputs/Outputs

   •     method —

   method specifies the interpolation method.


                                                    © National Instruments 3389

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3389 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3390 ordinal=3390 -->
## Functions

Functions


            nearest—Chooses the Y value corresponding to the X value that is nearest to the current xi           0
               value. LabVIEW sets the interpolated value to the nearest data point.
             linear—Sets the interpolated values to points along the line segments connecting the X and Y           1             data points.
             spline—Guarantees that the first and second derivatives of the cubic interpolating polynomials           2
              are continuous, even at the data points.
             cubic Hermite—Guarantees that the first derivative of the cubic interpolating polynomials is
           3 continuous and sets the derivative at the endpoints to certain values in order to preserve the
               original shape and monotonicity of the Y data.
           4 Lagrange—Uses the barycentric Lagrange interpolation algorithm.

               •      Y —

           Y specifies the array of tabulated values of the dependent variable.

               •     X —

          X specifies the array of tabulated values of the independent variable.

          The length of X must equal the length of Y.

               •        xi —

               xi specifies the array of values of the independent variable at which LabVIEW computes the
             interpolated values yi of the dependent variable.

               •     X is monotonic —

          X is monotonic specifies whether the values in X are increasing monotonically with the index.

                    If X is monotonic is TRUE, the interpolation algorithm can avoid sorting X and reordering Y
             accordingly. If X is monotonic is FALSE, this VI sorts the X input arrays to be in ascending order
          and then reorders Y accordingly.

               •      ntimes —

           ntimes determines the interpolation xi locations, yielding interpolated values between every Y
           element when xi is empty. Interpolation between Y elements is repeated ntimes. The VI ignores
           ntimes if you wire the xi input.

               •        yi —


3390   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3390 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3391 ordinal=3391 -->
## Functions

Functions


     yi returns the output array of interpolated values that correspond to the xi independent variable
     values.

   •        xi used —

     xi used is the 1D array of values of the independent variable at which interpolated values of the
    dependent variable yi are computed.

       If xi is empty, xi used returns (2ntimes – 1)*(N– 1) + Npoints with (2ntimes – 1) points located
    evenly between each two adjacent elements in X, where Nis the length of X. If you wire the xi
     input, this VI ignores ntimes, and xi used is the same as xi.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The VI accepts tabulated dependent and independent variable values Y and X and
provides interpolated values yi corresponding to each xi location. The VI finds each
value of xi in X and uses the relative location in X to find the interpolated value yi at the
same relative location in Y.

Interpolate 1D VI allows you to choose between five different interpolation methods.
The following sections contain more information about each of these methods. As you
read these sections, consider the following situation:

  • X and Y already are in ascending order.
  • xj and yj are the elements of X and Y, respectively.
  • xim is the m-th element in xi, and yim is the corresponding m-th dependent value
    in yi.

Nearest Method

The nearest method finds the point nearest to xi in X and then assigns the
corresponding y value in Y to yi, as shown in the following graph.


                                                    © National Instruments 3391

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3391 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3392 ordinal=3392 -->
## Functions

Functions


      Linear Method

      The linear method interpolates yi on the line segment that connects the two points (xj,
      xj+ 1) when xi is located between the two points (xj, xj+ 1) in X, as shown in the
       following graph.


        In the previous graph, the following equation is true:


3392   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3392 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3393 ordinal=3393 -->
## Functions

Functions

Spline Method

The spline method refers to the cubic spline method. With this method, the VI derives
a third-order polynomial for each interval between two adjacent points. The
polynomials meet the following conditions:

  • The first and second derivatives at xj are continuous.
  • The polynomials pass all the specified data points.
  • The second derivatives at the beginning and end are zero.

The following graph illustrates the cubic spline method.


In the previous graph, Pj(x) is the third-order polynomial between two adjacent
points, (xj, yj) and (xj+ 1, yj+ 1).

Refer to APracticalGuidetoSplinesin the Mathematics Related Documentation
topic for more information about the cubic spline method.

      Note If you choose the spline method, this VI returns the same results as
       the Spline Interpolation 1D VI with natural spline boundary conditions.


                                                    © National Instruments 3393

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3393 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3394 ordinal=3394 -->
## Functions

Functions

      Cubic Hermite Method

      The cubic Hermitian spline method is the piecewise cubic Hermitian interpolation.
       This method derives a third-order polynomial in Hermitian form for each interval and
       ensures only the first derivatives of the interpolation polynomials are continuous.
      Compared to the cubic spline method, the cubic Hermitian method has better local
       property. In other words, if you change one data point xj, the effect on the
       interpolation result lies in the range between [xj– 1, xj] and [xj, xj+ 1].

       Refer to APracticalGuidetoSplinesin the MathematicsRelated
     Documentationtopic for more information about the cubic Hermitian method.

           Note If you choose the cubic Hermite method, this VI returns the same
                results as the Hermite Interpolation 1D VI.

     Lagrange Method

      The Lagrange method derives a polynomial of order N– 1 that passes all the Npoints
       specified in X and Y, where Nis the length of X and Y. This method is a reformulation of
       the Newton polynomial that avoids the computation of divided differences. The
       following equation defines the Lagrange method:

                               , where


     When you choose between the five interpolation methods in this VI, the following tips
      might be useful:

            • The nearest method and the linear method are simple to use but are too
           inaccurate in most applications.
            • The spline method returns the smoothest result out of all five methods.
            • The cubic Hermite method has better local property than the spline
         method and the Lagrange method.
            • The Lagrange method is simple to implement but not suitable for exploratory
            calculation. When compared to the spline method, the Lagrange method
           yields the interpolation result with extreme derivatives.

3394   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3394 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3395 ordinal=3395 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Mathematics\Interpolation\1D
   Interpolation.vi

InterpolateInterpolate 2D2D

Performs two-dimensional interpolation using a selected interpolation method based
on the lookup table defined by X, Y, and Z, where Z is a 2D array. You must manually
select the polymorphic instance to use.


   • Interpolate 2D (2d X,Y) VI
   • Interpolate 2D (1d X,Y) VI
   • Interpolate 2D (1d xi,yi) VI

This VI accepts tabulated X, Y, and Z values (two independent variables and one
dependent variable, respectively) and provides interpolated values zi that correspond
to each xi, yi location. The VI looks up each value of xi, yi in X, Y and uses the relative
location in X, Y to find the interpolated value zi at the relative location within Z.

This VI allows you to choose between four different interpolation methods.

In the following illustration, xi and yi are 2D arrays that specify the coordinates to be
interpolated. In other words, the coordinates of zim, n are (xim, n, yim, n), where mand
nare the indices for xi, yi, and zi. X and Y are 1D arrays that specify the coordinates of
Z. iand jare the indices of X and Y, respectively. Z is the 2D array that represents the
corresponding dependent variable, and the red dot specifies the position of zim, n.


                                                    © National Instruments 3395

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3395 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3396 ordinal=3396 -->
## Functions

Functions


      Nearest Interpolation Method

      The nearest method finds the point nearest to (xim, n, yim, n) and commits the
       corresponding z value in Z to zim, n. In the previous illustration, zim, n = zi, j+ 1.

      Bilinear Interpolation Method

      The bilinear method is the extension of the linear method in the Interpolate 1D VI. The
        bilinear method calculates the 1D linear interpolation twice along the x-axis and
       returns the interpolated values at points aand b, represented by the blue dots in the
       following illustration. This VI then calculates the 1D linear interpolation along the y-
        axis, represented by the line segment that connects aand bin the following
        illustration, and returns zim, n.


      Bicubic Interpolation Method

      Use the bicubic method to perform interpolation within grid rectangles. This method
       ensures that the inside interpolated surfaces, their first partial derivatives, and the
       second-order mixed derivative all are continuous.

       Refer to NumericalRecipesinC++in the Mathematics Related Documentation

3396   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3396 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3397 ordinal=3397 -->
## Functions

Functions

topic for more information about the bicubic interpolation method.

Bicubic Spline Interpolation Method

The bicubic spline method is an extension of the cubic spline method in the
Interpolate 1D VI. This method performs interpolation along one axis using the cubic
spline method and then along the other axis using the same method. The bicubic
spline method ensures that the first and second partial derivatives of the interpolation
polynomials are continuous.

Refer to NumericalRecipesinC++in the MathematicsRelated
Documentationtopic for more information about the bicubic spline interpolation
method.

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Mathematics\Interpolation\2D
   Interpolation.vi

InterpolateInterpolate 2D2D (2d(2d X,Y)X,Y) VIVI

Performs two-dimensional interpolation using a selected interpolation method based
on the lookup table defined by X, Y, and Z, where Z is a 2D array. You must manually
select the polymorphic instance to use.


Inputs/Outputs

   •     method —


                                                    © National Instruments 3397

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3397 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3398 ordinal=3398 -->
## Functions

Functions


          method sets the interpolation method.

             nearest—Selects the Z value that corresponds to the X, Y value that is nearest to the current xi,
           0                yi value. The interpolated value is set to the nearest data point.
           1 bilinear—Sets the interpolated values to points along the line segments that connect X and Y.
             bicubic—Yields an interpolated point from a bicubic surface that covers sixteen of the closest X,
           2 Y, Z data points and guarantees that the first partial derivatives and the second-order mixed
               derivative of the interpolated surfaces are continuous.
              bicubic spline—Guarantees that the first and second partial derivatives of the cubic           3               interpolating polynomials are continuous, even at the data points.

               •     Z —

          Z is the 2D array of tabulated values of the dependent variable.

               •     X —

          X is the 2D array of tabulated values of the first independent variable. All interpolation methods
             require that X be monotonic along each row, and all rows must be identical. Otherwise, this VI
            uses only the first row of X to perform the interpolation.

                    If X is not empty, the number of columns in X must equal the number of columns in Z. If X is
           empty, this VI treats X as an array whose size equals the size of Z and whose rows are [0, 1, …, N
           – 1], where Nis the number of columns in Z.

               •      Y —

           Y is the 2D array of tabulated values of the second independent variable. All interpolation
          methods require that Y be monotonic along each column, and all columns must be identical.
            Otherwise, this VI uses only the first column of Y to perform the interpolation.

                    If Y is not empty, the number of rows in Y must equal the number of rows in Z. If Y is empty, this
              VI treats Y as an array whose size equals the size of Z and whose columns are [0, 1, …, M– 1]T,
           where Mis the number of rows in Z.

               •        xi —

               xi is the 2D array of values of the first independent variable at which interpolated values of the
           dependent variable zi are to be computed.

               •        yi —


3398   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3398 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3399 ordinal=3399 -->
## Functions

Functions


     yi is the 2D array of values of the second independent variable at which interpolated values of
    the dependent variable zi are to be computed. The size of yi must equal the size of xi.

   •      ntimes —

    ntimes determines the locations of the interpolation points. Interpolations between each X
    element and each Y element are repeated ntimes. If you wire data to xi or yi, this VI ignores
    ntimes.

   •        zi —

     zi is the output 2D array of interpolated values that correspond to the xi, yi independent variable
     values.

   •        xi used —

     xi used is the 2D array of values of the first independent variable at which interpolated values of
    the dependent variable zi are computed.

       If you wire data to xi, xi used returns xi unchanged. Otherwise, xi used returns an array with
     identical rows of 2ntimes – 1 points located evenly between each two adjacent elements in the
      first row of X, and the number of rows in xi used equals the number of rows in yi used.

   •        yi used —

     yi used is the 2D array of values of the second independent variable at which interpolated values
     of the dependent variable zi are computed.

       If you wire data to yi, yi used returns yi unchanged. Otherwise, yi used returns an array with
     identical columns of 2ntimes – 1 points located evenly between each two adjacent elements in
    the first column of Y, and the number of columns in yi used equals the number of columns in xi
    used.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


This VI accepts tabulated X, Y, and Z values (two independent variables and one
dependent variable, respectively) and provides interpolated values zi that correspond
to each xi, yi location. The VI looks up each value of xi, yi in X, Y and uses the relative
location in X, Y to find the interpolated value zi at the relative location within Z.

                                                    © National Instruments 3399

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3399 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3400 ordinal=3400 -->
## Functions

Functions

       This VI allows you to choose between four different interpolation methods.

        In the following illustration, xi and yi are 2D arrays that specify the coordinates to be
       interpolated. In other words, the coordinates of zim, n are (xim, n, yim, n), where mand
   nare the indices for xi, yi, and zi. X and Y are 1D arrays that specify the coordinates of
        Z. iand jare the indices of X and Y, respectively. Z is the 2D array that represents the
       corresponding dependent variable, and the red dot specifies the position of zim, n.


      Nearest Interpolation Method

      The nearest method finds the point nearest to (xim, n, yim, n) and commits the
       corresponding z value in Z to zim, n. In the previous illustration, zim, n = zi, j+ 1.

      Bilinear Interpolation Method

      The bilinear method is the extension of the linear method in the Interpolate 1D VI. The
        bilinear method calculates the 1D linear interpolation twice along the x-axis and
       returns the interpolated values at points aand b, represented by the blue dots in the
       following illustration. This VI then calculates the 1D linear interpolation along the y-
        axis, represented by the line segment that connects aand bin the following
        illustration, and returns zim, n.


3400   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3400 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3401 ordinal=3401 -->
## Functions

Functions


Bicubic Interpolation Method

Use the bicubic method to perform interpolation within grid rectangles. This method
ensures that the inside interpolated surfaces, their first partial derivatives, and the
second-order mixed derivative all are continuous.

Refer to NumericalRecipesinC++in the Mathematics Related Documentation
topic for more information about the bicubic interpolation method.

Bicubic Spline Interpolation Method

The bicubic spline method is an extension of the cubic spline method in the
Interpolate 1D VI. This method performs interpolation along one axis using the cubic
spline method and then along the other axis using the same method. The bicubic
spline method ensures that the first and second partial derivatives of the interpolation
polynomials are continuous.

Refer to NumericalRecipesinC++in the MathematicsRelated
Documentationtopic for more information about the bicubic spline interpolation
method.

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Mathematics\Interpolation\2D
   Interpolation.vi


                                                    © National Instruments 3401

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3401 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3402 ordinal=3402 -->
## Functions

Functions

       InterpolateInterpolate 2D2D (1d(1d X,Y)X,Y) VIVI

      Performs two-dimensional interpolation using a selected interpolation method based
      on the lookup table defined by X, Y, and Z, where Z is a 2D array. You must manually
        select the polymorphic instance to use.

           Note

              Performs two-dimensional interpolation when X and Y are 1D arrays and xi
            and yi are 2D arrays.


      Inputs/Outputs

               •     method —

          method sets the interpolation method.

             nearest—Selects the Z value that corresponds to the X, Y value that is nearest to the current xi,           0                yi value. The interpolated value is set to the nearest data point.
           1 bilinear—Sets the interpolated values to points along the line segments that connect X and Y.
             bicubic—Yields an interpolated point from a bicubic surface that covers sixteen of the closest X,
           2 Y, Z data points and guarantees that the first partial derivatives and the second-order mixed
               derivative of the interpolated surfaces are continuous.
              bicubic spline—Guarantees that the first and second partial derivatives of the cubic
           3
               interpolating polynomials are continuous, even at the data points.

               •     Z —

          Z is the 2D array of tabulated values of the dependent variable.

               •     X —


3402   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3402 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3403 ordinal=3403 -->
## Functions

Functions


  X is the 1D array of tabulated values of the first independent variable. All interpolation methods
  require that X be monotonic.

   If X is not empty, the length of X must equal the number of columns in Z. If X is empty, this VI
  treats X as [0, 1, …, N– 1], where Nis the number of columns in Z.

•      Y —

  Y is the 1D array of tabulated values of the second independent variable. All interpolation
  methods require that Y be monotonic.

   If Y is not empty, the length of Y must equal the number of rows in Z. If Y is empty, this VI treats Y
  as [0, 1, …, M– 1], where Mis the number of rows in Z.

•        xi —

   xi is the 2D array of values of the first independent variable at which interpolated values of the
  dependent variable zi are to be computed.

•        yi —

   yi is the 2D array of values of the second independent variable at which interpolated values of
  the dependent variable zi are to be computed. The size of yi must equal the size of xi.

•      ntimes —

  ntimes determines the locations of the interpolation points. Interpolations between each X
  element and each Y element are repeated ntimes. If you wire data to xi or yi, this VI ignores
  ntimes.

•        zi —

   zi is the output 2D array of interpolated values that correspond to the xi, yi independent variable
  values.

•        xi used —

   xi used is the 2D array of values of the first independent variable at which interpolated values of
  the dependent variable zi are computed.

   If you wire data to xi, xi used returns xi. Otherwise, xi used returns an array with rows of 2ntimes
  – 1 points located evenly between each two adjacent elements in X, and the number of rows in xi
  used equals the number of rows in yi used.


                                                   © National Instruments 3403

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3403 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3404 ordinal=3404 -->
## Functions

Functions

               •        yi used —

              yi used is the 2D array of values of the second independent variable at which interpolated values
             of the dependent variable zi are computed.

                    If you wire data to yi, yi used returns yi. Otherwise, yi used returns an array with columns of
             2ntimes – 1 points located evenly between each two adjacent elements in Y, and the number of
           columns in yi used equals the number of columns in xi used.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       This VI accepts tabulated X, Y, and Z values (two independent variables and one
      dependent variable, respectively) and provides interpolated values zi that correspond
       to each xi, yi location. The VI looks up each value of xi, yi in X, Y and uses the relative
       location in X, Y to find the interpolated value zi at the relative location within Z.

       This VI allows you to choose between four different interpolation methods.

        In the following illustration, xi and yi are 2D arrays that specify the coordinates to be
       interpolated. In other words, the coordinates of zim, n are (xim, n, yim, n), where mand
   nare the indices for xi, yi, and zi. X and Y are 1D arrays that specify the coordinates of
        Z. iand jare the indices of X and Y, respectively. Z is the 2D array that represents the
       corresponding dependent variable, and the red dot specifies the position of zim, n.


      Nearest Interpolation Method

      The nearest method finds the point nearest to (xim, n, yim, n) and commits the

3404   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3404 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3405 ordinal=3405 -->
## Functions

Functions

corresponding z value in Z to zim, n. In the previous illustration, zim, n = zi, j+ 1.

Bilinear Interpolation Method

The bilinear method is the extension of the linear method in the Interpolate 1D VI. The
bilinear method calculates the 1D linear interpolation twice along the x-axis and
returns the interpolated values at points aand b, represented by the blue dots in the
following illustration. This VI then calculates the 1D linear interpolation along the y-
axis, represented by the line segment that connects aand bin the following
illustration, and returns zim, n.


Bicubic Interpolation Method

Use the bicubic method to perform interpolation within grid rectangles. This method
ensures that the inside interpolated surfaces, their first partial derivatives, and the
second-order mixed derivative all are continuous.

Refer to NumericalRecipesinC++in the Mathematics Related Documentation
topic for more information about the bicubic interpolation method.

Bicubic Spline Interpolation Method

The bicubic spline method is an extension of the cubic spline method in the
Interpolate 1D VI. This method performs interpolation along one axis using the cubic
spline method and then along the other axis using the same method. The bicubic
spline method ensures that the first and second partial derivatives of the interpolation
polynomials are continuous.

Refer to NumericalRecipesinC++in the MathematicsRelated

                                                    © National Instruments 3405

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3405 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3406 ordinal=3406 -->
## Functions

Functions

     Documentationtopic for more information about the bicubic spline interpolation
      method.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Interpolation\2D
        Interpolation.vi

       InterpolateInterpolate 2D2D (1d(1d xi,yi)xi,yi) VIVI

      Performs two-dimensional interpolation using a selected interpolation method based
      on the lookup table defined by X, Y, and Z, where Z is a 2D array. You must manually
        select the polymorphic instance to use.

           Note

              Performs two-dimensional interpolation when X, Y, xi, and yi are 1D arrays.


      Inputs/Outputs

               •     method —

          method sets the interpolation method.

             nearest—Selects the Z value that corresponds to the X, Y value that is nearest to the current xi,
           0
                yi value. The interpolated value is set to the nearest data point.
           1 bilinear—Sets the interpolated values to points along the line segments that connect X and Y.


3406   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3406 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3407 ordinal=3407 -->
## Functions

Functions


   bicubic—Yields an interpolated point from a bicubic surface that covers sixteen of the closest X,
  2 Y, Z data points and guarantees that the first partial derivatives and the second-order mixed
    derivative of the interpolated surfaces are continuous.
   bicubic spline—Guarantees that the first and second partial derivatives of the cubic  3    interpolating polynomials are continuous, even at the data points.

•     Z —

  Z is the 2D array of tabulated values of the dependent variable.

•     X —

  X is the 1D array of tabulated values of the first independent variable. All interpolation methods
  require that X be monotonic.

   If X is not empty, the length of X must equal the number of columns in Z. If X is empty, this VI
  treats X as [0, 1, …, N– 1], where Nis the number of columns in Z.

•      Y —

  Y is the 1D array of tabulated values of the second independent variable. All interpolation
  methods require that Y be monotonic.

   If Y is not empty, the length of Y must equal the number of rows in Z. If Y is empty, this VI treats Y
  as [0, 1, …, M– 1], where Mis the number of rows in Z.

•        xi —

   xi is the 1D array of values of the first independent variable at which interpolated values of the
  dependent variable zi are to be computed.

•        yi —

   yi is the 1D array of values of the second independent variable at which interpolated values of
  the dependent variable zi are to be computed.

•      ntimes —

  ntimes determines the locations of the interpolation points. Interpolations between each X
  element and each Y element are repeated ntimes. If you wire data to xi or yi, this VI ignores
  ntimes.

•        zi —


                                                   © National Instruments 3407

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3407 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3408 ordinal=3408 -->
## Functions

Functions


                zi is the output 2D array of interpolated values that correspond to the xi, yi independent variable
             values.

               •        xi used —

               xi used is the 2D array of values of the first independent variable at which interpolated values of
            the dependent variable zi are computed.

                    If you wire data to xi, xi used returns xi. Otherwise, xi used returns an array with rows of 2ntimes
           – 1 points located evenly between each two adjacent elements in X, and the number of rows in xi
           used equals the number of rows in yi used.

               •        yi used —

              yi used is the 2D array of values of the second independent variable at which interpolated values
             of the dependent variable zi are computed.

                    If you wire data to yi, yi used returns yi. Otherwise, yi used returns an array with columns of
             2ntimes – 1 points located evenly between each two adjacent elements in Y, and the number of
           columns in yi used equals the number of columns in xi used.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       This VI accepts tabulated X, Y, and Z values (two independent variables and one
      dependent variable, respectively) and provides interpolated values zi that correspond
       to each xi, yi location. The VI looks up each value of xi, yi in X, Y and uses the relative
       location in X, Y to find the interpolated value zi at the relative location within Z.

       This VI allows you to choose between four different interpolation methods.

        In the following illustration, xi and yi are 2D arrays that specify the coordinates to be
       interpolated. In other words, the coordinates of zim, n are (xim, n, yim, n), where mand
   nare the indices for xi, yi, and zi. X and Y are 1D arrays that specify the coordinates of
        Z. iand jare the indices of X and Y, respectively. Z is the 2D array that represents the
       corresponding dependent variable, and the red dot specifies the position of zim, n.


3408   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3408 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3409 ordinal=3409 -->
## Functions

Functions


Nearest Interpolation Method

The nearest method finds the point nearest to (xim, n, yim, n) and commits the
corresponding z value in Z to zim, n. In the previous illustration, zim, n = zi, j+ 1.

Bilinear Interpolation Method

The bilinear method is the extension of the linear method in the Interpolate 1D VI. The
bilinear method calculates the 1D linear interpolation twice along the x-axis and
returns the interpolated values at points aand b, represented by the blue dots in the
following illustration. This VI then calculates the 1D linear interpolation along the y-
axis, represented by the line segment that connects aand bin the following
illustration, and returns zim, n.


Bicubic Interpolation Method

Use the bicubic method to perform interpolation within grid rectangles. This method
ensures that the inside interpolated surfaces, their first partial derivatives, and the
second-order mixed derivative all are continuous.

Refer to NumericalRecipesinC++in the Mathematics Related Documentation

                                                    © National Instruments 3409

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3409 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3410 ordinal=3410 -->
## Functions

Functions

       topic for more information about the bicubic interpolation method.

      Bicubic Spline Interpolation Method

      The bicubic spline method is an extension of the cubic spline method in the
       Interpolate 1D VI. This method performs interpolation along one axis using the cubic
       spline method and then along the other axis using the same method. The bicubic
       spline method ensures that the first and second partial derivatives of the interpolation
       polynomials are continuous.

       Refer to NumericalRecipesinC++in the MathematicsRelated
     Documentationtopic for more information about the bicubic spline interpolation
      method.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Interpolation\2D
        Interpolation.vi

      InterpolateInterpolate 2D2D ScatteredScattered

      Performs two-dimensional interpolation on scattered points.

       This VI accepts X, Y, and Z values (two independent variables and one dependent
        variable, respectively) and returns interpolated values Zi that correspond to each Xi
      and Yi location.

      You must manually select the polymorphic instance to use.


            • Interpolate 2D Scattered (1D) VI
            • Interpolate 2D Scattered (2D) VI


3410   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3410 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3411 ordinal=3411 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Interpolation\Scattered 2D
   Interpolation.vi

InterpolateInterpolate 2D2D ScatteredScattered (1D)(1D) VIVI

Performs two-dimensional interpolation on scattered points.

This VI accepts X, Y, and Z values (two independent variables and one dependent
variable, respectively) and returns interpolated values Zi that correspond to each Xi
and Yi location.

You must manually select the polymorphic instance to use.


Inputs/Outputs

   •     method —

   method sets the interpolation method.

     nearest—Performs interpolation on the nearest points (non-smooth). This method finds the
    0
      point closest to (Xi, Yi) and assigns the corresponding value in Z to Zi.

      linear (default)—Performs linear interpolation on the selected triangle (non-smooth). This
     method triangulates the convex hull of (X, Y) and interpolates Zi for the points inside a triangle.    1
       (Xi, Yi) is valid only inside the convex hull of (X, Y). Otherwise, LabVIEW returns NaN.


                                                    © National Instruments 3411

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3411 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3412 ordinal=3412 -->
## Functions

Functions


            cubic—Performs cubic interpolation on the selected triangle (smooth). This method
               triangulates the convex hull of (X, Y) and interpolates Zi for the points inside a triangle.           2
                  (Xi, Yi) is valid only inside the convex hull of (X, Y). Otherwise, LabVIEW returns NaN.


            biharmonic spline—Performs biharmonic spline interpolation (smooth). This method
              calculates 2D biharmonic spline interpolation using Green's function.
           3
              Refer to APracticalGuidetoSplinesin the Mathematics Related Documentation topic for
           more information about the biharmonic spline interpolation method.


               •     Z —

          Z is the value of the known points.

               •     X —

          X is the x-coordinates of the known points.

               •      Y —

           Y is the y-coordinates of the known points. X, Y, and Z must be the same size.

               •       Xi —

              Xi is the x-coordinates of the new points where the VI computes interpolated values at Zi.

               •        Yi —

              Yi is the y-coordinates of the new points where interpolated values compute at Yi.

          The size of Yi must equal the size of Xi.

               •       Zi —

              Zi returns the interpolated values of the new points that correspond to the Xi and Yi values.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


3412   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3412 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3413 ordinal=3413 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Interpolation\Scattered 2D
   Interpolation.vi

InterpolateInterpolate 2D2D ScatteredScattered (2D)(2D) VIVI

Performs two-dimensional interpolation on scattered points.

This VI accepts X, Y, and Z values (two independent variables and one dependent
variable, respectively) and returns interpolated values Zi that correspond to each Xi
and Yi location.

You must manually select the polymorphic instance to use.


Inputs/Outputs

   •     method —

   method sets the interpolation method.

     nearest—Performs interpolation on the nearest points (non-smooth). This method finds the
    0
      point closest to (Xi, Yi) and assigns the corresponding value in Z to Zi.

      linear (default)—Performs linear interpolation on the selected triangle (non-smooth). This
     method triangulates the convex hull of (X, Y) and interpolates Zi for the points inside a triangle.    1
       (Xi, Yi) is valid only inside the convex hull of (X, Y). Otherwise, LabVIEW returns NaN.


                                                    © National Instruments 3413

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3413 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3414 ordinal=3414 -->
## Functions

Functions


            cubic—Performs cubic interpolation on the selected triangle (smooth). This method
               triangulates the convex hull of (X, Y) and interpolates Zi for the points inside a triangle.           2
                  (Xi, Yi) is valid only inside the convex hull of (X, Y). Otherwise, LabVIEW returns NaN.


            biharmonic spline—Performs biharmonic spline interpolation (smooth). This method
              calculates 2D biharmonic spline interpolation using Green’s function.
           3
              Refer to APracticalGuidetoSplinesin the Mathematics Related Documentation topic for
           more information about the biharmonic spline interpolation method.


               •     Z —

          Z is the value of the known points.

               •     X —

          X is the x-coordinates of the known points.

               •      Y —

           Y is the y-coordinates of the known points. X, Y, and Z must be the same size.

               •       Xi —

              Xi is a 2D array of the corresponding values of X. Both sets of corresponding interpolated values
          compute the dependent variable Zi.

               •        Yi —

              Yi is a 2D array of the corresponding values of Y. Both sets of corresponding interpolated values
          compute the dependent variable Zi.

          The size of Yi must equal the size of Xi.

               •       Zi —

              Zi is the 2D array of interpolated values that correspond to the Xi and Yi independent variable
             values.

               •       error —


3414   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3414 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3415 ordinal=3415 -->
## Functions

Functions


    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Interpolation\Scattered 2D
   Interpolation.vi

CreateCreate MeshMesh GridGrid (2D)(2D)

Takes two x domain and y domain arrays and forms X and Y 2D arrays, which are
typically used to evaluate and plot functions of two variables. You must manually
select the polymorphic instance to use.


  • Create Mesh Grid (2D) (x,y arrays) VI
  • Create Mesh Grid (2D) (x array) VI

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Interpolation\2D
   Interpolation.vi

CreateCreate MeshMesh GridGrid (2D)(2D) (x,y(x,y arrays)arrays) VIVI

Takes two x domain and y domain arrays and forms X and Y 2D arrays, which are
typically used to evaluate and plot functions of two variables. You must manually
select the polymorphic instance to use.


                                                    © National Instruments 3415

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3415 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3416 ordinal=3416 -->
## Functions

Functions


      Inputs/Outputs

               •      x domain —

           x domain becomes the repeated row data in the output X.

               •      y domain —

           y domain becomes the repeated column data in the output Y.

               •     X —

          X is an N x M 2D array formed by creating N identical rows of x domain data, where N is the
          number of elements in y domain, and M is the number of elements in x domain.

               •      Y —

           Y is an N x M 2D array formed by creating M identical columns of y domain data, where N is the
          number of elements in y domain, and M is the number of elements in x domain.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Interpolation\2D
        Interpolation.vi

      CreateCreate MeshMesh GridGrid (2D)(2D) (x(x array)array) VIVI

      Takes two x domain and y domain arrays and forms X and Y 2D arrays, which are
        typically used to evaluate and plot functions of two variables. You must manually
        select the polymorphic instance to use.


3416   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3416 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3417 ordinal=3417 -->
## Functions

Functions


Inputs/Outputs

   •     domain —

   domain becomes the repeated row data in the output X.

   •     X —

    X is an N x N 2D array formed by creating N identical rows of domain data, where N is the number
     of elements in domain.

   •      Y —

    Y is an N x N 2D array formed by creating N identical columns of domain data, where N is the
   number of elements in domain.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Interpolation\2D
   Interpolation.vi

SplineSpline InterpolationInterpolation 1D1D

Performs one-dimensional interpolation using the spline interpolation method based
on the lookup table defined by X and Y.


                                                    © National Instruments 3417

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3417 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3418 ordinal=3418 -->
## Functions

Functions


      Inputs/Outputs

               •      Y —

           Y is the array of tabulated values of the dependent variable.

               •     X —

          X is the array of tabulated values of the independent variable. The length of X must equal the
            length of Y.

               •        xi —

               xi is the array of values of the independent variable at which interpolated values of the
           dependent variable yi are to be computed.

               •        initial boundary —

               initial boundary sets the conditions at the initial boundary.

                     •     boundary —

              boundary sets the boundary condition type. The default is natural spline.

                  natural spline—Specifies that the second derivative at the initial boundary is 0 and that
               0               LabVIEW ignores the derivative value input.
                  not-a-knot—Specifies that the third derivative at the second data point x1 in X is
                  continuous, which means this VI fits one polynomial through the first three data points,
               1 and the polynomial between [x0, x1] is the same as the polynomial between [x1, x2]. This
                 option is useful if you know nothing about the derivatives at the initial boundary. If you
                   specify not-a-knot, LabVIEW ignores the derivative value input.
                   1st derivative—Specifies that derivative value specifies the first derivative at the initial
               2
                 boundary.
               2nd derivative—Specifies that derivative value specifies the second derivative at the
               3
                       initial boundary.

                     •       derivative value —


3418   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3418 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3419 ordinal=3419 -->
## Functions

Functions


       derivative value is the value of the first or second derivative at the initial boundary. This VI
       ignores derivative value when boundary is natural spline or not-a-knot.


•       final boundary —

   final boundary sets the conditions at the final boundary.

      •     boundary —

     boundary sets the boundary condition type. The default is natural spline.

        natural spline—Specifies that the second derivative at the final boundary is 0 and that      0
       LabVIEW ignores the derivative value input.
        not-a-knot—Specifies that the third derivate at the second-to-last data point in X, xn– 2, is
        continuous, which means this VI fits one polynomial through the last three data points,
      1 and the polynomial between [xn– 2, xn– 1] is the same as the polynomial between [xn– 3,
     xn– 2]. This option is useful if you know nothing about the derivatives at the final
       boundary. If you specify not-a-knot, LabVIEW ignores the derivative value input.
        1st derivative—Specifies that derivative value specifies the first derivative at the final
      2       boundary.
      2nd derivative—Specifies that derivative value specifies the second derivative at the final
      3       boundary.

      •       derivative value —

       derivative value is the value of the first or second derivative at the final boundary. This VI
       ignores derivative value when boundary is natural spline or not-a-knot.


•        yi —

   yi is the output array of interpolated values that correspond to the xi independent variable
  values.

•      piecewise polynomial —

  piecewise polynomial is a cluster that contains the x locations and coefficients of the piecewise
  interpolating polynomial.


                                                   © National Instruments 3419

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3419 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3420 ordinal=3420 -->
## Functions

Functions


                     •      x locations —

               x locations are the x domain endpoint values of the piecewise interpolating polynomial. If x
                 locations is of size N, the coefficients array should contain N–1 rows of polynomial
                   coefficients.

                     •       coefficients —

                  coefficients is a 2D array of interpolating polynomial coefficients.

            Row iof coefficients contains the coefficients for the interpolating polynomial between
               elements xi and xi+1 of x locations.


               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The VI accepts tabulated X and Y values (independent and dependent variables,
       respectively) and provides interpolated values yi that correspond to each xi location.
      The VI looks up each value of xi in X and uses the relative location in X to find the
       interpolated value yi at the same relative location within Y.

      The spline interpolation method guarantees that the first and second derivative of the
       piecewise interpolating polynomial are continuous, even at the data points.

        In addition to the interpolated yi values, this VI also exports the piecewise polynomial
        cluster, which contains the piecewise x locations and corresponding polynomial
        coefficients used in the interpolation.

      You can use the Evaluate Interpolating Polynomial VI to calculate the interpolated
       values using the piecewise polynomial.

       Refer to APracticalGuidetoSplinesin the Mathematics Related Documentation
       topic for more information about the spline interpolation method.


3420   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3420 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3421 ordinal=3421 -->
## Functions

Functions

HermiteHermite InterpolationInterpolation 1D1D

Performs one-dimensional interpolation using the cubic Hermite interpolation
method based on the lookup table defined by X and Y.


Inputs/Outputs

   •      Y —

    Y is the array of tabulated values of the dependent variable.

   •     X —

    X is the array of tabulated values of the independent variable. The length of X must equal the
    length of Y.

   •        xi —

     xi is the array of values of the independent variable at which interpolated values of the
    dependent variable yi are to be computed.

   •        yi —

     yi is the output array of interpolated values that correspond to the xi independent variable
     values.

   •      piecewise polynomial —

    piecewise polynomial is a cluster that contains the x locations and coefficients of the piecewise
     interpolating polynomial.

         •      x locations —

        x locations are the x domain endpoint values of the piecewise interpolating polynomial.

         •       coefficients —


                                                    © National Instruments 3421

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3421 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3422 ordinal=3422 -->
## Functions

Functions


                  coefficients is a 2D array of interpolating polynomial coefficients.

            Row iof coefficients should contain the coefficients for the interpolating polynomial
              between elements xi and xi+1 of x locations. If the length of Y is N, the coefficients array
                should contain N– 1 rows of polynomial coefficients.


               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The VI accepts tabulated X and Y values (independent and dependent variables,
       respectively) and provides interpolated values yi that correspond to each xi location.
      The VI looks up each value of xi in X and uses the relative location in X to find the
       interpolated value yi at the same relative location within Y.

      The cubic Hermite interpolation method guarantees that the first derivative of the
       interpolant is continuous and sets the derivative at the endpoints in order to preserve
       the original shape and monotonicity of the Y data.

           Note This VI returns the same results as the Interpolate 1D VI with the cubic
             Hermite method. Refer to APracticalGuidetoSplinesin the
             Mathematics Related Documentation topic for more information about this
             method.

        In addition to the interpolated yi values, this VI also exports the piecewise polynomial
        cluster, which contains the piecewise x locations and corresponding polynomial
        coefficients used in the interpolation. You can use the Evaluate Interpolating
      Polynomial VI to find the interpolated values using the piecewise polynomial.

      CreateCreate InterpolatingInterpolating PolynomialPolynomial

      Takes the piecewise polynomial x locations and a 2D array of coefficients and forms
       the piecewise polynomial cluster for the Evaluate Interpolating Polynomial VI to use.

3422   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3422 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3423 ordinal=3423 -->
## Functions

Functions


Inputs/Outputs

   •      x locations —

    x locations are the x domain endpoint values of the piecewise interpolating polynomial. If x
    locations is of size N, the coefficients array should contain N–1 rows of polynomial coefficients.

   •       coefficients —

     coefficients is a 2D array of interpolating polynomial coefficients.

   Row iof coefficients should contain the coefficients for the interpolating polynomial between
    elements xi and xi+1 of x locations.

   •      piecewise polynomial —

    piecewise polynomial is a cluster that contains the x locations and coefficients of the piecewise
     interpolating polynomial.

         •      x locations —

        x locations are the x domain endpoint values of the piecewise interpolating polynomial. If x
         locations is of size N, the coefficients array should contain N–1 rows of polynomial
          coefficients.

         •       coefficients —

         coefficients is a 2D array of interpolating polynomial coefficients.

      Row iof coefficients contains the coefficients for the interpolating polynomial between
        elements xi and xi+1 of x locations.


   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


                                                    © National Instruments 3423

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3423 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3424 ordinal=3424 -->
## Functions

Functions

           If x locations contains values x0, x1,…, xn–1, row iof the coefficients 2D array
      corresponds to the coefficients for the interpolating polynomial between xi and xi+1.

      EvaluateEvaluate InterpolatingInterpolating PolynomialPolynomial

      Takes the piecewise polynomial cluster and computes the interpolated values yi at
      each xi location.


      Inputs/Outputs

               •      piecewise polynomial —

            piecewise polynomial is a cluster that contains the x locations and coefficients of the piecewise
             interpolating polynomial.

                     •      x locations —

               x locations are the x domain endpoint values of the piecewise interpolating polynomial. If x
                 locations is of size N, the coefficients array should contain N–1 rows of polynomial
                   coefficients.

                     •       coefficients —

                  coefficients is a 2D array of interpolating polynomial coefficients.

            Row iof coefficients should contain the coefficients for the interpolating polynomial
              between elements xi and xi+1 of x locations.


               •        xi —

               xi is the array of values of the independent variable at which interpolated values of the
           dependent variable yi are to be computed.

               •        yi —

              yi is the output array of interpolated values that correspond to the xi independent variable


3424   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3424 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3425 ordinal=3425 -->
## Functions

Functions


     values.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

InterpolateInterpolate 1D1D FourierFourier

Performs interpolation by transforming the array X into the frequency domain, zero-
padding and scaling appropriately for the interpolation factor you want and to
maintain correct symmetry in the frequency domain, and then transforming back into
the time domain to form the output interpolated array Y out.


Inputs/Outputs

   •     X —

    X is the array of tabulated values to be interpolated. It is assumed that the data in X are equally
    spaced samples along its x-axis.

   •     n —

   n is the interpolation size or interpolation factor as determined by the setting of type.

   •      dt in —

    dt in computes dt out depending on the interpolation settings n and type.

   •      type —

    type determines how to use n in determining the interpolation size.

    0 interpolation size—output size = n


                                                    © National Instruments 3425

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3425 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3426 ordinal=3426 -->
## Functions

Functions


           1 interpolation factor—output size = n * size of X

               •      Y —

           Y is the output array of interpolated values.

               •       interpolation size —

             interpolation size returns the size of the interpolated output array Y. If type is interpolation
               size, interpolation size = n. If type is interpolation factor, interpolation size = n * size of X.

               •      dt out —

            dt out is set to dt in * N/m, where Nis the size of the input array Y in, and mis the interpolation
              size (determined by n and type).

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Interpolation\1D Fourier
        Interpolation.vi

     SearchSearch OrderedOrdered TableTable

      Works on the assumption that ordered x array is in monotonically increasing or
       decreasing order and can therefore efficiently search for the relative index of the
       location of x value within the x array. The VI starts the search at the starting index and
       begins by using a fast hunting phase to roughly bracket the location and then narrows
       to the final bracket using a bisection search. The VI computes the fractional index
       location by using linear interpolation.


3426   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3426 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3427 ordinal=3427 -->
## Functions

Functions


Inputs/Outputs

   •      ordered x array —

    ordered x array is the array of tabulated values of the dependent variable and must be
    monotonically increasing or decreasing.

   •      x value —

    x value is the value whose relative location the VI needs to find within the x array.

   •       starting index —

     starting index is the assumed initial search location. This value is usually set to the index of a
    previous search when the values to locate tend to be near each other in subsequent searches.
    The closer the starting index is to the true location of x value, the faster the search.

   •       fractional index —

     fractional index is the relative index value of location of x value within the x array.

PolynomialPolynomial InterpolationInterpolation VIVI

Interpolates or extrapolates the function f at x given a set of n points (x[i]y[i]), where
f(x[i]) = y[i], f is any function, and given a number x value.


Inputs/Outputs

   •      Y —

    Y is the array of dependent values.

   •     X —


                                                    © National Instruments 3427

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3427 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3428 ordinal=3428 -->
## Functions

Functions


          X is the array of independent values. If the number of elements in X is different from the number
             of elements in Y, the VI sets the output interpolation value and interpolation error to NaN and
             returns an error.

               •      x value —

           x value specifies the point at which the interpolation or extrapolation is performed. If the value
             of x value is in the range of X, the VI performs interpolation. Otherwise, the VI performs
             extrapolation.

                    If x value is too far from the range of X, the extrapolation error may be large. It is not a
              satisfactory extrapolation.

               •       interpolation value —

             interpolation value is the interpolation of the function f at x value.

               •       interpolation error —

             interpolation error is an estimate of the error in the interpolation.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The VI calculates output interpolation value P[n– 1](x), where P[n– 1] is the unique
      polynomial of degree n– 1 that passes through the npoints (x[i]y[i]).

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Interpolation\Interpolation
        Solver.vi

      RationalRational InterpolationInterpolation VIVI

       Interpolates or extrapolates f at x value using a rational function. The rational function
       passes through all the points formed by Y and X.

3428   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3428 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3429 ordinal=3429 -->
## Functions

Functions


Inputs/Outputs

   •      Y —

    Y is the array of dependent values.

   •     X —

    X is the array of independent values. If the number of elements in the X is different from the
   number of elements in the Y, the VI sets the output interpolation value and interpolation error
    to NaN and returns an error.

   •      x value —

    x value specifies the point at which the interpolation or extrapolation is performed. If x value is
     in the range of X, the VI performs interpolation. Otherwise, the VI performs extrapolation.

       If x value is too far from the range of X, the extrapolation error may be large. It is not a
     satisfactory extrapolation.

   •       interpolation value —

    interpolation value is the interpolation of the function f at x value.

   •       interpolation error —

    interpolation error is an estimate of the error in the interpolation.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The rational function


                                                    © National Instruments 3429

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3429 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3430 ordinal=3430 -->
## Functions

Functions

       passes through all the points formed by Y and X. Pand Qare polynomials, and the
        rational function is unique, given a set of npoints (xiyi), where f(xi) = yi, fis any
       function, and given a number xin the range of the xi values.

       This VI calculates the output interpolation value yusing


           If the number of points is odd, the degrees of freedom of Pand Qare using       . If the
      number of points is even, the degrees of freedom of Pare       , and the degrees of
      freedom of Qare   , where nis the total number of points formed by Y and X.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Interpolation\Interpolation
        Solver.vi

      SplineSpline InterpolantInterpolant VIVI

       Returns an array Interpolant of length n, which contains the second derivatives of the
       spline interpolating function g(x) at the tabulated points x[i], where i = 0, 1, …, n–1.


      Inputs/Outputs

               •      Y —

           Y is the array of dependent values. If the number of elements in the X is different from the
          number of elements in the Y, the VI sets the output Interpolant to an empty array and returns an
               error.

               •     X —

3430   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3430 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3431 ordinal=3431 -->
## Functions

Functions


    X is the array of independent values. If the number of elements in the X is different from the
    number of elements in the Y, the VI sets the output Interpolant to an empty array and returns an
     error.

   •        initial boundary —

      initial boundary is the first derivative of interpolating function g(x) at x[0], g'(x[0]). The default is
    1.00E+30, which causes this VI to set the initial boundary condition for a natural spline.

     Refer to Spline Interpolant Details for a definition of g(x).

   •       final boundary —

     final boundary is the first derivative of interpolating function g(x) at x[n – 1], g'(x[n – 1]). The
     default is 1.00E+30, which causes this VI to set the final boundary condition for a natural spline.

   •      Interpolant —

    Interpolant is the second derivative of interpolating function g(x) at points x[i], i = 0, 1, …, n – 1.

    You can use Interpolant as an input to the Spline Interpolation VI to interpolate yat any value of
     x0 ≤ x < xn – 1.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Input arrays X and Y are of length nand contain a tabulated function where x0 < x1 <
… < xn- 1, as shown in the following equation:

f(xi) = yi

The interpolating function g(x) is a piecewise function in the following equation:


The function pi(x) is a third-order polynomial that must satisfy the following

                                                    © National Instruments 3431

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3431 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3432 ordinal=3432 -->
## Functions

Functions

       conditions:

         1. g(xi) = yi = pi(xi)
         2. g(xi) = yi = pi– 1(xi)
         3. The first and second derivatives, where i= 1, …, n– 2, at each interior xi is
          continuous:
             a. g'(xi) = p'i(xi) = p'i- 1(xi)
            b. g"(xi) = p"i(xi) = p"i– 1(xi)

      With the third condition, you can derive the following equation:

                                          =

      where i= 1, …, n– 2. According to this equation, n– 2 linear equations exist for n
     unknown g"(xi).

      The Spline Interpolant VI computes two equations for the derivatives at x0 and xn– 1 in
       the following equation:


       Consider the following equations:


      The initial boundary is the equation


      and the final boundary is the equation


3432   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3432 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3433 ordinal=3433 -->
## Functions

Functions

                                        .

For these equations, initial boundary and final boundary are the first derivative of
g(x) at points x0 and xn– 1, respectively. If initial boundary and final boundary are
equal to or greater than 1030, this VI sets the corresponding boundary condition for a
natural spline, with no second derivatives on the boundary.

This VI solves g"(xi) from nequations when i= 0, 1, …, n– 1. g"(xi) is the Interpolant
output.

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Mathematics\Interpolation\Interpolation
   Solver.vi

SplineSpline InterpolationInterpolation VIVI

Returns a spline interpolated value at x value given the tabulated values (x[i], y[i]) and
the second derivatives Interpolant that the VI obtains from the Spline Interpolant VI.


Inputs/Outputs

   •      Y —

    Y is the array of tabulated values of the dependent variable.

   •     X —

    X is the array of tabulated values of the independent variable.

   •      Interpolant —


                                                    © National Instruments 3433

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3433 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3434 ordinal=3434 -->
## Functions

Functions


            Interpolant is the second derivative of the cubic spline interpolating function. You can obtain
            Interpolant from the Spline Interpolant VI.

          The number of elements in the three input arrays X, Y, and Interpolant should be the same.
            Otherwise, the VI sets the output interpolation value to NaN and returns an error.

               •      x value —

           x value is a single value.

           x value should fall within the range [X0, Xn – 1].

               •       interpolation value —

             interpolation value is the cubic spline interpolation of f at x value.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The points are formed by the input arrays X and Y.

     On the interval [xi, xi + 1], the following equation defines the output interpolation
       value y.

       y = Ayi + Byi + 1 + Cy"i + Dy"i + 1

      where


     Examples

       Refer to the following example files included with LabVIEW.


3434   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3434 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3435 ordinal=3435 -->
## Functions

Functions

  • labview\examples\Mathematics\Interpolation\Interpolation
   Solver.vi

IntegrationIntegration && DifferentiationDifferentiation

Use the Integration & Differentiation VIs to perform integration and differentiation
procedures.

The VIs on this palette can return mathematics error codes.


 Palette             Description Object

 Numeric    Performs numeric integration on the Input Array using one of four popular numeric
 Integration  integration methods. Wire data to the Input Array input to determine the polymorphic
 VI           instance to use or manually select the instance.

 Uneven
 Numeric    Performs numeric integration on the unevenly spaced values in the input array using
 Integration  the trapezoidal method.
 VI

 Quadrature Performs numerical integration using adaptive quadrature approach. You must
 VI          manually select the polymorphic instance to use.


 Integral
            Performs the discrete integration of the sampled signal X.
 x(t)

 Derivative
            Performs a discrete differentiation of the sampled signal X.
 x(t)

 Time
 Domain     Performs one of several math functions on time domain signals.
 Math


                                                    © National Instruments 3435

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3435 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3436 ordinal=3436 -->
## Functions

Functions

     NumericNumeric IntegrationIntegration VIVI

      Performs numeric integration on the Input Array using one of four popular numeric
       integration methods. Wire data to the Input Array input to determine the polymorphic
       instance to use or manually select the instance.


            • 1D Numeric Integration VI
            • 2D Numeric Integration VI
            • 3D Numeric Integration VI

      The x values you wire to this VI must be evenly spaced, or result is incorrect. If the
       values are not evenly spaced, you can use the Uneven Numeric Integration VI to
      compute the integral.

     1D Numeric Integration

       Number of Points                     Partial Evaluations Performed

        224                             55 Bode, 1 Simpsons' 3/8

        225                             56 Bode

        226                             56 Bode, Trapezoidal

        227                             56 Bode, 1 Simpsons'

        228                             57 Bode, 1 Simpsons' 3/8

           If 224 points are provided and the Bode Method is chosen, the VI arrives at the result
      by performing 55 Bode Method partial evaluations and one Simpsons' 3/8 Method
       evaluation.

      Each of the methods depends on the sampling interval (dt) and computes the integral
       using successive applications of a basic formula in order to perform partial
       evaluations, which depend on some number of adjacent points. The number of points
      used in each partial evaluation represents the order of the method. The result is the
      summation of these successive partial evaluations.


3436   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3436 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3437 ordinal=3437 -->
## Functions

Functions


where jis a range dependent on the number of points and the method of integration.

The following are the basic formulas for the computation of the partial sum of each
rule in ascending method order:

  • Trapezoidal: 1/2(x[i] + x[i+ 1])*dt
  • Simpsons': (x[2i] + 4x[2i+ 1] + x[2i+ 2])*dt/3, k= 2
  • Simpsons' 3/8: (3x[3i] + 9x[3i+ 1] + 9x[3i+ 2] + 3x[3i+ 3]) * dt/8, k= 3

  • Bode: (14x[4i] + 64x[4i+ 1] + 24x[4i+ 2] + 64x[4i+ 3] + 14x[4i+ 4]) * dt/45, k= 4

    for i= 0, 1, 2, 3, 4, ..., Integral Part of [(N– 1)/k]

where Nis the number of data points, kis an integer dependent on the method, and x
is the input array.

      Note If the number of points provided for a certain chosen method does not
        contain an integral number of partial sums, then the method is applied for all
        possible points. For the remaining points, the next possible lower order
      method is used. For example, if the Bode method is selected, the previous
       example shows what this VI evaluates for different numbers of points.

2D Numeric Integration

To perform the 2D numeric integration of

                         ,

this VI first applies 1D numeric integration over xto evaluate

                         .


                                                    © National Instruments 3437

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3437 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3438 ordinal=3438 -->
## Functions

Functions

      Then this VI applies 1D numeric integration over yto obtain the result


     3D Numeric Integration

      To perform the 3D numeric integration of

                                                ,

        this VI applies 1D numeric integration over x, y, and z, in sequence, as shown by the
       following equations:


     1D1D NumericNumeric IntegrationIntegration VIVI

      Performs numeric integration on the Input Array using one of four popular numeric
       integration methods.

       Wire data to the Input Array input to determine the polymorphic instance to use or
      manually select the instance.


      Inputs/Outputs

               •      Input Array —

            Input Array contains the data to be integrated, which is obtained from sampling an integrand f(t)
             at multiples of dt, that is, f(0), f(dt), f(2dt),….

               •      dt —

            dt is the interval size, which represents the sampling step size used in obtaining data in Input


3438   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3438 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3439 ordinal=3439 -->
## Functions

Functions


    Array from the function.

       If you supply a negative dt, this VI uses its absolute value.

   •       integration method —

    integration method specifies the method to use to perform the numeric integration.

    0   Trapezoidal Rule (default)
    1   Simpson's Rule
    2   Simpson's 3/8 Rule
    3   Bode Rule

   •       result —

     result returns the numeric integral.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The x values you wire to this VI must be evenly spaced, or result is incorrect. If the
values are not evenly spaced, you can use the Uneven Numeric Integration VI to
compute the integral.

1D Numeric Integration

 Number of Points                     Partial Evaluations Performed

 224                             55 Bode, 1 Simpsons' 3/8

 225                             56 Bode

 226                             56 Bode, Trapezoidal

 227                             56 Bode, 1 Simpsons'

 228                             57 Bode, 1 Simpsons' 3/8

If 224 points are provided and the Bode Method is chosen, the VI arrives at the result
by performing 55 Bode Method partial evaluations and one Simpsons' 3/8 Method

                                                    © National Instruments 3439

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3439 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3440 ordinal=3440 -->
## Functions

Functions

       evaluation.

      Each of the methods depends on the sampling interval (dt) and computes the integral
       using successive applications of a basic formula in order to perform partial
       evaluations, which depend on some number of adjacent points. The number of points
      used in each partial evaluation represents the order of the method. The result is the
      summation of these successive partial evaluations.


      where jis a range dependent on the number of points and the method of integration.

      The following are the basic formulas for the computation of the partial sum of each
       rule in ascending method order:

            • Trapezoidal: 1/2(x[i] + x[i+ 1])*dt
            • Simpsons': (x[2i] + 4x[2i+ 1] + x[2i+ 2])*dt/3, k= 2
            • Simpsons' 3/8: (3x[3i] + 9x[3i+ 1] + 9x[3i+ 2] + 3x[3i+ 3]) * dt/8, k= 3

            • Bode: (14x[4i] + 64x[4i+ 1] + 24x[4i+ 2] + 64x[4i+ 3] + 14x[4i+ 4]) * dt/45, k= 4

            for i= 0, 1, 2, 3, 4, ..., Integral Part of [(N– 1)/k]

      where Nis the number of data points, kis an integer dependent on the method, and x
         is the input array.

           Note If the number of points provided for a certain chosen method does not
              contain an integral number of partial sums, then the method is applied for all
               possible points. For the remaining points, the next possible lower order
            method is used. For example, if the Bode method is selected, the previous
             example shows what this VI evaluates for different numbers of points.

     2D2D NumericNumeric IntegrationIntegration VIVI

      Performs numeric integration on the Input Array using one of four popular numeric


3440   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3440 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3441 ordinal=3441 -->
## Functions

Functions

integration methods.

Wire data to the Input Array input to determine the polymorphic instance to use or
manually select the instance.


Inputs/Outputs

   •      Input Array —

    Input Array contains the data to be integrated, which is obtained from sampling an integrand f(x,
     y) at multiples of dx and dy, that is, f(0, 0), f(dx, 0), f(0, dy), f(dx, dy),....

   •       interval size —

     interval size contains the interval sizes dx and dy.

         •     dx —

       dx is the interval size of the integration variable x. The default is 1.

         •     dy —

       dy is the interval size of the integration variable y. The default is 1.


   •       integration method —

    integration method specifies the method to use to perform the numeric integration.

    0   Trapezoidal Rule (default)
    1   Simpson's Rule
    2   Simpson's 3/8 Rule
    3   Bode Rule

   •       result —

     result returns the numeric integral.


                                                    © National Instruments 3441

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3441 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3442 ordinal=3442 -->
## Functions

Functions

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The x values you wire to this VI must be evenly spaced, or result is incorrect. If the
       values are not evenly spaced, you can use the Uneven Numeric Integration VI to
      compute the integral.

     2D Numeric Integration

      To perform the 2D numeric integration of

                                     ,

        this VI first applies 1D numeric integration over xto evaluate

                                     .

      Then this VI applies 1D numeric integration over yto obtain the result


     3D3D NumericNumeric IntegrationIntegration VIVI

      Performs numeric integration on the Input Array using one of four popular numeric
       integration methods.

       Wire data to the Input Array input to determine the polymorphic instance to use or
      manually select the instance.


3442   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3442 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3443 ordinal=3443 -->
## Functions

Functions

Inputs/Outputs

   •      Input Array —

    Input Array contains the data to be integrated, which is obtained from sampling an integrand f(x,
      y, z) at multiples of dx, dy, and dz, that is, f(0, 0, 0), f(dx, 0, 0), f(0, dy, 0), f(0, 0, dz), f(dx, dy, dz),....

   •       interval size —

     interval size contains the interval sizes dx, dy, and dz.

         •     dx —

       dx is the interval size of the integration variable x. The default is 1.

         •     dy —

       dy is the interval size of the integration variable y. The default is 1.

         •      dz —

        dz is the interval size of the integration variable z. The default is 1.


   •       integration method —

    integration method specifies the method to use to perform the numeric integration.

    0   Trapezoidal Rule (default)
    1   Simpson's Rule
    2   Simpson's 3/8 Rule
    3   Bode Rule

   •       result —

     result returns the numeric integral.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


                                                    © National Instruments 3443

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3443 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3444 ordinal=3444 -->
## Functions

Functions

      The x values you wire to this VI must be evenly spaced, or result is incorrect. If the
       values are not evenly spaced, you can use the Uneven Numeric Integration VI to
      compute the integral.

     3D Numeric Integration

      To perform the 3D numeric integration of

                                                ,

        this VI applies 1D numeric integration over x, y, and z, in sequence, as shown by the
       following equations:


     UnevenUneven NumericNumeric IntegrationIntegration VIVI

      Performs numeric integration on the unevenly spaced values in the input array using
       the trapezoidal method.


      Inputs/Outputs

               •     X —

          X contains the data to be integrated, which you obtain by computing the integrand value at
           sampling points t0, t1, t2, …, where t0, t1, t2, … are the elements of T.

               •     T —

          T contains the sampling points LabVIEW uses to compute X from the integrand. The sampling
            points can be spaced unevenly. T must be the same length as X.

               •       result —


3444   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3444 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3445 ordinal=3445 -->
## Functions

Functions


     result returns the numeric integral.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Before performing numeric integration, the VI reorders T in ascending order and
reorders X to correspond to T. The VI then performs numeric integration using the
following equation:


where nis the number of data points.

QuadratureQuadrature VIVI

Performs numerical integration using adaptive quadrature approach. You must
manually select the polymorphic instance to use.


  • 1D Quadrature (VI) VI
  • 1D Quadrature (Formula) VI
  • 2D Quadrature (VI) VI
  • 2D Quadrature (Formula) VI
  • 3D Quadrature (VI) VI
  • 3D Quadrature (Formula) VI

This VI compares the difference between the 4-points and 7-points Lobatto
quadratures on the interval with tolerance to terminate the calculation iteration. If the
difference is less than the tolerance, the algorithm stops the iteration and moves on to
next interval.


                                                    © National Instruments 3445

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3445 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3446 ordinal=3446 -->
## Functions

Functions

     1D Quadrature

       This VI numerically evaluates the following integral using the adaptive Lobatto
       quadrature:


      where x1 is the upper limit and x0 is the lower limit.

      To obtain high accuracy, this VI divides an interval into subintervals when the
       integrand f(x) varies sharply, as shown in the following front panel.


     2D Quadrature

       This VI numerically evaluates the following integral using the adaptive Lobatto
       quadrature:


      where x1 is x upper limit, x0 is x lower limit, y1 is y upper limit, and y0 is y lower limit.

      The 2D Quadrature instances divide an interval block into many sub-blocks when the
       integrand f(x,y) varies sharply.

3446   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3446 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3447 ordinal=3447 -->
## Functions

Functions

3D Quadrature

This VI numerically evaluates the following integral using the adaptive Lobatto
quadrature:


where x1 is x upper limit, x0 is x lower limit, y1 is y upper limit, y0 is y lower limit, z1
is z upper limit, z0 is z lower limit.

The 3D Quadrature instances divide an interval cube into many sub-cubes when the
integrand f(x,y,z) varies sharply.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Integration and
   Differentiation\VI Reference Based Quadrature.vi

1D1D QuadratureQuadrature (VI)(VI) VIVI

Performs numerical integration using adaptive quadrature approach. You must
manually select the polymorphic instance to use.


Inputs/Outputs

   •      data —

    data is a variant that you can use to pass arbitrary values to the integrand VI.

   •      integrand —


                                                    © National Instruments 3447

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3447 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3448 ordinal=3448 -->
## Functions

Functions


            integrand is a strictly typed reference to the VI that implements the expression to integrate.
            Create this VI by starting from the VI template located in labview\vi.lib\Analysis\
         8numeric.llb\1D Quadrature Integrand.vit.

               Note The elements in the X array and Y array of the integrand VI specify the values of
                     the two integral variables at different time stamps. The X array and Y array represent
                     the first and second variables, respectively, so you cannot separate the elements in
                     the X array and Y array.

               •      upper limit —

           upper limit is the upper limit of the integral. The default is 1.

               •      lower limit —

           lower limit is the lower limit of the integral. The default is 0.

               •      tolerance —

            tolerance controls the accuracy of the quadrature. A smaller tolerance leads to a more accurate
             result but more computation time. The default is 1E-5.

               •       result —

             result returns the integral result.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       This VI compares the difference between the 4-points and 7-points Lobatto
       quadratures on the interval with tolerance to terminate the calculation iteration. If the
       difference is less than the tolerance, the algorithm stops the iteration and moves on to
       next interval.

     1D Quadrature

       This VI numerically evaluates the following integral using the adaptive Lobatto
       quadrature:


3448   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3448 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3449 ordinal=3449 -->
## Functions

Functions


where x1 is the upper limit and x0 is the lower limit.

To obtain high accuracy, this VI divides an interval into subintervals when the
integrand f(x) varies sharply, as shown in the following front panel.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Integration and
   Differentiation\VI Reference Based Quadrature.vi

1D1D QuadratureQuadrature (Formula)(Formula) VIVI

Performs numerical integration using adaptive quadrature approach. You must
manually select the polymorphic instance to use.


                                                    © National Instruments 3449

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3449 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3450 ordinal=3450 -->
## Functions

Functions

      Inputs/Outputs

               •      integrand —

            integrand specifies the expression you want to integrate. The independent variable must be x.

               •      upper limit —

           upper limit is the upper limit of the integral. The default is 1.

               •      lower limit —

           lower limit is the lower limit of the integral. The default is 0.

               •      tolerance —

            tolerance controls the accuracy of the quadrature. A smaller tolerance leads to a more accurate
             result but more computation time. The default is 1E-5.

               •       result —

             result returns the integral result.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       This VI compares the difference between the 4-points and 7-points Lobatto
       quadratures on the interval with tolerance to terminate the calculation iteration. If the
       difference is less than the tolerance, the algorithm stops the iteration and moves on to
       next interval.

     1D Quadrature

       This VI numerically evaluates the following integral using the adaptive Lobatto
       quadrature:


      where x1 is the upper limit and x0 is the lower limit.

3450   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3450 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3451 ordinal=3451 -->
## Functions

Functions

To obtain high accuracy, this VI divides an interval into subintervals when the
integrand f(x) varies sharply, as shown in the following front panel.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Integration and
   Differentiation\VI Reference Based Quadrature.vi

2D2D QuadratureQuadrature (VI)(VI) VIVI

Performs numerical integration using adaptive quadrature approach. You must
manually select the polymorphic instance to use.


Inputs/Outputs

   •      data —


                                                    © National Instruments 3451

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3451 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3452 ordinal=3452 -->
## Functions

Functions


           data is a variant that you can use to pass arbitrary values to the integrand VI.

               •      integrand —

            integrand is a strictly typed reference to the VI that implements the expression to integrate.
            Create this VI by starting from the VI template located in labview\vi.lib\Analysis\
         8numeric.llb\2D Quadrature Integrand.vit.

               Note The elements in the X array and Y array of the integrand VI specify the values of
                     the two integral variables at different time stamps. The X array and Y array represent
                     the first and second variables, respectively, so you cannot separate the elements in
                     the X array and Y array.

               •     Upper Limits —

          Upper Limits specifies the upper limits of the integral.

                     •      x upper limit —

               x upper limit is the upper limit of the first integral variable x. The default is 1.

                     •      y upper limit —

               y upper limit is the upper limit of the second integral variable y. The default is 1.


               •     Lower Limits —

          Lower Limits specifies the lower limits of the integral.

                     •      x lower limit —

               x lower limit is the lower limit of the first integral variable x. The default is 0.

                     •      y lower limit —

               y lower limit is the lower limit of the second integral variable y. The default is 0.


               •      tolerance —


3452   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3452 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3453 ordinal=3453 -->
## Functions

Functions


    tolerance controls the accuracy of the quadrature. A smaller tolerance leads to a more accurate
     result but more computation time. The default is 1E-5.

   •       result —

     result returns the integral result.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


This VI compares the difference between the 4-points and 7-points Lobatto
quadratures on the interval with tolerance to terminate the calculation iteration. If the
difference is less than the tolerance, the algorithm stops the iteration and moves on to
next interval.

2D Quadrature

This VI numerically evaluates the following integral using the adaptive Lobatto
quadrature:


where x1 is x upper limit, x0 is x lower limit, y1 is y upper limit, and y0 is y lower limit.

The 2D Quadrature instances divide an interval block into many sub-blocks when the
integrand f(x,y) varies sharply.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Integration and
   Differentiation\VI Reference Based Quadrature.vi


                                                    © National Instruments 3453

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3453 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3454 ordinal=3454 -->
## Functions

Functions

     2D2D QuadratureQuadrature (Formula)(Formula) VIVI

      Performs numerical integration using adaptive quadrature approach. You must
      manually select the polymorphic instance to use.


      Inputs/Outputs

               •      integrand —

            integrand specifies the expression you want to integrate. The first and second integral variables
          must be xand y, respectively.

               •     Upper Limits —

          Upper Limits specifies the upper limits of the integral.

                     •      x upper limit —

               x upper limit is the upper limit of the first integral variable x. The default is 1.

                     •      y upper limit —

               y upper limit is the upper limit of the second integral variable y. The default is 1.


               •     Lower Limits —

          Lower Limits specifies the lower limits of the integral.

                     •      x lower limit —

               x lower limit is the lower limit of the first integral variable x. The default is 0.

                     •      y lower limit —


3454   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3454 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3455 ordinal=3455 -->
## Functions

Functions


        y lower limit is the lower limit of the second integral variable y. The default is 0.


   •      tolerance —

    tolerance controls the accuracy of the quadrature. A smaller tolerance leads to a more accurate
     result but more computation time. The default is 1E-5.

   •       result —

     result returns the integral result.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


This VI compares the difference between the 4-points and 7-points Lobatto
quadratures on the interval with tolerance to terminate the calculation iteration. If the
difference is less than the tolerance, the algorithm stops the iteration and moves on to
next interval.

2D Quadrature

This VI numerically evaluates the following integral using the adaptive Lobatto
quadrature:


where x1 is x upper limit, x0 is x lower limit, y1 is y upper limit, and y0 is y lower limit.

The 2D Quadrature instances divide an interval block into many sub-blocks when the
integrand f(x,y) varies sharply.

Examples

Refer to the following example files included with LabVIEW.

                                                    © National Instruments 3455

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3455 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3456 ordinal=3456 -->
## Functions

Functions

            • labview\examples\Mathematics\Integration and
        Differentiation\VI Reference Based Quadrature.vi

     3D3D QuadratureQuadrature (VI)(VI) VIVI

      Performs numerical integration using adaptive quadrature approach. You must
      manually select the polymorphic instance to use.


      Inputs/Outputs

               •      data —

           data is a variant that you can use to pass arbitrary values to the integrand VI.

               •      integrand —

            integrand is a strictly typed reference to the VI that implements the expression to integrate.
            Create this VI by starting from the VI template located in labview\vi.lib\Analysis\
         8numeric.llb\3D Quadrature Integrand.vit.

               Note The elements in the X array, Y array and Z array of the integrand VI specify the
                     values of the three integral variables at different time stamps. X array, Y array and Z
                      array represent the first, second and third variable, respectively, so you cannot
                     separate the elements in X array, Y array and Z array.

               •     Upper Limits —

          Upper Limits specifies the upper limits of the integral.

                     •      x upper limit —

               x upper limit is the upper limit of the first integral variable x. The default is 1.

                     •      y upper limit —


3456   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3456 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3457 ordinal=3457 -->
## Functions

Functions


        y upper limit is the upper limit of the second integral variable y. The default is 1.

         •      z upper limit —

         z upper limit is the upper limit of the third integral variable z. The default is 1.


   •     Lower Limits —

    Lower Limits specifies the lower limits of the integral.

         •      x lower limit —

        x lower limit is the lower limit of the first integral variable x. The default is 0.

         •      y lower limit —

        y lower limit is the lower limit of the second integral variable y. The default is 0.

         •      z lower limit —

         z lower limit is the lower limit of the third integral variable z. The default is 0.


   •      tolerance —

    tolerance controls the accuracy of the quadrature. A smaller tolerance leads to a more accurate
     result but more computation time. The default is 1E-5.

   •       result —

     result returns the integral result.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


This VI compares the difference between the 4-points and 7-points Lobatto
quadratures on the interval with tolerance to terminate the calculation iteration. If the


                                                    © National Instruments 3457

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3457 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3458 ordinal=3458 -->
## Functions

Functions

       difference is less than the tolerance, the algorithm stops the iteration and moves on to
       next interval.

     3D Quadrature

       This VI numerically evaluates the following integral using the adaptive Lobatto
       quadrature:


      where x1 is x upper limit, x0 is x lower limit, y1 is y upper limit, y0 is y lower limit, z1
         is z upper limit, z0 is z lower limit.

      The 3D Quadrature instances divide an interval cube into many sub-cubes when the
       integrand f(x,y,z) varies sharply.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Integration and
        Differentiation\VI Reference Based Quadrature.vi

     3D3D QuadratureQuadrature (Formula)(Formula) VIVI

      Performs numerical integration using adaptive quadrature approach. You must
      manually select the polymorphic instance to use.


      Inputs/Outputs

               •      integrand —


3458   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3458 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3459 ordinal=3459 -->
## Functions

Functions


  integrand specifies the expression you want to integrate. The first, second, and third integral
  variables must be x, y, and z, respectively.

•     Upper Limits —

  Upper Limits specifies the upper limits of the integral.

      •      x upper limit —

      x upper limit is the upper limit of the first integral variable x. The default is 1.

      •      y upper limit —

      y upper limit is the upper limit of the second integral variable y. The default is 1.

      •      z upper limit —

      z upper limit is the upper limit of the third integral variable z. The default is 1.


•     Lower Limits —

  Lower Limits specifies the lower limits of the integral.

      •      x lower limit —

      x lower limit is the lower limit of the first integral variable x. The default is 0.

      •      y lower limit —

      y lower limit is the lower limit of the second integral variable y. The default is 0.

      •      z lower limit —

      z lower limit is the lower limit of the third integral variable z. The default is 0.


•      tolerance —

  tolerance controls the accuracy of the quadrature. A smaller tolerance leads to a more accurate
  result but more computation time. The default is 1E-5.

•       result —

                                                   © National Instruments 3459

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3459 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3460 ordinal=3460 -->
## Functions

Functions


             result returns the integral result.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       This VI compares the difference between the 4-points and 7-points Lobatto
       quadratures on the interval with tolerance to terminate the calculation iteration. If the
       difference is less than the tolerance, the algorithm stops the iteration and moves on to
       next interval.

     3D Quadrature

       This VI numerically evaluates the following integral using the adaptive Lobatto
       quadrature:


      where x1 is x upper limit, x0 is x lower limit, y1 is y upper limit, y0 is y lower limit, z1
         is z upper limit, z0 is z lower limit.

      The 3D Quadrature instances divide an interval cube into many sub-cubes when the
       integrand f(x,y,z) varies sharply.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Integration and
        Differentiation\VI Reference Based Quadrature.vi

      IntegralIntegral x(t)x(t)

      Performs the discrete integration of the sampled signal X.


3460   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3460 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3461 ordinal=3461 -->
## Functions

Functions


Inputs/Outputs

   •     X —

    X is the sampled signal from time 0 to n– 1 where nis the number of elements in X.

   •        Initial Condition —

     Initial Condition specifies the initial condition of X in the integration calculation.

       If integration method is Trapezoidal Rule or Simpson's Rule, the VI uses the first
    element in Initial Condition to calculate the integration. If integration method is Simpson's
   3/8 Rule or Bode Rule, the VI uses the first two elements in Initial Condition to calculate
    the integration. The default is [0].

   •       Final Condition —

    Final Condition specifies the final condition of X in the integration calculation.

       If integration method is Trapezoidal Rule, the VI ignores Final Condition. If integration
   method is Simpson's Rule or Simpson's 3/8 Rule, the VI uses the first element in
    Final Condition to calculate the integration. If integration method is Bode Rule, the VI uses
    the first two elements in Final Condition to calculate the integration. The default is [0].

   •      dt —

    dt is the sampling interval and must be greater than 0. The default is 1.0.

       If dt is less than or equal to 0, the VI sets Integral X to an empty array and returns an error.

   •       integration method —

    integration method specifies the method to use to perform the numeric integration.

    0   Trapezoidal Rule
    1   Simpson's Rule (default)
    2   Simpson's 3/8 Rule


                                                    © National Instruments 3461

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3461 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3462 ordinal=3462 -->
## Functions

Functions


           3   Bode Rule

               •       Integral X —

             Integral X is the discrete integration of X.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


        Integral x(t) calculates a definite integral. The value of the output array at any value xis
       the area under the curve of the input array between 0 and x.

      The integral F(t) of a function f(t) is defined as


       Let yrepresent the sampled output sequence Integral X.

           If integration method is Trapezoidal Rule, the VI obtains the elements of yusing
       the following equation:


        for i= 0, 1, 2, …, n– 1,

      where nis the number of samples in X and x–1 is the first element in Initial Condition.

           If integration method is Simpson's Rule, the VI obtains the elements of yusing
       the following equation:


        for i= 0, 1, 2, …, n– 1,

3462   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3462 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3463 ordinal=3463 -->
## Functions

Functions

where nis the number of samples in X, x–1 is the first element in Initial Condition, and
xn is the first element in Final Condition.

If integration method is Simpson's 3/8 Rule, the VI obtains the elements of y
using the following equation:


for i= 0, 1, 2, …, n– 1,

where nis the number of samples in X, x–2 and x–1 are the first and second elements
in Initial Condition, and xn is the first element in Final Condition.

If integration method is Bode Rule, the VI obtains the elements of yusing the
following equation:


for i= 0, 1, 2, …, n– 1,

where nis the number of samples in X, x–2 and x–1 are the first and second elements
in Initial Condition, and xn and xn+1 are the first and second elements in Final
Condition.

The Initial Condition and Final Condition minimize the overall error by increasing the
accuracy at the boundaries, especially when the number of samples is small.
Determining boundary conditions before the fact enhances accuracy.

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Mathematics\Probability and Statistics\
   Probability Density.vi


                                                    © National Instruments 3463

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3463 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3464 ordinal=3464 -->
## Functions

Functions

      DerivativeDerivative x(t)x(t)

      Performs a discrete differentiation of the sampled signal X.


      Inputs/Outputs

               •     X —

          X is the sampled signal from time 0 to n– 1 where nis the number of elements in X.

               •        Initial Condition —

               Initial Condition specifies the initial condition of X in the differentiation calculation.

                    If method is 2nd Order Central or Backward, the VI uses the first element in Initial
            Condition to calculate the derivative. If method is 4th Order Central, the VI uses the first
          two elements in Initial Condition to calculate the derivative. The default is [0].

               •       Final Condition —

             Final Condition specifies the final condition of X in the differentiation calculation.

                    If method is 2nd Order Central or Forward, the VI uses the first element in Final
            Condition to calculate the derivative. If method is 4th Order Central, the VI uses the first
          two elements in Final Condition to calculate the derivative. The default is [0].

               •      dt —

            dt is the sampling interval and must be greater than zero. The default is 1.0.

                    If dt is less than or equal to zero, the VI sets dX/dt to an empty array and returns an error.

               •     method —

          method specifies the differentiation method.


3464   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3464 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3465 ordinal=3465 -->
## Functions

Functions


    0   2nd Order Central (default)
    1   4th Order Central
    2   Forward
    3   Backward

   •      dX/dt —

    dX/dt is the derivative of the input signal X.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The differentiation f(t) of a function F(t) is defined as


Let Yrepresent the sampled output sequence dX/dt.

If method is 2nd Order Central, Yis given by the following equation:


for i= 0, 1, 2, …, n– 1,

where nis the number of samples in x(t), x–1 is the first element in Initial Condition,
and xn is the first element in Final Condition.

If method is 4th Order Central, Yis given by the following equation:


for i= 0, 1, 2, …, n– 1,


                                                    © National Instruments 3465

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3465 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3466 ordinal=3466 -->
## Functions

Functions

      where nis the number of samples in x(t), x–2 and x–1 are the first and second elements
        in Initial Condition, xn and xn+ 1 are the first and second elements in Final Condition.

           If method is Forward, Yis given by the following equation:


        for i= 0, 1, 2, …, n– 1,

      where nis the number of samples in x(t) and xn is the first element in Final Condition.

           If method is Backward, Yis given by the following equation:


        for i= 0, 1, 2, …, n– 1,

      where nis the number of samples in x(t) and x–1 is the first element in Initial
       Condition.

      The Initial Condition and Final Condition minimize the error at the boundaries.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Probability Density.vi

     TimeTime DomainDomain MathMath

      Performs one of several math functions on time domain signals.


3466   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3466 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3467 ordinal=3467 -->
## Functions

Functions

Dialog Box Options

 Option        Description

               Contains the following options:

                          •  Derivative (dX/dt)—

                   Returns the numeric derivative of the signal.

                 LabVIEW computes the output sample of dX/dtat index ias yi=(xi– xi–1)/dt.

                          •  Difference (dX)—

                   Returns the numeric difference of the signal.

                 LabVIEW computes the output sample of dXat index ias yi=xi–xi–1.
 Mathematical
 Operation                          •  Integral (Sum[Xdt])—

                   Returns the numeric integral of the signal.

                 LabVIEW computes the output sample of Sum[Xdt]at index ias yi=yi–1 +
                    xidt.

                          • Summation (Sum[X])—

                   Returns the summation of the signal.

                 LabVIEW computes the output sample of Sum[X]at index ias yi=yi–1 + xi.

               Contains the following options:

                          • Continuous calculation—

                  Uses data from previous segments of data in performing the calculation. Calculation
 Mode                          • Per segment calculation—

                 Does not use data from previous segments of data in performing the
                      calculation.

 Result Name  Contains the following options:

                                                    © National Instruments 3467

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3467 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3468 ordinal=3468 -->
## Functions

Functions


        Option        Description

                                     • Use mathematical operation name—

                            Displays the name of the mathematical operation as the name of the Express VI
                       on the block diagram.

                                     • Express VI name—

                            Displays the name of the Express VI on the block diagram. Remove the
                        checkmark from the Use mathematical operation name checkbox to edit the
                     name of the Express VI.


                        Displays the input signal.

        Input Signal     If you wire data to the Express VI and run it, Input Signal displays real data. If you
                        close and reopen the Express VI, Input Signal displays sample data until you run
                       the Express VI again.


                        Displays a preview of the measurement. The Result Preview plot indicates the
                       value of the selected measurement with a dotted line.
         Result                                      If you wire data to the Express VI and run it, Result Preview displays real data. If you
        Preview                        close and reopen the Express VI, Result Preview displays sample data until you run
                       the VI again. If the cutoff frequency values are invalid, Result Preview does not
                        display valid data.


      Inputs/Outputs

               •      Signals —

            Contains the input signal or signals.

               •       error in (no error) —

            Describes error conditions that occur before this node runs.

               •       error out —


3468   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3468 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3469 ordinal=3469 -->
## Functions

Functions


    Contains error information. This output provides standard error out functionality.

   •      Result —

    Returns the resulting data based on the configuration of the Express VI.


Components

Displays the name of the Express VI on the block diagram. Remove the checkmark
from the Use mathematical operation name checkbox to edit the name of the Express
VI.

Displays a preview of the measurement. The Result Preview plot indicates the value of
the selected measurement with a dotted line.

Displays the input signal.

Does not use data from previous segments of data in performing the calculation.

Uses data from previous segments of data in performing the calculation.

Returns the summation of the signal.

Returns the numeric integral of the signal.

Returns the numeric difference of the signal.

Returns the numeric derivative of the signal.

Displays the name of the mathematical operation as the name of the Express VI on the
block diagram.

ProbabilityProbability && StatisticsStatistics

Use the Probability and Statistics VIs to perform probability, descriptive statistics,
analysis of variance, and interpolation functions.


                                                    © National Instruments 3469

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3469 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3470 ordinal=3470 -->
## Functions

Functions

           Note Many Probability and Statistics VIs are available only in the LabVIEW
                 Full and Professional Development Systems. If you have the LabVIEW Base
             Development System, you have only a subset of the Probability and Statistics
                  VIs.

      The VIs on this palette can return mathematics error codes.


         Palette
                       Description        Object

                   Computes the mean of the values in the input sequence X. You must manually select       Mean                      the polymorphic instance you want to use.


        Measures of
                   Computes the central tendency of the data values in x array.       Mean

        Standard                   Computes the mean, standard deviation, and variance of the values in the input         Deviation
                    sequence X.       and Variance

        Skewness                   Computes the skewness and kurtosis of the input sequence X.       and Kurtosis

        Measures of
                   Computes the spread of the data values in x array.
        Spread


                   Computes a value that is greater than p percent of the data values in x array. Wire
         Percentiles   data to the p input to determine the polymorphic instance to use or manually select
                      the instance.


      RMS VI      Computes the root mean square (rms) of the input sequence X.


3470   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3470 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3471 ordinal=3471 -->
## Functions

Functions


Palette              Description
Object

            Computes the mean square error (mse) of the input sequences X Values and YMSE VI              Values.


Moment            Computes the moment about the mean of the input sequence X using the specifiedabout Mean              order, m.
VI

Covariance
            Computes the covariance matrix of the input sequence X.Matrix


              Finds the modes (most common values) or estimated modes (most common range
Mode         centers) of the input sequence X. This VI can perform unimodal or multimodal
               analysis. You must manually select the polymorphic instance to use.


              Finds the median value of the input sequence X by sorting the values of X andMedian              averaging the middle element(s) of the sorted array.


Histogram    Finds the discrete histogram of the input sequence X.


General      Finds the discrete histogram of the input sequence X based on the given bin
Histogram VI  specifications.


Correlation
            Computes the linear correlation coefficient between input sequences X and Y.
Coefficient

Correlation
            Computes the Spearman's rank correlation coefficient between input sequences X
Coefficient
            and Y.
(Spearman)

Correlation
Coefficient   Computes the Kendall's Tau correlation coefficient between input sequences X and
(Kendall's     Y.
Tau)

                                                    © National Instruments 3471

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3471 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3472 ordinal=3472 -->
## Functions

Functions


         Palette                       Description
        Object

                   Use the Probability VIs to perform probability distribution and random number         Probability                      generation functions.


        Hypothesis                   Use the Hypothesis Testing VIs to test hypotheses about a population.         Testing

         Analysis of                   Use the Analysis of Variance VIs to perform analysis of variance functions.         Variance


          Statistics     Returns the selected parameter of the first signal in a waveform.


         Create                   Computes a histogram for Signal.
        Histogram

    MeanMean

      Computes the mean of the values in the input sequence X. You must manually select
       the polymorphic instance you want to use.


            • Mean (DBL) VI
            • Mean (CDB) VI

      The VI calculates mean using the following equation.


      where µ is mean and nis the number of elements in X.


3472   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3472 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3473 ordinal=3473 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Statistics Solver.vi

MeanMean (DBL)(DBL) VIVI

Computes the mean of the values in the input sequence X. You must manually select
the polymorphic instance you want to use.


Inputs/Outputs

   •     X —

    X is the input sequence. If the input sequence X is empty, mean is NaN.

   •     mean —

   mean is the mean, or average, of the values in the input sequence X.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The VI calculates mean using the following equation.


where µ is mean and nis the number of elements in X.


                                                    © National Instruments 3473

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3473 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3474 ordinal=3474 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Statistics Solver.vi

     MeanMean (CDB)(CDB) VIVI

      Computes the mean of the values in the input sequence X. You must manually select
       the polymorphic instance you want to use.


      Inputs/Outputs

               •     X —

          X is the input sequence. If the input sequence X is empty, mean is NaN.

               •     mean —

         mean is the mean, or average, of the values in the input sequence X.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The VI calculates mean using the following equation.


      where µ is mean and nis the number of elements in X.


3474   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3474 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3475 ordinal=3475 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Statistics Solver.vi

MeasuresMeasures ofof MeanMean

Computes the central tendency of the data values in x array.


Inputs/Outputs

   •      x array —

    x array specifies the data set.

   •      type —

    type specifies the type of mean to compute.

    0 arithmetic—Computes the arithmetic mean of x array.
    1 geometric—Computes the geometric mean of x array.
    2 harmonic—Computes the harmonic mean of x array.
     trimmed—Computes the arithmetic mean of x array after removing the percentage of potential
    3
      outliers that percent (trim) specifies.
    4 median—Computes the central value of x array. The median value also is the 50th percentile.

   •      percent (trim) —

    percent (trim) specifies the percentage of data to trim before computing the trimmed mean.
    Use this input to ignore outlier values in x array. LabVIEW trims the percentage you specify from
    both the lowest and highest values of x array. Thus, the total amount trimmed equals twice the
    value of percent (trim).

   •     mean value —


                                                    © National Instruments 3475

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3475 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3476 ordinal=3476 -->
## Functions

Functions


         mean value returns the mean measure of the data in x array.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The trimmed and median measures of mean resist outlier values in the data set and
       usually are more robust than the other measures of mean.

     StandardStandard DeviationDeviation andand VarianceVariance

      Computes the mean, standard deviation, and variance of the values in the input
      sequence X.


      Inputs/Outputs

               •     X —

          X is the input sequence.

               •      Weighting (Sample) —

           Weighting determines whether to calculate the population or the sample standard deviation
          and variance.

                  Sample
           0
                         (default)
           1        Population

               •     mean —

         mean is the mean, or average, of the values in the input sequence X.

               •      standard deviation —


3476   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3476 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3477 ordinal=3477 -->
## Functions

Functions


    standard deviation is the standard deviation calculated from the values in the input sequence X.

   •      variance —

    variance is the calculated variance of the values in the input sequence X.


The VI calculates the output values using the following equations.


where µ is mean and nis the number of elements in X.

standard deviation = σ

where σ² is variance, µ is mean, and wis nwhen Weighting is set to Population
and (n– 1) when Weighting is set to Sample.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Statistics Solver.vi
  • labview\examples\Signal Processing\Spectral Analysis\
   Power & Frequency Estimator.vi
  • labview\examples\Mathematics\Probability and Statistics\
   Noise Statistics.vi

SkewnessSkewness andand KurtosisKurtosis

Computes the skewness and kurtosis of the input sequence X.

Skewness is a measurement of symmetry. Kurtosis is the peak measurement of a
distribution.


                                                    © National Instruments 3477

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3477 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3478 ordinal=3478 -->
## Functions

Functions


      Inputs/Outputs

               •     X —

          X is the input sequence. If X is empty, skewness and kurtosis are NaN.

               •      Weighting (Sample) —

           Weighting specifies whether the input sequence X is a complete population or a random sample
            taken from a population.

                  Sample           0                         (default)
           1        Population

               •      skewness —

           skewness returns the symmetrical measurement of the input sequence X.

               •       kurtosis —

             kurtosis returns the peak measurement of the input sequence X.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      A negative value of skewness indicates that the left side of the probability density
       function is longer than the right side. A positive value of skewness indicates that the
        right side of the probability density function is longer than the right side.

      The following front panel image shows negative skewness.


3478   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3478 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3479 ordinal=3479 -->
## Functions

Functions


The following front panel image shows positive skewness.


When determining kurtosis, normal distribution has a kurtosis value of 3. A kurtosis
value of less than 3 indicates a flatter distribution than normal. A kurtosis value of
greater than 3 indicates a sharper distribution than normal. The following front panel
image shows three distributions with kurtosis values of 6, 3, 1.8.


                                                    © National Instruments 3479

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3479 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3480 ordinal=3480 -->
## Functions

Functions

     MeasuresMeasures ofof SpreadSpread

      Computes the spread of the data values in x array.


      Inputs/Outputs

               •      x array —

           x array specifies the data set.

               •      type —

           type specifies the type of spread to compute.

             standard deviation—Computes the standard deviation, or the square root of the variance, of x
           0               array. The standard deviation is the most common measure of spread in a data set.
           range—Computes the range, or the difference in the minimum and maximum values, of x
           1               array.
          mean absolute deviation—Computes the mean of the absolute value of the deviation of x
           2              array from its mean.
              interquartile rank—Computes the difference between the 25th and 75th percentile of x array.
           3              This measure of spread therefore is more resistive to outliers than the other measures.

               •      spread value —

           spread value returns the spread of the data in x array.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

      PercentilesPercentiles

      Computes a value that is greater than p percent of the data values in x array. Wire data
       to the p input to determine the polymorphic instance to use or manually select the


3480   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3480 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3481 ordinal=3481 -->
## Functions

Functions

instance.


  • st_Percentiles (scalar) VI
  • st_Percentiles (array) VI

st_Percentilesst_Percentiles (scalar)(scalar) VIVI

Computes a value that is greater than p percent of the data values in x array. Wire data
to the p input to determine the polymorphic instance to use or manually select the
instance.


Inputs/Outputs

   •      x array —

    x array specifies the data set.

   •     p —

   p specifies the percent of data values in x array that are less than percentile.

   •       percentile —

    percentile returns a value greater than p percent of the data values in x array.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


st_Percentilesst_Percentiles (array)(array) VIVI

Computes a value that is greater than p percent of the data values in x array. Wire data

                                                    © National Instruments 3481

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3481 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3482 ordinal=3482 -->
## Functions

Functions

       to the p input to determine the polymorphic instance to use or manually select the
       instance.


      Inputs/Outputs

               •      x array —

           x array specifies the data set.

               •     p array —

          p array specifies the percent of data values in x array that are less than the corresponding
           elements of percentiles.

               •       percentiles —

             percentiles returns the values greater than the corresponding p percent of the data values in x
             array.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

    RMSRMS VIVI

      Computes the root mean square (rms) of the input sequence X.


            • RMS (DBL) VI
            • RMS (CDB) VI

      The VI calculates rms value using the following equation:


3482   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3482 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3483 ordinal=3483 -->
## Functions

Functions


where ψx is rms value and nis the number of elements in X.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Statistics Solver.vi

RMSRMS (DBL)(DBL) VIVI

Computes the root mean square (rms) of the input sequence X.


Inputs/Outputs

   •     X —

    X is the real input sequence. If X is empty, rms value is NaN.

   •     rms value —

   rms value is the root mean square computed from the input sequence X.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The VI calculates rms value using the following equation:


                                                    © National Instruments 3483

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3483 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3484 ordinal=3484 -->
## Functions

Functions

      where ψx is rms value and nis the number of elements in X.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Statistics Solver.vi

     RMSRMS (CDB)(CDB) VIVI

      Computes the root mean square (rms) of the input sequence X.


      Inputs/Outputs

               •     X —

          X is the complex input sequence. If X is empty, rms value is NaN.

               •     rms value —

          rms value is the root mean square computed from the magnitudes of the input sequence X.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The VI calculates rms value using the following equation:


      where ψx is rms value and nis the number of elements in X.


3484   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3484 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3485 ordinal=3485 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Statistics Solver.vi

MSEMSE VIVI

Computes the mean square error (mse) of the input sequences X Values and Y Values.


Inputs/Outputs

   •      Y Values —

    Y Values is an array of values. If the number of elements in Y Values is different from the number
     of elements in X Values, the VI computes mse based on the sequence that contains the fewest
    elements and returns a warning.

   •     X Values —

    X Values is an array of values. If the number of elements in X Values is different from the number
     of elements in Y Values, the VI computes mse based on the sequence that contains the fewest
    elements and returns a warning.

   •     mse —

   mse is the mean square error. If one of the input sequences is an empty array, the value of mse is
    NaN.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The VI calculates mse using the following equation.


                                                    © National Instruments 3485

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3485 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3486 ordinal=3486 -->
## Functions

Functions


      where nis the number of data points, xi is the ith element of X Values, and yi is the ith
      element of Y Values.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Statistics Solver.vi

    MomentMoment aboutabout MeanMean VIVI

      Computes the moment about the mean of the input sequence X using the specified
       order, m.


      Inputs/Outputs

               •     X —

          X is the input sequence. If X is empty, moment is NaN.

               •      order —

            order must be greater than 0. If order is less than or equal to 0, the VI sets moment to NaN and
             returns an error. The default is 2.

               •     moment —

          moment, which is calculated using the specified order, is the moment about the mean of the
            input sequence X.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error


3486   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3486 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3487 ordinal=3487 -->
## Functions

Functions


    Code VI to convert the error code or warning into an error cluster.


The VI computes the mth-order moment using the following equation.


where σxm is the mth-order moment, and nis the number of elements in the input
sequence X.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Statistics Solver.vi
  • labview\examples\Mathematics\Probability and Statistics\
   Noise Statistics.vi

CovarianceCovariance MatrixMatrix

Computes the covariance matrix of the input sequence X.


Inputs/Outputs

   •     X —

    X is the input sequence.

    Each column of X represents one vector of observed samples from one variable. Each row of X
    represents an observation from each variable.

   •      covariance matrix V —


                                                    © National Instruments 3487

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3487 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3488 ordinal=3488 -->
## Functions

Functions


            covariance matrix V returns the covariance matrix of X. If X is an n-by-m2D array, then the
            covariance matrix is a square m-by-mmatrix.

               •     mean vector —

         mean vector returns the mean of each column variable in X.

      Given mvectors of observed samples where the ith column contains the variate xi, the
       covariance matrix is defined as:

       Vij = cov(xi, xj) = (xi – µi)(xj – µj)

      where µi is the mean of variate xi. Each element Vij of covariance matrix V is the
       covariance between variates xi and xj. The diagonal of covariance matrix V contains
       the standard variances of each xi variate.

     mean vector returns the computed mean of each variate as shown by the following
       equation:

     mean vectori = µi
    ModeMode

       Finds the modes (most common values) or estimated modes (most common range
       centers) of the input sequence X. This VI can perform unimodal or multimodal
        analysis. You must manually select the polymorphic instance to use.


            • Unimode VI
            • Multimode VI

       Select the Unimodal instance if you are sure that the input sequence X is unimodal or
      you expect one scalar mode result. Select the Multimodal instance if you expect an


3488   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3488 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3489 ordinal=3489 -->
## Functions

Functions

array of modes. If the VI does not find a mode, the Unimodal instance returns NaN
without error and the Multimodal instance returns an empty array without error.

As defined in statistics, mode is the most frequently occurring value in a sequence of
numbers. For example, for the data set (3, 7, 3, 9, 9, 3, 5, 1, 8, 5), the unique mode is 3.
Similarly, for the data set (2, 4, 9, 6, 4, 6, 6, 2, 8, 2), two modes exist: 2 and 6. A
distribution with a single mode is unimodal. A distribution with more than one mode is
multimodal.

If you use the input sequence X = {0, 1, 3, 3, 4, 4, 4, 5, 5, 7} and set intervals to 1, the
Mode VI calculates mode as 3.5 because 3.5 is the center value of the one interval
intervals specifies. If you use the same input sequence for X and set intervals to 0, the
Mode VI returns the exact mode 4.

Refer to the Histogram VI for more information about histograms.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Statistics Solver.vi
  • labview\examples\Mathematics\Probability and Statistics\
   Noise Statistics.vi

UnimodeUnimode VIVI

Finds the modes (most common values) or estimated modes (most common range
centers) of the input sequence X. This VI can perform unimodal or multimodal
analysis. You must manually select the polymorphic instance to use.


Inputs/Outputs

   •     X —


                                                    © National Instruments 3489

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3489 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3490 ordinal=3490 -->
## Functions

Functions


          X must contain at least one sample.

                    If X is empty, the Mode VI sets mode to NaN.

                    If the input sequence has a constant value, the Mode VI ignores the number of intervals and sets
         mode to the constant value in the input sequence:

                    if X = a → mode = a

               •       intervals —

             intervals specifies the number of histograms to use when computing estimated modes. The
             default is 100.

           To find estimated modes, set intervals to a positive number of histogram bins so that the VI uses
           a histogram algorithm to return the best estimated mode of the input sequence. For intervals
              less than or equal to 0, the VI returns only the exact mode(s) of the input sequence. For intervals
             greater than 0, the VI uses a histogram to divide the input sequence X into bins, or intervals, and
             returns the center value (unimodal instance) or values (multimodal instance) of the bin that
            contains the most values from the input sequence. These estimated modes are generally more
             useful than the exact modes in real-world applications, where the data sequence contains even
           a small amount of noise.

               •     mode —

         mode returns the mode or estimated mode of X.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       Select the Unimodal instance if you are sure that the input sequence X is unimodal or
      you expect one scalar mode result. Select the Multimodal instance if you expect an
       array of modes. If the VI does not find a mode, the Unimodal instance returns NaN
       without error and the Multimodal instance returns an empty array without error.

      As defined in statistics, mode is the most frequently occurring value in a sequence of
      numbers. For example, for the data set (3, 7, 3, 9, 9, 3, 5, 1, 8, 5), the unique mode is 3.
        Similarly, for the data set (2, 4, 9, 6, 4, 6, 6, 2, 8, 2), two modes exist: 2 and 6. A
        distribution with a single mode is unimodal. A distribution with more than one mode is

3490   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3490 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3491 ordinal=3491 -->
## Functions

Functions

multimodal.

If you use the input sequence X = {0, 1, 3, 3, 4, 4, 4, 5, 5, 7} and set intervals to 1, the
Mode VI calculates mode as 3.5 because 3.5 is the center value of the one interval
intervals specifies. If you use the same input sequence for X and set intervals to 0, the
Mode VI returns the exact mode 4.

Refer to the Histogram VI for more information about histograms.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Statistics Solver.vi
  • labview\examples\Mathematics\Probability and Statistics\
   Noise Statistics.vi

MultimodeMultimode VIVI

Finds the modes (most common values) or estimated modes (most common range
centers) of the input sequence X. This VI can perform unimodal or multimodal
analysis. You must manually select the polymorphic instance to use.


Inputs/Outputs

   •     X —

    X must contain at least one sample.

       If X is empty, the Mode VI sets Modes to an empty array.

       If the input sequence has a constant value, the Mode VI ignores the number of intervals and sets
   mode to the constant value in the input sequence:

       if X = a → mode = a


                                                    © National Instruments 3491

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3491 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3492 ordinal=3492 -->
## Functions

Functions

               •       intervals —

             intervals specifies the number of histograms to use when computing estimated modes. The
             default is 100.

           To find estimated modes, set intervals to a positive number of histogram bins so that the VI uses
           a histogram algorithm to return the best estimated mode of the input sequence. For intervals
              less than or equal to 0, the VI returns only the exact mode(s) of the input sequence. For intervals
             greater than 0, the VI uses a histogram to divide the input sequence X into bins, or intervals, and
             returns the center value (unimodal instance) or values (multimodal instance) of the bin that
            contains the most values from the input sequence. These estimated modes are generally more
             useful than the exact modes in real-world applications, where the data sequence contains even
           a small amount of noise.

               •     Modes —

          Modes returns the modes found in X.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       Select the Unimodal instance if you are sure that the input sequence X is unimodal or
      you expect one scalar mode result. Select the Multimodal instance if you expect an
       array of modes. If the VI does not find a mode, the Unimodal instance returns NaN
       without error and the Multimodal instance returns an empty array without error.

      As defined in statistics, mode is the most frequently occurring value in a sequence of
      numbers. For example, for the data set (3, 7, 3, 9, 9, 3, 5, 1, 8, 5), the unique mode is 3.
        Similarly, for the data set (2, 4, 9, 6, 4, 6, 6, 2, 8, 2), two modes exist: 2 and 6. A
        distribution with a single mode is unimodal. A distribution with more than one mode is
       multimodal.

           If you use the input sequence X = {0, 1, 3, 3, 4, 4, 4, 5, 5, 7} and set intervals to 1, the
     Mode VI calculates mode as 3.5 because 3.5 is the center value of the one interval
       intervals specifies. If you use the same input sequence for X and set intervals to 0, the
     Mode VI returns the exact mode 4.

       Refer to the Histogram VI for more information about histograms.


3492   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3492 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3493 ordinal=3493 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Statistics Solver.vi
  • labview\examples\Mathematics\Probability and Statistics\
   Noise Statistics.vi

MedianMedian

Finds the median value of the input sequence X by sorting the values of X and
averaging the middle element(s) of the sorted array.


Inputs/Outputs

   •     X —

    X is the input sequence. If X is empty, median is NaN.

   •     median —

    median is the calculated median value of the input sequence X.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The Median VI finds median using the following identity.


where nis the number of elements in the input sequence X, sis the sorted sequence of
X,            , and         .

                                                    © National Instruments 3493

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3493 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3494 ordinal=3494 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Statistics Solver.vi

     HistogramHistogram

       Finds the discrete histogram of the input sequence X.


      Inputs/Outputs

               •     X —

          X must contain at least one sample. If X is empty, the histogram is undefined, and the VI sets
            Histogram: h(x) and X Values to empty arrays and returns an error.

               •       intervals —

             intervals specifies the number of intervals, or bins, to use in the histogram and must be greater
           than 0. If intervals is less than or equal to 0, the histogram is undefined, and the VI sets
            Histogram: h(X) and X Values to empty arrays and returns an error. The default is 10.

               •      Histogram Graph —

           Histogram Graph displays the bar graph of the histogram of the input sequence X. The y-axis is
            the histogram count, and the x-axis is the histogram center values of the intervals (bins) of the
            histogram.

               •      Histogram: h(x) —

            Histogram: h(x) is the discrete histogram of the input sequence X.

               •     X Values —


3494   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3494 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3495 ordinal=3495 -->
## Functions

Functions


    X Values is an array of the center values of the interval (bin) of the histogram.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The histogram is a frequency count of the number of times that a specified interval
occurs in the input sequence. The width of the frequency bin is

delta_x= (max–min)/m

where mis the requested number of bins. The centers of each bin are set according to
the following equation:

center[i] = min + delta_x/2 + i* delta_x.

Example

If the input sequence is

X = {0, 1, 3, 3, 4, 4, 4, 5, 5, 8}

then the Histogram: h(x) of X for eight intervals is

h(X) = {h0, h1, h2, h3, h4, h5, h6, h7} = {1, 1, 0, 2, 3, 2, 0, 1}

Notice that the histogram of the input sequence X is a function of X.

The VI calculates Histogram: h(x) as follows. The VI scans the input sequence X to
determine the range of values in it. Then the VI establishes the interval width, Δx,
according to the specified number of intervals,


where max is the maximum value found in the input sequence X, min is the minimum
value found in the input sequence X, and mis the specified number of intervals.

                                                    © National Instruments 3495

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3495 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3496 ordinal=3496 -->
## Functions

Functions

       Let χ represent the output sequence X Values, because the histogram is a function of X.
      The VI evaluates elements of c using

       χi = min + 0.5Δx+ iΔx

        for i= 0, 1, 2, …, m– 1

      The VI defines the ith interval to be the range of values from up to but not including,

      Δi ∈ (χi – 0.5Δx, χi + 0.5Δx)

        for i= 0, 1, 2, …, m– 1

      and defines the function to be


      The function has unity value if the value of xfalls within the specified interval.
      Otherwise it is zero. Notice that the interval Δi is centered about χi, and its width is Δx.

      The last interval, Δm–1, is defined. In other words, if a value is equal to max, it is
      counted as belonging to the last interval.

        Finally, the VI evaluates the histogram sequence Husing


      where hi represents the elements of the output sequence Histogram: h(x), and nis the
      number of elements in the input sequence X.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Statistics Solver.vi

3496   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3496 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3497 ordinal=3497 -->
## Functions

Functions

  • labview\examples\Mathematics\Probability and Statistics\
   Probability Density.vi
  • labview\examples\Mathematics\Probability and Statistics\
   Noise Statistics.vi

GeneralGeneral HistogramHistogram VIVI

Finds the discrete histogram of the input sequence X based on the given bin
specifications.


Inputs/Outputs

   •     X —

    X represents the input data.

   •      Bins —

    Bins specifies the boundaries of each bin of the histogram.

    The input Bins is an array of clusters where each cluster defines the range of values for a bin.

         •      lower —

        lower specifies the lower boundaries of the bin.

         •      upper —

       upper specifies the upper boundaries of the bin.

         •       inclusion —

         inclusion specifies how to treat the boundaries of each bin.


                                                    © National Instruments 3497

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3497 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3498 ordinal=3498 -->
## Functions

Functions


                           If no bin specifications are provided in the input Bins, the inputs max, min, # bins, and
                 inclusion are used to specify a set of uniformly spaced bins.

               0 Lower—Lower boundary is part of the bin but not the upper boundary.
               1 Upper—Upper boundary is part of the bin but not the lower boundary.
               2 Both—Both boundaries are part of the bin.
               3 Neither—Excludes both boundaries from the bin.


               •     max —

         max specifies the maximum value to include in the histogram. LabVIEW ignores this control if
            the Bins input array is not empty.

               •     min —

          min specifies the minimum value to include in the histogram. LabVIEW ignores this control if the
            Bins input array is not empty.

               •      # bins —

           # bins specifies the number of bins in the histogram. # bins is ignored if the Bins input array is
            not empty.

          The default behavior is to determine the number of bins according to Sturges' Rule, number of
            bins = 1 + 3.3log(size of(X)).

               •       inclusion —

             inclusion specifies how to handle the boundaries of each bin.

                    If array Bins is not empty, LabVIEW ignores the max, min, # bins, and inclusion inputs.

           0  lower—Includes the lower boundary.
           1  upper—Includes the upper boundary.

               •      Histogram Graph —

           Histogram Graph displays the bar graph of the histogram of the input sequence X. The y-axis is
            the histogram count, and the x-axis is the histogram center values of the intervals (bins) of the


3498   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3498 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3499 ordinal=3499 -->
## Functions

Functions


  histogram.

•      Histogram —

  Histogram specifies the resulting histogram.

•       Axis —

  Axis specifies the center values for each bin of Histogram.

  The centers of each bin are set according to the following equation and returned in the output
  array Axis. center[i] = (lower + upper)/2,where lower is the lower boundary of bin i, and upper is
  the upper boundary of bin i.

•      # outside —

  # outside contains information about points not falling in any bin upon successful execution of
  the VI.

        Note The elements above and below have meaning only if you specify Bins such
           that Bins[0].upper ≤ Bins[1].lower < Bins[1].upper, …– < Bins[k– 1].lower, and <
          Bins[k– 1].upper, where kis the number of elements in Bins.

      •       total —

       total contains the total number of values in X not falling in any bin upon successful
       execution.

      •     below —

     below represents the number of values in X below the first bin on the lower boundary. The
         first bin on the lower boundary is Bins[0].lower.

      •     above —

     above represents the number of values in X above the last bin on the upper boundary. The
        last bin on the upper boundary is Bins[size of(Bins) – 1].upper.


•       error —

  error returns any error or warning from the VI. You can wire error to the Error Cluster From Error


                                                   © National Instruments 3499

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3499 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3500 ordinal=3500 -->
## Functions

Functions


          Code VI to convert the error code or warning into an error cluster.


      The General Histogram VI completes the following steps to obtain the Histogram:

         1. Establishes all the bins, which are the intervals, based on the information in the
          input array Bins.
         2. Defines the function yi(x).
         3. Evaluates the histogram sequence H.

      Establishing the Bins

      The following equation defines the bin intervals.

        Δi = (Bins[i].lower: Bins[i].upper) i= 0, 1, 2, ..., k– 1

      where Bins[i].lower is the value lower in the ith cluster of array Bins, Bins[i].upper is
       the value upper in the ith cluster of array Bins, and kis the number of elements in
       Bins, which consists of the number of total bins.

      Whether the two ending points Bins[i].lower and Bins[i].upper of each bin are
       included in the bin Δi depends on the value of inclusion in the corresponding cluster i
       of Bins.

           If Bins is an empty array, the General Histogram VI uses the inputs max, min, and #
       bins to establish the bins. Each bin width Δxis the same and calculated with the
       following equation.


           If the Bins array contains elements, the bin widths are determined by the inclusion
      subparameter of the Bins parameter.

           If inclusion is set to lower, the bin widths are determined according to the following
       equations.


3500   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3500 -->

