# NI DOCUMENT BUNDLE: g-web-development-api-ref

<!--NI_BUNDLE_CHUNK bundle=g-web-development-api-ref start=1 end=103 -->
<!--NI_TOPIC bundle=g-web-development-api-ref path=add.html language=enus -->
## TOPIC 00001: Add

- bundle_id: `g-web-development-api-ref`
- source_path: `add.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/add.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the sum of the inputs. You cannot add two timestamp values together. input An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, arrays of clusters of numbers, timestamps, or waveforms. Behavior with Timestamps You cannot add two timestamp values tog

Add

Computes the sum of the inputs.

You cannot add two timestamp values together.

[IMAGE alt='1378' src='Add.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### input

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, arrays of clusters of numbers, timestamps, or waveforms.

##### Behavior with Timestamps

You cannot add two timestamp values together. If you wire two timestamp values to this node, the code does not run.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

This input appears only when you wire a waveform to input.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### sum

The sum of the inputs.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

The node produces this output according to standard error behavior.

This output appears only when you wire a waveform to input.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=append-waveforms.html language=enus -->
## TOPIC 00002: Append Waveforms

- bundle_id: `g-web-development-api-ref`
- source_path: `append-waveforms.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/append-waveforms.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Appends a waveform to the end of another waveform. If the sampling rates of both waveforms do not match, the error cluster returns an error. This node ignores the trigger time of the second waveform. waveform A The first set of waveform data. waveform B The set of waveform data appended to the end o

Append Waveforms

Appends a waveform to the end of another waveform.

If the sampling rates of both waveforms do not match, the error cluster returns an error.

This node ignores the trigger time of the second waveform.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cmsdt.png']

##### waveform A

The first set of waveform data.

[IMAGE alt='datatype_icon' src='/assets/img/cmsdt.png']

##### waveform B

The set of waveform data appended to the end of waveform A.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Default value: No error

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/imsdt.png']

##### waveform out

The waveform that results from appending waveform B to waveform A.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

Analog Waveform Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=array-control.html language=enus -->
## TOPIC 00003: Array Controls

- bundle_id: `g-web-development-api-ref`
- source_path: `array-control.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/array-control.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Group data elements of the same type. Examples An example of a simple array is a 1D text array that lists the eight planets of our solar system in order. Array elements are ordered. An array uses an index so you can readily access any particular element. The index is zero-based, which means it is in

Array Controls

Group data elements of the same type.

[IMAGE alt='1378' src='GUID-68EA9307-F709-4754-8E3C-DCFCF3708706-a5.png']

#### Examples

An example of a simple array is a 1D text array that lists the eight planets of our solar
 system in order.

Array elements are ordered. An array uses an index so you can readily access any particular
 element. The index is zero-based, which means it is in the range 0 to n -
 1, where n is the number of elements in the array. For example,
 n = 8 for the eight planets, so the index ranges from 0 to 7. Earth is
 the third planet, so it has an index of 2.

#### What Is an Array?

An array consists of elements and dimensions. Elements are the data that make up the array.
 A dimension is the length, height, or depth of an array. An array can have one to 32
 dimensions and as many as (2<sup>31</sup>) - 1 elements per dimension, memory permitting.
 You can build arrays of numeric, Boolean, path, string, waveform, and cluster data types.
 Input arrays are classified as controls by default and allow users to input data into the
 control. Output arrays are classified as indicators by default and display data on the
 panel.

#### When Should I Use an Array?

Consider using arrays when you work with a collection of similar data and when you perform
 repetitive computations. Arrays are ideal for storing data you collect from waveforms or
 data generated in loops, where each iteration of a loop produces one element of the array.

#### How Do I Find an Array Element?

To locate a particular element in an array, you must use indexes. Each dimension in the
 array has an index. Indexes let you navigate through an array and retrieve elements, rows,
 columns, and pages from an array on the diagram.

Note

#### How Do I Create a Multidimensional
 Array?

Specify Dimensions on the Item tab to define
 the dimension or size of the array.

#### How Do I Manipulate Array Data?

- Extracting individual data elements from an
 array.
- Inserting, deleting, or replacing data
 elements in an array.
- Splitting arrays.

You can use the Build Array node or a loop to build an array
 programmatically.

<!--NI_TOPIC bundle=g-web-development-api-ref path=array-max-and-min.html language=enus -->
## TOPIC 00004: Array Max and Min

- bundle_id: `g-web-development-api-ref`
- source_path: `array-max-and-min.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/array-max-and-min.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum and minimum values found in an array, along with the indexes for each value. array An n-dimensional array of any type. This input also supports waveforms. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this input has a default data type that u

Array Max and Min

Returns the maximum and minimum values found in an array, along with the indexes for each value.

