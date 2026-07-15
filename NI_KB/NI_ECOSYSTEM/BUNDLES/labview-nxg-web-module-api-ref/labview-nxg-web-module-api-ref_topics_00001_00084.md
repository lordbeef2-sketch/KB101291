# NI DOCUMENT BUNDLE: labview-nxg-web-module-api-ref

<!--NI_BUNDLE_CHUNK bundle=labview-nxg-web-module-api-ref start=1 end=84 -->
<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=add-array-elements.html language=enus -->
## TOPIC 00001: Add Array Elements

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `add-array-elements.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/add-array-elements.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the sum of all of the elements in a numeric array. numeric array An array of any number of dimensions. This input changes to waveform when the data type is a waveform. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this input has a default data type that

Add Array Elements

Returns the sum of all of the elements in a numeric array.

[IMAGE alt='1378' src='AddArrayElements.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### numeric array

An array of any number of dimensions. This input changes to waveform when the data type is a waveform.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### waveform

The waveform whose array of y values you want to use in this operation. This input becomes available when you wire a waveform to array.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### sum

The sum of all elements in the numeric array.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=boolean-array-to-number.html language=enus -->
## TOPIC 00002: Boolean Array to Number

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `boolean-array-to-number.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/boolean-array-to-number.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a Boolean array to an integer by interpreting the array as the binary representation of the number. If the number is signed, this node interprets the array as the two's complement representation of the number. The first element of the array corresponds to the least significant bit in the nu

Boolean Array to Number

Converts a Boolean array to an integer by interpreting the array as the binary representation of the number.
 If the number is signed, this node interprets the array as the two's complement representation of the number. The first element of the array corresponds to the least significant bit in the number.

[IMAGE alt='1378' src='BooleanArrayToNumber.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1dbool.png']

##### Boolean array

A 1D array of Boolean values.

This node truncates the 
 Boolean array if it is too long and pads it with Boolean False bits if the 
 Boolean array is too short.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### number

An integer that represents Boolean array.

#### Examples

| Boolean array | number |
| --- | --- |
| {False, False} | 0 |
| {True, False} | 1 |
| {False, True} | 2 |
| {True, True} | 3 |

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=bus-class.html language=enus -->
## TOPIC 00003: Bus

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `bus-class.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/bus-class.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the properties of the Bus class to read and write the elements of a bus.

Bus

Use the properties of the Bus class to read and write the elements of a bus.

PlotBase

Use the properties of the PlotBase class to read and write the elements of a plot, cursor, or bus.

Color

Color of the plot.

LineWidth

Line width of the plot.

Parent topic:

PlotBase

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=busy-state-nodes.html language=enus -->
## TOPIC 00004: Busy State Nodes

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `busy-state-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/busy-state-nodes.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enable or disable user interactions on the panel.

Busy State
 Nodes

Enable or disable user interactions on the panel.

Panel Manipulation Nodes

Configure and manipulate controls and panels.

Set Busy

Changes the cursor on the panel to the busy state and disables mouse and keyboard input on both the panel and the menu.

Unset Busy

Changes the cursor from the busy cursor to the default cursor and enables mouse clicks on both the panel and the menu.

Parent topic:

Panel Manipulation Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=carriage-return-constant.html language=enus -->
## TOPIC 00005: Carriage Return Constant

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `carriage-return-constant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/carriage-return-constant.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the UTF-8 CR value on the diagram. Use this constant when you do not want to type in the backslash code for the character.

Carriage Return Constant

Represents the UTF-8 
CR value on the diagram.

Use this constant when you do not want to type in the backslash code for the character.

[IMAGE alt='1378' src='Literal.String.Carriage_Return_Constant.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=close-http-handle.html language=enus -->
## TOPIC 00006: Close HTTP Handle

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `close-http-handle.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/close-http-handle.html
- document_id: `labview-nxg-web-module-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=close-item.html language=enus -->
## TOPIC 00007: Close Item

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `close-item.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/close-item.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes an item in a tree control to hide the child items. reference in Reference to the tree control. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error location Hierarchica

Close Item

Closes an item in a tree control to hide the child items.

