# NI DOCUMENT BUNDLE: labview-nxg-data-types

<!--NI_BUNDLE_CHUNK bundle=labview-nxg-data-types start=1 end=18 -->
<!--NI_TOPIC bundle=labview-nxg-data-types path=addressing-issues-with-numeric-conversions.html language=enus -->
## TOPIC 00001: Addressing Issues with Numeric Conversions

- bundle_id: `labview-nxg-data-types`
- source_path: `addressing-issues-with-numeric-conversions.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-types/raw/resource/enus/addressing-issues-with-numeric-conversions.html
- document_id: `labview-nxg-data-types`
- page_type: `leaf`
- content_type: `task`
- source_description: When you wire numeric data to a node that expects a different numeric data type, the node coerces the data to the most precise type. A red coercion dot appears where the coercion takes place. Because numeric coercions can affect memory usage, performance of a VI, or cause a VI to generate inaccurate

Addressing Issues with Numeric Conversions

When you wire numeric data to a node that expects a different numeric data type, the node coerces the data to the most precise type. A red coercion dot appears where the coercion takes place. Because numeric coercions can affect memory usage, performance of a VI, or cause a VI to generate inaccurate results, use one of the strategies in the following table to eliminate or reduce the impact of a problematic coercion.

| Strategy | Details | Action | Example |
| --- | --- | --- | --- |
| Match input data types. | Create an object that matches the data type the node expects. If you wire data from a G type to a node or subVI that does not accept the data type of the G type, your VI may break or generate inaccurate data. Replace the node or subVI with one that matches the data type used in the G type, or replace the G type with a constant of the matching data type. | Right-click the coerced control, constant, or indicator on the diagram, select Representation from the shortcut menu, and select the matching data type. | In the following diagram, the red coercion dot on the top input of the Add node indicates that the node is coercing I16 (x), a signed integer, to an unsigned integer to match the data type of U16 (y). This causes Add to return a sum of 65,531 instead of -5. If you change the data type representation of I16 (x) so that both inputs are signed integers, no coercion is necessary, and the node performs an accurate computation, as you can see in the following diagram. |
| Use a conversion node. | Conversion nodes convert one data type to another. Conversion nodes have the same effect as the automatic coercions that occur when you wire numeric data to a node that expects a different numeric data type. However, when you use a conversion node you can control where in your VI the conversion takes place, which can improve VI performance in certain cases. | To add a conversion node from the diagram palette, navigate to Data Types » Numeric » Conversion and select the desired conversion node. | You may want to use a conversion node inside a loop that generates an array so the conversion is performed before the VI generates the array. This allows you to avoid a large data buffer. In the following diagram, To Single Precision Float converts the Random Number output to a single-precision number inside the For Loop to prevent the Add node from converting a large amount of data. |

Parent topic:

Numeric Data

Related concepts:

- Numeric Conversions

<!--NI_TOPIC bundle=labview-nxg-data-types path=array-controls.html language=enus -->
## TOPIC 00002: Array Controls

- bundle_id: `labview-nxg-data-types`
- source_path: `array-controls.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-types/raw/resource/enus/array-controls.html
- document_id: `labview-nxg-data-types`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following image is an example of a one-dimensional numeric array control. Index display—Determines which element to display at the top of the array control. An array index is zero-based. Element display—Value in the array.

Array Controls

The following image is an example of a one-dimensional numeric array control.

[IMAGE alt='1378' src='GUID-D61DFC01-601A-43FC-9F5B-553B20AF380A-a5.png']

1. Index display—Determines which element to display at the top of the array control. An array index is zero-based.
2. Element display—Value in the array.

Parent topic:

Arrays

<!--NI_TOPIC bundle=labview-nxg-data-types path=arrays.html language=enus -->
## TOPIC 00003: Arrays

