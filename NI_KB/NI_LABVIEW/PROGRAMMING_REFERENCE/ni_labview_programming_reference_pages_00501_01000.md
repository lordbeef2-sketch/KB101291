# NI_LABVIEW_PROGRAMMING_REFERENCE

<!--SYSTEM_CORPUS id=NI_LABVIEW_PROGRAMMING_REFERENCE format=markdown generated=2026-07-14T12:02:18+00:00 -->
- title: LabVIEW Programming Reference Manual
- source: https://docs-be.ni.com/bundle/labview-api-ref/preprocessedpdf/enus
- source_sha256: 7a54c389b4f3d78e2215f55c9f156124d3668ce61d0d5018094e356004d895ac
- versions: 2024 Q1|2024 Q3|2025 Q1|2025 Q3|2026 Q1
- fidelity: full-text-records

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:501 ordinal=501 -->
## Functions

Functions

GetGet VIVI InformationInformation

Retrieves VI information from the data type stored in variant. To obtain the connector
pane data type, read the Connector Pane:DataType property of the VI class in VI Server.
This VI returns an error if variant does not contain a connector pane data type.


Inputs/Outputs

   •       variant —

    variant specifies the variant data from which you want to retrieve data type information.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       thrall info —

     thrall info returns the thrall information for each input and output in the VI. A LabVIEW class
    output is thralled to a LabVIEW class input if LabVIEW determines that the output data type is
    the same as the input data type. If, at run time, LabVIEW detects that an output is the same class
     as, or is a child class of, an input, LabVIEW can downcast the LabVIEW class output so that the
    output data type is the same as the input data type.

         •       Thralls —

         Thralls returns an array which contains the indices to the LabVIEW class inputs that a
       LabVIEW class output is thralled to. If a terminal is an input or a terminal is not thralled to
        any LabVIEW class input, Thralls returns an empty array.


   •       VI info —

     VI info returns the attributes related to the connector pane and other settings of the VI.


                                                    © National Instruments 501

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:501 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:502 ordinal=502 -->
## Functions

Functions


                   •      Connector Pane Pattern —

             Connector Pane Pattern returns the index to the connector pane pattern of the VI. Refer to
              the Connector Pane Pattern Reference VI located in the labview\examples\
           Application Control\VI Scripting\Connector Pane directory for a list of
              connector pane patterns and their indexes.

                   •      Connector Pane Rotation —

             Connector Pane Rotation returns a numeric value corresponding to the rotation of the
              connector pane.

             The following table contains the possible values for this output:

             0 Indicates that the connector pane did not rotate.
             1 Indicates that the connector pane rotated counter-clockwise by 90 degrees.
             2 Indicates that the connector pane rotated counter-clockwise by 180 degrees.
             3 Indicates that the connector pane rotated counter-clockwise by 270 degrees.

                   •      Flags —

               Flags returns flags of the VI. Flags contain additional information about a VI. Flags are useful
                 for National Instruments to diagnose bug reports from customers.

                   •      Modification Date —

               Modification Date returns the date when the VI was last modified.

                   •      Asynchronous —

             Asynchronous returns whether the VI pauses the execution until VIs on other threads finish
               executing.

                   •      Non-Function —

              Non-Function returns whether the VI outputs depend on the system state. For example, if
              the output constants in a VI cannot be constant folded even when all the VI inputs are
                constants, Non-Function returns TRUE.

                   •      Subroutine —


502   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:502 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:503 ordinal=503 -->
## Functions

Functions


        Subroutine returns whether the VI enables the subroutine priority in the Execution page of
        the VI Properties dialog box.

         •     SubSystem —

       SubSystem returns whether the VI is a subVI for the LabVIEW Control Design and Simulation
       Module that you can place only on a simulation diagram. SubSystem is valid only if you
        have installed the Control Design and Simulation Module.


   •       VI terminal types —

     VI terminal types returns the data types of the terminals in the VI.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

GetGet PolymorphicPolymorphic VIVI InformationInformation

Retrieves polymorphic VI information from the data type stored in variant. This VI
returns an error if variant does not contain a polymorphic VI.


Inputs/Outputs

   •       variant —

    variant specifies the variant data from which you want to retrieve data type information.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      time stamp —


                                                    © National Instruments 503

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:503 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:504 ordinal=504 -->
## Functions

Functions


          time stamp returns the time and date at which the polymorphic VI was last edited.

            •       error out —

           error out contains error information. This output provides standard error out functionality.

   GetGet MapMap CollectionCollection InformationInformation

      Retrieves map information from the data type stored in variant.

          Note This VI does not return information about values stored in the map.


     Inputs/Outputs

            •       variant —

           variant specifies the variant data from which you want to retrieve data type information. This VI
           returns an error if variant does not contain a map.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •      key data type —

         key data type returns the data type of the keys in the map stored in variant.

            •      value data type —

          value data type returns the data type of the values in the map stored in variant.

            •       error out —


504   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:504 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:505 ordinal=505 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.

GetGet SetSet CollectionCollection InformationInformation

Retrieves set information from the data type stored in variant.

      Note This VI does not return information about values stored in the set.


Inputs/Outputs

   •       variant —

    variant specifies the variant data from which you want to retrieve data type information. This VI
    returns an error if variant does not contain a set.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      element data type —

    element data type returns the data type of the elements in the set stored in variant.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

GetGet TypeType DefinitionDefinition PathPath

Returns the path to the type definition of the data type stored in variant.


                                                    © National Instruments 505

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:505 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:506 ordinal=506 -->
## Functions

Functions


     Inputs/Outputs

            •       variant —

           variant specifies the variant data from which you want to retrieve data type information.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •      type definition path —

          type definition path returns the path to the type definition of the data type stored in variant
        when the data type is an instance of a type definition. Otherwise, LabVIEW returns an empty
           path.

            •       error out —

           error out contains error information. This output provides standard error out functionality.

    IsIs oror ContainsContains TypeType DefinitionDefinition

     Returns TRUE if the data type stored in variant is an instance of a type definition or
     contains a data type which is an instance of a type definition.

          Note To determine whether the data type stored in variant is an instance of
            a type definition, you also can use the Get Type Information VI and wire an
              indicator to type definition.


506   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:506 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:507 ordinal=507 -->
## Functions

Functions

Inputs/Outputs

   •       variant —

    variant specifies the variant data from which you want to retrieve data type information.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •        is or contains typedef —

      is or contains typedef returns TRUE when the data type stored in variant is an instance of a type
     definition or contains a data type which is an instance of a type definition.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

DisconnectDisconnect TypeType DefinitionsDefinitions

Returns the data type stored in variant in and removes all connections to type
definitions from the data type.


Inputs/Outputs

   •       variant in —

    variant in specifies the variant data that you want to disconnect from type definitions.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       variant out —


                                                    © National Instruments 507

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:507 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:508 ordinal=508 -->
## Functions

Functions


           variant out returns the data type stored in variant in and removes all connections to type
            definitions from the data type.

            •       error out —

           error out contains error information. This output provides standard error out functionality.

  CheckCheck forfor ContainedContained DataData TypeType

     Returns TRUE if variant contains the data type you specify.


     Inputs/Outputs

            •       variant —

           variant specifies the variant data from which you want to retrieve data type information.

            •      data type to find —

          data type to find specifies the data type for which you want to search within the data type
           stored in variant.

            •      check inside refnums? (F) —

         check inside refnums? specifies whether to compare the data type stored in a refnum to data
          type to find.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     LabVIEW class qualified name ("") —


508   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:508 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:509 ordinal=509 -->
## Functions

Functions


    LabVIEW class qualified name specifies the LabVIEW class name to compare to any LabVIEW
     class stored in variant when data type to find is LabVIEW Class Instance. If LabVIEW class
    qualified name is empty, contains data type to find? returns TRUE when variant contains any
    LabVIEW classes.

   •      contains data type to find? —

    contains data type to find? returns TRUE if variant contains data type to find. For example, if
    variant is a cluster that contains a Boolean element and elements of other data types and data
    type to find is Boolean, contains data type to find? returns TRUE.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

GetGet LabVIEWLabVIEW ClassClass InformationInformation

Retrieves LabVIEW class information from the data type stored in variant. This VI
returns an error if variant does not contain a LabVIEW class.


Inputs/Outputs

   •       variant —

    variant specifies the variant data from which you want to retrieve data type information.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     LabVIEW class file name —

    LabVIEW class file name returns the name of the LabVIEW class file on disk.

   •       qualified LabVIEW class name —

                                                    © National Instruments 509

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:509 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:510 ordinal=510 -->
## Functions

Functions


           qualified LabVIEW class name returns an array that contains the LabVIEW class stored in
           variant, the project library that owns the LabVIEW class, and any project libraries that own the
           project library.

            •       error out —

           error out contains error information. This output provides standard error out functionality.

   GetGet LabVIEWLabVIEW ClassClass ParentParent AndAnd MemberMember VIVI
   InformationInformation

      Retrieves parent and member VI information of the LabVIEW class or interface stored in
      variant. This VI returns an error if variant does not contain a LabVIEW class or interface
     or if the LabVIEW class or interface is broken due to missing parents or missing private
     data control dependencies.


     Inputs/Outputs

            •       variant —

           variant specifies the variant data from which you want to retrieve data type information.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •      parent class —

          parent class returns the parent class of the LabVIEW class or interface.

            •     member VI info —


510   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:510 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:511 ordinal=511 -->
## Functions

Functions


   member VI info returns the qualified name, path, access scope, and dynamic dispatch
    information of all member VIs of the LabVIEW class or interface. Each array element represents
    one member VI. The path is empty if the member VI has not been saved.

         •       qualified name —

         •      path —

         •      access scope —

         •        is dynamic dispatch —


   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •      parent interfaces —

    parent interfaces returns the interfaces that the LabVIEW class or interface inherits from directly.

NumericNumeric

Use the Numeric VIs and functions to create and perform arithmetic and complex
mathematical operations on numbers and to convert numbers from one data type to
another. Use the VIs and functions on the Elementary and Special Functions and VIs
palette to perform trigonometric and logarithmic functions.

You also can access the following constants from this palette:

  • positive infinity
  • negative infinity
  • machine epsilon
  • not a number


                                                    © National Instruments 511

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:511 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:512 ordinal=512 -->
## Functions

Functions


       Palette                     Description
       Object

      Add                  Computes the sum of the inputs.       Function

       Subtract                  Computes the difference of the inputs.
       Function

        Multiply                    Returns the product of the inputs.       Function

       Divide                  Computes the quotient of the inputs.
       Function

       Quotient &                  Computes the integer quotient and the remainder of the inputs. This function      Remainder                   rounds floor(x/y) to the nearest integer towards -inf.
       Function

       Conversion   Use the Conversion VIs and functions to convert data types.

       Increment                  Adds 1 to the input value.       Function

      Decrement                     Subtracts 1 from the input value.       Function

      Add Array
       Elements     Returns the sum of all the elements in numeric array.
       Function

        Multiply                    Returns the product of all the elements in numeric array. If numeric array is an
       Array                  empty array, the function returns a value of 1. If numeric array contains only one
       Elements
                    element, the function returns that element.
       Function

                    Performs arithmetic on one or more numeric, array, cluster, or Boolean inputs. To
                       select the operation (Add, Multiply, AND, OR, or XOR), right-click the function and
     Compound
                       select Change Mode from the shortcut menu. When you select this function from the
       Arithmetic
                  Numeric palette, the default mode is Add. When you select this function from the
                   Boolean palette, the default mode is OR.

       Data
                  Use the Data Manipulation functions to modify the data types used in LabVIEW.
       Manipulation

       Absolute      Returns the absolute value of the input.


512   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:512 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:513 ordinal=513 -->
## Functions

Functions


Palette              Description
Object

Value
Function

Round To            Rounds the input to the nearest integer. If the value of the input is midway between
Nearest            two integers, the function returns the nearest even integer.Function

Round
Toward              Truncates the input to the next lowest integer.
-Infinity
Function

Round
Toward            Rounds the input to the next highest integer.+Infinity
Function

Scale By
Power Of 2    Multiplies x by 2 raised to the power of n.
Function

            Use the Complex functions to create complex numbers from two values given in
Complex      rectangular or polar and to break a complex number into its rectangular or polar
            components.

Square Root            Computes the square root of the input value.
Function

Square            Computes the square of the input value.
Function

Negate
             Negates the input value.
Function

Reciprocal
              Divides 1 by the input value.
Function

Sign
             Returns the sign of number.
Function

Scaling      Use the Scaling VIs to convert voltage readings to other temperature or strain units.


                                                    © National Instruments 513

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:513 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:514 ordinal=514 -->
## Functions

Functions


       Palette                     Description
       Object

      Numeric     Use the numeric constant to pass a numeric value to the block diagram. Set this
       Constant     value by clicking inside the constant with the Operating tool and typing a value.

     Enum       Use the enumerated constant to create a list of string labels with corresponding
       Constant      integer values you can select on the block diagram.

       Ring        Use the ring constant to create a list of value pairs you can select on the block
       Constant     diagram. Each value pair consists of a numeric value and corresponding string label.

     Random                   Produces a double-precision, floating-point number between 0 and 1. The number
      Number (0-1)                    generated is greater than or equal to 0, but less than 1. The distribution is uniform.       Function

     Random      Generates a random value from a specified range. Wire data to the upper bound or
      Number      lower bound input to determine the polymorphic instance to use or manually select
       (Range)       the instance.


                  Use the Fixed-Point functions to manipulate the overflow status of a fixed-point
       Fixed-Point                   number.


                  Use the DBL numeric constant to pass a double-precision, floating-point numeric
      DBL Numeric                     value to the block diagram. Set this value by clicking inside the constant with the       Constant                    Operating tool and typing a value.

        Positive                    Returns the value Inf (infinity).         Infinity

       Negative                    Returns the value -Inf (negative infinity).         Infinity

                    Represents the round-off error for a floating-point number with a given precision.
      Machine
                  Use the machine epsilon constant to compare whether two floating-point numbers
       Epsilon
                     are equivalent.

      Not A
      Number      Returns the value NaN (not a number).
       Constant


514   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:514 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:515 ordinal=515 -->
## Functions

Functions


 Palette               Description
 Object

 Math &
 Scientific     Use the Math & Scientific Constants to create LabVIEW applications.
 Constants

 Range Limits
              Returns the maximum and minimum values of the input data type. for Type

             Use the Expression Node to calculate expressions that contain a single variable. The
               following built-in functions are allowed in formulas: abs, acos, acosh, asin, asinh, Expression                atan, atanh, ceil, cos, cosh, cot, csc, exp, expm1, floor, getexp, getman, int, intrz, ln, Node                lnp1, log, log2, max, min, mod, rand, rem, sec, sign, sin, sinc, sinh, sizeOfDim, sqrt,
                tan, tanh.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Numerics\Numeric Functions.vi

AddAdd FunctionFunction

Computes the sum of the inputs.


Inputs/Outputs

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •      y —

    y can be a scalar number, a fixed-point number, an array or cluster of numbers, an array of
     clusters of numbers, a time stamp, and so on.

   •      x+y —

                                                    © National Instruments 515

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:515 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:516 ordinal=516 -->
## Functions

Functions


          x+y is the sum of x and y.

              Note You can manually configure this function to output data of a type you want. To
                     specify the output data type, right-click the function and select Properties to display
                   the Object Properties dialog box. On the Output Configuration page, click the
                  Representation icon and select the data type you want. A blue coercion dot appears
                on the output terminal of the function to indicate that you have configured the
                  output data type.


     Matrix Details

    When you wire matrix data as an input to this function, a VI that includes subVIs that
     work with the matrix data type replaces the function. The resulting VI has the same
     icon but contains a matrix-specific algorithm. The node remains a VI if you disconnect
     the matrix from the inputs. Wire other data types as inputs to restore the original
      function. If you wire a data type to a function and that data type causes a basic math
     operation to fail, the function returns a NaN.

     You also can add two or more values using the Compound Arithmetic function.

     Fixed-Point Details

         If you wire fixed-point values to Numeric functions such as Add, Subtract, Multiply, and
     Square, the functions usually return values that do not lose any bits of word length.
     However, if the operation creates a value that exceeds the maximum word length that
     LabVIEW accepts, overflow or rounding conditions can occur. LabVIEW accepts a
    maximum word length of 64 bits. Use the Numeric Node Properties dialog box to
      configure how LabVIEW handles overflow or rounding of fixed-point data.

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Numerics\Numeric Functions.vi


516   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:516 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:517 ordinal=517 -->
## Functions

Functions

SubtractSubtract FunctionFunction

Computes the difference of the inputs.

If you wire two waveform values or two dynamic data type values to this function,
error in and error out terminals appear on the function. Subtracting two time stamp
values yields a numeric value (difference in time), and subtracting a numeric value
from a time stamp value yields a time stamp. You cannot subtract a time stamp value
from a numeric value. The dimensions of two matrices that you want to subtract must
be the same. Otherwise, this function returns an empty matrix. The connector pane
displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x specifies the input value.

    This input accepts the following data types:
         • Number
         • Timestamp
         • Analog Waveform
    This input also accepts an array or an array of clusters of the listed data types.
   •      y —

    y can be a scalar number, a fixed-point number, an array or cluster of numbers, an array of
     clusters of numbers, a time stamp, and so on.

   •       x-y —

    x-y is the difference between x and y.

          Note You can manually configure this function to output data of a type you want. To
              specify the output data type, right-click the function and select Properties to display
             the Object Properties dialog box. On the Output Configuration page, click the
            Representation icon and select the data type you want. A blue coercion dot appears


                                                    © National Instruments 517

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:517 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:518 ordinal=518 -->
## Functions

Functions


                on the output terminal of the function to indicate that you have configured the
                  output data type.


    When you wire matrix data as an input to this function, a VI that includes subVIs that
     work with the matrix data type replaces the function. The resulting VI has the same
     icon but contains a matrix-specific algorithm. The node remains a VI if you disconnect
     the matrix from the input(s). Wire other data types as inputs to restore the original
      function. If you wire a data type to a function and that data type causes a basic math
     operation to fail, the function returns an empty matrix or NaN.

     Fixed-Point Details

         If you wire fixed-point values to Numeric functions such as Add, Subtract, Multiply, and
     Square, the functions usually return values that do not lose any bits of word length.
     However, if the operation creates a value that exceeds the maximum word length that
     LabVIEW accepts, overflow or rounding conditions can occur. LabVIEW accepts a
    maximum word length of 64 bits. Use the Numeric Node Properties dialog box to
      configure how LabVIEW handles overflow or rounding of fixed-point data.

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Numerics\Numeric Functions.vi

     MultiplyMultiply FunctionFunction

     Returns the product of the inputs.

         If you wire two waveform values or two dynamic data type values to this function,
      error in and error out terminals appear on the function. The connector pane displays
     the default data types for this polymorphic function.


518   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:518 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:519 ordinal=519 -->
## Functions

Functions

Inputs/Outputs

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •      y —

    y can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •      x*y —

    x*y is the product of x multiplied by y.


You cannot use this function to multiply a matrix and a vector. Use the A x B VI instead.

When multiplying two matrices, if the number of rows in the second matrix does not
match the number of columns in the first matrix, this function returns an empty
matrix. Refer to the A x B VI for more information about matrix multiplication.

When you wire matrix data as an input to this function, a VI that includes subVIs that
work with the matrix data type replaces the function. The resulting VI has the same
icon but contains a matrix-specific algorithm. The node remains a VI if you disconnect
the matrix from the input(s). Wire other data types as inputs to restore the original
function. If you wire a data type to a function and that data type causes a basic math
operation to fail, the function returns an empty matrix or NaN.

Fixed-Point Details

If you wire fixed-point values to Numeric functions such as Add, Subtract, Multiply, and
Square, the functions usually return values that do not lose any bits of word length.
However, if the operation creates a value that exceeds the maximum word length that
LabVIEW accepts, overflow or rounding conditions can occur. LabVIEW accepts a
maximum word length of 64 bits. Use the Numeric Node Properties dialog box to
configure how LabVIEW handles overflow or rounding of fixed-point data.

Examples

Refer to the following example files included with LabVIEW.

                                                    © National Instruments 519

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:519 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:520 ordinal=520 -->
## Functions

Functions

          • labview\examples\Numerics\Numeric Functions.vi

     DivideDivide FunctionFunction

     Computes the quotient of the inputs.


     Inputs/Outputs

            •      x —

          x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

            •      y —

          y can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

            •       x/y —

           x/y is a double-precision, floating-point number if both x and y are integers. In general, the
          output type is the widest representation of the inputs if the inputs are not integers or if their
           representations differ.

              Note You can manually configure this function to output data of a type you want. To
                     specify the output data type, right-click the function and select Properties to display
                   the Object Properties dialog box. On the Output Configuration page, click the
                  Representation icon and select the data type you want. A blue coercion dot appears
                on the output terminal of the function to indicate that you have configured the
                  output data type.


     Fixed-Point Details

         If you wire fixed-point values to this function, by default LabVIEW configures the
      integer word length of the quotient to avoid overflow for nonzero values of y. However,
     because the precision of the quotient can be infinite, rounding conditions always
      occur. Use the Numeric Node Properties dialog box to configure how LabVIEW handles
     rounding of fixed-point data. This function always uses the Saturate overflow mode to

520   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:520 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:521 ordinal=521 -->
## Functions

Functions

handle overflow.

QuotientQuotient && RemainderRemainder FunctionFunction

Computes the integer quotient and the remainder of the inputs. This function rounds
floor(x/y) to the nearest integer towards -inf.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •      y —

    y can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •       x-y*floor(x/y) —

     x-y*floor(x/y) is the remainder.

    This corresponds to the modulo function of text-based programming languages. When y is 1,
    the remainder is the fractional part of x.

   •       floor(x/y) —

     floor(x/y) is the integer quotient. If either input is a floating-point number, the quotient is a
     floating-point number with an integer value.

   When y is 1, the quotient is the integer part of x.


If the integer input value of y is zero, the quotient is zero and remainder is dividend x.
For floating-point inputs, if y is zero, the quotient is infinity and the remainder defaults
to NaN.


                                                    © National Instruments 521

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:521 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:522 ordinal=522 -->
## Functions

Functions

          Note Not all real numbers can be represented in the ANSI/IEEE standard
              floating-point numbers. Because of this, LabVIEW may encounter rounding
              errors and yield unexpected results if you use floating-point numbers with
               this function. For exact calculations and comparisons, convert floating-point
           numbers to integers.

    ConversionConversion

     Use the Conversion VIs and functions to convert data types.

    When these functions convert a floating-point number to an integer, they round the
     output to the nearest integer, or the nearest even integer if the fractional part is 0.5. If
     the result is out of range for the integer, these functions return the minimum or
    maximum value for the integer type. When these functions convert an integer to a
     smaller integer, they copy the least-significant bits without checking for overflow.
    When they convert an integer to a larger integer, they extend the sign of a signed
      integer and pad an unsigned integer with zeros.

     Use caution when you convert numbers to smaller representations, particularly when
     converting integers, because the LabVIEW conversion routines do not check for
      overflow.


       Palette
                 Description
       Object

      To
       Extended
       Precision  Converts a number to an extended-precision, floating-point number.
        Float
       Function

      To
      Double
       Precision  Converts a number to a double-precision, floating-point number.
        Float
       Function

522   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:522 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:523 ordinal=523 -->
## Functions

Functions


Palette          Description
Object

To Single
Precision          Converts a number to a single-precision, floating-point number.Float
Function

To Fixed-
Point     Converts any non-complex number to fixed-point representation.
Function

To Quad
Integer    Converts a number to a 64-bit integer in the range -(2^63) to (2^63)-1.
Function

To Long          Converts a number to a 32-bit integer in the range -(2^ 31) to (2^ 31)-1. This functionInteger         rounds all floating-point and fixed-point numeric values to the nearest integer.
Function

To Word
Integer    Converts a number to a 16-bit integer in the range -32,768 to 32,767.
Function

To Byte
Integer    Converts a number to an 8-bit integer in the range -128 to 127.
Function

To
Unsigned
Quad     Converts a number to a 64-bit unsigned integer in the range 0 to (2^64)-1.
Integer
Function

To
Unsigned
Long      Converts a number to a 32-bit unsigned integer in the range 0 to (2^32)-1.
Integer
Function

To
Unsigned
Word     Converts a number to a 16-bit unsigned integer in the range 0 to 65,535.
Integer
Function

To
          Converts a number to an 8-bit unsigned integer in the range 0 to 255.
Unsigned

                                                    © National Instruments 523

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:523 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:524 ordinal=524 -->
## Functions

Functions


       Palette                 Description
       Object

       Byte
        Integer
       Function

      To
       Extended
       Precision  Converts a number to an extended-precision, complex number.
      Complex
       Function

      To
      Double
       Precision  Converts a number to a double-precision, complex number.
      Complex
       Function

      To Single
       Precision                 Converts a number to a single-precision, complex number.      Complex
       Function

       Coerce
                 Converts the input data to a compatible data type while preserving the data value.      To Type                  Unlike the Type Cast function, this function does not reinterpret the input data.       Function

                 Converts an integer or fixed-point number to a Boolean array. If you wire an integer to      Number               number, Boolean array returns an array of 8, 16, 32, or 64 elements, depending on the
      To              number of bits in the integer. If you wire a fixed-point number to number, the size of the      Boolean                  array that Boolean array returns equals the word length of the fixed-point number. The
       Array                 0th element of the array corresponds to the least significant bit of the two's complement       Function
                  representation of the integer.

      Boolean
                 Converts a Boolean array to an integer or a fixed-point number by interpreting the array
       Array To
                 as the binary representation of the number. The first element of the array corresponds
      Number
                  to the least significant bit in the number.
       Function

      Boolean
                 Converts a Boolean FALSE or TRUE value to a 16-bit integer with a value of 0 or 1,
      To (0,1)
                   respectively.
       Function

      To Time
      Stamp    Converts a number to a timestamp.
       Function


524   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:524 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:525 ordinal=525 -->
## Functions

Functions


 Palette           Description
 Object

 String To
 Byte           Converts a string into an array of unsigned bytes. Array
 Function

 Byte
 Array To           Converts an array of unsigned bytes representing ASCII characters into a string. String
 Function

           Converts a physical number (a number that has a unit) to a pure number (a number with Convert         no units) or a pure number to a physical number. Right-click the function and select Unit           Build Unit String from the shortcut menu to build and edit a string of units.

 Cast Unit          Changes the base units associated with the input to the base units associated with unit
 Bases         and returns the results at the output terminal. Function

 Color to   Resolves any color input, including system colors, into its respective red, green, and blue
 RGB      components.


 RGB to
           Converts a red, green, and blue value from 0 to 255 to the corresponding RGB color. Color

 Enum to
 Array of   Creates an array of enums with the same number of elements as values in the enum.
 Enums

ToTo ExtendedExtended PrecisionPrecision FloatFloat FunctionFunction

Converts a number to an extended-precision, floating-point number.

The connector pane displays the default data types for this polymorphic function.


                                                    © National Instruments 525

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:525 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:526 ordinal=526 -->
## Functions

Functions

     Inputs/Outputs

            •     number —

        number can be a scalar number, array or cluster of numbers, array of clusters of numbers, and
          so on.

            •      extended precision float —

         extended precision float is of the same data type structure as number.


    ToTo DoubleDouble PrecisionPrecision FloatFloat FunctionFunction

     Converts a number to a double-precision, floating-point number.

     The connector pane displays the default data types for this polymorphic function.


     Inputs/Outputs

            •     number —

        number can be a scalar number, array or cluster of numbers, array of clusters of numbers, a time
          stamp, and so on.

            •      double precision float —

         double precision float is of the same data type structure as number.


    ToTo SingleSingle PrecisionPrecision FloatFloat FunctionFunction

     Converts a number to a single-precision, floating-point number.

     The connector pane displays the default data types for this polymorphic function.


526   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:526 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:527 ordinal=527 -->
## Functions

Functions


Inputs/Outputs

   •     number —

   number can be a scalar number, array or cluster of numbers, array of clusters of numbers, and
    so on.

   •       single precision float —

    single precision float is of the same data type structure as number.


ToTo Fixed-PointFixed-Point FunctionFunction

Converts any non-complex number to fixed-point representation.

If you do not wire a value to the fixed-point type input or configure the output settings
of this function, the data type of the fixed-point output adapts to the data you wire to
the number input. For example, if you wire an 8-bit unsigned integer to the number
input, LabVIEW returns an 8-bit unsigned fixed-point number with 8 integer bits. This
function saturates the number by default if overflow occurs.


Inputs/Outputs

   •       fixed-point type —

    fixed-point type is the fixed-point data type to which you want to convert the integer data. You
    can configure the fixed-point data type in the Data Type page of the Properties dialog box.
    LabVIEW ignores any data in the constant or control that you wire to fixed-point type. You also
    can leave this input unwired and configure the output data type in the Output Configuration
    page of the Properties dialog box.

   •     number —


                                                    © National Instruments 527

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:527 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:528 ordinal=528 -->
## Functions

Functions


        number can be any non-complex number.

            •       fixed-point —

           fixed-point is the input data scaled to the requested fixed-point data type.


     To override the default behavior of this function, right-click the function and select
     Properties from the shortcut menu to display the Output Configuration page of the
     Properties dialog box. You can use this dialog box to configure the output settings of
      this function.

    ToTo QuadQuad IntegerInteger FunctionFunction

     Converts a number to a 64-bit integer in the range -(2^63) to (2^63)-1.

     The connector pane displays the default data types for this polymorphic function.


     Inputs/Outputs

            •     number —

        number can be a scalar number, array or cluster of numbers, array of clusters of numbers, a time
          stamp, and so on.

            •      64bit integer —

           64bit integer is of the same data type structure as number.


      This function rounds all floating-point and fixed-point numeric values to the nearest
      integer. If the fractional part of the value is .5, the function rounds the value to the
     nearest even integer. For example, the function rounds 13.5 to 14 and rounds 14.5
      to 14.


528   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:528 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:529 ordinal=529 -->
## Functions

Functions

ToTo LongLong IntegerInteger FunctionFunction

Converts a number to a 32-bit integer in the range -(2^ 31) to (2^ 31)-1. This function
rounds all floating-point and fixed-point numeric values to the nearest integer.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •     number —

   number can be a scalar number, array or cluster of numbers, array of clusters of numbers, and
    so on.

   •      32bit integer —

    32bit integer is of the same data type structure as number.


If the fractional part of the floating-point or fixed-point value is .5, the function
rounds the value to the nearest even integer. For example, the function rounds 13.5
to 14 and rounds 14.5 to 14.

ToTo WordWord IntegerInteger FunctionFunction

Converts a number to a 16-bit integer in the range -32,768 to 32,767.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •     number —


                                                    © National Instruments 529

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:529 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:530 ordinal=530 -->
## Functions

Functions


        number can be a scalar number, array or cluster of numbers, array of clusters of numbers, and
          so on.

            •      16bit integer —

           16bit integer is of the same data type structure as number.


      This function rounds all floating-point and fixed-point numeric values to the nearest
      integer. If the fractional part of the value is .5, the function rounds the value to the
     nearest even integer. For example, the function rounds 13.5 to 14 and rounds 14.5
      to 14.

    ToTo ByteByte IntegerInteger FunctionFunction

     Converts a number to an 8-bit integer in the range -128 to 127.

     The connector pane displays the default data types for this polymorphic function.


     Inputs/Outputs

            •     number —

        number can be a scalar number, array or cluster of numbers, array of clusters of numbers, and
          so on.

            •       8bit integer —

           8bit integer is of the same data type structure as number.


      This function rounds all floating-point numeric values to the nearest integer. If the
      fractional part of the floating-point value is .5, the function rounds the value to the
     nearest even integer. For example, the function rounds 13.5 to 14 and rounds 14.5
      to 14.


530   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:530 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:531 ordinal=531 -->
## Functions

Functions

ToTo UnsignedUnsigned QuadQuad IntegerInteger FunctionFunction

Converts a number to a 64-bit unsigned integer in the range 0 to (2^64)-1.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •     number —

   number can be a scalar number, array or cluster of numbers, array of clusters of numbers, a time
    stamp, and so on.

   •      unsigned 64bit integer —

    unsigned 64bit integer is of the same data type structure as number.


This function rounds all floating-point and fixed-point numeric values to the nearest
integer. If the fractional part of the value is .5, the function rounds the value to the
nearest even integer. For example, the function rounds 13.5 to 14 and rounds 14.5
to 14.

ToTo UnsignedUnsigned LongLong IntegerInteger FunctionFunction

Converts a number to a 32-bit unsigned integer in the range 0 to (2^32)-1.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •     number —


                                                    © National Instruments 531

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:531 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:532 ordinal=532 -->
## Functions

Functions


        number can be a scalar number, array or cluster of numbers, array of clusters of numbers, a time
          stamp, and so on.

            •      unsigned 32bit integer —

          unsigned 32bit integer is of the same data type structure as number.


      This function rounds all floating-point and fixed-point numeric values to the nearest
      integer. If the fractional part of the value is .5, the function rounds the value to the
     nearest even integer. For example, the function rounds 13.5 to 14 and rounds 14.5
      to 14.

    ToTo UnsignedUnsigned WordWord IntegerInteger FunctionFunction

     Converts a number to a 16-bit unsigned integer in the range 0 to 65,535.

     The connector pane displays the default data types for this polymorphic function.


     Inputs/Outputs

            •     number —

        number can be a scalar number, array or cluster of numbers, array of clusters of numbers, and
          so on.

            •      unsigned 16bit integer —

          unsigned 16bit integer is of the same data type structure as number.


      This function rounds all floating-point and fixed-point numeric values to the nearest
      integer. If the fractional part of the value is .5, the function rounds the value to the
     nearest even integer. For example, the function rounds 13.5 to 14 and rounds 14.5
      to 14.


532   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:532 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:533 ordinal=533 -->
## Functions

Functions

ToTo UnsignedUnsigned ByteByte IntegerInteger FunctionFunction

Converts a number to an 8-bit unsigned integer in the range 0 to 255.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •     number —

   number can be a scalar number, array or cluster of numbers, array of clusters of numbers, and
    so on.

   •      unsigned 8bit integer —

    unsigned 8bit integer is of the same data type structure as number.


This function rounds all floating-point and fixed-point numeric values to the nearest
integer. If the fractional part of the value is .5, the function rounds the value to the
nearest even integer. For example, the function rounds 13.5 to 14 and rounds 14.5
to 14.

ToTo ExtendedExtended PrecisionPrecision ComplexComplex FunctionFunction

Converts a number to an extended-precision, complex number.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •     number —


                                                    © National Instruments 533

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:533 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:534 ordinal=534 -->
## Functions

Functions


        number can be a scalar number, array or cluster of numbers, array of clusters of numbers, and
          so on.

            •      extended precision complex —

         extended precision complex is of the same data type structure as number.


    ToTo DoubleDouble PrecisionPrecision ComplexComplex FunctionFunction

     Converts a number to a double-precision, complex number.

     The connector pane displays the default data types for this polymorphic function.


     Inputs/Outputs

            •     number —

        number can be a scalar number, array or cluster of numbers, array of clusters of numbers, and
          so on.

            •      double precision complex —

         double precision complex is of the same data type structure as number.


    ToTo SingleSingle PrecisionPrecision ComplexComplex FunctionFunction

     Converts a number to a single-precision, complex number.

     The connector pane displays the default data types for this polymorphic function.


534   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:534 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:535 ordinal=535 -->
## Functions

Functions

Inputs/Outputs

   •     number —

   number can be a scalar number, array or cluster of numbers, array of clusters of numbers, and
    so on.

   •       single precision complex —

    single precision complex is of the same data type structure as number.


CoerceCoerce ToTo TypeType FunctionFunction

Converts the input data to a compatible data type while preserving the data value.
Unlike the Type Cast function, this function does not reinterpret the input data.

Use this function in the following cases:

  • To eliminate a coercion dot
  • To convert data without a type definition to a compatible type definition or vice
    versa
  • To rename data on the wire, such as a user event refnum


Inputs/Outputs

   •      type —

    type specifies the data type to which you want to convert the input data x.

    To set the data type to which you want to convert the input data, wire a constant or control of
    the desired data type to type. LabVIEW ignores any data in the constant or control wired to type.

   •      x —

    x specifies the data you want to convert.


                                                    © National Instruments 535

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:535 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:536 ordinal=536 -->
## Functions

Functions


           This input accepts any data type.

            •      coerced x —

          coerced x returns the value of the input data x after the conversion.


     The Type Cast function also converts data to a desired data type. Unlike the Type Cast
      function, the Coerce To Type function allows only conversion between compatible
     data types to preserve the value of the input data, similar to what a coercion dot does.
     The Type Cast function allows conversion between incompatible data types by
      flattening and unflattening the input data, which allows for radical reinterpretation of
     the data. When the desired data type requires a different memory size than the input
      data, the Type Cast function may reinterpret the input data. NI recommends that you
     use the Coerce To Type function instead of the Type Cast function to avoid
      reinterpreting the data.

    NumberNumber ToTo BooleanBoolean ArrayArray FunctionFunction

     Converts an integer or fixed-point number to a Boolean array. If you wire an integer to
     number, Boolean array returns an array of 8, 16, 32, or 64 elements, depending on the
    number of bits in the integer. If you wire a fixed-point number to number, the size of
     the array that Boolean array returns equals the word length of the fixed-point number.
     The 0th element of the array corresponds to the least significant bit of the two's
     complement representation of the integer.


     Inputs/Outputs

            •     number —

        number can be a number.

            •      Boolean array —

         Boolean array can have 8, 16, 32, or 64 elements if number is an integer. If number is a fixed-


536   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:536 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:537 ordinal=537 -->
## Functions

Functions


    point number, Boolean array can have between 1 and 64 elements.


If you wire a fixed-point number that includes an overflow status to number, this
function ignores the overflow status and converts only the number to a Boolean array.

BooleanBoolean ArrayArray ToTo NumberNumber FunctionFunction

Converts a Boolean array to an integer or a fixed-point number by interpreting the
array as the binary representation of the number. The first element of the array
corresponds to the least significant bit in the number.


Inputs/Outputs

   •      Boolean array —

    Boolean array is a one-dimensional array of Boolean values.

    This function truncates Boolean array if it is too long. If Boolean array is too short, this function
    pads Boolean array according to the Sign Extension Mode you can select by right-clicking the
     function.

         • Never —This function pads Boolean array with Boolean FALSE bits.
         •  If Output Is Signed —(default) For an output with an unsigned representation, this function
       pads Boolean array with Boolean FALSE bits. For an output with a signed representation,
          this function pads Boolean array with the last element of the array.
         • Always —This function pads Boolean array with the last element of the array.
   •     number —

   number is an integer or a fixed-point number.

    You can change the numeric representation of number on the Output Configuration page of the
    Properties dialog box. Right-click the function and select Properties to display the Properties
    dialog box.


The following table shows the relationship between Boolean array and number.


                                                    © National Instruments 537

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:537 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:538 ordinal=538 -->
## Functions

Functions


                                 Output              Sign Extension     Binary      Boolean array                                                        number
                                    Representation     Mode             Value

       {FALSE, TRUE}                     I8                                If Output Is Signed  11111110    -2

       {FALSE, TRUE}              U8                               If Output Is Signed  00000010   2

       {FALSE, TRUE, FALSE, TRUE}      I8                  Always            11111010    -6

       {FALSE, TRUE, FALSE, TRUE}      I8                  Never             00001010   10

       {FALSE, FALSE, TRUE, FALSE,                              U8                               If Output Is Signed  00010100   20      TRUE}

       {FALSE, FALSE, TRUE, FALSE,                              U8                  Always            11110100   244
      TRUE}

     BooleanBoolean ToTo (0,1)(0,1) FunctionFunction

     Converts a Boolean FALSE or TRUE value to a 16-bit integer with a value of 0 or 1,
      respectively.


     Inputs/Outputs

            •      Boolean —

         Boolean can be a scalar, an array, a cluster of Boolean values, an array of clusters of Boolean
           values, and so on. If Boolean is an error cluster, only the status parameter of the error cluster
          passes to the input terminal.

            •       0, 1 —

            0, 1 is 0 if Boolean is FALSE and 1 if Boolean is TRUE.


    ToTo TimeTime StampStamp FunctionFunction

     Converts a number to a timestamp.


538   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:538 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:539 ordinal=539 -->
## Functions

Functions


Inputs/Outputs

   •     number —

   number can be a scalar number, array or cluster of numbers, array of clusters of numbers, and
    so on, that represents the amount of seconds from the epoch time of 12 a.m., January 1, 1904
    [01-01-1904 00:00:00].

   •      time stamp —

    time stamp is a time-zone-independent number of seconds that have elapsed since 12:00 a.m.,
     Friday, January 1, 1904, Universal Time [01-01-1904 00:00:00].


StringString ToTo ByteByte ArrayArray FunctionFunction

Converts a string into an array of unsigned bytes.

Each byte in the array has the ASCII value of the corresponding character in the string.


Inputs/Outputs

   •       string —

     string is the input string the function converts.

   •      unsigned byte array —

    unsigned byte array is the output array.

    The first byte in the array has the ASCII value of the first character in string, the second byte has
    the second value, and so on.

ByteByte ArrayArray ToTo StringString FunctionFunction

Converts an array of unsigned bytes representing ASCII characters into a string.

                                                    © National Instruments 539

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:539 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:540 ordinal=540 -->
## Functions

Functions


     Inputs/Outputs

            •      unsigned byte array —

          unsigned byte array is the array of ASCII values you want to convert.

            •       string —

           string is the result of interpreting each array element as an ASCII value and forming a string out
           of the corresponding characters.

           Refer to ASCII Codes for the numbers that correspond to each character.


     ConvertConvert UnitUnit

     Converts a physical number (a number that has a unit) to a pure number (a number
     with no units) or a pure number to a physical number. Right-click the function and
      select Build Unit String from the shortcut menu to build and edit a string of units.


     Inputs/Outputs

            •    —

          x is a floating-point number with or without a unit.

            •    —

          y is a floating-point number that has a unit if x does not have a unit. y does not have a unit if x
         does have a unit.


      Edit the unit string by using the Labeling or Operating tool to highlight the string and
      entering a new string. You also can right-click the function and select Build Unit String
     from the shortcut menu to display the Build Unit String dialog box. The unit you enter

540   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:540 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:541 ordinal=541 -->
## Functions

Functions

must be a unit available in LabVIEW.

If the input is a physical number measured in a compatible unit, the output is a pure
number measured in the unit specified. For example, if x is 37 meters (m), and you
enter m (meters) as the unit in the Convert Unit function, y is 37 with no associated
units. If x is 37 meters and you enter ft (feet) as the unit in the Convert Unit function, y
is 121.36 with no associated units.

If the input is a pure number, LabVIEW assigns the unit you specify in the Convert Unit
function to the number and returns that physical number in the base unit (or a
combination of base units) for that class of measurement, as indicated in the following
table.


 Class                                         Base Unit         Abbreviation

 amount of substance                           mole           mol

 angle (plane)                                       radian            rad

 angle (solid)                                         steradian           sr

 electric current                               ampere         A

 length                                         meter       m

 luminous intensity                                candela          cd

 mass                                             kilogram         kg

 temperature (thermodynamic)                         kelvin          K

 time                                          second            s

For example, if x is 10 and you enter s (seconds) as the unit in the Convert Unit
function, y is 10 seconds because seconds is the base unit LabVIEW uses to measure
time. If x is 10 and you enter min (minutes) as the unit in the Convert Unit function, y is
600 seconds. You then can change the unit the indicator displays to show minutes,
hours, or any other unit of time.

CastCast UnitUnit BasesBases FunctionFunction

Changes the base units associated with the input to the base units associated with
unit and returns the results at the output terminal.

                                                    © National Instruments 541

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:541 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:542 ordinal=542 -->
## Functions

Functions

          Caution Use this function with extreme caution. Because this function
            works with bases, you must understand the conversion from an arbitrary unit
             to its bases before you can effectively use this function. This function can
           change base units, such as changing meters to kilograms.


     Inputs/Outputs

            •       unit (none) —

           unit associates input with output results.

         The default is none, which does not associate any units.

            •      x —

          x is a floating-point number with or without a unit.

            •      x —

          x returns the same data type and structure as x.


     Wiring unit to a constant of units mm is no different than wiring to a constant of units m
     because the base unit (m) is identical. In most instances, use the Convert Unit function
      to turn the units feature on or off or to convert between units.

     ColorColor toto RGBRGB

     Resolves any color input, including system colors, into its respective red, green, and
     blue components.

     To perform a task such as color arithmetic with symbolic colors, you must convert the
      colors to their red, green, and blue components.


542   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:542 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:543 ordinal=543 -->
## Functions

Functions


Inputs/Outputs

   •      Color —

    Color is the color that you want to convert to its respective red, green, and blue components.

   •      Resolved Color —

    resolved color is the resolved color in RGB format.

   •     R —

   R is the red component of the RGB value, 0 to 255.

   •     G —

   G is the green component of the RGB value, 0 to 255.

   •     B —

   B is the blue component of the RGB value, 0 to 255.


RGBRGB toto ColorColor

Converts a red, green, and blue value from 0 to 255 to the corresponding RGB color.


Inputs/Outputs

   •     R —

   R is the red value for the color, 0 to 255.

   •     G —


                                                    © National Instruments 543

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:543 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:544 ordinal=544 -->
## Functions

Functions


        G is the green value for the color, 0 to 255.

            •     B —

        B is the blue value for the color, 0 to 255.

            •      Color —

          Color is the RGB color value that corresponds to R, G, and B.


    EnumEnum toto ArrayArray ofof EnumsEnums

     Creates an array of enums with the same number of elements as values in the enum.


     Inputs/Outputs

            •     enum —

        enum specifies the input enum.

            •      array of enums —

           array of enums returns an array containing each enum value in order.

          For example, if enum has values {cat, dog, bird}, array of enums returns a three-element array
          with values cat, dog, and bird, respectively.

    IncrementIncrement FunctionFunction

     Adds 1 to the input value.

     The connector pane displays the default data types for this polymorphic function.


544   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:544 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:545 ordinal=545 -->
## Functions

Functions


Inputs/Outputs

   •      x —

    x specifies the input value.

    This input accepts the following data types:

         • Number
         • Timestamp
         • Analog Waveform

    This input also accepts an array or an array of clusters of the listed data types.

   •      x+1 —

    x+1 is the result of x+1. If the input is a time stamp value, this function increments the time by
    one second. If the input is an enumerated type value, this function increments the last
    enumerated value to the first.

          Note You can manually configure this function to output data of a type you want. To
              specify the output data type, right-click the function and select Properties to display
             the Object Properties dialog box. On the Output Configuration page, click the
            Representation icon and select the data type you want. A blue coercion dot appears
           on the output terminal of the function to indicate that you have configured the
            output data type.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Numerics\Numeric Functions.vi

DecrementDecrement FunctionFunction

Subtracts 1 from the input value.

The connector pane displays the default data types for this polymorphic function.

                                                    © National Instruments 545

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:545 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:546 ordinal=546 -->
## Functions

Functions


     Inputs/Outputs

            •      x —

          x specifies the input value.

           This input accepts the following data types:

                   • Number
                   • Timestamp
                   • Analog Waveform

           This input also accepts an array or an array of clusters of the listed data types.

            •       x-1 —

           x-1 is the result of x-1. If the input is a time stamp value, this function decrements the time by
         one second. If the input is an enumerated type value, this function decrements the first
         enumerated value to the last.

              Note You can manually configure this function to output data of a type you want. To
                     specify the output data type, right-click the function and select Properties to display
                   the Object Properties dialog box. On the Output Configuration page, click the
                  Representation icon and select the data type you want. A blue coercion dot appears
                on the output terminal of the function to indicate that you have configured the
                  output data type.


    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Numerics\Numeric Functions.vi

    AddAdd ArrayArray ElementsElements FunctionFunction

     Returns the sum of all the elements in numeric array.


546   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:546 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:547 ordinal=547 -->
## Functions

Functions

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      numeric array —

    numeric array can have any number of dimensions.

   •     sum —

   sum is of the same data type and structure as the elements in numeric array.


      Note You cannot use this function with fixed-point numbers. If you wire
        fixed-point numbers to this function, the VI appears with a broken Run
        button.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Numerics\Numeric Functions.vi

MultiplyMultiply ArrayArray ElementsElements FunctionFunction

Returns the product of all the elements in numeric array. If numeric array is an empty
array, the function returns a value of 1. If numeric array contains only one element, the
function returns that element.

The connector pane displays the default data types for this polymorphic function.


                                                    © National Instruments 547

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:547 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:548 ordinal=548 -->
## Functions

Functions

     Inputs/Outputs

            •      numeric array —

         numeric array can have any number of dimensions.

            •      product —

          product is of the same data type and structure as the elements in numeric array.


          Note You cannot use this function with fixed-point numbers. If you wire
              fixed-point numbers to this function, the VI appears with a broken Run
             button.

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Numerics\Numeric Functions.vi

   CompoundCompound ArithmeticArithmetic

     Performs arithmetic on one or more numeric, array, cluster, or Boolean inputs. To
      select the operation (Add, Multiply, AND, OR, or XOR), right-click the function and
      select Change Mode from the shortcut menu. When you select this function from the
     Numeric palette, the default mode is Add. When you select this function from the
     Boolean palette, the default mode is OR.

     The connector pane displays the default data types for this polymorphic function.


     Inputs/Outputs

            •      value —


548   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:548 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:549 ordinal=549 -->
## Functions

Functions


    value 0..n-1 can be a number or Boolean value, an array of numbers or Boolean values, a cluster,
    array of clusters, and so on.

    You can wire a waveform to only one value input. If an input is a waveform, you can have an
    unlimited number of scalar inputs of varying sizes. If value is an error cluster, only the status
    parameter of the error cluster passes to the input terminal.

   •      value —

   •       result —

     result returns the result of the selected operation applied to the value 0..n-1. For AND, OR, or
    XOR, result returns the bitwise operations on numeric inputs and logical operations on Boolean
     inputs.


Add inputs to the node by right-clicking an input and selecting Add Input from the
shortcut menu or by resizing the function.

You can invert the inputs or the output of this function by right-clicking the individual
terminals and selecting Invert from the shortcut menu. For Add, select Invert to
negate an input or the output. For Multiply, select Invert to use the reciprocal of an
input or to produce the reciprocal of the output. For AND, OR, or XOR, select Invert to
bitwise complement an integer input or output or to logically negate an input or
output.

When you use the Compound Arithmetic function to perform an XOR operation on 3 or
more values, the Compound Arithmetic function performs an XOR operation on the
first pair of inputs, then performs an XOR operation on the result of the first pair of
inputs and the next input, and so on until all inputs have been processed.

      Note You cannot use this function with fixed-point numbers. If you wire
        fixed-point numbers to this function, the VI appears with a broken Run
        button.

DataData ManipulationManipulation

Use the Data Manipulation functions to modify the data types used in LabVIEW.


                                                    © National Instruments 549

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:549 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:550 ordinal=550 -->
## Functions

Functions


       Palette                  Description
       Object

                   Casts x to the data type, type, by flattening it and unflattening it using the new data
      Type Cast  type. If the function must reinterpret data instead of transforming it, LabVIEW uses a
       Function   temporary buffer. This function has the risk of reinterpreting data. To preserve the data
                  value while converting the data, use the Coerce To Type function instead.

        Flatten To  Converts the anything input to a flattened data string of binary values. You also can use
        String       this function to convert the byte order, or endian format, of the data in the flattened
       Function   data string.

       Unflatten                  Converts binary string to the type wired to type. binary string should contain flattened      From                  data of the type wired to type. You also can use this function to specify the byte order,        String                  or endian format, of the data in the binary string.
       Function

       Mantissa
     &          Returns the mantissa and exponent of the input numeric value such that number =
      Exponent  mantissa * 2^exponent.
       Function

       Rotate
        Left With   Rotates each bit in the input value one bit to the left (from least significant to most
       Carry       significant bit), inserts carry in the low-order bit, and returns the most significant bit.
       Function

       Rotate
       Right With  Rotates each bit in value one bit to the right (from most significant to least significant),
       Carry       inserts carry in the high-order bit, and returns the least significant bit.
       Function

       Logical
        Shift        Shifts x the number of bits specified by y.
       Function

       Rotate
                  Rotates x the number of bits specified by y.
       Function

        Split
      Number   Breaks a number into its component bytes or words.
       Function

       Join
      Numbers   Creates a number from the component bytes or words.
       Function

      Swap     Swaps the high-order 8 bits and the low-order 8 bits for every word in data.

550   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:550 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:551 ordinal=551 -->
## Functions

Functions


 Palette            Description
 Object

 Bytes
 Function

 Swap
 Words    Swaps the high-order 16 bits and the low-order 16 bits for every long integer in data.
 Function

 Byte Array Computes the message digest on a byte array. You must manually select the
 Checksum polymorphic instance you want to use.


TypeType CastCast FunctionFunction

Casts x to the data type, type, by flattening it and unflattening it using the new data
type. If the function must reinterpret data instead of transforming it, LabVIEW uses a
temporary buffer. This function has the risk of reinterpreting data. To preserve the data
value while converting the data, use the Coerce To Type function instead.

      Note You can also use the Conversion VIs and functions to convert data
        types.


Inputs/Outputs

   •      type —

    type is the data type to which you want to convert the data. Wire any constant or control to type
    to set the data type to which you want to convert the data. LabVIEW ignores any data in the
    constant or control you wire to type.

   •      x —

    x specifies the data you want to convert.


                                                    © National Instruments 551

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:551 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:552 ordinal=552 -->
## Functions

Functions


           This input accepts any data type.

            •      *(type *) &x —

           *(type *) &x is the value provided in x and converted to the same data type as type.


    Choosing between the Type Cast Function and the Coerce To Type
    Function

     The Coerce To Type function also converts data to a desired data type. Unlike the
     Coerce To Type function, the Type Cast function allows conversion between
     incompatible data types by flattening and unflattening the input data, which allows for
      radical reinterpretation of the data. When the desired data type requires a different
    memory size than the input data, the Type Cast function may reinterpret the input
      data. The Coerce To Type function allows only conversion between compatible data
     types to preserve the value of the input data, similar to what a coercion dot does. You
      also can use the Coerce To Type function to convert a type definition or rename data
    on the wire, such as a user event refnum. NI recommends that you use the Coerce To
     Type function instead of the Type Cast function to avoid reinterpreting the data.

     Effects of Mismatching the Sizes of X and Type

      This function can generate unexpected data if x and type are not the same size. If x
      requires more bits of storage than type, this function uses the upper bytes of x and
      discards the remaining lower bytes. If x is of a smaller data type than type, this
      function moves the data in x to the upper bytes of type and fills the remaining bytes
     with zeros. For example, an 8-bit unsigned integer with value 1 type cast to a 16-bit
     unsigned integer results in a value of 256.

    Type Casting Arrays

     You can use this function with an array of scalars or an array of clusters of scalars. For
     example, if you typecast an array of four 16-bit integers to an array of 32-bit integers,
     the output array contains two elements, each formed from the bits of pairs of elements
     from the input array. If the input array does not contain enough bytes to form a whole
    number of output elements, LabVIEW omits the final elements of the input array.


552   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:552 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:553 ordinal=553 -->
## Functions

Functions

Type Casting References

If you want to upcast or downcast references, use the To More Generic Class function
and the To More Specific Class function instead of the Type Cast function. The Type
Cast function does not provide error checking, but the To More Generic Class function
and the To More Specific Class function do. The To More Specific Class function has
error in and error out parameters. The To More Generic Class function breaks the wire
at edit time when you wire a reference to an incompatible target class.

Type Casting Boolean Data from Early Versions of LabVIEW

If x might contain Boolean data created with LabVIEW 4.xor earlier, right-click this
function and select Convert 4.x Data from the shortcut menu to convert the data to a
format that is readable by LabVIEW 5.0 and later. In Convert 4.x Data mode, this
function interprets x as if the data is stored in LabVIEW 4.xdata storage layout and
displays the icon for this function with a red 4.x on it. LabVIEW 4.xand earlier stores
Boolean data in two bytes unless the data is in an array, in which case LabVIEW stores
each Boolean element in a single bit. LabVIEW 5.0 and later stores Boolean values in a
single byte, regardless of whether it is in an array. National Instruments recommends
reworking any application that uses the Convert 4.x Data mode as a long term
solution.

FlattenFlatten ToTo StringString FunctionFunction

Converts the anything input to a flattened data string of binary values. You also can
use this function to convert the byte order, or endian format, of the data in the
flattened data string.


Inputs/Outputs

   •      anything —


                                                    © National Instruments 553

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:553 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:554 ordinal=554 -->
## Functions

Functions


          anything contains the data you want to convert to a UTF-8 JSON string. This input accepts arrays
         and clusters of Booleans, floating-point numbers, and strings. anything can also accept an array
           of clusters, or a cluster of arrays, of these data types. This input does not support other data
           types, such as enums, refnums, file paths, and fixed-point numbers.

           Cluster elements may be named or unnamed, but not a combination of both. If cluster elements
           are named, then each name must be unique to that cluster. If you wire an unsupported data
           type, LabVIEW breaks the VI.

            •      prepend array or string size? (T) —

         prepend array or string size? specifies whether LabVIEW includes data size information at the
          beginning of data string when anything is an array or string. If prepend array or string size? is
          FALSE, LabVIEW does not include the size information. The default is TRUE.

         The string created by the Flatten To String function is a LabVIEW string. If prepend array or
           string size? is TRUE, the LabVIEW string has a 4-byte (I32) number at the beginning of the string
           that tells how long the string is. This enables a LabVIEW string to include NULL characters [ASCII
           character zero (0)]. If you pass a LabVIEW string to external code and use it as a C string, NULL
           characters embedded in the string may cause problems, since C strings are interpreted as
           terminating at the first NULL character. prepend array or string size? only controls the top-level
          data size information. Arrays and strings in hierarchical data types such as clusters always
           include size information.

            •      byte order (0:big-endian, network order) —

          byte order sets the endian format of the data in the resulting flattened string. Byte order, or
          endian form, indicates whether integers are represented in memory from most significant byte
           to least significant byte or vice versa.

            big-endian, network order (default)—The most significant byte occupies the lowest memory
          0
            address.
          1 native, host order—Uses the byte-ordering format of the host computer.
          2 little-endian—The least significant byte occupies the lowest memory address.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •      data string —


554   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:554 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:555 ordinal=555 -->
## Functions

Functions


    data string is the flattened data generated by the function.

    data string might contain header information before each non-scalar component describing its
     size. Such a string can be stored in a file or sent over a network. If you send the string over a
    network, the receiver must be able to interpret it. Usually, LabVIEW stores data as
    noncontiguous, indirectly referenced pieces. This function copies the data in LabVIEW form into
    a contiguous buffer data string. Use the Unflatten From String function to convert a data string
    back to any data type.

   •      type string (7.x only) —

    type string (7.x only) is visible only if the terminal is already wired from a previous version of
    LabVIEW or if you right-click the function and select Convert 7.x Data from the shortcut menu.
    type string (7.x only) is an encoded binary description of data string. type string (7.x only) is
    not the same as the type input in the Unflatten From String function.

       If type string (7.x only) cannot represent the data type wired to anything, this function returns
    an error.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Use the Type Cast function for conversion of data types that does not result in
flattened data.

If you need to flatten type descriptor data to a string that is readable by LabVIEW 7.xor
earlier, right-click this function and select Convert 7.x Data from the shortcut menu. In
Convert 7.x Data mode, this function shows the type string (7.x only) output and
displays the icon for this function with a red 7.x on it. LabVIEW 7.xand earlier stores
type descriptors in 16-bit flat representation. LabVIEW 8.0 and later stores type
descriptors in 32-bit flat representation. National Instruments recommends reworking
any application that uses the Convert 7.x Data mode as a long term solution.

If you need to flatten Boolean data to a string that is readable by LabVIEW 4.xor
earlier, right-click this function and select Convert 4.x Data from the shortcut menu.
The Convert 4.x Data shortcut menu item is visible only if you wire Boolean data to
anything. In Convert 4.x Data mode, this function writes the data in LabVIEW 4.xdata
storage layout and displays the icon for this function with a red 4.x on it. LabVIEW 4.x

                                                    © National Instruments 555

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:555 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:556 ordinal=556 -->
## Functions

Functions

     and earlier stores Boolean data in two bytes unless the data is in an array, in which
     case LabVIEW stores each Boolean element in a single bit. LabVIEW 5.0 and later stores
     Boolean values in a single byte, regardless of whether it is in an array. National
     Instruments recommends reworking any application that uses the Convert 4.x Data
    mode as a long term solution.

         If you use this function to flatten variant data, LabVIEW flattens the variant and all its
      contents, including attributes. However, if you use the Variant To Flattened String
      function, LabVIEW flattens only the variant and discards any attributes.

         If you use this function to flatten data from a custom control or indicator that you
     saved as a type definition, the function strips the type definition of its type definition
     wrapper. If you do not want to strip this wrapper, right-click the function and select
     Expose Typedefs from the shortcut menu. The Expose Typedefs shortcut menu item is
      visible only if you wire data to type string (7.x only).

     UnflattenUnflatten FromFrom StringString FunctionFunction

     Converts binary string to the type wired to type. binary string should contain
      flattened data of the type wired to type. You also can use this function to specify the
     byte order, or endian format, of the data in the binary string.


     Inputs/Outputs

            •      type —

          type is a normally constructed LabVIEW type.

          type is not the type string output in the Flatten To String function.

            •      binary string —

          binary string is a flattened string that is typically generated by the Flatten To String function.


556   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:556 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:557 ordinal=557 -->
## Functions

Functions


   If data includes array or string size? is TRUE, binary string contains header information
  describing its size.

•      data includes array or string size? (T) —

  data includes array or string size? indicates whether LabVIEW reads data size information from
  the beginning of an incoming array or string. If data includes array or string size? is TRUE,
  LabVIEW reads the size information from the beginning of binary string. If data includes array or
  string size? is FALSE, LabVIEW detects the size information from the memory size of binary
  string.

  The default is TRUE. data includes array or string size? only accesses the top-level data size
  information. Arrays and strings in hierarchical data types such as clusters always include size
  information.

•      byte order (0:big-endian, network order) —

  byte order indicates the endian format of the data in the incoming flattened string. Byte order,
  or endian form, indicates whether integers are represented in memory from most-significant
  byte to least-significant byte or vice versa.

   big-endian, network order (default)—The most-significant byte occupies the lowest memory  0    address.
  1 native, host order—Uses the byte-ordering format of the host computer.
  2 little-endian—The least-significant byte occupies the lowest memory address.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•       rest of the binary string —

  rest of the binary string contains any leftover bytes that this function did not convert. This
  function does not convert all the bytes if the size of binary string is not a multiple of the size of
  type.

•      value —

  value returns binary string as unflattened data of the same data type and structure as type.

•       error out —


                                                   © National Instruments 557

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:557 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:558 ordinal=558 -->
## Functions

Functions


           error out contains error information. This output provides standard error out functionality.


     Use the Type Cast function for conversion of data types that does not require already-
      flattened data.

         If you need to unflatten data from a string created by LabVIEW 4.xor earlier, right-click
      this function and select Convert 4.x Data from the shortcut menu. In Convert 4.x Data
     mode, this function interprets the data in LabVIEW 4.xdata storage layout and displays
     the icon for this function with a red 4.x on it. LabVIEW 4.xand earlier stores Boolean
     data in two bytes unless the data is in an array, in which case LabVIEW stores each
     Boolean element in a single bit. LabVIEW 5.0 and later stores Boolean values in a single
      byte, regardless of whether it is in an array. National Instruments recommends
     reworking any application that uses the Convert 4.x Data mode as a long term
      solution.

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\File IO\Binary\Endian Considerations\
       Endian Considerations with Binary Files.vi
          • labview\examples\Strings\Unflatten from String with
       Little-Endian Data.vi

     MantissaMantissa && ExponentExponent FunctionFunction

     Returns the mantissa and exponent of the input numeric value such that number =
     mantissa * 2^exponent.

         If number is 0, both mantissa and exponent are 0. Otherwise, the absolute value of
     mantissa is greater than or equal to 1 and less than 2, and the value of exponent is an
      integer. The connector pane displays the default data types for this polymorphic
      function.


558   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:558 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:559 ordinal=559 -->
## Functions

Functions


Inputs/Outputs

   •     number —

   number can be any decimal representation.

   •      mantissa —

    mantissa has the same decimal representation as number.

   •      exponent —

    exponent has the same decimal representation as number.


RotateRotate LeftLeft WithWith CarryCarry FunctionFunction

Rotates each bit in the input value one bit to the left (from least significant to most
significant bit), inserts carry in the low-order bit, and returns the most significant bit.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      carry —

    carry is the new low-order bit of value.

   •      value —

    value must be an integer. It cannot be an array or a cluster.

   •     msb carry out —

   msb carry out is the former high-order bit of value.

   •      value —

                                                    © National Instruments 559

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:559 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:560 ordinal=560 -->
## Functions

Functions


          value is the new value.

         The data type of the output value is determined by the data type of the input value.

     RotateRotate RightRight WithWith CarryCarry FunctionFunction

     Rotates each bit in value one bit to the right (from most significant to least significant),
      inserts carry in the high-order bit, and returns the least significant bit.

     The connector pane displays the default data types for this polymorphic function.


     Inputs/Outputs

            •      carry —

           carry is the new high-order bit of value.

            •      value —

          value must be an integer. It cannot be an array or a cluster.

            •       lsb carry out —

           lsb carry out is the former low-order bit of value.

            •      value —

          value is the new value.

         The data type of the output value is determined by the data type of the input value.

     LogicalLogical ShiftShift FunctionFunction

      Shifts x the number of bits specified by y.

     The connector pane displays the default data types for this polymorphic function.


560   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:560 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:561 ordinal=561 -->
## Functions

Functions


Inputs/Outputs

   •      y —

    y can be any numeric representation. If y is greater than 0, the function shifts x left y bits (from
     least significant to most significant bit) and inserts zeros in the low-order bits. If y is less than 0,
    the function shifts x right y bits in the positive direction (from most significant to least significant
     bit) and inserts zeros in the high-order bits.

   •      x —

    x can be any integer representation. If x is an 8-, 16-, 32-, or 64-bit integer and y is greater than 8,
     16, or 32, or 64 or is less than –8, –16, –32, or –64, respectively, the output value is all zeros.

   •      x << y —

    x << y is the result of the shift and has the same numeric representation as x.


RotateRotate FunctionFunction

Rotates x the number of bits specified by y.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      y —

    y specifies the number of bits in x that the function rotates.

       If y is greater than 0, the function shifts the first y bits at the left end of x to the right end. If y is
     less than 0, the function shifts the first y bits at the right end of x to the left end.
   •      x —


                                                    © National Instruments 561

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:561 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:562 ordinal=562 -->
## Functions

Functions


                 If x is an 8-, 16-, 32-, or 64-bit integer, then for any value of y, y ± 8, y ± 16, y ± 32, or y ± 64 yields
          the same output value, respectively, as y.

          For example, if x is an 8-bit integer, y = 1 and y = 9 yield the same result.
            •      x rotated left by y —

          x rotated left by y is the result of the rotation.

         The data type of x rotated left by y is determined by the data type of the x input.

     The following table illustrates how x and y affect x rotated left by y:


                      x rotated left by
      y  x                     Comments                     y

          3                             This function shifts the first one bit on the left, 0, to the right      1             6 (00000110)           (00000011)                  end.

          3                             This function shifts the first two bits on the left, 00, to the right      2             12 (00001100)           (00000011)                  end.

          3                             This function shifts the first three bits on the right, 011, to the       –3            96 (01100000)           (00000011)                         left end.

      SplitSplit NumberNumber FunctionFunction

     Breaks a number into its component bytes or words.


     Inputs/Outputs

            •      x —

          x can be an 8-, 16-, 32-, or 64-bit integer, or an array or cluster of those representations.

            •       hi(x) —

            hi(x) and lo(x) are integers that are half the width of x. hi(x) and lo(x) are 8-bit, 16-bit, or 32-bit


562   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:562 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:563 ordinal=563 -->
## Functions

Functions


    unsigned integers, respectively, or an array or cluster of those representations. hi(x) is the
    numerically high-order byte and lo(x) is the numerically low-order byte, regardless of the
    endianness of the operating system.

   •       lo(x) —


If you wire an 8-bit integer input, this function does not split the number. Instead,
LabVIEW returns the same 8-bit number in the lo(x) output, and returns zero for the
hi(x) output.
JoinJoin NumbersNumbers FunctionFunction

Creates a number from the component bytes or words.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •       hi —

     hi can be an 8-, 16-, or 32-bit number or an array or cluster of that representation.

   •       lo —

     lo can be an 8-, 16-, or 32-bit number or an array or cluster of that representation.

   •        (hi.lo) —

     (hi.lo) is an integer twice the width of hi and lo. (hi.lo) is a 16-, 32-, or 64-bit unsigned integer or
    an array or cluster of those representations. If hi and lo are of different widths, (hi.lo) is twice the
    width of the widest number.


SwapSwap BytesBytes FunctionFunction

Swaps the high-order 8 bits and the low-order 8 bits for every word in data.

                                                    © National Instruments 563

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:563 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:564 ordinal=564 -->
## Functions

Functions

         If you want to byte-swap floating-point or fixed-point numbers, use the Type Cast
      function to cast the value to a 1D array of bytes by wiring an array of numeric controls
      to the type input and the floating-point or fixed-point numbers to the x input. Then
     use the Reverse 1D Array function to convert the array to a floating-point number with
     the elements reversed. The connector pane displays the default data types for this
     polymorphic function.


     Inputs/Outputs

            •      data —

          data is an integer, an array of integers, or a cluster containing integers that you want to byte
          swap. If data is a cluster that contains integers, this function swaps only the integer elements of
          the cluster. Neither refnums or variants are valid inputs. Both will break the input wire.

            •      byte swapped —

          byte swapped is of the same data type and structure as data.


    SwapSwap WordsWords FunctionFunction

    Swaps the high-order 16 bits and the low-order 16 bits for every long integer in data.

     For example, if the input in hexadecimal format is 1234567890ABCDEF, this
      function swaps 1234 with 5678 and 90AB with CDEF, returning
    56781234CDEF90AB. The connector pane displays the default data types for this
     polymorphic function.


     Inputs/Outputs

            •      data —


564   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:564 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:565 ordinal=565 -->
## Functions

Functions


    data is an integer, an array of integers, or a cluster containing integers that you want to word
    swap. In the case of a cluster that contains integers, this function swaps only the integer
    elements of the cluster.

       If you want to byte-swap floating-point or fixed-point numbers, use the Type Cast function to
     cast the value to a 1D array of bytes. Then use the Reverse 1D Array function and type cast it back
    to a floating-point or fixed-point number. Neither refnums or variants are valid inputs. Both will
    break the input wire.
   •     word swapped —

   word swapped is of the same data type and structure as data.


ByteByte ArrayArray ChecksumChecksum

Computes the message digest on a byte array. You must manually select the
polymorphic instance you want to use.


  • SHA-256 Byte Array Checksum VI
  • SHA-224 Byte Array Checksum VI
  • SHA-384 Byte Array Checksum VI
  • SHA-512 Byte Array Checksum VI
  • SHA-512-256 Byte Array Checksum VI
  • SHA-512-224 Byte Array Checksum VI
  • SHA3-224 Byte Array Checksum VI
  • SHA3-256 Byte Array Checksum VI
  • SHA3-384 Byte Array Checksum VI
  • SHA3-512 Byte Array Checksum VI
SHA-256SHA-256 ByteByte ArrayArray ChecksumChecksum VIVI

Computes the message digest on a byte array. You must manually select the
polymorphic instance you want to use.


                                                    © National Instruments 565

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:565 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:566 ordinal=566 -->
## Functions

Functions


     Inputs/Outputs

            •       buffer —

           buffer specifies the byte array, or buffer, for which you want to compute the message digest.

            •       digest —

           digest returns the SHA-256 message digest of the byte array, or buffer, as a hexadecimal string.

  SHA-224SHA-224 ByteByte ArrayArray ChecksumChecksum VIVI

     Computes the message digest on a byte array. You must manually select the
     polymorphic instance you want to use.


     Inputs/Outputs

            •       buffer —

           buffer specifies the byte array, or buffer, for which you want to compute the message digest.

            •       digest —

           digest returns the SHA-224 message digest of the byte array, or buffer, as a hexadecimal string.

  SHA-384SHA-384 ByteByte ArrayArray ChecksumChecksum VIVI

     Computes the message digest on a byte array. You must manually select the
     polymorphic instance you want to use.


566   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:566 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:567 ordinal=567 -->
## Functions

Functions


Inputs/Outputs

   •       buffer —

    buffer specifies the byte array, or buffer, for which you want to compute the message digest.

   •       digest —

    digest returns the SHA-384 message digest of the byte array, or buffer, as a hexadecimal string.

SHA-512SHA-512 ByteByte ArrayArray ChecksumChecksum VIVI

Computes the message digest on a byte array. You must manually select the
polymorphic instance you want to use.


Inputs/Outputs

   •       buffer —

    buffer specifies the byte array, or buffer, for which you want to compute the message digest.

   •       digest —

    digest returns the SHA-512 message digest of the byte array, or buffer, as a hexadecimal string.

SHA-512-256SHA-512-256 ByteByte ArrayArray ChecksumChecksum VIVI

Computes the message digest on a byte array. You must manually select the
polymorphic instance you want to use.


                                                    © National Instruments 567

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:567 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:568 ordinal=568 -->
## Functions

Functions


     Inputs/Outputs

            •       buffer —

           buffer specifies the byte array, or buffer, for which you want to compute the message digest.

            •       digest —

           digest returns the SHA-512/256 message digest of the byte array, or buffer, as a hexadecimal
             string.

   SHA-512-224SHA-512-224 ByteByte ArrayArray ChecksumChecksum VIVI

     Computes the message digest on a byte array. You must manually select the
     polymorphic instance you want to use.


     Inputs/Outputs

            •       buffer —

           buffer specifies the byte array, or buffer, for which you want to compute the message digest.

            •       digest —

           digest returns the SHA-512/224 message digest of the byte array, or buffer, as a hexadecimal
             string.

   SHA3-224SHA3-224 ByteByte ArrayArray ChecksumChecksum VIVI

     Computes the message digest on a byte array. You must manually select the

568   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:568 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:569 ordinal=569 -->
## Functions

Functions

polymorphic instance you want to use.


Inputs/Outputs

   •       buffer —

    buffer specifies the byte array, or buffer, for which you want to compute the message digest.

   •       digest —

    digest returns the SHA3-224 message digest of the byte array, or buffer, as a hexadecimal string.

SHA3-256SHA3-256 ByteByte ArrayArray ChecksumChecksum VIVI

Computes the message digest on a byte array. You must manually select the
polymorphic instance you want to use.


Inputs/Outputs

   •       buffer —

    buffer specifies the byte array, or buffer, for which you want to compute the message digest.

   •       digest —

    digest returns the SHA3-256 message digest of the byte array, or buffer, as a hexadecimal string.

SHA3-384SHA3-384 ByteByte ArrayArray ChecksumChecksum VIVI

Computes the message digest on a byte array. You must manually select the

                                                    © National Instruments 569

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:569 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:570 ordinal=570 -->
## Functions

Functions

     polymorphic instance you want to use.


     Inputs/Outputs

            •       buffer —

           buffer specifies the byte array, or buffer, for which you want to compute the message digest.

            •       digest —

           digest returns the SHA3-384 message digest of the byte array, or buffer, as a hexadecimal string.

   SHA3-512SHA3-512 ByteByte ArrayArray ChecksumChecksum VIVI

     Computes the message digest on a byte array. You must manually select the
     polymorphic instance you want to use.


     Inputs/Outputs

            •       buffer —

           buffer specifies the byte array, or buffer, for which you want to compute the message digest.

            •       digest —

           digest returns the SHA3-512 message digest of the byte array, or buffer, as a hexadecimal string.

    AbsoluteAbsolute ValueValue FunctionFunction

     Returns the absolute value of the input.


570   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:570 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:571 ordinal=571 -->
## Functions

Functions

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x can be a scalar number, a fixed-point number, an array or cluster of numbers, an array of
     clusters of numbers, and so on.

    x cannot be an unsigned integer, because unsigned integers represent only non-negative
     integers.

   •       abs(x) —

    abs(x) is the absolute value of x.

   When x is of the form x = a + bi, that is, when x is complex, the following equation defines abs(x):


When you wire matrix data as an input to this function, a VI that includes subVIs that
work with the matrix data type replaces the function. The resulting VI has the same
icon but contains a matrix-specific algorithm. The node remains a VI if you disconnect
the matrix from the inputs. Wire other data types as inputs to restore the original
function. If you wire a data type to a function and that data type causes a basic math
operation to fail, the function returns a NaN.

If the absolute value of x is outside the range of the data type of x, abs(x) overflows to
a value within the range of the data type. For example, if x is an 8-bit integer and the
value of x is -128, abs(x) returns -128 since 128 is outside the range of 8-bit integers,
-128 to 127.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Numerics\Numeric Functions.vi

                                                    © National Instruments 571

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:571 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:572 ordinal=572 -->
## Functions

Functions

    RoundRound ToTo NearestNearest FunctionFunction

     Rounds the input to the nearest integer. If the value of the input is midway between
     two integers, the function returns the nearest even integer.

     For example, if number is 1.5 or 2.5, nearest integer value is 2.

          Note Note IEEE standards determine the rounding method for this function.
             This method produces more accurate values with no positive or negative bias
            because it does not round all integers in the same direction.

     The connector pane displays the default data types for this polymorphic function.


     Inputs/Outputs

            •     number —

        number can be a scalar number, array or cluster of numbers, array of clusters of numbers, and
          so on.

            •      nearest integer value —

          nearest integer value is the resulting nearest integer to number. If the input is a time stamp
           value, the function rounds to the nearest second.

        When number is in the form of a + bi, that is, when number is complex, the function returns a
         complex number defined by the nearest integer to the real and imaginary parts of number. The
           following equation defines nearest integer value: nearest integer value(x) = nearest integer
           value(a) + i* nearest integer value(b)

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Numerics\Numeric Functions.vi


572   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:572 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:573 ordinal=573 -->
## Functions

Functions

RoundRound TowardToward -Infinity-Infinity FunctionFunction

Truncates the input to the next lowest integer.

For example, if the input is 3.8, the result is 3. If the input is –3.8, the result is –4. The
connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •       floor(x): largest int <= x —

     floor(x): largest int ≤ x is the resulting lowest integer, closest to x. If the input is a time stamp
     value, the function rounds to the previous second.

   When x is of the form x = a + bi, that is, when x is complex, the function returns a complex
   number defined by the next lowest integers to the real and imaginary parts of x. The following
    equation defines floor(x): largest int ≤ x: floor(x) = floor(a) + ifloor(b)

RoundRound TowardToward +Infinity+Infinity FunctionFunction

Rounds the input to the next highest integer.

For example, if the input is 3.1, the result is 4. If the input is –3.1, the result is –3. The
connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —


                                                    © National Instruments 573

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:573 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:574 ordinal=574 -->
## Functions

Functions


          x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

            •        ceil(x): smallest int >= x —

             ceil(x): smallest int >= x is the resulting highest integer, closest to x. If the input is a time stamp
           value, the function rounds to the next second.

        When x is of the form x = a + bi, that is, when x is complex, the function returns a complex
         number defined by the next highest integers to the real and imaginary parts of x. The following
          equation defines ceil(x): smallest int >= x: ceil(x) = ceil(a) + iceil(b)

    ScaleScale ByBy PowerPower OfOf 22 FunctionFunction

      Multiplies x by 2 raised to the power of n.

         If x is an integer or fixed-point number, this function is the equivalent of an arithmetic
       shift. The connector pane displays the default data types for this polymorphic
      function.


     Inputs/Outputs

            •     n —

        n can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

                 If n is a floating-point number, this function rounds n before it scales x (0.5 rounds to 0; 0.51
          rounds to 1). If n is a 64-bit integer, LabVIEW coerces n to a 32-bit integer.
            •      x —

          x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

            •      x*2^n —

          x*2^n is the result of multiplying x by 2, raised to the power of n.


         If you wire a fixed-point value to this function, the resulting output value retains the

574   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:574 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:575 ordinal=575 -->
## Functions

Functions

fixed-point configuration settings of the input value. However, the value is likely to
truncate or wrap.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Numerics\Numeric Functions.vi

ComplexComplex

Use the Complex functions to create complex numbers from two values given in
rectangular or polar and to break a complex number into its rectangular or polar
components.


 Palette Object           Description

 Complex Conjugate
                       Produces the complex conjugate of x + iy. Function

 Polar To Complex
                         Creates a complex number from two values in polar notation. Function

 Complex To Polar
                        Breaks a complex number into its polar components. Function

 Re/Im To Complex
                         Creates a complex number from two values in rectangular notation.
 Function

 Complex To Re/Im
                        Breaks a complex number into its rectangular components.
 Function

                        Converts the rectangular components of a complex number into its polar
 Re/Im To Polar Function
                      components.

                        Converts the polar components of a complex number into its rectangular
 Polar To Re/Im Function
                      components.


                                                    © National Instruments 575

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:575 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:576 ordinal=576 -->
## Functions

Functions

    ComplexComplex ConjugateConjugate FunctionFunction

     Produces the complex conjugate of x + iy.

     The connector pane displays the default data types for this polymorphic function.


     Inputs/Outputs

            •      x + iy —

          x + iy can be a complex number, array or cluster of complex numbers, an array of cluster of
         complex numbers, and so on.

            •      x - iy —

          x - iy is the complex conjugate of x + iy.


     PolarPolar ToTo ComplexComplex FunctionFunction

     Creates a complex number from two values in polar notation.

     The dimensions of two matrices that you want to combine must be the same.
     Otherwise, this function returns an empty complex matrix. The connector pane
      displays the default data types for this polymorphic function.


     Inputs/Outputs

            •        r —

             r can be a scalar number, an array or cluster of numbers, array of clusters of numbers, and so on.

            •      theta —


576   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:576 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:577 ordinal=577 -->
## Functions

Functions


    theta can be a scalar number, an array or cluster of numbers, array of clusters of numbers, and
    so on. theta is in radians.

   •        r * e^(i*theta) —

     r * e^(i*theta) is of the same data type structure as r and theta, with complex representation
    instead of scalar.


Given z in rectangular form z = a + bi, this function converts the polar components
according to the following equation:

z = r*cos(theta) + ir*sin(theta)

When you wire matrix data as an input to this function, a VI that includes subVIs that
work with the matrix data type replaces the function. The resulting VI has the same
icon but contains a matrix-specific algorithm. The node remains a VI if you disconnect
the matrix from the input(s). Wire other data types as inputs to restore the original
function. If you wire a data type to a function and that data type causes a basic math
operation to fail, the function returns an empty matrix or NaN.

ComplexComplex ToTo PolarPolar FunctionFunction

Breaks a complex number into its polar components.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •        r * e^(i*theta) —

     r * e^(i*theta) can be a complex number, a cluster of complex numbers, an array of complex
    numbers, an array of clusters of complex numbers, and so on.

   •        r —


                                                    © National Instruments 577

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:577 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:578 ordinal=578 -->
## Functions

Functions


             r is of the same data type structure as r * e^(i*theta), with scalar representation instead of
          complex.

            •      theta —

          theta is of the same data type structure as r * e^(i*theta), with scalar representation instead of
          complex. theta is in radians.


     Given z in rectangular form z = a + bi, this function converts the polar components of z
     = r * e^(i*theta) according to the following equations:

       r = |z| = sqrt(a² + b²) theta = arg(z) = arctan2(b,a)

    When you wire matrix data as an input to this function, a VI that includes subVIs that
     work with the matrix data type replaces the function. The resulting VI has the same
     icon but contains a matrix-specific algorithm. The node remains a VI if you disconnect
     the matrix from the input(s). Wire other data types as inputs to restore the original
      function. If you wire a data type to a function and that data type causes a basic math
     operation to fail, the function returns an empty matrix or NaN.

    Re/ImRe/Im ToTo ComplexComplex FunctionFunction

     Creates a complex number from two values in rectangular notation.

     The dimensions of two matrices that you want to combine must be the same.
     Otherwise, this function returns an empty complex matrix. The connector pane
      displays the default data types for this polymorphic function.


     Inputs/Outputs

            •      x —

          x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

            •      y —

578   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:578 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:579 ordinal=579 -->
## Functions

Functions


    y can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •      x + iy —

    x + iy has the same structure as the input, with complex representation instead of scalar.


When you wire matrix data as an input to this function, a VI that includes subVIs that
work with the matrix data type replaces the function. The resulting VI has the same
icon but contains a matrix-specific algorithm. The node remains a VI if you disconnect
the matrix from the input(s). Wire other data types as inputs to restore the original
function. If you wire a data type to a function and that data type causes a basic math
operation to fail, the function returns an empty matrix or NaN.

ComplexComplex ToTo Re/ImRe/Im FunctionFunction

Breaks a complex number into its rectangular components.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x + iy —

    x + iy can be a complex number, array or cluster of complex numbers, an array of cluster of
    complex numbers, and so on.

   •      x —

    x is of the same data type structure as x + iy, with scalar representation instead of complex.

   •      y —

    y is of the same data type structure as x + iy, with scalar representation instead of complex.


When you wire matrix data as an input to this function, a VI that includes subVIs that

                                                    © National Instruments 579

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:579 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:580 ordinal=580 -->
## Functions

Functions

     work with the matrix data type replaces the function. The resulting VI has the same
     icon but contains a matrix-specific algorithm. The node remains a VI if you disconnect
     the matrix from the input(s). Wire other data types as inputs to restore the original
      function. If you wire a data type to a function and that data type causes a basic math
     operation to fail, the function returns an empty matrix or NaN.

    Re/ImRe/Im ToTo PolarPolar FunctionFunction

     Converts the rectangular components of a complex number into its polar components.

     The connector pane displays the default data types for this polymorphic function.


     Inputs/Outputs

            •      x —

          x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

            •      y —

          y can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

            •        r —

             r is of the same data type structure as x and y.

            •      theta —

          theta is of the same data type structure as x and y. theta is in radians.


      This function converts the rectangular components to polar components using the
      following equations:

       r = sqrt(x² + y²) theta = arctan2(y,x) radians


580   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:580 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:581 ordinal=581 -->
## Functions

Functions

PolarPolar ToTo Re/ImRe/Im FunctionFunction

Converts the polar components of a complex number into its rectangular components.


Inputs/Outputs

   •        r —

     r can be a scalar number, an array or cluster of numbers, array of clusters of numbers, and so on.

   •      theta —

    theta can be a scalar number, an array or cluster of numbers, array of clusters of numbers, and
    so on. theta is in radians.

   •      x —

    x is of the same data structure as r and theta.

   •      y —

    y is of the same data structure as r and theta.


This function converts the polar components to rectangular components using
following equations:

x = r*cos(theta) y = r*sin(theta)
SquareSquare RootRoot FunctionFunction

Computes the square root of the input value.

If x is negative, the square root is NaN unless x is complex. If x is a matrix, this function
takes the matrix square root of x. The connector pane displays the default data types
for this polymorphic function.


                                                    © National Instruments 581

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:581 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:582 ordinal=582 -->
## Functions

Functions

          Note If you wire a value that has a unit with an odd exponent to the square
             root function, the wire breaks because LabVIEW does not support units with
               fractional exponents. For example, 15m² is an acceptable input value, but
          15m3 is not an acceptable input value.


     Inputs/Outputs

            •      x —

          x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

            •       sqrt(x) —

            sqrt(x) is a double-precision, floating-point number if x is an integer.

                 If x is less than 0, sqrt(x) is not a number (NaN), unless x is complex. When x is of the form x = a +
             bi, that is, when x is complex, the function defines the magnitude and phase with the following
           equations:                            where |x| is the magnitude of x and arg(x) is the

         phase of x:              arg(x) = arctan2(b,a)

              Note You can manually configure this function to output data of a type you want. To
                     specify the output data type, right-click the function and select Properties to display
                   the Object Properties dialog box. On the Output Configuration page, click the
                  Representation icon and select the data type you want. A blue coercion dot appears
                on the output terminal of the function to indicate that you have configured the
                  output data type.


    When you wire matrix data as an input to this function, a VI that includes subVIs that
     work with the matrix data type replaces the function. The resulting VI has the same
     icon but contains a matrix-specific algorithm. The node remains a VI if you disconnect
     the matrix from the input(s). Wire other data types as inputs to restore the original
      function. If you wire a data type to a function and that data type causes a basic math
     operation to fail, the function returns an empty matrix or NaN.


582   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:582 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:583 ordinal=583 -->
## Functions

Functions

Refer to the Matrix Square Root VI for more information.

Fixed-Point Details

If you wire a signed fixed-point value to this function, the function converts the signed
number into a floating-point number and performs the square root operation. By
default, LabVIEW configures the integer word length of the square root to avoid
overflow. However, because the precision of the square root can be infinite, rounding
conditions always occur. Use the Numeric Node Properties dialog box to configure
how LabVIEW handles overflow and rounding of fixed-point data.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Numerics\Numeric Functions.vi

SquareSquare FunctionFunction

Computes the square of the input value.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •      x^2 —

    x^2 is of the same numeric representation as x.

          Note You can manually configure this function to output data of a type you want. To
              specify the output data type, right-click the function and select Properties to display


                                                    © National Instruments 583

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:583 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:584 ordinal=584 -->
## Functions

Functions


                   the Object Properties dialog box. On the Output Configuration page, click the
                  Representation icon and select the data type you want. A blue coercion dot appears
                on the output terminal of the function to indicate that you have configured the
                  output data type.


         If you wire fixed-point values to Numeric functions such as Add, Subtract, Multiply, and
     Square, the functions usually return values that do not lose any bits of word length.
     However, if the operation creates a value that exceeds the maximum word length that
     LabVIEW accepts, overflow or rounding conditions can occur. LabVIEW accepts a
    maximum word length of 64 bits. Use the Numeric Node Properties dialog box to
      configure how LabVIEW handles overflow or rounding of fixed-point data.

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Numerics\Numeric Functions.vi

    NegateNegate FunctionFunction

     Negates the input value.

     The connector pane displays the default data types for this polymorphic function.


     Inputs/Outputs

            •      x —

          x can be a scalar number, a fixed-point number, an array or cluster of numbers, an array of
            clusters of numbers, and so on. x cannot be an unsigned integer, because unsigned integers
           represent only non-negative integers.

            •       -x —


584   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:584 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:585 ordinal=585 -->
## Functions

Functions


     -x is the negative value of x.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Numerics\Numeric Functions.vi

ReciprocalReciprocal FunctionFunction

Divides 1 by the input value.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •      1/x —

    1/x is infinity if x is 0. If x is an integer, 1/x is a double-precision, floating-point number.


Fixed-Point Details

If you wire a fixed-point value to this function, by default LabVIEW configures the
integer word length of the reciprocal to avoid overflow. However, because the
precision of the reciprocal can be infinite, rounding conditions always occur. Use the
Numeric Node Properties dialog box to configure how LabVIEW handles rounding of
fixed-point data. This function always uses the Saturate overflow mode to handle
overflow.


                                                    © National Instruments 585

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:585 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:586 ordinal=586 -->
## Functions

Functions

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Numerics\Numeric Functions.vi

    SignSign FunctionFunction

     Returns the sign of number.

          Note For nonzero complex numbers, this function returns a complex value
             with the same phase as the input and with a magnitude of 1.

     Text-based programming languages typically call this function signum or sgn. The
     connector pane displays the default data types for this polymorphic function.


     Inputs/Outputs

            •     number —

        number can be a scalar number, array or cluster of numbers, array of clusters of numbers, and
          so on.

            •        -1, 0, 1 —

           –1, 0, 1 returns 1 if the input value is greater than 0, returns 0 if the input value is equal to 0, and
           returns –1 if the input value is less than 0.

        When number is in the form of a + bi, that is, when number is complex, the following defines -1,
            0, 1:

    Examples

      Refer to the following example files included with LabVIEW.


586   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:586 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:587 ordinal=587 -->
## Functions

Functions

  • labview\examples\Numerics\Numeric Functions.vi

ScalingScaling

Use the Scaling VIs to convert voltage readings to other temperature or strain units.


 Palette Object  Description

               Converts a voltage you read from an RTD into temperature in Celsius. Wire data to Convert RTD                the RTDvolts input to determine the polymorphic instance to use or manually Reading                  select the instance.


 Convert Strain  Converts a voltage read from a strain gauge to units of strain. Wire data to the Vsg
 Gauge         input to determine the polymorphic instance to use or manually select the
 Reading        instance.


               Converts a thermistor voltage into a temperature. This VI has different modes of Convert                operation for voltage-excited and current-excited thermistors. Wire data to the
 Thermistor                Voltage input to determine the polymorphic instance to use or manually select the Reading                 instance.


               Converts a voltage reading from a thermocouple into a temperature value. Wire
 Convert
               data to the Voltage Waveform (waveform), Voltage Array (array), or Thermocouple
 Thermocouple
                Voltage (scalar) input to determine the polymorphic instance to use or manually
 Reading
                  select the instance.


 Radians to
               Converts data from radians to degrees.
 Degrees

 Degrees to
               Converts data from degrees to radians.
 Radians


                                                    © National Instruments 587

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:587 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:588 ordinal=588 -->
## Functions

Functions


       Palette Object  Description

     RPM to
       Radians per    Converts data from revolutions per minute (RPM) to radians per second.
      Second

       Radians per
      Second to      Converts data from radians per second to revolutions per minute (RPM).
     RPM

     ConvertConvert RTDRTD ReadingReading

     Converts a voltage you read from an RTD into temperature in Celsius. Wire data to the
     RTDvolts input to determine the polymorphic instance to use or manually select the
      instance.


          • Convert RTD Reading (waveform) VI
          • Convert RTD Reading (scaler) VI
   ConvertConvert RTDRTD ReadingReading (waveform)(waveform) VIVI

     Converts a voltage you read from an RTD into temperature in Celsius. Wire data to the
     RTDvolts input to determine the polymorphic instance to use or manually select the
      instance.


     Inputs/Outputs

            •     Ro —


588   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:588 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:589 ordinal=589 -->
## Functions

Functions


   Ro is the RTD resistance at 0° C. The default is 100 Ω.

   •      RTDvolts —

    RTDvolts is the voltage you read from the RTD.

   •       Iex —

     Iex is the excitation current you used with the RTD. This parameter defaults to an excitation
    current of 0.15 mA.

   •     A —

   A is a coefficient of the Callendar Van-Dusen equation that fits your RTD. The default coefficients
    are those for the European curve (also called the DIN 43760 standard).

   •     B —

   B is a coefficient of the Callendar Van-Dusen equation that fits your RTD. The default coefficients
     of this equation are those for the European curve (also called the DIN 43760 standard).

   •     RTDtemp —

   RTDtemp is the return temperature value in degrees Celsius.

ConvertConvert RTDRTD ReadingReading (scaler)(scaler) VIVI

Converts a voltage you read from an RTD into temperature in Celsius. Wire data to the
RTDvolts input to determine the polymorphic instance to use or manually select the
instance.


Inputs/Outputs

   •     Ro —

                                                    © National Instruments 589

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:589 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:590 ordinal=590 -->
## Functions

Functions


        Ro is the RTD resistance at 0° C. The default is 100 Ω.

            •      RTDvolts —

          RTDvolts is the voltage you read from the RTD.

            •       Iex —

           Iex is the excitation current you used with the RTD. This parameter defaults to an excitation
           current of 0.15 mA.

            •     A —

         A is a coefficient of the Callendar Van-Dusen equation that fits your RTD. The default coefficients
           are those for the European curve (also called the DIN 43760 standard).

            •     B —

        B is a coefficient of the Callendar Van-Dusen equation that fits your RTD. The default coefficients
           of this equation are those for the European curve (also called the DIN 43760 standard).

            •     RTDtemp —

        RTDtemp is the return temperature value in degrees Celsius.


     ConvertConvert StrainStrain GaugeGauge ReadingReading

     Converts a voltage read from a strain gauge to units of strain. Wire data to the Vsg
     input to determine the polymorphic instance to use or manually select the instance.


          • Convert Strain Gauge Reading (waveform) VI
          • Convert Strain Gauge Reading (scaler) VI

     The conversion formula the VI uses is based solely on the bridge configuration. The
      following illustrations show the seven bridge configurations you can use and the
     corresponding formulas. For all bridge configurations, the VI uses the following
     formula to obtain Vr.

590   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:590 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:591 ordinal=591 -->
## Functions

Functions

Vr= (Vsg – Vinit) / Vex

In the circuit diagrams, VOUT is the voltage you measure and pass to the conversion VI
as the Vsg. In the quarter-bridge and half-bridge configurations, R1 and R2 are dummy
resistors that are not directly incorporated into the conversion formula.

The following illustrations show the available bridge-completion networks.


                                                    © National Instruments 591

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:591 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:592 ordinal=592 -->
## Functions

Functions


592   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:592 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:593 ordinal=593 -->
## Functions

Functions

ConvertConvert StrainStrain GaugeGauge ReadingReading (waveform)(waveform) VIVI

Converts a voltage read from a strain gauge to units of strain. Wire data to the Vsg
input to determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     Rg (120) —

   Rg is the strain gauge nominal resistance value in ohms. The default is 120 Ω.

   •     GF (2.0) —

   GF is the gauge factor of the strain gauge.

   •      v (0.0) —

    v is Poisson's Ratio. This parameter is only required for certain bridge configurations.

   •      Vsg (0.0) —

    Vsg is the voltage you read from the strain gauge.

   •      Bridge Configuration (3:Half Bridge II) —

    Bridge Configuration indicates the type of bridge configuration in which the strain gauge is
    mounted. The default is Half Bridge II.

    This input accepts the following values.

    0    Qtr Bridge I
    1    Qtr Bridge II


                                                    © National Instruments 593

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:593 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:594 ordinal=594 -->
## Functions

Functions


          2    Half Bridge I
          3    Half Bridge II (default)
          4     Full Bridge I
          5     Full Bridge II
          6     Full Bridge III

            •      Vex (3.33) —

          Vex is the excitation voltage you use. The defaults is 3.333 V.

            •       Vinit (0.0) —

            Vinit is the unstrained voltage of the strain gauge after you mount it in its bridge configuration.
         Read this voltage at the beginning of your application and save it to pass to this VI.

            •       Rl (0.0) —

           Rl is the lead resistance. The Rl parameter defaults to 0. In many cases, the lead resistance is
            negligible and you can leave this terminal unwired.

            •       Strain —

           Strain is the return strain value.


     The conversion formula the VI uses is based solely on the bridge configuration. The
      following illustrations show the seven bridge configurations you can use and the
     corresponding formulas. For all bridge configurations, the VI uses the following
     formula to obtain Vr.

    Vr= (Vsg – Vinit) / Vex

      In the circuit diagrams, VOUT is the voltage you measure and pass to the conversion VI
     as the Vsg. In the quarter-bridge and half-bridge configurations, R1 and R2 are dummy
      resistors that are not directly incorporated into the conversion formula.

     The following illustrations show the available bridge-completion networks.


594   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:594 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:595 ordinal=595 -->
## Functions

Functions


© National Instruments 595

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:595 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:596 ordinal=596 -->
## Functions

Functions


596   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:596 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:597 ordinal=597 -->
## Functions

Functions

ConvertConvert StrainStrain GaugeGauge ReadingReading (scaler)(scaler) VIVI

Converts a voltage read from a strain gauge to units of strain. Wire data to the Vsg
input to determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     Rg (120) —

   Rg is the strain gauge nominal resistance value in ohms. The default is 120 Ω.

   •     GF (2.0) —

   GF is the gauge factor of the strain gauge.

   •      v (0.0) —

    v is Poisson's Ratio. This parameter is only required for certain bridge configurations.

   •      Vsg (0.0) —

    Vsg is the voltage you read from the strain gauge.

   •      Bridge Configuration (3:Half Bridge II) —

    Bridge Configuration indicates the type of bridge configuration in which the strain gauge is
    mounted. The default is Half Bridge II.

    This input accepts the following values.

    0    Qtr Bridge I
    1    Qtr Bridge II


                                                    © National Instruments 597

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:597 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:598 ordinal=598 -->
## Functions

Functions


          2    Half Bridge I
          3    Half Bridge II (default)
          4     Full Bridge I
          5     Full Bridge II
          6     Full Bridge III

            •      Vex (3.33) —

          Vex is the excitation voltage you use. The defaults is 3.333 V.

            •       Vinit (0.0) —

            Vinit is the unstrained voltage of the strain gauge after you mount it in its bridge configuration.
         Read this voltage at the beginning of your application and save it to pass to this VI.

            •       Rl (0.0) —

           Rl is the lead resistance. The Rl parameter defaults to 0. In many cases, the lead resistance is
            negligible and you can leave this terminal unwired.

            •       Strain —

           Strain is the return strain value.


     The conversion formula the VI uses is based solely on the bridge configuration. The
      following illustrations show the seven bridge configurations you can use and the
     corresponding formulas. For all bridge configurations, the VI uses the following
     formula to obtain Vr.

    Vr= (Vsg – Vinit) / Vex

      In the circuit diagrams, VOUT is the voltage you measure and pass to the conversion VI
     as the Vsg. In the quarter-bridge and half-bridge configurations, R1 and R2 are dummy
      resistors that are not directly incorporated into the conversion formula.

     The following illustrations show the available bridge-completion networks.


598   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:598 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:599 ordinal=599 -->
## Functions

Functions


© National Instruments 599

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:599 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:600 ordinal=600 -->
## Functions

Functions


600   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:600 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:601 ordinal=601 -->
## Functions

Functions

ConvertConvert ThermistorThermistor ReadingReading

Converts a thermistor voltage into a temperature. This VI has different modes of
operation for voltage-excited and current-excited thermistors. Wire data to the Voltage
input to determine the polymorphic instance to use or manually select the instance.


  • Convert Thermistor Reading (waveform) VI
  • Convert Thermistor Reading (scaler) VI

The Convert Thermistor Reading VI has two modes of operation for use with different
types of thermistor circuits. The following illustration shows how the thermistor can be
connected to a voltage reference.


The following illustration shows a circuit where the thermistor is excited by a constant
current source.


If the thermistor is excited by voltage, the following equation shows the relationship of
the thermistor resistance, RT, to the input values.


                                                    © National Instruments 601

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:601 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:602 ordinal=602 -->
## Functions

Functions

         If the thermistor is excited by current, the following equation shows the relationship of
     the thermistor resistance, RT, to the input values.


     The following equation shows the standard formula the VI uses for converting a
      thermistor resistance to temperature.


     The values used by this VI for A, B, and C are given below. If you are using a thermistor
     with different values for A, B, and C (refer to the thermistor data sheet), you can edit
     the VI diagram to use different A, B, and C values.

    A = 1.295361E-3

    B = 2.343159E-4

    C = 1.018703E-7

     The VI produces a temperature in degrees Celsius. Therefore, TC = TK – 273.15.
   ConvertConvert ThermistorThermistor ReadingReading (waveform)(waveform) VIVI

     Converts a thermistor voltage into a temperature. This VI has different modes of
     operation for voltage-excited and current-excited thermistors. Wire data to the Voltage
     input to determine the polymorphic instance to use or manually select the instance.


602   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:602 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:603 ordinal=603 -->
## Functions

Functions

Inputs/Outputs

   •      Type of Excitation —

    Type of Excitation distinguishes the two modes of operation of the VI. This VI defaults to the
   Voltage Reference mode. Use the Voltage Reference (VREF) and the R1 values only in this
    mode. You use the Current Excitation (IEX) value only in the Current Reference mode.

    This input accepts the following values.

    0     Voltage Reference
    1     Current Reference

   •      Voltage —

    Voltage is the voltage read from a thermistor.

   •      Voltage Reference —

    Voltage Reference (VREF) is the reference you apply across a resistor of known value in series
    with your thermistor. The default is 2.5 V. Use this input only when you set Type of Excitation to
   Voltage Reference.

   •     R1 —

   R1 is the value of the resistor in series with your thermistor expressed in Ohms. The default is 5
    kΩ. Use this input only when you set Type of Excitation to Voltage Reference.

   •       Excitation Current —

    Excitation Current (IEX) is the current excitation applied to the thermistor. The default is 100 µA.
    Use this input only when you set Type of Excitation to Current Reference.

   •      Temperature Units (C) —

    Temperature Units is the units of temperature the VI outputs.

    This input accepts the following values.

    0         Celsius
    1        Fahrenheit
    2         Kelvin


                                                    © National Instruments 603

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:603 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:604 ordinal=604 -->
## Functions

Functions


          3        Rankine

            •      Temperature —

         Temperature is the return temperature value in the units specified in Temperature Units.


     The Convert Thermistor Reading VI has two modes of operation for use with different
     types of thermistor circuits. The following illustration shows how the thermistor can be
     connected to a voltage reference.


     The following illustration shows a circuit where the thermistor is excited by a constant
      current source.


         If the thermistor is excited by voltage, the following equation shows the relationship of
     the thermistor resistance, RT, to the input values.


         If the thermistor is excited by current, the following equation shows the relationship of
     the thermistor resistance, RT, to the input values.


604   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:604 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:605 ordinal=605 -->
## Functions

Functions

The following equation shows the standard formula the VI uses for converting a
thermistor resistance to temperature.


The values used by this VI for A, B, and C are given below. If you are using a thermistor
with different values for A, B, and C (refer to the thermistor data sheet), you can edit
the VI diagram to use different A, B, and C values.

A = 1.295361E-3

B = 2.343159E-4

C = 1.018703E-7

The VI produces a temperature in degrees Celsius. Therefore, TC = TK – 273.15.
ConvertConvert ThermistorThermistor ReadingReading (scaler)(scaler) VIVI

Converts a thermistor voltage into a temperature. This VI has different modes of
operation for voltage-excited and current-excited thermistors. Wire data to the Voltage
input to determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •      Type of Excitation —

    Type of Excitation distinguishes the two modes of operation of the VI. This VI defaults to the
   Voltage Reference mode. Use the Voltage Reference (VREF) and the R1 values only in this
    mode. You use the Current Excitation (IEX) value only in the Current Reference mode.


                                                    © National Instruments 605

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:605 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:606 ordinal=606 -->
## Functions

Functions


           This input accepts the following values.

          0     Voltage Reference
          1     Current Reference

            •      Voltage —

          Voltage is the voltage read from a thermistor.

            •      Voltage Reference —

          Voltage Reference (VREF) is the reference you apply across a resistor of known value in series
          with your thermistor. The default is 2.5 V. Use this input only when you set Type of Excitation to
        Voltage Reference.

            •     R1 —

         R1 is the value of the resistor in series with your thermistor expressed in Ohms. The default is 5
          kΩ. Use this input only when you set Type of Excitation to Voltage Reference.

            •       Excitation Current —

           Excitation Current (IEX) is the current excitation applied to the thermistor. The default is 100 µA.
         Use this input only when you set Type of Excitation to Current Reference.

            •      Temperature Units (C) —

         Temperature Units is the units of temperature the VI outputs.

           This input accepts the following values.

          0         Celsius
          1        Fahrenheit
          2         Kelvin
          3        Rankine

            •      Temperature —

         Temperature is the return temperature value in the units specified in Temperature Units.


     The Convert Thermistor Reading VI has two modes of operation for use with different

606   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:606 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:607 ordinal=607 -->
## Functions

Functions

types of thermistor circuits. The following illustration shows how the thermistor can be
connected to a voltage reference.


The following illustration shows a circuit where the thermistor is excited by a constant
current source.


If the thermistor is excited by voltage, the following equation shows the relationship of
the thermistor resistance, RT, to the input values.


If the thermistor is excited by current, the following equation shows the relationship of
the thermistor resistance, RT, to the input values.


The following equation shows the standard formula the VI uses for converting a
thermistor resistance to temperature.


The values used by this VI for A, B, and C are given below. If you are using a thermistor
with different values for A, B, and C (refer to the thermistor data sheet), you can edit

                                                    © National Instruments 607

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:607 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:608 ordinal=608 -->
## Functions

Functions

     the VI diagram to use different A, B, and C values.

    A = 1.295361E-3

    B = 2.343159E-4

    C = 1.018703E-7

     The VI produces a temperature in degrees Celsius. Therefore, TC = TK – 273.15.

     ConvertConvert ThermocoupleThermocouple ReadingReading

     Converts a voltage reading from a thermocouple into a temperature value. Wire data to
     the Voltage Waveform (waveform), Voltage Array (array), or Thermocouple Voltage
      (scalar) input to determine the polymorphic instance to use or manually select the
      instance.

          Note This VI does not work with the NI 9211 C Series module. Instead, use
             the NI 9211 Convert to Temperature VI located in the labview\examples\
          CompactRIO\Module Specific\NI 9211\NI 9211 Support
          Files.llb directory.


          • Convert Thermocouple Reading (waveform) VI
          • Convert Thermocouple Reading (array) VI
          • Convert Thermocouple Reading (scaler) VI
   ConvertConvert ThermocoupleThermocouple ReadingReading (waveform)(waveform)
   VIVI

     Converts a voltage reading from a thermocouple into a temperature value. Wire data to
     the Voltage Waveform (waveform), Voltage Array (array), or Thermocouple Voltage
      (scalar) input to determine the polymorphic instance to use or manually select the

608   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:608 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:609 ordinal=609 -->
## Functions

Functions

instance.

      Note This VI does not work with the NI 9211 C Series module. Instead, use
       the NI 9211 Convert to Temperature VI located in the labview\examples\
      CompactRIO\Module Specific\NI 9211\NI 9211 Support
      Files.llb directory.


Inputs/Outputs

   •      Temperature Units (C) —

    Temperature Units is the units of temperature the VI outputs.

    This input accepts the following values.

    0         Celsius
    1        Fahrenheit
    2         Kelvin
    3        Rankine

   •      Voltage Waveform —

    Voltage Waveform is a waveform of voltages read from a thermocouple.

   •      ThermocoupleType —

    ThermocoupleType can be B, E, J, K, R, S, T, or N.

    This input accepts the following values. Refer to your thermocouple user manual for more
    information about thermocouple types.

    0                             B
    1                                E


                                                    © National Instruments 609

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:609 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:610 ordinal=610 -->
## Functions

Functions


          2                                    J
          3                              K
          4                              R
          5                                S
          6                                T
          7                          N

            •     CJC Voltage —

         CJC Voltage is the cold-junction compensation reference voltage. The CJC Voltage parameter is
            either the IC sensor or the thermistor sensor, as specified by CJC Sensor.

            •     CJC Sensor(0) —

         CJC Sensor is the type of cold-junction compensation sensor you are using.

         A CJC Sensor value of 0 selects the IC sensor. A CJC Sensor value of 1 selects the thermistor
           sensor.

            •      Type of Excitation —

         Type of Excitation indicates the voltage and current reference.

           This input accepts the following values.

          0     Voltage Reference
          1     Current Reference

            •      Temperature Waveform —

         Temperature Waveform returns the linearized temperature value in the units specified in
         Temperature Units.

   ConvertConvert ThermocoupleThermocouple ReadingReading (array)(array) VIVI

     Converts a voltage reading from a thermocouple into a temperature value. Wire data to
     the Voltage Waveform (waveform), Voltage Array (array), or Thermocouple Voltage
      (scalar) input to determine the polymorphic instance to use or manually select the
      instance.

610   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:610 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:611 ordinal=611 -->
## Functions

Functions

      Note This VI does not work with the NI 9211 C Series module. Instead, use
       the NI 9211 Convert to Temperature VI located in the labview\examples\
      CompactRIO\Module Specific\NI 9211\NI 9211 Support
      Files.llb directory.


Inputs/Outputs

   •      Temperature Units (C) —

    Temperature Units is the units of temperature the VI outputs.

    This input accepts the following values.

    0         Celsius
    1        Fahrenheit
    2         Kelvin
    3        Rankine

   •      Voltage Array —

    Voltage Array is an array of voltages read from a thermocouple.

   •      ThermocoupleType —

    ThermocoupleType can be B, E, J, K, R, S, T, or N.

    This input accepts the following values. Refer to your thermocouple user manual for more
    information about thermocouple types.

    0                             B
    1                                E
    2                                    J
    3                              K


                                                    © National Instruments 611

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:611 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:612 ordinal=612 -->
## Functions

Functions


          4                              R
          5                                S
          6                                T
          7                          N

            •     CJC Voltage —

         CJC Voltage is the cold-junction compensation reference voltage. The CJC Voltage parameter is
            either the IC sensor or the thermistor sensor, as specified by CJC Sensor.

            •     CJC Sensor(0) —

         CJC Sensor is the type of cold-junction compensation sensor you are using.

         A CJC Sensor value of 0 selects the IC sensor. A CJC Sensor value of 1 selects the thermistor
           sensor.

            •      Type of Excitation —

         Type of Excitation indicates the voltage and current reference.

           This input accepts the following values.

          0     Voltage Reference
          1     Current Reference

            •      Temperature Array —

         Temperature Array returns the linearized temperature value in the units specified in
         Temperature Units.

   ConvertConvert ThermocoupleThermocouple ReadingReading (scaler)(scaler) VIVI

     Converts a voltage reading from a thermocouple into a temperature value. Wire data to
     the Voltage Waveform (waveform), Voltage Array (array), or Thermocouple Voltage
      (scalar) input to determine the polymorphic instance to use or manually select the
      instance.


612   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:612 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:613 ordinal=613 -->
## Functions

Functions

      Note This VI does not work with the NI 9211 C Series module. Instead, use
       the NI 9211 Convert to Temperature VI located in the labview\examples\
      CompactRIO\Module Specific\NI 9211\NI 9211 Support
      Files.llb directory.


Inputs/Outputs

   •      Temperature Units (C) —

    Temperature Units is the units of temperature the VI outputs.

    This input accepts the following values.

    0         Celsius
    1        Fahrenheit
    2         Kelvin
    3        Rankine

   •     Thermocouple Voltage —

    Thermocouple Voltage is the voltage read from a thermocouple.

   •      ThermocoupleType —

    ThermocoupleType can be B, E, J, K, R, S, T, or N.

    This input accepts the following values. Refer to your thermocouple user manual for more
    information about thermocouple types.

    0                             B
    1                                E
    2                                    J
    3                              K


                                                    © National Instruments 613

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:613 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:614 ordinal=614 -->
## Functions

Functions


          4                              R
          5                                S
          6                                T
          7                          N

            •     CJC Voltage —

         CJC Voltage is the cold-junction compensation reference voltage. The CJC Voltage parameter is
            either the IC sensor or the thermistor sensor, as specified by CJC Sensor.

            •     CJC Sensor(0) —

         CJC Sensor is the type of cold-junction compensation sensor you are using.

         A CJC Sensor value of 0 selects the IC sensor. A CJC Sensor value of 1 selects the thermistor
           sensor.

            •      Type of Excitation —

         Type of Excitation indicates the voltage and current reference.

           This input accepts the following values.

          0     Voltage Reference
          1     Current Reference

            •      Linearized Temperature —

           Linearized Temperature returns the linearized temperature value in the units specified in
         Temperature Units.


     RadiansRadians toto DegreesDegrees

     Converts data from radians to degrees.

      This VI is a preconfigured Expression Node.


614   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:614 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:615 ordinal=615 -->
## Functions

Functions

Inputs/Outputs

   •    —

   •    —


DegreesDegrees toto RadiansRadians

Converts data from degrees to radians.

This VI is a preconfigured Expression Node.


Inputs/Outputs

   •    —

   •    —


RPMRPM toto RadiansRadians perper SecondSecond

Converts data from revolutions per minute (RPM) to radians per second.

This VI is a preconfigured Expression Node.


Inputs/Outputs

   •    —

   •    —


                                                    © National Instruments 615

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:615 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:616 ordinal=616 -->
## Functions

Functions

     RadiansRadians perper SecondSecond toto RPMRPM

     Converts data from radians per second to revolutions per minute (RPM).

      This VI is a preconfigured Expression Node.


     Inputs/Outputs

            •    —

            •    —

    NumericNumeric ConstantConstant

     Use the numeric constant to pass a numeric value to the block diagram. Set this value
     by clicking inside the constant with the Operating tool and typing a value.

         If you enter a floating-point number for the numeric constant, the default
      representation is a double-precision, floating-point number. If you enter an integer,
     the default representation is a 32-bit integer. If you enter a complex number, the
      default representation is a double-precision, complex number. For example, if you
      enter 123, the representation is a 32-bit integer. If you enter 123., the representation is
     a double-precision, floating-point number. You also can change the numeric
      representation of a numeric constant.

     You cannot change the value of the numeric constant while the VI runs. You can assign
     a label to this constant.


   EnumEnum ConstantConstant

     Use the enumerated constant to create a list of string labels with corresponding
      integer values you can select on the block diagram.

616   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:616 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:617 ordinal=617 -->
## Functions

Functions

The enumerated constant is similar to a ring constant, but you cannot customize the
corresponding numeric values for the string labels in an enumerated constant. The
numeric value is always an integer from zero to n– 1, where nis the number of values
in the enumerated constant.

Unlike the ring constant, the labels associated with an integer value are part of the
data type. If you pass the value from an enumerated constant to an indicator, LabVIEW
displays the string label instead of the numeric value.

The enumerated constant is only visible on the block diagram and cannot be viewed
on the front panel. You also cannot change its value at run time, so you should select a
value from the enumerated constant before you run the VI. Use an enumerated type
control to allow the user to select an enumerated value from the front panel at run
time.

You select, add or remove, and rearrange values in enumerated constants much the
same way you do for ring and enumerated controls.

By default, the numeric representation of an enumerated constant is a 16-bit unsigned
integer. You can change the representation of an enumerated constant to any unsigned
integer data type except for an unsigned 64-bit integer data type.


RingRing ConstantConstant

Use the ring constant to create a list of value pairs you can select on the block diagram.
Each value pair consists of a numeric value and corresponding string label.

The ring constant is similar to an enumerated constant, but you can customize the
corresponding numeric values for the string labels in a ring constant. You also can
rearrange the order of the value pairs without changing their numeric values.

If you pass the value from a ring constant to an indicator, LabVIEW displays the
numeric value instead of the string label associated with it.

You select, add or remove, and rearrange values in ring constants much the same way

                                                    © National Instruments 617

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:617 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:618 ordinal=618 -->
## Functions

Functions

     you do for ring and enumerated controls.

     By default, the numeric representation of a ring constant is a 16-bit unsigned integer.
     You can change the representation of a ring constant to any numeric data type except
     complex.


   RandomRandom NumberNumber (0-1)(0-1) FunctionFunction

     Produces a double-precision, floating-point number between 0 and 1. The number
     generated is greater than or equal to 0, but less than 1. The distribution is uniform.

      Alternatively, you can use several of the Signal Generation VIs or the Signal Generation
     PtByPt VIs to regenerate the same random sequence. For example, the Uniform White
     Noise VI allows you to set a seed number that you can use to initialize the generation
      of a pseudorandom pattern.


     Inputs/Outputs

            •     number (0 to 1) —

        number (0 to 1) is a double-precision, floating-point number between 0 and 1.

   RandomRandom NumberNumber (Range)(Range)

     Generates a random value from a specified range. Wire data to the upper bound or
     lower bound input to determine the polymorphic instance to use or manually select
     the instance.


618   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:618 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:619 ordinal=619 -->
## Functions

Functions

  • Random Number (Range) U64 VI
  • Random Number (Range) I64 VI
  • Random Number (Range) DBL VI

RandomRandom NumberNumber (Range)(Range) U64U64 VIVI

Generates a random value from a specified range. Wire data to the upper bound or
lower bound input to determine the polymorphic instance to use or manually select
the instance.


Inputs/Outputs

   •      upper bound (100) —

    upper bound specifies the upper limit of the range. The default is 100.

   •      lower bound (0) —

    lower bound specifies the lower limit of the range. The default is 0.

   •     number —

   number returns a random number greater than or equal to lower bound and less than or equal
    to upper bound.

       If upper bound is less than or equal to lower bound, this output returns lower bound.


RandomRandom NumberNumber (Range)(Range) I64I64 VIVI

Generates a random value from a specified range. Wire data to the upper bound or
lower bound input to determine the polymorphic instance to use or manually select
the instance.


                                                    © National Instruments 619

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:619 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:620 ordinal=620 -->
## Functions

Functions

     Inputs/Outputs

            •      upper bound (100) —

         upper bound specifies the upper limit of the range. The default is 100.

            •      lower bound (-100) —

          lower bound specifies the lower limit of the range. The default is -100.

            •     number —

        number returns a random number greater than or equal to lower bound and less than or equal
           to upper bound.

                 If upper bound is less than or equal to lower bound, this output returns lower bound.


    RandomRandom NumberNumber (Range)(Range) DBLDBL VIVI

     Generates a random value from a specified range. Wire data to the upper bound or
     lower bound input to determine the polymorphic instance to use or manually select
     the instance.


     Inputs/Outputs

            •      upper bound (100) —

         upper bound specifies the upper limit of the range. The default is 100.

            •      lower bound (0) —

          lower bound specifies the lower limit of the range. The default is 0.

            •     number —

        number returns a random number greater than or equal to lower bound and less than upper
         bound.


620   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:620 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:621 ordinal=621 -->
## Functions

Functions


       If upper bound is less than or equal to lower bound, this output returns lower bound.

Fixed-PointFixed-Point

Use the Fixed-Point functions to manipulate the overflow status of a fixed-point
number.


 Palette              Description
 Object

 Fixed-Point              Scales the fixed-point input to produce an integer output. This function is the
 to Integer              equivalent of an arithmetic shift of the input, constrained so that the least significant Cast                 bit of the input becomes the least significant bit of the output.
 Function

 Integer to    Scales the integer input to produce an output with the requested fixed-point type.
 Fixed-Point   This function is the equivalent of an arithmetic shift of the input with configurable
 Cast         overflow handling, constrained so that the least significant bit of the input becomes
 Function     the least significant bit of the output.

 Clear Fixed-
 Point
 Overflow     Clears the overflow status of FXP by changing the overflow status of FXP to FALSE.
 Status
 Function

 Remove
 Fixed-Point
 Overflow    Removes the overflow status from FXP.
 Status
 Function

 Include
 Fixed-Point
              Includes an overflow status with FXP. The value of the overflow status equals the
 Overflow
              value specified in overflow.
 Status
 Function


                                                    © National Instruments 621

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:621 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:622 ordinal=622 -->
## Functions

Functions

     Fixed-PointFixed-Point toto IntegerInteger CastCast FunctionFunction

     Scales the fixed-point input to produce an integer output. This function is the
     equivalent of an arithmetic shift of the input, constrained so that the least significant
      bit of the input becomes the least significant bit of the output.


     Inputs/Outputs

            •       fixed-point —

           fixed-point is the data you want to scale. fixed-point can be any fixed-point data type.

            •       integer —

           integer is the input data scaled to the smallest compatible integer type that prevents overflow.
           This output discards the overflow status.


         If fixed-point is a signed number, LabVIEW sign-extends the input data as necessary to
     ensure that the input and output data are always the same sign.

          Note The Fixed-Point to Integer Cast function combines elements of the
             Scale by Power of 2 function and the Type Cast function. The Fixed-Point to
              Integer Cast function performs an operation that reinterprets the bits, like a
               cast, but also implements an arithmetic shift with sign extension, similar to
             the Scale by Power of 2.

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Numerics\Fixed-Point Cast.vi


622   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:622 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:623 ordinal=623 -->
## Functions

Functions

IntegerInteger toto Fixed-PointFixed-Point CastCast FunctionFunction

Scales the integer input to produce an output with the requested fixed-point type. This
function is the equivalent of an arithmetic shift of the input with configurable overflow
handling, constrained so that the least significant bit of the input becomes the least
significant bit of the output.


Inputs/Outputs

   •       fixed-point type —

    fixed-point type is the fixed-point data type to which you want to convert the integer data. You
    can configure the fixed-point data type in the Data Type page of the Properties dialog box.
    LabVIEW ignores any data in the constant or control that you wire to fixed-point type. You also
    can leave this input unwired and configure the output data type in the Output Configuration
    page of the Properties dialog box.

   •       integer —

    integer is the data you want to scale. integer can be any integer data type.

   •       fixed-point —

    fixed-point is the input data scaled to the requested fixed-point data type.


If the word length of integer is greater than or less than the word length of fixed-point
type, LabVIEW first converts integer to the integer word length of fixed-point type
before casting integer to the requested fixed-point type. The least significant bit of
integer becomes the least significant bit of fixed-point, so rounding is never
necessary.

To override the default behavior of this function, right-click the function and select
Properties from the shortcut menu to display the Output Configuration page of the
Properties dialog box. You can use this dialog box to configure the output settings of
this function.


                                                    © National Instruments 623

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:623 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:624 ordinal=624 -->
## Functions

Functions

          Note The Integer to Fixed-Point Cast function combines elements of the
            Conversion functions, the Type Cast function, and the Scale by Power of 2
              function. The Integer to Fixed-Point Cast function performs an operation that
              reinterprets the bits, like a cast, but also handles the numerical overflow and
              sign extension issues that commonly arise when combining integer and fixed-
             point algorithms.

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Numerics\Fixed-Point Cast.vi

     ClearClear Fixed-PointFixed-Point OverflowOverflow StatusStatus FunctionFunction

      Clears the overflow status of FXP by changing the overflow status of FXP to FALSE.


     Inputs/Outputs

            •     FXP —

         FXP specifies a fixed-point number.

            •     FXP with overflow cleared —

         FXP with overflow cleared returns FXP with an overflow status of FALSE. If FXP does not include
         an overflow status, FXP with overflow cleared returns FXP unchanged.

            •      overflow? —

          overflow? is TRUE if FXP includes an overflow status and FXP is the result of an operation that
           overflowed.

                 If FXP does not include an overflow status, or if FXP includes an overflow status but is not the
            result of an operation that overflowed, overflow? is FALSE.


624   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:624 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:625 ordinal=625 -->
## Functions

Functions

RemoveRemove Fixed-PointFixed-Point OverflowOverflow StatusStatus FunctionFunction

Removes the overflow status from FXP.

To change the overflow status to FALSE, use the Clear Fixed-Point Overflow Status
function.


Inputs/Outputs

   •     FXP —

    FXP specifies a fixed-point number.

   •     FXP with overflow removed —

    FXP with overflow removed returns FXP without an overflow status. If FXP does not include an
    overflow status, FXP with overflow removed returns FXP unchanged.

   •      overflow? —

    overflow? is TRUE if FXP includes an overflow status and FXP is the result of an operation that
    overflowed.

       If FXP does not include an overflow status, or if FXP includes an overflow status but is not the
     result of an operation that overflowed, overflow? is FALSE.

IncludeInclude Fixed-PointFixed-Point OverflowOverflow StatusStatus FunctionFunction

Includes an overflow status with FXP. The value of the overflow status equals the value
specified in overflow.


Inputs/Outputs

   •     FXP —

                                                    © National Instruments 625

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:625 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:626 ordinal=626 -->
## Functions

Functions


         FXP specifies a fixed-point number.

            •      overflow —

          overflow specifies whether the overflow status of FXP with overflow included is TRUE or FALSE.

            •     FXP with overflow included —

         FXP with overflow included returns FXP with an overflow status set to the value specified in
           overflow.

   DBLDBL NumericNumeric ConstantConstant

     Use the DBL numeric constant to pass a double-precision, floating-point numeric value
      to the block diagram. Set this value by clicking inside the constant with the Operating
      tool and typing a value.

         If you enter a floating-point number for the numeric constant, the default
      representation is a double-precision, floating-point number. For example, if you enter
     123, the representation is a 32-bit integer.

     You also can change the numeric representation of a numeric constant. If you enter an
      integer, the default representation is a 32-bit integer. For example, if you enter 123.,
     the representation is a double-precision, floating-point number. If you enter a complex
     number, the default representation is a double-precision, complex number.

     You cannot change the value of the numeric constant while the VI runs. You can assign
     a label to this constant.


     PositivePositive InfinityInfinity

     Returns the value Inf (infinity).

     LabVIEW converts Inf to the highest value for a data type. For example, converting Inf

626   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:626 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:627 ordinal=627 -->
## Functions

Functions

to a 16-bit signed integer returns the value 32,767, the highest possible value for a
16-bit signed integer.


MachineMachine EpsilonEpsilon

Represents the round-off error for a floating-point number with a given precision. Use
the machine epsilon constant to compare whether two floating-point numbers are
equivalent.


NotNot AA NumberNumber ConstantConstant

Returns the value NaN (not a number).

You can change the numeric representation of this constant by right-clicking the
constant and selecting Representation from the shortcut menu. You also can assign a
label to this constant.


MathMath && ScientificScientific ConstantsConstants

Use the Math & Scientific Constants to create LabVIEW applications.


 Palette Object                             Description

 Pi                                        Returns the value 3.1415926535897932.

 Pi Multiplied By 2                          Returns the value 6.2831853071795865.

                                                    © National Instruments 627

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:627 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:628 ordinal=628 -->
## Functions

Functions


       Palette Object                             Description

        Pi Divided By 2                            Returns the value 1.5707963267948966.

       Reciprocal Of Pi                           Returns the value 0.31830988618379067.

       Natural Logarithm Of Pi                    Returns the value 1.1447298858494002.

       Natural Logarithm Base                    Returns the value 2.7182818284590452.

       Reciprocal Of e                            Returns the value 0.36787944117144232.

      Base 10 Logarithm Of e                     Returns the value 0.43429448190325183.

       Natural Logarithm Of 10                    Returns the value 2.3025850929940597.

       Natural Logarithm Of 2                     Returns the value 0.69314718055994531.

       Planck's Constant (J/Hz)                    Returns the value 6.62607015e-34.

       Elementary Charge (C)                     Returns the value 1.602176634e-19.

      Speed Of Light In Vacuum (m/sec)           Returns the value 299792458.

        Gravitational Constant (N m2/kg2)           Returns the value 6.67430e-11.

      Avogadro Constant (1/mol)                 Returns the value 6.02214076e23.

      Rydberg Constant (1/m)                    Returns the value 10973731.568160.

       Molar Gas Constant (J/(mol K))              Returns the value 8.314462618.

    RangeRange LimitsLimits forfor TypeType

     Returns the maximum and minimum values of the input data type.


     Inputs/Outputs

            •      type —

          type specifies the data type.

           This input accepts any scalar numeric data type and enum.

            •     maximum value for type —

628   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:628 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:629 ordinal=629 -->
## Functions

Functions


   maximum value for type returns the maximum value of the data type wired to type. If type is an
    enum, this VI returns the last value of the enum.

    For example, if type is a 16-bit unsigned integer, this output returns 32767. If type is an enum
    with values {cat, dog, bird}, this output returns bird.

   •     minimum value for type —

   minimum value for type returns the minimum value of the data type wired to type. If type is an
    enum, this VI returns the first value of the enum.

    For example, if type is a 16-bit unsigned integer, this output returns -32768. If type is an enum
    with values {cat, dog, bird}, this output returns cat.

ExpressionExpression NodeNode

Use the Expression Node to calculate expressions that contain a single variable. The
following built-in functions are allowed in formulas: abs, acos, acosh, asin, asinh, atan,
atanh, ceil, cos, cosh, cot, csc, exp, expm1, floor, getexp, getman, int, intrz, ln, lnp1, log,
log2, max, min, mod, rand, rem, sec, sign, sin, sinc, sinh, sizeOfDim, sqrt, tan, tanh.


Inputs/Outputs

   •    —

    input is the value that the Expression Node uses as the variable.

   •    —

    output returns the value of the calculation.


Expression Nodes are useful when an expression has only one variable but is otherwise
complicated. Use the correct syntax, operators, and functions when creating
Expression Nodes.

Expression Nodes have the following restrictions:

                                                    © National Instruments 629

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:629 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:630 ordinal=630 -->
## Functions

Functions

          • Expression Nodes accept any non-complex numeric data type.
          • Expression Nodes accept only the period (.) as a decimal separator. The nodes do
         not recognize localized decimal separators.
          • Expression Nodes accept only pi as a constant. The constant is case-sensitive.
          • You cannot add Expression Nodes to a VI on which you enable inlining.

    BooleanBoolean

     Use the Boolean functions to perform logical operations on single Boolean values or
      arrays of Boolean values.


       Palette                   Description       Object

                Computes the logical AND of the inputs. Both inputs must be Boolean values, numeric      And                     values, or error clusters. If both inputs are TRUE, the function returns TRUE. Otherwise,
       Function                             it returns FALSE.

                Computes the logical OR of the inputs. Both inputs must be Boolean values, numeric
      Or                     values, or error clusters. If both inputs are FALSE, the function returns FALSE.       Function                   Otherwise, it returns TRUE.

        Exclusive   Computes the logical exclusive or (XOR) of the inputs. Both inputs must be Boolean
      Or          values, numeric values, or error clusters. If both inputs are TRUE or both inputs are
       Function    FALSE, the function returns FALSE. Otherwise, it returns TRUE.

      Not       Computes the logical negation of the input. If x is FALSE, the function returns TRUE. If x
       Function     is TRUE, the function returns FALSE.

                  Performs arithmetic on one or more numeric, array, cluster, or Boolean inputs. To
     Compound  select the operation (Add, Multiply, AND, OR, or XOR), right-click the function and
       Arithmetic  select Change Mode from the shortcut menu. When you select this function from the
        VI         Numeric palette, the default mode is Add. When you select this function from the
                 Boolean palette, the default mode is OR.

                Computes the logical NAND of the inputs. Both inputs must be Boolean values,
      Not And
                 numeric values, or error clusters. If both inputs are TRUE, the function returns FALSE.
       Function
                   Otherwise, it returns TRUE.


630   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:630 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:631 ordinal=631 -->
## Functions

Functions


Palette            Description
Object

          Computes the logical NOR of the inputs. Both inputs must be Boolean values, numericNot Or             values, or error clusters. If both inputs are FALSE, the function returns TRUE.Function            Otherwise, it returns FALSE.

Not          Computes the logical negation of the logical exclusive or (XOR) of the inputs. BothExclusive            inputs must be Boolean values, numeric values, or error clusters. If both inputs areOr         TRUE or both inputs are FALSE, the function returns TRUE. Otherwise, it returns FALSE.Function

           Negates x and then computes the logical OR of y and the negated x. Both inputs mustImplies          be Boolean values, numeric values, or error clusters. If x is TRUE and y is FALSE, theFunction            function returns FALSE. Otherwise, it returns TRUE.

And Array   Returns TRUE if all the elements in Boolean array are TRUE or if Boolean array is
Elements   empty. Otherwise, the function returns FALSE. This function accepts an array of any
Function    size but returns only a single value based on all values in Boolean array.

Or Array    Returns FALSE if all the elements in Boolean array are FALSE or if Boolean array is
Elements   empty. Otherwise, the function returns TRUE. This function accepts an array of any
Function    size but returns only a single value based on all values in Boolean array.

            Converts an integer or fixed-point number to a Boolean array. If you wire an integer to
Number To number, Boolean array returns an array of 8, 16, 32, or 64 elements, depending on the
Boolean   number of bits in the integer. If you wire a fixed-point number to number, the size of
Array       the array that Boolean array returns equals the word length of the fixed-point number.
Function   The 0th element of the array corresponds to the least significant bit of the two's
          complement representation of the integer.

Boolean            Converts a Boolean array to an integer or a fixed-point number by interpreting theArray To
             array as the binary representation of the number. The first element of the arrayNumber
           corresponds to the least significant bit in the number.
Function

Boolean To
            Converts a Boolean FALSE or TRUE value to a 16-bit integer with a value of 0 or 1,
(0,1)
             respectively.
Function

True
          Use this constant to provide a value of TRUE to the block diagram.
Constant

False
          Use this constant to provide a value of FALSE to the block diagram.
Constant


                                                    © National Instruments 631

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:631 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:632 ordinal=632 -->
## Functions

Functions

    AndAnd FunctionFunction

     Computes the logical AND of the inputs. Both inputs must be Boolean values, numeric
      values, or error clusters. If both inputs are TRUE, the function returns TRUE. Otherwise,
        it returns FALSE.

          Note This function performs bitwise operations on numeric inputs.

     The connector pane displays the default data types for this polymorphic function.


     Inputs/Outputs

            •      x —

          x must be a Boolean value or a number.x can be a scalar, array or cluster of numbers or Boolean
           values, array of clusters of numbers or Boolean values, and so on. If x is an error cluster, only the
           status parameter of the error cluster passes to the input terminal.

            •      y —

          y must be a Boolean value or a number. y can be a scalar, array or cluster of numbers or Boolean
           values, arrays of clusters of numbers or Boolean values, and so on. If y is an error cluster, only
          the status parameter of the error cluster passes to the input terminal.

            •      x .and. y? —

          x .and. y? is the logical AND of x and y.


    And Truth Table

       x             y              x .and. y?

      T            T            T

      T             F              F


632   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:632 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:633 ordinal=633 -->
## Functions

Functions


 x             y              x .and. y?

 F            T              F

 F             F              F

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Booleans\Boolean Functions.vi

OrOr FunctionFunction

Computes the logical OR of the inputs. Both inputs must be Boolean values, numeric
values, or error clusters. If both inputs are FALSE, the function returns FALSE.
Otherwise, it returns TRUE.

      Note This function performs bitwise operations on numeric inputs.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x must be a Boolean value or a number. x can be a scalar, array or cluster of numbers or Boolean
     values, array of clusters of numbers or Boolean values, and so on. If x is an error cluster, only the
    status parameter of the error cluster passes to the input terminal.

   •      y —

    y must be a Boolean value or a number. y can be a scalar, array or cluster of numbers or Boolean
     values, arrays of clusters of numbers or Boolean values, and so on. If y is an error cluster, only
    the status parameter of the error cluster passes to the input terminal.


                                                    © National Instruments 633

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:633 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:634 ordinal=634 -->
## Functions

Functions

            •      x .or. y? —

          x .or. y? is the logical Or of x and y.


    Or Truth Table

       x               y                x .or. y?

      T              T              T

      T               F              T

      F              T              T

      F               F               F

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Booleans\Boolean Functions.vi

     ExclusiveExclusive OrOr FunctionFunction

     Computes the logical exclusive or (XOR) of the inputs. Both inputs must be Boolean
      values, numeric values, or error clusters. If both inputs are TRUE or both inputs are
     FALSE, the function returns FALSE. Otherwise, it returns TRUE.

          Note This function performs bitwise operations on numeric inputs.

     The connector pane displays the default data types for this polymorphic function.


     Inputs/Outputs

            •      x —


634   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:634 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:635 ordinal=635 -->
## Functions

Functions


    x must be a Boolean value or a number.x can be a scalar, array or cluster of numbers or Boolean
     values, array of clusters of numbers or Boolean values, and so on. If x is an error cluster, only the
    status parameter of the error cluster passes to the input terminal.

   •      y —

    y must be a Boolean value or a number.y can be a scalar, array or cluster of numbers or Boolean
     values, arrays of clusters of numbers or Boolean values, and so on. If y is an error cluster, only
    the status parameter of the error cluster passes to the input terminal.

   •      x .xor. y? —

    x .xor. y? is the logical exclusive or (XOR) of x and y.


Exclusive Or Truth Table

 x              y               x .xor. y?

 T             T              F

 T              F             T

 F             T             T

 F              F              F

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Booleans\Boolean Functions.vi

NotNot FunctionFunction

Computes the logical negation of the input. If x is FALSE, the function returns TRUE. If x
is TRUE, the function returns FALSE.

      Note This function performs bitwise operations on numeric inputs.


                                                    © National Instruments 635

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:635 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:636 ordinal=636 -->
## Functions

Functions

     The connector pane displays the default data types for this polymorphic function.


     Inputs/Outputs

            •      x —

          x can be a scalar Boolean value or number, array or cluster of Boolean values or numbers, array
           of clusters of Boolean values or numbers, and so on. If x is an error cluster, only the status
          parameter of the error cluster passes to the input terminal.

            •       .not. x? —

            .not. x? is the logical negation of x.


    Not Truth Table

       x                        .not. x?

      F                  T

      T                   F

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Booleans\Boolean Functions.vi

    NotNot AndAnd FunctionFunction

     Computes the logical NAND of the inputs. Both inputs must be Boolean values,
     numeric values, or error clusters. If both inputs are TRUE, the function returns FALSE.
     Otherwise, it returns TRUE.

          Note This function performs bitwise operations on numeric inputs.


636   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:636 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:637 ordinal=637 -->
## Functions

Functions

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x must be a Boolean value or a number. x can be a scalar, array or cluster of numbers or Boolean
     values, array of clusters of numbers or Boolean values, and so on. If x is an error cluster, only the
    status parameter of the error cluster passes to the input terminal.

   •      y —

    y must be a Boolean value or a number. y can be a scalar, array or cluster of numbers or Boolean
     values, arrays of clusters of numbers or Boolean values, and so on. If y is an error cluster, only
    the status parameter of the error cluster passes to the input terminal.

   •       .not. (x .and. y)? —

     .not. (x .and. y)? is the logical NAND of x and y.


Not And Truth Table

 x         y            .not. (x .and. y)?

 T         T         F

 T         F         T

 F         T         T

 F         F         T

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Booleans\Boolean Functions.vi


                                                    © National Instruments 637

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:637 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:638 ordinal=638 -->
## Functions

Functions

    NotNot OrOr FunctionFunction

     Computes the logical NOR of the inputs. Both inputs must be Boolean values, numeric
      values, or error clusters. If both inputs are FALSE, the function returns TRUE.
     Otherwise, it returns FALSE.

          Note This function performs bitwise operations on numeric inputs.

     The connector pane displays the default data types for this polymorphic function.


     Inputs/Outputs

            •      x —

          x must be a Boolean value or a number. x can be a scalar, array or cluster of numbers or Boolean
           values, array of clusters of numbers or Boolean values, and so on. If x is an error cluster, only the
           status parameter of the error cluster passes to the input terminal.

            •      y —

          y must be a Boolean value or a number. y can be a scalar, array or cluster of numbers or Boolean
           values, arrays of clusters of numbers or Boolean values, and so on. If y is an error cluster, only
          the status parameter of the error cluster passes to the input terminal.

            •       .not. (x .or. y)? —

            .not. (x .or. y)? is the logical NOR of x and y.


    Not Or Truth Table

       x          y             .not. (x .or. y)?

      T         T          F

      T          F          F


638   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:638 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:639 ordinal=639 -->
## Functions

Functions


 x          y             .not. (x .or. y)?

 F         T          F

 F          F          T

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Booleans\Boolean Functions.vi

NotNot ExclusiveExclusive OrOr FunctionFunction

Computes the logical negation of the logical exclusive or (XOR) of the inputs. Both
inputs must be Boolean values, numeric values, or error clusters. If both inputs are
TRUE or both inputs are FALSE, the function returns TRUE. Otherwise, it returns FALSE.

      Note This function performs bitwise operations on numeric inputs.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x must be a Boolean value or a number. x can be a scalar, array or cluster of numbers or Boolean
     values, array of clusters of numbers or Boolean values, and so on. If x is an error cluster, only the
    status parameter of the error cluster passes to the input terminal.

   •      y —

    y must be a Boolean value or a number. y can be a scalar, array or cluster of numbers or Boolean
     values, arrays of clusters of numbers or Boolean values, and so on. If y is an error cluster, only
    the status parameter of the error cluster passes to the input terminal.


                                                    © National Instruments 639

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:639 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:640 ordinal=640 -->
## Functions

Functions

            •       .not. (x .xor. y)? —

            .not. (x .xor. y)? is the logical negation of the logical exclusive or (XOR) of x and y.


    Not Exclusive Or Truth Table>

       x          y            .not. (x .xor. y)?

      T         T         T

      T          F          F

      F         T          F

      F          F         T

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Booleans\Boolean Functions.vi

     ImpliesImplies FunctionFunction

     Negates x and then computes the logical OR of y and the negated x. Both inputs must
     be Boolean values, numeric values, or error clusters. If x is TRUE and y is FALSE, the
      function returns FALSE. Otherwise, it returns TRUE.

          Note This function performs bitwise operations on numeric inputs.

     The connector pane displays the default data types for this polymorphic function.


     Inputs/Outputs

            •      x —


640   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:640 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:641 ordinal=641 -->
## Functions

Functions


    x must be a Boolean value or a number. x can be a scalar, array or cluster of numbers or Boolean
     values, array of clusters of numbers or Boolean values, and so on. If x is an error cluster, only the
    status parameter of the error cluster passes to the input terminal.

   •      y —

    y must be a Boolean value or a number. y can be a scalar, array or cluster of numbers or Boolean
     values, arrays of clusters of numbers or Boolean values, and so on. If y is an error cluster, only
    the status parameter of the error cluster passes to the input terminal.

   •      x .implies. y? —

    x .implies. y? is the logical OR of y and of the logical negation of x.


Implies Truth Table

 x           y           x .implies. y?

 T          T          T

 T           F           F

 F          T          T

 F           F          T

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Booleans\Boolean Functions.vi

AndAnd ArrayArray ElementsElements FunctionFunction

Returns TRUE if all the elements in Boolean array are TRUE or if Boolean array is
empty. Otherwise, the function returns FALSE. This function accepts an array of any
size but returns only a single value based on all values in Boolean array.

The connector pane displays the default data types for this polymorphic function.


                                                    © National Instruments 641

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:641 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:642 ordinal=642 -->
## Functions

Functions


     Inputs/Outputs

            •      Boolean array —

         Boolean array can have any number of dimensions.

            •       logical AND —

            logical AND indicates if all elements in Boolean array are TRUE.

    OrOr ArrayArray ElementsElements FunctionFunction

     Returns FALSE if all the elements in Boolean array are FALSE or if Boolean array is
     empty. Otherwise, the function returns TRUE. This function accepts an array of any size
     but returns only a single value based on all values in Boolean array.

     The connector pane displays the default data types for this polymorphic function.


     Inputs/Outputs

            •      Boolean array —

         Boolean array can have any number of dimensions.

            •       logical OR —

            logical OR indicates if all of the elements in Boolean array are false.

   NumberNumber ToTo BooleanBoolean ArrayArray FunctionFunction

     Converts an integer or fixed-point number to a Boolean array. If you wire an integer to
     number, Boolean array returns an array of 8, 16, 32, or 64 elements, depending on the

642   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:642 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:643 ordinal=643 -->
## Functions

Functions

number of bits in the integer. If you wire a fixed-point number to number, the size of
the array that Boolean array returns equals the word length of the fixed-point number.
The 0th element of the array corresponds to the least significant bit of the two's
complement representation of the integer.


Inputs/Outputs

   •     number —

   number can be a number.

   •      Boolean array —

    Boolean array can have 8, 16, 32, or 64 elements if number is an integer. If number is a fixed-
    point number, Boolean array can have between 1 and 64 elements.


If you wire a fixed-point number that includes an overflow status to number, this
function ignores the overflow status and converts only the number to a Boolean array.

BooleanBoolean ArrayArray ToTo NumberNumber FunctionFunction

Converts a Boolean array to an integer or a fixed-point number by interpreting the
array as the binary representation of the number. The first element of the array
corresponds to the least significant bit in the number.


Inputs/Outputs

   •      Boolean array —

    Boolean array is a one-dimensional array of Boolean values.

    This function truncates Boolean array if it is too long. If Boolean array is too short, this function


                                                    © National Instruments 643

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:643 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:644 ordinal=644 -->
## Functions

Functions


         pads Boolean array according to the Sign Extension Mode you can select by right-clicking the
           function.

                   • Never —This function pads Boolean array with Boolean FALSE bits.
                   •  If Output Is Signed —(default) For an output with an unsigned representation, this function
             pads Boolean array with Boolean FALSE bits. For an output with a signed representation,
                 this function pads Boolean array with the last element of the array.
                   • Always —This function pads Boolean array with the last element of the array.
            •     number —

        number is an integer or a fixed-point number.

         You can change the numeric representation of number on the Output Configuration page of the
           Properties dialog box. Right-click the function and select Properties to display the Properties
           dialog box.


     The following table shows the relationship between Boolean array and number.


                                 Output              Sign Extension     Binary      Boolean array                                                        number                                    Representation     Mode             Value

       {FALSE, TRUE}                     I8                                If Output Is Signed  11111110    -2

       {FALSE, TRUE}              U8                               If Output Is Signed  00000010   2

       {FALSE, TRUE, FALSE, TRUE}      I8                  Always            11111010    -6

       {FALSE, TRUE, FALSE, TRUE}      I8                  Never             00001010   10

       {FALSE, FALSE, TRUE, FALSE,                              U8                               If Output Is Signed  00010100   20
      TRUE}

       {FALSE, FALSE, TRUE, FALSE,
                              U8                  Always            11110100   244
      TRUE}

    BooleanBoolean ToTo (0,1)(0,1) FunctionFunction

     Converts a Boolean FALSE or TRUE value to a 16-bit integer with a value of 0 or 1,
      respectively.


644   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:644 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:645 ordinal=645 -->
## Functions

Functions


Inputs/Outputs

   •      Boolean —

    Boolean can be a scalar, an array, a cluster of Boolean values, an array of clusters of Boolean
     values, and so on. If Boolean is an error cluster, only the status parameter of the error cluster
    passes to the input terminal.

   •       0, 1 —

     0, 1 is 0 if Boolean is FALSE and 1 if Boolean is TRUE.

TrueTrue ConstantConstant

Use this constant to provide a value of TRUE to the block diagram.

You can assign a label to this constant by right-clicking the constant and selecting
Visible Items»Label from the shortcut menu.

You can change this value to FALSE by using the Operating tool to click the T portion of
the constant or by right-clicking the constant and selecting Data Operations»Change
Value to False from the shortcut menu. You cannot change this value while the VI runs.


FalseFalse ConstantConstant

Use this constant to provide a value of FALSE to the block diagram.

You can assign a label to this constant by right-clicking the constant and selecting
Visible Items»Label from the shortcut menu.

You can change this value to TRUE by using the Operating tool to click the F portion of
the constant or by right-clicking the constant and selecting Data Operations»Change
Value to True from the shortcut menu. You cannot change this value while the VI runs.

                                                    © National Instruments 645

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:645 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:646 ordinal=646 -->
## Functions

Functions


    StringString

     Use the String functions to concatenate two or more strings, extract a subset of strings
     from a string, convert data into strings, and format a string for use in a word processing
     or spreadsheet application.


       Palette
                    Description       Object

        String
       Length       Returns in length the number of characters (bytes) in string.
       Function

       Concatenate Concatenates input strings and 1D arrays of strings into a single output string. For
        Strings       array inputs, this function concatenates each element of the array.

        String                    Returns the substring of the input string beginning at offset and containing length
       Subset                 number of characters.       Function

                 Removes all ASCII white space (spaces, tabs, carriage returns, and linefeeds) from the       Trim                     beginning, end, or both ends of string. The Trim Whitespace VI does not remove       Whitespace
                   double byte characters.


                    Converts the line endings of the input string to the line ending format you specify. If
       Normalize   you do not specify a line ending format, this VI converts the line endings of the string
      End Of Line   to the line endings that the current platform expects. Use this VI to make your strings
                    readable by different platforms or by the command line of the current platform.

       Replace
       Substring     Inserts, deletes, or replaces a substring at the offset you specify in string.
       Function

       Search and   Replaces one or all instances of a substring with another substring. To include the


646   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:646 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:647 ordinal=647 -->
## Functions

Functions


Palette             Description
Object

Replace              multiline? input and enable advanced regular expression searches, right-click theString              function and select Regular Expression.Function

             Searches for regular expression in string beginning at offset. If the function finds a
Match       match, it splits string into three substrings. A regular expression requires a specific
Pattern      combination of characters for pattern matching. This function gives you fewer
Function     options for matching strings but performs more quickly than the Match Regular
             Expression function.

             Searches for a regular expression in the input string beginning at the offset youMatch               enter. If the function finds a match, it splits the string into three substrings and anyRegular
           number of submatches. Resize the function to view any submatches found in theExpression                string.

Path/Array/
String       Use the Path/Array/String Conversion functions to convert strings, arrays, and paths.
Conversion

Scan From            Scans the input string and converts the string according to format string.
String

Format Into            Formats string, path, enumerated type, time stamp, Boolean, or numeric data as text.
String

Format
Date/Time    Displays a timestamp value or a numeric value as time in the format you specify
String        using time format codes.
Function

             Creates an output string from a combination of text and parameterized inputs. If the
Build Text    input is not a string, this Express VI converts the input into a string based on the
              configuration of the Express VI.

Number/
String       Use the String/Number Conversion functions to convert strings.
Conversion

Spreadsheet
             Converts the spreadsheet string to an array of the dimension and representation of
String To
             array type. This function works for arrays of strings and arrays of numbers.
Array


                                                    © National Instruments 647

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:647 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:648 ordinal=648 -->
## Functions

Functions


       Palette                    Description
       Object

       Function

       Array To                    Converts an array of any dimension to a table in string form, containing tabs       Spreadsheet                     separating column elements, a platform-dependent EOL character separating rows,
        String                    and, for arrays of three or more dimensions, headers separating pages.       Function

      To Upper     Converts all alphabetic characters in string to uppercase characters. Evaluates all
      Case       numbers in string as ASCII codes for characters. This function does not affect non-
       Function     alphabetic characters.

      To Lower     Converts all alphabetic characters in string to lowercase characters. Evaluates all
      Case       numbers in string as ASCII codes for characters. This function does not affect non-
       Function     alphabetic characters.

        Flatten/                  Use the Flatten/Unflatten String functions to flatten and unflatten LabVIEW data       Unflatten
                    types to and from strings.        String

        String                  Use this constant to supply a constant text string to the block diagram.
       Constant

      Empty
        String        Consists of a constant string that is empty (length zero).
       Constant

      Space
                  Use this constant to supply a one-character space string to the block diagram.       Constant

      Tab                     Consists of a constant string containing the ASCII HT (horizontal tab) value.
       Constant

       Additional
                  Use the Additional String VIs and functions to scan and search in strings, match
        String
                      patterns, and manipulate strings.
       Functions

       Carriage
       Return       Consists of a constant string containing the ASCII CR value.
       Constant

       Line Feed
                     Consists of a constant string containing the ASCII LF value.
       Constant

      End of Line   Consists of a constant string containing the platform-dependent end-of-line value.

648   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:648 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:649 ordinal=649 -->
## Functions

Functions


 Palette              Description
 Object

 Constant

StringString LengthLength FunctionFunction

Returns in length the number of characters (bytes) in string.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •       string —

     string can be a string or any data structure that contains only strings, such as an array or clusters
     of strings.

   •      length —

    length has the same structure as string.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Strings\String Length.vi

ConcatenateConcatenate StringsStrings

Concatenates input strings and 1D arrays of strings into a single output string. For
array inputs, this function concatenates each element of the array.

Add inputs to the function by right-clicking an input and selecting Add Input from the
shortcut menu or by resizing the function.

                                                    © National Instruments 649

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:649 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:650 ordinal=650 -->
## Functions

Functions


     Inputs/Outputs

            •       string —

           string 0..n-1 are the strings you want to concatenate.

            •       string —

            •      concatenated string —

          concatenated string contains the concatenated input strings in the order you wire them to the
         node from top to bottom.


     You can use this function to concatenate the output from Picture Functions VIs so that
     they draw on a single picture control. The pictures are drawn in order from top to
     bottom.

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Strings\Concatenate Strings.vi

     StringString SubsetSubset FunctionFunction

     Returns the substring of the input string beginning at offset and containing length
    number of characters.

     The connector pane displays the default data types for this polymorphic function.


650   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:650 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:651 ordinal=651 -->
## Functions

Functions

Inputs/Outputs

   •       string —

     string is the input string.

   •       offset (0) —

     offset specifies number of characters into string at which the function starts searching for a
    match. offset must be numeric.

    The offset of the first character in string is 0. If offset is unwired or less than 0, the function takes
     offset as 0.
   •      length (rest) —

    length must be numeric. If length is left unwired, the default is the length of string minus offset.

   •      substring —

    substring is empty if offset is greater than the length of the string or if the length is less than or
    equal to 0.

       If length is greater than or equal to the length of string minus offset, substring is the remainder
     of string beginning at offset.

TrimTrim WhitespaceWhitespace

Removes all ASCII white space (spaces, tabs, carriage returns, and linefeeds) from the
beginning, end, or both ends of string. The Trim Whitespace VI does not remove
double byte characters.

The default is to remove white space from both ends of string.


Inputs/Outputs

   •       location (both) —


                                                    © National Instruments 651

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:651 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:652 ordinal=652 -->
## Functions

Functions


           location determines if this function removes white space from the beginning, end, or both ends
           of string.

         The default is both.

          0 Both—Removes white space from both ends of the input string.
          1 Start of string—Removes white space from the start of the input string.
          2 End of string—Removes white space from the end of the input string.

            •       string —

           string is the input string.

            •     trimmed string —

         trimmed string contains the string with the white space removed.

    NormalizeNormalize EndEnd OfOf LineLine

     Converts the line endings of the input string to the line ending format you specify. If
     you do not specify a line ending format, this VI converts the line endings of the string
      to the line endings that the current platform expects. Use this VI to make your strings
     readable by different platforms or by the command line of the current platform.

     For example, if you specify UNIX in end of line, LabVIEW converts the line endings of
      string in to \n because \n is the standard UNIX line ending.


     Inputs/Outputs

            •     end of line (Native) —

         end of line specifies the line ending to which to convert.


652   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:652 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:653 ordinal=653 -->
## Functions

Functions


          Note In LabVIEW for macOS, Native and Native Command Line are equivalent to
             UNIX. In LabVIEW for OS X 32-bit, Native and Native Command Line are equivalent to
             Macintosh.


    0 Native—Specifies the native line ending of the current platform.
     Native Command Line—Specifies the native line ending of the command line of the current    1      platform.
    2 UNIX—Specifies the UNIX line ending, used by Linux, macOS, and other UNIX derivatives, \n.
    3 Macintosh—Specifies the Macintosh Classic line ending, \r.
    4 DOS—Specifies the standard DOS/Windows line ending, \r\n.

   •       string in —

     string in specifies the string containing the line endings you want to convert.

   •       string out —

     string out returns the string with converted line endings.

ReplaceReplace SubstringSubstring FunctionFunction

Inserts, deletes, or replaces a substring at the offset you specify in string.


Inputs/Outputs

   •       string —

     string is the string in which you want to replace characters.

   •      substring ("") —

    substring contains the substring that replaces length characters at offset in string.

   •       offset (0) —


                                                    © National Instruments 653

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:653 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:654 ordinal=654 -->
## Functions

Functions


            offset determines the number of characters into string at which the function places substring.

            •      length (len. of substring) —

          length determines the number of characters in string to replace with substring.

                 If substring is empty, length characters are deleted starting at offset.
            •       result string —

           result string contains the edited string with the replaced characters.

            •      replaced substring —

          replaced substring contains the characters that were replaced in string.


     The Replace Substring function deletes length characters in string starting at offset,
     and replaces the deleted portion with substring. If length is 0, the Replace Substring
      function inserts substring at offset. If substring is empty, the Replace Substring
      function deletes length characters at offset.

    SearchSearch andand ReplaceReplace StringString FunctionFunction

     Replaces one or all instances of a substring with another substring. To include the
      multiline? input and enable advanced regular expression searches, right-click the
      function and select Regular Expression.


     Inputs/Outputs

            •       multiline? (F) —

           multiline? specifies whether to treat the text in input string as a multiple-line string. This setting


654   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:654 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:655 ordinal=655 -->
## Functions

Functions


  affects how the ^ and $ characters handle matches.

   If you set multiline? to FALSE (default), when you enter ^ at the beginning of a regular
  expression, the expression matches only the beginning of the string in input string. When you
  enter $ at the end of a regular expression, the expression matches only the end of the string in
  input string. If you set multiline? to TRUE, ^ matches the beginning of any line in input string
  and $ matches the end of any line in input string.

        Note The ^ character anchors the match to the beginning of a string when used as
           the first character of a pattern. If you add ^ to the beginning of a character class
          immediately after an open square bracket, the expression matches any character not
            in a given character class.

•      ignore case? (F) —

  ignore case? specifies whether the string search is case sensitive.

   If FALSE (default), the string search is case sensitive.

•      replace all? (F) —

  replace all? specifies whether the function replaces all occurrences of the search string or only
  the first occurrence.

   If FALSE (default), the function replaces only the first occurrence.

•      input string —

  input string specifies the input string you want the function to search.

•      search string —

  search string specifies the string you want to search for and replace.

   If search string is an empty string and replace all? is FALSE, the function inserts replace string at
  the beginning of input string. If search string is an empty string and replace all? is TRUE, the
  function inserts replace string at the beginning, in between each character, and at the end of
  input string.

  To search using advanced regular expressions, right-click the function and select Regular
  Expression.

•      replace string ("") —


                                                   © National Instruments 655

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:655 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:656 ordinal=656 -->
## Functions

Functions


          replace string specifies the string you want to insert in place of search string. The default is an
         empty string.

         To configure the Search and Replace String function to accept backreferences in replace string,
             right-click the function and select Regular Expression.

            •       offset (0) —

            offset determines the number of characters into input string at which the function starts
           searching for search string.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •       result string —

           result string contains the input string with one or all occurrences of search string replaced with
          replace string.

                 If replace string is empty, result string contains input string with search string deleted.

            •     number of replacements —

        number of replacements returns the number of times LabVIEW replaced search string.

            •       offset past replacement —

            offset past replacement indicates the offset in result string of the character immediately
           following where the last match and replacement occurred.

                 If replace all? is FALSE, the next match, if any, is after this point.

                 If the function does not find search string, offset past replacement returns –1.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


          Note The Search and Replace String function does not support null
             characters in strings. If you include null characters in the strings you wire to

656   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:656 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:657 ordinal=657 -->
## Functions

Functions


         this function, LabVIEW returns an error and the function may return
       unexpected results.

If you want to search for more complex patterns, such as patterns that contain
character grouping, alternate pattern matching, backreferences, or non-greedy
quantification, configure the function for advanced regular expression searches or use
the Match Regular Expression function.

To search for matches using advanced regular expressions in search string and partial
match substitution in replace string, right-click the Search and Replace String function
and select Regular Expression from the shortcut menu. This function uses the same
regular expression syntax as the Match Regular Expression function.

Regular expression support is provided by the PCRE library package. Refer to the
<National Instruments>\_Legal Information directory for more
information about the license under which the PCRE library package is redistributed.

Refer to the PCRE website at www.pcre.org for more information about Perl
Compatible Regular Expressions.

MatchMatch PatternPattern FunctionFunction

Searches for regular expression in string beginning at offset. If the function finds a
match, it splits string into three substrings. A regular expression requires a specific
combination of characters for pattern matching. This function gives you fewer options
for matching strings but performs more quickly than the Match Regular Expression
function.

The Match Pattern function is compatible with a limited set of regular expressions and
does not support character grouping, alternate pattern matching, backreferences, or
non-greedy quantification. You can use a specific set of special characters to refine the
search. The connector pane displays the default data types for this polymorphic
function.


                                                    © National Instruments 657

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:657 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:658 ordinal=658 -->
## Functions

Functions


     Inputs/Outputs

            •       string —

           string specifies the input string you want the function to search.

            •      regular expression —

           regular expression is the pattern for which you want to search in string. If the function does not
            find regular expression, match substring returns an empty string, before substring returns the
            entire string, after substring returns an empty string, and offset past match returns –1.

            •       offset (0) —

            offset specifies number of characters into string at which the function starts searching for a
          match. offset must be numeric. The offset of the first character in string is 0. If offset is unwired
           or less than 0, the function takes offset as 0.

            •      before substring —

          before substring returns a string containing all the characters before the match.

            •     match substring —

         match substring is the matched string.

            •       after substring —

            after substring contains all characters following the matched pattern.

            •       offset past match —

            offset past match returns the index in string of the first character of after substring. If the
           function does not find a match, offset past match is –1. The offset input and the offset past
         match output might be equal when the empty string is a valid match for the regular expression.
          For example, if regular expression is b* and the string input is cdb, offset past match is 0. If
           string is bbbcd, offset past match is 3.


      This function is similar to the Search and Replace Pattern VI. The Match Pattern

658   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:658 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:659 ordinal=659 -->
## Functions

Functions

function gives you fewer options for matching strings but performs more quickly than
the Match Regular Expression function. For example, the Match Pattern function does
not support the parenthesis or vertical bar (|) characters.

The following table shows examples of regular expressions you can use with this
function. Some of these examples use special characters to refine the search.

      Note If you want to include special characters in the search string, you must
       enclose each special character in brackets. For example, to search for the
         string hz+, enter hz[+] in regular expression. Otherwise, LabVIEW uses the
        special character to refine the search.


 Characters to Find                                      Regular Expression

 VOLTS                                      VOLTS

 All uppercase and lowercase versions of volts, that is,
                                            [Vv][Oo][Ll][Tt][Ss]
 VOLTS, Volts, volts, and so on

 A space, a plus sign, or a minus sign                  [ +-]

 A sequence of one or more digits                    [0-9]+

                                            [\s*] or [ *] (that is, a space Zero or more spaces
                                                          followed by an asterisk)

 One or more spaces, tabs, new lines, or carriage returns     [\t \r \n \s]+

 One or more characters other than digits               [~0-9]+

 The word Level only if it begins at the offset position in the
                                            ^Level
 string

 The word Volts only if it appears at the end of the string   Volts$

 The longest string within parentheses                 (.*)

 The longest string within parentheses but not containing
                                            ([~()]*) any parentheses within it

 A left bracket                                  \[

 A right bracket                                 \]

 cat, dog, cot, dot, cog, and so on.                 [cd][ao][tg]


                                                    © National Instruments 659

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:659 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:660 ordinal=660 -->
## Functions

Functions

    MatchMatch RegularRegular ExpressionExpression

     Searches for a regular expression in the input string beginning at the offset you enter.
         If the function finds a match, it splits the string into three substrings and any number
      of submatches. Resize the function to view any submatches found in the string.


     Inputs/Outputs

            •       multiline? (F) —

           multiline? specifies whether to treat the text in input string as a multiple-line string. This setting
            affects how the ^ and $ characters handle matches. If you set multiline? to FALSE (default), when
         you enter ^ at the beginning of a regular expression, the expression matches only the beginning
           of the string in input string. When you enter $ at the end of a regular expression, the expression
         matches only the end of the string in input string. If you set multiline? to TRUE, ^ matches the
          beginning of any line in input string and $ matches the end of any line in input string.

              Note The ^ character anchors the match to the beginning of a string when used as
                   the first character of a pattern. If you add ^ to the beginning of a character class
                  immediately after an open square bracket, the expression matches any character not
                      in a given character class.

            •      ignore case? (F) —
          ignore case? specifies whether the string search is case sensitive. If FALSE (default), the string
          search is case sensitive.
            •      input string —
          input string specifies the input string the function searches. This string cannot contain null
           characters.
            •      regular expression —
           regular expression specifies the pattern you want to search for in input string. If the function
         does not find a match, whole match and after match contain empty strings, before match
           contains the entire input string, offset past match returns –1, and all submatches outputs return
         empty strings. Place any substrings you want to search for in parentheses. The function returns
         any substring expressions it finds in substring 1..n. This string cannot contain null characters.
            •       offset (0) —
            offset specifies the number of characters into input string at which the function starts searching
            for search string.
            •       error in —

660   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:660 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:661 ordinal=661 -->
## Functions

Functions

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.
   •      before match —
    before match returns all the characters before the match.
   •     whole match —
    whole match returns all the characters that match the expression entered in regular expression.
    Any substring matches the function finds appear in the submatch outputs.
   •       after match —
     after match returns all the characters after the match.
   •       offset past match —
     offset past match returns the index in input string of the first character after the last match. If
    the VI does not find a match, offset past match returns –1.
   •       error out —
    error out contains error information. This output provides standard error out functionality.

      Note The Match Regular Expression function does not support null
        characters in strings. If you include null characters in strings you wire to this
        function, LabVIEW returns an error and the function may return unexpected
         results.

Regular expression support is provided by the PCRE library package. Refer to
<National Instruments>\_Legal Information directory for more
information about the license under which the PCRE library package is redistributed.

Refer to the PCRE website at www.pcre.org for more information about Perl
Compatible Regular Expressions.

The Match Regular Expression function gives you more options for matching strings
but performs more slowly than the Match Pattern function.

Use regular expressions in this function to refine searches.

Avoiding Stack Overflow

Certain regular expressions that use repeated grouped expressions (such as (.|\s)*
or (a*)*) require significant resources to process when applied to large input
strings. In some cases a stack overflow may occur on large input strings. Some regular
expressions may recurse repeatedly while attempting to match a large string, which


                                                    © National Instruments 661

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:661 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:662 ordinal=662 -->
## Functions

Functions

    may eventually overflow the stack. For example, the regular expression (.|\n)*A
     and a large input string may cause LabVIEW to crash. To avoid recursion, you can
      rewrite the regular expression (.|\n)*A as (?s).*A. The (?s) notation indicates
      that a period matches new lines. You also can rewrite the expression as [^A]*A.

    Grouping Patterns for Submatches

     You can capture submatches by placing parentheses ( ) around a portion of a regular
     expression that you want the function to return as a submatch. For example, the
      regular expression (el.)..(L..) returns two submatches in the input string
    Hello LabVIEW!: ell and Lab. Each submatch corresponds to a character group
      in the order that the character group appears in the regular expression. In this
     example, submatch 1 is ell and submatch 2 is Lab.

         If you nest a character group within another character group, the regular expression
      creates a submatch for the outer group before the inner group. For example, the
      regular expression (.(el.).).(L..) returns three submatches in the input Hello
    LabVIEW!: Hello, ell, and Lab. In this example, submatch 1 is Hello because
     the regular expression matches the outer character group before the inner group.

    Examples of Regular Expressions

     The following table shows examples of regular expressions you can use with the Match
     Regular Expression function.


       Characters to Find                                               Regular Expression

     VOLTS                                             VOLTS

      A plus sign or a minus sign                                [+-]

      A sequence of one or more digits                            [0-9]+

                                                       \s* or * (that is, a space       Zero or more spaces
                                                                         followed by an asterisk)

      One or more spaces, tabs, new lines, or carriage returns            [\t \r \n \s]+

      One or more characters other than digits                      [^0-9]+

      The word Level only if it appears at the beginning of the string      ^Level


662   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:662 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:663 ordinal=663 -->
## Functions

Functions


 Characters to Find                                               Regular Expression

 The word Volts only if it appears at the end of the string          Volts$

 The longest string within parentheses                        \(.*\)

 The first string within parentheses but not containing any parentheses
                                                   \([^()]*\) within it

 A left bracket                                         \[

 A right bracket                                        \]

 cat, cag, cot, cog, dat, dag, dot, and dog                  [cd][ao][tg]

 cat or dog                                          cat|dog

 dog, cat dog, cat cat dog,cat cat cat dog, and so on     ((cat )*dog)

 One or more of the letter a followed by a space and the same number
                                                   (a+) \1
 of the letter a, that is, a a, aa aa, aaa aaa, and so on

Path/Array/StringPath/Array/String ConversionConversion

Use the Path/Array/String Conversion functions to convert strings, arrays, and paths.


 Palette Object           Description

 Path to Array of Strings   Converts a path into an array of strings and indicates whether the path is
 Function                    relative.

 Array of Strings to Path
                         Converts an array of strings into a relative or absolute path.
 Function

                         Converts path into a string describing a path in the standard format of
 Path To String Function
                         the platform.

                         Converts a string, describing a path in the standard format for the
 String To Path Function
                          current platform, to a path.

 String To Byte Array
                         Converts a string into an array of unsigned bytes.
 Function

 Byte Array To String      Converts an array of unsigned bytes representing ASCII characters into a


                                                    © National Instruments 663

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:663 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:664 ordinal=664 -->
## Functions

Functions


       Palette Object           Description

       Function                    string.

     PathPath toto ArrayArray ofof StringsStrings FunctionFunction

     Converts a path into an array of strings and indicates whether the path is relative.


     Inputs/Outputs

            •      path —

          path is the path you want to convert to an array of strings.

                 If path is <Not A Path>, the array of strings is empty and relative is FALSE.
            •       relative —

            relative indicates whether the path you converted is a relative path or an absolute path.

                 If TRUE, it is a relative path. If FALSE, it is an absolute path.
            •      array of strings —

           array of strings contains the components of the path.

         The first element is the first step of the path hierarchy. For file systems that support multiple
          volumes, the first element is the volume name. If path is a network path, the first element of
           array of strings includes the name of the server in addition to the first step of the path hierarchy.
         The last element of array of strings is the file or directory specified by the path.

     ArrayArray ofof StringsStrings toto PathPath FunctionFunction

     Converts an array of strings into a relative or absolute path.

         If you have an empty string in the array, the directory location before the empty string
       is deleted in the path output. This behavior is similar to moving up a level in directory
      hierarchy.


664   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:664 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:665 ordinal=665 -->
## Functions

Functions


Inputs/Outputs

   •       relative —

     relative indicates whether you want to create a relative path or an absolute path.

       If TRUE, the function creates a relative path. If FALSE (default), the function creates an absolute
    path. If FALSE and the path specified is not valid as an absolute path (for example, the path
   means go up a level), the function sets path to <Not A Path>.

   •      array of strings —

    array of strings contains the names of the components of the path you want to build.

    The first element is the highest level of the path hierarchy (the volume name, for file systems
    that support multiple volumes), and the last element is the last element of the hierarchy. An
    element that contains an empty string tells LabVIEW to go up a level in the hierarchy.

          Note Each string in the array of strings must represent a single element of the
            complete path. Partial paths, such as test\subtest, are not valid as array
            elements because they might produce invalid paths on platforms that use different
              directory separators.

   •      path —

    path is the resulting path.


Suppose the path to the VI containing this function is c:\dir1\main.vi. To use this
function to build a relative path to another VI such as c:\dir1\dir2\called.vi,
wire TRUE to relative. In array of strings, enter dir2 as the first element and
called.vi as the second element. The function returns a relative path of dir2\
called.vi. You can use the Build Path function to append the relative path to the
output of the Current VI's Path function.

To build an absolute path to c:\dir1\dir2\called.vi, wire FALSE to relative. In
array of strings, enter c as the first element, dir1 as the second element, dir2 as

                                                    © National Instruments 665

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:665 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:666 ordinal=666 -->
## Functions

Functions

     the third element, and called.vi as the fourth element. The function returns an
     absolute path of c:\dir1\dir2\called.vi.

     PathPath ToTo StringString FunctionFunction

     Converts path into a string describing a path in the standard format of the platform.

     The connector pane displays the default data types for this polymorphic function.


     Inputs/Outputs

            •      path —

          path is the path, array of paths, cluster of paths, or array of clusters of paths you want to convert
           to a string.

                 If path is <Not A Path>, the function sets string to <Not A Path>.
            •       string —

           string is the path descriptor(s) represented by path in the standard format for the current
           platform. string is of the same data type structure as path.


     StringString ToTo PathPath FunctionFunction

     Converts a string, describing a path in the standard format for the current platform, to
     a path.

     The connector pane displays the default data types for this polymorphic function.


     Inputs/Outputs

            •       string —


666   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:666 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:667 ordinal=667 -->
## Functions

Functions


     string can be a string or any data structure that contains only strings, such as an array or clusters
     of strings.

   •      path —

    path is the platform-independent representation of the path described by string.

       If string is not a valid path descriptor on the current platform, the function sets path to <Not a
    Path>. path is of the same data type structure as string.

          Note If string is <Not a Path>, the function returns a path to <Not a Path>. If
           you attempt to use the path, LabVIEW cannot find the file and throws an error.


StringString ToTo ByteByte ArrayArray FunctionFunction

Converts a string into an array of unsigned bytes.

Each byte in the array has the ASCII value of the corresponding character in the string.


Inputs/Outputs

   •       string —

     string is the input string the function converts.

   •      unsigned byte array —

    unsigned byte array is the output array.

    The first byte in the array has the ASCII value of the first character in string, the second byte has
    the second value, and so on.

ByteByte ArrayArray ToTo StringString FunctionFunction

Converts an array of unsigned bytes representing ASCII characters into a string.


                                                    © National Instruments 667

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:667 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:668 ordinal=668 -->
## Functions

Functions


     Inputs/Outputs

            •      unsigned byte array —

          unsigned byte array is the array of ASCII values you want to convert.

            •       string —

           string is the result of interpreting each array element as an ASCII value and forming a string out
           of the corresponding characters.

           Refer to ASCII Codes for the numbers that correspond to each character.

    ScanScan FromFrom StringString

     Scans the input string and converts the string according to format string.

     Use this function when you know the exact format of the input. The input can be
      string, path, enumerated type, time stamp, or numeric data. Alternatively, you can use
     the Scan From File function to scan text from a file. The connector pane displays the
      default data types for this polymorphic function.


     Inputs/Outputs

            •      format string —

          format string specifies how to convert the input string into the output arguments.

         The default is to scan the string according to the default format for the data types of the outputs.
          Formatting a time stamp as anything other than time returns an error. Right-click the function


668   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:668 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:669 ordinal=669 -->
## Functions

Functions


  and select Edit Scan String from the shortcut menu to create and edit the format string.

  A space in format string matches any amount of white space, such as spaces, tabs, linefeeds,
  and form feeds.

  This input accepts a maximum of 255 characters.

•      input string —

  input string is the string, path, enumerated type, time stamp, or numeric data to scan.

•        initial scan location —

   initial scan location is the offset into the string where the scan begins.

  The default is 0.
•       error in —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•       default value 1 —

  default 1..n specifies the type and default value for the output parameters.

   If this function cannot scan the input value from format string, the function uses the default. If
  you do not wire default 1 and you wire a constant to format string, the function uses format
  string to determine the type of the output. Otherwise, the default data type is double-precision,
  floating-point. The default value is 0 or an empty string, depending on the output data type. If
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


                                                   © National Instruments 669

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:669 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:670 ordinal=670 -->
## Functions

Functions

            •      remaining string —

          remaining string returns the portion of the string that remains after scanning all arguments.

            •       offset past scan —

            offset past scan is the offset of input string after completing the scan.

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
             contains a string of the form ''Scan From String (arg n),'' where
          n is the first argument for which the error occurred.

         If you set format string to return numeric values in the output parameters, LabVIEW
      ignores white spaces in the input string.

         If you wire a block diagram constant string to format string, LabVIEW uses format
      string to determine the number of outputs and the data type of each output at
     compile time. If the types you wire to the outputs do not match the types determined
     by format string, you must change the output types before the VI can run.

         If you do not directly wire a block diagram constant to format string, LabVIEW checks
      for type mismatches at run time. If you want to scan values that have data types other
     than double-precision, floating point, you must wire the data types to default 1..n.


670   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:670 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:671 ordinal=671 -->
## Functions

Functions

      Note By default, this function is locale aware, which means that it uses the
       system decimal separator configured in the regional settings of the operating
       system. In some instances, such as using GPIB instruments on European
        operating systems, you may need to override the system decimal separator
       by using the localization code syntax elements.

Examples of Formatting Strings

Refer to the Format Specifier Syntax topic for more information about and examples of
formatting strings.


                                                                            remaining input string       format string                      default(s)        output(s)
                                                                                          string

                              —              abc
 abc, xyz                         —                xyz
                  %3s, %s%f%2d                                            00
 >12.3+56i 7200                                        0.00+00i          12.30+56.00i
                              —              72

 Q+1.27E–3 tail    Q%f t                —               1.27E–3        ail

                              —               12.00
 0123456789      %3d%3d                                                  6789
                              —              345

                                                100 (I32)        10
 X:9.860 Z:3.450     X:%fY:%f                                                               Z: 3450
                                                    100.00 (DBL)     100.00

 set49.4.2         set%d               —              49             .4.2

                                                   blue (enum {red,
 color: red           color: %s                                        red      —
                                                      green, blue})

                                                             abcd

                                                               12
 abcd012xyz3      %[a-z]%d%[a-z]%d        —                —
                                                                        xyz

                                                               3

 welcome to
                                                          welcome to
 LabVIEW, John     %[^,],%s              —                          Smith
                                                             LabVIEW
 Smith

                                                    © National Instruments 671

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:671 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:672 ordinal=672 -->
## Functions

Functions


                                                                                  remaining       input string       format string                      default(s)        output(s)
                                                                                                 string

                                                                 John

                                                                               11:15:04.250       Time: 23:15:04.25                         Time:                               PM                                                          1/1/1904            —                   %<%H:%M:%S%2u%m/%d/%Y>T       5/31/2004                                                                          5/31/2004


    FormatFormat IntoInto StringString

     Formats string, path, enumerated type, time stamp, Boolean, or numeric data as text.

     You can use the Format Into String function to convert a number into a string. To
     format data as text and write the text to a file, use the Format Into File function
      instead.


     Inputs/Outputs

            •      format string —

          format string specifies how you want the function to convert the input arguments into resulting
            string.

           Defaults match the data type of the input arguments. Right-click the function and select Edit
         Format String from the shortcut menu to create and edit the format string. Use special escape
          codes to insert non-displayable characters, the backslash, and the percent characters.

              Note This function interprets backslashes as escape characters. To use a literal
                   backslash in format string, you must enter \\.

            •        initial string —


672   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:672 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:673 ordinal=673 -->
## Functions

Functions


     initial string specifies the base string to which you can append any arguments to form the
    resulting string.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      input 1 —

    input 1..n specifies the input parameters you want the function to convert.

    This parameter accepts a string, path, enumerated type, time stamp, Boolean, or any numeric
    data type. For complex numeric data types, this function converts only the real component. You
    cannot use arrays and clusters with this function. You can specify up to 4,096 characters for each
     input.

       If you specify a Boolean value for this parameter and %s as the format code, the Format Into
     String function outputs the value as TRUE or FALSE. If you specify a Boolean value for this
    parameter and any numeric format code, the Format Into String function outputs the
    appropriate version of 1 for TRUE and 0 for FALSE. For example, if you specify %f as the format
    code, the function outputs 1.00000. If you specify %d, the function outputs 1.

   •       resulting string —

    resulting string contains the concatenation of initial string and the formatted output.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


To increase the number of parameters, right-click input 1 and select Add Parameter
from the shortcut menu or resize the function.

      Note If an error occurs, the error out cluster element source contains a
         string of the form Format Into String (arg n), where nis the first
       argument for which the error occurred.

If you wire a block diagram constant string to format string, LabVIEW uses format
string to determine the number of outputs and the data type of each output at

                                                    © National Instruments 673

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:673 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:674 ordinal=674 -->
## Functions

Functions

     compile time. If the data types you wire to the outputs do not match the data types
     determined by format string, you must change the output data types before the VI can
      run.

     Specifying Which Input to Use within the Format String

     By default, this function uses the order of the inputs to populate the format specifiers,
     or percent codes in the Format String. However, you can use a number followed by a
      dollar sign ($) within a percent code to specify exactly which input to use for that
     percent code. For example, the percent code %3$d uses the third input regardless of
    how many percent codes appear before %3$d in the format string.

      Refer to the following block diagram and table for an example of how to use format
      specifiers:


     The following input combinations illustrate the effects of the $ specifier in the previous
     block diagram:


       Input           Format    Return               Input 2                     Comments
      1                 String     String
                           first     Format String does notuse the $ specifier, so the     first second %s %s
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


674   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:674 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:675 ordinal=675 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\Spreadsheet\Tab-Delimited Data\
   Buffered Stream to Tab-Delimited Text File.vi

FormatFormat Date/TimeDate/Time StringString FunctionFunction

Displays a timestamp value or a numeric value as time in the format you specify using
time format codes.


Inputs/Outputs

   •      time format string (%c) —

    time format string specifies the format of the output string.

    Time format codes (beginning with %) not recognized by the function as a format code return the
    character literally. The default code is %c, which corresponds to the date/time representation
    appropriate for the configured time zone for the computer. If time format string is an empty
     string, the function uses the default.
   •      time stamp —

    time stamp can be a timestamp or a numeric. If numeric, this number is the time-zone-
    independent number of seconds that have elapsed since 12:00 a.m., Friday, January 1, 1904,
    Universal Time [01-01-1904 00:00:00]. The default is the current date and time.

       If year is before 1904, time stamp is negative.
   •     UTC format —

   UTC format specifies if the output string is in Universal Time or in the configured time zone for
    the computer. If TRUE, date/time string is in Universal Time.

    The default is FALSE.
   •      date/time string —


                                                    © National Instruments 675

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:675 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:676 ordinal=676 -->
## Functions

Functions


          date/time string is the formatted date/time string.


      This function calculates date/time string by copying time format string and replacing
     each of the time format codes with the corresponding values. For example, the time
     format string %y%m%d displays timestamp in the format yymmdd. The time format
      string %y%m%d displays the date January 30, 2014 as 140130.

     The following list describes some of the caveats to consider when you use this
      function:

          • LabVIEW returns abbreviated weekday and month names as numeric values for
        systems that do not support abbreviated names, such as Chinese and Korean.
          • The %c, %u, %x, %X, %z, and %Z format codes depend on operating system locale
         support. The output of these codes is platform dependent. Interpretation of the
         Daylight Saving Time rule also can vary by platform.
          • The %p format code only takes effect at locales that use the 12-hour time system.
          • Time format codes have leading zeros as necessary to ensure a constant field
         width. An optional # modifier before the format code letter removes the leading
         zeros from the following format codes: %#d, %#H, %#I, %#j, %#m, %#M,
       %#s, %#S, %#U, %#w, %#W, %#X, %#y, %#Y. The # modifier does not
        modify the behavior of any other format codes.

     Related Information

     Time Format Codes

     BuildBuild TextText

     Creates an output string from a combination of text and parameterized inputs. If the
     input is not a string, this Express VI converts the input into a string based on the
      configuration of the Express VI.


676   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:676 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:677 ordinal=677 -->
## Functions

Functions

Dialog Box Options

 Option            Description

                     Specifies the text you want to build. Define parameters by placing text between Text with
                 a pair of percent signs. You can use each parameter only once in the text that Parameters in
                 you build. Percents
 (%parameter                 To include a percent sign in the output string, you must type the percent sign
 name%)                     twice.

                   Contains the following options:

                               • Parameter—

                            Lists all parameters defined in the Text with Parameters in Percents
                    (%parameter name%) section.

                               • Sample text—

                        Displays text configured according to the options set in Parameter
                        Properties.

                               • Sample boolean—
 Configure
 Parameters            Displays a button configured according to the options set in Parameter
                        Properties.

                               • Sample number—

                        Displays a number configured according to the options set in Parameter
                        Properties.

                               • Sample result—

                        Displays the value you enter in Sample text, Sample number, or Sample
                     boolean based on the options you select in the Parameter Properties
                          section.

                   Contains the following options:
 Parameter
 Properties               • Text—


                                                    © National Instruments 677

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:677 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:678 ordinal=678 -->
## Functions

Functions


      Option            Description

                           Formats the parameter as a text string.

                                         • Number—

                           Formats the parameter as a numeric value.

                                         • Boolean—

                           Formats the parameter as a Boolean value.

                                         • Format—

                             Provides formatting options for the parameter depending on the data type.
                           Examples of each format appear in parentheses after the name of the
                              format.

                                         • Use minimum field width—

                           Pads any excess space to the left or right of the text, number, or Boolean
                             with zeros or spaces to reach the minimum width you enter in Minimum
                                   field width.

                                         • Minimum field width—

                                Specifies the width to which you want to pad the text, number, or Boolean.
                         The default is 0.

                                         • Use specified precision—

                           Formats the numbers with the precision you specify in Precision. This
                             option is available only when you select Fractional/Scientific (12.345),
                               Fractional (12.345), or Scientific (1.234E1) from the Format the numbers
                            pull-down menu.

                                         • Precision—

                          Changes the digits of precision of the numbers in the table. The default is
                                    0.

        Justification      Contains the following options:


678   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:678 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:679 ordinal=679 -->
## Functions

Functions


 Option            Description

                               • Left—

                           Justifies the parameter to the left.

                               • Right—

                           Justifies the parameter to the right.

                   Contains the following options:

                               • Using spaces—

                     Pads numbers using spaces. Padding
                               • Using zeros—

                     Pads numbers using zeros.


Inputs/Outputs

   •      Beginning Text —

    Prepends the text you wire to this input to the text the Express VI generates.

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •       error out —

    Contains error information. This output provides standard error out functionality.

   •      Result —

    Returns the resulting data based on the configuration of the Express VI.


Components

Changes the digits of precision of the numbers in the table. The default is 0.

                                                    © National Instruments 679

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:679 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:680 ordinal=680 -->
## Functions

Functions

     Formats the numbers with the precision you specify in Precision. This option is
      available only when you select Fractional/Scientific (12.345), Fractional (12.345), or
      Scientific (1.234E1) from the Format the numbers pull-down menu.

     Pads any excess space to the left or right of the text, number, or Boolean with zeros or
     spaces to reach the minimum width you enter in Minimum field width.

     Pads numbers using zeros.

      Justifies the parameter to the left.

     Provides formatting options for the parameter depending on the data type. Examples
      of each format appear in parentheses after the name of the format.

      Displays a button configured according to the options set in Parameter Properties.

     Formats the parameter as a Boolean value.

      Displays a number configured according to the options set in Parameter Properties.

     Formats the parameter as a numeric value.

      Displays text configured according to the options set in Parameter Properties.

     Formats the parameter as a text string.

     Changes the digits of precision of the numbers in the table. The default is 0.

      Specifies the width to which you want to pad the text, number, or Boolean. The default
       is 0.

     Formats the numbers with the precision you specify in Precision. This option is
      available only when you select Fractional/Scientific (12.345), Fractional (12.345), or
      Scientific (1.234E1) from the Format the numbers pull-down menu.

     Pads any excess space to the left or right of the text, number, or Boolean with zeros or
     spaces to reach the minimum width you enter in Minimum field width.

     Pads numbers using spaces.

680   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:680 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:681 ordinal=681 -->
## Functions

Functions

Pads numbers using zeros.

Justifies the parameter to the right.

Justifies the parameter to the left.

Provides formatting options for the parameter depending on the data type. Examples
of each format appear in parentheses after the name of the format.

Specifies the text you want to build. Define parameters by placing text between a pair
of percent signs. You can use each parameter only once in the text that you build.

Lists all parameters defined in the Text with Parameters in Percents (%parameter
name%) section.

Displays the value you enter in Sample text, Sample number, or Sample boolean
based on the options you select in the Parameter Properties section.

Number/StringNumber/String ConversionConversion

Use the String/Number Conversion functions to convert strings.


 Palette              Description Object

 Number To
              Converts number to a string of decimal digits at least width characters wide or wider
 Decimal
                        if necessary. If number is floating-point or fixed-point, it is rounded to a 64-bit
 String
               integer before conversion.
 Function

 Number To   Converts number to a string of hexadecimal digits at least width characters wide or
 Hexadecimal wider if necessary. The digits A-F always appear in uppercase in the output string. If
 String      number is floating-point or fixed-point, it is rounded to a 64-bit integer before
 Function      conversion.

 Number To   Converts number to a string of octal digits at least width characters wide or wider if
 Octal String   necessary. If number is floating-point or fixed-point, it is rounded to a 64-bit integer
 Function     before conversion.

                                                    © National Instruments 681

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:681 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:682 ordinal=682 -->
## Functions

Functions


       Palette                     Description
       Object

      Number To
        Fractional    Converts number to an F-format (fractional notation), floating-point string at least
        String       width characters wide or wider if necessary.
       Function

      Number To
       Exponential  Converts number to an E-format (exponential notation), floating-point string at least
        String       width characters wide or wider if necessary.
       Function

      Number To
       Engineering  Converts number to an engineering format, floating-point string at least width
        String        characters wide or wider if necessary.
       Function

      Format                    Converts a number into a regular string according to the format specified in format       Value                      string and appends this to string.
       Function

       Decimal
        String To     Converts the numeric characters in string, starting at offset, to a decimal integer and
      Number      returns it in number.
       Function

      Hexadecimal
        String To      Interprets the characters 0 through 9, A through F, and a through f in string starting
      Number       at offset as a hex integer and returns it in number.
       Function

       Octal String   Interprets the characters 0 through 7 in string starting at offset as an octal integer
      To Number   and returns it in number. This function also returns the index in string of the first
       Function      character following the number.

       Fract/Exp
                       Interprets the characters 0 through 9, plus, minus, e, E, and the decimal point
        String To
                       (usually period) in string starting at offset as a floating-point number in engineering
      Number
                      notation, exponential, or fractional format and returns it in number.
       Function

                    Converts characters at the beginning of string to the data type represented by
      Scan Value    default, according to the conversion codes in format string, and returns the
       Function     converted number in value and the remainder of string after the match in output
                        string.


682   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:682 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:683 ordinal=683 -->
## Functions

Functions

NumberNumber ToTo DecimalDecimal StringString FunctionFunction

Converts number to a string of decimal digits at least width characters wide or wider if
necessary. If number is floating-point or fixed-point, it is rounded to a 64-bit integer
before conversion.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •     number —

   number can be a scalar number, array or cluster of numbers, array of clusters of numbers, and
    so on.

   •      width (-) —

    width must be numeric. If unwired, the function uses exactly as many digits as are needed to
    represent the number, with no extra padding.

   •      decimal integer string —

    decimal integer string is the resulting decimal string.

    The following table shows how the values of number and width affect decimal integer string. In
     this table, the underline character ( _ ) represents spaces in decimal integer string.

                decimal integer
   number width              Comments
                   string
                                      Floating-point and fixed-point numbers are rounded to
     4.6    2    _5
                                         integers.
     3.0    4    _ _ _3                      If width is larger than needed, spaces are added on the left.
                                                           If width is inadequate, decimal integer string is as large as
    –311   3    –311
                                     necessary.


                                                    © National Instruments 683

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:683 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:684 ordinal=684 -->
## Functions

Functions

    NumberNumber ToTo HexadecimalHexadecimal StringString FunctionFunction

     Converts number to a string of hexadecimal digits at least width characters wide or
     wider if necessary. The digits A-F always appear in uppercase in the output string. If
    number is floating-point or fixed-point, it is rounded to a 64-bit integer before
      conversion.

     The connector pane displays the default data types for this polymorphic function.


     Inputs/Outputs

            •     number —

        number can be a scalar number, array or cluster of numbers, array of clusters of numbers, and
          so on.

            •      width (-) —

          width must be numeric. If unwired, the function uses exactly as many digits as are needed to
           represent the number, with no extra padding.

            •      hex integer string —

         hex integer string is the resulting hexadecimal string.

         The following table shows how the values of number and width affect hex integer string.

                     hex
        number width integer  Comments
                          string
          3      4    0003        If width is larger than needed, zeros are added on the left.
          42     3    02A   —
                                   –4.2 is rounded up to –4 in 64-bit integer format. Width is too small to
           –4.2    3    FFFFFFFC represent the hex version of a negative number, so the field width is
                                extended.


684   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:684 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:685 ordinal=685 -->
## Functions

Functions

NumberNumber ToTo OctalOctal StringString FunctionFunction

Converts number to a string of octal digits at least width characters wide or wider if
necessary. If number is floating-point or fixed-point, it is rounded to a 64-bit integer
before conversion.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •     number —

   number can be a scalar number, array or cluster of numbers, array of clusters of numbers, and
    so on.

   •      width (-) —

    width must be numeric. If unwired, the function uses exactly as many digits as are needed to
    represent the number, with no extra padding.

   •       octal integer string —

    octal integer string is the resulting octal string. The following table shows how the values of
   number and width affect octal integer string.

                   octal integer   number width          Comments
                   string
    3      4    0003    —
    42     3    052     —
                               –4.2 is rounded up to –4 in 64-bit integer format. width is too small
    –4.2    3    37777777774 to represent the octal version of a negative number, so the field
                            width is extended.


NumberNumber ToTo FractionalFractional StringString FunctionFunction

Converts number to an F-format (fractional notation), floating-point string at least


                                                    © National Instruments 685

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:685 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:686 ordinal=686 -->
## Functions

Functions

     width characters wide or wider if necessary.

     The connector pane displays the default data types for this polymorphic function.


     Inputs/Outputs

            •      use system decimal point (T) —

          use system decimal point defines the decimal separator. If TRUE (default), the decimal
           separator uses the localized decimal separator. If FALSE, the decimal separator is a period.

            •     number —

        number can be a scalar number, array or cluster of numbers, array of clusters of numbers, and
          so on.

            •      width (-) —

          width must be numeric. If unwired, the function uses exactly as many digits as are needed to
           represent the number, with no extra padding.

            •       precision (6) —

           precision must be numeric. The function rounds the number of digits after the decimal point of
          the output string to precision.

            •      F-format string —

          F-format string is the resulting fractional string. F-format string can be Inf, -Inf, or NaN if the
           value you wire to number is infinity or is not a number. The following table shows how the
           values of number, width, and precision affect F-format string. In this table, the underline
           character ( _ ) represents a space in F-format string.

        number width precision F-format string Comments
           4.925   6    2       _ _4.92       number is rounded, padded with spaces on the left.
          .003926 8    4       _ _0.0039     number is rounded, padded with spaces on the left.
           –287.3  5    0        _–287        number is rounded, padded with spaces on the left.


686   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:686 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:687 ordinal=687 -->
## Functions

Functions

This function rounds number to the nearest integer. If the fractional part of number is
.5, the function rounds the value to the nearest even integer. For example, the
function rounds 13.5 to 14 and rounds 14.5 to 14.

NumberNumber ToTo ExponentialExponential StringString FunctionFunction

Converts number to an E-format (exponential notation), floating-point string at least
width characters wide or wider if necessary.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      use system decimal point (T) —

    use system decimal point defines the decimal separator. If TRUE (default), the decimal
    separator uses the localized decimal separator. If FALSE, the decimal separator is a period.

   •     number —

   number can be a scalar number, array or cluster of numbers, array of clusters of numbers, and
    so on.

   •      width (-) —

    width must be numeric. If unwired, the function uses exactly as many digits as are needed to
    represent the number, with no extra padding.

   •       precision (6) —

    precision must be numeric. The function rounds the number of digits after the decimal point of
    the output string to precision.

   •      E-format string —

    E-format string is the resulting string. The following table shows how the values of number,
    width, and precision affect E-format string. In this table, the underline character ( _ ) represents


                                                    © National Instruments 687

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:687 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:688 ordinal=688 -->
## Functions

Functions


         a space in E-format string.

        number width precision E-format string Comments
           4.911   5    2        4.91e0       number is rounded, width is extended.
          .003926 10   2       _ _ _3.93e–3   number is rounded, padded with spaces on the left.
          216.01  5    0       _ _2e2       number is rounded, padded with spaces on the left.


    NumberNumber ToTo EngineeringEngineering StringString FunctionFunction

     Converts number to an engineering format, floating-point string at least width
      characters wide or wider if necessary.

     Engineering format is similar to E format (exponential notation), except the exponent
       is a multiple of three (..., –3, 0, 3, 6, ...). The connector pane displays the default data
     types for this polymorphic function.


     Inputs/Outputs

            •      use system decimal point (T) —

          use system decimal point defines the decimal separator. If TRUE (default), the decimal
           separator uses the localized decimal separator. If FALSE, the decimal separator is a period.

            •     number —

        number can be a scalar number, array or cluster of numbers, array of clusters of numbers, and
          so on.

            •      width (-) —

          width must be numeric. If unwired, the function uses exactly as many digits as are needed to
           represent the number, with no extra padding.

            •       precision (6) —


688   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:688 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:689 ordinal=689 -->
## Functions

Functions


    precision must be numeric. The function rounds the number of digits after the decimal point of
    the output string to precision.

   •      Engineering string —

    Engineering string is the resulting string.

    The following table shows how the values of number, width, and precision affect Engineering
     string. In this table, the underline character ( _ ) represents a space in Engineering string.

   number width precision Engineering string Comments
    4.93    10   2       _ _ _4.93E+0     number is rounded, padded with spaces on the left.
     .49     10   2        _490.00E-3      number is rounded, padded with a space on the left.
    61.96   8    1        _62.0E+0       number is rounded, padded with a space on the left.
    1789.32 8    2       _ 1.79E+3       number is rounded, padded with a space on the left.


FormatFormat ValueValue FunctionFunction

Converts a number into a regular string according to the format specified in format
string and appends this to string.

The connector pane displays the default data types for this polymorphic function.

      Note The Format Into String function has the same functionality as Format
       Value but can use multiple inputs. Consider using Format Into String instead
        of this function to simplify your block diagram.


Inputs/Outputs

   •       string ("") —

     string is the input string to which LabVIEW appends the formatted string. The default is an
    empty string.


                                                    © National Instruments 689

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:689 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:690 ordinal=690 -->
## Functions

Functions

            •      format string —

          format string specifies how to convert value into output string.

         Use the format string syntax.
            •      value (0) —

          value must be numeric but can be a physical quantity. A physical quantity is a value with a unit.

            •      output string —

          output string is the result of converting value to a string, and appending this to string.


     DecimalDecimal StringString ToTo NumberNumber FunctionFunction

     Converts the numeric characters in string, starting at offset, to a decimal integer and
      returns it in number.

     The connector pane displays the default data types for this polymorphic function.

         If you want the function to return a 64-bit integer output, you must wire a 64-bit
      integer to the default input.


     Inputs/Outputs

            •       string —

           string can be a string, a cluster of strings, an array of strings, or an array of clusters of strings.

            •       offset —

            offset specifies number of characters into string at which the function starts searching for a
          match. offset must be numeric.

         The offset of the first character in string is 0. If offset is unwired or less than 0, the function takes
            offset as 0.


690   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:690 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:691 ordinal=691 -->
## Functions

Functions

   •       default (0 I32) —

    default is any object of numeric representation and specifies the numeric representation for
    number. The default is a 32-bit signed integer value of 0.

   •       offset past number —

     offset past number is the index in string of the first character following the number. offset past
   number reflects the value from the last string if you input an array of strings.

   •     number —

   number can be a number, a cluster, or an array of numbers, depending on the structure of
     string.

       If number is an integer, it can overflow if the input is out of range. In that case, number is set to
    the maximum or minimum value for the data type. For example, if the input string is 300, and the
    data type is a 8-bit signed integer, LabVIEW sets the value to 127. The following table shows how
    the values of string, offset, and default affect number.

                                offset past     string       offset default         number Comments                       number
    13ax       0    0     2         13   —
    –4.8bcde                                Because an integer is being converted,               0    0     2          –4
    conversion                                 conversion stops at the decimal point.
    a49b       0    –9    0          –9      default is used since no digits were read.


HexadecimalHexadecimal StringString ToTo NumberNumber FunctionFunction

Interprets the characters 0 through 9, A through F, and a through f in string starting at
offset as a hex integer and returns it in number.

The connector pane displays the default data types for this polymorphic function.


                                                    © National Instruments 691

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:691 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:692 ordinal=692 -->
## Functions

Functions

     Inputs/Outputs

            •       string —

           string can be a string, a cluster of strings, an array of strings, or an array of clusters of strings.

            •       offset —

            offset specifies number of characters into string at which the function starts searching for a
          match. offset must be numeric.

         The offset of the first character in string is 0. If offset is unwired or less than 0, the function takes
            offset as 0.

            •       default (0 U32) —

           default is any object of numeric representation and specifies the numeric representation for
         number. The default is a 32-bit unsigned integer value of 0. To return a 64-bit integer output,
           wire a 64-bit integer to default.

            •       offset past number —

            offset past number is the index in string of the first character following the number.

            offset past number reflects the value from the last string if you input an array of strings.

            •     number —

        number can be a number, a cluster, an array of numbers, or an array of clusters depending on
          the structure of string and offset.

                 If the input string represents a number outside the range of the representation of number,
        number is set to the maximum value for that data type.


     The following table illustrates how string, offset, and default affect number.


                                     offset
        string      offset  default past    number    Comments
                           number

                                                The conversion starts from the first character
      3ab       0             3       939
                                                                   3, as offset specifies.


692   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:692 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:693 ordinal=693 -->
## Functions

Functions


                              offset
 string      offset  default past    number    Comments
                      number

                                          The conversion starts from the third character 3ab       2             3       11                                                        b, as offset specifies.

                                       number is a 32-bit unsigned integer, as default
                                                         specifies. The result of the conversion is 1FFFFFFFF 0             9       4294967295                                                  saturated because it is too large to be
                                                  represented.

                                       number is a 64-bit unsigned integer, as default 1FFFFFFFF 0             9       8589934591                                                         specifies.

                                            g is not a valid hex character, so conversion
                                                 stops there. The value of offset past number f3g        0             2       243                                                     indicates the conversion stops at the third
                                                  character g.

 –30       0             0       0           Negative numbers are not permitted for hex.

OctalOctal StringString ToTo NumberNumber FunctionFunction

Interprets the characters 0 through 7 in string starting at offset as an octal integer and
returns it in number. This function also returns the index in string of the first character
following the number.

The connector pane displays the default data types for this polymorphic function.

If you want the function to return a 64-bit integer output, you must wire a 64-bit
integer to the default input.


Inputs/Outputs

   •       string —

     string can be a string, a cluster of strings, an array of strings, or an array of clusters of strings.


                                                    © National Instruments 693

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:693 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:694 ordinal=694 -->
## Functions

Functions

            •       offset —

            offset specifies number of characters into string at which the function starts searching for a
          match. offset must be numeric.

         The offset of the first character in string is 0. If offset is unwired or less than 0, the function takes
            offset as 0.
            •       default (0 U32) —

           default is any object of numeric representation and specifies the numeric representation for
         number. The default is a 32-bit unsigned integer value of 0. To return a 64-bit integer output,
           wire a 64-bit integer to default.

            •       offset past number —

            offset past number is the index in string of the first character following the number.

            offset past number reflects the value from the last string if you input an array of strings.
            •     number —

        number can be a number, a cluster, an array of numbers, or an array of clusters, depending on
          the structure of string.

                 If the input string represents a number outside the range of the representation of number,
        number is set to the maximum value for that data type. The following table shows how the
           values of string, offset, and default affect number.

            string offset default offset past number number Comments
          92   0    0     0                0      9 is not an octal digit.
          071a 0    0     3                57     a is not an octal digit, so conversion stops there.


     Fract/ExpFract/Exp StringString ToTo NumberNumber FunctionFunction

      Interprets the characters 0 through 9, plus, minus, e, E, and the decimal point (usually
      period) in string starting at offset as a floating-point number in engineering notation,
      exponential, or fractional format and returns it in number.

     The connector pane displays the default data types for this polymorphic function.


694   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:694 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:695 ordinal=695 -->
## Functions

Functions


Inputs/Outputs

   •      use system decimal point (T) —

    use system decimal point defines the decimal separator.

       If TRUE (default), the decimal separator uses the localized decimal separator. If FALSE, the
    decimal separator is a period.
   •       string —

     string can be a string, a cluster of strings, an array of strings, or an array of clusters of strings.

       If string contains the characters Inf or NaN, this function returns the LabVIEW values Inf and
    NaN, respectively.
   •       offset —

     offset specifies number of characters into string at which the function starts searching for a
    match. offset must be numeric.

    The offset of the first character in string is 0. If offset is unwired or less than 0, the function takes
     offset as 0.
   •       default (0 DBL) —

    default is any object of numeric representation and specifies the numeric representation for
    number.

    The default is a double-precision, floating-point value of 0.
   •       offset past number —

     offset past number is the index in string of the first character following the number.

     offset past number reflects the value from the last string if you input an array of strings.
   •     number —

   number can be a number, a cluster, an array of numbers, or an array of clusters, depending on
    the structure of string.

    The following table shows how the values of string, offset, and default affect number.


                                                    © National Instruments 695

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:695 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:696 ordinal=696 -->
## Functions

Functions


                                   offset past            string   offset default            number Comments
                         number
          –4.7e–3x 0    0     7             –0.0047 x is not allowed, so conversion stops there.
                                               Second decimal point not allowed, so conversion            +5.3.2  0    0     4               5.3                                                      stops there.

                 If you scan a string that does not fit into the numeric data type you specify, this function returns
          the largest number that fits into that data type.


         If you want the function to return a 64-bit integer output, you must wire a 64-bit
      integer to the default input.

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Strings\Extract Numbers with Match
       Pattern.vi

    ScanScan ValueValue FunctionFunction

     Converts characters at the beginning of string to the data type represented by default,
     according to the conversion codes in format string, and returns the converted number
      in value and the remainder of string after the match in output string.

     The connector pane displays the default data types for this polymorphic function.


     Inputs/Outputs

            •       string —

           string is the input string the function scans.

            •      format string —

696   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:696 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:697 ordinal=697 -->
## Functions

Functions


    format string specifies how to convert the input arguments into value.

    Use the format string syntax.
   •       default (0 dbl) —

    default is the numeric representation for value.

    The default is a double-precision, floating-point value of 0.
   •      output string —

    output string is the remaining characters in string after the match or string if there is no match.

   •      value —

    value is the converted value or the value in default if there is no match.

       If value is an integer, it can overflow if the input is out of range. In that case, value is set to the
   maximum or minimum value for the data type. For example, if the input string is 300 and the
    data type is an 8-bit signed integer, LabVIEW sets the value to 127.

SpreadsheetSpreadsheet StringString ToTo ArrayArray FunctionFunction

Converts the spreadsheet string to an array of the dimension and representation of
array type. This function works for arrays of strings and arrays of numbers.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •       delimiter (Tab) —

    delimiter specifies the value or values used to separate fields in the spreadsheet file. The default
      is a single tab character. You can specify multiple delimiters by wiring an array of strings to
     delimiter. Each element of the array should contain a different delimiter.

    For example, if you wire an array that contains two elements — a space character in one and a
    tab character in the other — the function allows either a space character or a tab character to

                                                    © National Instruments 697

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:697 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:698 ordinal=698 -->
## Functions

Functions

           separate elements in the output array.
            •      format string —

          format string specifies how to convert the spreadsheet string into an array. Use %s to convert
          spreadsheet string to an array of strings. Use %d or %f to convert spreadsheet string to an array
           of numbers.

         Use the format string syntax.
            •      spreadsheet string —

          spreadsheet string contains numeric or string values separated into columns by delimiters, such
          as tabs or commas, with an end-of-line (EOL) character separating rows.

         The function converts each element in spreadsheet string according to format string and stores
          the resulting values in array.
            •      array type (2D Dbl) —

           array type is the data type input for the array. The default is a 2D array of double-precision,
            floating-point numbers.

           Refer to Array To Spreadsheet String for information about the spreadsheet format expected for
           arrays of three dimensions or more.
            •      array —

           array is spreadsheet string converted to an array of the dimension and representation of array
           type.


    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\File IO\Spreadsheet\Tab-Delimited Data\
       Tab-Delimited Data.lvproj

     ArrayArray ToTo SpreadsheetSpreadsheet StringString FunctionFunction

     Converts an array of any dimension to a table in string form, containing tabs
      separating column elements, a platform-dependent EOL character separating rows,
     and, for arrays of three or more dimensions, headers separating pages.


698   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:698 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:699 ordinal=699 -->
## Functions

Functions


Inputs/Outputs

   •       delimiter (Tab) —

     delimiter is the value used to separate fields in the spreadsheet file. The default is a single tab
     character.

   •      format string —

    format string specifies how to convert the input array into a string. Use %s to convert an array of
     strings to spreadsheet string. Use %d or %f to convert arrays of numbers to spreadsheet string.

    Use the format string syntax.

          Note This function allows you to use only a single format specifier to format all
            elements of an array. You cannot wire multiple specifiers to this function to format
          some array elements according to one specifier and some elements to a different
                specifier.

   •      array —

    array specifies the input samples.

   •      spreadsheet string —

    spreadsheet string is separated into columns by delimiters, such as tabs, and an end-of-line
    (EOL) character separates rows.


For arrays of three dimensions or more, each page is preceded by a series of indexes of
the following format.

[n,m,…,0,0]

where nis the highest dimension index, mis the next highest dimension index, a
comma (,) separates indexes, 0,0 refers to the first row and column elements of page
n,m,…, and  represents the end-of-line character.


                                                    © National Instruments 699

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:699 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:700 ordinal=700 -->
## Functions

Functions

      In the following example, a spreadsheet string of a 4x4x3 array appears as it does when
     you print it. The period character (.) represents omitted values of the latter pages, and
     the end-of-line character ( ) does not appear in an actual printout.


     [0,0,0]


     1.3                              2.6                  5.7


     3.9                              –4.2                 6.5


     –5.5                             9.3                  3.3


     9.6                              9.8                  0.4


     [1,0,0]


     .                                .                    .


     .                                .                    .


     .                                .                    .


     .                                .                    .


     [2,0,0]


     .                                .                    .

700   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:700 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:701 ordinal=701 -->
## Functions

Functions


 .                                .                    .


 .                                .                    .


 .                                .                    .


 [3,0,0]


 .                                .                    .


 .                                .                    .


 .                                .                    .


 .                                .                    .


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Arrays\Array to Spreadsheet String.vi

ToTo UpperUpper CaseCase FunctionFunction

Converts all alphabetic characters in string to uppercase characters. Evaluates all
numbers in string as ASCII codes for characters. This function does not affect non-
alphabetic characters.


                                                    © National Instruments 701

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:701 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:702 ordinal=702 -->
## Functions

Functions

     The connector pane displays the default data types for this polymorphic function.


     Inputs/Outputs

            •       string —

           string can be a string, a cluster of strings, an array of strings, or an array of clusters of strings.

            •        all upper case string —

             all upper case string has the same structure as string.


         If string is a numeric value or an array of numeric values, each number is evaluated as
     an ASCII value. The To Upper Case function translates all values in the range of 97 to
     122 into values over the range of 65 to 90. It also translates any other value in the
     extended ASCII character set that has an uppercase counterpart, such as lowercase
     alphabetic characters with accents.

    ToTo LowerLower CaseCase FunctionFunction

     Converts all alphabetic characters in string to lowercase characters. Evaluates all
     numbers in string as ASCII codes for characters. This function does not affect non-
     alphabetic characters.

     The connector pane displays the default data types for this polymorphic function.


     Inputs/Outputs

            •       string —

           string can be a string, a cluster of strings, an array of strings, or an array of clusters of strings.

            •        all lower case string —

702   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:702 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:703 ordinal=703 -->
## Functions

Functions


     all lower case string has the same structure as string.


If string is a numeric value or an array of numeric values, each number is evaluated as
an ASCII value. The To Lower Case function translates all values in the range of 65 to 90
into values over the range of 97 to 122. It also translates any other value in the
extended ASCII character set that has a lowercase counterpart, such as uppercase
alphabetic characters with accents.

Flatten/UnflattenFlatten/Unflatten StringString

Use the Flatten/Unflatten String functions to flatten and unflatten LabVIEW data types
to and from strings.


 Palette              Description Object

 Flatten To    Converts the anything input to a flattened data string of binary values. You also can
 String       use this function to convert the byte order, or endian format, of the data in the
 Function      flattened data string.

 Unflatten     Converts binary string to the type wired to type. binary string should contain
 From String   flattened data of the type wired to type. You also can use this function to specify the
 Function     byte order, or endian format, of the data in the binary string.

 Variant To
 Flattened    Converts variant data into a flattened string and an array of integers that represent
 String        the data type. You cannot flatten ActiveX variant data.
 Function

 Flattened
 String To
              Converts flattened data into variant data.
 Variant
 Function

 Flatten To
              Converts any data type you wire to anything and converts it to an XML string
 XML
              according to the LabVIEW XML schema.
 Function


                                                    © National Instruments 703

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:703 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:704 ordinal=704 -->
## Functions

Functions


       Palette                     Description
       Object

       Unflatten                    Converts an XML string to a LabVIEW data type according to the LabVIEW XML      From XML                  schema.       Function

        Flatten To                    Converts data you wire to the anything input to a UTF-8 JavaScript Object Notation     JSON                   (JSON) string.       Function

       Unflatten                    Converts a UTF-8 JavaScript Object Notation (JSON) string to the LabVIEW data type
      From JSON                  you wire to type/defaults.       Function

     FlattenFlatten ToTo StringString FunctionFunction

     Converts the anything input to a flattened data string of binary values. You also can
     use this function to convert the byte order, or endian format, of the data in the
      flattened data string.


     Inputs/Outputs

            •      anything —

          anything contains the data you want to convert to a UTF-8 JSON string. This input accepts arrays
         and clusters of Booleans, floating-point numbers, and strings. anything can also accept an array
           of clusters, or a cluster of arrays, of these data types. This input does not support other data
           types, such as enums, refnums, file paths, and fixed-point numbers.

           Cluster elements may be named or unnamed, but not a combination of both. If cluster elements
           are named, then each name must be unique to that cluster. If you wire an unsupported data
           type, LabVIEW breaks the VI.

            •      prepend array or string size? (T) —

         prepend array or string size? specifies whether LabVIEW includes data size information at the


704   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:704 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:705 ordinal=705 -->
## Functions

Functions


  beginning of data string when anything is an array or string. If prepend array or string size? is
  FALSE, LabVIEW does not include the size information. The default is TRUE.

  The string created by the Flatten To String function is a LabVIEW string. If prepend array or
  string size? is TRUE, the LabVIEW string has a 4-byte (I32) number at the beginning of the string
  that tells how long the string is. This enables a LabVIEW string to include NULL characters [ASCII
  character zero (0)]. If you pass a LabVIEW string to external code and use it as a C string, NULL
  characters embedded in the string may cause problems, since C strings are interpreted as
  terminating at the first NULL character. prepend array or string size? only controls the top-level
  data size information. Arrays and strings in hierarchical data types such as clusters always
  include size information.

•      byte order (0:big-endian, network order) —

  byte order sets the endian format of the data in the resulting flattened string. Byte order, or
  endian form, indicates whether integers are represented in memory from most significant byte
  to least significant byte or vice versa.

   big-endian, network order (default)—The most significant byte occupies the lowest memory
  0    address.
  1 native, host order—Uses the byte-ordering format of the host computer.
  2 little-endian—The least significant byte occupies the lowest memory address.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      data string —

  data string is the flattened data generated by the function.

  data string might contain header information before each non-scalar component describing its
   size. Such a string can be stored in a file or sent over a network. If you send the string over a
  network, the receiver must be able to interpret it. Usually, LabVIEW stores data as
  noncontiguous, indirectly referenced pieces. This function copies the data in LabVIEW form into
  a contiguous buffer data string. Use the Unflatten From String function to convert a data string
  back to any data type.

•      type string (7.x only) —

  type string (7.x only) is visible only if the terminal is already wired from a previous version of


                                                   © National Instruments 705

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:705 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:706 ordinal=706 -->
## Functions

Functions


         LabVIEW or if you right-click the function and select Convert 7.x Data from the shortcut menu.
          type string (7.x only) is an encoded binary description of data string. type string (7.x only) is
          not the same as the type input in the Unflatten From String function.

                 If type string (7.x only) cannot represent the data type wired to anything, this function returns
         an error.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


     Use the Type Cast function for conversion of data types that does not result in
      flattened data.

         If you need to flatten type descriptor data to a string that is readable by LabVIEW 7.xor
       earlier, right-click this function and select Convert 7.x Data from the shortcut menu. In
     Convert 7.x Data mode, this function shows the type string (7.x only) output and
      displays the icon for this function with a red 7.x on it. LabVIEW 7.xand earlier stores
     type descriptors in 16-bit flat representation. LabVIEW 8.0 and later stores type
      descriptors in 32-bit flat representation. National Instruments recommends reworking
     any application that uses the Convert 7.x Data mode as a long term solution.

         If you need to flatten Boolean data to a string that is readable by LabVIEW 4.xor
       earlier, right-click this function and select Convert 4.x Data from the shortcut menu.
     The Convert 4.x Data shortcut menu item is visible only if you wire Boolean data to
     anything. In Convert 4.x Data mode, this function writes the data in LabVIEW 4.xdata
      storage layout and displays the icon for this function with a red 4.x on it. LabVIEW 4.x
     and earlier stores Boolean data in two bytes unless the data is in an array, in which
     case LabVIEW stores each Boolean element in a single bit. LabVIEW 5.0 and later stores
     Boolean values in a single byte, regardless of whether it is in an array. National
     Instruments recommends reworking any application that uses the Convert 4.x Data
    mode as a long term solution.

         If you use this function to flatten variant data, LabVIEW flattens the variant and all its
      contents, including attributes. However, if you use the Variant To Flattened String
      function, LabVIEW flattens only the variant and discards any attributes.


706   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:706 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:707 ordinal=707 -->
## Functions

Functions

If you use this function to flatten data from a custom control or indicator that you
saved as a type definition, the function strips the type definition of its type definition
wrapper. If you do not want to strip this wrapper, right-click the function and select
Expose Typedefs from the shortcut menu. The Expose Typedefs shortcut menu item is
visible only if you wire data to type string (7.x only).

UnflattenUnflatten FromFrom StringString FunctionFunction

Converts binary string to the type wired to type. binary string should contain
flattened data of the type wired to type. You also can use this function to specify the
byte order, or endian format, of the data in the binary string.


Inputs/Outputs

   •      type —

    type is a normally constructed LabVIEW type.

    type is not the type string output in the Flatten To String function.

   •      binary string —

    binary string is a flattened string that is typically generated by the Flatten To String function.

       If data includes array or string size? is TRUE, binary string contains header information
    describing its size.

   •      data includes array or string size? (T) —

    data includes array or string size? indicates whether LabVIEW reads data size information from
    the beginning of an incoming array or string. If data includes array or string size? is TRUE,
    LabVIEW reads the size information from the beginning of binary string. If data includes array or
     string size? is FALSE, LabVIEW detects the size information from the memory size of binary
     string.


                                                    © National Instruments 707

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:707 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:708 ordinal=708 -->
## Functions

Functions


         The default is TRUE. data includes array or string size? only accesses the top-level data size
           information. Arrays and strings in hierarchical data types such as clusters always include size
           information.

            •      byte order (0:big-endian, network order) —

          byte order indicates the endian format of the data in the incoming flattened string. Byte order,
           or endian form, indicates whether integers are represented in memory from most-significant
          byte to least-significant byte or vice versa.

            big-endian, network order (default)—The most-significant byte occupies the lowest memory          0            address.
          1 native, host order—Uses the byte-ordering format of the host computer.
          2 little-endian—The least-significant byte occupies the lowest memory address.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •       rest of the binary string —

            rest of the binary string contains any leftover bytes that this function did not convert. This
           function does not convert all the bytes if the size of binary string is not a multiple of the size of
           type.

            •      value —

          value returns binary string as unflattened data of the same data type and structure as type.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


     Use the Type Cast function for conversion of data types that does not require already-
      flattened data.

         If you need to unflatten data from a string created by LabVIEW 4.xor earlier, right-click
      this function and select Convert 4.x Data from the shortcut menu. In Convert 4.x Data
     mode, this function interprets the data in LabVIEW 4.xdata storage layout and displays


708   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:708 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:709 ordinal=709 -->
## Functions

Functions

the icon for this function with a red 4.x on it. LabVIEW 4.xand earlier stores Boolean
data in two bytes unless the data is in an array, in which case LabVIEW stores each
Boolean element in a single bit. LabVIEW 5.0 and later stores Boolean values in a single
byte, regardless of whether it is in an array. National Instruments recommends
reworking any application that uses the Convert 4.x Data mode as a long term
solution.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\Binary\Endian Considerations\
   Endian Considerations with Binary Files.vi
  • labview\examples\Strings\Unflatten from String with
   Little-Endian Data.vi

VariantVariant ToTo FlattenedFlattened StringString FunctionFunction

Converts variant data into a flattened string and an array of integers that represent the
data type. You cannot flatten ActiveX variant data.


Inputs/Outputs

   •       variant —

    variant is the variant data you want converted to a string of flattened data.

   •      type string —

    type string is an array of numeric integers that identifies the data type of the flattened string.

   •      data string —

    data string is the resulting flattened data you converted from variant data.


                                                    © National Instruments 709

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:709 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:710 ordinal=710 -->
## Functions

Functions

         If you use this function to flatten variant data, LabVIEW flattens only the variant and
      discards all its contents, including attributes. However, if you use the Flatten To String
      function, LabVIEW flattens the variant and all of its attributes.

     FlattenedFlattened StringString ToTo VariantVariant FunctionFunction

     Converts flattened data into variant data.

     Use the Flatten to String function to produce data string and type string.


     Inputs/Outputs

            •      type string —

          type string is an array of numeric integers that identifies the data type of the flattened string if
          the data type existed in LabVIEW 7.x or earlier.

            •      data string —

          data string is the flattened data you want to convert to variant data.

            •       error in —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •       variant —

           variant is the resulting variant data.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


     FlattenFlatten ToTo XMLXML FunctionFunction

     Converts any data type you wire to anything and converts it to an XML string according

710   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:710 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:711 ordinal=711 -->
## Functions

Functions

to the LabVIEW XML schema.

If anything contains the characters <, >, or &, the function converts those characters to
&lt;, &gt;, or &amp;, respectively. Use the Escape XML VI to convert other
characters, such as ", to XML syntax.


Inputs/Outputs

   •      anything —

    anything is any LabVIEW data you want to convert. This parameter is polymorphic.

   •     xml string —

    xml string is the resulting XML string that represents the LabVIEW data type.

   When converting decimal values, this function uses only the period (.) as a decimal separator.
    The function does not use localized decimal separators.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\XML\Flatten and Unflatten XML\
   Flatten and Unflatten XML.lvproj

UnflattenUnflatten FromFrom XMLXML FunctionFunction

Converts an XML string to a LabVIEW data type according to the LabVIEW XML schema.

If xml string contains the characters &lt;, &gt;, or &amp;, the function converts
those characters to <, >, or &, respectively. Use the Unescape XML VI to convert other
characters, such as ".


                                                    © National Instruments 711

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:711 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:712 ordinal=712 -->
## Functions

Functions


     Inputs/Outputs

            •     xml string —

         xml string is the XML string that includes the data you want to convert.

         xml string must conform to the LabVIEW XML schema, including the case and order of tags in the
         schema. If xml string does not conform to the schema, the function returns an error and value
           contains the default value for the data type wired to type. If the VI containing the function
           previously completed execution, value contains the value from the previous execution.

            In xml string, this function accepts only the period (.) as a decimal separator. The function does
          not recognize localized decimal separators. This restriction prevents errors when you use XML
            strings on operating systems with different settings for the decimal separator.

            •      type —

          type is the data type to which you want to convert xml string.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •      value —

          value is the data type you specified in type and the data in xml string.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


     FlattenFlatten ToTo JSONJSON FunctionFunction

     Converts data you wire to the anything input to a UTF-8 JavaScript Object Notation
     (JSON) string.


712   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:712 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:713 ordinal=713 -->
## Functions

Functions


Inputs/Outputs

   •      enable LabVIEW extensions? (T) —

    enable LabVIEW extensions enables LabVIEW JSON extensions to support NaN and Inf values
     of floating-point numbers. Not all JSON parsers support these extensions.

   •      anything —

    anything contains the data you want to convert to a UTF-8 JSON string. This input accepts arrays
    and clusters of Booleans, floating-point numbers, and strings. anything can also accept an array
     of clusters, or a cluster of arrays, of these data types. This input does not support other data
     types, such as enums, refnums, file paths, and fixed-point numbers.

     Cluster elements may be named or unnamed, but not a combination of both. If cluster elements
    are named, then each name must be unique to that cluster. If you wire an unsupported data
     type, LabVIEW breaks the VI.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     JSON string —

   JSON string is the flattened data encoded in UTF-8. UTF-8 encoded strings may not display
     correctly in LabVIEW controls.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


UnflattenUnflatten FromFrom JSONJSON FunctionFunction

Converts a UTF-8 JavaScript Object Notation (JSON) string to the LabVIEW data type
you wire to type/defaults.


                                                    © National Instruments 713

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:713 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:714 ordinal=714 -->
## Functions

Functions


     Inputs/Outputs

            •      enable LabVIEW extensions? (T) —

          enable LabVIEW extensions enables LabVIEW JSON extensions to support NaN and Inf values
           of floating-point numbers. Not all JSON parsers support these extensions.

            •      path —

          path identifies a specific item in JSON string. Use path if your JSON string contains multiple
           items, and you would like to extract a specific item from it. path uses an array of strings to
            identify the item, where each element in the array references either the name of a cluster
          element or an integer index of an array.

                 If you specify an item using path, you must wire a data type to type/defaults that corresponds to
          the data type of the specified item.

          For example, consider the JSON string {"0":"abc","1":false,"2":[9,8,7]}. The
           following table illustrates the type/defaults inputs required for various paths and the resulting
          value outputs.

          path      type/defaults value         Comments
                            A cluster
                                                                                 If path is empty, type/defaults must account for each                                   containing string
                                              element in the JSON string. For the example JSON      —                   abc, Boolean
                                                            string, you must wire a cluster containing a string, a
                                 FALSE, and array
                                                Boolean, and an array to type/defaults.
                          [9,8,7]
                                                       In this example, the path points to the cluster
                                     String abc     element named 0, or string abc. Therefore, you must
                                                  wire a string to type/defaults.
                                                       In this example, the path points to the cluster
                                              element named 2, which is an array, and the element
                           DBL numeric 9   at index 0 of that array. This element is a floating-
                                                  point number, so a DBL numeric must be wired to
                                                    type/defaults.

            •     JSON string —

714   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:714 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:715 ordinal=715 -->
## Functions

Functions


  JSON string is the flattened UTF-8 string that you want to unflatten. You can use the Flatten To
  JSON function to generate this string.

•      type and defaults —

  type/defaults specifies the data type and default values to which you want to unflatten the
  JSON string. This input accepts Booleans, integers, floating-point numbers, strings, and arrays
  or clusters of these types. Cluster elements may be labeled or unlabeled, but not a combination
  of both. If the elements in a cluster are labeled, then each name must be unique to that cluster. If
  you wire an unsupported data type, LabVIEW breaks the VI.

   If the elements in your JSON string are labeled, the elements wired to types/defaults must have
  an identical label. For example, if you have JSON string
  {"firstelement":"a","secondelement":"b"}, you must wire a cluster containing a
  string labeled firstelement and a string labeled secondelement. Additionally, if you
  specify the path to a particular item in your JSON string, the data type wired to type/defaults
  must match the data type of the item pointed to by path.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•       default null elements? (F) —

  default null elements specifies whether LabVIEW uses default values from the input cluster for
  null values in JSON. If default null elements is FALSE, LabVIEW returns an error for null values.

•        strict validation? (F) —

   strict validation determines whether LabVIEW returns an error when the JSON object contains
  items not defined in the input cluster. If strict validation is FALSE, JSON objects may contain
  items not defined in the cluster.

•      value —

  value returns JSON string as unflattened data of the same data type and structure as type/
  defaults.

•       error out —

  error out contains error information. This output provides standard error out functionality.


                                                   © National Instruments 715

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:715 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:716 ordinal=716 -->
## Functions

Functions

         If JSON string represents a data type that type/defaults does not accept, such as an
      array of arrays or an array of mixed types, you cannot use a single Unflatten From
    JSON function to convert the entire JSON string. However, you can use path to identify
     and extract items in the JSON string.

     StringString ConstantConstant

     Use this constant to supply a constant text string to the block diagram.

     Set the value of a string constant by using the Operating tool or the Labeling tool to
      click it and enter the string you want. You also can set the value of a string constant by
      right-clicking the constant and selecting Edit to display the Edit dialog box for string
      constants.

     Press the <Shift-Enter> keys on the keyboard to disable autosizing if it is enabled. If
      autosizing is disabled, press the <Shift-Enter> keys on the keyboard to display a scroll
     bar in the constant. If autosizing is disabled and the vertical scroll bar is not visible, the
     constant resizes vertically as you enter text in the constant. Resizing a string constant
     smaller than its contents displays the vertical scroll bar. If the vertical scroll bar is
      visible and you resize the constant larger than its contents, LabVIEW hides the scroll
      bar.

     You can change the display mode so you can see non-displayable characters or the hex
      ASCII equivalent to the characters. You also can set the constant in password display
    mode so asterisks are displayed when you type in characters. Right-click a string
     constant and select Visible Items»Display Style from the shortcut menu to display a
     glyph on the constant that indicates the display type.

     You cannot change the value of the string constant while the VI runs. You can assign a
      label to this constant.


    EmptyEmpty StringString ConstantConstant

      Consists of a constant string that is empty (length zero).


716   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:716 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:717 ordinal=717 -->
## Functions

Functions


SpaceSpace ConstantConstant

Use this constant to supply a one-character space string to the block diagram.


Inputs/Outputs

   •       String —

    Space constant string.

TabTab ConstantConstant

Consists of a constant string containing the ASCII HT (horizontal tab) value.

Use this constant when you do not want to type in the backslash code for the
character.


AdditionalAdditional StringString FunctionsFunctions

Use the Additional String VIs and functions to scan and search in strings, match
patterns, and manipulate strings.


                                                    © National Instruments 717

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:717 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:718 ordinal=718 -->
## Functions

Functions


       Palette                  Description
       Object

       Search/
        Split                  Divides a single string into two substrings.        String
       Function

       Pick Line                Chooses a line from multi-line string and appends that line to string.       Function

      Match               Compares each prefix string in string array to the beginning of string until it encounters
         First                a match. This function returns the original input string with the matching prefix string        String                removed.       Function

      Match
       True/     Examines the beginning of string to see whether it matches true string or false string.
       False      This function returns a Boolean TRUE or FALSE value in selection, depending on
        String     whether string matches true string or false string.
       Function

      Scan
        String For Scans input string starting at offset for tokens and outputs each segment as a token
      Tokens     string.
       Function

                 Searches string for substrings that match regular expression and replaces those       Search
                  substrings with replace string. A regular expression requires a specific combination of      and                  characters for pattern matching. For more information about special characters in       Replace
                   regular expressions, refer to the regular expression input description in the detailed       Pattern
                   help.

       Index
        String
                   Selects a string specified by index from string array and appends that string to string.
       Array
       Function

      Append
       True/
                   Selects either a FALSE or TRUE string according to a Boolean selector and appends that
       False
                    string to string.
        String
       Function

       Rotate     Places the first character of string in the last position of first char last, shifting the other


718   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:718 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:719 ordinal=719 -->
## Functions

Functions


 Palette           Description
 Object

 String            characters forward one position. For example, the string abcd becomes bcda. Function

 Reverse
 String     Produces a string whose characters are in reverse order of those in string.
 Function

 Delimited
 String to   Converts substrings in a delimited string to the elements of a one-dimensional string
 1D String  array.
 Array

 1D String
 Array to   Converts the elements of a one-dimensional string array to a single string with input
 Delimited  array elements separated by a delimiting character.
 String

 Create NI           Generates a globally unique identifier (GUID) string. GUID

Search/SplitSearch/Split StringString FunctionFunction

Divides a single string into two substrings.

You can divide the string at a certain character or substring. Search/Split String
searches string for the string or character in search string/char. The function splits the
string and returns the resulting two strings in substring before match and match +
rest of string.


Inputs/Outputs

   •       string —

     string is the input string the function searches or splits.


                                                    © National Instruments 719

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:719 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:720 ordinal=720 -->
## Functions

Functions

            •      search string/char (-) —

          search string/char is the string or character to search for in string. If you do not wire this input or
                it contains an empty string, the function splits string at offset. You must wire either search char
           or offset.

            •       offset (0) —

            offset specifies number of characters into string at which the function starts searching for a
          match. offset must be numeric. The offset of the first character in string is 0. If offset is unwired
           or less than 0, the function takes offset as 0.

            •      substring before match —

           substring before match returns the portion of string before search string/char or before offset if
          search string/char is unwired. If this function does not find the search string, substring before
         match returns the entire original string.

            •     match + rest of string —

         match + rest of string consists of search string/char and all subsequent characters in string. If
            this function does not find the search string, match + rest of string returns an empty string.

            •       offset of match —

            offset of match is the position of search string/char in string. If this function does not find the
          search string, offset of match returns -1.


         If you enable the Match Single Character option, this function uses only the first
      character in search string/char and searches string for this character. When finding
     the first match in string, this function splits string and returns the resulting two
      strings. To enable the Match Single Character option, right-click this function and
      select Match Single Character from the shortcut menu.

     For example, when you specify Test string for string and str for search string/
      char, this function returns different resulting strings depending on whether you enable
     the Match Single Character option. The following table shows the resulting strings.


                            Match Single Character Disabled   Match Single Character Enabled

       substring before match  Test                      Te


720   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:720 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:721 ordinal=721 -->
## Functions

Functions


                      Match Single Character Disabled   Match Single Character Enabled

 match + rest of string    string                    st string

PickPick LineLine FunctionFunction

Chooses a line from multi-line string and appends that line to string.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •       string ("") —

     string is the string to which LabVIEW appends the string selected from multi-line string. The
     default is an empty string.

   •       multi-line string —

     multi-line string contains one or more substrings separated by linefeeds.

   •       line index —

     line index selects the line the function appends from multi-line string.

     line index must be numeric. A line index of 0 selects the first line. If line index is negative or is
    greater than or equal to the number of lines in multi-line string, the function sets output string
    to string.
   •      output string —

    output string is the resulting string.


MatchMatch FirstFirst StringString FunctionFunction

Compares each prefix string in string array to the beginning of string until it
encounters a match. This function returns the original input string with the matching


                                                    © National Instruments 721

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:721 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:722 ordinal=722 -->
## Functions

Functions

      prefix string removed.


     Inputs/Outputs

            •       string —

           string specifies the string to match to the prefixes in string array. The default is an empty string.

            •       string array —

           string array specifies the array of strings that you want to match with string. If the function
          encounters an empty string in string array, the function considers that string a match.

            •      output string —

          output string returns the original string with the matching prefix removed. If the beginning of
           string does not match any string in string array, output string returns the original string.

            •      index —

          index returns the numeric index of the matching prefix in string array. If the beginning of string
         does not match any string in string array, index is –1.


      This function compares each string in string array to string in the order in which the
     elements are indexed. This function always searches from the beginning of string and
     matches the first string prefix that appears at the beginning of string. For example, this
      function matches Error 1 in the string Error 16: error occurred if Error
    1 comes before Error 16 in string array. However, the function matches Error 16
         if Error 16 comes before Error 1 in string array.

    MatchMatch True/FalseTrue/False StringString FunctionFunction

     Examines the beginning of string to see whether it matches true string or false string.
      This function returns a Boolean TRUE or FALSE value in selection, depending on
     whether string matches true string or false string.


722   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:722 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:723 ordinal=723 -->
## Functions

Functions


Inputs/Outputs

   •       string —

     string is the input string. The default is an empty string.

   •      true string —

       If true string matches string, selection is TRUE.

   •       false string —

       If false string matches string, selection is FALSE.

   •      output string —

    output string is a shortened version of string with the matching substring removed if either true
     string or false string matches the beginning of string. If neither true string nor false string
    matches the beginning of string, output string returns string unchanged.

   •       selection —

    selection is TRUE if true string matches the beginning of string, and FALSE if false string
    matches the beginning of string, or if neither string matches.


ScanScan StringString ForFor TokensTokens FunctionFunction

Scans input string starting at offset for tokens and outputs each segment as a token
string.


                                                    © National Instruments 723

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:723 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:724 ordinal=724 -->
## Functions

Functions

     Inputs/Outputs

            •      allow empty tokens? (F) —

          allow empty tokens? determines whether the function recognizes a token when it encounters
           multiple adjacent delimiters.

                 If allow empty tokens? is FALSE (default), multiple adjacent delimiters can separate two tokens
            in input string. If allow empty tokens? is TRUE, an empty token string is returned between
          every pair of adjacent delimiters.
            •      input string —

          input string is the string to scan for tokens.

            •       offset —

            offset is the point in input string to begin scanning.

         The default is 0, which specifies the beginning of the string.
            •      operators (none) —

          operators is an array of strings that the function identifies as tokens when they appear in input
            string, even if they are not surrounded by delimiters.

                 If a portion of input string matches more than one defined operator, the function chooses the
           longest match as a token. For example, if >, = and >= are defined operators, the input string
        4>=0 produces >= as the next token string with an offset of 1.

         A string in operators might contain the following special format codes, which you can use to
          scan entire numbers as single tokens.

       %d           match decimal integer
       %o           match octal integer
        %x            match hexadecimal integer
       %b           match binary integer
         %e,%f,%g      match floating-point or scientific real number
      %%           match a single % character


              Note If the strings + or – are defined as operators, the function does not recognize
                     leading, or unary, + and – signs. The function always returns them as separate tokens.
                    This is an exception to the "longest match" rule.

            •       delimiters (\s,\t,\r,\n) —

724   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:724 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:725 ordinal=725 -->
## Functions

Functions


  delimiters is an array of strings that act as separators between tokens.

  Strings in delimiters are not returned as tokens but serve to separate adjacent tokens from each
  other. The default delimiters are the white space characters: space, tab, linefeed, and carriage
  return.

•      use cached delim/oper data? (F) —

  use cached delim/oper data? is an advanced optional input. If unwired, token string still
  behaves correctly.

  However, you can use use cached delim/oper data? to greatly improve string parsing
  performance. Set use cached delim/oper data? to FALSE the first time token string is executed,
  and TRUE each subsequent time as long as operators and delimiters have not changed. Use a
   shift register with a constant FALSE coming in and a constant TRUE going out to ensure correct
  behavior if operators and delimiters do not change during the execution of the loop. If use
  cached delim/oper data? is TRUE and operators or delimiters has changed since the last
  execution, incorrect output might result. If both operators and delimiters are unwired or are
  wired to block diagram constants, you can leave use cached delim/oper data? unwired and still
  achieve optimal performance.

•       string out —

  string out returns input string unchanged.

•       offset past token —

  offset past token identifies the point in the input string immediately following the most recently
  found token and any trailing delimiters.

  Any subsequent scanning of the same input string should begin at this offset. If offset is less
  than 0 or greater than the number of characters in input string, or if the end of the string was
  reached, offset past token is –1.

•      token string —

  token string is the matched token. It can be one of the strings in operators or any text string in
  input string that appears between delimiters.

•      token index —

  token index is the index of token string in operators if token string matches one of the elements
  in operators.


                                                   © National Instruments 725

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:725 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:726 ordinal=726 -->
## Functions

Functions

                 If token string is any other string, token index returns –1. If the function reaches the end of input
           string without finding any valid operator, token index returns –2.

     Tokens are text segments that typically represent individual keywords, numeric values,
     or operators found when parsing a configuration file or other text-based data format.
     You can specify tokens with the data you pass into the function through the delimiters
     and operators inputs. For example, because the space character is a delimiter by
      default, each word of This is a string is a token, and you can parse the
     sentence into its component words.

     Use this function in a While Loop that processes one section of string at a time until
     token index returns –2 (indicating end of string). You can pass offset past token
     through a shift register into offset, so that each scan starts where the preceding scan
     ended.

     By default, the function identifies and returns a token when it encounters a space, tab,
      carriage return, or linefeed. You can parse a string using these or any other delimiters
     you choose or you can define operators.

     For example, suppose you wire the following values to the function.


       Input                 Value

       input string         This is a testLabVIEWstring

        offset              0 (default)

       operators           [NI,asdf,LabVIEW]

       delimiters          \s,\t,\r,\n (default)

         If you place the function in a While Loop, the function returns the following values.

      First Iteration

        string out               This is a testLabVIEWstring

        offset past token          5

      token string              This


726   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:726 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:727 ordinal=727 -->
## Functions

Functions


 token index              –1 (not an operator)

Second Iteration

 string out               This is a testLabVIEWstring

 offset past token          8

 token string              is

 token index              –1 (not an operator)

Third Iteration

 string out               This is a testLabVIEWstring

 offset past token          10

 token string              a

 token index              –1 (not an operator)

Fourth Iteration

 string out               This is a testLabVIEWstring

 offset past token          14

 token string              test

 token index              –1 (not an operator)

Fifth Iteration

 string out               This is a testLabVIEWstring

 offset past token          21

 token string              LabVIEW

 token index              2 (second item in operators)


                                                    © National Instruments 727

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:727 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:728 ordinal=728 -->
## Functions

Functions

     Sixth Iteration

        string out               This is a testLabVIEWstring

        offset past token          –1 (no more tokens present)

      token string              string

      token index              –1 (not an operator)

    Seventh Iteration

        string out               This is a testLabVIEWstring

        offset past token          –1 (no more tokens present)

      token string                 (end of string)

      token index              –2 (end of string)

     SearchSearch andand ReplaceReplace PatternPattern

     Searches string for substrings that match regular expression and replaces those
      substrings with replace string. A regular expression requires a specific combination of
      characters for pattern matching. For more information about special characters in
      regular expressions, refer to the regular expression input description in the detailed
      help.


     Inputs/Outputs

            •      replace all? (F) —

                 If replace all? is TRUE, the VI replaces all substrings in string that match regular expression.

                 If FALSE (default), the VI replaces only the first substring in string.

            •       string —

728   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:728 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:729 ordinal=729 -->
## Functions

Functions


     string specifies the input string you want the function to search.

   •      regular expression ("") —

    regular expression is the pattern for which you want to search in string.

    You can use special characters in regular expression.

       If the VI does not find regular expression, result string is string and offset past match is –1. If
    regular expression matches the empty string, the function makes no replacements, result string
      is string, and offset past match returns 0 or the length of the string, depending on whether
    replace all? is FALSE or TRUE, respectively.

   •      replace string ("") —

    replace string replaces the substring in string that matches regular expression. The default is an
    empty string.

   •       offset (0) —

     offset specifies number of characters into string at which the function starts searching for a
    match. offset must be numeric.

    The offset of the first character in string is 0. If offset is unwired or less than 0, the function takes
     offset as 0.

   •       result string —

     result string contains the edited string with the replaced characters.

   •       offset past match —

     offset past match is the index in string of the first character after the last match. If the VI does
    not find a match, offset past match is –1.


This VI is similar to the Match Pattern function.

This VI can perform a case-insensitive search or search for more complex patterns than
the Search and Replace String function.


                                                    © National Instruments 729

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:729 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:730 ordinal=730 -->
## Functions

Functions

     IndexIndex StringString ArrayArray FunctionFunction

      Selects a string specified by index from string array and appends that string to string.


     Inputs/Outputs

            •       string ("") —

           string is the string to which LabVIEW appends the string selected from string array. The default
              is an empty string.

            •       string array —

           string array is the array from which LabVIEW selects a string according to index to append to
            string.

            •      index —

          index must be numeric.

            •      output string —

          output string is string with the string in string array at offset index appended.

                 If index is less than zero or greater than the number of elements in string array, output string
           returns string unchanged.

    AppendAppend True/FalseTrue/False StringString FunctionFunction

      Selects either a FALSE or TRUE string according to a Boolean selector and appends
      that string to string.


730   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:730 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:731 ordinal=731 -->
## Functions

Functions

Inputs/Outputs

   •       string ("") —

     string is the input string. The default is an empty string.

   •      true string —

    true string is the string to append if selector is TRUE.

   •       false string —

     false string is the string to append if selector is FALSE.

   •       selector —

    selector determines whether the function appends true string (TRUE) or false string (FALSE) to
     string.

   •      output string —

    output string is the resulting string.


RotateRotate StringString FunctionFunction

Places the first character of string in the last position of first char last, shifting the
other characters forward one position. For example, the string abcd becomes bcda.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •       string —

     string can be a string or any data structure that contains only strings, such as an array or clusters
     of strings.

   •        first char last —


                                                    © National Instruments 731

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:731 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:732 ordinal=732 -->
## Functions

Functions


              first char last is the rotated string and has the same structure as string.


     ReverseReverse StringString FunctionFunction

     Produces a string whose characters are in reverse order of those in string.

     The connector pane displays the default data types for this polymorphic function.


     Inputs/Outputs

            •       string —

           string can be a string or any data structure that contains only strings, such as an array or clusters
           of strings.

            •      reversed —

          reversed is the reversed string and has the same structure as string.


     DelimitedDelimited StringString toto 1D1D StringString ArrayArray

     Converts substrings in a delimited string to the elements of a one-dimensional string
      array.


     Inputs/Outputs

            •      delimited string —

          delimited string specifies the string with a delimiting character between substrings.

            •       delimiter —

732   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:732 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:733 ordinal=733 -->
## Functions

Functions


    delimiter specifies the character that separates substrings in a delimited string. The default is
    \t, which specifies a single tab character.

   •       string array —

     string array returns an array of strings constructed from delimited string.


1D1D StringString ArrayArray toto DelimitedDelimited StringString

Converts the elements of a one-dimensional string array to a single string with input
array elements separated by a delimiting character.


Inputs/Outputs

   •       string array —

     string array specifies the one-dimensional array of strings on which the node operates.

   •       delimiter —

    delimiter specifies the character that separates substrings in a delimited string. The default is
    \t, which specifies a single tab character.

   •      delimited string —

    delimited string returns a string of concatenated array elements separated by the delimiter you
     specify.


CreateCreate NINI GUIDGUID

Generates a globally unique identifier (GUID) string.


                                                    © National Instruments 733

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:733 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:734 ordinal=734 -->
## Functions

Functions

     Inputs/Outputs

            •      NI GUID —

          NI GUID returns a globally unique identifier (GUID) string of the following format:
        12345678-1234-1234-1234-1234567890AB.

     ASCIIASCII CodesCodes

      ASCII encoding is a 7-bit code (from 0 to 127). It contains upper and lowercase English,
     American English punctuation, base 10 numbers, and a few control codes. The first 32
     codes (from 0 to 31) are control codes, which are a set of non-printable control
      characters used for text formatting.

     To represent international characters, single-byte operating systems use an 8-bit
     extension of ASCII. The lower 128 character codes are identical to ASCII, and the upper
     128 are different for each code page. The various international characters reside in the
     upper 128 character codes. Windows, Linux, and macOS use 8-bit character sets, but
     they each map differently. Because the upper 128 character sets differ between
     operating systems and languages, these are not displayed here.


      Dec       Oct      Hex         Ctrl Char             ASCII       Msg

      0         000      00       CTRL-@           NUL      —

      1         001      01        CTRL-A           SOH        GTL

      2         002      02        CTRL-B             STX      —

      3         003      03        CTRL-C             ETX      —

      4         004      04        CTRL-D           EOT        SDC

      5         005      05        CTRL-E           ENQ        PPC

      6         006      06        CTRL-F            ACK      —

      7         007      07        CTRL-G            BEL      —

      8         010      08        CTRL-H            BS         GET

      9         011      09         CTRL-I            HT          TCT

      10        012      0A        CTRL-J              LF       —


734   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:734 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:735 ordinal=735 -->
## Functions

Functions


Dec       Oct      Hex         Ctrl Char             ASCII       Msg

11        013      0B        CTRL-K            VT       —

12        014      0C        CTRL-L             FF       —

13        015      0D       CTRL-M           CR      —

14        016      0E        CTRL-N           SO      —

15        017      0F        CTRL-O                SI       —

16        020      10        CTRL-P            DLE      —

17        021      11        CTRL-Q            DC1         LLO

18        022      12        CTRL-R            DC2      —

19        023      13        CTRL-S            DC3      —

20        024      14        CTRL-T            DC4        DCL

21        025      15        CTRL-U           NAK        PPU

22        026      16        CTRL-V            SYN      —

23        027      17       CTRL-W            ETB      —

24        030      18        CTRL-X           CAN        SPE

25        031      19        CTRL-Y           EM         SPD

26        032      1A        CTRL-Z           SUB      —

27        033      1B         CTRL-[             ESC      —

28        034      1C         CTRL-\             FS       —

29        035      1D         CTRL-]            GS      —

30        036      1E        CTRL-^            RS      —

31        037      1F        CTRL-_           US      —

32        040      20     —                SP         MLA0

33        041      21     —                              !           MLA1

34        042      22     —                     "          MLA2

35        043      23     —                  #          MLA3

36        044      24     —                  $          MLA4

37        045      25     —           %          MLA5


                                                    © National Instruments 735

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:735 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:736 ordinal=736 -->
## Functions

Functions


      Dec       Oct      Hex         Ctrl Char             ASCII       Msg

      38        046      26     —              &          MLA6

      39        047      27     —                                   '           MLA7

      40        050      28     —                             (           MLA8

      41        051      29     —                             )           MLA9

      42        052      2A     —                     *           MLA10

      43        053      2B     —                  +          MLA11

      44        054      2C     —                                   ,           MLA12

      45        055      2D     —                  –           MLA13

      46        056      2E     —                                   .           MLA14

      47        057      2F     —                         /           MLA15

      48        060      30     —                  0          MLA16

      49        061      31     —                  1          MLA17

      50        062      32     —                  2          MLA18

      51        063      33     —                  3          MLA19

      52        064      34     —                  4          MLA20

      53        065      35     —                  5          MLA21

      54        066      36     —                  6          MLA22

      55        067      37     —                  7          MLA23

      56        070      38     —                  8          MLA24

      57        071      39     —                  9          MLA25

      58        072      3A     —                                   :           MLA26

      59        073      3B     —                                   ;           MLA27

      60        074      3C     —                  <          MLA28

      61        075      3D     —                  =          MLA29

      62        076      3E     —                  >          MLA30

      63        077      3F     —                     ?          UNL

      64        100      40     —          @          MTA0


736   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:736 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:737 ordinal=737 -->
## Functions

Functions


Dec       Oct      Hex         Ctrl Char             ASCII       Msg

65        101      41     —                A          MTA1

66        102      42     —               B          MTA2

67        103      43     —               C          MTA3

68        104      44     —              D          MTA4

69        105      45     —                 E          MTA5

70        106      46     —                  F          MTA6

71        107      47     —              G          MTA7

72        110      48     —             H          MTA8

73        111      49     —                                 I           MTA9

74        112      4A     —                  J          MTA10

75        113      4B     —               K          MTA11

76        114      4C     —                  L          MTA12

77        115      4D     —            M          MTA13

78        116      4E     —              N          MTA14

79        117      4F     —             O          MTA15

80        120      50     —               P          MTA16

81        121      51     —             Q          MTA17

82        122      52     —               R          MTA18

83        123      53     —                S          MTA19

84        124      54     —                T          MTA20

85        125      55     —              U          MTA21

86        126      56     —                 V          MTA22

87        127      57     —           W          MTA23

88        130      58     —                 X          MTA24

89        131      59     —                  Y          MTA25

90        132      5A     —                Z          MTA26

91        133      5B     —                             [           MTA27


                                                    © National Instruments 737

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:737 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:738 ordinal=738 -->
## Functions

Functions


      Dec       Oct      Hex         Ctrl Char             ASCII       Msg

      92        134      5C     —                         \           MTA28

      93        135      5D     —                             ]           MTA29

      94        136      5E     —                  ^          MTA30

      95        137      5F     —                 _         UNT

      96        140      60     —                `           MSA0,PPE

      97        141      61     —                 a           MSA1,PPE

      98        142      62     —                b           MSA2,PPE

      99        143      63     —                   c           MSA3,PPE

      100       144      64     —                d           MSA4,PPE

      101       145      65     —                  e           MSA5,PPE

      102       146      66     —                              f           MSA6,PPE

      103       147      67     —                 g           MSA7,PPE

      104       150      68     —                h           MSA8,PPE

      105       151      69     —                                    i           MSA9,PPE

      106       152      6A     —                                   j            MSA10,PPE

      107       153      6B     —                  k           MSA11,PPE

      108       154      6C     —                                  l           MSA12,PPE

      109       155      6D     —           m          MSA13,PPE

      110       156      6E     —                n           MSA14,PPE

      111       157      6F     —                o           MSA15,PPE

      112       160      70     —                p           MSA16,PPD

      113       161      71     —                q           MSA17,PPD

      114       162      72     —                         r           MSA18,PPD

      115       163      73     —                     s           MSA19,PPD

      116       164      74     —                          t           MSA20,PPD

      117       165      75     —                u           MSA21,PPD

      118       166      76     —                   v           MSA22,PPD


738   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:738 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:739 ordinal=739 -->
## Functions

Functions


 Dec       Oct      Hex         Ctrl Char             ASCII       Msg

 119       167      77     —            w          MSA23,PPD

 120       170      78     —                    x           MSA24,PPD

 121       171      79     —                   y           MSA25,PPD

 122       172      7A     —                     z           MSA26,PPD

 123       173      7B     —                             {           MSA27,PPD

 124       174      7C     —                                    |           MSA28,PPD

 125       175      7D     —                             }           MSA29,PPD

 126       176      7E     —                  ~           MSA30,PPD

 127       177      7F     —                DEL      —

ASCII Conversion Functions

The following is a list of some of the LabVIEW functions that use ASCII codes:

Decimal String To Number

Fract/Exp String To Number

Hexadecimal String To Number

Number To Engineering String

Number To Exponential String

Number To Fractional String

Number To Decimal String

Number To Octal String

Number To Hexadecimal String

Octal String To Number


                                                    © National Instruments 739

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:739 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:740 ordinal=740 -->
## Functions

Functions

      String to Byte Array

    FormatFormat CodesCodes forfor thethe TimeTime FormatFormat StringString

     The Format Date/Time String function calculates the date and time and formats the
     output string according to the following format codes.


      Format Code    Value

     <%a>           abbreviated weekday name (for example Wed)

     <%A>               full weekday name (for example Wednesday)

     <%b>           abbreviated month name (for example Jun)

     <%B>               full month name (for example June)

     <%c>            locale-specific default date and time

     <%d>          day of month (01–31)

     <%H>          hour (24-hour clock) (00–23)

     <%I>          hour (12-hour clock) (01–12)

     <%j>          day number of the year (001–366)

     <%m>         month number (01–12)

     <%M>          minute (00–59)

     <%p>        AM or PM flag

     <%S>          second (00–59)

     <%<digit>u>  fractional seconds with <digit> precision

                   week number of the year (00–53), with the first Sunday as the first day of week
     <%U>                       one; 00 represents the first week

     <%w>         weekday as a decimal number (0–6), with 0 representing Sunday

                   week number of the year (00–53), with the first Monday as the first day of week
     <%W>                       one; 00 represents the first week

     <%x>            locale-specific date

     <%.1x>        long date format

     <%.2x>        abbreviated long date format


740   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:740 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:741 ordinal=741 -->
## Functions

Functions


 Format Code    Value

 <%X>            locale-specific time

                 year within century (00–99); when you scan the numbers, numbers (00–68)
 <%y>           represent years in the twenty-first century (2000–2068) and numbers (69–99)
                 represent years in the twentieth century (1969–1999)

 <%Y>            year, including the century (for example, 1997)

 <%z>            difference between locale time and universal time (HH:MM:SS)

                time zone name or abbreviation, depending on the operating system locale
 <%Z>                   settings

CarriageCarriage ReturnReturn ConstantConstant

Consists of a constant string containing the ASCII CR value.

Use this constant when you do not want to type in the backslash code for the
character.


LineLine FeedFeed ConstantConstant

Consists of a constant string containing the ASCII LF value.

Use this constant when you do not want to type in the backslash code for the
character.


EndEnd ofof LineLine ConstantConstant

Consists of a constant string containing the platform-dependent end-of-line value.

(Windows) The value is CR/LF (carriage return/linefeed). (macOS/Linux) The value is
LF.

                                                    © National Instruments 741

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:741 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:742 ordinal=742 -->
## Functions

Functions

     Use this constant when you do not want to type in the backslash code for the
      character.


   ComparisonComparison

     Use the Comparison functions to compare Boolean values, strings, numeric values,
      arrays, and clusters.

     The Comparison functions treat Boolean, string, numeric, array, and cluster values
      differently. You also can use the Comparison functions to compare characters. You can
     change the comparison mode of some Comparison functions.


       Palette                    Description
       Object

       Equal?      Returns TRUE if x is equal to y. Otherwise, this function returns FALSE. You can
       Function    change the comparison mode of this function.

      Not Equal?   Returns TRUE if x is not equal to y. Otherwise, this function returns FALSE. You can
       Function    change the comparison mode of this function.

       Greater?     Returns TRUE if x is greater than y. Otherwise, this function returns FALSE. You can
       Function    change the comparison mode of this function.

       Less?        Returns TRUE if x is less than y. Otherwise, this function returns FALSE. You can
       Function    change the comparison mode of this function.

       Greater Or
                   Returns TRUE if x is greater than or equal to y. Otherwise, this function returns FALSE.
       Equal?
                  You can change the comparison mode of this function.
       Function

       Less Or
                   Returns TRUE if x is less than or equal to y. Otherwise, this function returns FALSE.
       Equal?
                  You can change the comparison mode of this function.
       Function

       Equal To 0?
                   Returns TRUE if x is equal to 0. Otherwise, this function returns FALSE.
       Function


742   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:742 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:743 ordinal=743 -->
## Functions

Functions


Palette             Description
Object

Not Equal
To 0?        Returns TRUE if x is not equal to 0. Otherwise, this function returns FALSE.
Function

Greater
Than 0?     Returns TRUE if x is greater than 0. Otherwise, this function returns FALSE.
Function

Less Than            Returns TRUE if x is less than 0. Otherwise, this function returns FALSE.
0? Function

Greater Or
Equal To 0?  Returns TRUE if x is greater than or equal to 0. Otherwise, this function returns FALSE.
Function

Less Or
Equal To 0?  Returns TRUE if x is less than or equal to 0. Otherwise, this function returns FALSE.
Function

            Returns the value wired to the t input or f input, depending on the value of s. If s isSelect           TRUE, this function returns the value wired to t. If s is FALSE, this function returns the
Function             value wired to f.

           Compares x and y and returns the larger value at the top output terminal and the
             smaller value at the bottom output terminal. This function accepts time stamp valuesMax & Min                     if all inputs are time stamp values. If the inputs are time stamp values, the function
Function             returns the later time at the top and the earlier time at the bottom. You can change
             the comparison mode of this function.

            Determines whether x falls within a range specified by the upper limit and lower limit
In Range     inputs and optionally coerces the value to fall within the range. The function performs
and Coerce  the coercion only in Compare Elements mode. This function accepts time stamp
Function     values if all inputs are time stamp values. You can change the comparison mode of
               this function.

Not A
Number/
            Returns TRUE if number/path/refnum is not a number (NaN), <Not a Path>, or not a
Path/
            refnum. Otherwise, this function returns FALSE.
Refnum?
Function

Empty
Array?       Returns TRUE if the input array is empty. Otherwise, this function returns FALSE.
Function


                                                    © National Instruments 743

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:743 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:744 ordinal=744 -->
## Functions

Functions


       Palette                    Description
       Object

      Empty                   Returns TRUE if string/path is an empty string or an empty path. Otherwise, this        String/                    function returns FALSE. This function is also designed to work with variants, pictures,       Path?                 and DSC tags.
       Function

                   Returns TRUE if char represents a decimal digit ranging from 0 through 9. If char is a
       Decimal      string, this function uses the first character in the string. If char is a number, this
        Digit?        function interprets it as the ASCII value of a character. If char is a floating-point
       Function    number, this function rounds to the nearest integer. Otherwise, this function returns
                   FALSE.

                   Returns TRUE if char represents a hex digit ranging from 0 through 9, A through F, or a
                   through f. If char is a string, this function uses the first character in the string. If char is
      Hex Digit?                  a number, this function interprets it as the ASCII value of a character. If char is a       Function
                      floating-point number, this function rounds to the nearest integer. Otherwise, this
                    function returns FALSE.

                   Returns TRUE if char represents an octal digit ranging from 0 through 7. If char is a
                        string, this function uses the first character in the string. If char is a number, this
       Octal Digit?                    function interprets it as the ASCII value of a character. If char is a floating-point       Function                  number, this function rounds to the nearest integer. Otherwise, this function returns
                   FALSE.

                   Returns TRUE if char represents a printable ASCII character. If char is a string, this
       Printable?   function uses the first character in the string. If char is a number, this function
       Function     interprets it as the ASCII value of a character. If char is a floating-point number, this
                    function rounds to the nearest integer. Otherwise, this function returns FALSE.

                   Returns TRUE if char represents a white space character, such as Space, Tab, Newline,
       White        Carriage Return, Form Feed, or Vertical Tab. If char is a string, this function uses the
       Space?         first character in the string. If char is a number, this function interprets it as the ASCII
       Function     value of a character. If char is a floating-point number, this function rounds to the
                    nearest integer. Otherwise, the function returns FALSE.

        Lexical      Returns the class number for char. If char is a string, this function uses the first
       Class        character in the string. If char is a number, this function interprets it as the ASCII value
       Function     of a character.

                 Compares input items you specify to determine whether values are equal, greater
      Comparison
                     than, less than, and so on.


744   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:744 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:745 ordinal=745 -->
## Functions

Functions


 Palette              Description
 Object

            Use the Assert Type VIs and functions in conjunction with the Type Specialization
               structure for the following purposes:
 Assert Type                       • Customizing sections of code in a malleable VI (.vim) for specific data types
                       • Forcing a malleable VI to accept only data types that meet certain requirements
                       • Forcing a malleable VI to decline specific data types


 Is Value      Returns TRUE if this is the first call of this VI or if the input value is different from the
 Changed     value when this VI was last called.

 Is Path and   Returns TRUE if path is any value other than <Not A Path> or an empty path.
 Not Empty?  Otherwise, this VI returns FALSE.

 Fixed-Point             Returns TRUE if FXP includes an overflow status and FXP is the result of an operation Overflow?
              that overflowed. Otherwise, this function returns FALSE. Function

Equal?Equal? FunctionFunction

Returns TRUE if x is equal to y. Otherwise, this function returns FALSE. You can change
the comparison mode of this function.

If you compare two matrices, the default comparison mode is Compare Aggregates,
and this function returns a scalar. You can compare an array or cluster of a data type to
a scalar of the same data type and produce an array or cluster of Boolean values. The
connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —


                                                    © National Instruments 745

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:745 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:746 ordinal=746 -->
## Functions

Functions


          x is a value to compare to y

            •      y —

          y must be of the same type as x.

            •      x = y? —

        When you compare arrays, x = y? is a scalar in Compare Aggregates mode and a Boolean array in
         Compare Elements mode (default).


    When comparing VI Server references, this function returns TRUE when the two
      references refer to the same object, regardless of whether the references have the
    same capability or the same value. For example, one might be a strict reference to a
      digital numeric control and the other might be a generic reference but if they refer to
     the same object, they are equal. To compare the actual values of the references, use
     the Type Cast function to convert the references to 32-bit signed integers. Then use the
     Equal? function to compare those integers.

      Similarly to the previous situation, if you have a local reference and a remote reference
      to the same LabVIEW object, this function returns FALSE. However, when two
      references refer to the same object but one of them is authenticated and the other is
      not, this function still returns TRUE.

          Note If you compare two inputs with the value not a number, NaN, or one
             input with the value NaN to an input with another value, this function always
             returns FALSE. Use the Not a Number/Path/Refnum? function to compare one
             or more inputs with a value of NaN.

    When you wire matrix data as an input to this function, a VI that includes subVIs that
     work with the matrix data type replaces the function. The resulting VI has the same
     icon but contains a matrix-specific algorithm. The node remains a VI if you disconnect
     the matrix from the input(s). Wire other data types as inputs to restore the original
      function. If you wire a data type to a function and that data type causes a basic math
     operation to fail, the function returns an empty matrix or NaN.


746   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:746 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:747 ordinal=747 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Comparison\Comparison Functions.vi

NotNot Equal?Equal? FunctionFunction

Returns TRUE if x is not equal to y. Otherwise, this function returns FALSE. You can
change the comparison mode of this function.

If you compare two matrices, the default comparison mode is Compare Aggregates,
and this function returns a scalar. You can compare an array or cluster of a data type to
a scalar of the same data type and produce an array or cluster of Booleans. The
connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

     xis a value to compare to y

   •      y —
    y must be of the same type as x
   •      x != y? —

    x!=y? returns the Boolean result of the operation. When you compare arrays, x!=y? is a scalar in
   Compare Aggregates mode and a Boolean array in Compare Elements mode (default).


When comparing VI Server references, this function returns FALSE when the two
references refer to the same object, regardless of whether the references have the
same capability or the same value. For example, one might be a strict reference to a
digital numeric control and the other might be a generic reference but if they refer to
the same object, they are equal. To compare the actual values of the references, use
the Type Cast function to convert the references to 32-bit signed integers. Then use the

                                                    © National Instruments 747

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:747 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:748 ordinal=748 -->
## Functions

Functions

     Not Equal? function to compare those integers.

      Similarly to the previous situation, if you have a local reference and a remote reference
      to the same LabVIEW object, this function returns TRUE. However, when two
      references refer to the same object but one of them is authenticated and the other is
      not, this function still returns FALSE.

          Note If you compare two inputs with the value not a number, NaN, or one
             input with the value NaN to an input with another value, this function always
             returns TRUE. Use the Not a Number/Path/Refnum? function to compare one
             or more inputs with a value of NaN.

    When you wire matrix data as an input to this function, a VI that includes subVIs that
     work with the matrix data type replaces the function. The resulting VI has the same
     icon but contains a matrix-specific algorithm. The node remains a VI if you disconnect
     the matrix from the input(s). Wire other data types as inputs to restore the original
      function. If you wire a data type to a function and that data type causes a basic math
     operation to fail, the function returns an empty matrix or NaN.

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Comparison\Comparison Functions.vi

     Greater?Greater? FunctionFunction

     Returns TRUE if x is greater than y. Otherwise, this function returns FALSE. You can
     change the comparison mode of this function.

     You can compare an array or cluster of a data type to a scalar of the same data type
     and produce an array or cluster of Boolean values. The connector pane displays the
      default data types for this polymorphic function.


748   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:748 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:749 ordinal=749 -->
## Functions

Functions

Inputs/Outputs

   •      x —

    x is a value to compare to y

   •      y —

    y must be of the same type as x

   •      x > y? —

    x > y? returns the Boolean result of the operation.

   When you compare arrays, x > y? is a scalar in Compare Aggregates mode and a Boolean array in
   Compare Elements mode (default).

Less?Less? FunctionFunction

Returns TRUE if x is less than y. Otherwise, this function returns FALSE. You can change
the comparison mode of this function.

You can compare an array or cluster of a data type to a scalar of the same data type
and produce an array or cluster of Boolean values. The connector pane displays the
default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x is a value to compare to y

   •      y —

    y must be of the same type as x

   •      x < y? —


                                                    © National Instruments 749

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:749 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:750 ordinal=750 -->
## Functions

Functions


          x < y? returns the Boolean result of the operation. When you compare arrays, x < y? is a scalar in
         Compare Aggregates mode and a Boolean array in Compare Elements mode (default).

    GreaterGreater OrOr Equal?Equal? FunctionFunction

     Returns TRUE if x is greater than or equal to y. Otherwise, this function returns FALSE.
     You can change the comparison mode of this function.

     You can compare an array or cluster of a data type to a scalar of the same data type
     and produce an array or cluster of Boolean values. The connector pane displays the
      default data types for this polymorphic function.


     Inputs/Outputs

            •      x —

          x is a value to compare to y

            •      y —

          y must be of the same type as x

            •      x >= y? —

          x >= y? returns the Boolean result of the operation.

        When you compare arrays, x >= y? is a scalar in Compare Aggregates mode and a Boolean array
            in Compare Elements mode (default).

    LessLess OrOr Equal?Equal? FunctionFunction

     Returns TRUE if x is less than or equal to y. Otherwise, this function returns FALSE. You
     can change the comparison mode of this function.


750   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:750 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:751 ordinal=751 -->
## Functions

Functions

You can compare an array or cluster of a data type to a scalar of the same data type
and produce an array or cluster of Boolean values. The connector pane displays the
default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x is a value to compare to y

   •      y —

    y must be of the same type as x

   •      x <= y? —

    x ≤ y? returns the Boolean result of the operation. When you compare arrays, x ≤ y? is a scalar in
   Compare Aggregates mode and a Boolean array in Compare Elements mode (default).

EqualEqual ToTo 0?0? FunctionFunction

Returns TRUE if x is equal to 0. Otherwise, this function returns FALSE.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x can be a numeric scalar value, cluster, array of numbers, or a time stamp value.

   •      x = 0? —


                                                    © National Instruments 751

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:751 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:752 ordinal=752 -->
## Functions

Functions


          x = 0? is a Boolean value of the same data type structure as x.

    NotNot EqualEqual ToTo 0?0? FunctionFunction

     Returns TRUE if x is not equal to 0. Otherwise, this function returns FALSE.

     The connector pane displays the default data types for this polymorphic function.


     Inputs/Outputs

            •      x —

          x can be a numeric scalar value, cluster, array of numbers, or a time stamp value.

            •      x != 0? —

           x!= 0? is a Boolean value of the same data type structure as x.

    GreaterGreater ThanThan 0?0? FunctionFunction

     Returns TRUE if x is greater than 0. Otherwise, this function returns FALSE.

     The connector pane displays the default data types for this polymorphic function.


     Inputs/Outputs

            •      x —

          x can be a numeric scalar value, cluster, array of numbers, or a time stamp value.

            •      x > 0? —

752   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:752 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:753 ordinal=753 -->
## Functions

Functions


    x > 0? is a Boolean value of the same data type structure as x.

LessLess ThanThan 0?0? FunctionFunction

Returns TRUE if x is less than 0. Otherwise, this function returns FALSE.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x can be a numeric scalar value, cluster, array of numbers, or a time stamp value.

   •      x < 0? —

    x < 0? is a Boolean value of the same data type structure as x.

GreaterGreater OrOr EqualEqual ToTo 0?0? FunctionFunction

Returns TRUE if x is greater than or equal to 0. Otherwise, this function returns FALSE.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x can be a numeric scalar value, cluster, array of numbers, or a time stamp value.

   •      x >= 0? —

                                                    © National Instruments 753

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:753 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:754 ordinal=754 -->
## Functions

Functions


          x >= 0? is a Boolean value of the same data type structure as x.

    LessLess OrOr EqualEqual ToTo 0?0? FunctionFunction

     Returns TRUE if x is less than or equal to 0. Otherwise, this function returns FALSE.

     The connector pane displays the default data types for this polymorphic function.


     Inputs/Outputs

            •      x —

          x can be a numeric scalar value, cluster, array of numbers, or a time stamp value.

            •      x <= 0? —

          x ≤ 0? is a Boolean value of the same data type structure as x.

     SelectSelect FunctionFunction

     Returns the value wired to the t input or f input, depending on the value of s. If s is
     TRUE, this function returns the value wired to t. If s is FALSE, this function returns the
     value wired to f.

     The connector pane displays the default data types for this polymorphic function.


     Inputs/Outputs

            •        t —


754   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:754 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:755 ordinal=755 -->
## Functions

Functions


     t is the value that this function returns if s passes a TRUE value.

     t and f must be of the same type, but they can have different numeric representations.
   •       s —

    s determines whether the function returns the value of t or f in s? t:f.

       If you wire an error cluster to s and an error occurs, the error cluster passes a TRUE value to the
     function. Otherwise, the error cluster passes a FALSE value to the function.
   •         f —

      f is the value that this function returns if s passes a FALSE value.

     t and f must be of the same type, but they can have different numeric representations.
   •       s? t:f —

    s? t:f is the value wired to t if s is TRUE. s? t:f is the value wired to f if s is FALSE.

MaxMax && MinMin FunctionFunction

Compares x and y and returns the larger value at the top output terminal and the
smaller value at the bottom output terminal. This function accepts time stamp values
if all inputs are time stamp values. If the inputs are time stamp values, the function
returns the later time at the top and the earlier time at the bottom. You can change the
comparison mode of this function.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

     xis a value to compare to y

   •      y —


                                                    © National Instruments 755

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:755 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:756 ordinal=756 -->
## Functions

Functions


          y must be of the same type as x

            •      max(x,y) —

          max(x, y) is the larger value. When you compare arrays in Compare Elements mode (default),
            this function compares corresponding elements in each input array and returns the element
          with the maximum value. max(x, y) is an array consisting of the maximum value elements. When
         you compare arrays in Compare Aggregates mode, this function compares corresponding
          elements in each input array starting at the beginning of the array. When this function reaches a
            pair of unequal corresponding elements, max(x, y) returns the array that has the greater value
            for that element.

            •      min(x,y) —

          min(x, y) is the smaller value. When you compare arrays in Compare Elements mode (default),
            this function compares corresponding elements in each input array and returns the element
          with the minimum value. min(x, y) is an array consisting of the minimum value elements. When
         you compare arrays in Compare Aggregates mode, this function compares corresponding
          elements in each input array starting at the beginning of the array. When this function reaches a
            pair of unequal corresponding elements, min(x, y) returns the array that has the smaller value
            for that element.


    Behavior When Comparing NaN Elements

      In Compare Elements mode, when one or both inputs are NaN (Not-a-Number), this
      function produces the following results:

          • Both inputs are NaN—Both max(x,y) and min(x,y) return NaN
          • Only one input is NaN—Both max(x,y) and min(x,y) return the non-NaN value
          • Inputs are arrays—The function evaluates each pair of elements according to the
         previous rules

      In Compare Aggregates mode, when one or both inputs are NaN (Not-a-Number), this
      function produces the following results:

          • Both inputs are NaN—Both max(x,y) and min(x,y) return NaN
          • Only one input is NaN—max(x,y) returns x and min(x,y) returns y
          • Inputs are arrays—If the function encounters a NaN element in either input array,
         max(x,y) returns x and min(x,y) returns y


756   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:756 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:757 ordinal=757 -->
## Functions

Functions

InIn RangeRange andand CoerceCoerce FunctionFunction

Determines whether x falls within a range specified by the upper limit and lower limit
inputs and optionally coerces the value to fall within the range. The function performs
the coercion only in Compare Elements mode. This function accepts time stamp values
if all inputs are time stamp values. You can change the comparison mode of this
function.

upper limit, x, and lower limit should usually be of the same data type structure,
either arrays or clusters, but they can have different numeric representations.

For example, if you change one of the data types to an array, you must change the
remaining data types to arrays to avoid broken wires. However, you can wire an array
to x and two scalars to upper limit and lower limit. You also can wire double-
precision, floating-point and integer data.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      upper limit —

    upper limit of the range.

   •      x —

    x is the value to check and/or coerce.

   •      lower limit —

    lower limit of the range.

   •      coerced(x) —

    coerced(x) returns the coerced or unchanged value of x. If x is within the range set by the upper
     limit and lower limit inputs or if the function is in Compare Aggregates mode, the value is


                                                    © National Instruments 757

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:757 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:758 ordinal=758 -->
## Functions

Functions


          unchanged. If x is not in range and the function is in Compare Elements mode, the function
           converts the value to the same value as upper limit or lower limit. If upper limit, x, or lower
            limit is NaN, coerced(x) is NaN.

            •       In Range? —

           In Range? is a Boolean value in Compare Aggregates mode. In Compare Elements mode, the
          data type structure of In Range? matches the data type structure of x, with each scalar replaced
         by a Boolean value. If upper limit, x, or lower limit is NaN, In Range? is FALSE.


      This function compares the input data values according to the Boolean comparison
      rules. If the function is in Compare Aggregates mode, it returns the unchanged value of
     x in coerced(x) rather than a coerced value. The function considers each input array as
     a single aggregate object, similar to a cluster, where the first element is primary in the
     comparison. If x is greater than upper limit and the function is in Compare Elements
    mode (default), the function coerces x to the upper limit value. If x is less than lower
      limit and the function is in Compare Elements mode, the function coerces x to the
     lower limit value.

         If you wire a combination of signed and unsigned integers to the upper limit, x, and
     lower limit inputs of the In Range and Coerce function, all of the inputs will be coerced
      to the same unsigned integer type. This can lead to unexpected results for negative
     input values. For example, wiring an unsigned integer to upper limit and a negative
     signed integer to lower limit may cause LabVIEW to interpret the lower limit input as
      larger than the upper limit input. To avoid this issue, convert integer inputs to the
    same type before you wire them to the In Range and Coerce function.

         If the lower limit value is greater than the upper limit value, In Range? is always FALSE
     and LabVIEW switches the lower limit value and the upper limit value internally before
     computing coerced(x).

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Comparison\In Range and Coerce.vi


758   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:758 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:759 ordinal=759 -->
## Functions

Functions

NotNot AA Number/Path/Refnum?Number/Path/Refnum? FunctionFunction

Returns TRUE if number/path/refnum is not a number (NaN), <Not a Path>, or not a
refnum. Otherwise, this function returns FALSE.

Use this function to make sure a reference to an object, such as a VI, application, or
control, still resides in system memory and was not closed.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      number/path/refnum —

    number/path/refnum can be a scalar number, path, or refnum, or it can be a cluster or array of
    numbers, paths, or refnums.

   •      NaN/Path/Refnum? —

    NaN/Path/Refnum? is a Boolean value of the same data type structure as number/path/refnum.


This function works only on references generated by LabVIEW functions. Do not use
this function to determine the validity of a rendezvous refnum, semaphore refnum, or
any refnum created by the GOOP wizard, LabVIEW Database Connectivity Toolkit, or
LabVIEW Internet Toolkit. For rendezvous refnums, use the Not A Rendezvous VI. For
semaphore refnums, use the Not A Semaphore VI. For all other GOOP refnums or
toolkit refnums, use the Vis defined by the refnum creator.

To avoid race conditions when evaluating the refnum status, National Instruments
recommends limiting the usage of this function in the following ways:

  • Do not use this function to evaluate whether a refnum is invalid before using the
   refnum.
  • Use this function in custom probes to get the refnum status.
  • Use this function to evaluate the status of an existing invalid refnum before

                                                    © National Instruments 759

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:759 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:760 ordinal=760 -->
## Functions

Functions

         evaluating a new refnum.
          • Use this function to evaluate the status of a refnum before using another refnum.
          • Consider using semaphores to protect code that the function executes
          conditionally.

    EmptyEmpty Array?Array? FunctionFunction

     Returns TRUE if the input array is empty. Otherwise, this function returns FALSE.


     Inputs/Outputs

            •      array —

           array specifies an n-dimensional array of any type.

            •     empty? —

         empty? is TRUE if array is empty. Otherwise, empty? is FALSE.

    EmptyEmpty String/Path?String/Path? FunctionFunction

     Returns TRUE if string/path is an empty string or an empty path. Otherwise, this
      function returns FALSE. This function is also designed to work with variants, pictures,
     and DSC tags.

     The connector pane displays the default data types for this polymorphic function.


     Inputs/Outputs

            •       string/path —


760   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:760 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:761 ordinal=761 -->
## Functions

Functions


    string/path can be a string, a path, a variant, a picture string, a DSC tag, or an array or a cluster
     of these types.

   •     empty? —

    empty? is a Boolean value of the same data type structure as string/path.

DecimalDecimal Digit?Digit? FunctionFunction

Returns TRUE if char represents a decimal digit ranging from 0 through 9. If char is a
string, this function uses the first character in the string. If char is a number, this
function interprets it as the ASCII value of a character. If char is a floating-point
number, this function rounds to the nearest integer. Otherwise, this function returns
FALSE.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      char —

    char can be a scalar string or number, clusters of strings or numbers, arrays of strings or
    numbers, and so on.

   •       digit? —

     digit? is a Boolean value of the same data type structure as char.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Comparison\Compare Character Types.vi


                                                    © National Instruments 761

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:761 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:762 ordinal=762 -->
## Functions

Functions

    HexHex Digit?Digit? FunctionFunction

     Returns TRUE if char represents a hex digit ranging from 0 through 9, A through F, or a
     through f. If char is a string, this function uses the first character in the string. If char is
     a number, this function interprets it as the ASCII value of a character. If char is a
      floating-point number, this function rounds to the nearest integer. Otherwise, this
      function returns FALSE.

     The connector pane displays the default data types for this polymorphic function.


     Inputs/Outputs

            •      char —

          char can be a scalar string or number, clusters of strings or numbers, arrays of strings or
          numbers, and so on.

            •      hex? —

          hex? is a Boolean value of the same data type structure as char.


    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Comparison\Compare Character Types.vi

     OctalOctal Digit?Digit? FunctionFunction

     Returns TRUE if char represents an octal digit ranging from 0 through 7. If char is a
      string, this function uses the first character in the string. If char is a number, this
      function interprets it as the ASCII value of a character. If char is a floating-point
     number, this function rounds to the nearest integer. Otherwise, this function returns
     FALSE.


762   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:762 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:763 ordinal=763 -->
## Functions

Functions

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      char —

    char can be a scalar string or number, clusters of strings or numbers, arrays of strings or
    numbers, and so on.

   •       octal? —

    octal? is a Boolean value of the same data type structure as char.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Comparison\Compare Character Types.vi

Printable?Printable? FunctionFunction

Returns TRUE if char represents a printable ASCII character. If char is a string, this
function uses the first character in the string. If char is a number, this function
interprets it as the ASCII value of a character. If char is a floating-point number, this
function rounds to the nearest integer. Otherwise, this function returns FALSE.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      char —


                                                    © National Instruments 763

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:763 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:764 ordinal=764 -->
## Functions

Functions


          char can be a scalar string or number, clusters of strings or numbers, arrays of strings or
          numbers, and so on.

            •       printable ASCII? —

           printable ASCII? is a Boolean value of the same data type structure as char.


    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Comparison\Compare Character Types.vi

    WhiteWhite Space?Space? FunctionFunction

     Returns TRUE if char represents a white space character, such as Space, Tab, Newline,
      Carriage Return, Form Feed, or Vertical Tab. If char is a string, this function uses the
        first character in the string. If char is a number, this function interprets it as the ASCII
     value of a character. If char is a floating-point number, this function rounds to the
     nearest integer. Otherwise, the function returns FALSE.

     The connector pane displays the default data types for this polymorphic function.


     Inputs/Outputs

            •      char —

          char can be a scalar string or number, clusters of strings or numbers, arrays of strings or
          numbers, and so on.

            •      space, h/v tab, cr, lf, ff? —

          space, h/v tab, cr, lf, ff? is a Boolean value of the same data type structure as char.


764   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:764 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:765 ordinal=765 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Comparison\Compare Character Types.vi

LexicalLexical ClassClass FunctionFunction

Returns the class number for char. If char is a string, this function uses the first
character in the string. If char is a number, this function interprets it as the ASCII value
of a character.


Inputs/Outputs

   •      char —

    char can be a scalar string or number, clusters of strings or numbers, arrays of strings or
    numbers, and so on.

   •       class number —

     class number is a number that corresponds to the lexical class.

    Refer to the ASCII Codes table for the numbers that correspond to each character.

    Class
              Lexical Class
   Number
    0       Extended characters (codes 128 through 255)
    1       Non-displayable ASCII characters (codes 0 to 31 excluding 9 through 13)
            White space characters: Space, Tab, Carriage Return, Form Feed, Newline, and Vertical
    2
           Tab (codes 32, 9, 13, 12, 10, and 11, respectively)
    3         Digits 0 through 9
    4       Uppercase characters A through Z
    5       Lowercase characters a through z
    6          All printable ASCII non-alphanumeric characters


                                                    © National Instruments 765

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:765 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:766 ordinal=766 -->
## Functions

Functions

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Comparison\Compare Character Types.vi

    ComparisonComparison

     Compares input items you specify to determine whether values are equal, greater
      than, less than, and so on.


     Dialog Box Options

      Option       Description

                    Contains the following options:

                                 • Data points—Compares the data points of the signals in Operand 1 to the data
                         points of the signals in Operand 2, the value you specify in Value, or the
                       Constant Value to Compare Against input.
                                 • Timestamps—Compares the initial time stamps (t0) of the signals in Operand 1
                         to the initial time stamps (t0) of the signals in Operand 2, the value you specify in
                         Value, or the Constant Value to Compare Against input.
                                 • Time between points—Compares the time between points (dt) of the signals in
                     Operand 1 to the time between points (dt) of the signals in Operand 2, the value
                     you specify in Value, or the Constant Value to Compare Against input.       Items to
                                 • Number of data points—Compares the number of data points of the signals in      Compare
                     Operand 1 to the number of data points of the signals in Operand 2, the value
                     you specify in Value, or the Constant Value to Compare Against input.
                                 • Signal name—Compares the signal names of the signals in Operand 1 to the
                           signal names of the signals in Operand 2, the value you specify in Value, or the
                       Constant Value to Compare Against input. When comparing signal names, you
                      can use wildcards to match strings. You can use the question mark character (?)
                         to match any single character. You can use the asterisk character (*) to match any
                      sequence of zero or more characters.

                                       If you select Signal name, the Comparison Condition section is disabled and set


766   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:766 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:767 ordinal=767 -->
## Functions

Functions


Option       Description

                  to = Equal.

             Contains the following options:

                      • = Equal—

                Determines if two inputs are equal.

                Because all comparison operations are floating-point operations, consider using
                Equal within tolerance for equality comparisons.

                      • <> Not equal—

                Determines if two inputs are unequal.

                      • > Greater—

                Determines if the first input is greater than the second input.

                      • >= Greater or equal—

Compare        Determines if the first input is greater than or equal to the second input.
Condition
                      • < Less—

                Determines if the first input is less than the second input.

                      • <= Less than or equal—

                Determines if the first input is less than or equal to the second input.

                      • Equal within tolerance—

                Determines if the inputs are equal within the tolerance you specify in Tolerance.

        ◦ Tolerance—

                       Specifies the level of tolerance to use when determining if an input is Equal
                     within tolerance. The default is 0.01.

                      •  In range—


                                                    © National Instruments 767

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:767 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:768 ordinal=768 -->
## Functions

Functions


      Option       Description

                       Determines if an input falls in the range Minimum and Maximum specify.

                                 • Out of range—

                       Determines if an input falls out of the range Minimum and Maximum specify.

                                 • Minimum—

                          Specifies the minimum value of the In range and Out of range comparisons. The
                        Express VI includes Minimum in the range. The default is 0.

                                 • Maximum—

                          Specifies the maximum value of the In range and Out of range comparisons. The
                        Express VI includes Maximum in the range. The default is 1.

                    Contains the following options:

                                 • Second signal input—

                     Compares the Operand 1 input of the Express VI to a second signal input as
                     opposed to a value you specify in Value or the Constant Value to Compare
                        Against input. Select this option to include the Operand 2 input on the Express
                                VI.

                                       If Operand 1 and Operand 2 are the same size, each item in Operand 1 is
                     compared to the corresponding item in Operand 2. If Operand 1 and Operand 2
                         are of different sizes, all the items in Operand 1 are compared to the first item in      Comparison
                     Operand 2.       Inputs

                                 • Value—

                     Compares the Operand 1 input to a constant value you specify. The default is 0. If
                     you wire the Constant Value to Compare Against input, the VI uses the value
                          that this input specifies instead.

           ◦ Point value—

                               Specifies the constant value with which to compare the Operand 1 input.
                        The default is 0.


768   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:768 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:769 ordinal=769 -->
## Functions

Functions


Option       Description

        ◦ Timestamp value—

                       Specifies the timestamp to apply to the signal.

                      This option is available only if you place a checkmark in the Timestamp
                     checkbox.

        ◦ Delta time value—

                       Specifies the constant value with which to compare the Operand 1 input.
                  The default is 0.

        ◦ Number of points value—

                       Specifies the number of points to compare. The default is 0.

        ◦ Signal name value—

                       Specifies the name of the signal.

             Contains the following options:

                      • One result per data point—

                 Returns one result per data point. This option is available only when you select
                Data points from the Items to Compare pull-down menu.

                      • One result per channel—

                 Returns one result per channel. When you select Data points from the Items to
Result         Compare pull-down menu, One result per channel returns 1 only if all data
                  points in the channel pass the specified comparison. If any point fails, it returns
                     0.

                      • One result for all channels—

                 Returns one result for all the channels. When you select Data points from the
                Items to Compare pull-down menu, One result for all channels returns 1 only if
                       all data points in the channels pass the specified comparison. If any point fails, it
                  returns 0.


                                                    © National Instruments 769

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:769 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:770 ordinal=770 -->
## Functions

Functions


      Option       Description

                                 •  Invert result—

                           Inverts the outputs.

                    Contains the following option:

                                 • Change Express VI name to name of function—
       Result
     Name          Changes the name of the Express VI on the block diagram to the name of the
                         function you select in the Comparison Condition section of the configuration
                         dialog box.


                     Displays the input signal.

       Input Signal   If you wire data to the Express VI and run it, Input Signal displays real data. If you
                     close and reopen the Express VI, Input Signal displays sample data until you run the
                    Express VI again.


                    Contains the following options:

       Result           If you wire data to the Express VI and run the VI, Result Preview displays real data. If
      Preview     you close and reopen the Express VI, Result Preview displays sample data until you
                   run the VI again. If the cutoff frequency values are invalid, Result Preview does not
                     display valid data.


     Inputs/Outputs

            •       error in (no error) —

           Describes error conditions that occur before this node runs.

            •     Operand 2 —

           Specifies the second signal input for comparison. This input is available only when you select
         Second signal input in the configuration dialog box.

            •      Constant Value to Compare Against —

770   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:770 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:771 ordinal=771 -->
## Functions

Functions


     Specifies the constant value with which to compare the Operand 1 input. If Constant Value to
   Compare Against is not wired, the VI uses the Value specified in the configuration dialog box.

   •     Operand 1 —

     Specifies the first input for comparison.

   •       Invert Output —

     Inverts the outputs.

   •      Result —

    Returns the resulting data based on the configuration of the Express VI.

   •       error out —

    Contains error information. This output provides standard error out functionality.


Components

Specifies the timestamp to apply to the signal.

Specifies the name of the signal.

Specifies the number of points to compare. The default is 0.

Specifies the constant value with which to compare the Operand 1 input. The default
is 0.

Contains the following options:

Displays the input signal.

Contains the following options:

Inverts the outputs.

Returns one result for all the channels. When you select Data points from the Items to
Compare pull-down menu, One result for all channels returns 1 only if all data points

                                                    © National Instruments 771

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:771 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:772 ordinal=772 -->
## Functions

Functions

      in the channels pass the specified comparison. If any point fails, it returns 0.

     Returns one result per channel. When you select Data points from the Items to
    Compare pull-down menu, One result per channel returns 1 only if all data points in
     the channel pass the specified comparison. If any point fails, it returns 0.

     Returns one result per data point. This option is available only when you select Data
     points from the Items to Compare pull-down menu.

     Compares the Operand 1 input to a constant value you specify. The default is 0. If you
     wire the Constant Value to Compare Against input, the VI uses the value that this
     input specifies instead.

     Compares the Operand 1 input of the Express VI to a second signal input as opposed to
     a value you specify in Value or the Constant Value to Compare Against input. Select
      this option to include the Operand 2 input on the Express VI.

      Specifies the constant value with which to compare the Operand 1 input. The default
       is 0.

      Specifies the level of tolerance to use when determining if an input is Equal within
      tolerance. The default is 0.01.

      Specifies the maximum value of the In range and Out of range comparisons. The
     Express VI includes Maximum in the range. The default is 1.

      Specifies the minimum value of the In range and Out of range comparisons. The
     Express VI includes Minimum in the range. The default is 0.

     Determines if an input falls out of the range Minimum and Maximum specify.

     Determines if an input falls in the range Minimum and Maximum specify.

     Determines if the inputs are equal within the tolerance you specify in Tolerance.

     Determines if the first input is less than or equal to the second input.

     Determines if the first input is less than the second input.


772   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:772 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:773 ordinal=773 -->
## Functions

Functions

Determines if the first input is greater than or equal to the second input.

Determines if the first input is greater than the second input.

Determines if two inputs are unequal.

Determines if two inputs are equal.

Changes the name of the Express VI on the block diagram to the name of the function
you select in the Comparison Condition section of the configuration dialog box.

AssertAssert TypeType

Use the Assert Type VIs and functions in conjunction with the Type Specialization
structure for the following purposes:

  • Customizing sections of code in a malleable VI (.vim) for specific data types
  • Forcing a malleable VI to accept only data types that meet certain requirements
  • Forcing a malleable VI to decline specific data types


 Palette
               Description Object

             Has one or more subdiagrams, exactly one of which LabVIEW compiles and
                executes, depending on the order and the compilation result of the subdiagram.
             LabVIEW declines subdiagrams in order if they have syntax errors. LabVIEW accepts
               the first subdiagram that does not have syntax errors and ignores the remaining
 Type          subdiagrams. If all subdiagrams have syntax errors, this structure accepts the last
 Specialization subdiagram. Syntax errors are errors within the structure, such as broken wires, not
 Structure      errors caused by subVIs or other dependencies. Use this structure to customize
                sections of code in a malleable VI (.vim) for specific data types. You also can use this
                structure in conjunction with the Assert Type VIs and functions to force a malleable
                  VI to accept only a subset of the acceptable data types or to decline specific data
                types.

 Assert
               Breaks the calling VI unless the two input data types are identical, ignoring type
 Structural
                 definitions and type names.
 Type Match

                                                    © National Instruments 773

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:773 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:774 ordinal=774 -->
## Functions

Functions


       Palette                      Description
       Object

       Function

       Assert
        Structural     Breaks the calling VI if type is the same data type as any of the mismatch inputs,
      Type          ignoring type definitions and type names.
      Mismatch

                     Breaks the calling VI unless the input data is an error cluster.
       Assert Error
        Cluster Type   This VI does nothing at run time. Use this VI in conjunction with the Type
        VI              Specialization structure to customize sections of code in a malleable VI (.vim) for
                        error clusters or to force a malleable VI to accept error clusters only.


                     Breaks the calling VI unless value in is an array with the same number of
                    dimensions as array type.

       Assert Array   To check if each dimension has the same size, use the Assert Array Dimension Sizes
      Dimension      VI.
      Count VI
                      This VI does nothing at run time. Use this VI in conjunction with the Type
                       Specialization structure to customize sections of code in a malleable VI (.vim) for
                        certain array types or to force a malleable VI to accept certain array types only.


                     Breaks the calling VI unless value in is an array with the same number of
                    dimensions as array type and each dimension in value in has the same size
                    requirement (fixed, bounded, or variable-sized) and size (for fixed and bounded) as
                     the corresponding dimension in array type.
       Assert Array
      Dimension       If you do not need to compare the size of each dimension, use the Assert Array
        Sizes VI       Dimension Count VI.

                      This VI does nothing at run time. Use this VI in conjunction with the Type
                       Specialization structure to customize sections of code in a malleable VI (.vim) for
                        certain array types or to force a malleable VI to accept certain array types only.

       Assert Same
       or            Breaks the calling VI unless the input data is the same as or is a descendant of the
      Descendant

774   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:774 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:775 ordinal=775 -->
## Functions

Functions


Palette               Description
Object

               input class or interface.

               This VI does nothing at run time. Use this VI in conjunction with the Type
Type VI        Specialization structure to customize sections of code in a malleable VI (.vim) for
              the specified class or interface or the descendants of the specified class or interface
               or to force a malleable VI to accept the specified class or interface or the
              descendants of the specified class or interface only.


              Breaks the calling VI unless the input data is a scalar numeric or analog waveform
                type.Assert Scalar
Numeric Or               This VI does nothing at run time. Use this VI in conjunction with the Type
Waveform                Specialization structure to customize sections of code in a malleable VI (.vim) for
Type VI                scalar numeric or waveform types or to force a malleable VI to accept scalar
             numeric or waveform types only.


              Breaks the calling VI unless the input data is a scalar numeric type.
Assert Scalar
Numeric Type  This VI does nothing at run time. Use this VI in conjunction with the Type
VI              Specialization structure to customize sections of code in a malleable VI (.vim) for
                scalar numeric types or to force a malleable VI to accept scalar numeric types only.


              Breaks the calling VI unless the input data is a non-complex numeric or analog
             waveform type.Assert Real
Numeric Or               This VI does nothing at run time. Use this VI in conjunction with the Type
Waveform                Specialization structure to customize sections of code in a malleable VI (.vim) for
Type VI             non-complex numeric or waveform types or to force a malleable VI to accept non-
             complex numeric or analog waveform types only.


              Breaks the calling VI unless the input data is a non-complex numeric type.Assert Real
Numeric Type               This VI does nothing at run time. Use this VI in conjunction with the Type
VI                Specialization structure to customize sections of code in a malleable VI (.vim) for


                                                    © National Instruments 775

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:775 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:776 ordinal=776 -->
## Functions

Functions


       Palette                      Description
       Object

                   non-complex numeric types or to force a malleable VI to accept non-complex
                    numeric types only.


                     Breaks the calling VI unless the input data is a floating-point, complex floating-
                       point, or fixed-point numeric type.
       Assert
        Fractional     This VI does nothing at run time. Use this VI in conjunction with the Type
      Numeric Type  Specialization structure to customize sections of code in a malleable VI (.vim) for
        VI              floating-point, complex floating-point, or fixed-point numeric types or to force a
                     malleable VI to accept floating-point, complex floating-point, or fixed-point
                    numeric types only.


                     Breaks the calling VI unless the input data is a complex numeric type.
       Assert
      Complex       This VI does nothing at run time. Use this VI in conjunction with the Type
      Numeric Type  Specialization structure to customize sections of code in a malleable VI (.vim) for
        VI           complex numeric types or to force a malleable VI to accept complex numeric types
                        only.


                     Breaks the calling VI unless the input data is a floating-point or complex floating-
       Assert         point numeric type.
        Floating-
       Point          This VI does nothing at run time. Use this VI in conjunction with the Type
      Numeric Type  Specialization structure to customize sections of code in a malleable VI (.vim) for
        VI              floating-point or complex floating-point numeric types or to force a malleable VI to
                     accept floating-point or complex floating-point numeric types only.


                     Breaks the calling VI unless the input data is a non-complex floating-point numeric
       Assert Real     type.
        Floating-
       Point          This VI does nothing at run time. Use this VI in conjunction with the Type
      Numeric Type  Specialization structure to customize sections of code in a malleable VI (.vim) for
        VI            non-complex floating-point numeric types or to force a malleable VI to accept non-
                   complex floating-point numeric types only.


776   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:776 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:777 ordinal=777 -->
## Functions

Functions


 Palette               Description
 Object

               Breaks the calling VI unless the input data is an integer numeric type.

 Assert Integer  This VI does nothing at run time. Use this VI in conjunction with the Type
 Type VI        Specialization structure to customize sections of code in a malleable VI (.vim) for
                integer numeric types or to force a malleable VI to accept integer numeric types
                 only.


               Breaks the calling VI unless the input data is a signed integer numeric type.
 Assert Signed                This VI does nothing at run time. Use this VI in conjunction with the Type
 Integer Type                Specialization structure to customize sections of code in a malleable VI (.vim) for
 VI               signed integer numeric types or to force a malleable VI to accept signed integer
              numeric types only.


               Breaks the calling VI unless the input data is an unsigned integer numeric type.
 Assert
 Unsigned      This VI does nothing at run time. Use this VI in conjunction with the Type
 Integer Type   Specialization structure to customize sections of code in a malleable VI (.vim) for
 VI            unsigned integer numeric types or to force a malleable VI to accept unsigned
                integer numeric types only.


               Breaks the calling VI unless the input data is a fixed-point numeric type.
 Assert Fixed-
 Point          This VI does nothing at run time. Use this VI in conjunction with the Type
 Numeric Type  Specialization structure to customize sections of code in a malleable VI (.vim) for
 VI              fixed-point numeric data types or to force a malleable VI to accept fixed-point
              numeric types only.


TypeType SpecializationSpecialization StructureStructure

Has one or more subdiagrams, exactly one of which LabVIEW compiles and executes,
depending on the order and the compilation result of the subdiagram. LabVIEW
declines subdiagrams in order if they have syntax errors. LabVIEW accepts the first
subdiagram that does not have syntax errors and ignores the remaining subdiagrams.

                                                    © National Instruments 777

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:777 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:778 ordinal=778 -->
## Functions

Functions

         If all subdiagrams have syntax errors, this structure accepts the last subdiagram.
     Syntax errors are errors within the structure, such as broken wires, not errors caused
     by subVIs or other dependencies. Use this structure to customize sections of code in a
     malleable VI (.vim) for specific data types. You also can use this structure in
     conjunction with the Assert Type VIs and functions to force a malleable VI to accept
     only a subset of the acceptable data types or to decline specific data types.

      After you create a Type Specialization structure, you can add, duplicate, rearrange, or
      delete the subdiagrams. To scroll through the available subdiagrams, click the
     decrement and increment arrows in the selector label. You also can remove the
      structure without deleting objects in the structure.

     The Type Specialization structure allows you to disable specific sections of code on the
     block diagram based on compilation results. To disable specific sections of code on
     the block diagram based on some user-defined condition, use the Conditional Disable
      structure. To disable a section of a block diagram, use the Diagram Disable structure.

     To switch to a Conditional Disable or Diagram Disable structure, right-click the border
      of the Type Specialization structure and select Replace with Conditional Disable
     Structure or Replace with Diagram Disable Structure from the shortcut menu.


    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Malleable VIs\Type Specialization
       Structure\Malleable VIs - Type Specialization
       Structure.lvproj

     AssertAssert StructuralStructural TypeType MatchMatch FunctionFunction

     Breaks the calling VI unless the two input data types are identical, ignoring type
      definitions and type names.


778   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:778 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:779 ordinal=779 -->
## Functions

Functions

This function does nothing at run time. Use this function in conjunction with the Type
Specialization structure to customize sections of code in a malleable VI (.vim) for
specific data types or to force a malleable VI to accept only data types that meet
certain requirements.


Inputs/Outputs

   •      anything —

    anything specifies the first input data type.

    LabVIEW ignores any run-time value on the wire connected to this input.

   •      reference —

    reference specifies the second input data type, which you want to compare against x.

    To set the data type of this input, wire a constant or control of the desired data type to reference.
    LabVIEW ignores any run-time value on the wire connected to this input.


For data types with subtypes, such as arrays, clusters, and some refnums, this function
also checks array dimensions and subtypes, but not the subtype names. For example,
this function causes the calling VI to break if one input data type is 1D array of variant
and the other is 2D array of variant or 1D array of scalars. If one input data type is a
cluster of a string named lecture and an unsigned 8-bit integer named number of
students, while the other input data type is a cluster of a string named lecture 1
and an unsigned 8-bit integer named size, the calling VI does not break because the
subtypes of the two clusters are the same even though the subtype names are
different.

AssertAssert StructuralStructural TypeType MismatchMismatch

Breaks the calling VI if type is the same data type as any of the mismatch inputs,
ignoring type definitions and type names.

This function does nothing at run time. Use this function in conjunction with the Type

                                                    © National Instruments 779

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:779 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:780 ordinal=780 -->
## Functions

Functions

      Specialization structure to customize sections of code in a malleable VI (.vim) for
      specific data types or to force a malleable VI to decline specific data types.


     Inputs/Outputs

            •      type —

          type specifies the input data type.

         LabVIEW ignores any run-time value on the wire connected to this input.

            •     mismatch —

         mismatch specifies the data type that you want to compare against type.

         To set the data type of this input, wire a constant or control of the desired data type to
          mismatch. Wire one data type to each mismatch input you want to compare against type.
         LabVIEW ignores any run-time value on the wire connected to this input.


     Avoiding Unexpected Behavior in Your Malleable VI

     To avoid unexpected behavior in your malleable VI, you can use this function to force a
      specific subdiagram of your Type Specialization structure to decline data types that
     you intend to be accepted by previous subdiagrams.

     For example, you create code in the first subdiagram of a Type Specialization structure
      for data type A in a malleable VI. When the input data type is A, you expect the Type
      Specialization structure to accept the first subdiagram. However, if the code in the first
     subdiagram breaks for reasons unrelated to the data type, for example, due to a
     broken subVI, the Type Specialization structure declines the first subdiagram and
     attempts to compile the remaining subdiagrams in order. A problem that can arise in
      this situation is when one of the remaining subdiagrams is also acceptable with data
     type A. In this case, the malleable VI is unbroken but may behave in an unexpected
    way for data type A.


780   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:780 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:781 ordinal=781 -->
## Functions

Functions

Handling Data Types with Subtypes

For data types with subtypes, such as arrays, clusters, and some refnums, this function
also checks array dimensions and subtypes, but not the subtype names. For example,
the calling VI does not break if the input data type is 1D array of variant and the
specified mismatch data type is 2D array of variant or 1D array of scalars. If the input
data type is a cluster of a string named lecture and an unsigned 8-bit integer named
number of students, while the specified mismatch data type is a cluster of a
string named lecture 1 and an unsigned 8-bit integer named size, the calling VI
breaks because the subtypes of the two clusters are the same even though the subtype
names are different.

AssertAssert ErrorError ClusterCluster TypeType VIVI

Breaks the calling VI unless the input data is an error cluster.

This VI does nothing at run time. Use this VI in conjunction with the Type Specialization
structure to customize sections of code in a malleable VI (.vim) for error clusters or to
force a malleable VI to accept error clusters only.

This VI does nothing at run time. Use this VI in conjunction with the Type Specialization
structure to customize sections of code in a malleable VI (.vim) for error clusters or to
force a malleable VI to accept error clusters only.


Inputs/Outputs

   •      value in —

    value in specifies the input data.

   •      value out —

    value out returns the input data if value in is an error cluster. Otherwise, this output returns an
    empty error cluster.


                                                    © National Instruments 781

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:781 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:782 ordinal=782 -->
## Functions

Functions

     AssertAssert ArrayArray DimensionDimension CountCount VIVI

     Breaks the calling VI unless value in is an array with the same number of dimensions
     as array type.

     To check if each dimension has the same size, use the Assert Array Dimension Sizes VI.

      This VI does nothing at run time. Use this VI in conjunction with the Type Specialization
      structure to customize sections of code in a malleable VI (.vim) for certain array types
     or to force a malleable VI to accept certain array types only.


     Inputs/Outputs

            •      array type —

           array type specifies the input comparison array with the requirements that the input data must
          meet.

           This input accepts arrays of any data type. To set the data type of this input, wire a constant or
           control of the desired data type to array type. LabVIEW ignores any data in the constant or
           control wired to array type.

            •      value in —

          value in specifies the input data.

           This input accepts arrays that meet the requirements of array type.

            •      value out —

          value out returns the input data if value in is an array that meets the requirements. Otherwise,
            this output returns an empty array of array type.


     AssertAssert ArrayArray DimensionDimension SizesSizes VIVI

     Breaks the calling VI unless value in is an array with the same number of dimensions

782   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:782 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:783 ordinal=783 -->
## Functions

Functions

as array type and each dimension in value in has the same size requirement (fixed,
bounded, or variable-sized) and size (for fixed and bounded) as the corresponding
dimension in array type.

If you do not need to compare the size of each dimension, use the Assert Array
Dimension Count VI.

This VI does nothing at run time. Use this VI in conjunction with the Type Specialization
structure to customize sections of code in a malleable VI (.vim) for certain array types
or to force a malleable VI to accept certain array types only.


Inputs/Outputs

   •      array type —

    array type specifies the input comparison array with the requirements that the input data must
    meet.

    This input accepts arrays of any data type. To set the data type of this input, wire a constant or
    control of the desired data type to array type. LabVIEW ignores any data in the constant or
    control wired to array type.

   •      value in —

    value in specifies the input data.

    This input accepts arrays that meet the requirements of array type.

   •      value out —

    value out returns the input data if value in is an array that meets the requirements. Otherwise,
     this output returns an empty array of array type.


AssertAssert SameSame oror DescendantDescendant TypeType VIVI

Breaks the calling VI unless the input data is the same as or is a descendant of the

                                                    © National Instruments 783

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:783 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:784 ordinal=784 -->
## Functions

Functions

     input class or interface.

      This VI does nothing at run time. Use this VI in conjunction with the Type Specialization
      structure to customize sections of code in a malleable VI (.vim) for the specified class
     or interface or the descendants of the specified class or interface or to force a
     malleable VI to accept the specified class or interface or the descendants of the
      specified class or interface only.


     Inputs/Outputs

            •      ancestor type —

          ancestor type specifies the input class or interface with the requirements that the input data
         must meet.

           This input accepts any class or interface. To set the class or interface of this input, wire a
          constant or control of the desired class or interface to ancestor type. LabVIEW ignores any data
            in the constant or control wired to ancestor type.

            •      value in —

          value in specifies the input data.

           This input accepts the class or interface of ancestor type or descendants of ancestor type.

            •      value out —

          value out returns the input data if value in meets the requirements. Otherwise, this output
           returns the default value of ancestor type.


     AssertAssert ScalarScalar NumericNumeric OrOr WaveformWaveform TypeType VIVI

     Breaks the calling VI unless the input data is a scalar numeric or analog waveform
      type.

      This VI does nothing at run time. Use this VI in conjunction with the Type Specialization

784   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:784 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:785 ordinal=785 -->
## Functions

Functions

structure to customize sections of code in a malleable VI (.vim) for scalar numeric or
waveform types or to force a malleable VI to accept scalar numeric or waveform types
only.


Inputs/Outputs

   •      value in —

    value in specifies the input data.

    This input accepts any scalar numeric or waveform data type.

   •      value out —

    value out returns the input data if value in is a scalar numeric or analog waveform type.
    Otherwise, this output returns a double-precision floating-point number 0.


AssertAssert ScalarScalar NumericNumeric TypeType VIVI

Breaks the calling VI unless the input data is a scalar numeric type.

This VI does nothing at run time. Use this VI in conjunction with the Type Specialization
structure to customize sections of code in a malleable VI (.vim) for scalar numeric
types or to force a malleable VI to accept scalar numeric types only.


Inputs/Outputs

   •      value in —

    value in specifies the input data.

    This input accepts any scalar numeric data type.


                                                    © National Instruments 785

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:785 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:786 ordinal=786 -->
## Functions

Functions

            •      value out —

          value out returns the input data if value in is a scalar numeric type. Otherwise, this output
           returns a double-precision floating-point number 0.


     AssertAssert RealReal NumericNumeric OrOr WaveformWaveform TypeType VIVI

     Breaks the calling VI unless the input data is a non-complex numeric or analog
     waveform type.

      This VI does nothing at run time. Use this VI in conjunction with the Type Specialization
      structure to customize sections of code in a malleable VI (.vim) for non-complex
     numeric or waveform types or to force a malleable VI to accept non-complex numeric
     or analog waveform types only.


     Inputs/Outputs

            •      value in —

          value in specifies the input data.

           This input accepts any non-complex numeric or waveform data type.

            •      value out —

          value out returns the input data if value in is a non-complex numeric or analog waveform type.
          Otherwise, this output returns a double-precision floating-point number 0.


     AssertAssert RealReal NumericNumeric TypeType VIVI

     Breaks the calling VI unless the input data is a non-complex numeric type.

      This VI does nothing at run time. Use this VI in conjunction with the Type Specialization
      structure to customize sections of code in a malleable VI (.vim) for non-complex
     numeric types or to force a malleable VI to accept non-complex numeric types only.

786   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:786 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:787 ordinal=787 -->
## Functions

Functions


Inputs/Outputs

   •      value in —

    value in specifies the input data.

    This input accepts any non-complex numeric data type.

   •      value out —

    value out returns the input data if value in is a non-complex numeric type. Otherwise, this
    output returns a double-precision floating-point number 0.


AssertAssert FractionalFractional NumericNumeric TypeType VIVI

Breaks the calling VI unless the input data is a floating-point, complex floating-point,
or fixed-point numeric type.

This VI does nothing at run time. Use this VI in conjunction with the Type Specialization
structure to customize sections of code in a malleable VI (.vim) for floating-point,
complex floating-point, or fixed-point numeric types or to force a malleable VI to
accept floating-point, complex floating-point, or fixed-point numeric types only.


Inputs/Outputs

   •      value in —

    value in specifies the input data.

    This input accepts any floating-point, complex floating-point, or fixed-point numeric data type.

   •      value out —


                                                    © National Instruments 787

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:787 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:788 ordinal=788 -->
## Functions

Functions


          value out returns the input data if value in is a floating-point, complex floating-point, or fixed-
           point numeric type. Otherwise, this output returns a double-precision floating-point number 0.


     AssertAssert ComplexComplex NumericNumeric TypeType VIVI

     Breaks the calling VI unless the input data is a complex numeric type.

      This VI does nothing at run time. Use this VI in conjunction with the Type Specialization
      structure to customize sections of code in a malleable VI (.vim) for complex numeric
     types or to force a malleable VI to accept complex numeric types only.


     Inputs/Outputs

            •      value in —

          value in specifies the input data.

           This input accepts any complex numeric data type.

            •      value out —

          value out returns the input data if value in is a complex numeric type. Otherwise, this output
           returns a complex double-precision number 0 +0 i.

           This output can return any complex numeric type.


     AssertAssert Floating-PointFloating-Point NumericNumeric TypeType VIVI

     Breaks the calling VI unless the input data is a floating-point or complex floating-point
     numeric type.

      This VI does nothing at run time. Use this VI in conjunction with the Type Specialization
      structure to customize sections of code in a malleable VI (.vim) for floating-point or
     complex floating-point numeric types or to force a malleable VI to accept floating-


788   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:788 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:789 ordinal=789 -->
## Functions

Functions

point or complex floating-point numeric types only.


Inputs/Outputs

   •      value in —

    value in specifies the input data.

    This input accepts any floating-point or complex floating-point numeric data type.

   •      value out —

    value out returns the input data if value in is a floating-point or complex floating-point numeric
     type. Otherwise, this output returns a double-precision floating-point number 0.


AssertAssert RealReal Floating-PointFloating-Point NumericNumeric TypeType VIVI

Breaks the calling VI unless the input data is a non-complex floating-point numeric
type.

This VI does nothing at run time. Use this VI in conjunction with the Type Specialization
structure to customize sections of code in a malleable VI (.vim) for non-complex
floating-point numeric types or to force a malleable VI to accept non-complex floating-
point numeric types only.


Inputs/Outputs

   •      value in —

    value in specifies the input data.

    This input accepts any non-complex floating-point numeric data type.


                                                    © National Instruments 789

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:789 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:790 ordinal=790 -->
## Functions

Functions

            •      value out —

          value out returns the input data if value in is a non-complex floating-point numeric type.
          Otherwise, this output returns a double-precision floating-point number 0.


     AssertAssert IntegerInteger TypeType VIVI

     Breaks the calling VI unless the input data is an integer numeric type.

      This VI does nothing at run time. Use this VI in conjunction with the Type Specialization
      structure to customize sections of code in a malleable VI (.vim) for integer numeric
     types or to force a malleable VI to accept integer numeric types only.


     Inputs/Outputs

            •      value in —

          value in specifies the input data.

           This input accepts any integer numeric data type.

            •      value out —

          value out returns the input data if value in is an integer numeric type. Otherwise, this output
           returns a 32-bit signed integer 0.


     AssertAssert SignedSigned IntegerInteger TypeType VIVI

     Breaks the calling VI unless the input data is a signed integer numeric type.

      This VI does nothing at run time. Use this VI in conjunction with the Type Specialization
      structure to customize sections of code in a malleable VI (.vim) for signed integer
     numeric types or to force a malleable VI to accept signed integer numeric types only.


790   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:790 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:791 ordinal=791 -->
## Functions

Functions


Inputs/Outputs

   •      value in —

    value in specifies the input data.

    This input accepts any signed integer numeric data type.

   •      value out —

    value out returns the input data if value in is a signed integer numeric type. Otherwise, this
    output returns a 32-bit signed integer 0.


AssertAssert UnsignedUnsigned IntegerInteger TypeType VIVI

Breaks the calling VI unless the input data is an unsigned integer numeric type.

This VI does nothing at run time. Use this VI in conjunction with the Type Specialization
structure to customize sections of code in a malleable VI (.vim) for unsigned integer
numeric types or to force a malleable VI to accept unsigned integer numeric types only.


Inputs/Outputs

   •      value in —

    value in specifies the input data.

    This input accepts any unsigned integer numeric data type.

   •      value out —

    value out returns the input data if value in is an unsigned integer numeric type. Otherwise, this
    output returns a 32-bit unsigned integer 0.


                                                    © National Instruments 791

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:791 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:792 ordinal=792 -->
## Functions

Functions

     AssertAssert Fixed-PointFixed-Point NumericNumeric TypeType VIVI

     Breaks the calling VI unless the input data is a fixed-point numeric type.

      This VI does nothing at run time. Use this VI in conjunction with the Type Specialization
      structure to customize sections of code in a malleable VI (.vim) for fixed-point
     numeric data types or to force a malleable VI to accept fixed-point numeric types only.

      This VI does nothing at run time. Use this VI in conjunction with the Type Specialization
      structure to customize sections of code in a malleable VI (.vim) for fixed-point
     numeric data types or to force a malleable VI to accept fixed-point numeric types only.


     Inputs/Outputs

            •      value in —

          value in specifies the input data.

            •      value out —

          value out returns the input data if value in is a fixed-point numeric type. Otherwise, this output
           returns a fixed-point number 0.

      IsIs ValueValue ChangedChanged

     Returns TRUE if this is the first call of this VI or if the input value is different from the
     value when this VI was last called.


     Inputs/Outputs

            •      value —


792   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:792 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:793 ordinal=793 -->
## Functions

Functions


    value specifies the value to check. This input accepts any data type.

   •     changed or first call? —

    changed or first call? returns TRUE if this is the first call of this VI or if the value changed since
    the last time this VI was called. Otherwise, this output returns FALSE.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Malleable VIs\Basics\Malleable VIs
   Basics.lvproj

IsIs PathPath andand NotNot Empty?Empty?

Returns TRUE if path is any value other than <Not A Path> or an empty path.
Otherwise, this VI returns FALSE.


Inputs/Outputs

   •      path —

    path specifies the path you want to check.

   •        Is Path and Not Empty? —

     Is Path and Not Empty? returns TRUE if path is any value other than <Not A Path> or an
    empty path. Otherwise, Is Path and Not Empty? returns FALSE.

Fixed-PointFixed-Point Overflow?Overflow? FunctionFunction

Returns TRUE if FXP includes an overflow status and FXP is the result of an operation
that overflowed. Otherwise, this function returns FALSE.

                                                    © National Instruments 793

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:793 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:794 ordinal=794 -->
## Functions

Functions


     Inputs/Outputs

            •     FXP —

         FXP specifies a fixed-point number.

            •      overflow? —

          overflow? is TRUE if FXP includes an overflow status and FXP is the result of an operation that
           overflowed.

                 If FXP does not include an overflow status, or if FXP includes an overflow status but is not the
            result of an operation that overflowed, overflow? is FALSE.

   WaveformWaveform

     Use the Waveform VIs and functions to build waveforms that include the waveform
      values, channel information, and timing information, and to set and retrieve waveform
      attributes and components.

     The VIs and functions on this palette can return waveform error codes.


       Palette
                     Description
       Object

       Get
                    Returns the analog waveform you specify. You specify components by clicking on the
      Waveform
                     center of the output terminal and selecting the component you want.
      Components

                     Builds an analog waveform or modifies an existing waveform. If you do not wire the
       Build       waveform input, the function creates a new waveform based on the components
      Waveform    you wire. If you wire the waveform input, the function modifies the waveform based
                 on the components you wire.

       Set         Adds or replaces a waveform attribute. You can use any type of data for the value of


794   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:794 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:795 ordinal=795 -->
## Functions

Functions


Palette              Description
Object

Waveform
Attribute     the attribute.
Function

Get
Waveform    Retrieves the names and values of all attributes or the value of a single attribute,
Attribute     depending on whether you wire the name parameter.
Function

Analog to     Converts analog waveform to a digital waveform or digital data. You must manually
Digital        select the polymorphic instance you want to use.


Digital to     Converts a digital waveform or digital data to analog waveform. You must manually
Analog        select the polymorphic instance you want to use.


              Selects one waveform out of an array of analog or digital waveforms by array indexIndex              or channel name. The data types you wire to the waveform array and index inputs
Waveform           and the data type of the Y component of the analog waveform determine theArray            polymorphic instance to use.


             Replaces all dt values with the dt value of the waveform at index position in
Copy       waveforms in. The data type you wire to the waveforms in input and the data type of
Waveform dt  the Y component of the analog waveform determine the polymorphic instance to
              use.


             Replaces all the time stamp values (t0) in waveforms in with the value of the index
Align
            element in the array. The data type you wire to the waveforms in input and the data
Waveform
             type of the Y component of the analog waveform determine the polymorphic
Timestamps
              instance to use.


Get
              Retrieves a subset of a waveform at a specified time or index. You must manually
Waveform
               select the polymorphic instance you want to use.
Subset


                                                    © National Instruments 795

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:795 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:796 ordinal=796 -->
## Functions

Functions


       Palette                     Description
       Object

                    Returns the ending time value of waveform in. The formula used is xf = x0 + duration       Get Final                      of waveform in. Wire data to the waveform in input to determine the polymorphic      Time Value                     instance to use or manually select the instance.


                 Computes the duration of waveform in using the following equation: duration =
      Waveform                     (#samples-1) × dx. Wire data to the waveform in input to determine the polymorphic       Duration
                     instance to use or manually select the instance.


                       Multiplies the delta t component of the waveform by the specified scale factor.
                      Generally, this lengthens or shortens the sample rate of the waveform. The data type       Scale Delta t
                  you wire to the waveform in input and the data type of the Y component of the
                   analog waveform determine the polymorphic instance to use.


                    Returns the X and Y value of a waveform or digital data set. The data type you wire to
       Get XY Value  the waveform in input and the data type of the Y component of the analog waveform
                   determine the polymorphic instance to use.


       Get          Creates an array of waveform time stamps. Each element in the array is the time
      Waveform    stamp for each data value in the waveform. Wire data to the waveform in input to
      Time Array   determine the polymorphic instance to use or manually select the instance.


       Analog      Use the Analog Waveform VIs and functions to perform arithmetic and comparison
      Waveform    functions on waveforms.


        Digital       Use the Digital Waveform VIs and functions to perform operations on digital
      Waveform    waveforms and digital data.


      Waveform    Use the Waveform File I/O VIs to write waveform data to and read waveform data
         File I/O      from files.


796   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:796 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:797 ordinal=797 -->
## Functions

Functions

GetGet WaveformWaveform ComponentsComponents

Returns the analog waveform you specify. You specify components by clicking on the
center of the output terminal and selecting the component you want.


Inputs/Outputs

   •     waveform —

    waveform is the waveform from which you want to retrieve components.

   •       t0 —

    t0 returns the trigger time of the waveform.

   •      dt —

    dt returns the time interval in seconds between data points in the waveform.

   •      Y —

    Y returns the data values of the waveform.

   •       attributes —

    attributes returns the names and values of all waveform attributes.

    You also can use the Get Waveform Attribute VI to retrieve the names and values of all attributes
    or the value of a single attribute.

BuildBuild WaveformWaveform

Builds an analog waveform or modifies an existing waveform. If you do not wire the
waveform input, the function creates a new waveform based on the components you
wire. If you wire the waveform input, the function modifies the waveform based on the
components you wire.


                                                    © National Instruments 797

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:797 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:798 ordinal=798 -->
## Functions

Functions


     Inputs/Outputs

            •     waveform —

         waveform is the analog waveform you want to edit. If you do not wire an existing waveform, the
           function creates a new waveform based on the components you wire.

            •       t0 —

           t0 specifies the start time of the waveform.

            •      dt —

          dt specifies the time interval in seconds between data points in the waveform.

            •      Y —

         Y specifies the data values of the waveform.

            •       attributes —

           attributes sets the names and values of all waveform attributes.

         You also can use the Set Waveform Attribute function to set the name and value of a single
            attribute.

            •      output waveform —

         waveform is the resulting waveform. If you did not wire an existing waveform, this is a new
          waveform. If you wired an existing waveform, this is the edited waveform.

    SetSet WaveformWaveform AttributeAttribute FunctionFunction

     Adds or replaces a waveform attribute. You can use any type of data for the value of
     the attribute.


798   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:798 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:799 ordinal=799 -->
## Functions

Functions


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
new value, and replaced is TRUE. If the attribute in name does not exist already, the
function creates a new attribute. Some attributes are set by NI-DAQ and Express VIs.

The following table lists the waveform attributes set by NI-DAQ.


 Name     Attribute          Data   Acceptable Values   Description

                                                    © National Instruments 799

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:799 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:800 ordinal=800 -->
## Functions

Functions


                                Type

      Hardware                        Any value is        NI_DeviceNumber is the device
       Device    NI_DeviceNumber   String  acceptable for     number of the hardware producing
      Number                           NI_DeviceNumber.  the waveform.

                                      Any value is        NI_ChannelName is the name of the     Name of
               NI_ChannelName   String  acceptable for        virtual channel producing the      Channel                                       NI_ChannelName.   waveform.

                                                         NI_LineNames is the name of the
     Name of                         Any value is           digital line in the waveform. For more
        Digital    NI_LineNames      String  acceptable for      than one digital line, the function
        Line(s)                            NI_LineNames.      returns the line names in reverse
                                                                      order.

                                                    Volts, PSI, and so
                                                forth are       Unit for                                                   NI_UnitDescription is the units of
                  NI_UnitDescription  String  acceptable values       Data                                              measure for the waveform.                                                   for
                                              NI_UnitDescription.

     The following table lists the waveform attributes set by Express VIs.


                                      Data     Name       Attribute                       Acceptable Values       Description                                    Type

                                                                      NI_ExpStartTimeStamp is
                                                                          the time stamp of the first
                                                                  sample in the first
                                                                     waveform. In Express VIs,
                                                                                       this is set once per start
                                                                                 of the VI and does not
                                                                        change, even if waveform
                                             Any value is acceptable  data is generated in a
        Start                          Time
                  NI_ExpStartTimeStamp            for                      loop. In Express VIs,
      Timestamp                     stamp
                                                 NI_ExpStartTimeStamp. NI_ExpStartTimeStamp is
                                                                                 set according to the PC
                                                                             clock unless the
                                                                 waveform originates in
                                                                        NI-DAQ. When the
                                                                 waveform originates in
                                                                        NI-DAQ, NI-DAQ sets
                                                                       NI_ExpStartTimeStamp.

800   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:800 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:801 ordinal=801 -->
## Functions

Functions


                                                             NI_ExpTimeStamp is the
                                                                 time stamp of the first
                                                             sample in the waveform.
                                                                            In Express VIs,
                                                             NI_ExpTimeStamp is set
                               Time    Any value is acceptable  according to the PC clock Timestamp NI_ExpTimeStamp                               stamp    for NI_ExpTimeStamp.   unless the waveform
                                                                          originates in NI-DAQ.
                                                    When the waveform
                                                                          originates in NI-DAQ, NI-
                                                   DAQ sets
                                                               NI_ExpTimeStamp.

                                                                                                               If the value of                                       Use a single character
                                                               NI_ExpXDimension is t, t0                                                    for the
                                                          and dt are unchanged. If                                         NI_ExpXDimension                                                                   the value of                                                 value. Currently, only t
 X                                                             NI_ExpXDimension is f,            NI_ExpXDimension      String    for time and f for Dimension                                                          Express VIs interpret t0
                                            frequency are                                                          and dt as f0 and df. For all                                            supported. The value                                                                     other values, or unknown
                                                    for NI_ExpXDimension                                                                  dimension, t0 and dt are                                                             is case sensitive.                                                                        interpreted as X0 and dX.

                                                                                                               If and only if
                                    TRUE or FALSE are      NI_ExpXDimension is t,
 Relative             NI_ExpIsRelativeTime   Boolean  acceptable values for    Express VIs set t0 as a Time?                                              NI_ExpIsRelativeTime.   relative/absolute time
                                                           stamp value.

      Note Express VIs also use the attributes set by NI-DAQ. If the waveform does
       not originate in NI-DAQ, Express VIs add NI_ChannelName.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Create.vi


                                                    © National Instruments 801

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:801 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:802 ordinal=802 -->
## Functions

Functions

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

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •      duplicate waveform —

           duplicate waveform is the waveform data you input in waveform.

            •     names —

802   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:802 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:803 ordinal=803 -->
## Functions

Functions


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


                            Data Name     Attribute                 Acceptable Values        Description
                          Type

 Hardware                                               NI_DeviceNumber is the device
                                 Any value is acceptable
 Device    NI_DeviceNumber   String                     number of the hardware device
                                           for NI_DeviceNumber.
 Number                                                   producing the waveform.

                                                     NI_ChannelName is the name of
 Name of                         Any value is acceptable
          NI_ChannelName   String                          the virtual channel producing
 Channel                                  for NI_ChannelName.
                                                             the waveform.

 Name of
                                 Any value is acceptable   NI_LineNames is the name of
 Digital    NI_LineNames      String
                                           for NI_LineNames.       the digital line in the waveform.
 Line(s)


                                                    © National Instruments 803

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:803 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:804 ordinal=804 -->
## Functions

Functions


                                  Data     Name     Attribute                 Acceptable Values        Description
                                Type

                                                    Volts, PSI, and so forth       Unit for                                                       NI_UnitDescription is the units                  NI_UnitDescription  String  are acceptable values for       Data                                                              of measure for the waveform.                                              NI_UnitDescription.

     The following table lists the waveform attributes set by Express VIs.


                                      Data     Name       Attribute                       Acceptable Values       Description
                                    Type

                                                                      NI_ExpStartTimeStamp is
                                                                          the time stamp of the first
                                                                  sample in the first
                                                                     waveform. In Express VIs,
                                                                                       this is set once per start
                                                                                 of the VI and does not
                                                                        change, even if waveform
                                             Any value is acceptable  data is generated in a        Start                          Time
                  NI_ExpStartTimeStamp            for                      loop. In Express VIs,      Timestamp                     stamp                                                 NI_ExpStartTimeStamp. NI_ExpStartTimeStamp is
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
                                    Time    Any value is acceptable  according to the PC clock
      Timestamp NI_ExpTimeStamp
                                    stamp    for NI_ExpTimeStamp.   unless the waveform
                                                                                 originates in NI-DAQ.
                                                         When the waveform
                                                                                 originates in NI-DAQ, NI-
                                                        DAQ sets
                                                                    NI_ExpTimeStamp.


804   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:804 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:805 ordinal=805 -->
## Functions

Functions


                                 Data Name       Attribute                       Acceptable Values       Description
                               Type

                                                                                                               If the value of
                                                               NI_ExpXDimension is t, t0                                       Use a single character                                                          and dt are unchanged. If                                                    for the
                                                                   the value of                                         NI_ExpXDimension                                                               NI_ExpXDimension is f,                                                 value. Currently, only t X                                                                  Express VIs interpret t0            NI_ExpXDimension      String    for time and f for Dimension                                                 and dt as f0 and df. For all                                            frequency are
                                                                     other values, Express VIs                                            supported. The value                                                                           generically interpret t0                                                    for NI_ExpXDimension                                                          and dt as X0 and dX, but                                                             is case sensitive.                                                                      there is no effect
                                                                      otherwise.

                                                                                                               If and only if
                                    TRUE or FALSE are      NI_ExpXDimension is t, Relative
             NI_ExpIsRelativeTime   Boolean  acceptable values for    Express VIs set t0 as a Time?                                              NI_ExpIsRelativeTime.   relative/absolute time
                                                           stamp value.

      Note Express VIs also use the attributes set by NI-DAQ. If the waveform does
       not originate in NI-DAQ, Express VIs add NI_ChannelName.

AnalogAnalog toto DigitalDigital

Converts analog waveform to a digital waveform or digital data. You must manually
select the polymorphic instance you want to use.


  • DWDT Analog to Digital VI
  • DTbl Analog to Digital VI

To create digital data from an analog waveform or to graph an analog signal in a digital
waveform graph, you must convert the raw analog data into digital data or the digital
waveform data type. Use the Analog to Digital VI to convert the data to digital
waveform. Use the Get Waveform Components function to extract the digital data from

                                                    © National Instruments 805

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:805 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:806 ordinal=806 -->
## Functions

Functions

     the digital waveform.

     The block diagram below simulates the acquisition of a sine wave with an amplitude of
       5, which means the sine wave can contain values that range from –5 to 5. The Analog to
      Digital VI in this block diagram represents each value with 8 bits. The 8 bits can
     represent a peak-to-peak value of 10. The probe displays a portion of the resulting
     values in binary format.


    DWDTDWDT AnalogAnalog toto DigitalDigital VIVI

     Converts analog waveform to a digital waveform or digital data. You must manually
      select the polymorphic instance you want to use.


806   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:806 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:807 ordinal=807 -->
## Functions

Functions

Inputs/Outputs

   •      compress digital (T) —

    compress digital specifies whether to compress the digital waveform or digital data. The default
      is TRUE.

   •      analog waveform —

    analog waveform is the waveform you want to convert to digital waveform or digital data.

   •       resolution (16 bit) —

    resolution specifies the number of bits represented in the digital waveform or digital data.

   •       full-scale range (pk-pk) —

     full-scale range (pk-pk) specifies the total peak-to-peak range, or the difference between the
   minimum and maximum, for the digital waveform or digital data. For example, if the maximum
    range of a waveform is 1 and the minimum is –1, the full-scale range for the waveform is 2. The
     default is 2.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

       If an error occurred before this node runs, this node outputs an empty waveform.

   •      data format (offset binary) —

    data format specifies which binary representation you want to use for the digital waveform or
     digital data.

    0 unsigned binary—Converts the data to unsigned binary.
      offset binary (default)—The largest negative full-scale value is represented by all zeros, and the
    1 largest positive full-scale value is represented by all ones. Zero-scale is represented by a one
     (MSB) followed by all zeros, for example, binary 1000.
      2's complement—Uses two's complement format, which is a common format for representing
    2
     signed binary values. This format is similar to offset binary, but the MSB is inverted.

   •       digital waveform —


                                                    © National Instruments 807

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:807 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:808 ordinal=808 -->
## Functions

Functions


            digital waveform returns the waveform that results from the conversion of analog waveform.

            •       resolution (out) —

           resolution (out) returns the number of bits represented in the digital waveform or digital data.

            •       full-scale range (out) —

            full-scale range (out) returns the total peak-to-peak range for the digital waveform or digital
           data.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


     To create digital data from an analog waveform or to graph an analog signal in a digital
     waveform graph, you must convert the raw analog data into digital data or the digital
     waveform data type. Use the Analog to Digital VI to convert the data to digital
     waveform. Use the Get Waveform Components function to extract the digital data from
     the digital waveform.

     The block diagram below simulates the acquisition of a sine wave with an amplitude of
       5, which means the sine wave can contain values that range from –5 to 5. The Analog to
      Digital VI in this block diagram represents each value with 8 bits. The 8 bits can
     represent a peak-to-peak value of 10. The probe displays a portion of the resulting
     values in binary format.


808   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:808 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:809 ordinal=809 -->
## Functions

Functions


DTblDTbl AnalogAnalog toto DigitalDigital VIVI

Converts analog waveform to a digital waveform or digital data. You must manually
select the polymorphic instance you want to use.


Inputs/Outputs

   •      compress digital (T) —

    compress digital specifies whether to compress the digital waveform or digital data. The default
      is TRUE.

   •      analog waveform —

    analog waveform is the waveform you want to convert to digital waveform or digital data.


                                                    © National Instruments 809

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:809 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:810 ordinal=810 -->
## Functions

Functions

            •       resolution (16 bit) —

           resolution specifies the number of bits represented in the digital waveform or digital data.

            •        full scale range (pk-pk) —

            full-scale range (pk-pk) specifies the total peak-to-peak range, or the difference between the
        minimum and maximum, for the digital waveform or digital data. For example, if the maximum
          range of a waveform is 1 and the minimum is –1, the full-scale range for the waveform is 2. The
           default is 2.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. With the following
           exception, this input provides standard error in functionality.

                 If an error occurred before this node runs, this node outputs an empty waveform.

            •      data format (offset binary) —

          data format specifies which binary representation you want to use for the digital waveform or
             digital data.

          0 unsigned binary—Converts the data to unsigned binary.
             offset binary (default)—The largest negative full-scale value is represented by all zeros, and the
          1 largest positive full-scale value is represented by all ones. Zero-scale is represented by a one
           (MSB) followed by all zeros, for example, binary 1000.
             2's complement—Uses two's complement format, which is a common format for representing          2
            signed binary values. This format is similar to offset binary, but the MSB is inverted.

            •       digital data —

            digital data returns the data resulting from the conversion of analog waveform.

            •       resolution (out) —

           resolution (out) returns the number of bits represented in the digital waveform or digital data.

            •       full-scale range (out) —

            full-scale range (out) returns the total peak-to-peak range for the digital waveform or digital
           data.

            •       error out —


810   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:810 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:811 ordinal=811 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.


To create digital data from an analog waveform or to graph an analog signal in a digital
waveform graph, you must convert the raw analog data into digital data or the digital
waveform data type. Use the Analog to Digital VI to convert the data to digital
waveform. Use the Get Waveform Components function to extract the digital data from
the digital waveform.

The block diagram below simulates the acquisition of a sine wave with an amplitude of
5, which means the sine wave can contain values that range from –5 to 5. The Analog to
Digital VI in this block diagram represents each value with 8 bits. The 8 bits can
represent a peak-to-peak value of 10. The probe displays a portion of the resulting
values in binary format.


DigitalDigital toto AnalogAnalog

Converts a digital waveform or digital data to analog waveform. You must manually
select the polymorphic instance you want to use.


                                                    © National Instruments 811

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:811 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:812 ordinal=812 -->
## Functions

Functions


          • DWDT Digital to Analog VI
          • DTbl Digital to Analog VI

    DWDTDWDT DigitalDigital toto AnalogAnalog VIVI

     Converts a digital waveform or digital data to analog waveform. You must manually
      select the polymorphic instance you want to use.


     Inputs/Outputs

            •       digital waveform —

            digital waveform is the waveform you want to convert to analog waveform.

            •       full-scale range (pk-pk) —

            full-scale range (pk-pk) specifies the total peak-to-peak range, or the difference between the
        minimum and maximum, for the digital waveform or digital data. For example, if the maximum
          range of a waveform is 1 and the minimum is –1, the full-scale range for the waveform is 2. The
           default is 2.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. With the following
           exception, this input provides standard error in functionality.

                 If an error occurred before this node runs, this node outputs an empty waveform.

            •      data format (offset binary) —

          data format specifies which binary representation you want to use for the digital waveform or
             digital data.


812   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:812 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:813 ordinal=813 -->
## Functions

Functions


    0 unsigned binary—Converts the data to unsigned binary.
      offset binary (default)—The largest negative full-scale value is represented by all zeros, and the
    1 largest positive full-scale value is represented by all ones. Zero-scale is represented by a one
     (MSB) followed by all zeros, for example, binary 1000.
      2's complement—Uses two's complement format, which is a common format for representing    2
     signed binary values. This format is similar to offset binary, but the MSB is inverted.

   •      analog waveform —

    analog waveform returns the waveform resulting from the conversion of digital waveform or
     digital table.

   •       resolution (out) —

    resolution (out) returns the number of bits represented in the digital waveform or digital data.

   •       full-scale range (out) —

     full-scale range (out) returns the total peak-to-peak range for the digital waveform or digital
     data.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


DTblDTbl DigitalDigital toto AnalogAnalog VIVI

Converts a digital waveform or digital data to analog waveform. You must manually
select the polymorphic instance you want to use.


Inputs/Outputs

   •       digital table —

     digital table is the digital data you want to convert to analog waveform.


                                                    © National Instruments 813

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:813 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:814 ordinal=814 -->
## Functions

Functions

            •       full-scale range (pk-pk) —

            full-scale range (pk-pk) specifies the total peak-to-peak range, or the difference between the
        minimum and maximum, for the digital waveform or digital data. For example, if the maximum
          range of a waveform is 1 and the minimum is –1, the full-scale range for the waveform is 2. The
           default is 2.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. With the following
           exception, this input provides standard error in functionality.

                 If an error occurred before this node runs, this node outputs an empty waveform.

            •      data format (offset binary) —

          data format specifies which binary representation you want to use for the digital waveform or
             digital data.

          0 unsigned binary—Converts the data to unsigned binary.
             offset binary (default)—The largest negative full-scale value is represented by all zeros, and the
          1 largest positive full-scale value is represented by all ones. Zero-scale is represented by a one
           (MSB) followed by all zeros, for example, binary 1000.
             2's complement—Uses two's complement format, which is a common format for representing          2
            signed binary values. This format is similar to offset binary, but the MSB is inverted.

            •      analog waveform —

          analog waveform returns the waveform resulting from the conversion of digital waveform or
            digital table.

            •       resolution (out) —

           resolution (out) returns the number of bits represented in the digital waveform or digital data.

            •       full-scale range (out) —

            full-scale range (out) returns the total peak-to-peak range for the digital waveform or digital
           data.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


814   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:814 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:815 ordinal=815 -->
## Functions

Functions

IndexIndex WaveformWaveform ArrayArray

Selects one waveform out of an array of analog or digital waveforms by array index or
channel name. The data types you wire to the waveform array and index inputs and
the data type of the Y component of the analog waveform determine the polymorphic
instance to use.


  • WDT Index Channel DBL VI
  • WDT Index Channel I64 VI
  • WDT Index Channel I32 VI
  • WDT Index Channel I16 VI
  • WDT Index Channel CDB VI
  • WDT Index Channel by Name DBL VI
  • WDT Index Channel by Name I64 VI
  • WDT Index Channel by Name I32 VI
  • WDT Index Channel by Name I16 VI
  • WDT Index Channel by Name CDB VI
  • DWDT Index Channel VI
  • DWDT Index Channel by Name VI

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Index Array.vi

WDTWDT IndexIndex ChannelChannel DBLDBL VIVI

Selects one waveform out of an array of analog or digital waveforms by array index or
channel name. The data types you wire to the waveform array and index inputs and
the data type of the Y component of the analog waveform determine the polymorphic
instance to use.


                                                    © National Instruments 815

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:815 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:816 ordinal=816 -->
## Functions

Functions


     Inputs/Outputs

            •     waveform array —

         waveform array is an array of analog waveforms from which to extract a single waveform.

            •      index —

          index is the index of the waveform to extract from waveform array.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveform —

         waveform is the analog waveform selected from the array of waveforms.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - Index Array.vi

   WDTWDT IndexIndex ChannelChannel I64I64 VIVI

      Selects one waveform out of an array of analog or digital waveforms by array index or
     channel name. The data types you wire to the waveform array and index inputs and
     the data type of the Y component of the analog waveform determine the polymorphic
      instance to use.


816   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:816 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:817 ordinal=817 -->
## Functions

Functions


Inputs/Outputs

   •     waveform array —

    waveform array is an array of analog waveforms from which to extract a single waveform.

   •      index —

    index is the index of the waveform to extract from waveform array.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveform —

    waveform is the analog waveform selected from the array of waveforms.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Index Array.vi

WDTWDT IndexIndex ChannelChannel I32I32 VIVI

Selects one waveform out of an array of analog or digital waveforms by array index or
channel name. The data types you wire to the waveform array and index inputs and
the data type of the Y component of the analog waveform determine the polymorphic
instance to use.


                                                    © National Instruments 817

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:817 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:818 ordinal=818 -->
## Functions

Functions


     Inputs/Outputs

            •     waveform array —

         waveform array is an array of analog waveforms from which to extract a single waveform.

            •      index —

          index is the index of the waveform to extract from waveform array.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveform —

         waveform is the analog waveform selected from the array of waveforms.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - Index Array.vi

   WDTWDT IndexIndex ChannelChannel I16I16 VIVI

      Selects one waveform out of an array of analog or digital waveforms by array index or
     channel name. The data types you wire to the waveform array and index inputs and
     the data type of the Y component of the analog waveform determine the polymorphic
      instance to use.


818   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:818 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:819 ordinal=819 -->
## Functions

Functions


Inputs/Outputs

   •     waveform array —

    waveform array is an array of analog waveforms from which to extract a single waveform.

   •      index —

    index is the index of the waveform to extract from waveform array.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveform —

    waveform is the analog waveform selected from the array of waveforms.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Index Array.vi

WDTWDT IndexIndex ChannelChannel CDBCDB VIVI

Selects one waveform out of an array of analog or digital waveforms by array index or
channel name. The data types you wire to the waveform array and index inputs and
the data type of the Y component of the analog waveform determine the polymorphic
instance to use.


                                                    © National Instruments 819

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:819 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:820 ordinal=820 -->
## Functions

Functions


     Inputs/Outputs

            •     waveform array —

         waveform array is an array of analog waveforms from which to extract a single waveform.

            •      index —

          index is the index of the waveform to extract from waveform array.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveform —

         waveform is the analog waveform selected from the array of waveforms.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - Index Array.vi

   WDTWDT IndexIndex ChannelChannel byby NameName DBLDBL VIVI

      Selects one waveform out of an array of analog or digital waveforms by array index or
     channel name. The data types you wire to the waveform array and index inputs and
     the data type of the Y component of the analog waveform determine the polymorphic
      instance to use.


820   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:820 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:821 ordinal=821 -->
## Functions

Functions


Inputs/Outputs

   •     waveform array —

    waveform array is an array of analog waveforms from which to extract a single waveform.

   •      channel name —

    channel name is the channel name of the waveform to extract from waveform array.

    To use this input, the waveform must have a channel name attribute. If you are using a virtual
    channel, you do not have to set the channel name attribute manually.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveform —

    waveform is the analog waveform selected from the array of waveforms.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Index Array.vi

WDTWDT IndexIndex ChannelChannel byby NameName I64I64 VIVI

Selects one waveform out of an array of analog or digital waveforms by array index or
channel name. The data types you wire to the waveform array and index inputs and
the data type of the Y component of the analog waveform determine the polymorphic
instance to use.

                                                    © National Instruments 821

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:821 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:822 ordinal=822 -->
## Functions

Functions


     Inputs/Outputs

            •     waveform array —

         waveform array is an array of analog waveforms from which to extract a single waveform.

            •      channel name —

          channel name is the channel name of the waveform to extract from waveform array.

         To use this input, the waveform must have a channel name attribute. If you are using a virtual
           channel, you do not have to set the channel name attribute manually.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveform —

         waveform is the analog waveform selected from the array of waveforms.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - Index Array.vi

   WDTWDT IndexIndex ChannelChannel byby NameName I32I32 VIVI

      Selects one waveform out of an array of analog or digital waveforms by array index or
     channel name. The data types you wire to the waveform array and index inputs and
     the data type of the Y component of the analog waveform determine the polymorphic

822   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:822 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:823 ordinal=823 -->
## Functions

Functions

instance to use.


Inputs/Outputs

   •     waveform array —

    waveform array is an array of analog waveforms from which to extract a single waveform.

   •      channel name —

    channel name is the channel name of the waveform to extract from waveform array.

    To use this input, the waveform must have a channel name attribute. If you are using a virtual
    channel, you do not have to set the channel name attribute manually.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveform —

    waveform is the analog waveform selected from the array of waveforms.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Index Array.vi

WDTWDT IndexIndex ChannelChannel byby NameName I16I16 VIVI

Selects one waveform out of an array of analog or digital waveforms by array index or

                                                    © National Instruments 823

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:823 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:824 ordinal=824 -->
## Functions

Functions

     channel name. The data types you wire to the waveform array and index inputs and
     the data type of the Y component of the analog waveform determine the polymorphic
      instance to use.


     Inputs/Outputs

            •     waveform array —

         waveform array is an array of analog waveforms from which to extract a single waveform.

            •      channel name —

          channel name is the channel name of the waveform to extract from waveform array.

         To use this input, the waveform must have a channel name attribute. If you are using a virtual
           channel, you do not have to set the channel name attribute manually.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveform —

         waveform is the analog waveform selected from the array of waveforms.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - Index Array.vi


824   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:824 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:825 ordinal=825 -->
## Functions

Functions

WDTWDT IndexIndex ChannelChannel byby NameName CDBCDB VIVI

Selects one waveform out of an array of analog or digital waveforms by array index or
channel name. The data types you wire to the waveform array and index inputs and
the data type of the Y component of the analog waveform determine the polymorphic
instance to use.


Inputs/Outputs

   •     waveform array —

    waveform array is an array of analog waveforms from which to extract a single waveform.

   •      channel name —

    channel name is the channel name of the waveform to extract from waveform array.

    To use this input, the waveform must have a channel name attribute. If you are using a virtual
    channel, you do not have to set the channel name attribute manually.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveform —

    waveform is the analog waveform selected from the array of waveforms.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.


                                                    © National Instruments 825

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:825 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:826 ordinal=826 -->
## Functions

Functions

          • labview\examples\Waveform\Waveform - Index Array.vi

    DWDTDWDT IndexIndex ChannelChannel VIVI

      Selects one waveform out of an array of analog or digital waveforms by array index or
     channel name. The data types you wire to the waveform array and index inputs and
     the data type of the Y component of the analog waveform determine the polymorphic
      instance to use.


     Inputs/Outputs

            •     waveform array —

         waveform array is an array of digital waveforms from which to extract a single digital waveform.

            •      index —

          index is the index of the waveform to extract from waveform array.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveform —

         waveform is the digital waveform selected from the array of digital waveforms.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - Index Array.vi

826   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:826 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:827 ordinal=827 -->
## Functions

Functions

DWDTDWDT IndexIndex ChannelChannel byby NameName VIVI

Selects one waveform out of an array of analog or digital waveforms by array index or
channel name. The data types you wire to the waveform array and index inputs and
the data type of the Y component of the analog waveform determine the polymorphic
instance to use.


Inputs/Outputs

   •     waveform array —

    waveform array is an array of digital waveforms from which to extract a single digital waveform.

   •      channel name —

    channel name is the channel name of the waveform to extract from waveform array.

    To use this input, the waveform must have a channel name attribute. If you are using a virtual
    channel, you do not have to set the channel name attribute manually.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveform —

    waveform is the digital waveform selected from the array of digital waveforms.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.


                                                    © National Instruments 827

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:827 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:828 ordinal=828 -->
## Functions

Functions

          • labview\examples\Waveform\Waveform - Index Array.vi

    CopyCopy WaveformWaveform dtdt

     Replaces all dt values with the dt value of the waveform at index position in
     waveforms in. The data type you wire to the waveforms in input and the data type of
     the Y component of the analog waveform determine the polymorphic instance to use.


          • WDT Copy Waveform dt DBL VI
          • WDT Copy Waveform dt I64 VI
          • WDT Copy Waveform dt I32 VI
          • WDT Copy Waveform dt I16 VI
          • WDT Copy Waveform dt CDB VI
          • WDT Copy Waveform dt EXT VI
          • WDT Copy Waveform dt CXT VI
          • DWDT Copy Waveform dt VI

   WDTWDT CopyCopy WaveformWaveform dtdt DBLDBL VIVI

     Replaces all dt values with the dt value of the waveform at index position in
     waveforms in. The data type you wire to the waveforms in input and the data type of
     the Y component of the analog waveform determine the polymorphic instance to use.


     Inputs/Outputs

            •     waveforms in —

         waveforms in contains the analog waveforms for which the time increment values are replaced
         by the time increment of the analog waveform indicated by index. The default is empty.

            •      index —


828   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:828 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:829 ordinal=829 -->
## Functions

Functions


    index is the specifier that the waveform in the waveforms in array uses for the dt value. The
     default is 0.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveforms out —

    waveforms out contains analog waveforms for which the dt values are all identical.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


WDTWDT CopyCopy WaveformWaveform dtdt I64I64 VIVI

Replaces all dt values with the dt value of the waveform at index position in
waveforms in. The data type you wire to the waveforms in input and the data type of
the Y component of the analog waveform determine the polymorphic instance to use.


Inputs/Outputs

   •     waveforms in —

    waveforms in contains the analog waveforms for which the time increment values are replaced
    by the time increment of the analog waveform indicated by index. The default is empty.

   •      index —

    index is the specifier that the waveform in the waveforms in array uses for the dt value. The
     default is 0.

   •       error in (no error) —


                                                    © National Instruments 829

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:829 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:830 ordinal=830 -->
## Functions

Functions


           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveforms out —

         waveforms out contains analog waveforms for which the dt values are all identical.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


   WDTWDT CopyCopy WaveformWaveform dtdt I32I32 VIVI

     Replaces all dt values with the dt value of the waveform at index position in
     waveforms in. The data type you wire to the waveforms in input and the data type of
     the Y component of the analog waveform determine the polymorphic instance to use.


     Inputs/Outputs

            •     waveforms in —

         waveforms in contains the analog waveforms for which the time increment values are replaced
         by the time increment of the analog waveform indicated by index. The default is empty.

            •      index —

          index is the specifier that the waveform in the waveforms in array uses for the dt value. The
           default is 0.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveforms out —


830   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:830 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:831 ordinal=831 -->
## Functions

Functions


    waveforms out contains analog waveforms for which the dt values are all identical.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


WDTWDT CopyCopy WaveformWaveform dtdt I16I16 VIVI

Replaces all dt values with the dt value of the waveform at index position in
waveforms in. The data type you wire to the waveforms in input and the data type of
the Y component of the analog waveform determine the polymorphic instance to use.


Inputs/Outputs

   •     waveforms in —

    waveforms in contains the analog waveforms for which the time increment values are replaced
    by the time increment of the analog waveform indicated by index. The default is empty.

   •      index —

    index is the specifier that the waveform in the waveforms in array uses for the dt value. The
     default is 0.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveforms out —

    waveforms out contains analog waveforms for which the dt values are all identical.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 831

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:831 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:832 ordinal=832 -->
## Functions

Functions

   WDTWDT CopyCopy WaveformWaveform dtdt CDBCDB VIVI

     Replaces all dt values with the dt value of the waveform at index position in
     waveforms in. The data type you wire to the waveforms in input and the data type of
     the Y component of the analog waveform determine the polymorphic instance to use.


     Inputs/Outputs

            •     waveforms in —

         waveforms in contains the analog waveforms for which the time increment values are replaced
         by the time increment of the analog waveform indicated by index. The default is empty.

            •      index —

          index is the specifier that the waveform in the waveforms in array uses for the dt value. The
           default is 0.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveforms out —

         waveforms out contains analog waveforms for which the dt values are all identical.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


   WDTWDT CopyCopy WaveformWaveform dtdt EXTEXT VIVI

     Replaces all dt values with the dt value of the waveform at index position in
     waveforms in. The data type you wire to the waveforms in input and the data type of
     the Y component of the analog waveform determine the polymorphic instance to use.


832   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:832 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:833 ordinal=833 -->
## Functions

Functions


Inputs/Outputs

   •     waveforms in —

    waveforms in contains the analog waveforms for which the time increment values are replaced
    by the time increment of the analog waveform indicated by index. The default is empty.

   •      index —

    index is the specifier that the waveform in the waveforms in array uses for the dt value. The
     default is 0.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveforms out —

    waveforms out contains analog waveforms for which the dt values are all identical.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


WDTWDT CopyCopy WaveformWaveform dtdt CXTCXT VIVI

Replaces all dt values with the dt value of the waveform at index position in
waveforms in. The data type you wire to the waveforms in input and the data type of
the Y component of the analog waveform determine the polymorphic instance to use.


                                                    © National Instruments 833

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:833 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:834 ordinal=834 -->
## Functions

Functions

     Inputs/Outputs

            •     waveforms in —

         waveforms in contains the analog waveforms for which the time increment values are replaced
         by the time increment of the analog waveform indicated by index. The default is empty.

            •      index —

          index is the specifier that the waveform in the waveforms in array uses for the dt value. The
           default is 0.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveforms out —

         waveforms out contains analog waveforms for which the dt values are all identical.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


    DWDTDWDT CopyCopy WaveformWaveform dtdt VIVI

     Replaces all dt values with the dt value of the waveform at index position in
     waveforms in. The data type you wire to the waveforms in input and the data type of
     the Y component of the analog waveform determine the polymorphic instance to use.


     Inputs/Outputs

            •     waveforms in —

         waveforms in contains the digital waveforms for which the time increment values are replaced
         by the time increment of the digital waveform indicated by index. The default is empty.


834   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:834 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:835 ordinal=835 -->
## Functions

Functions

   •      index —

    index is the specifier that the waveform in the waveforms in array uses for the dt value. The
     default is 0.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveforms out —

    waveforms out contains digital waveforms for which the dt values are all identical.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

AlignAlign WaveformWaveform TimestampsTimestamps

Replaces all the time stamp values (t0) in waveforms in with the value of the index
element in the array. The data type you wire to the waveforms in input and the data
type of the Y component of the analog waveform determine the polymorphic instance
to use.


  • WDT Align Waveform Timestamps DBL VI
  • WDT Align Waveform Timestamps I64 VI
  • WDT Align Waveform Timestamps I32 VI
  • WDT Align Waveform Timestamps I16 VI
  • WDT Align Waveform Timestamps CDB VI
  • WDT Align Waveform Timestamps EXT VI
  • WDT Align Waveform Timestamps CXT VI
  • DWDT Align Waveform Timestamps VI


                                                    © National Instruments 835

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:835 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:836 ordinal=836 -->
## Functions

Functions

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - Align Timestamps.vi

   WDTWDT AlignAlign WaveformWaveform TimestampsTimestamps DBLDBL VIVI

     Replaces all the time stamp values (t0) in waveforms in with the value of the index
     element in the array. The data type you wire to the waveforms in input and the data
     type of the Y component of the analog waveform determine the polymorphic instance
      to use.


     Inputs/Outputs

            •     waveforms in —

         waveforms in contains all the analog waveforms for which time stamps (t0) are to be changed.

            •      index —

          index selects which waveform to extract the time stamp from. The time stamps of all elements of
         waveforms in are changed to this time stamp.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveforms out —

         waveforms out contains the waveforms in array with all time stamps on the elements changed
           to the time stamp of the element indicated by index.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


836   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:836 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:837 ordinal=837 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Align Timestamps.vi

WDTWDT AlignAlign WaveformWaveform TimestampsTimestamps I64I64 VIVI

Replaces all the time stamp values (t0) in waveforms in with the value of the index
element in the array. The data type you wire to the waveforms in input and the data
type of the Y component of the analog waveform determine the polymorphic instance
to use.


Inputs/Outputs

   •     waveforms in —

    waveforms in contains all the analog waveforms for which time stamps (t0) are to be changed.

   •      index —

    index selects which waveform to extract the time stamp from. The time stamps of all elements of
    waveforms in are changed to this time stamp.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveforms out —

    waveforms out contains the waveforms in array with all time stamps on the elements changed
    to the time stamp of the element indicated by index.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 837

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:837 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:838 ordinal=838 -->
## Functions

Functions

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - Align Timestamps.vi

   WDTWDT AlignAlign WaveformWaveform TimestampsTimestamps I32I32 VIVI

     Replaces all the time stamp values (t0) in waveforms in with the value of the index
     element in the array. The data type you wire to the waveforms in input and the data
     type of the Y component of the analog waveform determine the polymorphic instance
      to use.


     Inputs/Outputs

            •     waveforms in —

         waveforms in contains all the analog waveforms for which time stamps (t0) are to be changed.

            •      index —

          index selects which waveform to extract the time stamp from. The time stamps of all elements of
         waveforms in are changed to this time stamp.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveforms out —

         waveforms out contains the waveforms in array with all time stamps on the elements changed
           to the time stamp of the element indicated by index.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


838   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:838 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:839 ordinal=839 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Align Timestamps.vi

WDTWDT AlignAlign WaveformWaveform TimestampsTimestamps I16I16 VIVI

Replaces all the time stamp values (t0) in waveforms in with the value of the index
element in the array. The data type you wire to the waveforms in input and the data
type of the Y component of the analog waveform determine the polymorphic instance
to use.


Inputs/Outputs

   •     waveforms in —

    waveforms in contains all the analog waveforms for which time stamps (t0) are to be changed.

   •      index —

    index selects which waveform to extract the time stamp from. The time stamps of all elements of
    waveforms in are changed to this time stamp.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveforms out —

    waveforms out contains the waveforms in array with all time stamps on the elements changed
    to the time stamp of the element indicated by index.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 839

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:839 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:840 ordinal=840 -->
## Functions

Functions

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - Align Timestamps.vi

   WDTWDT AlignAlign WaveformWaveform TimestampsTimestamps CDBCDB VIVI

     Replaces all the time stamp values (t0) in waveforms in with the value of the index
     element in the array. The data type you wire to the waveforms in input and the data
     type of the Y component of the analog waveform determine the polymorphic instance
      to use.


     Inputs/Outputs

            •     waveforms in —

         waveforms in contains all the analog waveforms for which time stamps (t0) are to be changed.

            •      index —

          index selects which waveform to extract the time stamp from. The time stamps of all elements of
         waveforms in are changed to this time stamp.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveforms out —

         waveforms out contains the waveforms in array with all time stamps on the elements changed
           to the time stamp of the element indicated by index.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


840   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:840 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:841 ordinal=841 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Align Timestamps.vi

WDTWDT AlignAlign WaveformWaveform TimestampsTimestamps EXTEXT VIVI

Replaces all the time stamp values (t0) in waveforms in with the value of the index
element in the array. The data type you wire to the waveforms in input and the data
type of the Y component of the analog waveform determine the polymorphic instance
to use.


Inputs/Outputs

   •     waveforms in —

    waveforms in contains all the analog waveforms for which time stamps (t0) are to be changed.

   •      index —

    index selects which waveform to extract the time stamp from. The time stamps of all elements of
    waveforms in are changed to this time stamp.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveforms out —

    waveforms out contains the waveforms in array with all time stamps on the elements changed
    to the time stamp of the element indicated by index.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 841

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:841 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:842 ordinal=842 -->
## Functions

Functions

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - Align Timestamps.vi

   WDTWDT AlignAlign WaveformWaveform TimestampsTimestamps CXTCXT VIVI

     Replaces all the time stamp values (t0) in waveforms in with the value of the index
     element in the array. The data type you wire to the waveforms in input and the data
     type of the Y component of the analog waveform determine the polymorphic instance
      to use.


     Inputs/Outputs

            •     waveforms in —

         waveforms in contains all the analog waveforms for which time stamps (t0) are to be changed.

            •      index —

          index selects which waveform to extract the time stamp from. The time stamps of all elements of
         waveforms in are changed to this time stamp.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveforms out —

         waveforms out contains the waveforms in array with all time stamps on the elements changed
           to the time stamp of the element indicated by index.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


842   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:842 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:843 ordinal=843 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Align Timestamps.vi

DWDTDWDT AlignAlign WaveformWaveform TimestampsTimestamps VIVI

Replaces all the time stamp values (t0) in waveforms in with the value of the index
element in the array. The data type you wire to the waveforms in input and the data
type of the Y component of the analog waveform determine the polymorphic instance
to use.


Inputs/Outputs

   •     waveforms in —

    waveforms in contains all the digital waveforms for which time stamps (t0) are to be changed.

   •      index —

    index selects which waveform to extract the time stamp from. The time stamps of all elements of
    waveforms in are changed to this time stamp.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveforms out —

    waveforms out contains the waveforms in array with all time stamps on the elements changed
    to the time stamp of the element indicated by index.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 843

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:843 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:844 ordinal=844 -->
## Functions

Functions

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - Align Timestamps.vi

    GetGet WaveformWaveform SubsetSubset

      Retrieves a subset of a waveform at a specified time or index. You must manually
      select the polymorphic instance you want to use.


          • WDT Get Waveform Subset DBL VI
          • WDT Get Waveform Subset CDB VI
          • WDT Get Waveform Subset EXT VI
          • WDT Get Waveform Subset I16 VI
          • WDT Get Waveform Subset I32 VI
          • WDT Get Waveform Subset I8 VI
          • WDT Get Waveform Subset SGL VI
          • DWDT Get Waveform Subset VI
          • DTbl Digital Subset VI

     For example, consider a waveform of 128 scans with a dt of 1.00. If you wire 40.00 to
     duration and 25.00 to start samples/time, the actual duration and actual start
     samples/time are the same, 40.00 and 25.00, respectively. However, if the waveform
     has a dt of 2.00, the actual duration and the actual start samples/time are 40.00 and
      24.00, respectively.

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - Get Subset.vi


844   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:844 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:845 ordinal=845 -->
## Functions

Functions

WDTWDT GetGet WaveformWaveform SubsetSubset DBLDBL VIVI

Retrieves a subset of a waveform at a specified time or index. You must manually
select the polymorphic instance you want to use.


Inputs/Outputs

   •     open interval? (T) —

   open interval? defines whether the waveform subset extracted is an open or closed interval. The
     default is TRUE, which selects an open interval.

    For example, if t0 = 0, dt = 1, Y = {0, 1, 2}, start/duration format is Relative Time, start samples/
    time is 0, and duration is 2, an open interval returns {0, 1}. A closed interval returns {0, 1, 2}.

   •       start/duration format —

    start/duration format specifies if you want to retrieve the data value of the specified element or
     at a specified time.

    0 Samples (default)—Returns the data value of the specified element in the waveform data.
      Relative Time—Returns the data value at a specified time relative to the first point in the
    1 waveform. In this mode, the dt of the waveform affects actual start samples/time and actual
      duration.

   •     waveform in —

    waveform in is the waveform for which you want to retrieve a subset.

   •       start samples/time —

     start samples/time is the data element or time value where you want to start acquiring a
    waveform subset.

   •      duration —


                                                    © National Instruments 845

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:845 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:846 ordinal=846 -->
## Functions

Functions


          duration is the amount of time to retrieve data or the number of elements of data you want to
            retrieve, depending on the start/duration format you select.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveform out —

         waveform out is the waveform subset.

            •      actual start samples/time —

           actual start samples/time is the actual data element when the subset was acquired.

            •      actual duration —

           actual duration is the actual number of elements retrieved or the actual amount of time the
          data values were acquired.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


     For example, consider a waveform of 128 scans with a dt of 1.00. If you wire 40.00 to
     duration and 25.00 to start samples/time, the actual duration and actual start
     samples/time are the same, 40.00 and 25.00, respectively. However, if the waveform
     has a dt of 2.00, the actual duration and the actual start samples/time are 40.00 and
      24.00, respectively.

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - Get Subset.vi

   WDTWDT GetGet WaveformWaveform SubsetSubset CDBCDB VIVI

      Retrieves a subset of a waveform at a specified time or index. You must manually


846   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:846 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:847 ordinal=847 -->
## Functions

Functions

select the polymorphic instance you want to use.


Inputs/Outputs

   •     open interval? (T) —

   open interval? defines whether the waveform subset extracted is an open or closed interval. The
     default is TRUE, which selects an open interval.

    For example, if t0 = 0, dt = 1, Y = {0, 1, 2}, start/duration format is Relative Time, start samples/
    time is 0, and duration is 2, an open interval returns {0, 1}. A closed interval returns {0, 1, 2}.

   •       start/duration format —

    start/duration format specifies if you want to retrieve the data value of the specified element or
     at a specified time.

    0 Samples (default)—Returns the data value of the specified element in the waveform data.
      Relative Time—Returns the data value at a specified time relative to the first point in the
    1 waveform. In this mode, the dt of the waveform affects actual start samples/time and actual
      duration.

   •     waveform in —

    waveform in is the waveform for which you want to retrieve a subset.

   •       start samples/time —

     start samples/time is the data element or time value where you want to start acquiring a
    waveform subset.

   •      duration —

    duration is the amount of time to retrieve data or the number of elements of data you want to
     retrieve, depending on the start/duration format you select.

   •       error in (no error) —

                                                    © National Instruments 847

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:847 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:848 ordinal=848 -->
## Functions

Functions


           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveform out —

         waveform out is the waveform subset.

            •      actual start samples/time —

           actual start samples/time is the actual data element when the subset was acquired.

            •      actual duration —

           actual duration is the actual number of elements retrieved or the actual amount of time the
          data values were acquired.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


     For example, consider a waveform of 128 scans with a dt of 1.00. If you wire 40.00 to
     duration and 25.00 to start samples/time, the actual duration and actual start
     samples/time are the same, 40.00 and 25.00, respectively. However, if the waveform
     has a dt of 2.00, the actual duration and the actual start samples/time are 40.00 and
      24.00, respectively.

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - Get Subset.vi

   WDTWDT GetGet WaveformWaveform SubsetSubset EXTEXT VIVI

      Retrieves a subset of a waveform at a specified time or index. You must manually
      select the polymorphic instance you want to use.


848   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:848 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:849 ordinal=849 -->
## Functions

Functions


Inputs/Outputs

   •     open interval? (T) —

   open interval? defines whether the waveform subset extracted is an open or closed interval. The
     default is TRUE, which selects an open interval.

    For example, if t0 = 0, dt = 1, Y = {0, 1, 2}, start/duration format is Relative Time, start samples/
    time is 0, and duration is 2, an open interval returns {0, 1}. A closed interval returns {0, 1, 2}.

   •       start/duration format —

    start/duration format specifies if you want to retrieve the data value of the specified element or
     at a specified time.

    0 Samples (default)—Returns the data value of the specified element in the waveform data.
      Relative Time—Returns the data value at a specified time relative to the first point in the
    1 waveform. In this mode, the dt of the waveform affects actual start samples/time and actual
      duration.

   •     waveform in —

    waveform in is the waveform for which you want to retrieve a subset.

   •       start samples/time —

     start samples/time is the data element or time value where you want to start acquiring a
    waveform subset.

   •      duration —

    duration is the amount of time to retrieve data or the number of elements of data you want to
     retrieve, depending on the start/duration format you select.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides


                                                    © National Instruments 849

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:849 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:850 ordinal=850 -->
## Functions

Functions


          standard error in functionality.

            •     waveform out —

         waveform out is the waveform subset.

            •      actual start samples/time —

           actual start samples/time is the actual data element when the subset was acquired.

            •      actual duration —

           actual duration is the actual number of elements retrieved or the actual amount of time the
          data values were acquired.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


     For example, consider a waveform of 128 scans with a dt of 1.00. If you wire 40.00 to
     duration and 25.00 to start samples/time, the actual duration and actual start
     samples/time are the same, 40.00 and 25.00, respectively. However, if the waveform
     has a dt of 2.00, the actual duration and the actual start samples/time are 40.00 and
      24.00, respectively.

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - Get Subset.vi

   WDTWDT GetGet WaveformWaveform SubsetSubset I16I16 VIVI

      Retrieves a subset of a waveform at a specified time or index. You must manually
      select the polymorphic instance you want to use.


850   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:850 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:851 ordinal=851 -->
## Functions

Functions


Inputs/Outputs

   •     open interval? (T) —

   open interval? defines whether the waveform subset extracted is an open or closed interval. The
     default is TRUE, which selects an open interval.

    For example, if t0 = 0, dt = 1, Y = {0, 1, 2}, start/duration format is Relative Time, start samples/
    time is 0, and duration is 2, an open interval returns {0, 1}. A closed interval returns {0, 1, 2}.

   •       start/duration format —

    start/duration format specifies if you want to retrieve the data value of the specified element or
     at a specified time.

    0 Samples (default)—Returns the data value of the specified element in the waveform data.
      Relative Time—Returns the data value at a specified time relative to the first point in the
    1 waveform. In this mode, the dt of the waveform affects actual start samples/time and actual
      duration.

   •     waveform in —

    waveform in is the waveform for which you want to retrieve a subset.

   •       start samples/time —

     start samples/time is the data element or time value where you want to start acquiring a
    waveform subset.

   •      duration —

    duration is the amount of time to retrieve data or the number of elements of data you want to
     retrieve, depending on the start/duration format you select.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides


                                                    © National Instruments 851

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:851 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:852 ordinal=852 -->
## Functions

Functions


          standard error in functionality.

            •     waveform out —

         waveform out is the waveform subset.

            •      actual start samples/time —

           actual start samples/time is the actual data element when the subset was acquired.

            •      actual duration —

           actual duration is the actual number of elements retrieved or the actual amount of time the
          data values were acquired.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


     For example, consider a waveform of 128 scans with a dt of 1.00. If you wire 40.00 to
     duration and 25.00 to start samples/time, the actual duration and actual start
     samples/time are the same, 40.00 and 25.00, respectively. However, if the waveform
     has a dt of 2.00, the actual duration and the actual start samples/time are 40.00 and
      24.00, respectively.

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - Get Subset.vi

   WDTWDT GetGet WaveformWaveform SubsetSubset I32I32 VIVI

      Retrieves a subset of a waveform at a specified time or index. You must manually
      select the polymorphic instance you want to use.


852   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:852 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:853 ordinal=853 -->
## Functions

Functions


Inputs/Outputs

   •     open interval? (T) —

   open interval? defines whether the waveform subset extracted is an open or closed interval. The
     default is TRUE, which selects an open interval.

    For example, if t0 = 0, dt = 1, Y = {0, 1, 2}, start/duration format is Relative Time, start samples/
    time is 0, and duration is 2, an open interval returns {0, 1}. A closed interval returns {0, 1, 2}.

   •       start/duration format —

    start/duration format specifies if you want to retrieve the data value of the specified element or
     at a specified time.

    0 Samples (default)—Returns the data value of the specified element in the waveform data.
      Relative Time—Returns the data value at a specified time relative to the first point in the
    1 waveform. In this mode, the dt of the waveform affects actual start samples/time and actual
      duration.

   •     waveform in —

    waveform in is the waveform for which you want to retrieve a subset.

   •       start samples/time —

     start samples/time is the data element or time value where you want to start acquiring a
    waveform subset.

   •      duration —

    duration is the amount of time to retrieve data or the number of elements of data you want to
     retrieve, depending on the start/duration format you select.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides


                                                    © National Instruments 853

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:853 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:854 ordinal=854 -->
## Functions

Functions


          standard error in functionality.

            •     waveform out —

         waveform out is the waveform subset.

            •      actual start samples/time —

           actual start samples/time is the actual data element when the subset was acquired.

            •      actual duration —

           actual duration is the actual number of elements retrieved or the actual amount of time the
          data values were acquired.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


     For example, consider a waveform of 128 scans with a dt of 1.00. If you wire 40.00 to
     duration and 25.00 to start samples/time, the actual duration and actual start
     samples/time are the same, 40.00 and 25.00, respectively. However, if the waveform
     has a dt of 2.00, the actual duration and the actual start samples/time are 40.00 and
      24.00, respectively.

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - Get Subset.vi

   WDTWDT GetGet WaveformWaveform SubsetSubset I8I8 VIVI

      Retrieves a subset of a waveform at a specified time or index. You must manually
      select the polymorphic instance you want to use.


854   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:854 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:855 ordinal=855 -->
## Functions

Functions


Inputs/Outputs

   •     open interval? (T) —

   open interval? defines whether the waveform subset extracted is an open or closed interval. The
     default is TRUE, which selects an open interval.

    For example, if t0 = 0, dt = 1, Y = {0, 1, 2}, start/duration format is Relative Time, start samples/
    time is 0, and duration is 2, an open interval returns {0, 1}. A closed interval returns {0, 1, 2}.

   •       start/duration format —

    start/duration format specifies if you want to retrieve the data value of the specified element or
     at a specified time.

    0 Samples (default)—Returns the data value of the specified element in the waveform data.
      Relative Time—Returns the data value at a specified time relative to the first point in the
    1 waveform. In this mode, the dt of the waveform affects actual start samples/time and actual
      duration.

   •     waveform in —

    waveform in is the waveform for which you want to retrieve a subset.

   •       start samples/time —

     start samples/time is the data element or time value where you want to start acquiring a
    waveform subset.

   •      duration —

    duration is the amount of time to retrieve data or the number of elements of data you want to
     retrieve, depending on the start/duration format you select.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides


                                                    © National Instruments 855

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:855 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:856 ordinal=856 -->
## Functions

Functions


          standard error in functionality.

            •     waveform out —

         waveform out is the waveform subset.

            •      actual start samples/time —

           actual start samples/time is the actual data element when the subset was acquired.

            •      actual duration —

           actual duration is the actual number of elements retrieved or the actual amount of time the
          data values were acquired.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


     For example, consider a waveform of 128 scans with a dt of 1.00. If you wire 40.00 to
     duration and 25.00 to start samples/time, the actual duration and actual start
     samples/time are the same, 40.00 and 25.00, respectively. However, if the waveform
     has a dt of 2.00, the actual duration and the actual start samples/time are 40.00 and
      24.00, respectively.

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - Get Subset.vi

   WDTWDT GetGet WaveformWaveform SubsetSubset SGLSGL VIVI

      Retrieves a subset of a waveform at a specified time or index. You must manually
      select the polymorphic instance you want to use.


856   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:856 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:857 ordinal=857 -->
## Functions

Functions


Inputs/Outputs

   •     open interval? (T) —

   open interval? defines whether the waveform subset extracted is an open or closed interval. The
     default is TRUE, which selects an open interval.

    For example, if t0 = 0, dt = 1, Y = {0, 1, 2}, start/duration format is Relative Time, start samples/
    time is 0, and duration is 2, an open interval returns {0, 1}. A closed interval returns {0, 1, 2}.

   •       start/duration format —

    start/duration format specifies if you want to retrieve the data value of the specified element or
     at a specified time.

    0 Samples (default)—Returns the data value of the specified element in the waveform data.
      Relative Time—Returns the data value at a specified time relative to the first point in the
    1 waveform. In this mode, the dt of the waveform affects actual start samples/time and actual
      duration.

   •     waveform in —

    waveform in is the waveform for which you want to retrieve a subset.

   •       start samples/time —

     start samples/time is the data element or time value where you want to start acquiring a
    waveform subset.

   •      duration —

    duration is the amount of time to retrieve data or the number of elements of data you want to
     retrieve, depending on the start/duration format you select.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides


                                                    © National Instruments 857

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:857 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:858 ordinal=858 -->
## Functions

Functions


          standard error in functionality.

            •     waveform out —

         waveform out is the waveform subset.

            •      actual start samples/time —

           actual start samples/time is the actual data element when the subset was acquired.

            •      actual duration —

           actual duration is the actual number of elements retrieved or the actual amount of time the
          data values were acquired.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


     For example, consider a waveform of 128 scans with a dt of 1.00. If you wire 40.00 to
     duration and 25.00 to start samples/time, the actual duration and actual start
     samples/time are the same, 40.00 and 25.00, respectively. However, if the waveform
     has a dt of 2.00, the actual duration and the actual start samples/time are 40.00 and
      24.00, respectively.

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - Get Subset.vi

    DWDTDWDT GetGet WaveformWaveform SubsetSubset VIVI

      Retrieves a subset of a waveform at a specified time or index. You must manually
      select the polymorphic instance you want to use.


858   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:858 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:859 ordinal=859 -->
## Functions

Functions


Inputs/Outputs

   •     open interval? (T) —

   open interval? defines whether the waveform subset extracted is an open or closed interval. The
     default is TRUE, which selects an open interval.

    For example, if t0 = 0, dt = 1, Y = {0, 1, 2}, start/duration format is Relative Time, start samples/
    time is 0, and duration is 2, an open interval returns {0, 1}. A closed interval returns {0, 1, 2}.

   •       start/duration format —

    start/duration format specifies if you want to retrieve the data value of the specified element or
     at a specified time.

    0 Samples (default)—Returns the data value of the specified element in the waveform data.
      Relative Time—Returns the data value at a specified time relative to the first point in the
    1 waveform. In this mode, the dt of the waveform affects actual start samples/time and actual
      duration.

   •     waveform in —

    waveform in is the digital waveform for which you want to retrieve a subset.

   •       start samples/time —

     start samples/time is the data element or time value where you want to start acquiring a
    waveform subset.

   •      duration —

    duration is the amount of time to retrieve data or the number of elements of data you want to
     retrieve, depending on the start/duration format you select.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides


                                                    © National Instruments 859

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:859 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:860 ordinal=860 -->
## Functions

Functions


          standard error in functionality.

            •     waveform out —

         waveform out is the waveform subset.

            •      actual start samples/time —

           actual start samples/time is the actual data element when the subset was acquired.

            •      actual duration —

           actual duration is the actual number of elements retrieved or the actual amount of time the
          data values were acquired.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


     For example, consider a waveform of 128 scans with a dt of 1.00. If you wire 40.00 to
     duration and 25.00 to start samples/time, the actual duration and actual start
     samples/time are the same, 40.00 and 25.00, respectively. However, if the waveform
     has a dt of 2.00, the actual duration and the actual start samples/time are 40.00 and
      24.00, respectively.

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - Get Subset.vi

     DTblDTbl DigitalDigital SubsetSubset VIVI

      Retrieves a subset of a waveform at a specified time or index. You must manually
      select the polymorphic instance you want to use.


860   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:860 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:861 ordinal=861 -->
## Functions

Functions


Inputs/Outputs

   •       digital data —

     digital data is the set of digital data for which you want to retrieve a subset.

   •       start —

     start is the data element or time value where you want to start acquiring a data subset.

   •     number of samples —

   number of samples specifies the number of samples to include in digital data subset.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       digital data subset —

     digital data subset is the digital data subset.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


For example, consider a waveform of 128 scans with a dt of 1.00. If you wire 40.00 to
duration and 25.00 to start samples/time, the actual duration and actual start
samples/time are the same, 40.00 and 25.00, respectively. However, if the waveform
has a dt of 2.00, the actual duration and the actual start samples/time are 40.00 and
24.00, respectively.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Get Subset.vi

                                                    © National Instruments 861

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:861 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:862 ordinal=862 -->
## Functions

Functions

    GetGet FinalFinal TimeTime ValueValue

     Returns the ending time value of waveform in. The formula used is xf = x0 + duration of
     waveform in. Wire data to the waveform in input to determine the polymorphic
      instance to use or manually select the instance.


          • WDT Get Final Time Value DBL VI
          • DWDT Get Final Time Value VI

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - Get Final Time and
       Duration.vi

   WDTWDT GetGet FinalFinal TimeTime ValueValue DBLDBL VIVI

     Returns the ending time value of waveform in. The formula used is xf = x0 + duration of
     waveform in. Wire data to the waveform in input to determine the polymorphic
      instance to use or manually select the instance.


     Inputs/Outputs

            •     open interval? (T) —

         open interval? defines the interval over which the input waveform extends. The default is TRUE,
         which selects an open interval.

          For example, assume an input waveform contains 3 data elements at t= {0, dt, 2dt}. An open


862   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:862 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:863 ordinal=863 -->
## Functions

Functions


     interval defines the waveform as extending over the time interval 0 ≤ t< 2dt, and a closed
     interval defines the waveform as extending over the time interval 0 ≤ t< 3dt.

   •     waveform in —

    waveform in is the analog waveform for which you want to retrieve the final time value.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveform out —

    waveform out returns waveform in unchanged.

   •        tf —

      tf is the time value when the final data value was acquired.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Get Final Time and
   Duration.vi

DWDTDWDT GetGet FinalFinal TimeTime ValueValue VIVI

Returns the ending time value of waveform in. The formula used is xf = x0 + duration of
waveform in. Wire data to the waveform in input to determine the polymorphic
instance to use or manually select the instance.


                                                    © National Instruments 863

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:863 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:864 ordinal=864 -->
## Functions

Functions


     Inputs/Outputs

            •     open interval? (T) —

         open interval? defines the interval over which the input waveform extends. The default is TRUE,
         which selects an open interval.

          For example, assume an input waveform contains 3 data elements at t= {0, dt, 2dt}. An open
            interval defines the waveform as extending over the time interval 0 ≤ t< 2dt, and a closed
            interval defines the waveform as extending over the time interval 0 ≤ t< 3dt.

            •     waveform in —

         waveform in is the digital waveform for which you want to retrieve the final time value.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveform out —

         waveform out returns waveform in unchanged.

            •        tf —

              tf is the time value when the final data value was acquired.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - Get Final Time and
       Duration.vi

864   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:864 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:865 ordinal=865 -->
## Functions

Functions

WaveformWaveform DurationDuration

Computes the duration of waveform in using the following equation: duration =
(#samples-1) × dx. Wire data to the waveform in input to determine the polymorphic
instance to use or manually select the instance.


  • WDT Waveform Duration DBL VI
  • DWDT Waveform Duration VI

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Get Final Time and
   Duration.vi

WDTWDT WaveformWaveform DurationDuration DBLDBL VIVI

Computes the duration of waveform in using the following equation: duration =
(#samples-1) × dx. Wire data to the waveform in input to determine the polymorphic
instance to use or manually select the instance.


Inputs/Outputs

   •     open interval? (T) —

   open interval? defines the interval over which the input waveform extends. The default is TRUE,
    which selects an open interval.

    For example, assume an input waveform contains 3 data elements at t= {0, dt, 2dt}. An open


                                                    © National Instruments 865

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:865 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:866 ordinal=866 -->
## Functions

Functions


            interval defines the waveform as extending over the time interval 0 ≤ t< 2dt, and a closed
            interval defines the waveform as extending over the time interval 0 ≤ t< 3dt.

            •     waveform in —

         waveform in is the analog waveform for which you want the duration.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveform out —

         waveform out returns waveform in unchanged.

            •      duration —

          duration is the duration of the waveform.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - Get Final Time and
       Duration.vi

    DWDTDWDT WaveformWaveform DurationDuration VIVI

     Computes the duration of waveform in using the following equation: duration =
     (#samples-1) x dx. Wire data to the waveform in input to determine the polymorphic
      instance to use or manually select the instance.


866   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:866 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:867 ordinal=867 -->
## Functions

Functions


Inputs/Outputs

   •     open interval? (T) —

   open interval? defines the interval over which the input waveform extends. The default is TRUE,
    which selects an open interval.

    For example, assume an input waveform contains 3 data elements at t= {0, dt, 2dt}. An open
     interval defines the waveform as extending over the time interval 0 ≤ t< 2dt, and a closed
     interval defines the waveform as extending over the time interval 0 ≤ t< 3dt.

   •     waveform in —

    waveform in is the digital waveform for which you want the duration.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveform out —

    waveform out returns waveform in unchanged.

   •      duration —

    duration is the duration of the waveform.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Get Final Time and
   Duration.vi

                                                    © National Instruments 867

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:867 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:868 ordinal=868 -->
## Functions

Functions

    ScaleScale DeltaDelta tt

      Multiplies the delta t component of the waveform by the specified scale factor.
      Generally, this lengthens or shortens the sample rate of the waveform. The data type
     you wire to the waveform in input and the data type of the Y component of the analog
     waveform determine the polymorphic instance to use.


          • WDT Scale Delta t DBL VI
          • WDT Scale Delta t SGL VI
          • WDT Scale Delta t I64 VI
          • WDT Scale Delta t I32 VI
          • WDT Scale Delta t I16 VI
          • WDT Scale Delta t CDB VI
          • WDT Scale Delta t EXT VI
          • DWDT Scale Delta t VI

   WDTWDT ScaleScale DeltaDelta tt DBLDBL VIVI

      Multiplies the delta t component of the waveform by the specified scale factor.
      Generally, this lengthens or shortens the sample rate of the waveform. The data type
     you wire to the waveform in input and the data type of the Y component of the analog
     waveform determine the polymorphic instance to use.


     Inputs/Outputs

            •     waveform in —

         waveform in is the waveform for which you want to scale the delta t. The default is empty.

            •       scale factor —


868   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:868 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:869 ordinal=869 -->
## Functions

Functions


    scale factor is the number by which you multiply the waveform's delta t. A value of greater than
    zero but less than 1 shortens the sample rate. A value of greater than 1 increases the sample rate.
    The default is 1000.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveform out —

    waveform out returns the resulting waveform with the new delta t value.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


WDTWDT ScaleScale DeltaDelta tt SGLSGL VIVI

Multiplies the delta t component of the waveform by the specified scale factor.
Generally, this lengthens or shortens the sample rate of the waveform. The data type
you wire to the waveform in input and the data type of the Y component of the analog
waveform determine the polymorphic instance to use.


Inputs/Outputs

   •     waveform in —

    waveform in is the waveform for which you want to scale the delta t. The default is empty.

   •       scale factor —

    scale factor is the number by which you multiply the waveform's delta t. A value of greater than
    zero but less than 1 shortens the sample rate. A value of greater than 1 increases the sample rate.
    The default is 1000.

   •       error in (no error) —

                                                    © National Instruments 869

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:869 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:870 ordinal=870 -->
## Functions

Functions


           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveform out —

         waveform out returns the resulting waveform with the new delta t value.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


   WDTWDT ScaleScale DeltaDelta tt I64I64 VIVI

      Multiplies the delta t component of the waveform by the specified scale factor.
      Generally, this lengthens or shortens the sample rate of the waveform. The data type
     you wire to the waveform in input and the data type of the Y component of the analog
     waveform determine the polymorphic instance to use.


     Inputs/Outputs

            •     waveform in —

         waveform in is the waveform for which you want to scale the delta t. The default is empty.

            •       scale factor —

           scale factor is the number by which you multiply the waveform's delta t. A value of greater than
           zero but less than 1 shortens the sample rate. A value of greater than 1 increases the sample rate.
         The default is 1000.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveform out —


870   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:870 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:871 ordinal=871 -->
## Functions

Functions


    waveform out returns the resulting waveform with the new delta t value.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


WDTWDT ScaleScale DeltaDelta tt I32I32 VIVI

Multiplies the delta t component of the waveform by the specified scale factor.
Generally, this lengthens or shortens the sample rate of the waveform. The data type
you wire to the waveform in input and the data type of the Y component of the analog
waveform determine the polymorphic instance to use.


Inputs/Outputs

   •     waveform in —

    waveform in is the waveform for which you want to scale the delta t. The default is empty.

   •       scale factor —

    scale factor is the number by which you multiply the waveform's delta t. A value of greater than
    zero but less than 1 shortens the sample rate. A value of greater than 1 increases the sample rate.
    The default is 1000.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveform out —

    waveform out returns the resulting waveform with the new delta t value.

   •       error out —


                                                    © National Instruments 871

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:871 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:872 ordinal=872 -->
## Functions

Functions


           error out contains error information. This output provides standard error out functionality.


   WDTWDT ScaleScale DeltaDelta tt I16I16 VIVI

      Multiplies the delta t component of the waveform by the specified scale factor.
      Generally, this lengthens or shortens the sample rate of the waveform. The data type
     you wire to the waveform in input and the data type of the Y component of the analog
     waveform determine the polymorphic instance to use.


     Inputs/Outputs

            •     waveform in —

         waveform in is the waveform for which you want to scale the delta t. The default is empty.

            •       scale factor —

           scale factor is the number by which you multiply the waveform's delta t. A value of greater than
           zero but less than 1 shortens the sample rate. A value of greater than 1 increases the sample rate.
         The default is 1000.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveform out —

         waveform out returns the resulting waveform with the new delta t value.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


872   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:872 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:873 ordinal=873 -->
## Functions

Functions

WDTWDT ScaleScale DeltaDelta tt CDBCDB VIVI

Multiplies the delta t component of the waveform by the specified scale factor.
Generally, this lengthens or shortens the sample rate of the waveform. The data type
you wire to the waveform in input and the data type of the Y component of the analog
waveform determine the polymorphic instance to use.


Inputs/Outputs

   •     waveform in —

    waveform in is the waveform for which you want to scale the delta t. The default is empty.

   •       scale factor —

    scale factor is the number by which you multiply the waveform's delta t. A value of greater than
    zero but less than 1 shortens the sample rate. A value of greater than 1 increases the sample rate.
    The default is 1000.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveform out —

    waveform out returns the resulting waveform with the new delta t value.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


WDTWDT ScaleScale DeltaDelta tt EXTEXT VIVI

Multiplies the delta t component of the waveform by the specified scale factor.
Generally, this lengthens or shortens the sample rate of the waveform. The data type
you wire to the waveform in input and the data type of the Y component of the analog

                                                    © National Instruments 873

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:873 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:874 ordinal=874 -->
## Functions

Functions

     waveform determine the polymorphic instance to use.


     Inputs/Outputs

            •     waveform in —

         waveform in is the waveform for which you want to scale the delta t. The default is empty.

            •       scale factor —

           scale factor is the number by which you multiply the waveform's delta t. A value of greater than
           zero but less than 1 shortens the sample rate. A value of greater than 1 increases the sample rate.
         The default is 1000.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveform out —

         waveform out returns the resulting waveform with the new delta t value.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


    DWDTDWDT ScaleScale DeltaDelta tt VIVI

      Multiplies the delta t component of the waveform by the specified scale factor.
      Generally, this lengthens or shortens the sample rate of the waveform. The data type
     you wire to the waveform in input and the data type of the Y component of the analog
     waveform determine the polymorphic instance to use.


874   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:874 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:875 ordinal=875 -->
## Functions

Functions


Inputs/Outputs

   •     waveform in —

    waveform in is the waveform for which you want to scale the delta t. The default is empty.

   •       scale factor —

    scale factor is the number by which you multiply the waveform's delta t. A value of greater than
    zero but less than 1 shortens the sample rate. A value of greater than 1 increases the sample rate.
    The default is 1000.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveform out —

    waveform out returns the resulting waveform with the new delta t value.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

GetGet XYXY ValueValue

Returns the X and Y value of a waveform or digital data set. The data type you wire to
the waveform in input and the data type of the Y component of the analog waveform
determine the polymorphic instance to use.


  • WDT Get XY Value DBL VI
  • WDT Get XY Value I64 VI
  • WDT Get XY Value I32 VI


                                                    © National Instruments 875

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:875 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:876 ordinal=876 -->
## Functions

Functions

          • WDT Get XY Value I16 VI
          • WDT Get XY Value CDB VI
          • WDT Get XY Value EXT VI
          • WDT Get XY Value CXT VI
          • DWDT Get XY Value VI
          • DTbl Get Digital Value VI

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - Get Y Value.vi

   WDTWDT GetGet XYXY ValueValue DBLDBL VIVI

     Returns the X and Y value of a waveform or digital data set. The data type you wire to
     the waveform in input and the data type of the Y component of the analog waveform
     determine the polymorphic instance to use.


     Inputs/Outputs

            •     waveform in —

         waveform in is the analog waveform for which you want to retrieve a specified data value (X and
          Y value). The default is empty.

            •      Y position format —

         Y position format indicates if you want to retrieve the data value of the specified element or at a
           specified time.

          0 Samples—Returns the data value of the specified sample in the waveform data.
          1 Relative Time—Returns the data value at a specified time relative to the first point in the


876   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:876 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:877 ordinal=877 -->
## Functions

Functions


     waveform.

   •      Y position —

    Y position is the element number you want from the set of waveform data or the value at a
     specified time. The default is 0.

    For example, if you want the value of the 200th scan, wire 199 to this input. If you want the value
     at time 100, wire 100 to this input. You select whether this is a samples or relative time Y
    position format. In Relative Time mode, this VI checks the Y position input to determine if it is
    an integer multiple of dt. If Y position is not an integer multiple of dt, the VI uses the closest
    exact multiple of dt.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     X value —

    X value returns the X value.

   •     waveform out —

    waveform out returns waveform in unchanged.

   •      actual Y position —

    actual Y position is the actual index or time value of the point returned.

   •      Y value —

    Y value returns the Y value.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.


                                                    © National Instruments 877

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:877 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:878 ordinal=878 -->
## Functions

Functions

          • labview\examples\Waveform\Waveform - Get Y Value.vi

   WDTWDT GetGet XYXY ValueValue I64I64 VIVI

     Returns the X and Y value of a waveform or digital data set. The data type you wire to
     the waveform in input and the data type of the Y component of the analog waveform
     determine the polymorphic instance to use.


     Inputs/Outputs

            •     waveform in —

         waveform in is the analog waveform for which you want to retrieve a specified data value (X and
          Y value). The default is empty.

            •      Y position format —

         Y position format indicates if you want to retrieve the data value of the specified element or at a
           specified time.

          0 Samples—Returns the data value of the specified sample in the waveform data.
            Relative Time—Returns the data value at a specified time relative to the first point in the
          1           waveform.

            •      Y position —

         Y position is the element number you want from the set of waveform data or the value at a
           specified time. The default is 0.

          For example, if you want the value of the 200th scan, wire 199 to this input. If you want the value
           at time 100, wire 100 to this input. You select whether this is a samples or relative time Y
           position format. In Relative Time mode, this VI checks the Y position input to determine if it is
         an integer multiple of dt. If Y position is not an integer multiple of dt, the VI uses the closest
           exact multiple of dt.

            •       error in (no error) —

878   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:878 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:879 ordinal=879 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     X value —

    X value returns the X value.

   •     waveform out —

    waveform out returns waveform in unchanged.

   •      actual Y position —

    actual Y position is the actual index or time value of the point returned.

   •      Y value —

    Y value returns the Y value.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Get Y Value.vi

WDTWDT GetGet XYXY ValueValue I32I32 VIVI

Returns the X and Y value of a waveform or digital data set. The data type you wire to
the waveform in input and the data type of the Y component of the analog waveform
determine the polymorphic instance to use.


                                                    © National Instruments 879

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:879 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:880 ordinal=880 -->
## Functions

Functions

     Inputs/Outputs

            •     waveform in —

         waveform in is the analog waveform for which you want to retrieve a specified data value (X and
          Y value). The default is empty.

            •      Y position format —

         Y position format indicates if you want to retrieve the data value of the specified element or at a
           specified time.

          0 Samples—Returns the data value of the specified sample in the waveform data.
            Relative Time—Returns the data value at a specified time relative to the first point in the          1           waveform.

            •      Y position —

         Y position is the element number you want from the set of waveform data or the value at a
           specified time. The default is 0.

          For example, if you want the value of the 200th scan, wire 199 to this input. If you want the value
           at time 100, wire 100 to this input. You select whether this is a samples or relative time Y
           position format. In Relative Time mode, this VI checks the Y position input to determine if it is
         an integer multiple of dt. If Y position is not an integer multiple of dt, the VI uses the closest
           exact multiple of dt.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     X value —

         X value returns the X value.

            •     waveform out —

         waveform out returns waveform in unchanged.

            •      actual Y position —

           actual Y position is the actual index or time value of the point returned.


880   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:880 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:881 ordinal=881 -->
## Functions

Functions

   •      Y value —

    Y value returns the Y value.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Get Y Value.vi

WDTWDT GetGet XYXY ValueValue I16I16 VIVI

Returns the X and Y value of a waveform or digital data set. The data type you wire to
the waveform in input and the data type of the Y component of the analog waveform
determine the polymorphic instance to use.


Inputs/Outputs

   •     waveform in —

    waveform in is the analog waveform for which you want to retrieve a specified data value (X and
    Y value). The default is empty.

   •      Y position format —

    Y position format indicates if you want to retrieve the data value of the specified element or at a
     specified time.

    0 Samples—Returns the data value of the specified sample in the waveform data.


                                                    © National Instruments 881

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:881 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:882 ordinal=882 -->
## Functions

Functions


            Relative Time—Returns the data value at a specified time relative to the first point in the          1
           waveform.

            •      Y position —

         Y position is the element number you want from the set of waveform data or the value at a
           specified time. The default is 0.

          For example, if you want the value of the 200th scan, wire 199 to this input. If you want the value
           at time 100, wire 100 to this input. You select whether this is a samples or relative time Y
           position format. In Relative Time mode, this VI checks the Y position input to determine if it is
         an integer multiple of dt. If Y position is not an integer multiple of dt, the VI uses the closest
           exact multiple of dt.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     X value —

         X value returns the X value.

            •     waveform out —

         waveform out returns waveform in unchanged.

            •      actual Y position —

           actual Y position is the actual index or time value of the point returned.

            •      Y value —

         Y value returns the Y value.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


    Examples

      Refer to the following example files included with LabVIEW.

882   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:882 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:883 ordinal=883 -->
## Functions

Functions

  • labview\examples\Waveform\Waveform - Get Y Value.vi

WDTWDT GetGet XYXY ValueValue CDBCDB VIVI

Returns the X and Y value of a waveform or digital data set. The data type you wire to
the waveform in input and the data type of the Y component of the analog waveform
determine the polymorphic instance to use.


Inputs/Outputs

   •     waveform in —

    waveform in is the analog waveform for which you want to retrieve a specified data value (X and
    Y value). The default is empty.

   •      Y position format —

    Y position format indicates if you want to retrieve the data value of the specified element or at a
     specified time.

    0 Samples—Returns the data value of the specified sample in the waveform data.
      Relative Time—Returns the data value at a specified time relative to the first point in the
    1     waveform.

   •      Y position —

    Y position is the element number you want from the set of waveform data or the value at a
     specified time. The default is 0.

    For example, if you want the value of the 200th scan, wire 199 to this input. If you want the value
     at time 100, wire 100 to this input. You select whether this is a samples or relative time Y
    position format. In Relative Time mode, this VI checks the Y position input to determine if it is
    an integer multiple of dt. If Y position is not an integer multiple of dt, the VI uses the closest
    exact multiple of dt.

   •       error in (no error) —

                                                    © National Instruments 883

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:883 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:884 ordinal=884 -->
## Functions

Functions


           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     X value —

         X value returns the X value.

            •     waveform out —

         waveform out returns waveform in unchanged.

            •      actual Y position —

           actual Y position is the actual index or time value of the point returned.

            •      Y value —

         Y value returns the Y value.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - Get Y Value.vi

   WDTWDT GetGet XYXY ValueValue EXTEXT VIVI

     Returns the X and Y value of a waveform or digital data set. The data type you wire to
     the waveform in input and the data type of the Y component of the analog waveform
     determine the polymorphic instance to use.


884   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:884 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:885 ordinal=885 -->
## Functions

Functions

Inputs/Outputs

   •     waveform in —

    waveform in is the analog waveform for which you want to retrieve a specified data value (X and
    Y value). The default is empty.

   •      Y position format —

    Y position format indicates if you want to retrieve the data value of the specified element or at a
     specified time.

    0 Samples—Returns the data value of the specified sample in the waveform data.
      Relative Time—Returns the data value at a specified time relative to the first point in the    1     waveform.

   •      Y position —

    Y position is the element number you want from the set of waveform data or the value at a
     specified time. The default is 0.

    For example, if you want the value of the 200th scan, wire 199 to this input. If you want the value
     at time 100, wire 100 to this input. You select whether this is a samples or relative time Y
    position format. In Relative Time mode, this VI checks the Y position input to determine if it is
    an integer multiple of dt. If Y position is not an integer multiple of dt, the VI uses the closest
    exact multiple of dt.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     X value —

    X value returns the X value.

   •     waveform out —

    waveform out returns waveform in unchanged.

   •      actual Y position —

    actual Y position is the actual index or time value of the point returned.


                                                    © National Instruments 885

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:885 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:886 ordinal=886 -->
## Functions

Functions

            •      Y value —

         Y value returns the Y value.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - Get Y Value.vi

   WDTWDT GetGet XYXY ValueValue CXTCXT VIVI

     Returns the X and Y value of a waveform or digital data set. The data type you wire to
     the waveform in input and the data type of the Y component of the analog waveform
     determine the polymorphic instance to use.


     Inputs/Outputs

            •     waveform in —

         waveform in is the analog waveform for which you want to retrieve a specified data value (X and
          Y value). The default is empty.

            •      Y position format —

         Y position format indicates if you want to retrieve the data value of the specified element or at a
           specified time.

          0 Samples—Returns the data value of the specified sample in the waveform data.


886   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:886 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:887 ordinal=887 -->
## Functions

Functions


      Relative Time—Returns the data value at a specified time relative to the first point in the    1
     waveform.

   •      Y position —

    Y position is the element number you want from the set of waveform data or the value at a
     specified time. The default is 0.

    For example, if you want the value of the 200th scan, wire 199 to this input. If you want the value
     at time 100, wire 100 to this input. You select whether this is a samples or relative time Y
    position format. In Relative Time mode, this VI checks the Y position input to determine if it is
    an integer multiple of dt. If Y position is not an integer multiple of dt, the VI uses the closest
    exact multiple of dt.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     X value —

    X value returns the X value.

   •     waveform out —

    waveform out returns waveform in unchanged.

   •      actual Y position —

    actual Y position is the actual index or time value of the point returned.

   •      Y value —

    Y value returns the Y value.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

                                                    © National Instruments 887

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:887 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:888 ordinal=888 -->
## Functions

Functions

          • labview\examples\Waveform\Waveform - Get Y Value.vi

    DWDTDWDT GetGet XYXY ValueValue VIVI

     Returns the X and Y value of a waveform or digital data set. The data type you wire to
     the waveform in input and the data type of the Y component of the analog waveform
     determine the polymorphic instance to use.


     Inputs/Outputs

            •     waveform in —

         waveform in is the digital waveform for which you want to retrieve a specified data value (X and
          Y value). The default is empty.

            •      Y position format —

         Y position format indicates if you want to retrieve the data value of the specified element or at a
           specified time.

          0 Samples—Returns the data value of the specified sample in the waveform data.
            Relative Time—Returns the data value at a specified time relative to the first point in the
          1           waveform.

            •      Y position —

         Y position is the element number you want from the set of waveform data or the value at a
           specified time. The default is 0.

          For example, if you want the value of the 200th scan, wire 199 to this input. If you want the value
           at time 100, wire 100 to this input. You select whether this is a samples or relative time Y
           position format. In Relative Time mode, this VI checks the Y position input to determine if it is
         an integer multiple of dt. If Y position is not an integer multiple of dt, the VI uses the closest
           exact multiple of dt.


888   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:888 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:889 ordinal=889 -->
## Functions

Functions

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     X value —

    X value returns the X value.

   •     waveform out —

    waveform out returns waveform in unchanged.

   •      actual Y position —

    actual Y position is the actual index or time value of the point returned.

   •      Y value —

    Y value returns an array of Y values.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •     waveform data value —

    waveform data value returns the values of the waveform data.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Get Y Value.vi

DTblDTbl GetGet DigitalDigital ValueValue VIVI

Returns the X and Y value of a waveform or digital data set. The data type you wire to
the waveform in input and the data type of the Y component of the analog waveform
determine the polymorphic instance to use.


                                                    © National Instruments 889

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:889 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:890 ordinal=890 -->
## Functions

Functions


     Inputs/Outputs

            •       digital data in —

            digital data in is the set of digital data for which you want to retrieve the X and Y values.

            •       Start —

           Start is the data element or time value where you want to start acquiring X and Y values.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     Compressed Index —

         Compressed Index returns the index of the data element or time value with respect to the
         compressed waveform. For example, if the actual sample number is 8 but the sample is
         compressed in a portion of the waveform that starts at 3, the compressed index is 3.

            •       digital data out —

            digital data out returns digital data in unchanged.

            •     Sample Number —

         Sample Number returns the sample number of the data element or time value. If the value of
           Start is inside a compressed portion of the waveform, Sample Number is the sample number
           calculated as if the waveform was not compressed.

            •       digital value —

            digital value returns an array of Y values.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


890   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:890 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:891 ordinal=891 -->
## Functions

Functions

   •       digital data value —

     digital data value returns the values of the digital data.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Get Y Value.vi

GetGet WaveformWaveform TimeTime ArrayArray

Creates an array of waveform time stamps. Each element in the array is the time stamp
for each data value in the waveform. Wire data to the waveform in input to determine
the polymorphic instance to use or manually select the instance.


  • WDT Get Waveform Time Array DBL VI
  • DWDT Get Waveform Time Array VI

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Get Time Array.vi

WDTWDT GetGet WaveformWaveform TimeTime ArrayArray DBLDBL VIVI

Creates an array of waveform time stamps. Each element in the array is the time stamp
for each data value in the waveform. Wire data to the waveform in input to determine
the polymorphic instance to use or manually select the instance.


                                                    © National Instruments 891

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:891 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:892 ordinal=892 -->
## Functions

Functions

     Inputs/Outputs

            •     waveform in —

         waveform in is the waveform for which you want to retrieve the time stamp information.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     X array —

         X array is the array of waveform time stamps.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - Get Time Array.vi

    DWDTDWDT GetGet WaveformWaveform TimeTime ArrayArray VIVI

     Creates an array of waveform time stamps. Each element in the array is the time stamp
      for each data value in the waveform. Wire data to the waveform in input to determine
     the polymorphic instance to use or manually select the instance.


     Inputs/Outputs

            •     waveform in —

         waveform in is the digital waveform for which you want to retrieve the time stamp information.


892   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:892 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:893 ordinal=893 -->
## Functions

Functions

   •     match transition array —

    match transition array specifies whether the timestamp array output contains a timestamp for
    every Y value in a digital waveform or for only the Y values identified as transitions in a
    compressed digital waveform. The default is FALSE, which means this VI returns the timestamps
     of all Y values in the digital waveform.

       If the digital waveform is uncompressed, this VI treats this input as FALSE.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     X array —

    X array is the array of waveform time stamps.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Get Time Array.vi

AnalogAnalog WaveformWaveform

Use the Analog Waveform VIs and functions to perform arithmetic and comparison
functions on waveforms.

      Note Many Analog Waveform VIs are available only in the LabVIEW Full and
        Professional Development Systems. If you have the LabVIEW Base
       Development System, you do not have the full set of the Analog Waveform
        VIs described in this help file.

The VIs and functions on this palette can return waveform error codes.


                                                    © National Instruments 893

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:893 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:894 ordinal=894 -->
## Functions

Functions


       Palette Object  Description

       Get Waveform  Returns the analog waveform you specify. You specify components by clicking on
      Components   the center of the output terminal and selecting the component you want.

                       Builds an analog waveform or modifies an existing waveform. If you do not wire the
       Build         waveform input, the function creates a new waveform based on the components
      Waveform     you wire. If you wire the waveform input, the function modifies the waveform
                    based on the components you wire.

       Set Waveform                   Adds or replaces a waveform attribute. You can use any type of data for the value        Attribute                        of the attribute.       Function

       Get Waveform                       Retrieves the names and values of all attributes or the value of a single attribute,        Attribute
                    depending on whether you wire the name parameter.       Function

      Waveform                       Scales the waveform data using the equation waveform out = (scale * waveform in
       Scale and                    + offset).        Offset


       Normalize     Determines the scale and offset necessary to transform the waveform data so that
      Waveform        its maximum is 1.00 and its minimum is -1.00.


                   Appends waveform B to the end of waveform A. If the sampling rates do not
      Append       match, the error cluster returns an error. The trigger time of waveform B is ignored.
      Waveforms    The data type of the Y component of waveform A and waveform B determines the
                     polymorphic instance to use or you can manually select the instance.


      Number of
                      Returns the number of data elements in the waveform. You must manually select
      Waveform
                      the polymorphic instance you want to use.
      Samples


      Waveform Min  Determines the maximum and minimum values and their associate time values for
      Max          a waveform.


894   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:894 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:895 ordinal=895 -->
## Functions

Functions


 Palette Object  Description

 Waveform
 Scalar Limit    Compares the waveform data values to a scalar value.
 Comparison

 Search               Returns the time value in x for the value specified. Waveform


                Creates an array of data values and their corresponding time stamps. Wire the data
 Waveform to               type of the Y component to the waveform in input to determine the polymorphic XY Pairs                instance to use or manually select the instance.


 Waveform              Use the waveform constant to hold acquired data for analysis and display. Constant


 Waveform     Use the Waveform Generation VIs to generate different types of single and multi-
 Generation     tone signals, function generator signals, and noise signals.


              Use the Waveform Measurements VIs to perform common time and frequency
 Waveform             domain measurements, such as DC, RMS, Tone Frequency/Amplitude/Phase, Measurements              Harmonic Distortion, SINAD, and Averaged FFT Measurements.


GetGet WaveformWaveform ComponentsComponents

Returns the analog waveform you specify. You specify components by clicking on the
center of the output terminal and selecting the component you want.


Inputs/Outputs

   •     waveform —


                                                    © National Instruments 895

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:895 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:896 ordinal=896 -->
## Functions

Functions


         waveform is the waveform from which you want to retrieve components.

            •       t0 —

           t0 returns the trigger time of the waveform.

            •      dt —

          dt returns the time interval in seconds between data points in the waveform.

            •      Y —

         Y returns the data values of the waveform.

            •       attributes —

           attributes returns the names and values of all waveform attributes.

         You also can use the Get Waveform Attribute VI to retrieve the names and values of all attributes
           or the value of a single attribute.

     BuildBuild WaveformWaveform

      Builds an analog waveform or modifies an existing waveform. If you do not wire the
     waveform input, the function creates a new waveform based on the components you
      wire. If you wire the waveform input, the function modifies the waveform based on the
     components you wire.


     Inputs/Outputs

            •     waveform —

         waveform is the analog waveform you want to edit. If you do not wire an existing waveform, the
           function creates a new waveform based on the components you wire.

            •       t0 —


896   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:896 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:897 ordinal=897 -->
## Functions

Functions


    t0 specifies the start time of the waveform.

   •      dt —

    dt specifies the time interval in seconds between data points in the waveform.

   •      Y —

    Y specifies the data values of the waveform.

   •       attributes —

    attributes sets the names and values of all waveform attributes.

    You also can use the Set Waveform Attribute function to set the name and value of a single
     attribute.

   •      output waveform —

    waveform is the resulting waveform. If you did not wire an existing waveform, this is a new
    waveform. If you wired an existing waveform, this is the edited waveform.


SetSet WaveformWaveform AttributeAttribute FunctionFunction

Adds or replaces a waveform attribute. You can use any type of data for the value of
the attribute.


Inputs/Outputs

   •     waveform —

    waveform is the waveform for which you want to add or replace an attribute.

   •     name —

   name is the name of the attribute.


                                                    © National Instruments 897

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:897 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:898 ordinal=898 -->
## Functions

Functions

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
    new value, and replaced is TRUE. If the attribute in name does not exist already, the
      function creates a new attribute. Some attributes are set by NI-DAQ and Express VIs.

     The following table lists the waveform attributes set by NI-DAQ.


                                  Data     Name     Attribute                 Acceptable Values   Description
                                Type

      Hardware                        Any value is        NI_DeviceNumber is the device
       Device    NI_DeviceNumber   String  acceptable for     number of the hardware producing
      Number                           NI_DeviceNumber.  the waveform.

                                      Any value is        NI_ChannelName is the name of the
     Name of
               NI_ChannelName   String  acceptable for        virtual channel producing the
      Channel
                                       NI_ChannelName.   waveform.

                                                         NI_LineNames is the name of the
     Name of                         Any value is           digital line in the waveform. For more
        Digital    NI_LineNames      String  acceptable for      than one digital line, the function
        Line(s)                            NI_LineNames.      returns the line names in reverse
                                                                      order.


898   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:898 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:899 ordinal=899 -->
## Functions

Functions


                                            Volts, PSI, and so
                                         forth are Unit for                                                   NI_UnitDescription is the units of            NI_UnitDescription  String  acceptable values Data                                              measure for the waveform.                                           for
                                       NI_UnitDescription.

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
                                       Any value is acceptable  data is generated in a Start                          Time
            NI_ExpStartTimeStamp            for                      loop. In Express VIs, Timestamp                     stamp                                           NI_ExpStartTimeStamp. NI_ExpStartTimeStamp is
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
                               Time    Any value is acceptable  according to the PC clock
 Timestamp NI_ExpTimeStamp
                               stamp    for NI_ExpTimeStamp.   unless the waveform
                                                                          originates in NI-DAQ.
                                                    When the waveform
                                                                          originates in NI-DAQ, NI-
                                                   DAQ sets
                                                               NI_ExpTimeStamp.

 X          NI_ExpXDimension      String   Use a single character      If the value of

                                                    © National Instruments 899

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:899 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:900 ordinal=900 -->
## Functions

Functions


                                                                    NI_ExpXDimension is t, t0                                                           for the
                                                               and dt are unchanged. If                                               NI_ExpXDimension                                                                          the value of                                                        value. Currently, only t                                                                    NI_ExpXDimension is f,                                                           for time and f for      Dimension                                                          Express VIs interpret t0                                                  frequency are
                                                               and dt as f0 and df. For all                                                  supported. The value                                                                           other values, or unknown                                                           for NI_ExpXDimension                                                                        dimension, t0 and dt are                                                                      is case sensitive.                                                                               interpreted as X0 and dX.

                                                                                                                          If and only if
                                         TRUE or FALSE are      NI_ExpXDimension is t,        Relative                   NI_ExpIsRelativeTime   Boolean  acceptable values for    Express VIs set t0 as a      Time?                                                    NI_ExpIsRelativeTime.   relative/absolute time
                                                                 stamp value.

          Note Express VIs also use the attributes set by NI-DAQ. If the waveform does
            not originate in NI-DAQ, Express VIs add NI_ChannelName.

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - Create.vi

     GetGet WaveformWaveform AttributeAttribute FunctionFunction

      Retrieves the names and values of all attributes or the value of a single attribute,
     depending on whether you wire the name parameter.

      Attributes can be channel names. The connector pane displays the default data types
      for this polymorphic function.


900   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:900 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:901 ordinal=901 -->
## Functions

Functions

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


                                                    © National Instruments 901

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:901 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:902 ordinal=902 -->
## Functions

Functions


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
     Name     Attribute                 Acceptable Values        Description                                Type

      Hardware                                               NI_DeviceNumber is the device                                      Any value is acceptable       Device    NI_DeviceNumber   String                     number of the hardware device                                                   for NI_DeviceNumber.
      Number                                                   producing the waveform.

                                                           NI_ChannelName is the name of     Name of                         Any value is acceptable
               NI_ChannelName   String                          the virtual channel producing      Channel                                  for NI_ChannelName.                                                                   the waveform.

     Name of                                      Any value is acceptable   NI_LineNames is the name of        Digital    NI_LineNames      String                                                   for NI_LineNames.       the digital line in the waveform.
        Line(s)

                                                    Volts, PSI, and so forth       Unit for                                                       NI_UnitDescription is the units
                  NI_UnitDescription  String  are acceptable values for
       Data                                                              of measure for the waveform.
                                              NI_UnitDescription.

     The following table lists the waveform attributes set by Express VIs.


                                      Data
     Name       Attribute                       Acceptable Values       Description
                                    Type

                                                                      NI_ExpStartTimeStamp is
                                             Any value is acceptable
        Start                          Time                            the time stamp of the first
                  NI_ExpStartTimeStamp            for
      Timestamp                     stamp                        sample in the first
                                                 NI_ExpStartTimeStamp.
                                                                     waveform. In Express VIs,


902   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:902 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:903 ordinal=903 -->
## Functions

Functions


                                DataName       Attribute                       Acceptable Values       Description
                              Type

                                                                               this is set once per start
                                                                         of the VI and does not
                                                                 change, even if waveform
                                                                  data is generated in a
                                                                        loop. In Express VIs,
                                                               NI_ExpStartTimeStamp is
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
                              Time    Any value is acceptable  according to the PC clockTimestamp NI_ExpTimeStamp                              stamp    for NI_ExpTimeStamp.   unless the waveform
                                                                         originates in NI-DAQ.
                                                    When the waveform
                                                                         originates in NI-DAQ, NI-
                                                   DAQ sets
                                                              NI_ExpTimeStamp.

                                                                                                              If the value of
                                                              NI_ExpXDimension is t, t0
                                      Use a single character
                                                         and dt are unchanged. If
                                                   for the
                                                                   the value of
                                        NI_ExpXDimension
                                                              NI_ExpXDimension is f,
                                                value. Currently, only t
X                                                                  Express VIs interpret t0
           NI_ExpXDimension      String    for time and f for
Dimension                                                 and dt as f0 and df. For all
                                           frequency are
                                                                    other values, Express VIs
                                           supported. The value
                                                                          generically interpret t0
                                                   for NI_ExpXDimension
                                                         and dt as X0 and dX, but
                                                            is case sensitive.
                                                                     there is no effect
                                                                      otherwise.

Relative                             TRUE or FALSE are           If and only if
            NI_ExpIsRelativeTime   Boolean
Time?                                      acceptable values for    NI_ExpXDimension is t,

                                                    © National Instruments 903

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:903 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:904 ordinal=904 -->
## Functions

Functions


                                      Data     Name       Attribute                       Acceptable Values       Description
                                    Type

                                                                           Express VIs set t0 as a
                                                    NI_ExpIsRelativeTime.   relative/absolute time
                                                                 stamp value.

          Note Express VIs also use the attributes set by NI-DAQ. If the waveform does
            not originate in NI-DAQ, Express VIs add NI_ChannelName.

    WaveformWaveform ScaleScale andand OffsetOffset

     Scales the waveform data using the equation waveform out = (scale * waveform in +
      offset).


     Inputs/Outputs

            •     waveform in —

         waveform in is the waveform for which you want to multiply the data values.

            •       offset —

            offset is the value to add to the waveform values according to the following equation: y= (scale
           * x) + offset, where xis the data from the waveform in and yis the data written to the waveform
           out. The default is 0.

            •       scale —

           scale is the number by which you multiply the waveform data values. A value of greater than
           zero but less than 1 decreases the waveform amplitude. A value of greater than 1 increases the
         waveform amplitude. The default is 1.0.

            •       error in (no error) —


904   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:904 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:905 ordinal=905 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveform out —

    waveform out is the resulting waveform with the new scaled data values.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Scale and Offset.vi

NormalizeNormalize WaveformWaveform

Determines the scale and offset necessary to transform the waveform data so that its
maximum is 1.00 and its minimum is -1.00.


Inputs/Outputs

   •     waveform in —

    waveform in is the waveform you want to normalize.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      normalized waveform —


                                                    © National Instruments 905

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:905 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:906 ordinal=906 -->
## Functions

Functions


          normalized waveform is the resulting signal.

            •       scale —

           scale identifies the factor by which the waveform was multiplied.

            •       offset —

            offset identifies the amount the waveform was shifted.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


     The transformation is given by the following equation.


    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - Normalize.vi

    AppendAppend WaveformsWaveforms

     Appends waveform B to the end of waveform A. If the sampling rates do not match,
     the error cluster returns an error. The trigger time of waveform B is ignored. The data
     type of the Y component of waveform A and waveform B determines the polymorphic
      instance to use or you can manually select the instance.


          • WDT Append Waveforms DBL VI
          • WDT Append Waveforms I64 VI
          • WDT Append Waveforms I32 VI
          • WDT Append Waveforms I16 VI

906   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:906 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:907 ordinal=907 -->
## Functions

Functions

  • WDT Append Waveforms CDB VI
  • WDT Append Waveforms EXT VI
  • WDT Append Waveforms CXT VI

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Append.vi
WDTWDT AppendAppend WaveformsWaveforms DBLDBL VIVI

Appends waveform B to the end of waveform A. If the sampling rates do not match,
the error cluster returns an error. The trigger time of waveform B is ignored. The data
type of the Y component of waveform A and waveform B determines the polymorphic
instance to use or you can manually select the instance.


Inputs/Outputs

   •     waveform A —

    waveform A is the first set of data in the waveform.

   •     waveform B —

    waveform B is the set of data appended to the end of waveform A.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveform out —

    waveform out is the waveform that results from appending waveform B to waveform A.


                                                    © National Instruments 907

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:907 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:908 ordinal=908 -->
## Functions

Functions

            •       error out —

           error out contains error information. This output provides standard error out functionality.


    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - Append.vi
  WDTWDT AppendAppend WaveformsWaveforms I64I64 VIVI

     Appends waveform B to the end of waveform A. If the sampling rates do not match,
     the error cluster returns an error. The trigger time of waveform B is ignored. The data
     type of the Y component of waveform A and waveform B determines the polymorphic
      instance to use or you can manually select the instance.


     Inputs/Outputs

            •     waveform A —

         waveform A is the first set of data in the waveform.

            •     waveform B —

         waveform B is the set of data appended to the end of waveform A.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveform out —

         waveform out is the waveform that results from appending waveform B to waveform A.


908   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:908 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:909 ordinal=909 -->
## Functions

Functions

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Append.vi
WDTWDT AppendAppend WaveformsWaveforms I32I32 VIVI

Appends waveform B to the end of waveform A. If the sampling rates do not match,
the error cluster returns an error. The trigger time of waveform B is ignored. The data
type of the Y component of waveform A and waveform B determines the polymorphic
instance to use or you can manually select the instance.


Inputs/Outputs

   •     waveform A —

    waveform A is the first set of data in the waveform.

   •     waveform B —

    waveform B is the set of data appended to the end of waveform A.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveform out —

    waveform out is the waveform that results from appending waveform B to waveform A.


                                                    © National Instruments 909

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:909 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:910 ordinal=910 -->
## Functions

Functions

            •       error out —

           error out contains error information. This output provides standard error out functionality.


    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - Append.vi
  WDTWDT AppendAppend WaveformsWaveforms I16I16 VIVI

     Appends waveform B to the end of waveform A. If the sampling rates do not match,
     the error cluster returns an error. The trigger time of waveform B is ignored. The data
     type of the Y component of waveform A and waveform B determines the polymorphic
      instance to use or you can manually select the instance.


     Inputs/Outputs

            •     waveform A —

         waveform A is the first set of data in the waveform.

            •     waveform B —

         waveform B is the set of data appended to the end of waveform A.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveform out —

         waveform out is the waveform that results from appending waveform B to waveform A.


910   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:910 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:911 ordinal=911 -->
## Functions

Functions

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Append.vi
WDTWDT AppendAppend WaveformsWaveforms CDBCDB VIVI

Appends waveform B to the end of waveform A. If the sampling rates do not match,
the error cluster returns an error. The trigger time of waveform B is ignored. The data
type of the Y component of waveform A and waveform B determines the polymorphic
instance to use or you can manually select the instance.


Inputs/Outputs

   •     waveform A —

    waveform A is the first set of data in the waveform.

   •     waveform B —

    waveform B is the set of data appended to the end of waveform A.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveform out —

    waveform out is the waveform that results from appending waveform B to waveform A.


                                                    © National Instruments 911

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:911 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:912 ordinal=912 -->
## Functions

Functions

            •       error out —

           error out contains error information. This output provides standard error out functionality.


    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - Append.vi
  WDTWDT AppendAppend WaveformsWaveforms EXTEXT VIVI

     Appends waveform B to the end of waveform A. If the sampling rates do not match,
     the error cluster returns an error. The trigger time of waveform B is ignored. The data
     type of the Y component of waveform A and waveform B determines the polymorphic
      instance to use or you can manually select the instance.


     Inputs/Outputs

            •     waveform A —

         waveform A is the first set of data in the waveform.

            •     waveform B —

         waveform B is the set of data appended to the end of waveform A.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveform out —

         waveform out is the waveform that results from appending waveform B to waveform A.


912   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:912 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:913 ordinal=913 -->
## Functions

Functions

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Append.vi
WDTWDT AppendAppend WaveformsWaveforms CXTCXT VIVI

Appends waveform B to the end of waveform A. If the sampling rates do not match,
the error cluster returns an error. The trigger time of waveform B is ignored. The data
type of the Y component of waveform A and waveform B determines the polymorphic
instance to use or you can manually select the instance.


Inputs/Outputs

   •     waveform A —

    waveform A is the first set of data in the waveform.

   •     waveform B —

    waveform B is the set of data appended to the end of waveform A.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveform out —

    waveform out is the waveform that results from appending waveform B to waveform A.


                                                    © National Instruments 913

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:913 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:914 ordinal=914 -->
## Functions

Functions

            •       error out —

           error out contains error information. This output provides standard error out functionality.


    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - Append.vi

    NumberNumber ofof WaveformWaveform SamplesSamples

     Returns the number of data elements in the waveform. You must manually select the
     polymorphic instance you want to use.


          • WDT Number of Waveform Samples DBL VI
          • WDT Number of Waveform Samples CDB VI
          • WDT Number of Waveform Samples EXT VI
          • WDT Number of Waveform Samples I16 VI
          • WDT Number of Waveform Samples I32 VI
          • WDT Number of Waveform Samples I8 VI
          • WDT Number of Waveform Samples SGL VI
  WDTWDT NumberNumber ofof WaveformWaveform SamplesSamples DBLDBL VIVI

     Returns the number of data elements in the waveform. You must manually select the
     polymorphic instance you want to use.


914   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:914 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:915 ordinal=915 -->
## Functions

Functions

Inputs/Outputs

   •     waveform in —

    waveform in is the waveform for which you want to retrieve the number of data elements.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveform out —

    waveform out returns waveform in unchanged.

   •     number of samples —

   number of samples is the number of data elements in the waveform.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

WDTWDT NumberNumber ofof WaveformWaveform SamplesSamples CDBCDB VIVI

Returns the number of data elements in the waveform. You must manually select the
polymorphic instance you want to use.


Inputs/Outputs

   •     waveform in —

    waveform in is the waveform for which you want to retrieve the number of data elements.

   •       error in (no error) —


                                                    © National Instruments 915

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:915 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:916 ordinal=916 -->
## Functions

Functions


           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveform out —

         waveform out returns waveform in unchanged.

            •     number of samples —

        number of samples is the number of data elements in the waveform.

            •       error out —

           error out contains error information. This output provides standard error out functionality.

  WDTWDT NumberNumber ofof WaveformWaveform SamplesSamples EXTEXT VIVI

     Returns the number of data elements in the waveform. You must manually select the
     polymorphic instance you want to use.


     Inputs/Outputs

            •     waveform in —

         waveform in is the waveform for which you want to retrieve the number of data elements.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveform out —

         waveform out returns waveform in unchanged.

            •     number of samples —

916   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:916 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:917 ordinal=917 -->
## Functions

Functions


   number of samples is the number of data elements in the waveform.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

WDTWDT NumberNumber ofof WaveformWaveform SamplesSamples I16I16 VIVI

Returns the number of data elements in the waveform. You must manually select the
polymorphic instance you want to use.


Inputs/Outputs

   •     waveform in —

    waveform in is the waveform for which you want to retrieve the number of data elements.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveform out —

    waveform out returns waveform in unchanged.

   •     number of samples —

   number of samples is the number of data elements in the waveform.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 917

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:917 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:918 ordinal=918 -->
## Functions

Functions

  WDTWDT NumberNumber ofof WaveformWaveform SamplesSamples I32I32 VIVI

     Returns the number of data elements in the waveform. You must manually select the
     polymorphic instance you want to use.


     Inputs/Outputs

            •     waveform in —

         waveform in is the waveform for which you want to retrieve the number of data elements.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveform out —

         waveform out returns waveform in unchanged.

            •     number of samples —

        number of samples is the number of data elements in the waveform.

            •       error out —

           error out contains error information. This output provides standard error out functionality.

  WDTWDT NumberNumber ofof WaveformWaveform SamplesSamples I8I8 VIVI

     Returns the number of data elements in the waveform. You must manually select the
     polymorphic instance you want to use.


918   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:918 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:919 ordinal=919 -->
## Functions

Functions


Inputs/Outputs

   •     waveform in —

    waveform in is the waveform for which you want to retrieve the number of data elements.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveform out —

    waveform out returns waveform in unchanged.

   •     number of samples —

   number of samples is the number of data elements in the waveform.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

WDTWDT NumberNumber ofof WaveformWaveform SamplesSamples SGLSGL VIVI

Returns the number of data elements in the waveform. You must manually select the
polymorphic instance you want to use.


Inputs/Outputs

   •     waveform in —


                                                    © National Instruments 919

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:919 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:920 ordinal=920 -->
## Functions

Functions


         waveform in is the waveform for which you want to retrieve the number of data elements.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveform out —

         waveform out returns waveform in unchanged.

            •     number of samples —

        number of samples is the number of data elements in the waveform.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


    WaveformWaveform MinMin MaxMax

     Determines the maximum and minimum values and their associate time values for a
     waveform.


     Inputs/Outputs

            •     waveform in —

         waveform in is the waveform for which you want to retrieve the maximum and minimum values.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.


920   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:920 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:921 ordinal=921 -->
## Functions

Functions

   •     max time —

   max time is the time value at which the maximum data value was reached.

   •     waveform out —

    waveform out returns waveform in unchanged.

   •      Y max —

    Y max is the maximum data value of the waveform.

   •      Y min —

    Y min is the minimum data value of the waveform.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •     min time —

   min time is the time value at which the minimum data value was reached.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Min Max.vi

WaveformWaveform ScalarScalar LimitLimit ComparisonComparison

Compares the waveform data values to a scalar value.


Inputs/Outputs

   •      data —

                                                    © National Instruments 921

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:921 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:922 ordinal=922 -->
## Functions

Functions


          data is the waveform that includes the data you want to compare to a specified limit.

            •     compare condition —

         compare condition indicates whether the highest or lowest data value of waveform must be
          lower than and/or equal to or higher than and/or equal to the number in limit.

          0 <—The highest or lowest value in the waveform is less than the limit.
          1 <=—The highest or lowest value in the waveform is less than or equal to the limit.
          2 >—The highest or lowest value in the waveform is greater than the limit.
          3 >= (default)—The highest or lowest value in the waveform is greater than or equal to the limit.

            •       limit —

            limit specifies the number to which you want to compare the highest or lowest data value in the
          waveform.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •      output waveforms —

          output waveforms returns two waveforms in an array.

         The first is a copy of data. The second is the failure waveform, which is a copy of data with all
          elements that passed replaced by NaN. All valid elements are failures.

            •      passed? —

          passed? indicates whether the highest or lowest data value met the compare condition based
         on the limit. FALSE indicates the highest or lowest data value did not meet the comparison.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


     passed? is FALSE if any point in the waveform fails the specified comparison. For
     example, passed? is FALSE if any waveform point is greater than the limit value when
     compare condition is set to <.


922   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:922 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:923 ordinal=923 -->
## Functions

Functions

This VI also returns an array of waveforms where the first waveform is the original data.
The second waveform contains the data with the failed limit comparison values
replaced by NaN.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Scalar Limit
   Comparison.vi

SearchSearch WaveformWaveform

Returns the time value in x for the value specified.


Inputs/Outputs

   •      tolerance (%) —

    tolerance is the percent tolerance on the input value for a match. The default is 0.01.

   •     waveform in —

    waveform in is the waveform you want to search for a particular data value. The default is
    empty.

   •      value —

    value is the data value for which you want to search. The default is 0.

   •       start index —

     start index defines the point in the waveform data where the search begins. The default is 0, the
    beginning of the waveform. The VI returns an error if start index is out of range for the waveform.


                                                    © National Instruments 923

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:923 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:924 ordinal=924 -->
## Functions

Functions

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •       indices of fits —

           indices of fits is an array of indexes of all values that meet the input value and tolerance criteria.

            •     waveform out —

         waveform out returns waveform in unchanged.

            •      index of best fit —

          index of best fit is the index of the data value that best matches the input value.

            •      time of best fit —

          time of best fit is the time value where the data value that best matches the input value was
          found.

            •       error out —

           error out contains error information. This output provides standard error out functionality.

            •      time of fits —

          time of fits is an array of all time values of all values that meet the input value and tolerance
             criteria.


    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - Search.vi

    WaveformWaveform toto XYXY PairsPairs

     Creates an array of data values and their corresponding time stamps. Wire the data
     type of the Y component to the waveform in input to determine the polymorphic
      instance to use or manually select the instance.

924   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:924 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:925 ordinal=925 -->
## Functions

Functions


  • WDT Waveform to XY Pairs DBL VI
  • WDT Waveform to XY Pairs SGL VI
  • WDT Waveform to XY Pairs I64 VI
  • WDT Waveform to XY Pairs I32 VI
  • WDT Waveform to XY Pairs I16 VI
  • WDT Waveform to XY Pairs I8 VI
  • WDT Waveform to XY Pairs U64 VI
  • WDT Waveform to XY Pairs U32 VI
  • WDT Waveform to XY Pairs U16 VI
  • WDT Waveform to XY Pairs U8 VI
  • WDT Waveform to XY Pairs CDB VI
  • WDT Waveform to XY Pairs CSG VI
  • WDT Waveform to XY Pairs EXT VI
  • WDT Waveform to XY Pairs CXT VI

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - XY Pairs.vi
WDTWDT WaveformWaveform toto XYXY PairsPairs DBLDBL VIVI

Creates an array of data values and their corresponding time stamps. Wire the data
type of the Y component to the waveform in input to determine the polymorphic
instance to use or manually select the instance.


Inputs/Outputs

   •     waveform in —

                                                    © National Instruments 925

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:925 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:926 ordinal=926 -->
## Functions

Functions


         waveform in is the waveform for which you want to retrieve data values and corresponding time
          stamps.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveform out —

         waveform out returns waveform in unchanged.

            •      XY pairs —

         XY pairs is the data values of the waveforms and their corresponding time stamps.

                   •      x —

              x is the time stamp of y.

                   •      y —

             y is the data value.


            •       error out —

           error out contains error information. This output provides standard error out functionality.


    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - XY Pairs.vi
  WDTWDT WaveformWaveform toto XYXY PairsPairs SGLSGL VIVI

     Creates an array of data values and their corresponding time stamps. Wire the data
     type of the Y component to the waveform in input to determine the polymorphic
      instance to use or manually select the instance.

926   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:926 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:927 ordinal=927 -->
## Functions

Functions


Inputs/Outputs

   •     waveform in —

    waveform in is the waveform for which you want to retrieve data values and corresponding time
    stamps.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveform out —

    waveform out returns waveform in unchanged.

   •      XY pairs —

    XY pairs is the data values of the waveforms and their corresponding time stamps.

         •      x —

        x is the time stamp of y.

         •      y —

        y is the data value.


   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - XY Pairs.vi

                                                    © National Instruments 927

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:927 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:928 ordinal=928 -->
## Functions

Functions

  WDTWDT WaveformWaveform toto XYXY PairsPairs I64I64 VIVI

     Creates an array of data values and their corresponding time stamps. Wire the data
     type of the Y component to the waveform in input to determine the polymorphic
      instance to use or manually select the instance.


     Inputs/Outputs

            •     waveform in —

         waveform in is the waveform for which you want to retrieve data values and corresponding time
          stamps.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveform out —

         waveform out returns waveform in unchanged.

            •      XY pairs —

         XY pairs is the data values of the waveforms and their corresponding time stamps.

                   •      x —

              x is the time stamp of y.

                   •      y —

             y is the data value.


            •       error out —


928   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:928 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:929 ordinal=929 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - XY Pairs.vi
WDTWDT WaveformWaveform toto XYXY PairsPairs I32I32 VIVI

Creates an array of data values and their corresponding time stamps. Wire the data
type of the Y component to the waveform in input to determine the polymorphic
instance to use or manually select the instance.


Inputs/Outputs

   •     waveform in —

    waveform in is the waveform for which you want to retrieve data values and corresponding time
    stamps.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveform out —

    waveform out returns waveform in unchanged.

   •      XY pairs —

    XY pairs is the data values of the waveforms and their corresponding time stamps.


                                                    © National Instruments 929

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:929 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:930 ordinal=930 -->
## Functions

Functions


                   •      x —

              x is the time stamp of y.

                   •      y —

             y is the data value.


            •       error out —

           error out contains error information. This output provides standard error out functionality.


    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - XY Pairs.vi
  WDTWDT WaveformWaveform toto XYXY PairsPairs I16I16 VIVI

     Creates an array of data values and their corresponding time stamps. Wire the data
     type of the Y component to the waveform in input to determine the polymorphic
      instance to use or manually select the instance.


     Inputs/Outputs

            •     waveform in —

         waveform in is the waveform for which you want to retrieve data values and corresponding time
          stamps.

            •       error in (no error) —


930   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:930 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:931 ordinal=931 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveform out —

    waveform out returns waveform in unchanged.

   •      XY pairs —

    XY pairs is the data values of the waveforms and their corresponding time stamps.

         •      x —

        x is the time stamp of y.

         •      y —

        y is the data value.


   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - XY Pairs.vi
WDTWDT WaveformWaveform toto XYXY PairsPairs I8I8 VIVI

Creates an array of data values and their corresponding time stamps. Wire the data
type of the Y component to the waveform in input to determine the polymorphic
instance to use or manually select the instance.


                                                    © National Instruments 931

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:931 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:932 ordinal=932 -->
## Functions

Functions


     Inputs/Outputs

            •     waveform in —

         waveform in is the waveform for which you want to retrieve data values and corresponding time
          stamps.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveform out —

         waveform out returns waveform in unchanged.

            •      XY pairs —

         XY pairs is the data values of the waveforms and their corresponding time stamps.

                   •      x —

              x is the time stamp of y.

                   •      y —

             y is the data value.


            •       error out —

           error out contains error information. This output provides standard error out functionality.


    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - XY Pairs.vi


932   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:932 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:933 ordinal=933 -->
## Functions

Functions

WDTWDT WaveformWaveform toto XYXY PairsPairs U64U64 VIVI

Creates an array of data values and their corresponding time stamps. Wire the data
type of the Y component to the waveform in input to determine the polymorphic
instance to use or manually select the instance.


Inputs/Outputs

   •     waveform in —

    waveform in is the waveform for which you want to retrieve data values and corresponding time
    stamps.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveform out —

    waveform out returns waveform in unchanged.

   •      XY pairs —

    XY pairs is the data values of the waveforms and their corresponding time stamps.

         •      x —

        x is the time stamp of y.

         •      y —

        y is the data value.


   •       error out —


                                                    © National Instruments 933

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:933 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:934 ordinal=934 -->
## Functions

Functions


           error out contains error information. This output provides standard error out functionality.


    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - XY Pairs.vi
  WDTWDT WaveformWaveform toto XYXY PairsPairs U32U32 VIVI

     Creates an array of data values and their corresponding time stamps. Wire the data
     type of the Y component to the waveform in input to determine the polymorphic
      instance to use or manually select the instance.


     Inputs/Outputs

            •     waveform in —

         waveform in is the waveform for which you want to retrieve data values and corresponding time
          stamps.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveform out —

         waveform out returns waveform in unchanged.

            •      XY pairs —

         XY pairs is the data values of the waveforms and their corresponding time stamps.


934   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:934 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:935 ordinal=935 -->
## Functions

Functions


         •      x —

        x is the time stamp of y.

         •      y —

        y is the data value.


   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - XY Pairs.vi
WDTWDT WaveformWaveform toto XYXY PairsPairs U16U16 VIVI

Creates an array of data values and their corresponding time stamps. Wire the data
type of the Y component to the waveform in input to determine the polymorphic
instance to use or manually select the instance.


Inputs/Outputs

   •     waveform in —

    waveform in is the waveform for which you want to retrieve data values and corresponding time
    stamps.

   •       error in (no error) —


                                                    © National Instruments 935

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:935 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:936 ordinal=936 -->
## Functions

Functions


           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveform out —

         waveform out returns waveform in unchanged.

            •      XY pairs —

         XY pairs is the data values of the waveforms and their corresponding time stamps.

                   •      x —

              x is the time stamp of y.

                   •      y —

             y is the data value.


            •       error out —

           error out contains error information. This output provides standard error out functionality.


    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - XY Pairs.vi
  WDTWDT WaveformWaveform toto XYXY PairsPairs U8U8 VIVI

     Creates an array of data values and their corresponding time stamps. Wire the data
     type of the Y component to the waveform in input to determine the polymorphic
      instance to use or manually select the instance.


936   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:936 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:937 ordinal=937 -->
## Functions

Functions


Inputs/Outputs

   •     waveform in —

    waveform in is the waveform for which you want to retrieve data values and corresponding time
    stamps.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveform out —

    waveform out returns waveform in unchanged.

   •      XY pairs —

    XY pairs is the data values of the waveforms and their corresponding time stamps.

         •      x —

        x is the time stamp of y.

         •      y —

        y is the data value.


   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - XY Pairs.vi


                                                    © National Instruments 937

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:937 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:938 ordinal=938 -->
## Functions

Functions

  WDTWDT WaveformWaveform toto XYXY PairsPairs CDBCDB VIVI

     Creates an array of data values and their corresponding time stamps. Wire the data
     type of the Y component to the waveform in input to determine the polymorphic
      instance to use or manually select the instance.


     Inputs/Outputs

            •     waveform in —

         waveform in is the waveform for which you want to retrieve data values and corresponding time
          stamps.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveform out —

         waveform out returns waveform in unchanged.

            •      XY pairs —

         XY pairs is the data values of the waveforms and their corresponding time stamps.

                   •      x —

              x is the time stamp of y.

                   •      y —

             y is the data value.


            •       error out —


938   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:938 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:939 ordinal=939 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - XY Pairs.vi
WDTWDT WaveformWaveform toto XYXY PairsPairs CSGCSG VIVI

Creates an array of data values and their corresponding time stamps. Wire the data
type of the Y component to the waveform in input to determine the polymorphic
instance to use or manually select the instance.


Inputs/Outputs

   •     waveform in —

    waveform in is the waveform for which you want to retrieve data values and corresponding time
    stamps.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveform out —

    waveform out returns waveform in unchanged.

   •      XY pairs —

    XY pairs is the data values of the waveforms and their corresponding time stamps.


                                                    © National Instruments 939

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:939 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:940 ordinal=940 -->
## Functions

Functions


                   •      x —

              x is the time stamp of y.

                   •      y —

             y is the data value.


            •       error out —

           error out contains error information. This output provides standard error out functionality.


    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - XY Pairs.vi
  WDTWDT WaveformWaveform toto XYXY PairsPairs EXTEXT VIVI

     Creates an array of data values and their corresponding time stamps. Wire the data
     type of the Y component to the waveform in input to determine the polymorphic
      instance to use or manually select the instance.


     Inputs/Outputs

            •     waveform in —

         waveform in is the waveform for which you want to retrieve data values and corresponding time
          stamps.

            •       error in (no error) —


940   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:940 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:941 ordinal=941 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     waveform out —

    waveform out returns waveform in unchanged.

   •      XY pairs —

    XY pairs is the data values of the waveforms and their corresponding time stamps.

         •      x —

        x is the time stamp of y.

         •      y —

        y is the data value.


   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - XY Pairs.vi
WDTWDT WaveformWaveform toto XYXY PairsPairs CXTCXT VIVI

Creates an array of data values and their corresponding time stamps. Wire the data
type of the Y component to the waveform in input to determine the polymorphic
instance to use or manually select the instance.


                                                    © National Instruments 941

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:941 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:942 ordinal=942 -->
## Functions

Functions


     Inputs/Outputs

            •     waveform in —

         waveform in is the waveform for which you want to retrieve data values and corresponding time
          stamps.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •     waveform out —

         waveform out returns waveform in unchanged.

            •      XY pairs —

         XY pairs is the data values of the waveforms and their corresponding time stamps.

                   •      x —

              x is the time stamp of y.

                   •      y —

             y is the data value.


            •       error out —

           error out contains error information. This output provides standard error out functionality.


    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Waveform\Waveform - XY Pairs.vi


942   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:942 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:943 ordinal=943 -->
## Functions

Functions

WaveformWaveform ConstantConstant

Use the waveform constant to hold acquired data for analysis and display.

The waveform constant consists of components that include a start time, a delta t, the
waveform data, and attributes. Use the Analog Waveform VIs and functions to access
and manipulate individual components of a waveform.

The start time (t0) is a time stamp associated with the first measurement point in the
waveform. Use the start time to synchronize plots on a multi-plot waveform graph or
digital waveform graph and to determine delays between waveforms. Delta t (dt) is the
time interval in seconds between any two points in the signal. The waveform data is
the value that represents the waveform. An array of any numeric data type other than
the fixed-point numeric data type can represent analog waveform data. Generally, the
number of data values in the array corresponds directly to the number of scans from a
DAQ device. Attributes include information about the signal, such as the name of the
signal and the device acquiring the signal. NI-DAQ automatically sets some attributes
for you. Use the Set Waveform Attribute function to set attributes, and use the Get
Waveform Attribute function to read attributes.

Use the Get Waveform Components function to extract and manipulate the
components of a waveform you generate. The Negate function negates waveform data
and plots the results to a graph.

To represent waveform data in the front panel window, use the waveform control or
the waveform graph.


WaveformWaveform GenerationGeneration

Use the Waveform Generation VIs to generate different types of single and multi-tone
signals, function generator signals, and noise signals.

The VIs on this palette can return waveform error codes.


                                                    © National Instruments 943

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:943 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:944 ordinal=944 -->
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


       Sine                     Generates a waveform containing a sine wave.      Waveform

      Square                     Generates a waveform containing a square wave.
      Waveform

        Triangle
                     Generates a waveform containing a triangle wave.      Waveform

      Sawtooth                     Generates a waveform containing a sawtooth wave.      Waveform

       Basic                     Generates a waveform that is the sum of integer cycle sine tones.
       Multitone

       Basic
       Multitone with Generates a waveform that is the sum of integer cycle sine tones.
       Amplitudes

       Multitone
                     Generates a waveform that is the sum of integer cycle sine tones.
       Generator

      Uniform White                     Generates a uniformly distributed pseudorandom pattern whose values are in the
       Noise                     range [–a:a], where ais the absolute value of amplitude.      Waveform


944   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:944 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:945 ordinal=945 -->
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


                                                    © National Instruments 945

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:945 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:946 ordinal=946 -->
## Functions

Functions


       Palette Object  Description

       Simulate
        Arbitrary       Simulates a signal that you define.
       Signal

   BasicBasic FunctionFunction GeneratorGenerator

     Creates an output waveform based on signal type.


     Inputs/Outputs

            •       offset —

            offset is the DC offset of the signal. The default is 0.0.

            •       reset signal —

           reset signal, if TRUE, resets the phase to the phase control value and the time stamp to zero. The
           default is FALSE.

            •       signal type —

           signal type is the type of waveform to generate.

                 Sine Wave
          0
                    (default)
          1      Triangle Wave
          2     Square Wave
          3     Sawtooth Wave

            •      frequency —

946   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:946 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:947 ordinal=947 -->
## Functions

Functions


  frequency is the frequency of the waveform in units of hertz. The default is 10.

•      amplitude —

  amplitude is the amplitude of the waveform. The amplitude is also the peak voltage. The default
   is 1.0.

•      phase —

  phase is the initial phase, in degrees, of the waveform. The default is 0. The VI ignores phase if
  reset signal is FALSE.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      sampling info —

  sampling info contains sampling information.

      •      Fs —

      Fs is the sampling rate in samples per second. The default is 1000.

      •      #s —

      #s is the number of samples in the waveform. The default is 1000.


•      square wave duty cycle (%) —

  square wave duty cycle is the percentage of time a square wave remains high versus low over
  one period. The VI uses this parameter only if the signal type is a square wave. The default is 50.

•       signal out —

  signal out is the generated waveform.

•      phase out —

  phase out is the phase of the waveform in degrees.

•       error out —


                                                   © National Instruments 947

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:947 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:948 ordinal=948 -->
## Functions

Functions


           error out contains error information. This output provides standard error out functionality.


      This VI remembers the time stamp of the previous waveform generated and continues
      to increment the time stamp from that point. It takes as inputs the type of waveform,
    number of samples, phase in, and the frequency of the waveform to be generated in
      Hz.
   TonesTones andand NoiseNoise WaveformWaveform

     Generates a waveform composed of a sum of sine tones, noise, and DC offset.


     Inputs/Outputs

            •       reset signal —

           reset signal, if TRUE, resets the phase of each tone to the phase value from the tones array, the
          seed to the seed control value, and the time stamp to zero. The default is FALSE.

            •      tones —

          tones contains the parameters for each sine tone.

                   •      frequency —

              frequency specifies the frequency of the sine tone in hertz.

                   •      amplitude —

             amplitude specifies the amplitude of the sine tone.

                   •      phase —


948   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:948 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:949 ordinal=949 -->
## Functions

Functions


      phase specifies the initial phase of the sine tone in degrees. The default is 0.


•      noise (rms) —

  noise specifies the rms level of the additive Gaussian noise. The default is 0.0.

•       offset —

  offset is the DC offset of the signal. The default is 0.0.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. With the following
  exception, this input provides standard error in functionality.

  This node runs normally evenifan error occurred before this node runs.

•      sampling info —

  sampling info contains sampling information.

      •      Fs —

      Fs is the sampling rate in samples per second. The default is 1000.

      •      #s —

      #s is the number of samples in the waveform. The default is 1000.


•      seed —

  seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

  LabVIEW maintains the internal seed state independently for each instance of this reentrant VI.
  For a specific instance of this VI, if seed is less than or equal to 0, LabVIEW does not reseed the
  noise generator, and the noise generator resumes producing noise samples as a continuation of
  the previous noise sequence.

•       signal out —


                                                   © National Instruments 949

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:949 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:950 ordinal=950 -->
## Functions

Functions


           signal out is the generated waveform.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Mathematics\Interpolation\1D Fourier
       Interpolation.vi
   FormulaFormula WaveformWaveform

     Creates an output waveform using a formula string to specify the time function to be
     used.


     Inputs/Outputs

            •       offset —

            offset is the DC offset of the signal. The default is 0.0.

            •       reset signal —

           reset signal, if TRUE, resets the time stamp to zero. The default is FALSE.

            •      frequency —

          frequency is the frequency of the waveform in units of hertz. The default is 100.


950   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:950 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:951 ordinal=951 -->
## Functions

Functions

•      amplitude —

  amplitude is the amplitude of the waveform. The amplitude is also the peak voltage. The default
   is 1.0.

•      formula —

  formula is the representation used to generate the signal out waveform. The default is
  sin(w*t)*sin(2*pi(1)*10).

  The following table lists the defined variable names.

   f   Frequency equal to the frequency input
 a  Amplitude equal to the amplitude input
 w  2*pi*f
 n  Number of samples generated so far
 t  Number of elapsed seconds
  fs Sampling frequency equal to sampling info→>Fs

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      sampling info —

  sampling info contains sampling information.

      •      Fs —

      Fs is the sampling rate in samples per second. The default is 1000.

      •      #s —

      #s is the number of samples in the waveform. The default is 1000.


•       signal out —

  signal out is the generated waveform.

•       error out —


                                                   © National Instruments 951

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:951 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:952 ordinal=952 -->
## Functions

Functions


           error out contains error information. This output provides standard error out functionality.


     Related Information

     Formula Node and Expression Node Functions

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Signal Processing\Waveform Measurements\
       Waveform Generation Using Formula.vi
   SineSine WaveformWaveform

     Generates a waveform containing a sine wave.


     Inputs/Outputs

            •       offset —

            offset is the DC offset of the signal. The default is 0.0.

            •       reset signal —

           reset signal, if TRUE, resets the phase to the phase control value and the time stamp to zero. The
           default is FALSE.

            •      frequency —


952   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:952 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:953 ordinal=953 -->
## Functions

Functions


    frequency is the frequency of the waveform in units of hertz. The default is 10.

   •      amplitude —

    amplitude is the amplitude of the waveform. The amplitude is also the peak voltage. The default
      is 1.0.

   •      phase —

    phase is the initial phase, in degrees, of the waveform. The default is 0. The VI ignores phase if
    reset signal is FALSE.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      sampling info —

    sampling info contains sampling information.

         •      Fs —

        Fs is the sampling rate in samples per second. The default is 1000.

         •      #s —

        #s is the number of samples in the waveform. The default is 1000.


   •       signal out —

    signal out is the generated waveform.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


If sine wave is represented by the sequence Y, the VI generates the pattern according to
the following equation.

y[i] = amp × sin(phase[i]), for i = 0, 1, 2, …, n– 1,

                                                    © National Instruments 953

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:953 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:954 ordinal=954 -->
## Functions

Functions

     where amp = amplitude, n= number of samples (#s), and phase[i] is:

      initial_phase + frequency × 360.0 × i/Fs

      This VI initializes the phase on the first run. After the first run, if reset signal is TRUE,
     phase sets the initial phase of the input signal. If reset signal is FALSE, the VI ignores
     phase.

      This VI is reentrant so that it can be used to simulate a continuous acquisition from a
      sine wave function generator. If the input control reset signal is FALSE, subsequent
      calls to this VI produce the output sine wave waveform containing the next nsamples
      of a sine wave. This VI remembers the phase and time stamp of the current waveform
     and uses this to continuously generate and time stamp the subsequent waveforms, as
     long as the reset signal input is FALSE.

    Examples

      Refer to the following example files included with LabVIEW.

          • labview\examples\Signal Processing\Waveform Measurements\
       Noise Waveforms and PS Density.vi
   SquareSquare WaveformWaveform

     Generates a waveform containing a square wave.


     Inputs/Outputs

            •       offset —


954   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:954 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:955 ordinal=955 -->
## Functions

Functions


  offset is the DC offset of the signal. The default is 0.0.

•       reset signal —

  reset signal, if TRUE, resets the phase to the phase control value and the time stamp to zero. The
  default is FALSE.

•      frequency —

  frequency is the frequency of the waveform in units of hertz. The default is 10.

•      amplitude —

  amplitude is the amplitude of the waveform. The amplitude is also the peak voltage. The default
   is 1.0.

•      phase —

  phase is the initial phase, in degrees, of the waveform. The default is 0. The VI ignores phase if
  reset signal is FALSE.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      sampling info —

  sampling info contains sampling information.

      •      Fs —

      Fs is the sampling rate in samples per second. The default is 1000.

      •      #s —

      #s is the number of samples in the waveform. The default is 1000.


•      duty cycle (%) —

  duty cycle is the percentage of time a square wave remains high versus low over one period. The
  default is 50.


                                                   © National Instruments 955

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:955 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:956 ordinal=956 -->
## Functions

Functions

            •       signal out —

           signal out is the generated waveform.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


         If square wave is represented by the sequence Y, the VI generates the pattern according
      to the following equation.

       y[i] = amp × square(phase[i]), for i = 0, 1, 2, …, n– 1,

     where amp = amplitude, n= number of samples (#s), and square[p] is:

      1.0 if 0 ≤ pmod < (0.01 × duty) × 360.0

     or

      –1.0 if (0.01 × duty) × 360.0 ≤ pmod < 360.0

     where pmod = p modulo 360.0, duty = duty cycle in percent, and phase[i] is:

      initial_phase + frequency × 360.0 × i/Fs

     where initial_phase = phase if reset signal is TRUE, or last output phase if reset signal
       is FALSE.

      This VI is reentrant so that it can be used to simulate a continuous acquisition from a
     square wave function generator. If the input control reset signal is FALSE, subsequent
      calls to this VI produce the output Square Wave waveform containing the next n
     samples of a square wave. This VI remembers the phase and time stamp of the current
     waveform and uses this to continuously generate and time stamp the subsequent
     waveforms, as long as the reset signal input is FALSE.


956   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:956 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:957 ordinal=957 -->
## Functions

Functions

TriangleTriangle WaveformWaveform

Generates a waveform containing a triangle wave.


Inputs/Outputs

   •       offset —

     offset is the DC offset of the signal. The default is 0.0.

   •       reset signal —

    reset signal, if TRUE, resets the phase to the phase control value and the time stamp to zero. The
     default is FALSE.

   •      frequency —

    frequency is the frequency of the waveform in units of hertz. The default is 10.

   •      amplitude —

    amplitude is the amplitude of the waveform. The amplitude is also the peak voltage. The default
      is 1.0.

   •      phase —

    phase is the initial phase, in degrees, of the waveform. The default is 0. The VI ignores phase if
    reset signal is FALSE.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      sampling info —


                                                    © National Instruments 957

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:957 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:958 ordinal=958 -->
## Functions

Functions


          sampling info contains sampling information.

                   •      Fs —

               Fs is the sampling rate in samples per second. The default is 1000.

                   •      #s —

              #s is the number of samples in the waveform. The default is 1000.


            •       signal out —

           signal out is the generated waveform.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


         If triangle wave is represented by the sequence Y, the VI generates the pattern
     according to the following equation.

       y[i] = amp × tri(phase[i]), for i = 0, 1, 2, …, n– 1,

     where amp = amplitude, n= number of samples (#s), and tri[p] is:

      (2 × pmod/180.0) if 0 ≤ pmod < 90.0

     or

      (2 × (1 – pmod/180.0)) if 90.0 ≤ pmod < 270.0

     or

      (2 × (pmod/180.0 – 2.0)) if 270.0 ≤ pmod < 360.0

     where pmod = p modulo 360.0 and phase[i] is:

      initial_phase + frequency × 360.0 × i/Fs


958   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:958 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:959 ordinal=959 -->
## Functions

Functions

where initial_phase = phase if reset signal is TRUE, or last output phase if reset signal
is FALSE.

This VI is reentrant so that it can be used to simulate a continuous acquisition from a
triangle wave function generator. If the input control reset signal is FALSE, subsequent
calls to this VI produce the output triangle wave waveform containing the next n
samples of a triangle wave. This VI remembers the phase and time stamp of the
current waveform and uses this to continuously generate and time stamp the
subsequent waveforms, as long as the reset signal input is FALSE.
SawtoothSawtooth WaveformWaveform

Generates a waveform containing a sawtooth wave.


Inputs/Outputs

   •       offset —

     offset is the DC offset of the signal. The default is 0.0.

   •       reset signal —

    reset signal, if TRUE, resets the phase to the phase control value and the time stamp to zero. The
     default is FALSE.

   •      frequency —

    frequency is the frequency of the waveform in units of hertz. The default is 10.

   •      amplitude —

    amplitude is the amplitude of the waveform. The amplitude is also the peak voltage. The default


                                                    © National Instruments 959

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:959 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:960 ordinal=960 -->
## Functions

Functions


              is 1.0.

            •      phase —

         phase is the initial phase, in degrees, of the waveform. The default is 0. The VI ignores phase if
           reset signal is FALSE.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •      sampling info —

          sampling info contains sampling information.

                   •      Fs —

               Fs is the sampling rate in samples per second. The default is 1000.

                   •      #s —

              #s is the number of samples in the waveform. The default is 1000.


            •       signal out —

           signal out is the generated waveform.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


         If Sawtooth Wave is represented by the sequence Y, the VI generates the pattern
     according to the following equation.

       y[i] = amp × sawtooth(phase[i]), for i = 0, 1, 2, …, n– 1,

     where amp = amplitude, n= number of samples (#s), and sawtooth (phase[i]) is:

     (pmod/180.0) if 0 ≤ pmod < 180.0

960   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:960 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:961 ordinal=961 -->
## Functions

Functions

or

(pmod/180.0 - 2.0) if 180.0 ≤ pmod < 360.0

where pmod = p modulo 360.0 and phase[i] is:

initial_phase + frequency × 360.0 × i/Fs

where initial_phase = phase if reset signal is TRUE, or last output phase if reset signal
is FALSE.

This VI is reentrant so that it can be used to simulate a continuous acquisition from a
sawtooth wave function generator. If the input control reset signal is FALSE,
subsequent calls to this VI produce the output Sawtooth Wave waveform containing
the next nsamples of a sawtooth wave. This VI remembers the phase and time stamp
of the current waveform and uses this to continuously generate and time stamp the
subsequent waveforms, as long as the reset signal input is FALSE.
BasicBasic MultitoneMultitone

Generates a waveform that is the sum of integer cycle sine tones.


Inputs/Outputs

   •      amplitude —

    amplitude is the value that the sum of all the tones is scaled to and is the largest absolute value
    that the waveform contains. The default is –1.


                                                    © National Instruments 961

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:961 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:962 ordinal=962 -->
## Functions

Functions


          amplitude is useful when outputting the waveform to an analog output channel. If the
        maximum value that the hardware can output is 5 volts, set amplitude to 5. If amplitude ≤ 0, the
           scaling is not applied.

            •       reset signal —

           reset signal, if TRUE, resets the phase to the phase control value and the time stamp to zero. The
           default is FALSE.

            •      #tones —

          #tones is the number of tones present in the output waveform.

            •       start frequency —

            start frequency is the lowest tone frequency generated. This value must be an integer multiple
           of Fs/#s. The default is 10.

            •      seed —

           seed, when > 0, causes reseeding of the noise sample generator.

         seed is ignored if phase relationship is set to Linear.

            •       delta frequency —

           delta frequency is the magnitude of the spacing between adjacent tone frequencies. delta
          frequency must be an integer multiple of Fs/#s.

                 If start frequency is 100 Hz, delta frequency is ten, and #tones is three, the tone frequencies
          generated are 100 Hz, 110 Hz, and 120 Hz.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •      sampling info —

          sampling info contains sampling information.

                   •      Fs —


962   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:962 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:963 ordinal=963 -->
## Functions

Functions


        Fs is the sampling rate in samples per second. The default is 1000.

         •      #s —

        #s is the number of samples in the waveform. The default is 1000.


   •      coerce frequencies? —

       If coerce frequencies? is TRUE, the specified tone frequencies will be coerced to the nearest
    multiple of Fs/n.

   •      phase relationship —

    phase relationship is the distribution of the phases of the sine tones. The phase distribution
     affects the Peak/RMS ratio of the overall waveform.

    0 random—Each phase is chosen randomly between 0 and 360 degrees.
      linear difference—The phase difference between adjacent frequency tones varies linearly from
    1 0 to 360 degrees. This gives the best Peak/RMS ratio but might cause the signal to have
      periodic components within the period of the overall waveform.
    2 linear phase—The phase varies linearly from 0 to 360 degrees.

   •       signal out —

    signal out is the generated waveform.

   •       crest factor —

     crest factor is the ratio of the Peak voltage to the RMS voltage of signal out.

   •      actual tone frequencies —

    actual tone frequencies are the tone frequencies generated after accounting for coercion, if
    coerce frequencies? is TRUE, and the Nyquist criteria.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


The frequency domain representation of this waveform is a sequence of impulses at

                                                    © National Instruments 963

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:963 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:964 ordinal=964 -->
## Functions

Functions

     the specified tone frequencies and zero at all other frequencies. The sine tones are
     generated using the frequency and samples information. The phases of the tones are
    random and the amplitude of each tone is equal. This raw array then is scaled so that
     the largest absolute value is equal to amplitude. Finally, the waveform is bundled. The
     X0 element of the waveform is always set equal to 0 and the delta X element is set
     equal to 1/Fs.
   BasicBasic MultitoneMultitone withwith AmplitudesAmplitudes

     Generates a waveform that is the sum of integer cycle sine tones.


     Inputs/Outputs

            •      amplitude —

          amplitude is the value that the sum of all the tones is scaled to and is the largest absolute value
           that the waveform contains. The default is –1.

          amplitude is useful when outputting the waveform to an analog output channel. If the
        maximum value that the hardware can output is 5 volts, set amplitude to 5. If amplitude ≤ 0, the
           scaling is not applied.

            •       reset signal —

           reset signal, if TRUE, resets the phase to the phase control value and the time stamp to zero. The
           default is FALSE.

            •       start frequency —

            start frequency is the lowest tone frequency generated. This value must be an integer multiple


964   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:964 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:965 ordinal=965 -->
## Functions

Functions


  of Fs/#s. The default is 10.

•      tone amplitudes —

  tone amplitudes is an array in which each element is a single tone amplitude. The size of this
  array determines how many tones are generated.

•      seed —

  seed, when > 0, causes reseeding of the noise sample generator.

  seed is ignored if phase relationship is set to Linear.

•       delta frequency —

  delta frequency is the magnitude of the spacing between adjacent tone frequencies. delta
  frequency must be an integer multiple of Fs/#s. The default is 100.

   If start frequency is 100 Hz, delta frequency is ten, and the tone amplitudes array contains
  three elements, the tone frequencies generated are 100 Hz, 110 Hz, and 120 Hz.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      sampling info —

  sampling info contains sampling information.

      •      Fs —

      Fs is the sampling rate in samples per second. The default is 1000.

      •      #s —

      #s is the number of samples in the waveform. The default is 1000.


•      coerce frequencies? —

   If coerce frequencies? is TRUE, the specified tone frequencies will be coerced to the nearest
  multiple of Fs/n.


                                                   © National Instruments 965

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:965 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:966 ordinal=966 -->
## Functions

Functions

            •      phase relationship —

         phase relationship is the distribution of the phases of the sine tones. The phase distribution
            affects the Peak/RMS ratio of the overall waveform.

          0 random—Each phase is chosen randomly between 0 and 360 degrees.
             linear difference—The phase difference between adjacent frequency tones varies linearly from
          1 0 to 360 degrees. This gives the best Peak/RMS ratio but might cause the signal to have
            periodic components within the period of the overall waveform.
          2 linear phase—The phase varies linearly from 0 to 360 degrees.

            •       signal out —

           signal out is the generated waveform.

            •       crest factor —

           crest factor is the ratio of the Peak voltage to the RMS voltage of signal out.

            •      actual tone frequencies —

           actual tone frequencies are the tone frequencies generated after accounting for coercion, if
          coerce frequencies? is TRUE, and the Nyquist criteria.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


     The frequency domain representation of this waveform is a sequence of impulses at
     the specified tone frequencies and zero at all other frequencies. The number of tones
       is determined by the size of the tone amplitudes array. The sine tones are generated
     using the frequency, amplitude, and samples information. The phases of the tones are
     determined using the relationship specified in phase relationship. This raw array then
       is scaled so that the largest absolute value is equal to amplitude. Finally, the waveform
       is bundled. The X0 element of the waveform is always set equal to 0 and the delta X
     element is set equal to 1/Fs.

    Examples

      Refer to the following example files included with LabVIEW.


966   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:966 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:967 ordinal=967 -->
## Functions

Functions

  • labview\examples\Signal Processing\Waveform Measurements\
   Multitone with Amplitudes.vi
MultitoneMultitone GeneratorGenerator

Generates a waveform that is the sum of integer cycle sine tones.


Inputs/Outputs

   •      amplitude —

    amplitude is the value that the sum of all the tones is scaled to and is the largest absolute value
    that the waveform contains. The default is –1.

    amplitude is useful when outputting the waveform to an analog output channel. If the
   maximum value that the hardware can output is 5 volts, set amplitude to 5. If amplitude ≤ 0, the
     scaling is not applied.

   •       reset signal —

    reset signal, if TRUE, resets the phase to the phase control value and the time stamp to zero. The
     default is FALSE.

   •      tone frequencies —

    tone frequencies is an array in which each element is a single tone frequency. The size of this
    array must match the size of the tone amplitudes array and the size of the tone phases array.

   •      tone amplitudes —

    tone amplitudes is an array in which each element is a single tone amplitude. The size of this
    array must match the size of the tone frequencies array and the size of the tone phases array.

   •      tone phases —

                                                    © National Instruments 967

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:967 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:968 ordinal=968 -->
## Functions

Functions


          tone phases is an array in which each element is a single tone phase in degrees. The size of this
           array must match the size of the tone frequencies array and the size of the tone amplitude
            array.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •      sampling info —

          sampling info contains sampling information.

                   •      Fs —

               Fs is the sampling rate in samples per second. The default is 1000.

                   •      #s —

              #s is the number of samples in the waveform. The default is 1000.


            •      coerce frequencies? —

                 If coerce frequencies? is TRUE, the specified tone frequencies will be coerced to the nearest
           multiple of Fs/n.

            •       signal out —

           signal out is the generated waveform.

            •       crest factor —

           crest factor is the ratio of the Peak voltage to the RMS voltage of signal out.

            •      actual tone frequencies —

           actual tone frequencies are the tone frequencies generated after accounting for coercion, if
          coerce frequencies? is TRUE, and the Nyquist criteria.

            •       error out —

           error out contains error information. This output provides standard error out functionality.


968   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:968 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:969 ordinal=969 -->
## Functions

Functions

The frequency domain representation of this waveform is a sequence of impulses at
the specified tone frequencies and zero at all other frequencies. The number of tones
is determined by the size of the array inputs tone frequencies, tone amplitudes, and
tone phases. The sine tones are generated using the frequency, phase, amplitude, and
samples information. This raw array then is scaled so the largest absolute value is
equal to amplitude. Finally, the waveform is bundled. The X0 element of the waveform
always is set equal to 0 and the delta X element is set equal to 1/Fs.

LabVIEW assumes tone phases to be referenced to the sine function. To reference tone
phases to the cosine function, add 90 degrees. Be aware that this may change the crest
factor. The following code excerpt shows how to reference tone phases to the cosine
function:


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Measurements\
   Bandlimited Signal Generation.vi
  • labview\examples\Signal Processing\Waveform Measurements\
   Multitone with Amplitudes and Phases.vi
UniformUniform WhiteWhite NoiseNoise WaveformWaveform

Generates a uniformly distributed pseudorandom pattern whose values are in the
range [–a:a], where ais the absolute value of amplitude.


                                                    © National Instruments 969

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:969 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:970 ordinal=970 -->
## Functions

Functions

     Inputs/Outputs

            •       reset signal —

           reset signal, if TRUE, resets the seed to the seed control value and the time stamp to zero. The
           default is FALSE.

            •      amplitude —

          amplitude is the maximum absolute value that signal out can have. The default is 1.0.

            •      seed —

           seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

         LabVIEW maintains the internal seed state independently for each instance of this reentrant VI.
          For a specific instance of this VI, if seed is less than or equal to 0, LabVIEW does not reseed the
           noise generator, and the noise generator resumes producing noise samples as a continuation of
          the previous noise sequence.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. This input provides
          standard error in functionality.

            •      sampling info —

          sampling info contains sampling information.

                   •      Fs —

               Fs is the sampling rate in samples per second. The default is 1000.

                   •      #s —

              #s is the number of samples in the waveform. The default is 1000.


            •       signal out —

           signal out is the generated waveform.

            •       error out —


970   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:970 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:971 ordinal=971 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.

GaussianGaussian WhiteWhite NoiseNoise WaveformWaveform

Generates a Gaussian distributed pseudorandom pattern whose statistical profile is
(0,s), where s is the absolute value of the specified standard deviation.


Inputs/Outputs

   •       reset signal —

    reset signal, if TRUE, resets the seed to the seed control value and the time stamp to zero. The
     default is FALSE.

   •      standard deviation —

    standard deviation is the standard deviation of the generated noise. The default is 1.0.

   •      seed —

    seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

    LabVIEW maintains the internal seed state independently for each instance of this reentrant VI.
    For a specific instance of this VI, if seed is less than or equal to 0, LabVIEW does not reseed the
    noise generator, and the noise generator resumes producing noise samples as a continuation of
    the previous noise sequence.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      sampling info —


                                                    © National Instruments 971

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:971 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:972 ordinal=972 -->
## Functions

Functions


          sampling info contains sampling information.

                   •      Fs —

               Fs is the sampling rate in samples per second. The default is 1000.

                   •      #s —

              #s is the number of samples in the waveform. The default is 1000.


            •       signal out —

           signal out is the generated waveform.

            •       error out —

           error out contains error information. This output provides standard error out functionality.

   PeriodicPeriodic RandomRandom NoiseNoise WaveformWaveform

     Generates a waveform containing periodic random noise (PRN).


     Inputs/Outputs

            •       reset signal —

           reset signal, if TRUE, resets the seed to the seed control value and the time stamp to zero. The
           default is FALSE.

            •       spectral amplitude —

           spectral amplitude is the magnitude of the frequency domain components of signal out.


972   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:972 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:973 ordinal=973 -->
## Functions

Functions

   •      seed —

    seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

    LabVIEW maintains the internal seed state independently for each instance of this reentrant VI.
    For a specific instance of this VI, if seed is less than or equal to 0, LabVIEW does not reseed the
    noise generator, and the noise generator resumes producing noise samples as a continuation of
    the previous noise sequence.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      sampling info —

    sampling info contains sampling information.

         •      Fs —

        Fs is the sampling rate in samples per second. The default is 1000.

         •      #s —

        #s is the number of samples in the waveform. The default is 1000.


   •       signal out —

    signal out is the generated waveform.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


The output array contains all frequencies which can be represented with an integral
number of cycles in the requested number of samples. Each frequency-domain
component has a magnitude of the input spectral amplitude and random phase.
Another way of thinking of the output array of PRN is that it is a summation of
sinusoidal signals with the same amplitudes but with random phases. The unit of
spectral amplitude is the same as the output PRN unit and is a linear measure of
amplitude, much like the other Waveform Generation VIs.


                                                    © National Instruments 973

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:973 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:974 ordinal=974 -->
## Functions

Functions

   InverseInverse ff NoiseNoise WaveformWaveform

     Generates a continuous noise waveform with a power spectral density that is inversely
     proportional to frequency over a specified frequency range.


     Inputs/Outputs

            •       reset signal (F) —

           reset signal resets the noise sample generator and the time stamp to zero. The default is FALSE.

            •      noise density —

          noise density specifies the spectral density (V/root Hz) of the ideal inverse-f noise waveform at
          the frequency reference freq.

         The actual inverse-f noise waveform approximates the ideal inverse-f noise over the frequency
          range defined by filter specifications. Therefore, the actual spectral density of the inverse-f
           noise waveform at reference freq is near noise density only if reference freq is within the design
          frequency range specified in filter specifications.

            •      exponent —

         exponent specifies the exponent of the desired inverse-f noise spectral shape.

           This VI generates the inverse-f noise waveform by passing white noise through a digital filter
          with a desired magnitude-squared response of 1/frequency^exponent.

            •        filter specifications —

              filter specifications specifies the operating frequency range and the filter order of the filter.

                   •      lower cutoff freq —


974   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:974 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:975 ordinal=975 -->
## Functions

Functions


      lower cutoff freq specifies the lower frequency edge of the operating frequency range of the
         filter.

      •      higher cutoff freq —

      higher cutoff freq specifies the higher frequency edge of the operating frequency range of
      the filter.

      •      order —

      order specifies the number of first order stages of the inverse-f filter. Increasing order
      improves the inverse-f spectral shape but requires more computation time during filter
       operation.


•      seed —

  seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

  LabVIEW maintains the internal seed state independently for each instance of this reentrant VI.
  For a specific instance of this VI, if seed is less than or equal to 0, LabVIEW does not reseed the
  noise generator, and the noise generator resumes producing noise samples as a continuation of
  the previous noise sequence.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. With the following
  exception, this input provides standard error in functionality.

  This node runs normally evenifan error occurred before this node runs.

•      sampling info —

  sampling info contains sampling information.

      •      Fs —

      Fs is the sampling rate in samples per second. The default is 1000.

      •      #s —


                                                   © National Instruments 975

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:975 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:976 ordinal=976 -->
## Functions

Functions


              #s is the number of samples in the waveform. The default is 1000.


            •      reference freq (Hz) —

           reference freq specifies the frequency in Hz at which the spectral density of the ideal inverse-f
           noise waveform is equal to noise density.

         The actual inverse-f noise waveform source is designed to approximate the ideal inverse-f noise
         waveform over the frequency range defined in filter specifications. Therefore, the actual
           spectral density of the inverse-f noise waveform at reference freq is near noise density if
           reference freq is within the design frequency range specified in filter specifications.

            •       signal out —

           signal out returns the generated inverse-f noise waveform.

            •      magnitude error (dB) —

         magnitude error returns the magnitude of the deviation of the actual inverse-f filter in dB when
         measured against the ideal inverse-f filter.

                                                                                exponent         The ideal filter has a magnitude-squared response proportional to 1/f        over the
          frequency range specified by filter specifications.

                   •      frequency (Hz) —

              frequency returns the frequencies of the magnitude error in Hz.

                   •      magnitude (dB) —

             magnitude returns the magnitudes of the magnitude error in dB.


            •      expected rms —

          expected rms returns the expected RMS level of the generated noise waveform.

            •        filter information —

              filter information returns the magnitude and phase of the frequency response of the designed
            inverse-f filter.


976   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:976 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:977 ordinal=977 -->
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


   •       error out —

    error out contains error information. This output provides standard error out functionality.


This VI generates the inverse-f noise waveform by passing spectrally flat, or white,
noise through a digital filter with a desired magnitude-squared response of 1/
frequency^exponent.


                                                    © National Instruments 977

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:977 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:978 ordinal=978 -->
## Functions

Functions

  GammaGamma NoiseNoise WaveformWaveform

     Generates a pseudorandom pattern of values which are the waiting times to the order
    number event of a unit mean Poisson process.


     Inputs/Outputs

            •       reset signal —

           reset signal, if TRUE, resets the seed to the seed control value and the time stamp to zero. The
           default is FALSE.

            •      order —

          order specifies the event number of the unit mean Poisson process. order must be greater than
             0. The default is 1.

            •      seed —

           seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

         LabVIEW maintains the internal seed state independently for each instance of this reentrant VI.
          For a specific instance of this VI, if seed is less than or equal to 0, LabVIEW does not reseed the
           noise generator, and the noise generator resumes producing noise samples as a continuation of
          the previous noise sequence.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. With the following
           exception, this input provides standard error in functionality.

           This node runs normally evenifan error occurred before this node runs.

            •      sampling info —

          sampling info contains sampling information.


978   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:978 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:979 ordinal=979 -->
## Functions

Functions


         •      Fs —

        Fs is the sampling rate in samples per second. The default is 1000.

         •      #s —

        #s is the number of samples in the waveform. The default is 1000.


   •       signal out —

    signal out is the generated waveform.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

PoissonPoisson NoiseNoise WaveformWaveform

Generates a pseudorandom sequence of values which are the number of discrete
events occurring in the interval specified by mean of a unit rate Poisson process.


Inputs/Outputs

   •       reset signal —

    reset signal, if TRUE, resets the seed to the seed control value and the time stamp to zero. The
     default is FALSE.

   •     mean —

   mean specifies the interval of a unit rate Poisson process. mean must be greater than or equal to
     0. The default is 1.0.


                                                    © National Instruments 979

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:979 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:980 ordinal=980 -->
## Functions

Functions

            •      seed —

           seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

         LabVIEW maintains the internal seed state independently for each instance of this reentrant VI.
          For a specific instance of this VI, if seed is less than or equal to 0, LabVIEW does not reseed the
           noise generator, and the noise generator resumes producing noise samples as a continuation of
          the previous noise sequence.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. With the following
           exception, this input provides standard error in functionality.

           This node runs normally evenifan error occurred before this node runs.

            •      sampling info —

          sampling info contains sampling information.

                   •      Fs —

               Fs is the sampling rate in samples per second. The default is 1000.

                   •      #s —

              #s is the number of samples in the waveform. The default is 1000.


            •       signal out —

           signal out is the generated waveform.

            •       error out —

           error out contains error information. This output provides standard error out functionality.

   BinomialBinomial NoiseNoise WaveformWaveform

     Generates a binomially-distributed pseudorandom pattern whose values are the
    number of occurrences of an event given the probability of that event occurring and


980   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:980 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:981 ordinal=981 -->
## Functions

Functions

the number of trials.


Inputs/Outputs

   •       reset signal —

    reset signal, if TRUE, resets the seed to the seed control value and the time stamp to zero. The
     default is FALSE.

   •        trial probability —

     trial probability is the probability that a given trial is true (1). trial probability must be in the
    range [0, 1]. The default is 0.5.

   •      seed —

    seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

    LabVIEW maintains the internal seed state independently for each instance of this reentrant VI.
    For a specific instance of this VI, if seed is less than or equal to 0, LabVIEW does not reseed the
    noise generator, and the noise generator resumes producing noise samples as a continuation of
    the previous noise sequence.

   •        trials —

     trials is the number of trials performed for each element of signal out. The default is 1.0.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •      sampling info —

    sampling info contains sampling information.


                                                    © National Instruments 981

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:981 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:982 ordinal=982 -->
## Functions

Functions


                   •      Fs —

               Fs is the sampling rate in samples per second. The default is 1000.

                   •      #s —

              #s is the number of samples in the waveform. The default is 1000.


            •       signal out —

           signal out is the generated waveform.

            •       error out —

           error out contains error information. This output provides standard error out functionality.

   BernoulliBernoulli NoiseNoise WaveformWaveform

     Generates a pseudorandom pattern of ones and zeros, where the probability of
     generating a one is one probability and the probability of generating a zero is (1–one
      probability).

         If one probability is 0.7, each element of signal out has a 70% chance of being one and
     a 30% chance of being zero.


     Inputs/Outputs

            •       reset signal —

           reset signal, if TRUE, resets the seed to the seed control value and the time stamp to zero. The
           default is FALSE.

            •     one probability —

982   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:982 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:983 ordinal=983 -->
## Functions

Functions


  one probability specifies the probability of a given element of signal out being true (1). The
  default is 0.5.

•      seed —

  seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

  LabVIEW maintains the internal seed state independently for each instance of this reentrant VI.
  For a specific instance of this VI, if seed is less than or equal to 0, LabVIEW does not reseed the
  noise generator, and the noise generator resumes producing noise samples as a continuation of
  the previous noise sequence.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. With the following
  exception, this input provides standard error in functionality.

  This node runs normally evenifan error occurred before this node runs.

•      sampling info —

  sampling info contains sampling information.

      •      Fs —

      Fs is the sampling rate in samples per second. The default is 1000.

      •      #s —

      #s is the number of samples in the waveform. The default is 1000.


•       signal out —

  signal out is the generated waveform.

•       error out —

  error out contains error information. This output provides standard error out functionality.


                                                   © National Instruments 983

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:983 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:984 ordinal=984 -->
## Functions

Functions

  MLSMLS SequenceSequence WaveformWaveform

     Generates a maximum length sequence of ones and zeros using a modulo-2 primitive
     polynomial of order polynomial order.


     Inputs/Outputs

            •       reset signal —

           reset signal, if TRUE, resets the seed to the seed control value and the time stamp to zero. The
           default is FALSE.

            •      polynomial order —

          polynomial order specifies the order of the modulo-2 primitive polynomial used to generate
           signal out. The default value is 31.

            •      seed —

           seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

         LabVIEW maintains the internal seed state independently for each instance of this reentrant VI.
          For a specific instance of this VI, if seed is less than or equal to 0, LabVIEW does not reseed the
           noise generator, and the noise generator resumes producing noise samples as a continuation of
          the previous noise sequence.

            •       error in (no error) —

           error in describes error conditions that occur before this node runs. With the following
           exception, this input provides standard error in functionality.

           This node runs normally evenifan error occurred before this node runs.

            •      sampling info —

          sampling info contains sampling information.


984   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:984 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:985 ordinal=985 -->
## Functions

Functions


         •      Fs —

        Fs is the sampling rate in samples per second. The default is 1000.

         •      #s —

        #s is the number of samples in the waveform. The default is 1000.


   •       signal out —

    signal out is the generated waveform.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


The binary Maximum Length Sequence (MLS) also is known as the Pseudo-Random
Binary Sequence (PRBS).
SimulateSimulate SignalSignal

Simulates a sine wave, square wave, triangle wave, sawtooth wave, or noise signal.


Dialog Box Options

 Option   Description

          Contains the following options:

                  • Signal type—
 Signal
             Type of waveform to simulate. You can simulate a sine wave, square wave, sawtooth
             wave, triangle wave, or noise (DC).


                                                    © National Instruments 985

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:985 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:986 ordinal=986 -->
## Functions

Functions


      Option   Description

                           • Frequency (Hz)—

                   Frequency in hertz of the waveform. The default is 10.1.

                           • Phase (deg)—

                           Initial phase in degrees of the waveform. The default is 0.

                           • Amplitude—

                   Amplitude of the waveform. The default is 1.

                           • Offset—

                DC offset of the signal. The default is 0.

                           • Duty cycle (%)—

                    Percentage of time a square wave remains high versus low over one period. The
                      default is 50.

                           • Add noise—

                  Adds noise to the simulated waveform.

                           • Noise type—

                      Specifies the type of noise to add to the waveform. This option is available only when
                  you place a checkmark in the Add Noise checkbox.

                  You can add the following noise types:
         ◦ Uniform White Noise generates a signal that contains a uniformly distributed,
                     pseudorandom pattern whose values are in the range [-a:a], where ais the
                        absolute value of Amplitude.
         ◦ Gaussian White Noise generates a signal that contains a Gaussian-distributed,
                     pseudorandom pattern whose statistical profile is (µ,sigma) = (0,s), where sis
                        the absolute value of the specified Standard deviation.
         ◦  Periodic Random Noise generates a signal that contains periodic random noise
                         (PRN).
         ◦ Gamma Noise generates a signal that contains a pseudorandom pattern of
                         values that are the waiting times to the Order number event of a unit mean


986   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:986 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:987 ordinal=987 -->
## Functions

Functions


Option   Description

                 Poisson process.
      ◦ Poisson Noise generates a signal that contains a pseudorandom sequence of
                  values that are the number of discrete events occurring in a given interval,
                   specified by Mean, of a unit rate Poisson process.
      ◦ Binomial Noise generates a signal that contains a binomially distributed,
               pseudorandom pattern whose values are the number of occurrences of an
                  event, given the probability of that event occurring and the number of trials.
      ◦  Bernoulli Noise generates a signal that contains a pseudorandom pattern of
                ones and zeros.
      ◦ MLS Sequence generates a signal that contains a maximum length sequence of
                ones and zeros using a modulo-2 primitive polynomial of order Polynomial
                  order.
      ◦ Inverse F Noise generates a signal that contains a continuous noise waveform
                 with a power spectral density that is inversely proportional to frequency over a
                   specified frequency range.
                 • Noise amplitude—

          Maximum absolute value the signal can have. The default is 0.6. This option is
              available only when you select Uniform White Noise or Inverse F Noise from the
             Noise type pull-down menu.

                 • Standard deviation—

             Standard deviation of the noise you generate. The default is 0.6. This option is
              available only when you select Gaussian White Noise from the Noise type pull-down
           menu.

                 • Spectral amplitude—

            Magnitude of the frequency domain components of the simulated signal. The default
                  is 0.6. This option is available only when you select Periodic Random Noise from the
             Noise type pull-down menu.

                 • Order—

               Specifies the event number of the unit mean Poisson process. The default is 0.6. This
             option is available only when you select Gamma Noise from the Noise type pull-
          down menu.

                 • Mean—


                                                    © National Instruments 987

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:987 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:988 ordinal=988 -->
## Functions

Functions


      Option   Description

                      Specifies the interval of a unit rate Poisson process. The default is 0.6. This option is
                      available only when you select Poisson Noise from the Noise type pull-down menu.

                           •  Trial probability—

                      Probability that a given trial is TRUE. The default is 0.6. This option is available only
                when you select Binomial Noise from the Noise type pull-down menu.

                           • One probability—

                      Specifies the probability that a given element of the signal is TRUE. The default is 0.6.
                     This option is available only when you select Bernoulli Noise from the Noise type
                   pull-down menu.

                           • Polynomial order—

                      Specifies the order of the modulo-2 primitive polynomial to use to generate the
                        signal. The default is 0.6. This option is available only when you select MLS Sequence
                  from the Noise type pull-down menu.

                           • Seed number—

                When greater than 0, causes reseeding of the noise sample generator. The default is
                       –1. LabVIEW maintains the internal seed state independently for each instance of this
                     reentrant VI. For a specific instance of this VI, if Seed number is less than or equal to
                         0, LabVIEW does not reseed the noise generator, and the noise generator resumes
                   producing noise samples as a continuation of the previous noise sequence.

                           • Exponent—

                      Specifies the exponent of the inverse-f spectral shape you want. The default is 1. This
                    option is available only when you select Inverse F Noise from the Noise type pull-
                down menu.

                Contains the following options:

                           • Samples per second (Hz)—
      Timing
                   Sampling rate in samples per second. The default is 1000.

                           • Number of samples—


988   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:988 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:989 ordinal=989 -->
## Functions

Functions


Option   Description

           Number of samples in the signal. The default is 100.

                 • Automatic—

              Sets the Number of samples to be one-tenth of Samples per second (Hz).

                 •  Integer number of cycles—

              Sets the nearest frequency and Number of samples such that the waveform contains
           an integer number of cycles.

                 • Actual number of samples—

              Indicates the actual number of samples in the waveform when you select Integer
           number of cycles.

                 • Actual frequency—

              Indicates the actual frequency of the waveform when you select Integer number of
               cycles.

                 • Simulate acquisition timing—

             Simulates an acquisition rate comparable to an actual acquisition rate.

                 • Run as fast as possible—

             Simulates the signal as quickly as the system allows.

         Contains the following options:

                 • Absolute (date and time)—

              Displays the timestamp in terms of time elapsed since 12:00 a.m., Friday, January 1,
Time         1904, Universal Time [01-01-1904 00:00:00].
Stamps
                 •  Relative to start of measurement—

              Displays the timestamp in terms of seconds starting from zero. For example, 100 in
               relative time equals 1 minute and 40 seconds.


                                                    © National Instruments 989

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:989 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:990 ordinal=990 -->
## Functions

Functions


      Option   Description

                Contains the following options:

                           • Reset phase, seed, and time stamps—

                    Resets the phase to the phase value and the time stamp to zero. Resets the seed
       Reset       number to –1.
       Signal
                           • Use continuous generation—

                    Continuously simulates the signal. Does not reset the phase, time stamp, or seed
                  number.

                Contains the following options:

                           • Use signal type name—

       Signal       Uses the default signal name.
     Name
                           • Signal name—

                    Contains the following options:

       Result
                 Displays a preview of the signal to be simulated.      Preview

     Inputs/Outputs

            •       error in (no error) —

           Describes error conditions that occur before this node runs.

            •       Offset —

           Specifies the DC offset of the signal. The default is 0. The value you wire to this input overrides
          the value you set in the configuration dialog box.

            •      Phase —

           Specifies the initial phase in degrees of the signal. The default is 0. The value you wire to this
           input overrides the value you set in the configuration dialog box.

            •      Amplitude —

990   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:990 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:991 ordinal=991 -->
## Functions

Functions


  Specifies the amplitude of the signal. The default is 1. The value you wire to this input overrides
  the value you set in the configuration dialog box.

•      Duty Cycle (%) —

  Specifies the percentage of time a square wave remains high versus low over one period. The
  default is 50. The value you wire to this input overrides the value you set in the configuration
  dialog box.

•      Noise Amplitude —

  Specifies the maximum absolute value the signal can have. The default is 0.6. The value you wire
  to this input overrides the value you set in the configuration dialog box.

•      Standard deviation —

  Specifies the standard deviation of the noise you generate. The default is 0.6. The value you wire
  to this input overrides the value you set in the configuration dialog box.

•      Spectral amplitude —

  Specifies the magnitude of the frequency domain components of the simulated signal. The
  default is 0.6. The value you wire to this input overrides the value you set in the configuration
  dialog box.

•      Order —

  Specifies the event number of the unit mean Poisson process. The default is 0.6. The value you
  wire to this input overrides the value you set in the configuration dialog box.

•     Mean —

  Specifies the interval of a unit rate Poisson process. The default is 0.6. The value you wire to this
  input overrides the value you set in the configuration dialog box.

•       Trial probability —

  Specifies the probability that a given trial is TRUE. The default is 0.6. The value you wire to this
  input overrides the value you set in the configuration dialog box.

•     One probability —

  Specifies the probability that a given element of the signal is TRUE. The default is 0.6. The value


                                                   © National Instruments 991

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:991 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:992 ordinal=992 -->
## Functions

Functions


         you wire to this input overrides the value you set in the configuration dialog box.

            •      Polynomial Order —

           Specifies the order of the modulo-2 primitive polynomial to use to generate the signal. The
           default is 0.6. The value you wire to this input overrides the value you set in the configuration
           dialog box.

            •      Exponent —

           Specifies the exponent of the inverse-f spectral shape you want. The default is 1. The value you
           wire to this input overrides the value you set in the configuration dialog box.

            •       Trials —

           Specifies the number of trials performed for each element of the simulated signal. The default is
             1. The value you wire to this input overrides the value you set in the configuration dialog box.

            •      Reset Signal —

           Specifies when to reset the signal. The value you wire to this input overrides the value you set in
          the configuration dialog box.

            •     Seed Number —

          Reseeds the noise sample generator when this value is > 0. The default is –1. If seed is 0, the
           noise generator does not reseed and resumes producing noise samples as a continuation of the
           previous noise sequence. The value you wire to this input overrides the value you set in the
           configuration dialog box.

            •      Frequency —

           Specifies the frequency in hertz of the waveform. The default is 10.1. The value you wire to this
           input overrides the value you set in the configuration dialog box.

            •      Signal —

          Returns the output signal formatted as dynamic data.

            •       error out —

          Contains error information. This output provides standard error out functionality.


992   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:992 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:993 ordinal=993 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Express VIs\Express VI - Amplitude and
   Level Measurements.vi

Components

Specifies the type of noise to add to the waveform. This option is available only when
you place a checkmark in the Add Noise checkbox.

Type of waveform to simulate. You can simulate a sine wave, square wave, sawtooth
wave, triangle wave, or noise (DC).

Continuously simulates the signal. Does not reset the phase, time stamp, or seed
number.

Resets the phase to the phase value and the time stamp to zero. Resets the seed
number to –1.

Indicates the actual number of samples in the waveform when you select Integer
number of cycles.

Indicates the actual frequency of the waveform when you select Integer number of
cycles.

Sets the nearest frequency and Number of samples such that the waveform contains
an integer number of cycles.

Probability that a given trial is TRUE. The default is 0.6. This option is available only
when you select Binomial Noise from the Noise type pull-down menu.

When greater than 0, causes reseeding of the noise sample generator. The default is –1.
LabVIEW maintains the internal seed state independently for each instance of this
reentrant VI. For a specific instance of this VI, if Seed number is less than or equal to 0,
LabVIEW does not reseed the noise generator, and the noise generator resumes
producing noise samples as a continuation of the previous noise sequence.


                                                    © National Instruments 993

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:993 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:994 ordinal=994 -->
## Functions

Functions

    Maximum absolute value the signal can have. The default is 0.6. This option is
      available only when you select Uniform White Noise or Inverse F Noise from the Noise
     type pull-down menu.

     Adds noise to the simulated waveform.

     Simulates the signal as quickly as the system allows.

     Simulates an acquisition rate comparable to an actual acquisition rate.

      Displays the timestamp in terms of time elapsed since 12:00 a.m., Friday, January 1,
     1904, Universal Time [01-01-1904 00:00:00].

      Displays the timestamp in terms of seconds starting from zero. For example, 100 in
      relative time equals 1 minute and 40 seconds.

      Sets the Number of samples to be one-tenth of Samples per second (Hz).

     Contains the following options:

     Percentage of time a square wave remains high versus low over one period. The
      default is 50.

    DC offset of the signal. The default is 0.

       Initial phase in degrees of the waveform. The default is 0.

     Amplitude of the waveform. The default is 1.

     Frequency in hertz of the waveform. The default is 10.1.

     Sampling rate in samples per second. The default is 1000.

     Uses the default signal name.

      Displays the default signal name when you place a checkmark in the Use signal type
    name checkbox.

    Number of samples in the signal. The default is 100.

994   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:994 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:995 ordinal=995 -->
## Functions

Functions

Number of samples in the signal. The default is 100.

Displays a preview of the signal to be simulated.
SimulateSimulate ArbitraryArbitrary SignalSignal

Simulates a signal that you define.


Dialog Box Options

 Option          Description

                 Contains the following options:

                             • Define Signal—

                      Displays the Define Signal dialog box, which you use to generate an arbitrary
                         signal.

                             •  Start over when end of signal is reached—

                     Continuously simulates the signal you defined.
 Signal
 Specifications    ◦ X values repeat (0, 1, 2, 0, 1, 2)—

                        Repeats the xvalues when you select Start over when end of signal is
                         reached.

          ◦ X values continue (0, 1, 2, 3, 4, 5)—

                           Sequentially increments the xvalues when you select Start over when
                     end of signal is reached.

 Signal
                 Contains the following options:
 Generation


                                                    © National Instruments 995

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:995 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:996 ordinal=996 -->
## Functions

Functions


      Option          Description

                                      • One point per iteration—

                           Simulates one point per iteration.

                                      •  Entire signal each iteration—

                           Simulates the entire signal each iteration.

                                      • One defined Y point per iteration (no interpolation)—

                           Simulates one defined Y point per iteration without using interpolation.


       Signal Name     Specifies the name of the signal to display on the block diagram.


                         Displays a preview of the signal to be simulated.

                                      • Number of points—
       Result Preview
                             Displays the number of data points in the signal you defined in the Define
                             Signal dialog box.


     Inputs/Outputs

            •      Reset —

           Controls the initialization of the internal state of the VI. The default is FALSE.

            •      Next Value —

           Specifies the next value of the signal. The default is TRUE. If FALSE, the Express VI outputs the
        same value for each iteration.

            •       error in (no error) —

           Describes error conditions that occur before this node runs.

            •      Signal —


996   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:996 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:997 ordinal=997 -->
## Functions

Functions


    Returns the output signal formatted as dynamic data.

   •       error out —

    Contains error information. This output provides standard error out functionality.

   •      Data Valid —

     Indicates whether the data is valid.


Components

Specifies the name of the signal to display on the block diagram.

Displays the Define Signal dialog box, which you use to generate an arbitrary signal.

Displays the number of data points in the signal you defined in the Define Signal dialog
box.

Sequentially increments the xvalues when you select Start over when end of signal is
reached.

Repeats the xvalues when you select Start over when end of signal is reached.

Continuously simulates the signal you defined.

Simulates the entire signal each iteration.

Simulates one point per iteration.

Simulates one defined Y point per iteration without using interpolation.

Specifies the name of the signal to display on the block diagram.

Displays a preview of the signal to be simulated.


                                                    © National Instruments 997

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:997 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:998 ordinal=998 -->
## Functions

Functions

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


                       Calculates the DC and RMS values of an input waveform or array of waveforms.       Averaged DC-                       This VI is similar to the Basic Averaged DC-RMS VI, but this VI gives more precise     RMS
                       control over the individual DC and RMS calculations.


                      Returns the average and RMS levels of a selected cycle of a periodic waveform or
       Cycle Average
                   an array of periodic waveforms. Wire data to the signal in input to determine the
      and RMS
                     polymorphic instance to use or manually select the instance.


      Waveform     Use the Waveform Monitoring VIs to analyze the waveforms for trigger points, to
       Monitoring     search for peaks, and to perform limit mask testing.


        Transition
                      Accepts an input signal of a single waveform or an array of waveforms and
      Measurements


998   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:998 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:999 ordinal=999 -->
## Functions

Functions


Palette Object  Description

              measures the transition duration (rise or fall time), slew rate, undershoot, and
               overshoot of a selected positive or negative transition in each waveform. Wire data
                to the signal in input to determine the polymorphic instance to use or manually
                 select the instance.


               Accepts a periodic waveform or an array of periodic waveforms and returns the
Pulse          period, pulse duration (pulse width), duty cycle (duty factor), and pulse center of
Measurements a selected pulse and period. Wire data to the signal in input to determine the
              polymorphic instance to use or manually select the instance.


               Returns the amplitude, high state level, and low state level of a waveform or anAmplitude                array of waveforms. Wire data to the signal in input to determine the polymorphic
and Levels                instance to use or manually select the instance.


              Takes a signal in, finds the single tone with the highest amplitude or searches a
Extract Single   specified frequency range, and returns the single tone frequency, amplitude, and
Tone          phase. The input signal can be real or complex and single-channel or multichannel.
Information    Wire data to the time signal in input to determine the polymorphic instance to use
               or manually select the instance.


Extract         Returns the frequency, amplitude, and phase for each signal tone whose
Multiple Tone  amplitude exceeds a specified threshold. Wire data to the time signal in input to
Information    determine the polymorphic instance to use or manually select the instance.


              Takes a signal in and performs a full harmonic analysis, including measuring the
Harmonic     fundamental frequency tone and harmonics, and returning the fundamental
Distortion      frequency, all harmonic amplitude levels, and the total harmonic distortion (THD).
Analyzer       Wire data to the signal in input to determine the polymorphic instance to use or
              manually select the instance.


SINAD         Takes a signal in and performs a full Signal in Noise and Distortion (SINAD)
Analyzer        analysis, including measuring the fundamental frequency tone and returning the


                                                    © National Instruments 999

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:999 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1000 ordinal=1000 -->
## Functions

Functions


         Palette Object  Description

                      fundamental frequency and SINAD level in dB. Wire data to the signal in input to
                      determine the polymorphic instance to use or manually select the instance.


        FFT Power     Computes the averaged auto power spectrum of time signal. Wire data to the time
        Spectrum and  signal input to determine the polymorphic instance to use or manually select the
       PSD            instance.


                    Computes the averaged FFT spectrum of time signal. This VI returns the FFT results        FFT Spectrum                       as magnitude and phase. Wire data to the time signal input to determine the        (Mag-Phase)                      polymorphic instance to use or manually select the instance.


                    Computes the averaged FFT spectrum of time signal. This VI returns the FFT results        FFT Spectrum                       as real and imaginary parts. Wire data to the time signal input to determine the         (Real-Im)
                      polymorphic instance to use or manually select the instance.

        Frequency
        Response     Computes the frequency response and the coherence based on the input signals.
         Function       Results are returned as magnitude, phase, and coherence.
        (Mag-Phase)

        Frequency
        Response     Computes the frequency response and the coherence based on the input signals.
         Function       Results are returned as real part, imaginary part, and coherence.
         (Real-Im)

         Cross
                    Computes the averaged cross power spectrum of the input signals. Results are
        Spectrum
                        returned as magnitude and phase.
        (Mag-Phase)

         Cross
                    Computes the averaged cross power spectrum of the input signals. Results are
        Spectrum
                        returned as real and imaginary parts.
         (Real-Im)


         Spectral       Performs FFT-based spectral measurements, such as the averaged magnitude
        Measurements spectrum, power spectrum, and phase spectrum on a signal.


1000   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1000 -->