[IMAGE alt='1378' src='CloseTreeItem.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### reference in

Reference to the tree control.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### location

Hierarchical location of the tree item to close.

If location is empty or unwired, the node closes all items in the tree.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### reference out

Reference to the tree control.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Tree Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=cluster-class.html language=enus -->
## TOPIC 00008: Cluster

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `cluster-class.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/cluster-class.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the properties in the Cluster class to read and write the elements of a cluster control.No properties are specific to this class.

Cluster

Use the properties in the Cluster class to read and write the elements of a cluster control.No properties are specific to this class.

Control

Use the properties in the Control class to read and write the elements of a control.

Parent topic:

Control

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=cluster-constant.html language=enus -->
## TOPIC 00009: Cluster Constant

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `cluster-constant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/cluster-constant.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a group, or cluster, of mixed-type data elements on the diagram.

Cluster Constant

Represents a group, or cluster, of mixed-type data elements on the diagram.

[IMAGE alt='1378' src='Literal.Cluster.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=cluster-controls.html language=enus -->
## TOPIC 00010: Cluster Controls

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `cluster-controls.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/cluster-controls.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Group data elements of a mixed type that logically belong together. What Is a Cluster? Clusters group data elements of mixed types. A cluster is similar to a record or a struct in text-based programming languages. Which Cluster Should I Use? You can choose from the following cluster types, and clust

Cluster Controls

Group data elements of a mixed type that logically belong together.

[IMAGE alt='1378' src='GUID-8FE65D23-9CF7-464A-A04F-79F73A15DC48-a5.png']

#### What Is a Cluster?

Clusters group data elements of mixed types. A cluster is similar to a record or a struct in text-based programming languages.

#### Which Cluster Should I Use?

You can choose from the following cluster types, and clusters can be nested:

| Use | Type |
| --- | --- |
| Groups a checkbox, numeric control, and string control together to input error information. | Error In |
| Groups a checkbox, numeric indicator, and string control together to display error information. | Error Out |
| Create a custom group by dragging and dropping controls, such as buttons, graphs, arrays, and so on, into the cluster shell. | Empty Cluster |

#### How Do I Reorder Cluster Elements?

You can reorder cluster elements by using the 
 Data items section on the 
 Item tab or by moving controls inside or outside the cluster. The order of the controls within the cluster is determined by the order in which you add them to the cluster.

#### How Do I Tab Through Cluster Elements?

Press Ctrl-Down Arrow or Ctrl-Up Arrow to tab through cluster elements, even nested clusters.

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=colorscale-class.html language=enus -->
## TOPIC 00011: ColorAxis

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `colorscale-class.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/colorscale-class.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the properties of the ColorAxis class to read and write the elements of a color axis.

ColorAxis

Use the properties of the ColorAxis class to read and write the elements of a color
 axis.

Scale

Use the properties of the Scale class to read and write the elements of a scale on a graph, chart, or numeric control such as a slider.

Range

Range of values, defined as a cluster. The range of values depends on the G Type of the control.

Parent topic:

Scale

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=comparison-nodes.html language=enus -->
## TOPIC 00012: Comparison Nodes

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `comparison-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/comparison-nodes.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`

Comparison Nodes

Decimal Digit?

Returns True if a value represents a decimal digit ranging from 0 through 9. Otherwise, this node returns False.

Empty Array?

Returns True if an array is empty. Otherwise, this node returns False.

Empty String or Path?

Returns whether the input is an empty string or path.

Equal?

Compares two values and returns True only if the values are equal to each other.

Equal to 0?

Returns True if a value is equal to 0. Otherwise, this node returns False.

Greater?

Compares two values and returns True only if the first value is greater than the second value.

Greater or Equal?

Compares two values and returns True only if the first value is greater than or equal to the second value.

Greater or Equal to 0?

Returns True if a value is greater than or equal to 0. Otherwise, this node returns False.

Greater Than 0?

Returns True if a value is greater than 0. Otherwise, this node returns False.

Hexadecimal Digit?

Returns True if a value represents a hexadecimal digit ranging from 0 through 9, A through F, or a through f. Otherwise, this node returns False.

Less?

Returns True if the first value is less than the second value. Otherwise, this node returns False.

Less or Equal?

Returns True if the first value is less than or equal to the second value. Otherwise, this node returns False.

Less or Equal to 0?

Returns True if a value is less than or equal to 0. Otherwise, this node returns False.

Less Than 0?

Returns True if a value is less than 0. Otherwise, this node returns False.

Not a Number/Path/Refnum?

Returns True if a value is not a number, not a path, or not a refnum. Otherwise, this node returns False.

Not Equal?

Compares two values and returns True only if the values are not equal to each other.

Not Equal to 0?

Returns True if a value is not equal to 0. Otherwise, this node returns False.

Octal Digit?

Returns True if a value represents an octal digit ranging from 0 through 7. Otherwise, this node returns False.

White Space?

Returns True if a value represents a white space character, such as Space, Tab, Newline, Carriage Return, Form Feed, or Vertical Tab. Otherwise, this node returns False.

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=complex-conjugate.html language=enus -->
## TOPIC 00013: Complex Conjugate

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `complex-conjugate.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/complex-conjugate.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Produces the complex conjugate of x + yi. x + yi A complex number. This input supports complex numbers, arrays or clusters of complex numbers, arrays of clusters of complex numbers, and waveforms. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this input has a de

Complex Conjugate

Produces the complex conjugate of x + y*i*.

[IMAGE alt='1378' src='ComplexConjugate.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccdb.png']

##### x + yi

A complex number.

This input supports complex numbers, arrays or clusters of complex numbers, arrays of clusters of complex numbers, and waveforms.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/icdb.png']

##### x - yi

The complex conjugate of x + yi.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=data-grid.html language=enus -->
## TOPIC 00014: Data Grid

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `data-grid.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/data-grid.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Group elements of various data types as rows on a table. The data grid control is a 1D array of clusters. Each row of the table is one cluster, and each element in a cluster represents one column. You can use the data grid control to configure hardware or to display data in a table.

Data Grid

Group elements of various data types as rows on a table.

The data grid control is a 1D array of clusters. Each row of the table is one cluster, and each element in a cluster represents one column.

You can use the data grid control to configure hardware or to display data in a table.

[IMAGE alt='1378' src='GUID-E5B69C4B-B03D-40B0-98F3-75EC3F3FDF99-a5.png']

Parent topic:

Array Controls

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=datagrid-class.html language=enus -->
## TOPIC 00015: DataGrid

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `datagrid-class.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/datagrid-class.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the properties in the DataGrid class to read and write the elements of a data grid.

DataGrid

Use the properties in the DataGrid class to read and write the elements of a data grid.

Control

Use the properties in the Control class to read and write the elements of a control.

Parent topic:

Control

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=decimal-string-to-number.html language=enus -->
## TOPIC 00016: Decimal String to Number

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `decimal-string-to-number.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/decimal-string-to-number.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the numeric characters in a string to a decimal integer. string The string that you want to convert. This input can also be any data type that contains only strings, such as an array or cluster of strings. offset The number of characters into the input string at which this node begins its o

Decimal String to Number

Converts the numeric characters in a string to a decimal integer.

[IMAGE alt='1378' src='DecimalStringToNumber.png']

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

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### default

A numeric value whose representation determines the representation of 
number.

Default value: 32-bit signed integer

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### offset past number

The index in string of the first character following the number.

If string is an array of strings, offset past number reflects the offset within the last string.

Note

16

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### number

The result of converting string into a number.

number

string

string

number

If the input string represents a number outside the range of the representation of this output, this output returns the maximum or minimum value for the representation. For example, if the input string is 300, and the representation of this output is an 8-bit signed integer, this output returns 127.

#### Examples

string

offset

default

number

| string | offset | default | offset past number | number | Comments |
| --- | --- | --- | --- | --- | --- |
| 13ax | 0 | 0 | 2 | 13 | — |
| –4.8bcde conversion | 0 | 0 | 2 | –4 | Because an integer is being converted, conversion stops at the decimal point. |
| a49b | 0 | –9 | 0 | –9 | default is used since no digits were read. |

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=decimate-1d-array.html language=enus -->
## TOPIC 00017: Decimate 1D Array

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `decimate-1d-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/decimate-1d-array.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Divides the elements of an array into multiple output arrays, placing elements into the outputs successively. This node drops any elements that cause the output arrays to have different lengths. array A 1D array of any type. Data Type Changes on FPGA When you add this node to a document targeted to

Decimate 1D Array

Divides the elements of an array into multiple output arrays, placing elements into the outputs successively.

This node drops any elements that cause the output arrays to have different lengths.

[IMAGE alt='1378' src='DecimateArray.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### array

A 1D array of any type.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### decimated array

The node stores array[0] at index 0 of the first output array, array[1] is stored at index 0 of the second output array, array[n-1] at index 0 of the last output array, array[n] at index 1 of the first output array, and so on, where 
n is the number of output terminals for this node.

#### Examples

Decimate 1D Array

| array input | decimated array 1 | decimated array 2 | decimated array 3 | decimated array 4 | Comments |
| --- | --- | --- | --- | --- | --- |
| 1D array with 16 elements numbered 0 to 15 | {0,4,8,12} | {1,5,9,13} | {2,6,10,14} | {3,7,11,15} | Decimate 1D Array divides the array input between all decimated array outputs, element-by-element. |
| 1D array with 15 elements numbered 0 to 14 | {0,4,8} | {1,5,9} | {2,6,10} | {3,7,11} | Because Decimate 1D Array only returns arrays of the same size, all decimated array outputs drop the last element so that all of the arrays contain 3 elements. |

Parent topic:

Array Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=delete-registry-key.html language=enus -->
## TOPIC 00018: Delete Registry Key

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `delete-registry-key.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/delete-registry-key.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes a specific key or subkey. Incorrectly modifying the registry can damage Windows or prevent you from starting Windows. reference in Reference to the open registry key. subkey Name of a subkey of root key. A beginning backslash \ might cause an error. Default value: Empty string registry view

Delete Registry Key

Deletes a specific key or subkey.

Caution

[IMAGE alt='1378' src='Delete_Registry_Key.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### reference in

Reference to the open registry key.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### subkey

Name of a subkey of root key.

A beginning backslash 
 \ might cause an error.

Default value: Empty string

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### registry view

Value that specifies whether to delete a 32-bit key or a 64-bit key on a 64-bit operating system.

| Default | 0 | This node selects the type of key based on the software that is installed. For example, if a 64-bit product is installed, this node deletes a 64-bit key. |
| --- | --- | --- |
| KEY_WOW64_64KEY | 8 | This node deletes a 64-bit key. |
| KEY_WOW64_32KEY | 9 | This node deletes a 32-bit key. |

Default value: Default

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### reference out

Reference to the open registry key.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Registry Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=delete-variant-attribute.html language=enus -->
## TOPIC 00019: Delete Variant Attribute

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `delete-variant-attribute.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/delete-variant-attribute.html
- document_id: `labview-nxg-web-module-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=dequeue-element.html language=enus -->
## TOPIC 00020: Dequeue Element

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `dequeue-element.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/dequeue-element.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes an element from the front of a queue and returns the element. If the queue becomes invalid because the queue reference is released, then this node stops waiting and returns an error. queue A reference to a queue. timeout in milliseconds The number of milliseconds that the node waits for an e

Dequeue Element

Removes an element from the front of a queue and returns the element.

If the queue becomes invalid because the queue reference is released, then this node stops waiting and returns an error.

[IMAGE alt='1378' src='DequeueElement.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### queue

A reference to a queue.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### timeout in milliseconds

The number of milliseconds that the node waits for an element to become available in the queue if the queue is empty.

If an element becomes available in the queue during the wait, the node removes and returns the element and does not time out.

Default value: -1 — The node never times out.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### queue out

Reference to the queue.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### element

The element at the front of the queue.

The data type of this output changes to match the data type of the queue elements.

If the node times out or an error occurs, this output returns the default value of the element data type.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### timed out?

A Boolean value that indicates whether an element became available in the queue before the node timed out or if an error occurred.

| True | An element did not become available before the node timed out or this node generated an error. |
| --- | --- |
| False | An element did become available before the node timed out or an error occurred before this node executed. |

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

The node produces this output according to standard error behavior.

This node can return the following error codes.

| 1122 | The reference became invalid while the node was waiting for it. |
| --- | --- |

Note

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

Transferring Data Between Loops Using Queue Nodes

Parent topic:

Queue Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=destroy-user-event.html language=enus -->
## TOPIC 00021: Destroy User Event

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `destroy-user-event.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/destroy-user-event.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Releases a user event reference by destroying its associated user event refnum. Any Event Structures registered for this user event no longer receive the event. user event User event refnum created by a Create User Event node. error in Error conditions that occur before this node runs. Unlike most n

Destroy User Event

Releases a user event reference by destroying its associated user event refnum.
 Any Event Structures registered for this user event no longer receive the event.

[IMAGE alt='1378' src='DestroyUserEvent.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### user event

User event refnum created by a Create User Event node.

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

#### Programming Patterns

- Executing
 Code Based on a User Event

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=digital-waveform-t0.html language=enus -->
## TOPIC 00022: t0

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `digital-waveform-t0.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/digital-waveform-t0.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Start time of the waveform.

t0

Start time of the waveform.

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

Parent topic:

Digital Waveform

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=downgrade-to-warning.html language=enus -->
## TOPIC 00023: Downgrade to Warning

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `downgrade-to-warning.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/downgrade-to-warning.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Changes an error to a warning. error in An error cluster that you use to check for errors or warnings. Standard Error Behavior error out An error cluster including any values this node writes, removes, or replaces. If no values change, this node returns error in unchanged. Standard Error Behavior

Downgrade to Warning

Changes an error to a warning.

[IMAGE alt='1378' src='Downgrade_To_Warning.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

An error cluster that you use to check for errors or warnings.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

An error cluster including any values this node writes, removes, or replaces. If no values change, this node returns 
error in unchanged.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Error Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=elementary-charge.html language=enus -->
## TOPIC 00024: Elementary Charge Constant

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `elementary-charge.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/elementary-charge.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value 1.6021766208e-19. The elementary charge is the electric charge carried by a single proton, or equivalently, the opposite of the electric charge carried by a single electron.

Elementary Charge Constant

Returns the value 1.6021766208e-19. The elementary charge is the electric charge carried by a single proton, or equivalently, the opposite of the electric charge carried by a single electron.

[IMAGE alt='1378' src='Literal.Numeric.Elementary_Charge_Constant.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=end-of-line-constant.html language=enus -->
## TOPIC 00025: End of Line Constant

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `end-of-line-constant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/end-of-line-constant.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the end-of-line value on the diagram. The value is CR/LF (carriage return/linefeed). Use this constant when you do not want to type in the backslash code for the character.

End of Line Constant

Represents the end-of-line value on the diagram.

The value is 
 CR/LF (carriage return/linefeed).

Use this constant when you do not want to type in the backslash code for the character.

[IMAGE alt='1378' src='Literal.String.End_of_Line_Constant.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=enqueue-element-at-opposite-end.html language=enus -->
## TOPIC 00026: Enqueue Element At Opposite End

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `enqueue-element-at-opposite-end.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/enqueue-element-at-opposite-end.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds an element to the front of a queue. Queues typically use a first-in-first-out flow where data is enqueued at the back of the queue and dequeued in the front of the queue. In rare situations, you might want to interrupt this normal flow of data by adding an element to the front of the queue. For

Enqueue Element At Opposite End

Adds an element to the front of a queue.

Queues typically use a first-in-first-out flow where data is enqueued at the back of the queue and dequeued in the front of the queue. In rare situations, you might want to interrupt this normal flow of data by adding an element to the front of the queue. For example, you may want to use the queue as a stack structure or add high-priority elements to the front of the queue. After you add an element to the front of a queue, the next Dequeue Element node you call removes and returns that element.

If the queue becomes invalid because the queue reference is released, then this node stops waiting and returns an error.

[IMAGE alt='1378' src='EnqueueElementAtOppositeEnd.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### queue

A reference to a queue.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### element

The element you want to add to the front of the queue.

The data type of this input changes to match the data type of the elements in the queue.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### timeout in milliseconds

The number of milliseconds that the node waits for available space in the queue if the queue is full.

Note

Obtain Queue

Default value: -1 — The node never times out.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### queue out

Reference to the queue.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### timed out?

A Boolean value that indicates whether there is space available in the queue before the node times out or an error occurs.

| True | There was no space available in the queue before the node timed out, or this node generated an error. |
| --- | --- |
| False | There was space available in the queue before the node timed out, or an error occurred before this node executed. |

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

The node produces this output according to standard error behavior.

This node can return the following error codes.

| 1122 | The reference became invalid while the node was waiting for it. |
| --- | --- |

Note

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

Use Dequeue Element to remove and return the element after you enqueue it.

Parent topic:

Queue Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=enum-class.html language=enus -->
## TOPIC 00027: Enum

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `enum-class.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/enum-class.html
- document_id: `labview-nxg-web-module-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=enum-registry-keys.html language=enus -->
## TOPIC 00028: Enum Registry Keys

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `enum-registry-keys.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/enum-registry-keys.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enumerates subkeys of a specific key or subkey. Incorrectly modifying the registry can damage Windows or prevent you from starting Windows. reference in Reference to the open registry key. subkey info Set of parameters describing the subkey associated with reference in. numSubKeys Number of subkeys

Enum Registry Keys

Enumerates subkeys of a specific key or subkey.

Caution

[IMAGE alt='1378' src='Enum_Registry_Keys.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### reference in

Reference to the open registry key.

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### subkey info

Set of parameters describing the subkey associated with reference in.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### numSubKeys

Number of subkeys under the key specified by hKey.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### maxSubKeyLen

Length of the longest subkey name under the key specified by hKey.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### maxSubKeyClassLen

Length of the longest class name under the key specified by hKey.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### reference out

Reference to the open registry key.

[IMAGE alt='datatype_icon' src='/assets/img/i1dstr.png']

##### subkeys

An array of the names of all subkeys of the specified key.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

You can wire the subkey info output of the Query Registry Key Info node to the Enum Registry Keys node to get the subkey information of a specific key or subkey.

Parent topic:

Registry Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=enum-registry-values-simple.html language=enus -->
## TOPIC 00029: Enum Registry Values Simple

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `enum-registry-values-simple.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/enum-registry-values-simple.html
- document_id: `labview-nxg-web-module-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=equal-to-0.html language=enus -->
## TOPIC 00030: Equal to 0?

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `equal-to-0.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/equal-to-0.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns True if a value is equal to 0. Otherwise, this node returns False. x An input to this operation. This input supports numeric scalar values, clusters, timestamp values, waveforms, and arrays of numbers. For waveforms, the node compares only the y values of this input. Data Type Changes on FPG

Equal to 0?

Returns True if a value is equal to 0. Otherwise, this node returns False.

[IMAGE alt='1378' src='IsEqualTo0.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports numeric scalar values, clusters, timestamp values, waveforms, and arrays of numbers.

For waveforms, the node compares only the y values of this input.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### x = 0?

Boolean result of the operation.

This output assumes the same data type structure as 
 x.

Parent topic:

Comparison Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=event-loop.html language=enus -->
## TOPIC 00031: Event Loop

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `event-loop.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/event-loop.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an Event Structure within a While Loop.

Event Loop

Creates an Event Structure within a While Loop.

Parent topic:

Program Flow Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=format-date-time-string.html language=enus -->
## TOPIC 00032: Format Date and Time String

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `format-date-time-string.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/format-date-time-string.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a timestamp or numeric value into a string that displays the corresponding time. This node calculates date and time string by copying time format string and replacing each of the time format codes with the corresponding values. time format string Format of the output string. The syntax for

Format Date and Time String

Converts a timestamp or numeric value into a string that displays the corresponding time.

This node calculates date and time string by copying time format string and replacing each of the time format codes with the corresponding values.

[IMAGE alt='1378' src='FormatDateTimeString.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### time format string

Format of the output string.

The syntax for this string is 
 %<optional #><format code>.

The 
 # modifier removes the leading zeros from the output of 
 %d, %H, %I, %j, %m, %M, %S, %U, %w, %W, %X, %y, %Y. By default, the output contains leading zeros as necessary to ensure a constant field width.

This node uses the following format codes to interpret timestamp:

| Time Format Code | Definition | Values |
| --- | --- | --- |
| %a | Abbreviated weekday name. This node returns a numeric value for systems that do not support abbreviated names, such as Chinese and Korean. | Sun - Sat |
| %A | Full weekday name | Sunday - Saturday |
| %b | Abbreviated month name. This node returns a numeric value for systems that do not support abbreviated names, such as Chinese and Korean. | Jan - Dec |
| %B | Full month name | January - December |
| %c | Locale-specific default date and time |  |
| %d | Day of month | 01-31 |
| %H | Hour (24-hour clock) | 00-23 |
| %I | Hour (12-hour clock) | 01-12 |
| %j | Day number of the year | 001-366 |
| %m | Month number | 01-12 |
| %M | Minute | 00-59 |
| %p | AM or PM flag | AM or PM |
| %S | Second | 00-59 |
| %<digit>u | Fractional seconds with <digit> precision |  |
| %U | Week number of the year, with the first Sunday as the first day of the first week | 00-53 |
| %w | Weekday as a decimal number, with 0 representing Sunday | 0-6 |
| %W | Week number of the year, with the first Sunday as the first day of the first week | 00-53 |
| %x | Locale-specific date |  |
| %.1x | Long date format |  |
| %.2x | Abbreviated long date format. This node returns a numeric value for systems that do not support abbreviated names, such as Chinese and Korean. |  |
| %X | Locale-specific time |  |
| %y | Year within century | 00-99 |
| %Y | Year, including the century | 1997, for example |
| %z | Difference between locale time and universal time | HH:MM:SS |
| %Z | Time zone name or abbreviation |  |
| Literal text | Literal text |  |

Default value: 
 %c—Corresponds to the locale-specific date/time representation.

[IMAGE alt='datatype_icon' src='/assets/img/ctimestamp.png']

##### timestamp

The time that you want to convert.

The year in this timestamp must be between 1600 and 3000.

If you wire a numeric value to this input, the node interprets the number as the time-zone-independent number of seconds that have elapsed since 12:00 a.m. on January 1, 1904, Universal Time [01-01-1904 00:00:00]. The node interprets a negative number as the number of seconds before this time.

Default value: The current date and time

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### UTC format

Boolean value that specifies whether the output string is in Universal Time or in the configured time zone for the computer.

| True | date and time string is in Universal Time. |
| --- | --- |
| False | date and time string is in the configured time zone for the computer. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### date and time string

timestamp formatted by the code specified in time format string.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=image-class.html language=enus -->
## TOPIC 00033: Image

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `image-class.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/image-class.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the properties of the Image class to read and write the elements of a graphic.

Image

Use the properties of the Image class to read and write the elements of a graphic.

Decoration

Use the properties in the Decoration class to read and write the elements of user interface decorations, such as images, lines, or shapes.

Parent topic:

Decoration

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=index-array.html language=enus -->
## TOPIC 00034: Index Array

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `index-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/index-array.html
- document_id: `labview-nxg-web-module-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=index-waveform-array.html language=enus -->
## TOPIC 00035: Index Waveform Array

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `index-waveform-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/index-waveform-array.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Selects one waveform out of an array of analog or digital waveforms by array index or channel name. waveform array Array of waveforms from which to extract a single waveform. This input accepts a 1D array of waveforms or a 1D array of digital waveforms. index Index of the waveform to extract from th

Index Waveform Array

Selects one waveform out of an array of analog or digital waveforms by array index or channel name.

[IMAGE alt='1378' src='WDT_Index_Channel_DBL.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1dmsdt.png']

##### waveform array

Array of waveforms from which to extract a single waveform.

This input accepts a 1D array of waveforms or a 1D array of digital waveforms.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### index

Index of the waveform to extract from the waveform array.

This input is available only when you wire a numeric to channel name. If you wire a string to index, this input changes to channel name.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Channel name of the waveform to extract from the waveform array.

This input is available only when you wire a string to index. If you wire a numeric to channel name, this input changes to index.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/imsdt.png']

##### waveform

Waveform selected from the array of waveforms.

This output is a digital waveform when you wire a digital waveform array to waveform array.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Waveform Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=interoperability-nodes.html language=enus -->
## TOPIC 00036: Interoperability Nodes

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `interoperability-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/interoperability-nodes.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Integrate communication with local applications.

Interoperability Nodes

Integrate communication with local applications.

Write to System Log

nierrlog

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=inverse-cotangent.html language=enus -->
## TOPIC 00037: Inverse Cotangent

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `inverse-cotangent.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/inverse-cotangent.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the inverse cotangent of a specified value (x) in radians. x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this input has a

Inverse Cotangent

Computes the inverse cotangent of a specified value (x) in radians.

[IMAGE alt='1378' src='InverseCotangent.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### arccot

Result of the operation.

This output assumes the same numeric representation as 
 x.

Parent topic:

Trigonometric Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=inverse-tangent-2-input.html language=enus -->
## TOPIC 00038: Inverse Tangent (2 Input)

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `inverse-tangent-2-input.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/inverse-tangent-2-input.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the arctangent of one value divided by another value (y/x). This node can compute the arctangent for angles in any of the four quadrants of the x-y plane, whereas the Inverse Tangent node computes the arctangent in only two quadrants. y An input to this operation. This input supports scalar

Inverse Tangent (2 Input)

Computes the arctangent of one value divided by another value (y/x).

This node can compute the arctangent for angles in any of the four quadrants of the x-y plane, whereas the Inverse Tangent node computes the arctangent in only two quadrants.

[IMAGE alt='1378' src='InverseTangentXY.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### y

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### atan2(y,x)

Result of the operation. 
atan2(y,x) falls in the range [-pi, pi].

x

y

atan2(y,x)

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

Parent topic:

Trigonometric Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=layouts.html language=enus -->
## TOPIC 00039: Layouts

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `layouts.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/layouts.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Organize the appearance of controls and indicators or display the panel of other VIs. When Should I Use a Tab Control? Tab controls are useful when you have several panel objects that are used together or during a specific phase of operation. For example, you might have a VI that requires the user t

Layouts

Organize the appearance of controls and indicators or display the panel of other VIs.

[IMAGE alt='1378' src='GUID-85F8BB75-2862-4AEC-A74F-56C1F26564EF-a5.png']

#### When Should I Use a Tab Control?

Tab controls are useful when you have several panel objects that are used together or during a specific phase of operation. For example, you might have a VI that requires the user to first configure several settings before a test can start, then allows the user to modify aspects of the test as it progresses, and finally allows the user to display and store only pertinent data.

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=less-or-equal.html language=enus -->
## TOPIC 00040: Less or Equal?

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `less-or-equal.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/less-or-equal.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns True if the first value is less than or equal to the second value. Otherwise, this node returns False. This node can also compare an array or cluster of a data type to a scalar of the same data type and produce an array or cluster of Boolean values. x First value to compare. x must be either

Less or Equal?

Returns True if the first value is less than or equal to the second value. Otherwise, this node returns False.

This node can also compare an array or cluster of a data type to a scalar of the same data type and produce an array or cluster of Boolean values.

[IMAGE alt='1378' src='IsLessOrEqual.png']

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

##### x <= y?

Boolean result of the operation.

When you compare two arrays, 
 x <= y? is a scalar in 
 Compare Aggregates mode and a Boolean array in 
 Compare Elements mode (default).

#### Behavior with Array Inputs

Less or Equal?

Compare Aggregates

Less or Equal?

Compare Aggregates

Parent topic:

Comparison Nodes

Related information:

- Comparison Modes for Array and Cluster Data

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=line-class.html language=enus -->
## TOPIC 00041: Line

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `line-class.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/line-class.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the properties of the Line class to read and write the elements of a straight line.

Line

Use the properties of the Line class to read and write the elements of a straight line.

Decoration

Use the properties in the Decoration class to read and write the elements of user interface decorations, such as images, lines, or shapes.

Parent topic:

Decoration

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=machine-epsilon.html language=enus -->
## TOPIC 00042: Machine Epsilon

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `machine-epsilon.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/machine-epsilon.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the round-off error for a floating-point number with a given precision. Use the machine epsilon constant to compare whether two floating-point numbers are equivalent.

Machine Epsilon

Represents the round-off error for a floating-point number with a given precision.
 Use the machine epsilon constant to compare whether two floating-point numbers are equivalent.

[IMAGE alt='1378' src='Literal.Numeric.Machine_Epsilon.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=natural-log-of-ten.html language=enus -->
## TOPIC 00043: ln10

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `natural-log-of-ten.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/natural-log-of-ten.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the value 2.3025850929940459.

ln10

Represents the value 2.3025850929940459.

[IMAGE alt='1378' src='Literal.Numeric.ln10.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=number-to-octal-string.html language=enus -->
## TOPIC 00044: Number to Octal String

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `number-to-octal-string.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/number-to-octal-string.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a numeric value to a string that shows the number's octal format. number A number to be converted into a string. This input can also be any data type that contains only numbers, such as an array of numbers or a cluster of numbers. If this input is floating-point, this node rounds it to a 64

Number to Octal String

Converts a numeric value to a string that shows the number's octal format.

[IMAGE alt='1378' src='NumberToOctalString.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### number

A number to be converted into a string.

This input can also be any data type that contains only numbers, such as an array of numbers or a cluster of numbers. If this input is floating-point, this node rounds it to a 64-bit integer before conversion.

[IMAGE alt='datatype_icon' src='/assets/img/ci16.png']

##### width

A number specifying how many characters to use to express number as a string.

If width is less than the number of characters required, this node uses exactly as many characters as needed. If width is greater than the number of characters required, this node adds a space on the left side of the output string for each additional character.

Default value: No value — Exactly as many characters as are needed to represent the number, with no extra padding.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### octal integer string

number represented as an octal string.

#### Examples

number

width

octal integer string

| number | width | octal integer string | Comments |
| --- | --- | --- | --- |
| 3 | 4 | 0003 | — |
| 42 | 3 | 052 | — |
| -4.2 | 3 | 37777777774 | -4.2 is rounded up to -4 in 64-bit integer format. width is too small to represent the octal version of a negative number, so the field width is extended. |

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=numeric-constant.html language=enus -->
## TOPIC 00045: Numeric Constant

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `numeric-constant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/numeric-constant.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a number on the diagram. Set this value by clicking inside the constant and typing a value.

Numeric Constant

Represents a number on the diagram.
 Set this value by clicking inside the constant and typing a value.

[IMAGE alt='1378' src='Literal.Numeric.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=numeric-interval.html language=enus -->
## TOPIC 00046: Interval

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `numeric-interval.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/numeric-interval.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Amount by which the increment and decrement buttons increase or decrease the value of the numeric control.

Interval

Amount by which the increment and decrement buttons increase or decrease the value of the numeric control.

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

Parent topic:

NumericTextBox

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=numerics.html language=enus -->
## TOPIC 00047: Numeric Controls

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `numerics.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/numerics.html
- document_id: `labview-nxg-web-module-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=one-button-dialog.html language=enus -->
## TOPIC 00048: One Button Dialog

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `one-button-dialog.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/one-button-dialog.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Displays a dialog box that contains a custom message and a single button. message The text to display in the dialog box. button name The text to display in the button that appears in the dialog box. Default value: OK true A Boolean value of TRUE when the user clicks the button. TRUE The user clicked

One Button Dialog

Displays a dialog box that contains a custom message and a single button.

[IMAGE alt='1378' src='OneButtonDialog.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### message

The text to display in the dialog box.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### button name

The text to display in the button that appears in the dialog box.

Default value: OK

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### true

A Boolean value of TRUE when the user clicks the button.

| TRUE | The user clicked the button. |
| --- | --- |
| FALSE | This output cannot return FALSE. |

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=one-over-e.html language=enus -->
## TOPIC 00049: 1/e

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `one-over-e.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/one-over-e.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the value 0.36787944117144233.

1/e

Represents the value 0.36787944117144233.

[IMAGE alt='1378' src='Literal.Numeric.1Overe.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=positive-infinity.html language=enus -->
## TOPIC 00050: Positive Infinity

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `positive-infinity.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/positive-infinity.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the value infinity.

Positive Infinity

Represents the value infinity.

[IMAGE alt='1378' src='Literal.Numeric.Positive_Infinity.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=post-buffer.html language=enus -->
## TOPIC 00051: POST Buffer

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `post-buffer.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/post-buffer.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends data within the buffer input to the URL you specify. This node uses the POST HTTP method. Unlike a PUT request, POST requests do not require all available property and attribute values when updating a resource. You can choose to send all values to update the entire resource or just a subset of

POST Buffer

Sends data within the buffer input to the URL you specify.

This node uses the POST HTTP method. Unlike a PUT request, POST requests do not require all available property and attribute values when updating a resource. You can choose to send all values to update the entire resource or just a subset of the available values.

[IMAGE alt='1378' src='POST_Buffer.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cpath.png']

##### output file

File to save body data returned by the server. If you do not specify an output file, the node does not save the body data to a file.

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

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### buffer

String of data to send to the server.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### timeout

Amount of time in milliseconds you must wait to obtain a response from the server before the web request times out. A value of -1 defers timeout monitoring to the operating system.

Default value: 10000 ms

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### status code

Status code information returned by the server.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### client handle out

Unique value that returns data back to the node. You can use the same client handle to wire together multiple HTTP nodes to preserve authentication credentials, HTTP headers, and cookies. Client handles are not required when making independent web requests without persistent data such as headers or credentials.

[IMAGE alt='datatype_icon' src='/assets/img/i1dstr.png']

##### headers

Header fields returned by the server. Refer to the World Wide Web Consortium website at [www.w3.org](http://digital.ni.com/express.nsf/bycode/exctg8) for more information about header field definitions including available headers, descriptions, and syntax.

[IMAGE alt='datatype_icon' src='/assets/img/i1dstr.png']

##### body

Body data that is returned by the server.

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

#### Default Content-Type for HTTP Request

If you do not specify a Content-Type header for an HTTP request, this node adds the 
 application/x-www-url-formencoded Content-Type header to the request by default.

Parent topic:

POST

Related reference:

- PUT
- PUT Buffer

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=radialnumeric-class.html language=enus -->
## TOPIC 00052: RadialNumeric

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `radialnumeric-class.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/radialnumeric-class.html
- document_id: `labview-nxg-web-module-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=radiusaxis-class.html language=enus -->
## TOPIC 00053: RadialAxis

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `radiusaxis-class.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/radiusaxis-class.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the properties of the RadialAxis class to read and write the elements of a radial axis of a polar plot.

RadialAxis

Use the properties of the RadialAxis class to read and write the elements of a radial
 axis of a polar plot.

RangeScale

Use the properties in the RangeScale class to read and write the elements of the uncolored scale.

FitType

Autoscale type.

Parent topic:

RangeScale

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=random-number-range.html language=enus -->
## TOPIC 00054: Random Number (Range)

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `random-number-range.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/random-number-range.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates a random value from a specified range.

Random Number (Range)

Generates a random value from a specified range.

Numeric Nodes

DBL

Generates a random value from a specified range.

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=read-call-chain.html language=enus -->
## TOPIC 00055: Read Call Chain

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `read-call-chain.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/read-call-chain.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the call chain from where the error or warning occurred. error in An error cluster that you use to check for errors or warnings. Standard Error Behavior call chain An array of names representing the chain of callers from the location that the error or warning occurred to the current VI. This

Read Call Chain

Returns the call chain from where the error or warning occurred.

[IMAGE alt='1378' src='Read_Call_Chain.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

An error cluster that you use to check for errors or warnings.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/i1dstr.png']

##### call chain

An array of names representing the chain of callers from the location that the error or warning occurred to the current VI.

This array is empty if there is no error, the call chain has been overwritten with a string that describes the location at which the error occurred, or there is no location information at all.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### has location?

A Boolean that indicates whether you replaced the call chain with a string that describes the location at which the error occurred.

| True | The error cluster has location information other than a call chain. Use Read Location to access the information. |
| --- | --- |
| False | The error cluster has no location information. |

Parent topic:

Error Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=read-error-code.html language=enus -->
## TOPIC 00056: Read Error Code

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `read-error-code.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/read-error-code.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the error code of an error cluster. error in An error cluster that you use to check for errors or warnings. Standard Error Behavior code The error or warning code of the error cluster. If there is no error, this is 0.

Read Error Code

Returns the error code of an error cluster.

[IMAGE alt='1378' src='Read_Error_Code.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

An error cluster that you use to check for errors or warnings.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### code

The error or warning code of the error cluster.

0

Parent topic:

Error Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=read-location.html language=enus -->
## TOPIC 00057: Read Location

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `read-location.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/read-location.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string that describes where the error or warning occurred. Use this node if the code that generated the error overrides the call chain because the location at which the error occurred cannot be described by a call chain. For example, if the error occurred across a network connection the lo

Read Location

Returns a string that describes where the error or warning occurred. Use this node if the code that generated the error overrides the call chain because the location at which the error occurred cannot be described by a call chain. For example, if the error occurred across a network connection the location might be network URL or a more specific string describing the location.

[IMAGE alt='1378' src='Read_Location.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

An error cluster that you use to check for errors or warnings.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### location

A string describing where the error or warning occurred.

This string is empty if the error cluster contains no location information. If the error cluster contains a call chain, this node returns the call chain formatted as a single, multiline string.

Parent topic:

Error Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=reciprocal.html language=enus -->
## TOPIC 00058: Reciprocal

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `reciprocal.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/reciprocal.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Divides 1 by the input value. x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, arrays of clusters of numbers, and waveforms. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this input has a default data type that use

Reciprocal

Divides 1 by the input value.

[IMAGE alt='1378' src='Reciprocal.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, arrays of clusters of numbers, and waveforms.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### 1 / x

The reciprocal of the input value.

##### Behavior with Various x Input Types

If x is 0, 1 / x is infinity. If x is an integer, 1 / x is a double-precision, floating-point number.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=refnum-class.html language=enus -->
## TOPIC 00059: Refnum

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `refnum-class.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/refnum-class.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the properties in the Refnum class to read and write the elements of a refnum.No properties are specific to this class.

Refnum

Use the properties in the Refnum class to read and write the elements of a refnum.No properties are specific to this class.

Control

Use the properties in the Control class to read and write the elements of a control.

Parent topic:

Control

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=reverse-string.html language=enus -->
## TOPIC 00060: Reverse String

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `reverse-string.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/reverse-string.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Produces a string whose characters are in reverse order of those in an input string. string The string you want to modify. This input can also be any data type that contains only strings, such as an array or cluster of strings. reversed The result of reversing the string. The data type of this outpu

Reverse String

Produces a string whose characters are in reverse order of those in an input string.

[IMAGE alt='1378' src='ReverseString.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### string

The string you want to modify.

This input can also be any data type that contains only strings, such as an array or cluster of strings.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### reversed

The result of reversing the string.

string

Parent topic:

String Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=rotate-string.html language=enus -->
## TOPIC 00061: Rotate String

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `rotate-string.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/rotate-string.html
- document_id: `labview-nxg-web-module-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=scale-delta-t.html language=enus -->
## TOPIC 00062: Scale Delta t

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `scale-delta-t.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/scale-delta-t.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Multiplies the delta t component of the waveform by the specified scale factor, which lengthens or shortens the sample rate of the waveform. waveform in Waveform to use to scale the delta t. This input accepts a waveform or a digital waveform. scale factor Number by which this node multiplies the de

Scale Delta t

Multiplies the delta 
*t* component of the waveform by the specified scale factor, which lengthens or shortens the sample rate of the waveform.

[IMAGE alt='1378' src='WDT_Scale_Delta_t_DBL.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cmsdt.png']

##### waveform in

Waveform to use to scale the delta 
t.

This input accepts a waveform or a digital waveform.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### scale factor

Number by which this node multiplies the delta 
t of the waveform. A value greater than zero but less than one shortens the sample rate. A value greater than one increases the sample rate.

Default value: 1000

[IMAGE alt='datatype_icon' src='/assets/img/imsdt.png']

##### waveform out

Resulting waveform with the new delta 
t value.

This output is a digital waveform when you wire a digital waveform to waveform in.

Parent topic:

Waveform Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=search-split-string.html language=enus -->
## TOPIC 00063: Search/Split String

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `search-split-string.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/search-split-string.html
- document_id: `labview-nxg-web-module-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=search-waveform.html language=enus -->
## TOPIC 00064: Search Waveform

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `search-waveform.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/search-waveform.html
- document_id: `labview-nxg-web-module-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=sinc.html language=enus -->
## TOPIC 00065: Sinc

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `sinc.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/sinc.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the sine of a specified value divided by that value (sin(x)/x) in radians. x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA,

Sinc

Computes the sine of a specified value divided by that value (sin(x)/x) in radians.

[IMAGE alt='1378' src='Sinc.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### sinc

Result of the operation.

This output assumes the same numeric representation as 
 x.

Parent topic:

Trigonometric Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=sort-1d-array.html language=enus -->
## TOPIC 00066: Sort 1D Array

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `sort-1d-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/sort-1d-array.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a sorted version of an array with the elements arranged in ascending order. If the specified array is an array of clusters, the node sorts the elements by comparing the first elements. If the first elements match, the node compares the second and subsequent elements. array A 1D array of any

Sort 1D Array

Returns a sorted version of an array with the elements arranged in ascending order.
 If the specified array is an array of clusters, the node sorts the elements by comparing the first elements. If the first elements match, the node compares the second and subsequent elements.

[IMAGE alt='1378' src='Sort1DArray.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### array

A 1D array of any type.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### sorted array

array sorted in ascending order.

#### Sorting String Arrays

Sort 1D Array sorts string arrays based on case-sensitivity. For example, if array is {b, C, A}, Sort 1D Array returns {A, C, b} for sorted array.

Parent topic:

Array Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=string-nodes.html language=enus -->
## TOPIC 00067: String Nodes

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `string-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/string-nodes.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`

String Nodes

Append True Or False String

Appends one of two possible strings, determined by a Boolean value, to another string you specify.

Concatenate Strings

Concatenates input strings and/or 1D arrays of strings into a single output string.

Format Value

Converts a number into a regular string and appends the result to the input string.

Match Pattern

Searches for a pattern of characters in a string as specified by a limited set of regular expressions.

Pick Line

Copies a specified line from one string and appends that line to another string.

Replace Substring

Deletes a specified length of characters in a string and replaces the deleted portion with another string.

Reverse String

Produces a string whose characters are in reverse order of those in an input string.

Rotate String

Moves the first character of a string to the end of the string.

Scan Value

Converts the characters at the beginning of a string to a numeric value, using format specifiers to determine the representation and precision of the resulting number.

Search and Replace Pattern

Searches for a pattern in the input string and replaces either the first match or every match with a substring you specify.

Search/Split String

Divides a single string into two substrings.

String Length

Returns the number of characters in a string.

String Subset

Returns a portion, or substring, of a string.

To Lowercase

Converts all alphabetic characters in a string to lowercase characters.

To Uppercase

Converts all alphabetic characters in a string to uppercase characters.

Trim Whitespace

Removes all ASCII whitespace, such as spaces, tabs, carriage returns, and linefeeds, from the beginning, end, or both ends of the input string.

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=stringcontrol-class.html language=enus -->
## TOPIC 00068: StringControl

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `stringcontrol-class.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/stringcontrol-class.html
- document_id: `labview-nxg-web-module-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=tank-class.html language=enus -->
## TOPIC 00069: Tank

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `tank-class.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/tank-class.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the properties in the Tank class to read and write the elements of a tank.No properties are specific to this class.

Tank

Use the
 properties in the Tank class to read and write the elements of a tank.No properties are specific to this class.

LinearNumeric

Use the properties in the LinearNumeric class to read and write the elements of a linear numeric.

Parent topic:

LinearNumeric

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=target-shape.html language=enus -->
## TOPIC 00070: TargetShape

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `target-shape.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/target-shape.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Shape of the cursor target that displays over a plot. Target Shapes Cross Diamond Ellipse Rectangle Plus

TargetShape

Shape of the cursor target that displays over a plot.

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

#### Target Shapes

- Cross
- Diamond
- Ellipse
- Rectangle
- Plus

Parent topic:

Cursor

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=tick-count-us.html language=enus -->
## TOPIC 00071: Microseconds

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `tick-count-us.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/tick-count-us.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value of the microsecond timer. microsecond timer value Value of the operating system's microsecond timer. Timer Count Time vs. Real-World Time The base reference time (microsecond zero) for this node is undefined, so you cannot convert the output value to a real-world time or date. Micr

Microseconds

Returns the value of the microsecond timer.

[IMAGE alt='1378' src='TickCount.Microseconds.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### microsecond timer value

Value of the operating system's microsecond timer.

#### Timer Count Time vs. Real-World Time

The base reference time (microsecond zero) for this node is undefined, so you cannot convert the output value to a real-world time or date.

#### Microsecond Timer Wrap Behavior

Be careful when you use this node in comparisons because the value of the microsecond timer wraps from 
 (2^32)-1 to 
 0. You can also change the value at which the microsecond timer wraps by changing the size of the output integer.

Parent topic:

Timer Count

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=to-double-precision-float.html language=enus -->
## TOPIC 00072: To Double Precision Float

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `to-double-precision-float.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/to-double-precision-float.html
- document_id: `labview-nxg-web-module-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=to-signed-32-bit-integer.html language=enus -->
## TOPIC 00073: To Signed 32-bit Integer

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `to-signed-32-bit-integer.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/to-signed-32-bit-integer.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a number to a 32-bit integer in the range -(2^31) to (2^31)-1. number An input to this operation. This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA W

To Signed 32-bit Integer

Converts a number to a 32-bit integer in the range -(2<sup>31</sup>) to (2<sup>31</sup>)-1.

[IMAGE alt='1378' src='ToSigned32BitInteger.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### number

An input to this operation.

This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### 32-bit integer

Result of the conversion.

This output assumes the same data type structure as 
 number.

#### Examples

| number | 32-bit integer (range: -(231) to (231)-1) | Comments |
| --- | --- | --- |
| 0 | 0 | number is within the allowable range, so no value change occurs. |
| 1 | 1 | Same as above. |
| ... | ... | ... |
| (231)-2 | (231)-2 | Same as above. |
| (231)-1 | (231)-1 | number is the maximum allowable value, so no value change occurs. |
| 231 | -(231) | number exceeds the maximum allowable value by 1, so the node returns the first allowable value at the bottom of the range. |
| (231)+1 | -(231)+1 | number exceeds the maximum allowable value by 2, so the node returns the second allowable value at the bottom of the range. |
| -(231)+1 | -(231)+1 | number is within the allowable range, so no value change occurs. |
| -(231) | -(231) | number is the minimum allowable value, so no value change occurs. |
| -(231)-1 | (231)-1 | number undershoots the minimum allowable value by 1, so the node returns the first allowable value at the top of the range. |
| -(231)-1 | (231)-2 | number undershoots the minimum allowable value by 2, so the node returns the second allowable value at the top of the range. |
| 13.7 | 14 | The node rounds 13.7 up to 14 because 14 is the nearest integer. |
| 13.5 | 14 | The node rounds 13.5 up to 14 because 14 is the nearest even integer. |
| 14.5 | 14 | The node rounds 14.5 down to 14 because 14 is the nearest even integer. |

#### Rounding Behavior for Floating-Point Values

This node rounds all floating-point numeric values to the nearest integer. If the fractional part of the floating-point value is 
 .5, the node rounds the value to the nearest even integer. For example, the node rounds 
 13.5 to 
 14 and rounds 
 14.5 to 
 14.

#### Wrapping Behavior for Out-of-Range Values

If this node receives an input value that falls outside of the range of values that the output can represent, the node returns a value that wraps to the other end of the range. This differs from the behavior for nodes that convert values to unsigned integers.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=to-signed-8-bit-integer.html language=enus -->
## TOPIC 00074: To Signed 8-bit Integer

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `to-signed-8-bit-integer.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/to-signed-8-bit-integer.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a number to an 8-bit integer in the range -128 to 127. number An input to this operation. This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA When you

To Signed 8-bit Integer

Converts a number to an 8-bit integer in the range -128 to 127.

[IMAGE alt='1378' src='ToSigned8BitInteger.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### number

An input to this operation.

This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/ii8.png']

##### 8-bit integer

Result of the conversion.

This output assumes the same data type structure as 
 number.

#### Examples

| number | 8-bit integer (range: -128 to 127) | Comments |
| --- | --- | --- |
| 0 | 0 | number is within the allowable range, so no value change occurs. |
| 1 | 1 | Same as above. |
| ... | ... | ... |
| 126 | 126 | Same as above. |
| 127 | 127 | number is the maximum allowable value, so no value change occurs. |
| 128 | -128 | number exceeds the maximum allowable value by 1, so the node returns the first allowable value at the bottom of the range. |
| 129 | -127 | number exceeds the maximum allowable value by 2, so the node returns the second allowable value at the bottom of the range. |
| -127 | -127 | number is within the allowable range, so no value change occurs. |
| -128 | -128 | number is the minimum allowable value, so no value change occurs. |
| -129 | 127 | number undershoots the minimum allowable value by 1, so the node returns the first allowable value at the top of the range. |
| -130 | 126 | number undershoots the minimum allowable value by 2, so the node returns the second allowable value at the top of the range. |
| 13.7 | 14 | The node rounds 13.7 up to 14 because 14 is the nearest integer. |
| 13.5 | 14 | The node rounds 13.5 up to 14 because 14 is the nearest even integer. |
| 14.5 | 14 | The node rounds 14.5 down to 14 because 14 is the nearest even integer. |

#### Rounding Behavior for Floating-Point Values

This node rounds all floating-point numeric values to the nearest integer. If the fractional part of the floating-point value is 
 .5, the node rounds the value to the nearest even integer. For example, the node rounds 
 13.5 to 
 14 and rounds 
 14.5 to 
 14.

#### Wrapping Behavior for Out-of-Range Values

If this node receives an input value that falls outside of the range of values that the output can represent, the node returns a value that wraps to the other end of the range. This differs from the behavior for nodes that convert values to unsigned integers.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=to-single-precision-float.html language=enus -->
## TOPIC 00075: To Single Precision Float

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `to-single-precision-float.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/to-single-precision-float.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a number to a single-precision, floating-point number. number An input to this operation. This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA When you

To Single Precision Float

Converts a number to a single-precision, floating-point number.

[IMAGE alt='1378' src='ToSinglePrecisionFloat.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### number

An input to this operation.

This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/isgl.png']

##### single precision float

Result of the conversion.

This output assumes the same data type structure as 
 number.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=to-variant.html language=enus -->
## TOPIC 00076: To Variant

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `to-variant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/to-variant.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts any data to variant data. anything The data you want to convert. You can wire any data type to this input. This input accepts arrays and clusters of Booleans, floating-point numbers, and strings. This input can also accept an array of clusters, or a cluster of arrays, of those data types. H

To Variant

Converts any data to variant data.

[IMAGE alt='1378' src='ToVariant.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cvoid.png']

##### anything

The data you want to convert. You can wire any data type to this input.

This input accepts arrays and clusters of Booleans, floating-point numbers, and strings. This input can also accept an array of clusters, or a cluster of arrays, of those data types. However, anything does not support refnums.

[IMAGE alt='datatype_icon' src='/assets/img/ifxdt.png']

##### variant

The converted variant data.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=two-button-dialog.html language=enus -->
## TOPIC 00077: Two Button Dialog

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `two-button-dialog.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/two-button-dialog.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Displays a dialog box that contains a custom message and two buttons. message The text to display in the dialog box. true button name The text displayed on the left button in the dialog box. Default value: OK false button name The text displayed on the right button in the dialog box. Default value:

Two Button Dialog

Displays a dialog box that contains a custom message and two buttons.

[IMAGE alt='1378' src='TwoButtonDialog.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### message

The text to display in the dialog box.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### true button name

The text displayed on the left button in the dialog box.

Default value: OK

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### false button name

The text displayed on the right button in the dialog box.

Default value: Cancel

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### true button?

A Boolean value that indicates whether the user clicked the dialog box button designated by true button name.

| True | The user clicked the dialog box button designated by true button name. |
| --- | --- |
| False | The user clicked the dialog box button designated by false button name. |

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=unflatten-from-json.html language=enus -->
## TOPIC 00078: Unflatten from JSON

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `unflatten-from-json.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/unflatten-from-json.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a UTF-8 JavaScript Object Notation (JSON) string to another data type. enable LabVIEW extensions A Boolean that determines whether JSON extensions support NaN and Inf values of floating-point numbers. Not all JSON parsers support these extensions. True Enable JSON extension support of NaN a

Unflatten from JSON

Converts a UTF-8 JavaScript Object Notation (JSON) string to another data type.

[IMAGE alt='1378' src='UnflattenFromJson.png']

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

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### path

A specific item in the JSON string. Use path if your JSON string contains multiple items and you would like to extract a specific item from it. path uses an array of strings to identify the item, where each element in the array references either the name of a cluster element or an integer index of an array. If you specify an item using path, you must wire a data type to type and defaults that corresponds to the data type of the specified item.

##### Type/Default Inputs and Corresponding Outputs

Consider the JSON string 
 {"0":"abc","1":false,"2":[9,8,7]}. The following table illustrates an example of type/defaults inputs required for various paths and the resulting value outputs.

| Path | Type and Defaults | Value | Comments |
| --- | --- | --- | --- |
|  |  |  | If path is empty, type and defaults must account for each element in the JSON string. You must wire a cluster containing a string, a Boolean, and an array to type and defaults. |
|  |  |  | In this example, the path points to the cluster element named 0, or string abc. You must wire a string to type and defaults. |
|  |  |  | In this example, the path points to the cluster element named 2, which is an array, and the element at index 0 of that array. This element is a floating-point number, so you must wire a DBL numeric to type and defaults. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### JSON string

The flattened UTF-8 string that you want to unflatten.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### type and defaults

The data type and default values to which you want to unflatten the JSON string. This input accepts Booleans, integers, floating-point numbers, strings, and arrays or clusters of these types. Cluster elements may be labeled or unlabeled, but not a combination of both. If elements in a cluster are labeled, then each name must be unique to that cluster.

JSON string

type and defaults

{"firstelement":"a","secondelement":"b"}

firstelement

secondelement

path

JSON string

type and defaults

path

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### default null elements?

A Boolean that determines how null values in JSON string are processed.

| True | Uses default values from the input cluster for null values in JSON string. |
| --- | --- |
| False | Returns an error for null values. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### strict validation?

A Boolean that determines whether to return an error when JSON string contains items not defined in type and defaults.

| True | Returns an error when JSON string contains items not defined in type and defaults. |
| --- | --- |
| False | The JSON object may contain items not defined in type and defaults. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### value

Unflattened data of the same data type and structure as type and defaults.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Converting Data Types not Supported by Type and Defaults

Unflatten From JSON

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=unset-busy.html language=enus -->
## TOPIC 00079: Unset Busy

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `unset-busy.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/unset-busy.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Changes the cursor from the busy cursor to the default cursor and enables mouse clicks on both the panel and the menu. In a WebVI, this node removes the loading spinner on the panel, instead of updating the cursor. panel reference in Reference to the panel. If you leave this input unwired, the node

Unset Busy

Changes the cursor from the busy cursor to the default cursor and enables mouse
 clicks on both the panel and the menu.

In a WebVI, this node removes the loading spinner on the panel, instead of updating the
 cursor.

[IMAGE alt='1378' src='UnsetBusy.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### panel reference in

Reference to the panel.

If you leave this input unwired, the node changes the cursor on the panel of the current
 VI.

Note

panel reference
 in

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### panel reference out

Reference to the panel.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Busy State Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=upgrade-to-error.html language=enus -->
## TOPIC 00080: Upgrade To Error

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `upgrade-to-error.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/upgrade-to-error.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Changes a warning to an error. error in An error cluster that you use to check for errors or warnings. Standard Error Behavior error out An error cluster including any values this node writes, removes, or replaces. If no values change, this node returns error in unchanged. Standard Error Behavior

Upgrade To Error

Changes a warning to an error.

[IMAGE alt='1378' src='Upgrade_To_Error.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

An error cluster that you use to check for errors or warnings.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

An error cluster including any values this node writes, removes, or replaces. If no values change, this node returns 
error in unchanged.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Error Nodes

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=urlimage-class.html language=enus -->
## TOPIC 00081: UrlImage

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `urlimage-class.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/urlimage-class.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the properties in the UrlImage class to read and write the elements of the URL image control.This class is supported in VIs that run in a web application only.

UrlImage

Use the properties in the UrlImage class to read and write the elements of the URL image control.This class is supported in VIs that run in a web application only.

Control

Use the properties in the Control class to read and write the elements of a control.

HyperlinkUrl

URL to open when the user clicks the image.

Parent topic:

Control

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=variant-class.html language=enus -->
## TOPIC 00082: Variant

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `variant-class.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/variant-class.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the properties in the Variant class to read and write the elements of a variant.No properties are specific to this class.

Variant

Use the properties in the Variant class to read and write the elements of a variant.No properties are specific to this class.

Control

Use the properties in the Control class to read and write the elements of a control.

Parent topic:

Control

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=variant-constant.html language=enus -->
## TOPIC 00083: Variant Constant

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `variant-constant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/variant-constant.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an empty variant on the diagram. You cannot set a value for a variant constant.

Variant Constant

Represents an empty variant on the diagram.

You cannot set a value for a variant constant.

[IMAGE alt='1378' src='Literal.Variant.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-web-module-api-ref path=variant-to-data.html language=enus -->
## TOPIC 00084: Variant To Data

- bundle_id: `labview-nxg-web-module-api-ref`
- source_path: `variant-to-data.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-web-module-api-ref/raw/resource/enus/variant-to-data.html
- document_id: `labview-nxg-web-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts variant data to the data type that you specify so that you can display or process the data. type The data type of the data stored in variant. You can wire any data type to this input. If the data type wired to type does not match the data stored in variant, the node returns an error. If the

Variant To Data

Converts variant data to the data type that you specify so that you can display or process the data.

[IMAGE alt='1378' src='VariantToData.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cvoid.png']

##### type

The data type of the data stored in variant. You can wire any data type to this input.

type

variant

[IMAGE alt='datatype_icon' src='/assets/img/cfxdt.png']

##### variant

The variant data you want to convert to the data type that you specify in type.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ivoid.png']

##### data

The variant data changed to the data type specified by type. If variant could not be converted to the data type specified, this returns the default value for the data type.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Conversion Nodes