- bundle_id: `labview-nxg-data-types`
- source_path: `arrays.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-types/raw/resource/enus/arrays.html
- document_id: `labview-nxg-data-types`
- page_type: `leaf`
- content_type: `concept`
- source_description: An array combines data of the same data type into one data structure. An array consists of elements and dimensions. Elements are the data that make up the array. Dimensions represent the length, height, or depth of an array. Consider using arrays when you work with a collection of similar data and w

Arrays

An 
 *array* combines data of the same data type into one data structure. An array consists of elements and dimensions. Elements are the data that make up the array. Dimensions represent the length, height, or depth of an array.

Consider using arrays when you work with a collection of similar data and when you perform repetitive computations. You can build arrays of numeric, Boolean, path, string, waveform, and cluster data types. You cannot create arrays of arrays. However, you can use a multidimensional array or create an array of clusters where each cluster contains one or more arrays.

[IMAGE alt='1378' src='GUID-F3583466-6AA3-436B-AC52-878EDF6F47B7-a5.png']

Parent topic:

Data Type Reference

<!--NI_TOPIC bundle=labview-nxg-data-types path=boolean-data.html language=enus -->
## TOPIC 00004: Boolean Data

- bundle_id: `labview-nxg-data-types`
- source_path: `boolean-data.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-types/raw/resource/enus/boolean-data.html
- document_id: `labview-nxg-data-types`
- page_type: `leaf`
- content_type: `concept`
- source_description: Boolean data represents True and False values. On the diagram, Boolean values are represented by green objects and wires. On the panel, Boolean data is represented as switches or buttons with mechanical actions that represent physical switches and buttons.

Boolean Data

Boolean data represents True and False values.

On the diagram, Boolean values are represented by green objects and wires.

[IMAGE alt='1378' src='GUID-DE0DFD50-C59B-4038-8BE5-22A8FEAEF60D-a5.png']

On the panel, Boolean data is represented as switches or buttons with mechanical actions that represent physical switches and buttons.

Parent topic:

Data Type Reference

<!--NI_TOPIC bundle=labview-nxg-data-types path=comparison-modes.html language=enus -->
## TOPIC 00005: Comparison Modes for Array and Cluster Data

- bundle_id: `labview-nxg-data-types`
- source_path: `comparison-modes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-types/raw/resource/enus/comparison-modes.html
- document_id: `labview-nxg-data-types`
- page_type: `leaf`
- content_type: `concept`
- source_description: When using certain Comparison nodes to compare data contained in arrays or clusters, you can select from two comparison modes. Compare elements when you want to compare the individual corresponding elements of the input arrays or clusters. Compare aggregates when you want to compare the input arrays

Comparison Modes for Array and Cluster Data

When using certain Comparison nodes to compare data contained in arrays or clusters, you can select from two comparison modes.

Compare elements when you want to compare the individual corresponding elements of the input arrays or clusters.

Compare aggregates when you want to compare the input arrays or clusters in their entirety.

Note

Greater?

Equal?

Less or Equal?

Greater Than 0?

#### Example

The following table describes the behavior of Greater? in each of the two comparison modes.

| Comparison Mode | Input Array 1 (x) | Input Array 2 (y) | Result (x > y?) | Comments |
| --- | --- | --- | --- | --- |
| Elements | [1,2,3,4] | [2,1,4,3] | [False, True, False, True] | Greater? compares the individual corresponding elements and returns an array of Boolean values that represent the result of each comparison. |
| Aggregates | [1,2,3,4] | [2,1,4,3] | False | In Aggregates mode, a Comparison node processes corresponding elements sequentially, checking for inequalities. The node stops as soon as it encounters corresponding elements that are not equal or reaches the end of one of the input arrays or clusters and performs the comparison on those elements. The first elements in the input arrays are not equal, so Greater? stops and returns a single Boolean value representing the result of 1 > 2? |

You can change the comparison mode for a selected Comparison node by selecting 
 Elements or 
 Aggregates on the 
 Item tab in the 
 Compare section.

Parent topic:

Data Type Reference

Related information:

- Comparison Nodes

<!--NI_TOPIC bundle=labview-nxg-data-types path=conversion-behavior.html language=enus -->
## TOPIC 00006: Conversion Behaviors

- bundle_id: `labview-nxg-data-types`
- source_path: `conversion-behavior.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-types/raw/resource/enus/conversion-behavior.html
- document_id: `labview-nxg-data-types`
- page_type: `leaf`
- content_type: `concept`
- source_description: By default, a data type with fewer bits changes to match the data type with more bits. If the number of bits is the same, unsigned data types are chosen over signed data types to retain as much precision as possible. Conversion behaviors depend on the data types you are converting between or the nod