[IMAGE alt='1378' src='ArrayMaxAndMin.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### array

An 
n-dimensional array of any type. This input also supports waveforms.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### max value

Maximum value found in array.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### max index(es)

Index for the first max value.

If array is multidimensional, max index(es) is an array whose elements are the indexes for the first maximum value in array.

If array is empty, max index(es) and min index(es) are -1.

##### Data Type Changes Based on Input Array Dimension

The following table explains how the output data types change based on the dimension of the input array.

| Dimensions in a numeric array | max index(es) and min index(es) data type |
| --- | --- |
| 1 | scalar integers |
| More than 1 | 1D arrays that contain the indexes of the maximum and minimum values |

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### min value

Minimum value found in array.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### min index(es)

Index for the first min value.

If array is multidimensional, min index(es) is an array whose elements are the indexes for the first minimum value in array.

If array is empty, max index(es) and min index(es) are -1.

##### Data Type Changes Based on Input Array Dimension

The following table explains how the output data types change based on the dimension of the input array.

| Dimensions in a numeric array | max index(es) and min index(es) data type |
| --- | --- |
| 1 | scalar integers |
| More than 1 | 1D arrays that contain the indexes of the maximum and minimum values |

Parent topic:

Array Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=array-subset.html language=enus -->
## TOPIC 00005: Array Subset

- bundle_id: `g-web-development-api-ref`
- source_path: `array-subset.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/array-subset.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a portion of an array starting at a specified index and containing a specified number of elements. array An n-dimensional array of any type. This input also accepts clusters containing a single array, such as waveforms. This input changes to waveform when the data type is a waveform. Data Ty

Array Subset

Returns a portion of an array starting at a specified index and containing a specified number of elements.

[IMAGE alt='1378' src='ArraySubset.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### array

An 
n-dimensional array of any type.

This input also accepts clusters containing a single array, such as waveforms. This input changes to waveform when the data type is a waveform.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### index

First element, row, column, or page to include in the portion of array you want to return.

If index is less than 0, the node treats it as 0. If index is greater than or equal to the array size, the node returns an empty array.

##### Relationship between index Inputs and array Dimensions

For multidimensional arrays, index inputs correspond to row-major order. Thus, the first index corresponds last dimension of the array input, and the last index corresponds to the first dimension of the array input. The following table shows the relationship between four index inputs and the dimensions of a 4D array input.

| index Order | Corresponding Dimension in array Input | index Name |
| --- | --- | --- |
| 1 | 4th | volume index |
| 2 | 3rd | page index |
| 3 | 2nd | row index |
| 4 | 1st | column index |

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### waveform

The waveform whose array of y values you want to use in this operation. This input becomes available when you wire a waveform to array.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### length

The number of elements, rows, columns, or pages to include in the portion of array you want to return.

If index plus length is larger than the size of the array, the node returns only as much data as is available.

Default value: The length from index to the end of array.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### subarray

The portion of array starting at index and containing length elements. This output changes to waveform subset when the input data type is a waveform.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/imsdt.png']

##### waveform subset

Subset of the provided waveform based on the parameters you specify. This output is only available when the input data type is a waveform.

#### When to Use Index Array Instead of Array Subset

When you need to extract a subarray that is an entire row or column of the array input, use Index Array. To extract a subarray using Index Array, wire only index and length inputs for the dimension(s) you want to extract. For example, if the input to Index Array is a 2D array and you wire only the row input, you extract a complete 1D row of the array. If you wire only the column input, you extract a complete column of the array. If you wire the row input and the column input, you extract a single element of the array. Each input group is independent and can access any portion of any dimension of the array.

Parent topic:

Array Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=avogadro.html language=enus -->
## TOPIC 00006: Avogadro Constant

- bundle_id: `g-web-development-api-ref`
- source_path: `avogadro.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/avogadro.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value 6.022140857e23. The Avogadro constant is the number of constituent particles, usually atoms or molecules, that are contained in the amount of substance given by one mole.

Avogadro Constant

Returns the value 6.022140857e23. The Avogadro constant is the number of constituent particles, usually atoms or molecules, that are contained in the amount of substance given by one mole.

[IMAGE alt='1378' src='Literal.Numeric.Avogadro_Constant.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=g-web-development-api-ref path=axis-class.html language=enus -->
## TOPIC 00007: CartesianAxis

- bundle_id: `g-web-development-api-ref`
- source_path: `axis-class.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/axis-class.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the properties of the CartesianAxis class to read and write the elements of an axis.

CartesianAxis

Use the properties of the CartesianAxis class to read and write the elements of an
 axis.

RangeScale

Use the properties in the RangeScale class to read and write the elements of the uncolored scale.

Mapping

Mapping mode of the scale.

Range

Range of values, defined as a cluster. The range of values depends on the G Type of the control.

FitType

Autoscale type.

Parent topic:

RangeScale

<!--NI_TOPIC bundle=g-web-development-api-ref path=boolean-class.html language=enus -->
## TOPIC 00008: Boolean

- bundle_id: `g-web-development-api-ref`
- source_path: `boolean-class.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/boolean-class.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the properties in the Boolean class to read and write the elements of a Boolean.

Boolean

Use the properties in the Boolean class to read and write the elements of a Boolean.

Control

Use the properties in the Control class to read and write the elements of a control.

FalseColor

Color of the Boolean control when the Boolean value is False.

Text

Text displayed in the control. For switches and LED controls, this property reads and writes the text for the true and false states.

TrueColor

Color of the Boolean control when the Boolean value is True.

Checkbox

Use the properties in the Checkbox class to read and write the elements of a checkbox.

Parent topic:

Control

<!--NI_TOPIC bundle=g-web-development-api-ref path=boolean-truecolor.html language=enus -->
## TOPIC 00009: TrueColor

- bundle_id: `g-web-development-api-ref`
- source_path: `boolean-truecolor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/boolean-truecolor.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Color of the Boolean control when the Boolean value is True. If you use the Property Node to read the property of a control configured with gradient instead of a solid color, the Property Node returns an error.

TrueColor

Color
 of the Boolean control when the Boolean value is True.

If you use the Property Node to read the property of a
 control configured with gradient instead of a solid color, the Property Node returns
 an error.

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

Parent topic:

Boolean

<!--NI_TOPIC bundle=g-web-development-api-ref path=build-error-cluster.html language=enus -->
## TOPIC 00010: Build Error Cluster

- bundle_id: `g-web-development-api-ref`
- source_path: `build-error-cluster.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/build-error-cluster.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an error cluster that contains an error or warning with a description and location information. Use this node to return an error or warning that you define or to handle return values you receive from a shared library call. make warning A Boolean that specifies whether the error cluster built

Build Error Cluster

Creates an error cluster that contains an error or warning with a description and location information. Use this node to return an error or warning that you define or to handle return values you receive from a shared library call.

[IMAGE alt='1378' src='Build_Error_Cluster.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### make warning

A Boolean that specifies whether the error cluster built contains an error or a warning.

| True | Creates an error cluster that contains a warning. |
| --- | --- |
| False | Creates an error cluster that contains an error. |

Default value: False

##### Effect on Execution When You Change an Error to a Warning

Some nodes that halt execution when an error occurs will execute normally if you change an error to a warning.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### include call chain

A Boolean that specifies whether to include the call chain from the location at which the error or warning occurred to the top-level VI in the source string of the error cluster.

| True | Includes the call chain in the source string of the error cluster. |
| --- | --- |
| False | Only includes the calling VI in the source string of the error cluster. |

Default value: True

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

An error cluster that you use to check for errors or warnings that occur before this node executes. If error in contains an error or warning, this node ignores all other values and error out is error in unchanged.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### code

The error or warning code you want to write.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### description

The description for the code that appears in the error cluster.

description

##### Programming Patterns

Use Display Error or Generate Error Report to see the description that an error cluster contains.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

The error cluster created by this node.

error in

error out

error in

error out

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Error Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=checkbox-checkmarkcolor.html language=enus -->
## TOPIC 00011: CheckMarkColor

- bundle_id: `g-web-development-api-ref`
- source_path: `checkbox-checkmarkcolor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/checkbox-checkmarkcolor.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Color of the checkmark. If you use the Property Node to read the property of a control configured with gradient instead of a solid color, the Property Node returns an error.

CheckMarkColor

Color
 of the checkmark.

If you use the Property Node to read the property of a
 control configured with gradient instead of a solid color, the Property Node returns
 an error.

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

Parent topic:

Checkbox

<!--NI_TOPIC bundle=g-web-development-api-ref path=checkbox-class.html language=enus -->
## TOPIC 00012: Checkbox

- bundle_id: `g-web-development-api-ref`
- source_path: `checkbox-class.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/checkbox-class.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the properties in the Checkbox class to read and write the elements of a checkbox.

Checkbox

Use the properties in the Checkbox class to read and write the elements of a checkbox.

Boolean

Use the properties in the Boolean class to read and write the elements of a Boolean.

CheckMarkColor

Color of the checkmark.

Parent topic:

Boolean

<!--NI_TOPIC bundle=g-web-development-api-ref path=clear-error-cluster.html language=enus -->
## TOPIC 00013: Clear Error Cluster

- bundle_id: `g-web-development-api-ref`
- source_path: `clear-error-cluster.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/clear-error-cluster.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets an error cluster to no error. error in An error cluster that you use to check for errors or warnings. Standard Error Behavior error out An error cluster containing no errors. Standard Error Behavior

Clear Error Cluster

Resets an error cluster to no error.

[IMAGE alt='1378' src='Clear_Error_Cluster.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

An error cluster that you use to check for errors or warnings.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

An error cluster containing no errors.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Error Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=close-http-handle.html language=enus -->
## TOPIC 00014: Close HTTP Handle

- bundle_id: `g-web-development-api-ref`
- source_path: `close-http-handle.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/close-http-handle.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the client handle and deletes all stored cookies, authentication credentials, and HTTP headers associated with the client handle. This node also terminates all HTTP connections and logs out of any authentication, if applicable. client handle Unique value that identifies the web request. You c

Close HTTP Handle

Closes the client handle and deletes all stored cookies, authentication credentials, and HTTP headers associated with the client handle.
 This node also terminates all HTTP connections and logs out of any authentication, if applicable.

[IMAGE alt='1378' src='Close_HTTP_Handle.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### client handle

Unique value that identifies the web request.

You can use the same client handle to wire together multiple HTTP nodes to preserve authentication credentials, HTTP headers, and cookies.

Client handles are not required when making web requests without persistent data such as headers or credentials.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

HTTP Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=close-registry-key.html language=enus -->
## TOPIC 00015: Close Registry Key

- bundle_id: `g-web-development-api-ref`
- source_path: `close-registry-key.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/close-registry-key.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes a key in the Windows registry. Incorrectly modifying the registry can damage Windows or prevent you from starting Windows. reference Reference to the open registry key. error in Error conditions that occur before this node runs. Unlike most nodes, this node runs normally even if an error occu

Close Registry Key

Closes a key in the Windows registry.

Caution

[IMAGE alt='1378' src='Close_Registry_Key.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### reference

Reference to the open registry key.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: no error

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Registry Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=colorselector-class.html language=enus -->
## TOPIC 00016: ColorSelector

- bundle_id: `g-web-development-api-ref`
- source_path: `colorselector-class.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/colorselector-class.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the properties in the ColorSelector class to read and write the elements of a color selector.No properties are specific to this class.

ColorSelector

Use the properties in the ColorSelector class to read and write the elements of a color selector.No properties are specific to this class.

Control

Use the properties in the Control class to read and write the elements of a control.

Parent topic:

Control

<!--NI_TOPIC bundle=g-web-development-api-ref path=complex-to-polar.html language=enus -->
## TOPIC 00017: Complex to Polar

- bundle_id: `g-web-development-api-ref`
- source_path: `complex-to-polar.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/complex-to-polar.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the polar components of a complex number. Given z in rectangular form z = a + bi, this node converts the polar components of z=r*cos⁡(theta)+i r*sin⁡(theta)z=r*cos⁡(theta)+i r*sin⁡(theta) according to the following equations: r = | z | = a 2 + b 2 r = | z | = a 2 + b 2 theta = arg ⁡ ( z ) =

Complex to Polar

Returns the polar components of a complex number.

Given z in rectangular form z = a + b*i*, this node converts the polar components of

z

=

r

*

cos

⁡

(

theta

)

+

i

r

*

sin

⁡

(

theta

)

z

=

r

*

cos

⁡

(

theta

)

+

i

r

*

sin

⁡

(

theta

)

r

=

|

z

|

=

a

2

+

b

2

r

=

|

z

|

=

a

2

+

b

2

theta

=

arg

⁡

(

z

)

=

arctan

2

(

b

,

a

)

theta

=

arg

⁡

(

z

)

=

arctan

2

(

b

,

a

)

[IMAGE alt='1378' src='ComplexToPolar.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccdb.png']

##### z

The complex number.

This input supports complex numbers, clusters of complex numbers, arrays of complex numbers, arrays of clusters of complex numbers, and waveforms.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### r

The distance from the origin to the point, z.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### theta

The angle for the line, r, from the origin to the point, z, in radians.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

Parent topic:

Numeric Nodes

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=complex-to-real-imaginary.html language=enus -->
## TOPIC 00018: Complex to Real and Imaginary

- bundle_id: `g-web-development-api-ref`
- source_path: `complex-to-real-imaginary.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/complex-to-real-imaginary.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the rectangular components of a complex number. x + yi A complex number. This input supports complex numbers, arrays or clusters of complex numbers, arrays of clusters of complex numbers, and waveforms. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this

Complex to Real and Imaginary

Returns the rectangular components of a complex number.

[IMAGE alt='1378' src='ComplexToRealAndImaginary.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccdb.png']

##### x + yi

A complex number.

This input supports complex numbers, arrays or clusters of complex numbers, arrays of clusters of complex numbers, and waveforms.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### x

The x rectangular component of x + yi.

x

x + yi

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### y

The y rectangular component of x + yi.

y

x + yi

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=concatenate-strings.html language=enus -->
## TOPIC 00019: Concatenate Strings

- bundle_id: `g-web-development-api-ref`
- source_path: `concatenate-strings.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/concatenate-strings.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Concatenates input strings and/or 1D arrays of strings into a single output string. For array inputs, this node concatenates each element of the array. string String you want to concatenate. concatenated string The concatenated input strings in the order you wire them to the node from top to bottom.

Concatenate Strings

Concatenates input strings and/or 1D arrays of strings into a single output string.
 For array inputs, this node concatenates each element of the array.

[IMAGE alt='1378' src='ConcatenateStrings.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### string

String you want to concatenate.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### concatenated string

The concatenated input strings in the order you wire them to the node from top to bottom.

Parent topic:

String Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=control-value.html language=enus -->
## TOPIC 00020: Value

- bundle_id: `g-web-development-api-ref`
- source_path: `control-value.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/control-value.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Data value of this control. The data type of this property depends on the data type of the control.

Value

Data value of this control.

The data type of this property depends on the data type of the control.

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

Parent topic:

Control

<!--NI_TOPIC bundle=g-web-development-api-ref path=control-valuesignaling.html language=enus -->
## TOPIC 00021: ValueSignaling

- bundle_id: `g-web-development-api-ref`
- source_path: `control-valuesignaling.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/control-valuesignaling.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the data value of the control and generates an event. This property is similar to the Value property and also generates an event as if the user had interactively changed the value of the object. Use this property only when you rely on the node to generate an event in response to the programmati

ValueSignaling

Sets the data value of the control and generates an event. This property is similar to the Value property and also generates an event as if the user had interactively changed the value of the object. Use this property only when you rely on the node to generate an event in response to the programmatic value change.

The data type of this property depends on the data type of the control.

**Permissions:** Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

Parent topic:

Control

<!--NI_TOPIC bundle=g-web-development-api-ref path=conversion-nodes.html language=enus -->
## TOPIC 00022: Conversion Nodes

- bundle_id: `g-web-development-api-ref`
- source_path: `conversion-nodes.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/conversion-nodes.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`

Conversion Nodes

Array to Cluster

Converts a 1D array to a cluster of elements of the same type as the array elements.

Boolean Array to Number

Converts a Boolean array to an integer by interpreting the array as the binary representation of the number.

Boolean to Integer

Converts a Boolean False or True value to a 16-bit integer with a value of 0 or 1, respectively.

Byte Array To String

Converts an array of unsigned bytes representing encoded characters into a string using the encoding you specify.

Cluster to Array

Converts a cluster of elements of the same data type to a 1D array.

Date and Time to Timestamp

Creates a timestamp from a set of individual values that specify a date and time.

Decimal String to Number

Converts the numeric characters in a string to a decimal integer.

Flatten To JSON

Converts data to a UTF-8 JavaScript Object Notation (JSON) string.

Floating Point String to Number

Converts the characters 0 through 9, plus, minus, e, E, and the decimal point (usually period) in a string to a floating-point number.

Format into String

Inserts input data into specified locations in a string and formats that data according to your specifications.

Format Date and Time String

Converts a timestamp or numeric value into a string that displays the corresponding time.

Hexadecimal String to Number

0

9

A

F

a

f

Number of Waveform Samples

Returns the number of data elements in the waveform. You must manually select the polymorphic instance you want to use.

Number to Boolean Array

Converts an integer to a Boolean array.

Number to Decimal String

Converts a numeric value to a string that shows the number's decimal format.

Number to Engineering String

Converts a numeric value to a string that shows the number's engineering format.

Number to Exponential String

Converts a numeric value to a string in E-format (exponential notation).

Number to Fractional String

Converts a numeric value to an F-format (fractional notation), floating-point string.

Number to Hexadecimal String

Converts a numeric value to a string that shows the number's hexadecimal format.

Number to Octal String

Converts a numeric value to a string that shows the number's octal format.

Octal String to Number

Converts the characters 0 through 7 in a string to an octal integer.

Scan from String

Scans a string for text that matches a specified format and returns the matches as the data type you specify.

String To Byte Array

Converts a string into an array of unsigned bytes.

Timestamp to Date and Time

Converts a timestamp or a number of seconds to a set of individual values that represent a date and time.

To Double Precision Complex

Converts a number to a double-precision, complex number.

To Double Precision Float

Converts a number to a double-precision, floating-point number.

To Signed 8-bit Integer

Converts a number to an 8-bit integer in the range -128 to 127.

To Signed 16-bit Integer

Converts a number to a 16-bit integer in the range -32,768 to 32,767.

To Signed 32-bit Integer

31

31

To Signed 64-bit Integer

63

63

To Single Precision Complex

Converts a number to a single-precision, complex number.

To Single Precision Float

Converts a number to a single-precision, floating-point number.

To Timestamp

Creates a timestamp for the date and time represented by a specified number of seconds since 12:00 a.m., January 1, 1904, Universal Time.

To Unsigned 8-bit Integer

Converts a number to an 8-bit unsigned integer in the range 0 to 255.

To Unsigned 16-bit Integer

Converts a number to a 16-bit unsigned integer in the range 0 to 65,535.

To Unsigned 32-bit Integer

Converts a number to a 32-bit unsigned integer in the range 0 to (2^32)-1.

To Unsigned 64-bit Integer

Converts a number to a 64-bit unsigned integer in the range 0 to (2^64)-1.

To Variant

Converts any data to variant data.

Unflatten from JSON

Converts a UTF-8 JavaScript Object Notation (JSON) string to another data type.

Variant To Data

Converts variant data to the data type that you specify so that you can display or process the data.

<!--NI_TOPIC bundle=g-web-development-api-ref path=create-registry-key.html language=enus -->
## TOPIC 00023: Create Registry Key

- bundle_id: `g-web-development-api-ref`
- source_path: `create-registry-key.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/create-registry-key.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a key in the Windows registry or opens the key, if it already exists. Incorrectly modifying the registry can damage Windows or prevent you from starting Windows. machine Name of the networked machine. Default value: Empty — The local machine. options Special options for the key. REG_OPTION_N

Create Registry Key

Creates a key in the Windows registry or opens the key, if it already exists.

Caution

[IMAGE alt='1378' src='Create_Registry_Key.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### machine

Name of the networked machine.

Default value: Empty — The local machine.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### options

Special options for the key.

| REG_OPTION_NON_VOLATILE | This node creates the key as non-volatile and preserves the information stored in memory when the OS is restarted. |
| --- | --- |
| REG_OPTION_VOLATILE | This node creates the key as volatile and does not preserve the information stored in memory when the corresponding registry hive is unloaded. |
| REG_OPTION_BACKUP_RESTORE | This node creates the key with access to backing up and restoring the key. |

Default value: REG_OPTION_NON_VOLATILE

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### root key

Windows registry root key.

| HKEY_CLASSES_ROOT | Contains information about registered applications. |
| --- | --- |
| HKEY_CURRENT_USER | Stores settings that are specific to the currently logged-in user. |
| HKEY_LOCAL_MACHINE | Stores settings that are specific to the local computer. |
| HKEY_USERS | Contains subkeys corresponding to the HKEY_CURRENT_USER keys for each user profile actively loaded on the machine. |
| HKEY_PERFORMANCE_DATA | Provides runtime information into performance data provided by either the Windows NT kernel, or running system drivers, programs and services. |
| HKEY_CURRENT_CONFIG | Contains information gathered at runtime. |
| HKEY_DYN_DATA | Contains information about hardware devices. This key is used only on Windows 95, Windows 98 and Windows ME. |

Default value: HKEY_LOCAL_MACHINE

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### subkey

Name of a subkey of root key.

A beginning backslash 
 \ might cause an error.

Default value: Empty string

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### security access mask

Access rights to assign the key.

| KEY_QUERY_VALUE | Access right to query the values of a registry key. |
| --- | --- |
| KEY_SET_VALUE | Access right to create, delete, or set a registry value. |
| KEY_CREATE_SUB_KEY | Access right to create a subkey of a registry key. |
| KEY_ENUMERATE_SUB_KEYS | Access right to enumerate the subkeys of a registry key. |
| KEY_NOTIFY | Access right to request change notifications for a registry key or for subkeys of a registry key. |
| KEY_CREATE_LINK | Access right reserved for system use. |
| KEY_READ | Access right that combines the STANDARD_RIGHTS_READ, KEY_QUERY_VALUE, KEY_ENUMERATE_SUB_KEYS, and KEY_NOTIFY values. |
| KEY_WRITE | Access right that combines the STANDARD_RIGHTS_WRITE, KEY_SET_VALUE, and KEY_CREATE_SUB_KEY values. |
| KEY_ALL_ACCESS | Access right that combines the STANDARD_RIGHTS_REQUIRED, KEY_QUERY_VALUE, KEY_SET_VALUE, KEY_CREATE_SUB_KEY, KEY_ENUMERATE_SUB_KEYS, KEY_NOTIFY, and KEY_CREATE_LINK values. |
| KEY_READ \| KEY_WRITE | Access right that combines the KEY_READ and KEY_WRITE values. |

Default value: KEY_READ | KEY_WRITE

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### class

Class or object type of the key.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### registry view

Value that specifies whether to create a 32-bit key or a 64-bit key on a 64-bit operating system.

| Default | 0 | This node selects the type of key based on the software that is installed. For example, if a 64-bit product is installed, this node creates a 64-bit key. |
| --- | --- | --- |
| KEY_WOW64_64KEY | 8 | This node creates a 64-bit key. |
| KEY_WOW64_32KEY | 9 | This node creates a 32-bit key. |

Default value: Default

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### reference

Reference to the open registry key.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### action taken

Action taken by the node.

| Unknown | The action taken is unknown. |
| --- | --- |
| REG_CREATED_NEW_KEY | This node created a new key. |
| REG_OPENED_EXISTING_KEY | This node opened an existing key. |

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Registry Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=ctrlprop-disabledindexes.html language=enus -->
## TOPIC 00024: DisabledIndexes

- bundle_id: `g-web-development-api-ref`
- source_path: `ctrlprop-disabledindexes.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/ctrlprop-disabledindexes.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Array of indexes to disable. When you remove an item, G Web Development Software clears disabled item indexes that are out of range.

DisabledIndexes

Array of indexes to disable. When you remove an item, G Web Development Software
 clears disabled item indexes that are out of range.

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

Parent topic:

ComboBox

Parent topic:

Enum

Parent topic:

ListBox

Parent topic:

RadioButtonGroup

Parent topic:

Ring

<!--NI_TOPIC bundle=g-web-development-api-ref path=ctrlprop-text.html language=enus -->
## TOPIC 00025: Text

- bundle_id: `g-web-development-api-ref`
- source_path: `ctrlprop-text.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/ctrlprop-text.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Text displayed in the control. For switches and LED controls, this property reads and writes the text for the true and false states.

Text

Text displayed in the control. For switches and LED controls, this property reads and writes the text for the true and false states.

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

Parent topic:

Boolean

Parent topic:

Text

<!--NI_TOPIC bundle=g-web-development-api-ref path=delete-variant-attribute.html language=enus -->
## TOPIC 00026: Delete Variant Attribute

- bundle_id: `g-web-development-api-ref`
- source_path: `delete-variant-attribute.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/delete-variant-attribute.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes either a single variant attribute or all variant attributes. variant in The variant data for which you want to delete one or all attributes. name The name of the attribute you want to delete. If name matches an attribute, this node deletes the attribute and its value. If name is an empty str

Delete Variant Attribute

Deletes either a single variant attribute or all variant attributes.

[IMAGE alt='1378' src='DeleteVariantAttribute.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cfxdt.png']

##### variant in

The variant data for which you want to delete one or all attributes.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### name

The name of the attribute you want to delete. If name
 matches an attribute, this node deletes the attribute and its value. If
 name is an empty string, this node deletes all attributes in the
 variant data.

Default value: all attributes

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ifxdt.png']

##### variant out

The variant data with the deleted attribute(s).

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### found?

A Boolean value that indicates whether the node found the attribute that is specified in name.

| True | The node found the attribute specified in name. If name is unwired, the node located and deleted all attributes. |
| --- | --- |
| False | The node did not find the attribute specified in name. If name is unwired, the node found no attributes. |

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Variant Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=digital-waveform-t0.html language=enus -->
## TOPIC 00027: t0

- bundle_id: `g-web-development-api-ref`
- source_path: `digital-waveform-t0.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/digital-waveform-t0.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Start time of the waveform.

t0

Start time of the waveform.

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

Parent topic:

Digital Waveform

<!--NI_TOPIC bundle=g-web-development-api-ref path=enum-class.html language=enus -->
## TOPIC 00028: Enum

- bundle_id: `g-web-development-api-ref`
- source_path: `enum-class.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/enum-class.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the properties in the Enum class to read and write the elements of an enum selector.

Enum

Use the properties in the Enum class to read and write the elements of an enum selector.

Control

Use the properties in the Control class to read and write the elements of a control.

DisabledIndexes

Array of indexes to disable. When you remove an item, G Web Development Software clears disabled item indexes that are out of range.

Parent topic:

Control

<!--NI_TOPIC bundle=g-web-development-api-ref path=enum-registry-values-simple.html language=enus -->
## TOPIC 00029: Enum Registry Values Simple

- bundle_id: `g-web-development-api-ref`
- source_path: `enum-registry-values-simple.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/enum-registry-values-simple.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enumerates the values for a specific key or subkey. Incorrectly modifying the registry can damage Windows or prevent you from starting Windows. reference in Reference to the open registry key. retrieve data A Boolean that determines whether this node retrieves data and data types. True Retrieves dat

Enum Registry Values Simple

Enumerates the values for a specific key or subkey.

Caution

[IMAGE alt='1378' src='Enum_Registry_Values_Simple.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### reference in

Reference to the open registry key.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### retrieve data

A Boolean that determines whether this node retrieves data and data types.

| True | Retrieves data and data types. The node also returns DWORD data and string/binary data in addition to values and simple data types. |
| --- | --- |
| False | Does not retrieve data and data types. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### value info

Set of parameters describing the set of values and data.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### numValues

Number of values under the key specified by hKey.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### maxValueNameLen

Length of the longest value name under the key specified by hKey.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### maxValueDataLen

Length of the longest datum under the key specified by hKey.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/i1du32.png']

##### DWORD data

An array of data of Windows registry type 
DWORD.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### reference out

Reference to the open registry key.

[IMAGE alt='datatype_icon' src='/assets/img/i1dstr.png']

##### values

An array of value names.

[IMAGE alt='datatype_icon' src='/assets/img/i1du16.png']

##### simple data types

An array of simplified Windows registry data types.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/i1dstr.png']

##### string/binary data

An array of data of Windows registry type 
String or 
Binary .

#### Programming Patterns

You can wire the value info output of the Query Registry Key Info node to the Enum Registry Values Simple node to get the value information of a specific key or subkey.

Parent topic:

Registry Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=equal.html language=enus -->
## TOPIC 00030: Equal?

- bundle_id: `g-web-development-api-ref`
- source_path: `equal.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/equal.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Compares two values and returns True only if the values are equal to each other. This node can also compare an array or cluster of a data type to a scalar of the same data type and produce an array or cluster of Boolean values. x First value to compare. x must be either the same type as y or compose

Equal?

Compares two values and returns True only if the values are equal to each other.

This node can also compare an array or cluster of a data type to a scalar of the same data type and produce an array or cluster of Boolean values.

[IMAGE alt='1378' src='IsEqual.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

First value to compare. x must be either the same type as y or composed of the same type as y.

This input supports all data types.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### y

Second value to compare. y must be either the same type as x or composed of the same type as x.

This input supports all data types.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### x = y?

Boolean result of the operation.

When you compare two arrays, x = y? is a scalar in 
 Compare Aggregates mode and a Boolean array in 
 Compare Elements mode (default).

#### Behavior for 
 NaN Inputs

If at least one input is 
 NaN (not a number), this node returns FALSE. To compare inputs with a value of 
 NaN, use Not a Number/Path/Refnum?.

Parent topic:

Comparison Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=first-call.html language=enus -->
## TOPIC 00031: First Call?

- bundle_id: `g-web-development-api-ref`
- source_path: `first-call.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/first-call.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the diagram or subdiagram containing this node is running for the first time since the top-level caller began execution. You can place First Call? in multiple locations within a program, such as the diagram of a VI, a subdiagram of a Case Structure, inside a loop, or the diagram of

First Call?

Indicates whether the diagram or subdiagram containing this node is running for the first time since the top-level caller began execution.

You can place First Call? in multiple locations within a program, such as the diagram of a VI, a subdiagram of a Case Structure, inside a loop, or the diagram of a subVI.

[IMAGE alt='1378' src='IsFirstCall.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### First Call?

A Boolean value that indicates whether the diagram or subdiagram containing this node is running for the first time since the top-level caller began execution.

| True | This is the first time the diagram or subdiagram is running since the program began execution. |
| --- | --- |
| False | This is not the first time the diagram or subdiagram is running since the program began execution. |

#### Behavior for Multiple Top-Level Callers

First Call? returns True the first time the calling diagram or subdiagram runs after the first top-level calling VI starts running, such as when you click the 
 Run button. If a second top-level caller calls the diagram or subdiagram while the first top-level caller is still running, First Call? does not return True a second time. After all the top-level callers become idle and a top-level caller starts again, First Call? returns True the first time the VI runs after the idle state.

#### Behavior with Reentrant VIs

A stateless reentrant VI has one instance of the VI per caller at compile time. Therefore, First Call? in a stateless reentrant VI returns True the first time a top-level caller calls each instance of the VI.

Note

First Call?

Parent topic:

Program Flow Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=flatten-to-json.html language=enus -->
## TOPIC 00032: Flatten To JSON

- bundle_id: `g-web-development-api-ref`
- source_path: `flatten-to-json.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/flatten-to-json.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts data to a UTF-8 JavaScript Object Notation (JSON) string. enable LabVIEW extensions A Boolean that determines whether JSON extensions support NaN and Inf values of floating-point numbers. Not all JSON parsers support these extensions. True Enable JSON extension support of NaN and Inf values

Flatten To JSON

Converts data to a UTF-8 JavaScript Object Notation (JSON) string.

[IMAGE alt='1378' src='FlattenToJson.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### enable LabVIEW extensions

A Boolean that determines whether JSON extensions support 
NaN and 
Inf values of floating-point numbers. Not all JSON parsers support these extensions.

| True | Enable JSON extension support of NaN and Inf values of floating-point numbers. |
| --- | --- |
| False | Disable JSON extension support of NaN and Inf values of floating-point numbers. |

Default value: True

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### anything

The data you want to convert to a UTF-8 JSON string. This input accepts arrays and clusters of Booleans, floating-point numbers, and strings. anything can also accept an array of clusters, or a cluster of arrays, of these data types. This input does not support other data types, such as enums, refnums, file paths, and fixed-point numbers. Cluster elements may be named or unnamed, but not a combination of both. If cluster elements are named, then each name must be unique to that cluster.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### JSON string

The flattened data encoded in UTF-8. UTF-8 encoded strings may not display correctly.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=get-queue-status.html language=enus -->
## TOPIC 00033: Get Queue Status

- bundle_id: `g-web-development-api-ref`
- source_path: `get-queue-status.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/get-queue-status.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns information about the current state of a queue, such as the number of elements currently in the queue. Using this node in parallel code may result in race conditions. To avoid race conditions, use this node only for monitoring and not for controlling code. queue A reference to a queue. retur

Get Queue Status

Returns information about the current state of a queue, such as the number of elements currently in the queue.

Using this node in parallel code may result in race conditions. To avoid race conditions, use this node only for monitoring and not for controlling code.

[IMAGE alt='1378' src='GetQueueStatus.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### queue

A reference to a queue.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### return elements

A Boolean value that determines whether to return the elements in the queue.

| True | This node returns the elements in the queue. |
| --- | --- |
| False | This node does not return the elements in the queue. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: no error

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### max queue size

The maximum number of elements the queue can contain.

If max queue size is -1, the queue can contain an unlimited number of elements.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### queue name

The name of the queue, if the queue is named.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### queue out

Reference to the queue.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### number pending remove

The number of Dequeue Element or Preview Queue Element nodes currently waiting to remove an element from the queue.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### number pending insert

The number of Enqueue Element or Enqueue Element at Opposite End nodes currently waiting to insert an element in the queue.

If the maximum queue size is 
 -1, this output returns 
 0.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### number elements in queue

Current number of elements in the queue.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### elements

An array of all the elements currently in the queue.

If return elements? is set to False, this output returns an empty array.

The data type of the array elements changes to match the data type of the queue elements.

#### Programming Patterns

Transferring Data Between Loops Using Queue Nodes

#### Verifying Valid Queue References

You can use Get Queue Status to verify that a queue reference is valid. If a queue reference is not valid, this node returns error code 
 1.

Parent topic:

Queue Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=get-xy-value.html language=enus -->
## TOPIC 00034: Get XY Value

- bundle_id: `g-web-development-api-ref`
- source_path: `get-xy-value.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/get-xy-value.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the X and Y value of a waveform or digital data set. waveform Waveform from which to retrieve a specified data value (X and Y value). This input accepts a waveform or a digital waveform. This input is available when you wire a waveform or digital waveform to digital data in. If you wire a di

Get XY Value

Returns the X and Y value of a waveform or digital data set.

[IMAGE alt='1378' src='WDT_Get_XY_Value_DBL.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cmsdt.png']

##### waveform

Waveform from which to retrieve a specified data value (X and Y value).

This input accepts a waveform or a digital waveform.

This input is available when you wire a waveform or digital waveform to digital data in. If you wire a digital table to waveform in, this input changes to digital data in.

[IMAGE alt='datatype_icon' src='/assets/img/cdigtbl.png']

##### digital data

Digital table for which you want to retrieve the X and Y values.

This input is available when you wire a digital table to waveform. If you wire a waveform or digital waveform to digital data, this input changes to waveform.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### Y position format

Data value of the specified element or at a specified time.

This input is available when you wire a waveform or digital waveform to digital data in. If you wire a digital table to waveform in, this input changes to start.

| Samples | 0 | Data value of the specified sample in the waveform data. |
| --- | --- | --- |
| Relative Time | 1 | Data value at a specified time relative to the first point in the waveform. |

Default value: Samples

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### start

Data element or time value where you want to start acquiring X and Y values.

This input is available when you wire a digital table to waveform in. If you wire a waveform or digital waveform to digital data in, this input changes to Y position format.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### Y position

Element number you want from the set of waveform data or the value at a specified time.

For example, if you want the value of the 200th scan, wire 
 199 to this input. If you want the value at time 100, wire 
 100 to this input. You specify whether this input operates based on samples or relative time in Y position format.

In Relative Time mode, this node determines whether the value wired to this input is an integer multiple of 
 dt. If the value is not an integer multiple of 
 dt, the node uses the closest exact multiple of 
 dt.

This input is available when you wire a waveform or digital waveform to digital data in. If you wire a digital table to waveform in, this input is not available.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### X value

Timestamp that captures the X value of the waveform at the location or time you specify.

This output is available when you wire a waveform or digital waveform to digital data in. If you wire a digital table to waveform in, this output changes to compressed index.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### compressed index

Index of the data element or time value with respect to the compressed waveform.

For example, if the actual sample number is 8 but the sample is compressed in a portion of the waveform that starts at 3, the compressed index is 3.

This output is available when you wire a digital table to waveform in. If you wire a waveform or digital waveform to digital data in, this output changes to X value.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### actual Y position

Index or time value of the point this node returns.

This output is available when you wire a waveform or digital waveform to digital data in. If you wire a digital table to waveform in, this output changes to sample number.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### sample number

Sample number of the data element or time value. If the value of start is inside a compressed portion of the waveform, this node calculates the sample number as if the waveform were not compressed.

This output is available when you wire a digital table to waveform in. If you wire a waveform or digital waveform to digital data out, this output changes to actual Y position.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### Y value

Integer that captures the Y value of the waveform at the location you specify.

This output is an integer array of Y values when you wire a digital waveform to waveform in.

This output is available when you wire a waveform or digital waveform to digital data in. If you wire a digital table to waveform in, this output changes to digital value.

[IMAGE alt='datatype_icon' src='/assets/img/i1du8.png']

##### digital value

Integer array of Y values.

This output is available when you wire a digital table to waveform in. If you wire a waveform or digital waveform to digital data in, this output changes to Y value.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/idigwfm.png']

##### waveform data value

Values of the digital waveform data.

This output is available when you wire a digital waveform to waveform in or digital data in. If you wire a digital table to waveform in or digital data in, this output changes to digital data value. If you wire an analog waveform to waveform in or digital data in, this output is not available.

[IMAGE alt='datatype_icon' src='/assets/img/idigtbl.png']

##### digital data value

Values of the digital data.

This output is available when you wire a digital table to waveform in. If you wire a digital waveform to waveform in or digital data in, this output changes to digital waveform value. If you wire a waveform to waveform in or digital data in, this output is not available.

Parent topic:

Waveform Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=get.html language=enus -->
## TOPIC 00035: GET

- bundle_id: `g-web-development-api-ref`
- source_path: `get.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/get.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a web request that returns header and body data from a server, web page, or web service. This node uses the GET HTTP method and does not submit any data to the server. output file File where you can save body data returned by the server. If you do not specify an output file, the node does not

GET

Sends a web request that returns header and body data from a server, web page, or web service.
 This node uses the GET HTTP method and does not submit any data to the server.

[IMAGE alt='1378' src='GET.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cpath.png']

##### output file

File where you can save body data returned by the server. If you do not specify an output file, the node does not save the body data to a file.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### client handle

Unique value that identifies the web request. You can use the same client handle to wire together multiple HTTP nodes to preserve authentication credentials, HTTP headers, and cookies. Client handles are not required when making independent web requests without persistent data such as headers or credentials.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### url

URL of the server, web page, or web service where this node will send the web request.

##### Relative URL behavior

If you do not specify a URL scheme on a Web Server target, each URL you enter is relative to the location the WebVI is hosted. The WebVI sends HTTP requests to the server at the relative URL. For example, if you host the WebVI on http://website.com/MyApp/, specifying the relative URL 
 subdirectory/myfile.txt sends an HTTP request to http://website.com/MyApp/subdirectory/myfile.txt.

If you do not specify a URL scheme on a non-Web Server target, the node prefixes http:// to the URL and treats it as an absolute URL.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### timeout

Amount of time in milliseconds the node has to wait for a response from the server before the web request times out. A value of -1 defers timeout monitoring to the operating system.

Default value: 10000 ms

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### status code

Status code information returned by the server.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### client handle out

Unique value that identifies the web request. Use this value to refer to this web request in subsequent node calls.

You can use the same client handle to wire together multiple HTTP nodes to preserve authentication credentials, HTTP headers, and cookies.

Client handles are not required when making independent web requests without persistent data such as headers or credentials.

[IMAGE alt='datatype_icon' src='/assets/img/i1dstr.png']

##### headers

Header fields returned by the server. Refer to the World Wide Web Consortium website at [www.w3.org](http://digital.ni.com/express.nsf/bycode/exctg8) for more information about header field definitions including available headers, descriptions, and syntax.

[IMAGE alt='datatype_icon' src='/assets/img/i1dstr.png']

##### body

The body data contained in the server, web page, or web service.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### CORS Restrictions on HTTP Requests

Requests from HTTP clients are subject to CORS restrictions when the WebVI communicates with a web service on a different origin. The web service responding to the HTTP request must return a valid CORS configuration for the HTTP request to complete successfully.

On non-Web Server targets, HTTP requests are not subject to CORS restrictions. The VI can make HTTP requests regardless of the CORS configuration of the server.

Note

#### Cached Response Behavior for Repeat Requests

HTTP nodes on a Web Server target may create caches of responses to HTTP requests. If a duplicate request occurs, the HTTP nodes can avoid querying the network by returning a previous response from the cache. The specific browser environment and server configuration determine the behavior of the cache.

On non-Web Server targets, every HTTP request creates a unique network request.

#### Forbidden Headers on a Web Server

A WebVI cannot transmit or receive specific 
 [forbidden headers](https://developer.mozilla.org/en-us/docs/glossary/forbidden_header_name) in HTTP requests. For header transmissions, the request to the server does not include forbidden headers. When the HTTP nodes receive a forbidden header from a server, they exclude the header from the headers output. Additionally, the CORS configuration of a server may exclude some headers in server requests or from server responses.

On non-Web Server targets, you do not need to account for forbidden headers in HTTP requests.

Parent topic:

HTTP Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=gobject-totalbounds.html language=enus -->
## TOPIC 00036: TotalBounds

- bundle_id: `g-web-development-api-ref`
- source_path: `gobject-totalbounds.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/gobject-totalbounds.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Coordinates of all sides of the control including label, caption, and other visible parts connected to the control. The coordinates are relative to the parent object, such as the owning pane of a control. An error occurs if you use the Property Node to read the property of a control inside a flexibl

TotalBounds

Coordinates of all sides of the control including label, caption, and other
 visible parts connected to the control. The coordinates are relative to the parent
 object, such as the owning pane of a control.

An error occurs if you use the Property Node to read the property
 of a control inside a flexible layout container of a WebVI.

**Permissions:** Read

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

Parent topic:

GObject

<!--NI_TOPIC bundle=g-web-development-api-ref path=gobject-visible.html language=enus -->
## TOPIC 00037: Visible

- bundle_id: `g-web-development-api-ref`
- source_path: `gobject-visible.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/gobject-visible.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Boolean value that determines whether to display the object.

Visible

Boolean value that determines whether to display the object.

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

Parent topic:

GObject

Parent topic:

PlotBase

Parent topic:

NumericScale

Parent topic:

TabItem

<!--NI_TOPIC bundle=g-web-development-api-ref path=greater.html language=enus -->
## TOPIC 00038: Greater?

- bundle_id: `g-web-development-api-ref`
- source_path: `greater.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/greater.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Compares two values and returns True only if the first value is greater than the second value. This node can also compare an array or cluster of a data type to a scalar of the same data type and produce an array or cluster of Boolean values. x First value to compare. x must be either the same type a

Greater?

Compares two values and returns True only if the first value is greater than the second value.

This node can also compare an array or cluster of a data type to a scalar of the same data type and produce an array or cluster of Boolean values.

[IMAGE alt='1378' src='IsGreater.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

First value to compare. x must be either the same type as y or composed of the same type as y.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### y

Second value to compare. y must be either the same type as x or composed of the same type as x.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### x > y?

Boolean result of the operation.

When you compare two arrays, 
 x > y? is a scalar in 
 Compare Aggregates mode and a Boolean array in 
 Compare Elements mode (default).

#### Behavior with Array Inputs

Compare Aggregates

Compare Aggregates

Parent topic:

Comparison Nodes

Related information:

- Comparison Modes for Array and Cluster Data

<!--NI_TOPIC bundle=g-web-development-api-ref path=head.html language=enus -->
## TOPIC 00039: HEAD

- bundle_id: `g-web-development-api-ref`
- source_path: `head.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/head.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a web request that returns headers from a server, web page, or web service. This node uses the HEAD HTTP method. This node does not submit any data to the server or receive body data. The minimal data exchange makes the HEAD node useful for testing the validity of a URL. client handle Unique v

HEAD

Sends a web request that returns headers from a server, web page, or web service.
 This node uses the HEAD HTTP method. This node does not submit any data to the server or receive body data. The minimal data exchange makes the HEAD node useful for testing the validity of a URL.

[IMAGE alt='1378' src='HEAD.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### client handle

Unique value that identifies the web request. You can use the same client handle to wire together multiple HTTP nodes to preserve authentication credentials, HTTP headers, and cookies. Client handles are not required when making independent web requests without persistent data such as headers or credentials.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### url

URL of the server, web page, or web service where this node will send the web request.

##### Relative URL behavior

If you do not specify a URL scheme on a Web Server target, each URL you enter is relative to the location the WebVI is hosted. The WebVI sends HTTP requests to the server at the relative URL. For example, if you host the WebVI on http://website.com/MyApp/, specifying the relative URL 
 subdirectory/myfile.txt sends an HTTP request to http://website.com/MyApp/subdirectory/myfile.txt.

If you do not specify a URL scheme on a non-Web Server target, the node prefixes http:// to the URL and treats it as an absolute URL.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### timeout

Amount of time in milliseconds the node has to wait for a response from the server before the web request times out. A value of -1 defers timeout monitoring to the operating system.

Default value: 10000 ms

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### status code

Status code information returned by the server.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### client handle out

Unique value that identifies the web request. Use this value to refer to this web request in subsequent node calls.

You can use the same client handle to wire together multiple HTTP nodes to preserve authentication credentials, HTTP headers, and cookies.

Client handles are not required when making independent web requests without persistent data such as headers or credentials.

[IMAGE alt='datatype_icon' src='/assets/img/i1dstr.png']

##### headers

Header fields returned by the server. Refer to the World Wide Web Consortium website at [www.w3.org](http://digital.ni.com/express.nsf/bycode/exctg8) for more information about header field definitions including available headers, descriptions, and syntax.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### CORS Restrictions on HTTP Requests

Requests from HTTP clients are subject to CORS restrictions when the WebVI communicates with a web service on a different origin. The web service responding to the HTTP request must return a valid CORS configuration for the HTTP request to complete successfully.

On non-Web Server targets, HTTP requests are not subject to CORS restrictions. The VI can make HTTP requests regardless of the CORS configuration of the server.

Note

#### Cached Response Behavior for Repeat Requests

HTTP nodes on a Web Server target may create caches of responses to HTTP requests. If a duplicate request occurs, the HTTP nodes can avoid querying the network by returning a previous response from the cache. The specific browser environment and server configuration determine the behavior of the cache.

On non-Web Server targets, every HTTP request creates a unique network request.

#### Forbidden Headers on a Web Server

A WebVI cannot transmit or receive specific 
 [forbidden headers](https://developer.mozilla.org/en-us/docs/glossary/forbidden_header_name) in HTTP requests. For header transmissions, the request to the server does not include forbidden headers. When the HTTP nodes receive a forbidden header from a server, they exclude the header from the headers output. Additionally, the CORS configuration of a server may exclude some headers in server requests or from server responses.

On non-Web Server targets, you do not need to account for forbidden headers in HTTP requests.

Parent topic:

HTTP Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=header-exists.html language=enus -->
## TOPIC 00040: Header Exists

- bundle_id: `g-web-development-api-ref`
- source_path: `header-exists.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/header-exists.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines if the header is associated with the client handle. Headers define attributes of the data exchanged between the client and server. client handle Unique value that identifies the web request. You can use the same client handle to wire together multiple HTTP nodes to preserve authentication

Header Exists

Determines if the header is associated with the client handle.
 Headers define attributes of the data exchanged between the client and server.

[IMAGE alt='1378' src='Header_Exists.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### client handle

Unique value that identifies the web request.

You can use the same client handle to wire together multiple HTTP nodes to preserve authentication credentials, HTTP headers, and cookies.

Client handles are not required when making web requests without persistent data such as headers or credentials.

[IMAGE alt='datatype_icon' src='/assets/img/c1dstr.png']

##### header

Header field included in the web requests of the client handle. The header control provides a pull-down menu with available header fields.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### client handle out

Unique value that returns data back to the node. You can use the same client handle to wire together multiple HTTP nodes to preserve authentication credentials, HTTP headers, and cookies. Client handles are not required when making independent web requests without persistent data such as headers or credentials.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### header exists?

A Boolean value that determines if the header is associated with the client handle.

| True | The specified header is associated with the client handle. |
| --- | --- |
| False | The specified header is not associated with the client handle. |

[IMAGE alt='datatype_icon' src='/assets/img/i1dstr.png']

##### value

Value assigned to the header. If header exists? returns False, this output returns an empty string.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

HTTP Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=hex-digit.html language=enus -->
## TOPIC 00041: Hexadecimal Digit?

- bundle_id: `g-web-development-api-ref`
- source_path: `hex-digit.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/hex-digit.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns True if a value represents a hexadecimal digit ranging from 0 through 9, A through F, or a through f. Otherwise, this node returns False. If the value is a string, this node uses the first character in the string. If the value is a number, this node interprets it as the ASCII value of a char

Hexadecimal Digit?

Returns True if a value represents a hexadecimal digit ranging from 0 through 9, A through F, or a through f. Otherwise, this node returns False.

If the value is a string, this node uses the first character in the string. If the value is a number, this node interprets it as the ASCII value of a character. If the value is a floating-point number, this node rounds to the nearest integer.

[IMAGE alt='1378' src='IsHexadecimalDigit.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### char

An input to this operation.

This input supports scalar strings or numbers, clusters of strings or numbers, arrays of strings or numbers, and so on.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### hex?

Boolean result of the operation.

This output assumes the same data type structure as 
 char.

Parent topic:

Comparison Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=hexadecimal-string-to-number.html language=enus -->
## TOPIC 00042: Hexadecimal String to Number

- bundle_id: `g-web-development-api-ref`
- source_path: `hexadecimal-string-to-number.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/hexadecimal-string-to-number.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the characters 0 through 9, A through F, and a through f in a string to a hexadecimal integer. string The string that you want to convert. This input can also be any data type that contains only strings, such as an array or cluster of strings. offset The number of characters into the input

Hexadecimal String to Number

Converts the characters 
0 through 
9, 
A through 
F, and 
a through 
f in a string to a hexadecimal integer.

[IMAGE alt='1378' src='HexadecimalStringToNumber.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### string

The string that you want to convert.

This input can also be any data type that contains only strings, such as an array or cluster of strings.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### offset

The number of characters into the input string at which this node begins its operation.

The offset of the first character in the input string is 0. If offset is beyond the end of the input string, this node returns an empty string.

Note

16

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### default

A numeric value whose representation determines the representation of 
number.

Default value: 32-bit unsigned integer

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### offset past number

The index in string of the first character following the number.

If string is an array of strings, offset past number reflects the offset within the last string.

Note

16

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### number

The result of converting string into a number.

number

string

string

number

If the input string represents a number outside the range of the representation of 
 number, 
 number is set to the maximum value for that representation.

#### Examples

string

offset

default

offset past number

number

| string | offset | default | offset past number | number | Comments |
| --- | --- | --- | --- | --- | --- |
| f3g | 0 | 0 | 2 | 243 | g is not a valid hex character, so conversion stops there. |
| –30 | 0 | 0 | 0 | 0 | Negative numbers are not permitted for hex. |

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=html-container.html language=enus -->
## TOPIC 00043: HTML Container

- bundle_id: `g-web-development-api-ref`
- source_path: `html-container.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/html-container.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Interact with your custom content in the Placeholder HTML Container.

HTML
 Container

Interact with your custom content in the Placeholder HTML Container.

Obtain JavaScript Reference

Create a JavaScript Reference for the element within the HTML Container.

<!--NI_TOPIC bundle=g-web-development-api-ref path=http-nodes.html language=enus -->
## TOPIC 00044: HTTP Nodes

- bundle_id: `g-web-development-api-ref`
- source_path: `http-nodes.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/http-nodes.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Build a web client that interacts with servers, web pages, and web services with Hypertext Transfer Protocol (HTTP).

HTTP Nodes

Build a web client that interacts with servers, web pages, and web services with Hypertext Transfer Protocol (HTTP).

Data Exchange Nodes

Add Header

client handle

Close HTTP Handle

client handle

GET

Sends a web request that returns header and body data from a server, web page, or web service.

Get Header

header

client handle

HEAD

headers

Header Exists

header

client handle

List Headers

headers

client handle

Open HTTP Handle

Opens a client handle.

POST

Sends data to the URL you specify.

PUT

Creates or updates data and sends it to the URL you specify.

Remove Header

client handle

Parent topic:

Data Exchange Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=hyperlink-class.html language=enus -->
## TOPIC 00045: Hyperlink

- bundle_id: `g-web-development-api-ref`
- source_path: `hyperlink-class.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/hyperlink-class.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the properties in the Hyperlink class to read and write the elements of a hyperlink control.No properties are specific to this class.

Hyperlink

Use the properties in the Hyperlink class to read and write the elements of a hyperlink control.No properties are specific to this class.

Control

Use the properties in the Control class to read and write the elements of a control.

Parent topic:

Control

<!--NI_TOPIC bundle=g-web-development-api-ref path=implies.html language=enus -->
## TOPIC 00046: Implies

- bundle_id: `g-web-development-api-ref`
- source_path: `implies.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/implies.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Negates the first input and then computes the logical OR of the second input and the negated input. In other words, if the first input is True and the second input is False, this node returns False. Otherwise, it returns True. This function performs bitwise operations on numeric inputs. x The first

Implies

Negates the first input and then computes the logical OR of the second input and the negated input.

In other words, if the first input is True and the second input is False, this node returns False. Otherwise, it returns True.

This function performs bitwise operations on numeric inputs.

[IMAGE alt='1378' src='Implies.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### x

The first input to the operation.

This input can be any data type that contains only Boolean values, numbers, or error clusters, such as an array of numbers or a cluster of Booleans. If this input is an error cluster, the node uses only the 
 status element of the error cluster.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### y

The second input to the operation.

This input must be the same data type as x.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### x implies y?

The logical OR of 
y and of the logical negation of 
x.

#### Examples

| x | y | x implies y? |
| --- | --- | --- |
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |

Parent topic:

Boolean Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=index-array.html language=enus -->
## TOPIC 00047: Index Array

- bundle_id: `g-web-development-api-ref`
- source_path: `index-array.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/index-array.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value stored in an array at a specified index. array An n-dimensional array of any type. If array is an empty array, element returns the default value of the defined data type for the array. This input changes to waveform when the data type is a waveform. Data Type Changes on FPGA When y

Index Array

Returns the value stored in an array at a specified index.

[IMAGE alt='1378' src='ArrayIndex.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### array

An 
n-dimensional array of any type.

If array is an empty array, element returns the default value of the defined data type for the array.

This input changes to waveform when the data type is a waveform.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### index

A number that refers to a location within the input array.

This node automatically provides an index input for each dimension of the array.

Default value: 0

##### Behavior for Out of Range Values

If index for any dimension is less than zero or greater than the length of array in that dimension, this node returns the default value of the defined data type for the array.

##### Relationship between index Inputs and array Dimensions

For multidimensional arrays, index inputs correspond to row-major order. Thus, the first index corresponds last dimension of the array input, and the last index corresponds to the first dimension of the array input. The following table shows the relationship between four index inputs and the dimensions of a 4D array input.

| index Order | Corresponding Dimension in array Input | index Name |
| --- | --- | --- |
| 1 | 4th | volume index |
| 2 | 3rd | page index |
| 3 | 2nd | row index |
| 4 | 1st | column index |

##### Unwired Index Inputs

Unwired index inputs allow you to retrieve a subarray of the array rather than a single element. For example, to retrieve column 1 of a 2D array, specify 1 in the column index and leave the row index unwired.

When all index inputs are unwired, the retrieved subarray contains one less dimension than array.

##### Relationship between index and Multiple element or subarray Outputs

If you expand the node to show more than one element or subarray output, the node provides a set of index inputs for each output. The values you wire to a set of index inputs determine the value of the corresponding output. However, if you do not wire values to a set of index inputs, the corresponding element or subarray output returns the element or subarray that follows the previous element or subarray output in the original array. Refer to the 
 *Examples* tab for an illustration of this relationship.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### waveform

The waveform whose array of y values you want to use in this operation. This input becomes available when you wire a waveform to array.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### element

The scalar element or subarray stored in array at the specified index.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

#### Examples

The following image illustrates this node's behavior for a variety of inputs:

[IMAGE alt='1378' src='GUID-034E3164-BB62-4B69-BE48-0E3B9AF60EAD-a5.png']

| Output | Panel Indicator | Comments |
| --- | --- | --- |
| element, all indexes wired |  |  |
| subarray, row wired |  | Without a value for the column dimension, Index Array returns the entire row specified by the row input. |
| subarray, indexes unwired |  | This output has no values specified for its corresponding row and column inputs. Therefore, the node returns the subarray that immediately follows the previous output. |
| subarray, column wired |  | Without a value for the row dimension, Index Array returns the entire column specified by the column input. |

#### Resizing Behavior

When you wire an array to this node, the node resizes automatically to display index inputs for each dimension in the array you wire to array. You also can add additional element or subarray outputs by resizing the node. The node provides index inputs for each output.

#### Accessing a Subarray by Disabling Indexing along a Dimension

You can disable indexing along a dimension by leaving the corresponding index input unwired. By default, the first dimension has indexing enabled, with the others disabled. You can wire a constant or control to the index inputs that you want enabled.

For example, if you want to index a row in a 2D array, the first index input is enabled and the second index input is disabled. If you want to index that same 2D array also by column, you can resize the node to show another set of input terminals. This next set of inputs has its own corresponding element output. By default, if you do not wire any index input terminals, the first element indexes row 0, the second element indexes row 1, and so on.

Parent topic:

Array Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=inverse-cosine.html language=enus -->
## TOPIC 00048: Inverse Cosine

- bundle_id: `g-web-development-api-ref`
- source_path: `inverse-cosine.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/inverse-cosine.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the arccosine of a specified value (x) in radians. If x is not complex and is less than -1 or greater than 1, the result is not a number (NaN). x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Chang

Inverse Cosine

Computes the arccosine of a specified value (x) in radians.

If 
 x is not complex and is less than -1 or greater than 1, the result is not a number (NaN).

[IMAGE alt='1378' src='InverseCosine.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### arccos

Result of the operation.

x

x

x

i

x

arccos

Parent topic:

Trigonometric Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=inverse-secant.html language=enus -->
## TOPIC 00049: Inverse Secant

- bundle_id: `g-web-development-api-ref`
- source_path: `inverse-secant.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/inverse-secant.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the inverse secant of a specified value (x) in radians. x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this input has a de

Inverse Secant

Computes the inverse secant of a specified value (x) in radians.

[IMAGE alt='1378' src='InverseSecant.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### arcsec

Result of the operation.

This output assumes the same numeric representation as 
 x.

Parent topic:

Trigonometric Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=ionamecontrol-class.html language=enus -->
## TOPIC 00050: IONameControl

- bundle_id: `g-web-development-api-ref`
- source_path: `ionamecontrol-class.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/ionamecontrol-class.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the properties in the IONameControl class to read and write the elements of a tag endpoint.No properties are specific to this class.

IONameControl

Use the properties in the IONameControl class to read and write the elements of a tag endpoint.No properties are specific to this class.

Control

Use the properties in the Control class to read and write the elements of a control.

Parent topic:

Control

<!--NI_TOPIC bundle=g-web-development-api-ref path=join-numbers.html language=enus -->
## TOPIC 00051: Join Numbers

- bundle_id: `g-web-development-api-ref`
- source_path: `join-numbers.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/join-numbers.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a number from the component bytes or words. high(x) An 8-, 16-, or 32-bit number or an array or cluster of that representation. low(x) An 8-, 16-, or 32-bit number or an array or cluster of that representation. x An integer twice the width of high(x) and low(x). This output is a 16-, 32-, or

Join Numbers

Creates a number from the component bytes or words.

[IMAGE alt='1378' src='JoinNumbers.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### high(x)

An 8-, 16-, or 32-bit number or an array or cluster of that representation.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### low(x)

An 8-, 16-, or 32-bit number or an array or cluster of that representation.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### x

An integer twice the width of high(x) and low(x).

This output is a 16-, 32-, or 64-bit unsigned integer or an array or cluster of those representations. If high(x) and low(x) are of different widths, this output is twice the width of the widest number.

Parent topic:

Data Manipulation Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=knob-class.html language=enus -->
## TOPIC 00052: Knob

- bundle_id: `g-web-development-api-ref`
- source_path: `knob-class.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/knob-class.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the properties in the Knob class to read and write the elements of a knob.No properties are specific to this class.

Knob

Use the properties in the Knob class to read and write the elements of a knob.No properties are specific to this class.

RadialNumeric

Use the properties in the RadialNumeric class to read and write the elements of a radial numeric.

Parent topic:

RadialNumeric

<!--NI_TOPIC bundle=g-web-development-api-ref path=labview-standard-error-behavior.html language=enus -->
## TOPIC 00053: Standard Error Behavior

- bundle_id: `g-web-development-api-ref`
- source_path: `labview-standard-error-behavior.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/labview-standard-error-behavior.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `concept`
- source_description: Many nodes provide error in and an error out parameters so that the node can respond to and communicate errors that occur while code is running. When you create an application, wire all error inputs and outputs of each node on the diagram so that error information moves through the application in th

Standard Error Behavior

Many nodes provide error in and an error out parameters so that the node can respond to and communicate errors that occur while code is running. When you create an application, wire all error inputs and outputs of each node on the diagram so that error information moves through the application in the same way as data values. As your VI runs, each node with error-checking capabilities monitors for error information that is passed to the error input from the previous node. Since each node with error inputs and outputs does the same thing, allowing only valid data or error information to flow through the diagram.

The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way:

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Note

error in

error in

If you enable error information to flow through the diagram by wiring all error inputs and outputs, you can also use Error nodes to process information provided by the error, access additional information about the error, and use that information to make run-time decisions based on the error conditions in the application.

<!--NI_TOPIC bundle=g-web-development-api-ref path=less.html language=enus -->
## TOPIC 00054: Less?

- bundle_id: `g-web-development-api-ref`
- source_path: `less.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/less.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns True if the first value is less than the second value. Otherwise, this node returns False. This node can also compare an array or cluster of a data type to a scalar of the same data type and produce an array or cluster of Boolean values. x First value to compare. x must be either the same ty

Less?

Returns True if the first value is less than the second value. Otherwise, this node returns False.

This node can also compare an array or cluster of a data type to a scalar of the same data type and produce an array or cluster of Boolean values.

[IMAGE alt='1378' src='IsLess.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

First value to compare. x must be either the same type as y or composed of the same type as y.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### y

Second value to compare. y must be either the same type as x or composed of the same type as x.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### x < y?

Boolean result of the operation.

When you compare two arrays, 
 x < y? is a scalar in 
 Compare Aggregates mode and a Boolean array in 
 Compare Elements mode (default).

#### Behavior with Array Inputs

When using Less? in 
 Compare Aggregates mode, if all values in the input arrays are equal but one array has extra elements at the end, the shorter array is considered less than the longer one. For example, a Less? node set to 
 Compare Aggregates considers the array [1,2,3] to be less than the array [1,2,3,2].

Parent topic:

Comparison Nodes

Related information:

- Comparison Modes for Array and Cluster Data

<!--NI_TOPIC bundle=g-web-development-api-ref path=linearnumeric-class.html language=enus -->
## TOPIC 00055: LinearNumeric

- bundle_id: `g-web-development-api-ref`
- source_path: `linearnumeric-class.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/linearnumeric-class.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the properties in the LinearNumeric class to read and write the elements of a linear numeric.

LinearNumeric

Use the properties in the LinearNumeric class to read and write the elements of a linear numeric.

Numeric

Use the properties in the Numeric class to read and write the elements of a numeric control.No properties are specific to this class.

Scale

Reference to the scale of the numeric control.

Slider

Use the properties of the Slider class to read and write the elements of a slider.No properties are specific to this class.

Tank

Use the properties in the Tank class to read and write the elements of a tank.No properties are specific to this class.

Parent topic:

Numeric

<!--NI_TOPIC bundle=g-web-development-api-ref path=machine-epsilon.html language=enus -->
## TOPIC 00056: Machine Epsilon

- bundle_id: `g-web-development-api-ref`
- source_path: `machine-epsilon.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/machine-epsilon.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the round-off error for a floating-point number with a given precision. Use the machine epsilon constant to compare whether two floating-point numbers are equivalent.

Machine Epsilon

Represents the round-off error for a floating-point number with a given precision.
 Use the machine epsilon constant to compare whether two floating-point numbers are equivalent.

[IMAGE alt='1378' src='Literal.Numeric.Machine_Epsilon.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=g-web-development-api-ref path=natural-log-base.html language=enus -->
## TOPIC 00057: Base 10 Logarithm of e

- bundle_id: `g-web-development-api-ref`
- source_path: `natural-log-base.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/natural-log-base.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the value 0.43429448190325182.

Base 10 Logarithm of e

Represents the value 0.43429448190325182.

[IMAGE alt='1378' src='Literal.Numeric.Log10e.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=g-web-development-api-ref path=natural-log-of-pi.html language=enus -->
## TOPIC 00058: lnPi

- bundle_id: `g-web-development-api-ref`
- source_path: `natural-log-of-pi.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/natural-log-of-pi.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the value 1.1447298858494002.

lnPi

Represents the value 1.1447298858494002.

[IMAGE alt='1378' src='Literal.Numeric.lnPi.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=g-web-development-api-ref path=natural-log-of-ten.html language=enus -->
## TOPIC 00059: ln10

- bundle_id: `g-web-development-api-ref`
- source_path: `natural-log-of-ten.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/natural-log-of-ten.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the value 2.3025850929940459.

ln10

Represents the value 2.3025850929940459.

[IMAGE alt='1378' src='Literal.Numeric.ln10.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=g-web-development-api-ref path=natural-log-of-two.html language=enus -->
## TOPIC 00060: ln2

- bundle_id: `g-web-development-api-ref`
- source_path: `natural-log-of-two.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/natural-log-of-two.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the value 0.6931471805599453.

ln2

Represents the value 0.6931471805599453.

[IMAGE alt='1378' src='Literal.Numeric.ln2.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=g-web-development-api-ref path=negate.html language=enus -->
## TOPIC 00061: Negate

- bundle_id: `g-web-development-api-ref`
- source_path: `negate.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/negate.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Makes the input value negative. x An input to this operation. This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, arrays of clusters of numbers, and waveforms. x cannot be an unsigned integer because unsigned integers rep

Negate

Makes the input value negative.

[IMAGE alt='1378' src='Negate.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, arrays of clusters of numbers, and waveforms. 
 x cannot be an unsigned integer because unsigned integers represent only non-negative integers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### -x

The negative value of the input value.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=not-equal.html language=enus -->
## TOPIC 00062: Not Equal?

- bundle_id: `g-web-development-api-ref`
- source_path: `not-equal.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/not-equal.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Compares two values and returns True only if the values are not equal to each other. This node can also compare an array or cluster of a data type to a scalar of the same data type and produce an array or cluster of Booleans. x First value to compare. x must be either the same type as y or composed

Not Equal?

Compares two values and returns True only if the values are not equal to each other.

This node can also compare an array or cluster of a data type to a scalar of the same data type and produce an array or cluster of Booleans.

[IMAGE alt='1378' src='IsNotEqual.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

First value to compare. x must be either the same type as y or composed of the same type as y.

This input supports all data types.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### y

Second value to compare. y must be either the same type as x or composed of the same type as x.

This input supports all data types.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### x != y?

Boolean result of the operation.

When you compare two arrays, 
 x != y? is a scalar in 
 Compare Aggregates mode and a Boolean array in 
 Compare Elements mode (default).

#### Behavior for 
 NaN Inputs

If at least one input is 
 NaN (not a number), this node returns FALSE. To compare inputs with a value of 
 NaN, use Not a Number/Path/Refnum?.

Parent topic:

Comparison Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=number-to-engineering-string.html language=enus -->
## TOPIC 00063: Number to Engineering String

- bundle_id: `g-web-development-api-ref`
- source_path: `number-to-engineering-string.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/number-to-engineering-string.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a numeric value to a string that shows the number's engineering format. Engineering format is similar to exponential format, except the exponent is a multiple of three (..., -3, 0, 3, 6, ...). number A number to be converted into a string. This input can also be any data type that contains

Number to Engineering String

Converts a numeric value to a string that shows the number's engineering format.

Engineering format is similar to exponential format, except the exponent is a multiple of three (..., -3, 0, 3, 6, ...).

[IMAGE alt='1378' src='NumberToEngineeringString.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### number

A number to be converted into a string.

This input can also be any data type that contains only numbers, such as an array of numbers or a cluster of numbers.

[IMAGE alt='datatype_icon' src='/assets/img/ci16.png']

##### width

A number specifying how many characters to use to express number as a string.

If width is less than the number of characters required, this node uses exactly as many characters as needed. If width is greater than the number of characters required, this node adds a space on the left side of the output string for each additional character.

Default value: No value — Exactly as many characters as are needed to represent the number, with no extra padding.

[IMAGE alt='datatype_icon' src='/assets/img/ci16.png']

##### precision

A number specifying the number of digits after the decimal point in the output string. The node rounds number to this decimal place.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### use system decimal point?

Boolean specifying whether to use the system decimal separator to designate a decimal point.

| True | This node uses the localized decimal separator. |
| --- | --- |
| False | This node uses a period as the decimal separator. |

Default value: FALSE

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### engineering string

number represented as an engineering string.

#### Examples

number

width

precision

engineering string

engineering string

| number | width | precision | engineering string | Comments |
| --- | --- | --- | --- | --- |
| 4.93 | 10 | 2 | _ _ _4.93E+0 | number is rounded, padded with spaces on the left. |
| .49 | 10 | 2 | _490.00E-3 | number is rounded, padded with a space on the left. |
| 61.96 | 8 | 1 | _62.0E+0 | number is rounded, padded with a space on the left. |
| 1789.32 | 8 | 2 | _ 1.79E+3 | number is rounded, padded with a space on the left. |

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=number-to-exponential-string.html language=enus -->
## TOPIC 00064: Number to Exponential String

- bundle_id: `g-web-development-api-ref`
- source_path: `number-to-exponential-string.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/number-to-exponential-string.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a numeric value to a string in E-format (exponential notation). number A number to be converted into a string. This input can also be any data type that contains only numbers, such as an array of numbers or a cluster of numbers. width A number specifying how many characters to use to expres

Number to Exponential String

Converts a numeric value to a string in E-format (exponential notation).

[IMAGE alt='1378' src='NumberToExponentialString.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### number

A number to be converted into a string.

This input can also be any data type that contains only numbers, such as an array of numbers or a cluster of numbers.

[IMAGE alt='datatype_icon' src='/assets/img/ci16.png']

##### width

A number specifying how many characters to use to express number as a string.

If width is less than the number of characters required, this node uses exactly as many characters as needed. If width is greater than the number of characters required, this node adds a space on the left side of the output string for each additional character.

Default value: No value — Exactly as many characters as are needed to represent the number, with no extra padding.

[IMAGE alt='datatype_icon' src='/assets/img/ci16.png']

##### precision

A number specifying the number of digits after the decimal point in the output string. The node rounds number to this decimal place.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### use system decimal point?

Boolean specifying whether to use the system decimal separator to designate a decimal point.

| True | This node uses the localized decimal separator. |
| --- | --- |
| False | This node uses a period as the decimal separator. |

Default value: FALSE

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### exponential format string

number represented as a string in exponential format.

#### Examples

number

width

precision

exponential format string

exponential format string

| number | width | precision | exponential format string | Comments |
| --- | --- | --- | --- | --- |
| 4.911 | 5 | 2 | 4.91e0 | number is rounded, width is extended. |
| .003926 | 10 | 2 | _ _ _3.93e-3 | number is rounded, padded with spaces on the left. |
| 216.01 | 5 | 0 | _ _2e2 | number is rounded, padded with spaces on the left. |

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=numeric-minimum.html language=enus -->
## TOPIC 00065: Minimum

- bundle_id: `g-web-development-api-ref`
- source_path: `numeric-minimum.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/numeric-minimum.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Minimum value of the data range.

Minimum

Minimum value of the data range.

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

Parent topic:

NumericTextBox

<!--NI_TOPIC bundle=g-web-development-api-ref path=numeric-nodes.html language=enus -->
## TOPIC 00066: Numeric Nodes

- bundle_id: `g-web-development-api-ref`
- source_path: `numeric-nodes.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/numeric-nodes.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`

Numeric Nodes

Absolute Value

Returns the absolute value of the input.

Add

Computes the sum of the inputs.

Add Array Elements

Returns the sum of all of the elements in a numeric array.

Complex Conjugate

i

Complex to Polar

Returns the polar components of a complex number.

Complex to Real and Imaginary

Returns the rectangular components of a complex number.

Decrement

Subtracts 1 from the input value.

Divide

Computes the quotient of the inputs.

Increment

Adds 1 to the input value.

In Range and Coerce

Determines whether the input value falls within a range specified by the upper and lower limits and optionally coerces the value to fall within the range.

Max and Min

Compares two values and returns the maximum and minimum values.

Multiply

Returns the product of the inputs.

Multiply Array Elements

Returns the product of all of the elements in a numeric array.

Negate

Makes the input value negative.

Polar to Complex

Creates a complex number from two values in polar notation.

Polar to Real and Imaginary

Converts the polar components of a complex number into its rectangular components.

Quotient and Remainder

Computes the integer quotient and the remainder of the inputs.

Random Number

Generates a double-precision, floating-point number between 0 and 1.

Random Number (Range)

Generates a random value from a specified range.

Real and Imaginary to Complex

Creates a complex number from two values in rectangular notation.

Real and Imaginary to Polar

Converts the rectangular components of a complex number into its polar components.

Reciprocal

Divides 1 by the input value.

Round toward Negative Infinity

Expresses the input to the next lower round integer.

Round toward Positive Infinity

Expresses the input to the next higher round integer.

Round to Nearest

Expresses the input to the nearest round integer.

Scale by Power of 2

Multiplies the input by 2 raised to a specified power.

Sign

Returns the sign of the input value.

Square

Computes the square of the input value.

Square Root

Computes the square root of an input value.

Subtract

Computes the difference between numbers, timestamps, or waveforms.

<!--NI_TOPIC bundle=g-web-development-api-ref path=numerics.html language=enus -->
## TOPIC 00067: Numeric Controls

- bundle_id: `g-web-development-api-ref`
- source_path: `numerics.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/numerics.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enter and display numeric data. Which Numeric Should I Use? Control Use Numeric control and indicator Enter or display numeric data. Slider Display numeric data in a vertical or horizontal slide with a customizable scale and a pointer that helps you see the exact value. Gauge Enter or display numeri

Numeric Controls

Enter and display numeric data.

[IMAGE alt='1378' src='GUID-E85553F2-0E8F-44F9-A8CF-9D1044A048FA-a5.png']

#### Which Numeric Should I Use?

| Control | Use |
| --- | --- |
| Numeric control and indicator | Enter or display numeric data. |
| Slider | Display numeric data in a vertical or horizontal slide with a customizable scale and a pointer that helps you see the exact value. |
| Gauge | Enter or display numeric data in a rotary scale. |
| Tank | Display numeric data in a vertical slide that resembles a real tank or thermometer instrument. |
| Timestamp | Enter or display a time and date value. |
| Progress bars | Show progress in a vertical bar or circle. |

#### What Is the Difference between Significant Digits and Digits of Precision?

Significant digits specifies the number of significant digits to display in the numeric control.

Digits of precision specifies how many digits to display after the decimal mark.

#### How Do I Use, View, and Store Absolute Time?

Use the timestamp control to use, view, and store absolute time with high precision. This data type can accurately store 18 digits of precision in whole seconds and 19 digits of precision in fractions of a second. The timestamp control displays values in local time. However, the timestamp wire data type stores values in UTC.

Although you can use a numeric control to display timestamp values, the numeric control holds a relative quantity. The timestamp control holds an absolute quantity.

#### What Characters Do Numeric Controls Accept?

| Character(s) | Description |
| --- | --- |
| Hexadecimal digits | 0 through F |
| Octal digits | 0 through 7 |
| Binary digits | 0 and 1 |
| Decimal digits | 1, 1.0, 2, 3.5, and so on |
| . | Decimal point |
| , | Decimal comma |
| + | Positive symbol |
| - | Negative symbol |
| E or e | For scientific or engineering notation format |
| Infinity | Infinity |
| NaN | Not a number |
| / | For use in absolute time format |
| : | For use in absolute time format |
| AM, am, PM, pm | For use in absolute time format |
| SI prefixes |  |
| y | yocto (10 -24 ) |
| z | zepto (10 -21 ) |
| a | atto (10 -18 ) |
| f | femto (10 -15 ) |
| p | pico (10 -12 ) |
| n | nano (10 -9 ) |
| u | micro (10 -6 ) |
| m | milli (10 -3 ) |
| c | centi (10 -2 ) |
| d | deci (10 -1 ) |
| da | deka (10 1 ) |
| h | hecto (10 2 ) |
| k | kilo (10 3 ) |
| M | mega (10 6 ) |
| G | giga (10 9 ) |
| T | tera (10 12 ) |
| P | peta (10 15 ) |
| E | exa (10 18 ) |
| Z | zetta (10 21 ) |
| Y | yotta (10 24 ) |

<!--NI_TOPIC bundle=g-web-development-api-ref path=numericscale-class.html language=enus -->
## TOPIC 00068: NumericScale

- bundle_id: `g-web-development-api-ref`
- source_path: `numericscale-class.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/numericscale-class.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the properties in the NumericScale class to read and write the elements of the scale on a numeric control.

NumericScale

Use the properties in the NumericScale class to read and write the elements of the scale on a numeric control.

RangeScale

Use the properties in the RangeScale class to read and write the elements of the uncolored scale.

Visible

Boolean value that determines whether to display the object.

Parent topic:

RangeScale

<!--NI_TOPIC bundle=g-web-development-api-ref path=plot-baroutlinecolor.html language=enus -->
## TOPIC 00069: BarOutlineColor

- bundle_id: `g-web-development-api-ref`
- source_path: `plot-baroutlinecolor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/plot-baroutlinecolor.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Outline color of bars in the bar plot.

BarOutlineColor

Outline color of bars in the bar plot.

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

Parent topic:

Plot

<!--NI_TOPIC bundle=g-web-development-api-ref path=plotbase-class.html language=enus -->
## TOPIC 00070: PlotBase

- bundle_id: `g-web-development-api-ref`
- source_path: `plotbase-class.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/plotbase-class.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the properties of the PlotBase class to read and write the elements of a plot, cursor, or bus.

PlotBase

Use the properties of the PlotBase class to read and write the elements of a plot, cursor, or bus.

Name

Name of the object.

Visible

Boolean value that determines whether to display the object.

Bus

Use the properties of the Bus class to read and write the elements of a bus.

Cursor

Use the properties of the Cursor class to read and write the elements of a graph or chart cursor.

DigitalSignalPlot

Use the properties of the DigitalSignalPlot class to read and write the elements of a digital plot.No properties are specific to this class.

Plot

Use the properties of the Plot class to read and write the elements of a plot.

PolarPlot

Use the properties of the PolarPlot class to read and write the elements of a polar plot.

<!--NI_TOPIC bundle=g-web-development-api-ref path=plotbase-linestyle.html language=enus -->
## TOPIC 00071: LineStyle

- bundle_id: `g-web-development-api-ref`
- source_path: `plotbase-linestyle.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/plotbase-linestyle.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Line style of the plot.

LineStyle

Line style of the plot.

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

Parent topic:

Plot

Parent topic:

PolarPlot

<!--NI_TOPIC bundle=g-web-development-api-ref path=polarplot-class.html language=enus -->
## TOPIC 00072: PolarPlot

- bundle_id: `g-web-development-api-ref`
- source_path: `polarplot-class.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/polarplot-class.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the properties of the PolarPlot class to read and write the elements of a polar plot.

PolarPlot

Use the properties of the PolarPlot class to read and write the elements of a polar plot.

PlotBase

Use the properties of the PlotBase class to read and write the elements of a plot, cursor, or bus.

Color

Color of the plot.

LineWidth

Line width of the plot.

LineStyle

Line style of the plot.

PointShape

Shape of points in the plot.

Parent topic:

PlotBase

<!--NI_TOPIC bundle=g-web-development-api-ref path=positive-infinity.html language=enus -->
## TOPIC 00073: Positive Infinity

- bundle_id: `g-web-development-api-ref`
- source_path: `positive-infinity.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/positive-infinity.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the value infinity.

Positive Infinity

Represents the value infinity.

[IMAGE alt='1378' src='Literal.Numeric.Positive_Infinity.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=g-web-development-api-ref path=post.html language=enus -->
## TOPIC 00074: POST

- bundle_id: `g-web-development-api-ref`
- source_path: `post.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/post.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends data to the URL you specify. This node uses the POST HTTP method. Unlike a PUT request, POST requests do not require all available property and attribute values when updating a resource. You can choose to send all values to update the entire resource or just a subset of the available values.

POST

Sends data to the URL you specify.

This node uses the POST HTTP method. Unlike a PUT request, POST requests do not require all available property and attribute values when updating a resource. You can choose to send all values to update the entire resource or just a subset of the available values.

HTTP Nodes

Build a web client that interacts with servers, web pages, and web services with Hypertext Transfer Protocol (HTTP).

POST Buffer

buffer

PUT

Creates or updates data and sends it to the URL you specify.

PUT Buffer

buffer

Parent topic:

HTTP Nodes

Related reference:

- PUT
- PUT Buffer

<!--NI_TOPIC bundle=g-web-development-api-ref path=progressbar-class.html language=enus -->
## TOPIC 00075: ProgressBar

- bundle_id: `g-web-development-api-ref`
- source_path: `progressbar-class.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/progressbar-class.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the properties in the ProgressBar class to read and write the elements of a progress bar.No properties are specific to this class.

ProgressBar

Use the properties in the ProgressBar class to read and write the elements of a progress bar.No properties are specific to this class.

Numeric

Use the properties in the Numeric class to read and write the elements of a numeric control.No properties are specific to this class.

Parent topic:

Numeric

<!--NI_TOPIC bundle=g-web-development-api-ref path=radialnumeric-class.html language=enus -->
## TOPIC 00076: RadialNumeric

- bundle_id: `g-web-development-api-ref`
- source_path: `radialnumeric-class.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/radialnumeric-class.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the properties in the RadialNumeric class to read and write the elements of a radial numeric.

RadialNumeric

Use the properties in the RadialNumeric class to read and write the elements of a radial numeric.

Numeric

Use the properties in the Numeric class to read and write the elements of a numeric control.No properties are specific to this class.

Scale

Reference to the scale of the numeric control.

Gauge

Use the properties in the Gauge class to read and write the elements of a gauge.No properties are specific to this class.

Knob

Use the properties in the Knob class to read and write the elements of a knob.No properties are specific to this class.

Meter

Use the properties in the Meter class to read and write the elements of a meter.No properties are specific to this class.

Parent topic:

Numeric

<!--NI_TOPIC bundle=g-web-development-api-ref path=random-number-range-dbl.html language=enus -->
## TOPIC 00077: DBL

- bundle_id: `g-web-development-api-ref`
- source_path: `random-number-range-dbl.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/random-number-range-dbl.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates a random value from a specified range. This node returns a value greater than or equal to lower bound and less than upper bound. If upper bound is less than or equal to lower bound, this node returns lower bound. upper bound The upper limit of the range. Default value: 100 lower bound The

DBL

Generates a random value from a specified range.

This node returns a value greater than or equal to lower bound and less than upper bound. If upper bound is less than or equal to lower bound, this node returns lower bound.

[IMAGE alt='1378' src='Random_Number_(Range)_DBL.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### upper bound

The upper limit of the range.

Default value: 100

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### lower bound

The lower limit of the range.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### number

A random number greater than or equal to lower bound and less than upper bound.

Parent topic:

Random Number (Range)

<!--NI_TOPIC bundle=g-web-development-api-ref path=real-and-imaginary-to-complex.html language=enus -->
## TOPIC 00078: Real and Imaginary to Complex

- bundle_id: `g-web-development-api-ref`
- source_path: `real-and-imaginary-to-complex.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/real-and-imaginary-to-complex.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a complex number from two values in rectangular notation. x The x rectangular component of x + yi. This input supports scalar numbers, arrays or clusters of numbers, arrays of clusters of numbers, and waveforms. y The y rectangular component of x + yi. This input supports scalar numbers, arr

Real and Imaginary to Complex

Creates a complex number from two values in rectangular notation.

[IMAGE alt='1378' src='RealAndImaginaryToComplex.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

The x rectangular component of x + yi.

This input supports scalar numbers, arrays or clusters of numbers, arrays of clusters of numbers, and waveforms.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### y

The y rectangular component of x + yi.

This input supports scalar numbers, arrays or clusters of numbers, arrays of clusters of numbers, and waveforms.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/icdb.png']

##### x + yi

The complex number.

x + yi has the same structure as the input, with complex representation instead of scalar.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=real-and-imaginary-to-polar.html language=enus -->
## TOPIC 00079: Real and Imaginary to Polar

- bundle_id: `g-web-development-api-ref`
- source_path: `real-and-imaginary-to-polar.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/real-and-imaginary-to-polar.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the rectangular components of a complex number into its polar components. This node converts the rectangular components to polar components using the following equations: r = x 2 + y 2 r = x 2 + y 2 t h e t a = arctan 2 ( y , x )   r a d i a n s t h e t a = arctan 2 ( y , x )   r a d i a n

Real and Imaginary to Polar

Converts the rectangular components of a complex number into its polar components.

This node converts the rectangular components to polar components using the following equations:

r

=

x

2

+

y

2

r

=

x

2

+

y

2

t

h

e

t

a

=

arctan

2

(

y

,

x

)

r

a

d

i

a

n

s

t

h

e

t

a

=

arctan

2

(

y

,

x

)

r

a

d

i

a

n

s

[IMAGE alt='1378' src='RealAndImaginaryToPolar.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

The x rectangular component of x + yi.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### y

The y rectangular component of x + yi.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### r

The distance from the origin to the point.

r

x

y

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### theta

The angle for the line, r, from the origin to the point in radians.

theta

x

y

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=release-queue.html language=enus -->
## TOPIC 00080: Release Queue

- bundle_id: `g-web-development-api-ref`
- source_path: `release-queue.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/release-queue.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Releases a reference to a queue. queue A reference to a queue. force destroy A Boolean value that determines whether to release all references to the queue. Releasing all references to a queue destroys the queue, which deletes any elements in the queue and invalidates all references to the queue. Yo

Release Queue

Releases a reference to a queue.

[IMAGE alt='1378' src='ReleaseQueue.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### queue

A reference to a queue.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### force destroy

A Boolean value that determines whether to release all references to the queue.

Note

| True | The node releases all references to the queue. |
| --- | --- |
| False | The node only releases the specified reference to the queue. This does not destroy the queue unless a reference to the queue has only been obtained once. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### queue name

The name of the queue, if the queue is named.

[IMAGE alt='datatype_icon' src='/assets/img/i1dstr.png']

##### remaining elements

The array of elements that were in the queue before the node released the queue.

The first element in the array is the element from the front of the queue, and the last element in the array is the element from the back of the queue.

The data type of the array elements changes to match the data type of the queue elements.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

Transferring Data Between Loops Using Queue Nodes

#### Releasing Multiple References to the Same Queue

If you obtain a reference to the same queue multiple times, you can release multiple references to that queue by calling Release Queue up to the same number of times that you obtained the reference. Releasing all references to a queue destroys the queue and deletes any elements in the queue.

If you are not using a loop to release references as they are obtained or otherwise keeping track of the number of times you obtain a reference, you can also destroy a queue with a single Release Queue node using force destroy?.

Parent topic:

Queue Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=rotate-string.html language=enus -->
## TOPIC 00081: Rotate String

- bundle_id: `g-web-development-api-ref`
- source_path: `rotate-string.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/rotate-string.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Moves the first character of a string to the end of the string. The remaining characters move forward one position. For example, the string abcd becomes bcda. string The string you want to modify. This input can also be any data type that contains only strings, such as an array or cluster of strings

Rotate String

Moves the first character of a string to the end of the string.

The remaining characters move forward one position. For example, the string abcd becomes bcda.

[IMAGE alt='1378' src='RotateString.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### string

The string you want to modify.

This input can also be any data type that contains only strings, such as an array or cluster of strings.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### first char last

The rotated string.

string

Parent topic:

String Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=round-to-nearest.html language=enus -->
## TOPIC 00082: Round to Nearest

- bundle_id: `g-web-development-api-ref`
- source_path: `round-to-nearest.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/round-to-nearest.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Expresses the input to the nearest round integer. x An input to this operation. This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. nearest integer value The resulting nearest integer to

Round to Nearest

Expresses the input to the nearest round integer.

[IMAGE alt='1378' src='RoundToNearest.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### nearest integer value

The resulting nearest integer to the input value.

##### Complex Numbers

When x is complex, this node returns a complex number defined by the nearest integer to the real and imaginary parts of x. The following equation defines 
 nearest integer value:

nearest integer value(x) = nearest integer value(a) + 
 i * nearest integer value(b)

##### Rounding Behavior

If the value of the input is midway between two integers, this node returns the nearest even integer.

For example, if x is 1.5 or 2.5, nearest integer value is 2.

Note

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=scan-value.html language=enus -->
## TOPIC 00083: Scan Value

- bundle_id: `g-web-development-api-ref`
- source_path: `scan-value.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/scan-value.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the characters at the beginning of a string to a numeric value, using format specifiers to determine the representation and precision of the resulting number. This node also returns the remainder of the input string that follows the converted value. string The string you want to scan for a

Scan Value

Converts the characters at the beginning of a string to a numeric value, using format specifiers to determine the representation and precision of the resulting number.

This node also returns the remainder of the input string that follows the converted value.

[IMAGE alt='1378' src='ScanValue.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### string

The string you want to scan for a numeric value.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### format string

A string that uses format specifiers to determine how to convert the input text into a numeric value.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### default

A numeric value whose representation determines the representation of value.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### output string

The characters in string that follow format string. If there is no match for format string, this node returns string in its entirety.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### value

A portion of string converted into a numeric value according to the format specifiers in format string.

format string

default

If the input string represents a number outside the range of the representation of this output, this output returns the maximum or minimum value for the representation. For example, if the input string is 300, and the representation of this output is an 8-bit signed integer, this output returns 127.

Parent topic:

String Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=scroll-to-end.html language=enus -->
## TOPIC 00084: Scroll To End

- bundle_id: `g-web-development-api-ref`
- source_path: `scroll-to-end.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/scroll-to-end.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the vertical scroll position to the end of the string you specify. User interactions to scroll within the string control override this node. reference in Reference to the string. error in Error conditions that occur before this node runs. The node responds to this input according to standard er

Scroll To End

Sets the vertical scroll position to the end of the string you specify.

User interactions to scroll within the string control override this node.

[IMAGE alt='1378' src='ScrollToEnd.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### reference in

Reference to the string.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### reference out

Reference to the string.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

String Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=search-split-string.html language=enus -->
## TOPIC 00085: Search/Split String

- bundle_id: `g-web-development-api-ref`
- source_path: `search-split-string.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/search-split-string.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Divides a single string into two substrings. This node searches a string for the string or character in search string/char and splits the string when it finds a match. This node returns two strings: the substring before the match, and the match plus the rest of the original string. string The input

Search/Split String

Divides a single string into two substrings.

This node searches a string for the string or character in search string/char and splits the string when it finds a match. This node returns two strings: the substring before the match, and the match plus the rest of the original string.

[IMAGE alt='1378' src='SearchOrSplitString.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### string

The input string the node searches or splits.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### search string/char

The string or character to search for in the input string.

If you do not wire this input or it contains an empty string, the function splits the string at the specified offset.

Default value: 
 -

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### offset

Number of characters into the string at which the node begins searching.

The offset of the first character in the string is 0. If the offset is unwired or less than 0, the node interprets the offset as 0.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### substring before match

Portion of the string before the search string or before the offset if the search string is unwired. If the node does not find the search string, this output returns the entire string.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### match and rest of string

The search string and all subsequent characters in the string. If the node does not find the search string, this output returns an empty string.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### offset of match

The position of the search string/char in the string. If there is no match, this output returns 
-1.

#### Reducing Performance Burden

Characters in UTF-8 can be multiple bytes so string nodes count the number of characters in a string instead of jumping to a point in memory. Since the length and offset parameters are in units of characters, avoid nesting this node with large strings because that can create exponential functions that carry a higher performance burden.

Parent topic:

String Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=search-waveform.html language=enus -->
## TOPIC 00086: Search Waveform

- bundle_id: `g-web-development-api-ref`
- source_path: `search-waveform.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/search-waveform.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the timestamp values of the waveform that correspond to a y-axis input value. tolerance The amount, in percentage, values may differ from the input value and still produce a match. Default value: 0.01 waveform The waveform you want to search for a particular data value. Default value: empty

Search Waveform

Returns the timestamp values of the waveform that correspond to a y-axis input value.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### tolerance

The amount, in percentage, values may differ from the input value and still produce a match.

Default value: 0.01

[IMAGE alt='datatype_icon' src='/assets/img/cmsdt.png']

##### waveform

The waveform you want to search for a particular data value.

Default value: empty

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### value

The data value for which you want to search.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### start index

Point in the waveform data where the search begins. The node returns an error if start index is out of range for the waveform.

Default value: 0—Corresponds to the beginning of the waveform.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Default value: No error

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/i1di32.png']

##### indices of fits

An array of indexes of all values that meet the input value and tolerance criteria.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### index of best fit

The index of the data value that best matches the input value.

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### time of best fit

The timestamp value where the data value that best matches the input value was found.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/i1dtimestamp.png']

##### times of fits

An array of all timestamp values that meet the input value and tolerance criteria.

Parent topic:

Analog Waveform Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=storage-nodes.html language=enus -->
## TOPIC 00087: Storage Nodes

- bundle_id: `g-web-development-api-ref`
- source_path: `storage-nodes.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/storage-nodes.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Access data via files.

Storage Nodes

Access data via files.

Write Delimited Spreadsheet

Converts data to a text string and writes the string to a file.

<!--NI_TOPIC bundle=g-web-development-api-ref path=string-constant.html language=enus -->
## TOPIC 00088: String Constant

- bundle_id: `g-web-development-api-ref`
- source_path: `string-constant.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/string-constant.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a text string that you enter on the diagram.

String Constant

Represents a text string that you enter on the diagram.

[IMAGE alt='1378' src='Literal.String.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=g-web-development-api-ref path=string-subset.html language=enus -->
## TOPIC 00089: String Subset

- bundle_id: `g-web-development-api-ref`
- source_path: `string-subset.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/string-subset.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a portion, or substring, of a string. string The string from which you want to obtain a subset. offset The number of characters into the input string at which this node begins its operation. The offset of the first character in the input string is 0. If offset is beyond the end of the input

String Subset

Returns a portion, or substring, of a string.

[IMAGE alt='1378' src='StringSubset.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### string

The string from which you want to obtain a subset.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### offset

The number of characters into the input string at which this node begins its operation.

The offset of the first character in the input string is 0. If offset is beyond the end of the input string, this node returns an empty string.

Note

16

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### length

The number of characters you want to include in the substring.

If length is negative or 0, this node returns an empty string.

Note

Default value: The entire length of string minus offset.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### substring

The portion of the input string that is the specified length beginning at the offset.

Note

#### Reducing Performance Burden

Characters in UTF-8 can be multiple bytes so string nodes count the number of characters in a string instead of jumping to a point in memory. Since the length and offset parameters are in units of characters, avoid nesting this node with large strings because that can create exponential functions that carry a higher performance burden.

Parent topic:

String Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=stringcontrol-class.html language=enus -->
## TOPIC 00090: StringControl

- bundle_id: `g-web-development-api-ref`
- source_path: `stringcontrol-class.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/stringcontrol-class.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the properties in the StringControl class to read and write the elements of a string.

StringControl

Use the properties in the StringControl class to read and write the elements of a string.

Control

Use the properties in the Control class to read and write the elements of a control.

EnableWrap

Boolean value that determines whether to wrap text.

HorizontalScrollBarVisibility

Enum value that determines whether to show the horizontal scrollbar.

SelectAllOnFocus

Boolean value that determines whether to select all the text in the control when the control receives focus.

ShowEscapeSequences

Boolean value that determines whether to show escape sequences in the text.

VerticalScrollBarVisibility

Enum value that determines whether to show the vertical scrollbar.

Parent topic:

Control

<!--NI_TOPIC bundle=g-web-development-api-ref path=stringcontrol-verticalscrollbarvisibility.html language=enus -->
## TOPIC 00091: VerticalScrollBarVisibility

- bundle_id: `g-web-development-api-ref`
- source_path: `stringcontrol-verticalscrollbarvisibility.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/stringcontrol-verticalscrollbarvisibility.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enum value that determines whether to show the vertical scrollbar. None Does not show the vertical scrollbar. Automatic Automatically determines whether to show the vertical scrollbar, depending on the current text of the string control.

VerticalScrollBarVisibility

Enum value that determines whether to show the vertical scrollbar.

| None | Does not show the vertical scrollbar. |
| --- | --- |
| Automatic | Automatically determines whether to show the vertical scrollbar, depending on the current text of the string control. |

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

Parent topic:

StringControl

<!--NI_TOPIC bundle=g-web-development-api-ref path=tabcontrol-activetab.html language=enus -->
## TOPIC 00092: ActiveTab

- bundle_id: `g-web-development-api-ref`
- source_path: `tabcontrol-activetab.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/tabcontrol-activetab.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the index of the active tab. Use the properties of the TabItem class to read and write elements of the active tab.

ActiveTab

Gets or sets the index of the active tab. Use the properties of the TabItem class to read and write elements of the active tab.

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

Parent topic:

TabControl

<!--NI_TOPIC bundle=g-web-development-api-ref path=tabitem-class.html language=enus -->
## TOPIC 00093: TabItem

- bundle_id: `g-web-development-api-ref`
- source_path: `tabitem-class.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/tabitem-class.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the properties of the TabItem class to read and write the elements of an item in a tab control.

TabItem

Use the properties of the TabItem class to read and write the elements of an item in a tab control.

Enabled

Boolean value that determines whether the control is enabled or disabled.

Name

Name of the object.

Visible

Boolean value that determines whether to display the object.

<!--NI_TOPIC bundle=g-web-development-api-ref path=table-class.html language=enus -->
## TOPIC 00094: Table

- bundle_id: `g-web-development-api-ref`
- source_path: `table-class.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/table-class.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Allows you to read and write the elements of a table.

Table

Allows you to read and write the elements of a table.

Control

Use the properties in the Control class to read and write the elements of a control.

ColumnHeaders

Array of strings in the column headers. Each string maps to the column of the same index.

Parent topic:

Control

<!--NI_TOPIC bundle=g-web-development-api-ref path=text-class.html language=enus -->
## TOPIC 00095: Text

- bundle_id: `g-web-development-api-ref`
- source_path: `text-class.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/text-class.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the properties of the Text class to read and write the elements of a text control.

Text

Use the properties of the Text class to read and write the elements of a text control.

Decoration

Use the properties in the Decoration class to read and write the elements of user interface decorations, such as images, lines, or shapes.

Text

Text displayed in the control. For switches and LED controls, this property reads and writes the text for the true and false states.

Parent topic:

Decoration

<!--NI_TOPIC bundle=g-web-development-api-ref path=threshold-1d-array.html language=enus -->
## TOPIC 00096: Threshold 1D Array

- bundle_id: `g-web-development-api-ref`
- source_path: `threshold-1d-array.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/threshold-1d-array.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Interpolates points in a 1D array that represents a 2D non-descending graph. This node compares a threshold to the values in an array, starting at a specified index, until it finds a pair of consecutive elements such that the threshold is greater than the value of the first element and less than or

Threshold 1D Array

Interpolates points in a 1D array that represents a 2D non-descending graph.
 This node compares a threshold to the values in an array, starting at a specified index, until it finds a pair of consecutive elements such that the threshold is greater than the value of the first element and less than or equal to the value of the second element.

[IMAGE alt='1378' src='Threshold1DArray.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### array of numbers or points

An array of numbers or an array of points where each point is a cluster of x- and y-coordinates.

If this input is an array of numbers, this node assumes the x-coordinates are the same as the indexes of the array itself.

If this input is an array of points, this node uses the second elements in the clusters, or the y-coordinates, to obtain a fractional index that it then uses to interpolate the corresponding x value.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### threshold y

The threshold value for the node. If threshold y is less than or equal to the array value at start index, the node returns start index for fractional index or x. If threshold y is greater than every value in the array, the node returns the index of the last value. If the array is empty, the node returns 
NaN.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### start index

The index to start interpolation.

Default value: 0—The node returns the result calculated from the entire array rather than a specified section of the array.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### fractional index or x

The interpolated result calculated for the array of numbers or points 1D input array.

If array of numbers or points is an array of points where each point is a cluster of x- and y-coordinates, fractional index or x is the interpolated x value corresponding to the interpolated position of threshold y among the y-coordinates, rather than the fractional index of the array. fractional index or x returns the interpolated x value associated with the given y value if you graphed the points.

#### Examples

| array of numbers or points | start index | threshold y | fractional index or x | comments |
| --- | --- | --- | --- | --- |
| [4, 5, 5, 6] | 0 | 5 | 1 | The output is 1, corresponding to the index of the first value of 5 the node finds. |
| [2.3, 5.2, 7.8, 7.9, 10.0] | 0 | 6.5 | 1.5 | The output is 1.5 because 6.5 is halfway between 5.2 (index 1) and 7.8 (index 2). |
| [0, 1, 2, 3, 4, 9.1, 10.3, 12.9, 15.5] | 5 | 14.2 | 7.5 | threshold y falls between elements 7 and 8 because 14.2 is midway between 12.9 and 15.5. Therefore, the output is 7.5, halfway between 7 and 8. |
| Array of points [(1,1), (2,2), (3,3), (4,4), (-2.5,5), (0,6) | 0 | 5.5 | -1.25 | The output is not an index value of 4.5 as it would be for a numeric array, but rather an x value of -1.25, which is the interpolated x value associated with the given y value if you graphed the points. |

#### Method for Calculating Fractional Index

This node calculates the fractional distance between the first value and threshold y and returns the fractional index at which threshold y would be placed within array of numbers or points using linear interpolation.

#### Use Threshold 1D Array Only with Non-Descending Arrays

This node only returns a reliable fractional index or x result for non-descending arrays. This node might return unexpected data for the following reasons:

- This node does not recognize the index of a negative slope crossing.
- This node does not return multiple fractional index or x results if the input array crosses threshold y at multiple points.
- This node returns the start index value if threshold y is less than the value at start index .

Use Threshold Detector for more advanced analysis of arrays.

Parent topic:

Array Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=to-double-precision-float.html language=enus -->
## TOPIC 00097: To Double Precision Float

- bundle_id: `g-web-development-api-ref`
- source_path: `to-double-precision-float.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/to-double-precision-float.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a number to a double-precision, floating-point number. number An input to this operation. This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA When you

To Double Precision Float

Converts a number to a double-precision, floating-point number.

[IMAGE alt='1378' src='ToDoublePrecisionFloat.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### number

An input to this operation.

This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### double precision float

Result of the conversion.

This output assumes the same data type structure as 
 number.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=tree-nodes.html language=enus -->
## TOPIC 00098: Tree Nodes

- bundle_id: `g-web-development-api-ref`
- source_path: `tree-nodes.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/tree-nodes.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Modify trees.

Tree Nodes

Modify trees.

Panel Manipulation Nodes

Configure and manipulate controls and panels.

Open Item

Expands an item in a tree control to display the child items.

Close Item

Closes an item in a tree control to hide the child items.

Parent topic:

Panel Manipulation Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=tree-selection.html language=enus -->
## TOPIC 00099: Selection

- bundle_id: `g-web-development-api-ref`
- source_path: `tree-selection.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/tree-selection.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Hierarchical location of the selected item. Selection can be a string or an array of strings, depending on the selection mode of the tree control. An empty string or array represents no selection.

Selection

Hierarchical location of the selected item.

Selection can be a string or an array of strings, depending on the
 selection mode of the tree control. An empty string or array represents no
 selection.

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

Parent topic:

Tree

<!--NI_TOPIC bundle=g-web-development-api-ref path=trigonometric-nodes.html language=enus -->
## TOPIC 00100: Trigonometric Nodes

- bundle_id: `g-web-development-api-ref`
- source_path: `trigonometric-nodes.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/trigonometric-nodes.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`

Trigonometric Nodes

Cosecant

x

Cosine

x

Cotangent

x

Inverse Cosecant

x

Inverse Cosine

x

Inverse Cotangent

x

Inverse Secant

x

Inverse Sine

x

Inverse Tangent

x

Inverse Tangent (2 Input)

y

x

Secant

x

Sinc

x

x

Sine

x

Sine and Cosine

x

Tangent

x

<!--NI_TOPIC bundle=g-web-development-api-ref path=waveform-duration.html language=enus -->
## TOPIC 00101: Waveform Duration

- bundle_id: `g-web-development-api-ref`
- source_path: `waveform-duration.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/waveform-duration.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the duration of the specified waveform using the following equation: duration = (number of samples-1) x dx. open interval Interval over which the specified waveform extends. For example, assume a waveform contains 3 data elements at t = {0, dt, 2dt}. An open interval defines the waveform as

Waveform Duration

Computes the duration of the specified waveform using the following equation: 
*duration* = (*number of samples*-1) x *dx*.

[IMAGE alt='1378' src='WDT_Waveform_Duration_DBL.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### open interval

Interval over which the specified waveform extends.

t

dt

dt

t

dt

t

dt

| True | The specified waveform extends over an open interval. |
| --- | --- |
| False | The specified waveform extends over a closed interval. |

Default value: True

[IMAGE alt='datatype_icon' src='/assets/img/cmsdt.png']

##### waveform

Waveform for which you want the duration.

This input accepts a waveform or a digital waveform.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### duration

Duration of the waveform.

Parent topic:

Waveform Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=waveform-min-max.html language=enus -->
## TOPIC 00102: Waveform Min Max

- bundle_id: `g-web-development-api-ref`
- source_path: `waveform-min-max.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/waveform-min-max.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines the maximum and minimum values and their associated timestamp values for a waveform. waveform The waveform for which you want to retrieve the maximum and minimum values. max time The timestamp value corresponding to the maximum data value. Y max The maximum data value of the waveform. Y m

Waveform Min Max

Determines the maximum and minimum values and their associated timestamp values for a waveform.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cmsdt.png']

##### waveform

The waveform for which you want to retrieve the maximum and minimum values.

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### max time

The timestamp value corresponding to the maximum data value.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### Y max

The maximum data value of the waveform.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### Y min

The minimum data value of the waveform.

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### min time

The timestamp value corresponding to the minimum data value.

Parent topic:

Analog Waveform Nodes

<!--NI_TOPIC bundle=g-web-development-api-ref path=waveform-nodes.html language=enus -->
## TOPIC 00103: Waveform Nodes

- bundle_id: `g-web-development-api-ref`
- source_path: `waveform-nodes.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development-api-ref/raw/resource/enus/waveform-nodes.html
- document_id: `g-web-development-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create waveforms and access their components.

Waveform Nodes

Create waveforms and access their components.

Align Waveform Timestamps

Replaces the timestamp value (t0) of each waveform in waveform array with the timestamp value of the waveform at the index position you specify.

Copy Waveform dt

Replaces the dt value of each waveform in the waveform array with the dt value of the waveform at the index position you specify.

Get Final Time Value

xf

x

duration

Get Waveform Subset

Retrieves a subset of a waveform at a specified time or index.

Get Waveform Time Array

Creates an array of timestamps based on the specified waveform.

Get XY Value

Returns the X and Y value of a waveform or digital data set.

Index Waveform Array

Selects one waveform out of an array of analog or digital waveforms by array index or channel name.

Scale Delta t

t

Waveform Duration

duration

number of samples

dx

Analog Waveform Nodes

Create analog waveforms and access their components.