Conversion Behaviors

By default, a data type with fewer bits changes to match the data
 type with more bits. If the number of bits is the same, unsigned data types are chosen
 over signed data types to retain as much precision as possible.

Conversion behaviors depend on the data types you are converting between or the node accepting the data. For example, if you wire two different data types to a node that expects matching data types, one of the inputs is converted to match the other.

| Original Type | Converted Type | Conversion Behavior | Behavior Details |
| --- | --- | --- | --- |
| Signed or unsigned integer | Floating-point number | Data is coerced to the nearest value possible. | This conversion is exact when the floating-point number is more precise than the integer. If the integer is more precise than the floating-point number, the floating-point data type maintains as much precision as possible in the conversion. |
| Floating-point number | Signed or unsigned integer | In-range values are coerced to a signed or unsigned integer. Out-of-range values are coerced to the minimum or maximum value of the integer. | This conversion is less precise if the floating-point number is an out-of-range value. For example, unsigned integers represent only non-negative integers. If you convert a negative floating-point number to an unsigned integer, the result is 0. |
| Integer | Integer | If the source is smaller than the destination, the sign of a signed source is extended and zeros are placed in the extra bits of an unsigned source. If the source is larger than the destination, the destination retains only the least significant bits of the source value. | Out-of-range values are not coerced to the minimum or maximum value of an integer. The software attempts to retain as much precision as possible when converting between integer types. |

Note

Parent topic:

Numeric Data

<!--NI_TOPIC bundle=labview-nxg-data-types path=creating-custom-data-type-using-g-type-document.html language=enus -->
## TOPIC 00007: Creating a Custom Data Type Using a G Type Document

- bundle_id: `labview-nxg-data-types`
- source_path: `creating-custom-data-type-using-g-type-document.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-types/raw/resource/enus/creating-custom-data-type-using-g-type-document.html
- document_id: `labview-nxg-data-types`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a type definition, or custom data type, to reuse a control or constant throughout your project. You define the type definition with the control you add to the panel of a G Type document. An example of when a type definition would be useful is keeping state enums of a state machine in sync. Be

Creating a Custom Data Type Using a G Type Document

Create a type definition, or custom data type, to reuse a control or constant
 throughout your project. You define the type definition with the control you
 add to the panel of a G Type document.

An example of when a type definition would be useful is keeping state enums of a state machine
 in sync. Because instances of a type definition share a source file, you can update
 the source enum, the type definition, with additional states as needed and propagate
 the changes to all instances rather than having to update each copy individually.

1. From the Project Files tab, expand the
 New menu and select Type
 Definition to create a G Type document.
2. In the G Type document, add a single control, array of controls, or cluster of controls that you want to reuse throughout your application. 
 The data type of the control you add to the G Type document panel defines the data type of
 the type definition. org.dita.html5/xsl/topic.xsl 455Note Adding
 more than one control outside of an array or cluster or more than one array
 or cluster of controls to a G Type document makes the type definition
 unusable.
3. In the Item tab, configure the control with the settings
 you want to persist to each instance of the type definition.
4. Save the G Type document.

Project Files

Parent topic:

Type Definitions

Related concepts:

- Type Definitions

Related tasks:

- Updating Custom Data Type Instances Throughout Your Project

<!--NI_TOPIC bundle=labview-nxg-data-types path=data-types.html language=enus -->
## TOPIC 00008: Data Type Reference

- bundle_id: `labview-nxg-data-types`
- source_path: `data-types.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-types/raw/resource/enus/data-types.html
- document_id: `labview-nxg-data-types`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can use the following data types for controls and indicators, diagram terminals, wires, and node terminals. Icon Data Type Details Single-precision, floating-point numeric (SGL) Minimum positive number: 1.40e-45 Maximum positive number: 3.40e+38 Minimum negative number: -3.40e+38 Maximum negativ

Data Type Reference

You can use the following data types for controls and indicators, diagram terminals, wires, and node terminals.

| Icon | Data Type | Details |
| --- | --- | --- |
|  | Single-precision, floating-point numeric (SGL) | Minimum positive number: 1.40e-45 Maximum positive number: 3.40e+38 Minimum negative number: -3.40e+38 Maximum negative number: -1.40e-45 |
|  | Double-precision, floating-point numeric (DBL) | Minimum positive number: 4.94e-324 Maximum positive number: 1.79e+308 Minimum negative number: -1.79e+308 Maximum negative number: -4.94e-324 |
|  | Complex single-precision, floating-point numeric (CSG) | Same as single-precision, floating-point, with a real and an imaginary part. |
|  | Complex double-precision, floating-point numeric (CDB) | Same as double-precision, floating-point, with a real and an imaginary part. |
|  | 8-bit signed integer numeric (I8) | A positive or negative integer stored using 8 bits, or a single byte. Range: -128 to 127 |
|  | 16-bit signed integer numeric (I16) | A positive or negative integer stored using 16 bits, or two bytes. Range: -32,768 to 32,767 |
|  | 32-bit signed integer numeric (I32) | A positive or negative integer stored using 32 bits, or four bytes. Range: -2,147,483,648 to 2,147,483,647 |
|  | 64-bit signed integer numeric (I64) | A positive or negative integer stored using 64 bits, or eight bytes. Approximate Range: -1e19 to 1e19 |
|  | 8-bit unsigned integer numeric (U8) | A positive integer stored using 8 bits, or a single byte. Range: 0 to 255 |
|  | 16-bit unsigned integer numeric (U16) | A positive integer stored using 16 bits, or two bytes. Range: 0 to 65,535 |
|  | 32-bit unsigned integer numeric (U32) | A positive integer stored using 32 bits, or four bytes. Range: 0 to 4,294,967,295 |
|  | 64-bit unsigned integer numeric (U64) | A positive integer stored using 64 bits, or eight bytes. Approximate Range: 0 to 2e19 |
|  | timestamp | A time and date. Minimum time: 01/01/1600 00:00:00 UTC maximum time: 01/01/3001 00:00:00 UTC |
|  | enumerated type | A list of items from which to select. |
|  | Boolean | A TRUE/FALSE value. |
|  | string | A series of text characters. |
|  | array | A collection of multiple pieces of data, each of which must be the same data type. The array icon shows the data type of the array's elements in square brackets and takes the color of that data type. As you add dimensions to the array, the thickness of the output wire increases. |
|  | cluster | A collection of multiple pieces of data, each of which can be a different data type. Cluster data types appear brown if all elements in the cluster are numeric or pink if any elements in the cluster are of non-numeric types. |
|  | error cluster | A cluster of information that specifies error conditions returned by a node. |
|  | path | The location of a file or directory. |
|  | waveform | A cluster of information that specifies an array of data, the start time at which the data was collected, and the change in time between each measurement. |
|  | digital waveform | A cluster of information that specifies a digital table of data, the start time at which the data was collected, and the change in time between each measurement. |
|  | reference number (refnum) | A unique identifier for an object, such as a file or a task. |
|  | variant | A generic container for all other types of data. |

Parent topic:

Programming in G

<!--NI_TOPIC bundle=labview-nxg-data-types path=enum-data.html language=enus -->
## TOPIC 00009: Enum Data

- bundle_id: `labview-nxg-data-types`
- source_path: `enum-data.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-types/raw/resource/enus/enum-data.html
- document_id: `labview-nxg-data-types`
- page_type: `leaf`
- content_type: `concept`
- source_description: The enumerated type, or enum, is a container for a finite set of user-named values. Each item in the set has both a string and a numeric value. On the diagram, an enum appears as a pull-down list of names represented as numeric data. You can use the named values to drive the logic of your program. F

Enum Data

The enumerated type, or enum, is a container for a finite set of user-named values. Each item in the set has both a string and a numeric value.

On the diagram, an enum appears as a pull-down list of names represented as numeric data.

You can use the named values to drive the logic of your program. For example, you can wire an enum constant or control to the selector of a Case Structure to create cases that correspond to each item in the enum.

[IMAGE alt='1378' src='GUID-480CCAEC-EEC7-4817-9025-D0FA36C8609B-a5.png']

You can use the numeric values within the enum for numeric calculations or comparisons. If you wire an enum control to a numeric node or indicator, the enum value is coerced to a numeric value. All arithmetic functions except Increment and Decrement treat enum data the same as an unsigned integer.

Parent topic:

Data Type Reference

<!--NI_TOPIC bundle=labview-nxg-data-types path=g-types.html language=enus -->
## TOPIC 00010: Type Definitions

- bundle_id: `labview-nxg-data-types`
- source_path: `g-types.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-types/raw/resource/enus/g-types.html
- document_id: `labview-nxg-data-types`
- page_type: `leaf`
- content_type: `concept`
- source_description: Type definitions are custom data types that you define using the G language and can reuse throughout your project. You define a type definition in a G Type document.

Type Definitions

*Type definitions* are custom data types that you define using the G
 language and can reuse throughout your project.

You define a type definition in a G Type document.

Parent topic:

Data Type Reference

Related tasks:

- Creating a Custom Data Type Using a G Type Document
- Updating Custom Data Type Instances Throughout Your Project

<!--NI_TOPIC bundle=labview-nxg-data-types path=numeric-conversion.html language=enus -->
## TOPIC 00011: Numeric Conversions

- bundle_id: `labview-nxg-data-types`
- source_path: `numeric-conversion.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-types/raw/resource/enus/numeric-conversion.html
- document_id: `labview-nxg-data-types`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you wire numeric data to a node that expects a different numeric data type, the node coerces the data to the most precise type. A red coercion dot appears on the node input where the coercion takes place. In the following diagram, a red coercion dot appears on the Add node because the node expe

Numeric Conversions

When you wire numeric data to a node that expects a different numeric data type, the node coerces the data to the most precise type.

A red coercion dot appears on the node input where the coercion takes place.

In the following diagram, a red coercion dot appears on the Add node because the node expects two inputs of matching numeric data types but receives a double-precision, floating-point number and an integer. Because input 0 (a double-precision, floating-point number) is more precise than input 1 (an unsigned, 32-bit integer), the node coerces input 1 to a double-precision, floating-point number.

[IMAGE alt='1378' src='GUID-2F0C60CB-5DCA-4733-9701-AEB3A56CE4C7-a5.png']

Parent topic:

Numeric Data

Related tasks:

- Addressing Issues with Numeric Conversions

<!--NI_TOPIC bundle=labview-nxg-data-types path=numeric-data.html language=enus -->
## TOPIC 00012: Numeric Data

- bundle_id: `labview-nxg-data-types`
- source_path: `numeric-data.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-types/raw/resource/enus/numeric-data.html
- document_id: `labview-nxg-data-types`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can program using a variety of numeric data types, each with different qualities and ranges. The differences among the numeric data types are the number of bits they use to store data and the data values they represent. The following table describes the differences among the numeric data types.

Numeric Data

You can program using a variety of numeric data types, each with different qualities and ranges. 
 The differences among the numeric data types are the number of bits they use to store data and the data values they represent.

The following table describes the differences among the numeric data types.

| Type | Description | Representation on the Diagram |
| --- | --- | --- |
| Integers | Represent whole numbers. Signed integers can be positive or negative. Use unsigned integers when you know the integer is always zero or positive. |  |
| Floating-Point Numbers | Represent fractional numbers. Double-precision floating-point numbers store more digits than single-precision floating-point numbers. |  |
| Complex Numbers | Represent a point in the complex numeric plane. Each value is comprised of two floating-point numbers, one representing the real part and the other representing the imaginary part. |  |

On the panel, you can use many types of controls and indicators to represent numeric values.

Parent topic:

Data Type Reference

<!--NI_TOPIC bundle=labview-nxg-data-types path=scan-string.html language=enus -->
## TOPIC 00013: Parsing a String into Smaller Pieces

- bundle_id: `labview-nxg-data-types`
- source_path: `scan-string.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-types/raw/resource/enus/scan-string.html
- document_id: `labview-nxg-data-types`
- page_type: `leaf`
- content_type: `task`
- source_description: Parsing a string into smaller pieces allows you to perform operations on individual words or groups of characters in the string. These words or groups of characters are often referred to as tokens. A token is defined as either the next set of characters that appears before a separator character, cal

Parsing a String into Smaller Pieces

Parsing a string into smaller pieces allows you to perform operations on individual words or groups of characters in the string. These words or groups of characters are often referred to as 
 *tokens*. A token is defined as either the next set of characters that appears before a separator character, called a 
 *delimiter*, or one of a specified set of operators.

#### What to Use

- Scan String for Tokens
- While Loop with shift registers

#### What to Do

Create the following diagram to parse a string into smaller pieces.

Customize the gray sections for your unique programming goals.

[IMAGE alt='1378' src='GUID-CA7A14D0-F1F0-4EA2-B485-28FB6A5B421F-a5.png']

|  | In order to identify all the tokens in a string, you must use a While Loop. Inside a While Loop, Scan String for Tokens scans the entire input string, returning all tokens it identifies until it reaches the end of the string. If you do not use Scan String for Tokens inside a While Loop, the node stops scanning as soon as it identifies the first token in a string and returns only that token. |
| --- | --- |
|  | The input string input of Scan String for Tokens contains the string to scan for tokens. |
|  | To start each scan at the location within the string where the preceding scan ended, pass the offset past token output of Scan String for Tokens through a shift register and back into the offset input of the same node. Initialize this shift register with the location within the string at which you want to begin parsing. Use 0 if you want Scan String for Tokens to begin its operation at the beginning of the string each time the program runs. |
|  | Add any strings that you want Scan String for Tokens to identify as tokens to the operators input array. The node identifies these strings as tokens even if they are not surrounded by any delimiters. |
|  | Detect the end of the input string by comparing the token index output of Scan String for Tokens to -2. |
|  | Use the auto-indexing output tunnel of the While Loop to collect the individual tokens in an array. This array contains all text that appears between delimiters as well as any strings specified in the operators input array that are found in the input string. Scan String for Tokens does not return delimiters as tokens but instead uses them to determine where tokens begin and end. |

#### Troubleshooting

- If Scan String for Tokens does not identify a token that you expect it to identify, check to make sure the operators input array does not contain regular expression notation or any invisible characters. Scan String for Tokens does not process regular expressions. Also check for correct capitalization of items in the operators input array, as scanning is case-sensitive.

#### Examples

| input string | operators | delimiters | token string | Comments |
| --- | --- | --- | --- | --- |
| 4>=0 | [>, =, >=] | \\s, \\t, \\r, \\n (default) | [4, >=, 0] | If a portion of the input string matches more than one defined operator, Scan String for Tokens chooses the longest match as a token. |
| a==b c!=d | [==, !=] | \\s, \\t, \\r, \\n (default) | [a, ==, b, c, !=, d] |  |
| G2 X0.5Y1.0 i0.5j0 z-0.05 | [X, Y, Z, i, j, z] | \\s, \\t, \\r, \\n (default) | [G2, X, 0.5, Y, 1.0, i, 0.5, j, 0, z, -0.05] | This is an example of a string of G-code, a language commonly used for machine control. This string describes a circle. |
| C1_1.11C2_2.22C3_3.33 | None | C, _ (add to delimiters array) \\s, \\t, \\r, \\n (default) | [1, 1.11, 2, 2.22, 3, 3.33] | This is an example of a string from a DAQ log with three channels. |

Parent topic:

String Data

<!--NI_TOPIC bundle=labview-nxg-data-types path=string-data.html language=enus -->
## TOPIC 00014: String Data

- bundle_id: `labview-nxg-data-types`
- source_path: `string-data.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-types/raw/resource/enus/string-data.html
- document_id: `labview-nxg-data-types`
- page_type: `leaf`
- content_type: `concept`
- source_description: Strings represent text. A string is a sequence of zero or more letters, numbers, and special characters. On the diagram, strings are represented by pink objects and wires. The string data type cannot represent binary data. For binary data, use an array of U8 integers. For text, use a string data typ

String Data

Strings represent text. A 
 *string* is a sequence of zero or more letters, numbers, and special characters. On the diagram, strings are represented by pink objects and wires.

[IMAGE alt='1378' src='GUID-F0800853-DCB1-45E9-A9B1-D6AB854B6906-a5.png']

The string data type cannot represent binary data. For binary data, use an array of U8 integers. For text, use a string data type. Casting any data type to a string may cause unexpected behavior when displaying or manipulating the string.

You can use built-in nodes to format, parse, and manipulate strings.

On the panel, strings appear as tables, text entry boxes, and labels.

Parent topic:

Data Type Reference

<!--NI_TOPIC bundle=labview-nxg-data-types path=two-dimensional-arrays.html language=enus -->
## TOPIC 00015: Two-Dimensional Arrays

- bundle_id: `labview-nxg-data-types`
- source_path: `two-dimensional-arrays.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-types/raw/resource/enus/two-dimensional-arrays.html
- document_id: `labview-nxg-data-types`
- page_type: `leaf`
- content_type: `concept`
- source_description: A two-dimensional (2D) array stores elements in a grid. It requires a column index and a row index to locate an element. 2D array controls and indicators have two index displays to navigate to specific indexes. Top index display—Controls the row index to display in the array control. Bottom index di

Two-Dimensional Arrays

A two-dimensional (2D) array stores elements in a grid. It requires a column index and a row index to locate an element.

[IMAGE alt='1378' src='GUID-A4FFDB53-70C7-42BE-9DE3-0A960631B06B-a5.png']

2D array controls and indicators have two index displays to navigate to specific indexes.

[IMAGE alt='1378' src='GUID-AF7CBC79-B871-4A95-B4A9-3BBBBD36F890-a5.png']

1. Top index display—Controls the row index to display in the array control.
2. Bottom index display—Controls the column index to display in the array control.
3. Element display—Values in the 2D array.

Parent topic:

Arrays

<!--NI_TOPIC bundle=labview-nxg-data-types path=updating-g-type-instances.html language=enus -->
## TOPIC 00016: Updating Custom Data Type Instances Throughout Your Project

- bundle_id: `labview-nxg-data-types`
- source_path: `updating-g-type-instances.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-types/raw/resource/enus/updating-g-type-instances.html
- document_id: `labview-nxg-data-types`
- page_type: `leaf`
- content_type: `task`
- source_description: Modify a G Type document to update all the instances of a custom data type in your project. Open the G Type document that defines the control you want to modify. You can right-click an instance of the type definition control or constant you want to modify and select Open Type Definition to open the

Updating Custom Data Type Instances Throughout Your Project

Modify a G Type document to update all the instances of a custom data type in your project.

1. Open the G Type document that defines the control you want to modify. 
 org.dita.html5/xsl/topic.xsl 455Tip You can right-click an instance
 of the type definition control or constant you want to modify and select
 Open Type Definition to open the associated G
 Type document. On the diagram, type definition controls and constants
 display a black marker on the left side to help you identify them.
2. In the G Type document, modify the control to your needs.
3. Save the G Type document to propagate the control updates to all instances of
 the type definition.

Parent topic:

Type Definitions

Related concepts:

- Type Definitions

Related tasks:

- Creating a Custom Data Type Using a G Type Document

<!--NI_TOPIC bundle=labview-nxg-data-types path=waveforms.html language=enus -->
## TOPIC 00017: Waveforms

- bundle_id: `labview-nxg-data-types`
- source_path: `waveforms.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-types/raw/resource/enus/waveforms.html
- document_id: `labview-nxg-data-types`
- page_type: `leaf`
- content_type: `concept`
- source_description: One common example of a cluster is the waveform. You might be familiar with the waveform data type if you have used it to collect data from a signal. On the diagram, waveform objects and wires appear brown. A waveform cluster is made up of three data types: a timestamp, an array of numerics, and a n

Waveforms

One common example of a cluster is the waveform. You might be familiar with the waveform data type if you have used it to collect data from a signal.

On the diagram, waveform objects and wires appear brown.

[IMAGE alt='1378' src='GUID-F70FC2E1-3D60-49DA-860C-772587780B72-a5.png']

A waveform cluster is made up of three data types: a timestamp, an array of numerics, and a numeric constant. You can use these three pieces of data to create a signal that you can plot on a chart or graph.

| Item | Details |
| --- | --- |
| t0 | Start time—A timestamp associated with the first measurement point in the waveform. |
| Y | Waveform data—An array of Y values associated with the waveform data. |
| dt | Delta t—The time interval in seconds between any two points in the signal. |

Because this data type is so common, you can access a waveform control from the palette on the panel, and you can access built-in nodes for waveforms from the palette on the diagram.

Parent topic:

Clusters: Building and Interacting with Grouped Data

<!--NI_TOPIC bundle=labview-nxg-data-types path=working-with-clusters.html language=enus -->
## TOPIC 00018: Clusters: Building and Interacting with Grouped Data

- bundle_id: `labview-nxg-data-types`
- source_path: `working-with-clusters.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-types/raw/resource/enus/working-with-clusters.html
- document_id: `labview-nxg-data-types`
- page_type: `leaf`
- content_type: `concept`
- source_description: Like elements of arrays, elements of a cluster are ordered. Unlike elements of arrays, the elements of a cluster are not ordered by their positions in the cluster but by the order in which the elements are added to the cluster. The first object you place in the cluster is element 0, the second is el

Clusters: Building and Interacting with Grouped Data

Like elements of arrays, elements of a cluster are ordered. Unlike elements of arrays, the elements of a cluster are not ordered by their positions in the cluster but by the order in which the elements are added to the cluster. The first object you place in the cluster is element 0, the second is element 1, and so on. You can verify the order of elements in a cluster and reorder them as desired.

A cluster groups data elements of mixed data types. Grouping related data
 elements into clusters allows you to keep them together while you program. For example,
 you can use a cluster to store a person's name, age, and whether the person is a student
 instead of storing this data in three separate controls.

The following images show Name,
 Age, and Student controls as
 individual elements versus the same controls in a single Census
 Cluster control.

| On the panel |  |
| --- | --- |
| On the diagram |  |

Parent topic:

Data Type Reference
