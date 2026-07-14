# NI DOCUMENT BUNDLE: daqexpress-api-ref

<!--NI_BUNDLE_CHUNK bundle=daqexpress-api-ref start=1 end=88 -->
<!--NI_TOPIC bundle=daqexpress-api-ref path=1d-array-constant.html language=enus -->
## TOPIC 00001: Array Constant

- bundle_id: `daqexpress-api-ref`
- source_path: `1d-array-constant.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/1d-array-constant.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an array on the diagram. The data type of the array constant is defined by the element inside the array. If the array constant is empty, you must drag a constant of any type into the array to define the data type of the array. All elements of the array are of this type. To change the dime

Array Constant

Represents an array on the diagram.

The data type of the array constant is defined by the element inside the array. If the array constant is empty, you must drag a constant of any type into the array to define the data type of the array. All elements of the array are of this type.

To change the dimensionality of the array, select the array and adjust the value of 
 Dimensions in the 
 **Item** tab.

[IMAGE alt='1378' src='Literal.Array.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=daqexpress-api-ref path=absolute-value.html language=enus -->
## TOPIC 00002: Absolute Value

- bundle_id: `daqexpress-api-ref`
- source_path: `absolute-value.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/absolute-value.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute value of the input. x An input to this operation. This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, arrays of clusters of numbers, and waveforms. x cannot be an unsigned integer because unsigned int

Absolute Value

Returns the absolute value of the input.

[IMAGE alt='1378' src='AbsoluteValue.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, arrays of clusters of numbers, and waveforms. 
 x cannot be an unsigned integer because unsigned integers represent only non-negative integers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### absolute value

The absolute value of the input.

x

x

i

x

abs

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=add-array-elements.html language=enus -->
## TOPIC 00003: Add Array Elements

- bundle_id: `daqexpress-api-ref`
- source_path: `add-array-elements.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/add-array-elements.html
- document_id: `daqexpress-api-ref`
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

<!--NI_TOPIC bundle=daqexpress-api-ref path=amplitude-measurements-ac-dc-and-rms-basic-continuous.html language=enus -->
## TOPIC 00004: Basic Continuous

- bundle_id: `daqexpress-api-ref`
- source_path: `amplitude-measurements-ac-dc-and-rms-basic-continuous.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/amplitude-measurements-ac-dc-and-rms-basic-continuous.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates continuous AC, DC, and RMS values of a signal. This node gives simpler control over the individual AC, DC, and RMS calculations than the AC DC and RMS (Continuous) node. reset A Boolean that specifies the initialization of the internal state of the node. True Initializes the internal stat

Basic Continuous

Calculates continuous AC, DC, and RMS values of a signal. This node gives simpler control over the individual AC, DC, and RMS calculations than the AC DC and RMS (Continuous) node.

[IMAGE alt='1378' src='AC_DC_and_RMS_(basic_continuous)(Wfm).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset

A Boolean that specifies the initialization of the internal state of the node.

| True | Initializes the internal state to zero. |
| --- | --- |
| False | Initializes the internal state to the final state from the previous call of this node. |

This node automatically initializes the internal state to zero on the first call and runs continuously until this input is True.

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cmsdt.png']

##### signal

The input signal.

This input can be a waveform or an array of waveforms.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### averaging type

Type of averaging to apply to the signal.

| Linear | Applies linear averaging to the signal. |
| --- | --- |
| Exponential | Applies exponential averaging to the signal. |

Default value: Linear

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### window type

Type of window to apply to the signal when you use linear averaging.

Windowing can help increase measurement accuracy for signals that are dominated by periodic components.

| Rectangular (none) | Does not apply a window. |
| --- | --- |
| Hanning | Applies a Hanning window. |
| Low side lobe | Applies a low side lobe window. |

Default value: Rectangular (none)

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### AC value

AC value of the signal.

This output can return a double-precision, floating-point number or a 1D array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### DC value

DC value of the signal.

This output can return a double-precision, floating-point number or a 1D array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### RMS value

Root mean square value of the signal.

This output can return a double-precision, floating-point number or a 1D array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Amplitude Measurements

<!--NI_TOPIC bundle=daqexpress-api-ref path=amplitude-measurements-ac-dc-and-rms-single-shot.html language=enus -->
## TOPIC 00005: Single-shot

- bundle_id: `daqexpress-api-ref`
- source_path: `amplitude-measurements-ac-dc-and-rms-single-shot.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/amplitude-measurements-ac-dc-and-rms-single-shot.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates single-shot AC, DC, and RMS values of a signal. reset A Boolean that specifies whether to reset the internal state of the node. True Resets the internal state of the node. False Does not reset the internal state of the node. This input is available only if you wire a double-precision, flo

Single-shot

Calculates single-shot AC, DC, and RMS values of a signal.

[IMAGE alt='1378' src='AC_DC_and_RMS_(single-shot)(Wfm).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset

A Boolean that specifies whether to reset the internal state of the node.

| True | Resets the internal state of the node. |
| --- | --- |
| False | Does not reset the internal state of the node. |

This input is available only if you wire a double-precision, floating-point number to signal.

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cmsdt.png']

##### signal

Input signal.

This input accepts the following data types:

- Waveform
- 1D array of waveforms
- Double-precision, floating-point number
- 1D array of double-precision, floating-point numbers

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sample length

Length of each set of data.

The node performs computation for each set of data. sample length must be greater than zero.

This input is available only if you wire a double-precision, floating-point number to signal.

Default value: 100

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### AC value

AC value of the signal.

This output can return a double-precision, floating-point number or a 1D array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### DC value

DC value of the signal.

This output can return a double-precision, floating-point number or a 1D array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### RMS value

Root mean square value of the signal.

This output can return a double-precision, floating-point number or a 1D array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Amplitude Measurements

<!--NI_TOPIC bundle=daqexpress-api-ref path=amplitude-measurements-multimode-function.html language=enus -->
## TOPIC 00006: Amplitude Measurements

- bundle_id: `daqexpress-api-ref`
- source_path: `amplitude-measurements-multimode-function.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/amplitude-measurements-multimode-function.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns signal characteristics such as peak amplitude, pulse level, and cycle average.

Amplitude Measurements

Returns signal characteristics such as peak amplitude, pulse level, and cycle
 average.

Signal Processing Nodes

Peak Amplitude

Returns data signal maximum, minimum, and peak-to-peak values.

Parent topic:

Signal Processing Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=analog-waveform-nodes.html language=enus -->
## TOPIC 00007: Analog Waveform Nodes

- bundle_id: `daqexpress-api-ref`
- source_path: `analog-waveform-nodes.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/analog-waveform-nodes.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`

Analog Waveform Nodes

Build Waveform

Creates a waveform by accepting an array input of various types.

Get Waveform Attribute

Retrieves either the value of a single waveform attribute or the names and values of all waveform attributes.

Set Waveform Attribute

Adds or replaces a waveform attribute.

Waveform Properties

Writes or reads the elements of a waveform.

<!--NI_TOPIC bundle=daqexpress-api-ref path=array-nodes.html language=enus -->
## TOPIC 00008: Array Nodes

- bundle_id: `daqexpress-api-ref`
- source_path: `array-nodes.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/array-nodes.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`

Array Nodes

Array Max and Min

Returns the maximum and minimum values found in an array, along with the indexes for each value.

Array Size

Returns the number of elements in each dimension of an array.

Array Subset

Returns a portion of an array starting at a specified index and containing a specified number of elements.

Build Array

n

Decimate 1D Array

Divides the elements of an array into multiple output arrays, placing elements into the outputs successively.

Delete from Array

Deletes a specified element or subarray of an array.

Index Array

Returns the value stored in an array at a specified index.

Initialize Array

n

Insert into Array

Inserts an element or subarray into an array at the index you specify.

Interleave 1D Arrays

Interleaves corresponding elements from the input arrays into a single output array.

Interpolate 1D Array

Calculates a decimal y-value from an array of numbers or points at a specified fractional index or x-value using linear interpolation.

Replace Array Subset

Replaces an element or subarray in an array at the index you specify.

Reshape Array

Changes the dimensions of an array according to a specified dimension size.

Reverse 1D Array

Reverses the order of the elements in an array.

Rotate 1D Array

Rotates the elements of an array a specified number of places and direction.

Search 1D Array

Searches for an element in a 1D array starting at a specified index.

Sort 1D Array

Returns a sorted version of an array with the elements arranged in ascending order.

Split 1D Array

Divides an array at a specified index and returns the two portions.

Threshold 1D Array

Interpolates points in a 1D array that represents a 2D non-descending graph.

Transpose 2D Array

Rearranges the elements of a 2D array such that the array [i,j] becomes a transposed array [j,i].

<!--NI_TOPIC bundle=daqexpress-api-ref path=array-of-strings-to-path.html language=enus -->
## TOPIC 00009: Array of Strings to Path

- bundle_id: `daqexpress-api-ref`
- source_path: `array-of-strings-to-path.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/array-of-strings-to-path.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts an array of strings into a relative or absolute path. If you have an empty string in the array, the directory location before the empty string is deleted in the path output. This behavior is the same as using ..\ in a command line path to move up a level in directory hierarchy. relative Whe

Array of Strings to Path

Converts an array of strings into a relative or absolute path.

If you have an empty string in the array, the directory location before the empty string is deleted in the path output. This behavior is the same as using 
 ..\ in a command line path to move up a level in directory hierarchy.

[IMAGE alt='1378' src='ArrayOfStringsToPath.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### relative

Whether you want to create a relative path or an absolute path.

path

<Not A Path>

[IMAGE alt='datatype_icon' src='/assets/img/c1dstr.png']

##### array of strings

The names of the components of the path you want to build.

The first element is the highest level of the path hierarchy (the volume name, for file systems that support multiple volumes), and the last element is the last element of the hierarchy. An element that contains an empty string tells the software to go up a level in the hierarchy.

[IMAGE alt='datatype_icon' src='/assets/img/ipath.png']

##### path

The resulting path.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=array-size.html language=enus -->
## TOPIC 00010: Array Size

- bundle_id: `daqexpress-api-ref`
- source_path: `array-size.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/array-size.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of elements in each dimension of an array. array An n-dimensional array of any type. This input also accepts clusters containing a single array, such as waveforms. This input changes to waveform when the data type is a waveform. Data Type Changes on FPGA When you add this node to

Array Size

Returns the number of elements in each dimension of an array.

[IMAGE alt='1378' src='ArraySize.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### array

An 
n-dimensional array of any type.

This input also accepts clusters containing a single array, such as waveforms. This input changes to waveform when the data type is a waveform.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### waveform

The waveform whose array of y values you want to use in this operation. This input becomes available when you wire a waveform to array.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### size(s)

The number of elements in the array.

This output returns different data types, depending on the dimension of the array:

- One-dimension—This output returns a 32-bit integer.
- Multidimensional—This output returns a 1D array in which each element is a 32-bit integer that represents the number of elements in the corresponding dimension of array .

##### Representation of Array Dimensions in the Output Array

For multidimensional arrays, the order of elements in the output array corresponds to row-major order. Thus, the first dimension in the input array always corresponds to the last element in the output array. The following table shows how output array elements correspond to input array dimensions for a 4D array.

| Element in Output Array | Corresponding Input Array Dimension | Index Name |
| --- | --- | --- |
| 1 | 4th | Volume |
| 2 | 3rd | Page |
| 3 | 2nd | Row |
| 4 | 1st | Column |

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### size

The number of elements in the waveform's array of y values. This output becomes available when the input data type is a waveform.

#### Examples

| Diagram | Panel Indicator | Comments |
| --- | --- | --- |
|  |  | size(s) for 1D Array returns a scalar element with the size of the input array. |
|  |  | size(s) for 2D Array returns a 1D array where each element corresponds to the size of a dimension in the input array. The first element returns the number of rows in the input array, and the second element returns the number of columns in the input array. |

Parent topic:

Array Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=chart-control.html language=enus -->
## TOPIC 00011: Chart Control

- bundle_id: `daqexpress-api-ref`
- source_path: `chart-control.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/chart-control.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Chart numeric data by displaying a history of values. How is Charting Different Than Plotting? Graphs and charts differ in the way they display and update data. VIs with a graph usually collect the data in an array and then plot the data to the graph. This process is similar to a spreadsheet that fi

Chart Control

Chart numeric data by displaying a history of values.

[IMAGE alt='1378' src='GUID-998D1272-BA2D-4196-9653-B8E6CDFC9EF7-a5.png']

#### How is Charting Different Than Plotting?

Graphs and charts differ in the way they display and update data. VIs with a graph usually collect the data in an array and then plot the data to the graph. This process is similar to a spreadsheet that first stores the data then generates a plot of it. When the data is plotted, the graph discards the previously plotted data and displays only the new data.

In contrast, a chart appends new data points to those points already in the display to create a history or a buffer. On a chart, you can see the current reading or measurement in context with data previously acquired. When more data points are added than can be displayed on the chart, the chart scrolls so that new points are added to the right side of the chart while old points disappear to the left.

#### What Types of Data Can I Chart?

You can chart numeric data contained in arrays and analog waveforms. By default, the chart data type is an array of doubles. You can change the data type on the diagram.

The waveform data type carries the start time (t0), delta t (dt), and y-values (Y) of a waveform. When you wire waveform data to a chart, the chart automatically plots a waveform based on the start time, delta t, and y-values of the waveform. A waveform that specifies 
 t0 and a single-element 
 Y array is useful for plotting data that is not evenly sampled because each data point has its own time stamp.

For data contained in arrays, the chart displays a general-purpose Cartesian graph that charts any set of points, evenly sampled or not.

The following table describes how different types of array data are charted.

| Data Type | Plot Behavior |
| --- | --- |
| Scalar numeric value | The chart displays a single plot using the scaler numeric value as the most recent value and previous values up to the history length. |
| 1D array of numeric values | The array is a single plot. X-value: Array index Y-value: Array element |
| Cluster of numeric values | Each element of the cluster is a single plot which uses the numeric value as the most recent value and previous values up to the history length. |
| 1D array of clusters of numeric values | Each element of the cluster is a single plot which uses the numeric value as the most recent value and previous values up to the history length. The array represents an aggregated set of samples. |
| 1D array of waveforms | Each waveform is a separate plot. This data type is not supported. |
| 2D array of numeric values | Each column of the array is a separate plot. |

#### How Do I Define the Chart History Length?

On the 
 Item tab, in the 
 Behavior section, specify 
 History length to configure the size of the buffer. For waveforms, the history length is the number of individual waveforms the buffer can hold. The waveforms can be of various sample sizes. For numeric data, the history length is the number of samples the buffer can hold.

Parent topic:

Charts and Graphs

<!--NI_TOPIC bundle=daqexpress-api-ref path=charts-and-graphs.html language=enus -->
## TOPIC 00012: Charts and Graphs

- bundle_id: `daqexpress-api-ref`
- source_path: `charts-and-graphs.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/charts-and-graphs.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Chart and plot data. What Is the Difference between Graphs and Charts? You can collect data, usually in an array, and then plot the data to a graph. This process is similar to a spreadsheet that first stores the data and then generates a plot of it. A chart appends new data points to those points al

Charts and Graphs

Chart and plot data.

[IMAGE alt='1378' src='GUID-8410F478-BE1A-457B-A198-A4EA7CB22028-a5.png']

#### What Is the Difference between Graphs
 and Charts?

You can collect data, usually in an array, and then plot the data to a graph. This
 process is similar to a spreadsheet that first stores the data and then generates a plot
 of it.

A chart appends new data points to those points already in the display to create a
 history. On a chart, you can see the current reading or measurement in context with data
 previously acquired.

#### Deciding Which Graph or Chart to Use

Knowing what type of data you need to display determines the type of graph or chart you should use.

| Control | Accepted Data Types | Display Examples | When to Use |
| --- | --- | --- | --- |
| Graph | Numeric, complex, X/Y, or point sample data contained in arrays and analog waveforms | Analog waveform data acquired at a constant rate | Use a graph for fast processes that acquire data continuously. |
| Chart | Numeric data contained in arrays and analog waveforms | Analog waveform data acquired at a constant rate with a history, or buffer, of the data from previous updates | Use a chart for processes that require a cumulative history of incremental updates to be maintained. |
| Intensity Graph | 3D data on a 2D plot by using color to display the values of the third dimension | Patterned data, such as frequency of sound intensity | Use an intensity graph for 3D data. |

#### Autoscaling

You can enable autoscaling for graphs and charts, which means they adjust their horizontal or vertical scales to fit the data you wire to them. Graphs and charts support the following types of autoscaling:

- Fit exactly —Fits the end markers to the exact minimum and maximum values of the data.
- Fit loosely —Rounds the end markers to a multiple of the increment used for the scale.
- Grow only —Fits the end markers to the minimum and maximum values of the data at run time. This type of autoscaling is available only for the vertical axis of graph, chart, and intensity graph.

Related information:

- Capturing Data
- Clearing Indicator Display Data in a Chart, Graph or Array

<!--NI_TOPIC bundle=daqexpress-api-ref path=comparison-nodes.html language=enus -->
## TOPIC 00013: Comparison Nodes

- bundle_id: `daqexpress-api-ref`
- source_path: `comparison-nodes.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/comparison-nodes.html
- document_id: `daqexpress-api-ref`
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

Printable?

Returns True if a value represents a printable ASCII character. Otherwise, this node returns False.

White Space?

Returns True if a value represents a white space character, such as Space, Tab, Newline, Carriage Return, Form Feed, or Vertical Tab. Otherwise, this node returns False.

<!--NI_TOPIC bundle=daqexpress-api-ref path=cosine.html language=enus -->
## TOPIC 00014: Cosine

- bundle_id: `daqexpress-api-ref`
- source_path: `cosine.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/cosine.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the cosine of a specified value (x) in radians. x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this input has a default da

Cosine

Computes the cosine of a specified value (x) in radians.

[IMAGE alt='1378' src='Cosine.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### cos

Result of the operation.

x

x

x

i

x

cos

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

Parent topic:

Trigonometric Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=cotangent.html language=enus -->
## TOPIC 00015: Cotangent

- bundle_id: `daqexpress-api-ref`
- source_path: `cotangent.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/cotangent.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the cotangent of a specified value (x) in radians. x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this input has a default

Cotangent

Computes the cotangent of a specified value (x) in radians.

[IMAGE alt='1378' src='Cotangent.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### cot

Result of the operation.

This output assumes the same numeric representation as 
 x.

Parent topic:

Trigonometric Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=create-file-with-incrementing-suffix.html language=enus -->
## TOPIC 00016: Create File with Incrementing Suffix

- bundle_id: `daqexpress-api-ref`
- source_path: `create-file-with-incrementing-suffix.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/create-file-with-incrementing-suffix.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a file and appends an incrementing number suffix to the filename if the file already exists at a specified path. If the file does not exist, this node creates the file without appending an incrementing number suffix to the filename. format string A string that uses format specifiers to deter

Create File with Incrementing Suffix

Creates a file and appends an incrementing number suffix to the filename if the file already exists at a specified path.
 If the file does not exist, this node creates the file without appending an incrementing number suffix to the filename.

[IMAGE alt='1378' src='Create_File_with_Incrementing_Suffix.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### format string

A string that uses format specifiers to determine how to convert the data into what you specify.

Default value:   %d

##### Syntax Elements for Creating a Format Specifier

Use the following syntax elements to create a format specifier for the input string.

| Syntax Element | Description |
| --- | --- |
| % | Syntax element that begins the format specifier. |
| $ (optional) | Modifier that specifies the order in which to display variables when used within a formatting node. Include the digit that represents the order of the variable immediately before this modifier. |
| - (optional) | Modifier that justifies the parameter to the left, within its width, when used within a formatting node. |
| + (optional) | Modifier that includes mathematical symbols when used within a formatting node. Note The mathematical symbols appear even when the number is positive. |
| ^ (optional) | Modifier that formats the number in engineering notation, where the exponent is always a multiple of three. Note This modifier must be used within a formatting node that has either an e or g conversion code in the format specifier. |
| # (optional) | Modifier that removes trailing zeros when used within a formatting node. If the number has no fractional part, this modifier also removes the description part. |
| 0 (optional) | Modifier that pads any excess space to the left of a numeric parameter with zeros, rather than spaces, to reach a minimum width when used within a formatting node. Note Using the - modifier with 0 nullifies the effect. |
| Width (optional) | Syntax element that specifies an exact field width to use. When used within a formatting node, the Width element specifies the minimum character field with of the output. The field is padded to the left or right of the parameter with spaces, depending on justification. Note As many characters as necessary are used to format the parameter without truncating it. |
| .Precision or _Significant Digits (optional) | Syntax element that controls the number of digits displayed when used within a formatting node. .precision—Yields the number of digits to the right of the decimal point. _Significant Digits—Rounds the data to the number of digits you specify. Note You cannot use precision and significant digits together in a single format specifier. |
| {Unit} (optional) | Syntax element that overrides the original unit of a VI when you use a node to convert a physical quantity. |
| <Embedded Time Format> (optional) | Contains a time-specific format string for use with the T (absolute time) and the t (relative time) conversion codes. Note Only %W, %D, %H, %M, %S, and %u apply to relative time. |
| Conversion Codes | Characters that specify how to scan or format a parameter. x—Hexadecimal integer o—Octal integer b—Binary integer d—Signed decimal integer u—Unsigned decimal integer f—Floating-point number with fractional format e—Floating-point number in scientific notation g—Uses f or e depending on the exponent of the number p—Floating-point number in SI notation s—Scans a string, matching only up to the next white-space character. [ ]—Scans characters in a set, matching a string that contains only the characters specified between the brackets. % [aeiou]—Scans characters in a set, matching any string that contains only lowercase vowels % [0-9a-zA-Z ]— Scans characters in a set, matching a string that contains numbers, letters, or spaces. You can use a hyphen to specify ranges of characters in the set. % [^,;]— Scans characters in a set, matching any string of characters up to but not including the first comma or semicolon. T—Absolute time t—Relative time |
| Localization Codes | Characters that determine whether to use a decimal or a comma to separate the whole number from the decimal part of the number. %,;—Comma decimal separator %.;—Period decimal separator %;—System default separator |
| Backslash (\\) Codes | Characters that specify hex values, spacing, backspaces, and other formatting options. |

##### Format Specifier Examples for Format String

| format string | file path | actual path | Comments |
| --- | --- | --- | --- |
| %d | C:\\test.txt | C:\\test (1).txt | The %d in format string specifies that the node appends an incrementing number starting with 1 to the filename before the period (.). Note There is a space at the beginning of the format string. |
| %4d | C:\\test.txt | C:\\test 1.txt | The 4 in format string specifies that the suffix after the filename and before the period (.) has a width of 4. |

[IMAGE alt='datatype_icon' src='/assets/img/cpath.png']

##### file

Absolute path to the file you want to create. If you specify an empty or relative path, this node returns an error.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### disable buffering

A Boolean that specifies whether the file opens without buffering, which, for large amounts of data, may increase the rate of data transfer to the file.

| True | The file opens without buffering. |
| --- | --- |
| False | The file opens with buffering. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### reference

A reference to the file this node creates.

[IMAGE alt='datatype_icon' src='/assets/img/ipath.png']

##### actual path

Path to the file this node creates.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

The node produces this output according to standard error behavior.

This node can return the following error codes.

| 1430 | The path is empty or relative. You must use an absolute path. |
| --- | --- |

Note

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Storage Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=curve-fitting-linear.html language=enus -->
## TOPIC 00017: Linear

- bundle_id: `daqexpress-api-ref`
- source_path: `curve-fitting-linear.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/curve-fitting-linear.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Finds the line that best represents an input signal or input data set using a specific fitting method. reset A Boolean that specifies whether to reset the internal state of the node. True Resets the internal state of the node. False Does not reset the internal state of the node. This input is availa

Linear

Finds the line that best represents an input signal or input data set using a specific fitting method.

[IMAGE alt='1378' src='Linear_Fit_Waveform.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset

A Boolean that specifies whether to reset the internal state of the node.

| True | Resets the internal state of the node. |
| --- | --- |
| False | Does not reset the internal state of the node. |

This input is available only if you wire a double-precision, floating-point number to y or signal.

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cmsdt.png']

##### signal

Input signal.

This input accepts a waveform or a 1D array of waveforms.

This input changes to y when the data type is a double-precision, floating-point number or a 1D array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### y

Dependent values representing the y-values of the data set.

This input accepts a double-precision, floating-point number or a 1D array of double-precision, floating-point numbers.

This input changes to signal when the data type is a waveform or a 1D array of waveforms.

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### x

Independent values representing the x-values of the data set.

This input accepts a double-precision, floating-point number or a 1D array of double-precision, floating-point numbers.

This input is available only if you wire a double-precision, floating-point number or a 1D array of double-precision, floating-point numbers to y or signal.

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### weight

An array of weights for the data set.

This input is available only if you wire one of the following data types to signal or y:

- Waveform
- 1D array of waveforms
- 1D array of double-precision, floating-point numbers

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### tolerance

Value that determines when to stop the iterative adjustment of the slope and intercept when you use the Least Absolute Residual or Bisquare methods.

If tolerance is less than or equal to 0, this node sets tolerance to 0.0001.

This input is available only if you wire one of the following data types to signal or y.

- Waveform
- 1D array of waveforms
- 1D array of double-precision, floating-point numbers

Default value: 0.0001

##### How tolerance Affects the Outputs with Different Fitting Methods

For the Least Absolute Residual method, if the relative difference between residue in two successive iterations is less than tolerance, this node returns the resulting residue. For the Bisquare method, if any relative difference between slope and intercept in two successive iterations is less than tolerance, this node returns the resulting slope and intercept.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### block size

Length of each set of data. The node performs computation for each set of data.

When you set block size to zero, the node calculates a cumulative solution for the input data from the time that you called or initialized the node. When block size is greater than zero, the node calculates the solution for only the newest set of input data.

This input is available only if you wire a double-precision, floating-point number to signal or y.

Default value: 100

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### parameter bounds

Upper and lower constraints for the slope and intercept of the calculated best linear fit.

This input is available only if you wire one of the following data types to signal or y:

- Waveform
- 1D array of waveforms
- 1D array of double-precision, floating-point numbers

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### slope min

Lower bound for the slope.

Default value: -Infinity

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### slope max

Upper bound for the slope.

Default value: Infinity

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### intercept min

Lower bound for the intercept.

Default value: -Infinity

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### intercept max

Upper bound for the intercept.

Default value: Infinity

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### method

Method of fitting data to a line.

This input is available only if you wire one of the following data types to signal or y:

- Waveform
- 1D array of waveforms
- 1D array of double-precision, floating-point numbers

| Least Square | 0 | Uses the least square method. |
| --- | --- | --- |
| Least Absolute Residual | 1 | Uses the least absolute residual method. |
| Bisquare | 2 | Uses the bisquare method. |

Default value: Least Square

##### Algorithm for the Least Square Method

The least square method of fitting finds the slope and intercept of the linear model by minimizing residue according to the following equation:

where

- N is the length of y or the number of data values in a waveform
- w 
 i is the i th element of weight
- f 
 i is the i th element of best linear fit
- y 
 i is the i th element of y or the i th data value in a waveform

##### Algorithm for the Least Absolute Residual Method

The least absolute residual method finds the slope and intercept of the linear model by minimizing residue according to the following equation:

where

- N is the length of y or the number of data values in a waveform
- w 
 i is the i th element of weight
- f 
 i is the i th element of best linear fit
- y 
 i is the i th element of y or the i th data value in a waveform

##### Algorithm for the Bisquare Method

The bisquare method of fitting finds the slope and intercept using an iterative process, as shown in the following illustration.

[IMAGE alt='1378' src='GUID-4285140F-420D-481C-87DE-3C5B147D69CE-a5.svg']

The node calculates residue according to the following equation:

where

- N is the length of y or the number of data values in a waveform
- w 
 i is the i th element of weight
- f 
 i is the i th element of best linear fit
- y 
 i is the i th element of y or the i th data value in a waveform.

[IMAGE alt='datatype_icon' src='/assets/img/imsdt.png']

##### best linear fit

Linear curve that best fits the input signal.

This output can return the following data types:

- Waveform
- 1D array of waveforms
- 1D array of double-precision, floating-point numbers

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### slope

Slope of the calculated best linear fit.

This output can return a double-precision, floating-point number or a 1D array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### intercept

Intercept of the calculated best linear fit.

This output can return a double-precision, floating-point number or a 1D array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### residue

Weighted mean error of the fitted model.

This output can return a double-precision, floating-point number or a 1D array of double-precision, floating-point numbers.

##### Algorithm for Calculating residue When the Input Signal is a Double-Precision, Floating-Point Number

When the input signal is a double-precision, floating-point number, this node calculates residue according to the following equation:

where

- N is the number of elements in the data set
- f 
 i is the i th element of best linear fit
- y 
 i is the y component of the i th input data point

#### Examples

The following illustration shows a linear fit result using this node.

[IMAGE alt='1378' src='GUID-8E6BF315-FFAD-437E-A9DB-DE18B8A181C4-a5.png']

#### Algorithm for Calculating best linear fit

This node uses the general least squares method to fit the data points in an input signal to a straight line of the general form described by the following equation:

f

=

a

x

+

b

f

=

a

x

+

b

where x is an input sequence, a is the slope of best linear fit, and b is the intercept of best linear fit.

This node finds the values of a and b that best fit the observations (X, Y). When the input signal is a double-precision, floating-point number or an array of double-precision, floating-point numbers, X is the x component of the input signal and Y is y component of the input signal. When the input signal is a waveform or an array of waveforms, X is the input sequence calculated from the start time of the waveform and Y is the data values in the waveform.

The following equation describes the linear curve resulting from the linear fit algorithm:

y

[

i

]

=

a

x

[

i

]

+

b

y

[

i

]

=

a

x

[

i

]

+

b

Parent topic:

Curve Fitting

<!--NI_TOPIC bundle=daqexpress-api-ref path=curve-fitting-multimode-function.html language=enus -->
## TOPIC 00018: Curve Fitting

- bundle_id: `daqexpress-api-ref`
- source_path: `curve-fitting-multimode-function.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/curve-fitting-multimode-function.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs curve fitting on a signal or data set.

Curve Fitting

Performs curve fitting on a signal or data set.

Fitting Nodes

Linear

Finds the line that best represents an input signal or input data set using a specific fitting method.

Polynomial

Finds the set of polynomial fit coefficients that best represents an input signal or input data set using a specific fitting method.

Parent topic:

Fitting Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=decimal-digit.html language=enus -->
## TOPIC 00019: Decimal Digit?

- bundle_id: `daqexpress-api-ref`
- source_path: `decimal-digit.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/decimal-digit.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns True if a value represents a decimal digit ranging from 0 through 9. Otherwise, this node returns False. If the value is a string, this node uses the first character in the string. If the value is a number, this node interprets it as the ASCII value of a character. If the value is a floating

Decimal Digit?

Returns True if a value represents a decimal digit ranging from 0 through 9. Otherwise, this node returns False.

If the value is a string, this node uses the first character in the string. If the value is a number, this node interprets it as the ASCII value of a character. If the value is a floating-point number, this node rounds to the nearest integer.

[IMAGE alt='1378' src='IsDecimalDigit.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### char

An input to this operation.

This input supports scalar strings or numbers, clusters of strings or numbers, arrays of strings or numbers, and so on.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### digit?

Boolean result of the operation.

This output assumes the same data type structure as 
 char.

Parent topic:

Comparison Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=display-error.html language=enus -->
## TOPIC 00020: Display Error

- bundle_id: `daqexpress-api-ref`
- source_path: `display-error.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/display-error.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a dialog that displays details if an error or warning occurs. This node does nothing if no error or warning occurs. error in An error cluster that you use to check for errors or warnings. Standard Error Behavior type of dialog Type of dialog box to display, if any. Regardless of this value, th

Display Error

Opens a dialog that displays details if an error or warning occurs. This node does nothing if no error or warning occurs.

[IMAGE alt='1378' src='Display_Error.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

An error cluster that you use to check for errors or warnings.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### type of dialog

Type of dialog box to display, if any.

Regardless of this value, this node returns the error information and a message describing the error.

| no dialog | Displays no dialog box. This is useful if you want to have programmatic control over handling errors. |
| --- | --- |
| OK message | Displays a dialog box with a single OK button if an error occurs. After the user clicks OK, this node returns control to the main diagram. |
| continue or stop message | Displays a dialog box with buttons if an error occurs. The buttons either continue or stop execution. |
| OK message + warnings | Displays a dialog box with a single OK button if an error or warning occurs. After the user clicks OK, this node returns control to the main diagram. |
| continue/stop + warnings | Displays a dialog box with buttons if an error or warning occurs. The buttons either continue or stop execution. |

Default value: 
 OK message

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### error?

A Boolean that indicates if an error occurred.

| True | An error occurred. |
| --- | --- |
| False | A warning occurred or no error or warning occurred. |

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### code

The error or warning code.

error?

code

error?

code

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### location

A string describing where the error or warning occurred.

This string is empty if the error cluster contains no location information. If the error cluster contains a call chain, this node returns the call chain formatted as a single, multiline string.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### description

The human-readable error description of the error cluster.

No error

Parent topic:

Error Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=divide.html language=enus -->
## TOPIC 00021: Divide

- bundle_id: `daqexpress-api-ref`
- source_path: `divide.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/divide.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the quotient of the inputs. x The dividend. This input supports scalar numbers, arrays, or clusters of numbers, arrays of clusters of numbers, and waveforms. A waveform can only be divided by either another waveform or a scalar numeric value. Data Type Changes on FPGA When you add this node

Divide

Computes the quotient of the inputs.

[IMAGE alt='1378' src='Divide.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

The dividend.

This input supports scalar numbers, arrays, or clusters of numbers, arrays of clusters of numbers, and waveforms.

A waveform can only be divided by either another waveform or a scalar numeric value.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### y

The divisor.

This input supports scalar numbers, arrays or clusters of numbers, arrays of clusters of numbers, and waveforms.

A waveform can only be divided by either another waveform or a scalar numeric value.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

This input appears only when you wire a waveform to input.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### x / y

The quotient.

In general, the output type is the widest representation of the inputs if the inputs are not integers or if their representations differ.

##### Behavior with Integers

If both x and y are integers, x / y is a double-precision, floating-point number.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

The node produces this output according to standard error behavior.

This output appears only when you wire a waveform to input.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=empty-string-path.html language=enus -->
## TOPIC 00022: Empty String or Path?

- bundle_id: `daqexpress-api-ref`
- source_path: `empty-string-path.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/empty-string-path.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns whether the input is an empty string or path. string or path The string or path that you want to evaluate. This input can also be any data type that contains only strings or paths, such as an array of strings or paths or a cluster of strings or paths. empty? A Boolean specifying whether the

Empty String or Path?

Returns whether the input is an empty string or path.

[IMAGE alt='1378' src='IsEmptyStringOrPath.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### string or path

The string or path that you want to evaluate.

This input can also be any data type that contains only strings or paths, such as an array of strings or paths or a cluster of strings or paths.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### empty?

A Boolean specifying whether the input is empty.

This value is of the same data type structure as 
 string or path. For example, if string or path is an array, empty? is also an array.

Parent topic:

Comparison Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=error-cluster-constant.html language=enus -->
## TOPIC 00023: Error Cluster Constant

- bundle_id: `daqexpress-api-ref`
- source_path: `error-cluster-constant.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/error-cluster-constant.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a constant error on the diagram.

Error Cluster Constant

Represents a constant error on the diagram.

[IMAGE alt='1378' src='Literal.Error.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=daqexpress-api-ref path=filter-bandpass.html language=enus -->
## TOPIC 00024: Bandpass

- bundle_id: `daqexpress-api-ref`
- source_path: `filter-bandpass.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/filter-bandpass.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Filters a signal using a Butterworth bandpass filter. Bandpass filters pass a certain band of frequencies. reset A Boolean that specifies the initialization of the internal state of the node. True Initializes the internal state to zero. False Initializes the internal state to the final state from th

Bandpass

Filters a signal using a Butterworth bandpass filter. Bandpass filters pass a certain band of frequencies.

[IMAGE alt='1378' src='Butterworth_Bandpass_Filter_(Waveform).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset

A Boolean that specifies the initialization of the internal state of the node.

| True | Initializes the internal state to zero. |
| --- | --- |
| False | Initializes the internal state to the final state from the previous call of this node. |

This node automatically initializes the internal state to zero on the first call and runs continuously until this input is True.

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cmsdt.png']

##### signal

The input signal.

This input supports the following data types:

- Waveform
- Array of waveforms
- 1D array of double-precision, floating-point numbers
- 2D array of double-precision, floating-point numbers

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### low cutoff frequency

Low cutoff frequency of the filter.

low cutoff frequency

high cutoff frequency

Default value: 0.125

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### high cutoff frequency

High cutoff frequency of the filter.

high cutoff frequency

low cutoff frequency

f

s

f

s

Default value: 0.45

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### order

Order of the filter.

Default value: 2

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### sampling frequency

Sampling frequency in Hz.

sampling frequency

This input is available only if you wire one of the following data types to signal:

- Double-precision, floating-point number
- Complex double-precision, floating-point number
- 1D array of double-precision, floating-point numbers
- 1D array of complex double-precision, floating-point numbers
- 2D array of double-precision, floating-point numbers

Default value: 1, which is the normalized sampling frequency

[IMAGE alt='datatype_icon' src='/assets/img/imsdt.png']

##### filtered signal

Result of filtering the input signal.

This output can return the following data types:

- Waveform
- Double-precision, floating-point number
- Complex double-precision, floating-point number
- 1D array of waveforms
- 1D array of double-precision, floating-point numbers
- 1D array of complex double-precision, floating-point numbers
- 2D array of double-precision, floating-point numbers

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Filter

<!--NI_TOPIC bundle=daqexpress-api-ref path=filter-bandstop.html language=enus -->
## TOPIC 00025: Bandstop

- bundle_id: `daqexpress-api-ref`
- source_path: `filter-bandstop.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/filter-bandstop.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Filters a signal using a Butterworth bandstop filter. Bandstop filters attenuate a certain band of frequencies. reset A Boolean that specifies the initialization of the internal state of the node. True Initializes the internal state to zero. False Initializes the internal state to the final state fr

Bandstop

Filters a signal using a Butterworth bandstop filter. Bandstop filters attenuate a certain band of frequencies.

[IMAGE alt='1378' src='Butterworth_Bandstop_Filter_(Waveform).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset

A Boolean that specifies the initialization of the internal state of the node.

| True | Initializes the internal state to zero. |
| --- | --- |
| False | Initializes the internal state to the final state from the previous call of this node. |

This node automatically initializes the internal state to zero on the first call and runs continuously until this input is True.

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cmsdt.png']

##### signal

The input signal.

This input supports the following data types:

- Waveform
- Array of waveforms
- 1D array of double-precision, floating-point numbers
- 2D array of double-precision, floating-point numbers

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### low cutoff frequency

Low cutoff frequency of the filter.

low cutoff frequency

high cutoff frequency

Default value: 0.125

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### high cutoff frequency

High cutoff frequency of the filter.

high cutoff frequency

low cutoff frequency

f

s

f

s

Default value: 0.45

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### order

Order of the filter.

Default value: 2

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### sampling frequency

Sampling frequency in Hz.

sampling frequency

This input is available only if you wire one of the following data types to signal:

- Double-precision, floating-point number
- Complex double-precision, floating-point number
- 1D array of double-precision, floating-point numbers
- 1D array of complex double-precision, floating-point numbers
- 2D array of double-precision, floating-point numbers

Default value: 1, which is the normalized sampling frequency

[IMAGE alt='datatype_icon' src='/assets/img/imsdt.png']

##### filtered signal

Result of filtering the input signal.

This output can return the following data types:

- Waveform
- Double-precision, floating-point number
- Complex double-precision, floating-point number
- 1D array of waveforms
- 1D array of double-precision, floating-point numbers
- 1D array of complex double-precision, floating-point numbers
- 2D array of double-precision, floating-point numbers

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Filter

<!--NI_TOPIC bundle=daqexpress-api-ref path=filter-highpass.html language=enus -->
## TOPIC 00026: Highpass

- bundle_id: `daqexpress-api-ref`
- source_path: `filter-highpass.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/filter-highpass.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Filters a signal using a Butterworth highpass filter. Highpass filters pass high frequencies and attenuate low frequencies. reset A Boolean that specifies the initialization of the internal state of the node. True Initializes the internal state to zero. False Initializes the internal state to the fi

Highpass

Filters a signal using a Butterworth highpass filter. Highpass filters pass high frequencies and attenuate low frequencies.

[IMAGE alt='1378' src='Butterworth_Highpass_Filter_(Waveform).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset

A Boolean that specifies the initialization of the internal state of the node.

| True | Initializes the internal state to zero. |
| --- | --- |
| False | Initializes the internal state to the final state from the previous call of this node. |

This node automatically initializes the internal state to zero on the first call and runs continuously until this input is True.

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cmsdt.png']

##### signal

The input signal.

This input supports the following data types:

- Waveform
- Array of waveforms
- 1D array of double-precision, floating-point numbers
- 2D array of double-precision, floating-point numbers

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### cutoff frequency

Cutoff frequency of the filter.

Default value: 0.125

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### order

Order of the filter.

Default value: 2

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### sampling frequency

Sampling frequency in Hz.

sampling frequency

This input is available only if you wire one of the following data types to signal:

- Double-precision, floating-point number
- Complex double-precision, floating-point number
- 1D array of double-precision, floating-point numbers
- 1D array of complex double-precision, floating-point numbers
- 2D array of double-precision, floating-point numbers

Default value: 1, which is the normalized sampling frequency

[IMAGE alt='datatype_icon' src='/assets/img/imsdt.png']

##### filtered signal

Result of filtering the input signal.

This output can return the following data types:

- Waveform
- Double-precision, floating-point number
- Complex double-precision, floating-point number
- 1D array of waveforms
- 1D array of double-precision, floating-point numbers
- 1D array of complex double-precision, floating-point numbers
- 2D array of double-precision, floating-point numbers

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Filter

<!--NI_TOPIC bundle=daqexpress-api-ref path=filter-lowpass.html language=enus -->
## TOPIC 00027: Lowpass

- bundle_id: `daqexpress-api-ref`
- source_path: `filter-lowpass.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/filter-lowpass.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Filters a signal using a Butterworth lowpass filter. Lowpass filters pass low frequencies and attenuate high frequencies. reset A Boolean that specifies the initialization of the internal state of the node. True Initializes the internal state to zero. False Initializes the internal state to the fina

Lowpass

Filters a signal using a Butterworth lowpass filter. Lowpass filters pass low frequencies and attenuate high frequencies.

[IMAGE alt='1378' src='Butterworth_Lowpass_Filter_(Waveform).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset

A Boolean that specifies the initialization of the internal state of the node.

| True | Initializes the internal state to zero. |
| --- | --- |
| False | Initializes the internal state to the final state from the previous call of this node. |

This node automatically initializes the internal state to zero on the first call and runs continuously until this input is True.

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cmsdt.png']

##### signal

The input signal.

This input supports the following data types:

- Waveform
- Array of waveforms
- 1D array of double-precision, floating-point numbers
- 2D array of double-precision, floating-point numbers

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### cutoff frequency

Cutoff frequency of the filter.

Default value: 0.125

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### order

Order of the filter.

Default value: 2

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### sampling frequency

Sampling frequency in Hz.

sampling frequency

This input is available only if you wire one of the following data types to signal:

- Double-precision, floating-point number
- Complex double-precision, floating-point number
- 1D array of double-precision, floating-point numbers
- 1D array of complex double-precision, floating-point numbers
- 2D array of double-precision, floating-point numbers

Default value: 1, which is the normalized sampling frequency

[IMAGE alt='datatype_icon' src='/assets/img/imsdt.png']

##### filtered signal

Result of filtering the input signal.

This output can return the following data types:

- Waveform
- Double-precision, floating-point number
- Complex double-precision, floating-point number
- 1D array of waveforms
- 1D array of double-precision, floating-point numbers
- 1D array of complex double-precision, floating-point numbers
- 2D array of double-precision, floating-point numbers

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Filter

<!--NI_TOPIC bundle=daqexpress-api-ref path=filter-multimode-function.html language=enus -->
## TOPIC 00028: Filter

- bundle_id: `daqexpress-api-ref`
- source_path: `filter-multimode-function.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/filter-multimode-function.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Processes signals through a lowpass, highpass, bandpass, or bandstop filter.

Filter

Processes signals through a lowpass, highpass, bandpass, or bandstop filter.

Signal Processing Nodes

Bandpass

Filters a signal using a Butterworth bandpass filter. Bandpass filters pass a certain band of frequencies.

Bandstop

Filters a signal using a Butterworth bandstop filter. Bandstop filters attenuate a certain band of frequencies.

Highpass

Filters a signal using a Butterworth highpass filter. Highpass filters pass high frequencies and attenuate low frequencies.

Lowpass

Filters a signal using a Butterworth lowpass filter. Lowpass filters pass low frequencies and attenuate high frequencies.

Parent topic:

Signal Processing Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=first-call.html language=enus -->
## TOPIC 00029: First Call?

- bundle_id: `daqexpress-api-ref`
- source_path: `first-call.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/first-call.html
- document_id: `daqexpress-api-ref`
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

<!--NI_TOPIC bundle=daqexpress-api-ref path=flat-sequence.html language=enus -->
## TOPIC 00030: Sequence Structure

- bundle_id: `daqexpress-api-ref`
- source_path: `flat-sequence.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/flat-sequence.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Consists of one or more subdiagrams, or frames, that execute sequentially. Use the Sequence Structure to ensure that a subdiagram executes before or after another subdiagram. Dataflow for the Sequence Structure differs from dataflow for other structures. Frames in a Sequence Structure execute from l

Sequence Structure

Consists of one or more subdiagrams, or frames, that execute sequentially.

Use the Sequence Structure to ensure that a subdiagram executes before or after another subdiagram.

Dataflow for the Sequence Structure differs from dataflow for other structures. Frames in a Sequence Structure execute from left to right and when all data values wired to a frame are available. The data leaves each frame as the frame finishes executing. This means the input of one frame can depend on the output of another frame.

#### Inputs/Outputs

##### Tunnel

Point through which data enters or exits a structure.

[IMAGE alt='1378' src='GUID-43DB7847-2DDA-4B38-86E0-27BE4951A189-a5.png']

[IMAGE alt='1378' src='GUID-576AD071-36DE-4DB2-812C-E5C8DBC156BA-a5.png']

#### Tunnel Restrictions

You cannot drag tunnels across the frames of a Sequence Structure.

#### Avoid Overuse

Attempt to control the dataflow of your VI by establishing data dependency or using flow-through parameters.

Parent topic:

Program Flow Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=format-date-time-string.html language=enus -->
## TOPIC 00031: Format Date and Time String

- bundle_id: `daqexpress-api-ref`
- source_path: `format-date-time-string.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/format-date-time-string.html
- document_id: `daqexpress-api-ref`
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

<!--NI_TOPIC bundle=daqexpress-api-ref path=format-into-file.html language=enus -->
## TOPIC 00032: Format into File

- bundle_id: `daqexpress-api-ref`
- source_path: `format-into-file.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/format-into-file.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Formats data as a string and writes it to a file. format string A string that includes a format specifier for each input along with any additional text that you want to appear in the output. A format specifier is a series of characters, initiated by a %, that indicates how to convert the associated

Format into File

Formats data as a string and writes it to a file.

[IMAGE alt='1378' src='FormatIntoFile.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### format string

A string that includes a format specifier for each input along with any additional text that you want to appear in the output.

%

Each format specifier uses the following general syntax:

% 
 modifiersspecifier

This input accepts a maximum of 255 characters.

Default value: A string containing the default format specifier for the data type of each input, separated by spaces

##### Specifiers

| Specifier | Definition |
| --- | --- |
| x | hexadecimal integer |
| o | octal integer |
| b | binary integer |
| d | signed decimal integer |
| u | unsigned decimal integer |
| f | floating-point number with fractional format |
| e | floating-point number in scientific notation |
| g | floating-point number in either fractional format (f) or scientific notation (e) depending on the exponent of the number: f—The exponent is greater than -4 and less than the precision specifiede—exponent is less than -4 or greater than the precision specified |
| ^e or ^g | floating-point number in engineering notation |
| p | floating-point number in SI notation |
| T | absolute time, most commonly used to interpret timestamp data |
| t | relative time, most commonly used to interpret numeric data as elapsed seconds |

##### Modifiers for Numeric Specifiers (x, o, b, d, u, f, e, g, p)

If you use multiple modifiers, they must appear in the following order:

%[-][+][#][0][width][.precision || 
 _significantDigits]specifier

| Modifier | Definition | Usage Example | Output for 12345 |
| --- | --- | --- | --- |
| 0 | Pads any excess space to the left of a numeric parameter with zeros rather than with spaces to reach minimum width. | %06_2f | 012000 |
| + | Includes the sign of the number even when the number is positive. | %+6_2f | +12000 |
| # | Removes zeros at the end of the number. |  |  |
| - | Left justifies the output within its width. If the node inserts spaces to create the specified width, the spaces appear to the right of the value. | %-6_2f | 12000_ |
| width | A number specifying the minimum number of characters that the node uses in the output. If the value requires fewer characters, the node pads the output with spaces to meet this width. This width is not a maximum width. The node uses as many characters as necessary to output the value without truncating it. Non-numeric characters, such as a decimal point or negative sign, count toward the total width of an output string. If width is missing or 0, the output uses only as many characters as necessary to contain the formatted value. | %6f | _12345 |
| width . precision | A number specifying how many digits appear to the right of the decimal point in the output. If neither .precision nor _significantDigits is present, the node uses a precision of six digits. If precision is 0, the node rounds the value to the nearest whole number. | %6.2f | 12345.00 |
| width _ significantDigits | A number specifying how many significant digits appear in the output. The node rounds the data only for display purposes, which does not affect the original data. You cannot use .precision and _significantDigits together in a single format specifier. | %6_2f | _12000 |

##### Modifiers for Time Specifiers (t, T)

Use the following syntax to specify which parts of a time you want to format:

%[-]width <time specifier codes>t

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

| Modifier | Definition |
| --- | --- |
| - | Left justifies the output within its width. If the node inserts spaces to create the specified width, the spaces appear to the right of the value. |
| width | A number specifying the minimum number of characters that the node uses in the output. If the value requires fewer characters, the node pads the output with spaces to meet this width. This width is not a maximum width. The node uses as many characters as necessary to output the value without truncating it. If width is missing or 0, the output uses only as many characters as necessary to contain the formatted value. |

##### Modifiers for the String Specifier (s)

Use the following syntax to format a string:

%[-]width s

| Modifier | Definition |
| --- | --- |
| - | Left justifies the output within its width. If the node inserts spaces to create the specified width, the spaces appear to the right of the value. |
| width | A number specifying the minimum number of characters that the node uses in the output. If the value requires fewer characters, the node pads the output with spaces to meet this width. This width is not a maximum width. The node uses as many characters as necessary to output the value without truncating it. If width is missing or 0, the output uses only as many characters as necessary to contain the formatted value. |

##### Modifier for Reordering Inputs

| Modifier | Definition |
| --- | --- |
| number $ | Explicitly specifies which input to use for the containing format specifier. This modifier overrides the default input with the input specified by number. When you use this modifier, the subsequent format specifiers become associated with the inputs that follow the input specified by number. To avoid confusion, National Instruments recommends using this modifier in all format specifiers if you use it in one. |

##### Modifiers for Overriding Units

| Modifier | Definition |
| --- | --- |
| { unit } | Overrides the original unit of a VI when you use a function to convert a physical quantity (a value with an associated unit). You must use a compatible unit. |

##### Syntax for Including Literal Characters in a Format String

Most characters outside of a format specifier appear literally in the output. However, you must use special syntax for the following special characters:

| Syntax | Definition |
| --- | --- |
| \\00 - \\FF | Hex value of an 8-bit character; must be uppercase |
| \\b | Backspace (ASCII BS, equivalent to \\08) |
| \\f | Form feed (ASCII FF, equivalent to \\0C) |
| \\n | Linefeed (ASCII LF, equivalent to \\0A). Format into File automatically converts this code into the platform-dependent end-of-line character. |
| \\r | Carriage return (ASCII CR, equivalent to \\0D) |
| \\t | Tab (ASCII HT, equivalent to \\09) |
| \\s | Space (equivalent to \\20) |
| \\\\ | Backslash (ASCII \\, equivalent to \\5C) |
| %% | Percent sign |

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### input file

The file that this node uses.

This input can be a reference to a file or an absolute file path. In both cases, the node creates the specified file if it does not already exist. The node opens the specified file without requiring you to call Open/Create/Replace File first.

If you specify an empty or relative path, this node returns an error.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### input

Input data to be converted to text, as determined by the corresponding format specifier in format string. This node assigns inputs to format specifiers sequentially, such that the first format specifier formats input 1, the second format specifier formats input 2, and so on.

Each input can be a string, path, Boolean, enumerated type, timestamp, or numeric value. You cannot use arrays and clusters with this node.

The number of input parameters must match the number of format specifiers in format string. Furthermore, the data type of each input must be compatible with the associated format specifier. Otherwise, the node returns an error.

Note

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### output file

The reference to the file to which the node wrote the formatted data.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Examples

| Syntax element(s) | input | format string | output | Comments |
| --- | --- | --- | --- | --- |
| %g # modifier | 12.00 | %#g | 12 | The node interprets the g specifier as f because the exponent of the input in scientific notation (1) is less than the default precision of 6. The # modifier omits the six zeroes that would normally appear after the decimal based on the default precision of 6. |
| 12000000 | %#g | 1.2E+7 | The node interprets the g specifier as e because the exponent of the input in scientific notation (7) is greater than the default precision of 6. The # modifier omits the six zeroes that would normally appear after the decimal based on the default precision of 6. |  |
| %d literal % | 12.67 | score= %d%% | score= 13% | Because the d specifier produces an integer output, the input is rounded to the nearest integer. %% produces a literal %. |
| width precision literal text | 12.67 | Temp: %5.1f | Temp: 12.7 | The 5 in the format specifier specifies a width of 5, and the 1 specifies the precision, or number of digits to the right of the decimal. |
| overriding units | 12.67 N | %5.3f | 12.670 N | The format specifier does not include the unit override syntax ({ }), so the output contains the original unit. |
| 12.67 N | %5.3{mN}f | 12670.000 mN | {mN} is compatible with N, so the node makes the appropriate conversion. |  |
| 12.67 N | %5.3{kg}f | 12.670 ?kg | {kg} is not compatible with N, so no conversion occurs, and the output includes a ?. |  |
| converting to engineering notation | 12.67 | %.3e | 1.267E+1 | Without the ^ modifier, the e specifier places the decimal to the right of the most significant digit. |
| 12.67 | %^.3e | 12.670E+0 | Adding ^ to the format specifier produces an output in which the exponent is a multiple of 3. This determines the placement of the decimal. |  |
| %p precision vs. significant digits | 12000000 | %.2p | 120.00M | Using the decimal point as part of the format specifier impacts the precision, or number of digits after the decimal point in the output. mega (10^6) is the closest SI prefix to the input value, so the output represents the value as M. |
| 12000000 | %_2p | 120M | Using the _ modifier specifies the number of significant digits in the output. mega (10^6) is the closest SI prefix to the input value, so the output represents the value as M. |  |
| non-decimal numbers (%x, %o, %b) padding with zeroes | 12 | %02x | 0C | The 2 in the format specifier causes the output to contain at least 2 characters. The 0 in the format specifier causes 0's to appear as the extra characters required to meet the width. |
| 12 | %06o | 000014 | The 6 in the format specifier causes the output to contain at least 6 characters. The 0 in the format specifier causes 0's to appear as the extra characters required to meet the width. |  |
| 12 | %b | 1100 | This format specifier omits the width, so the output contains only enough characters to represent the input value as a binary number. |  |
| %s multiple format specifiers | Smith John | Name: %s, %s. | Name: Smith, John. | The format string must contain two format specifiers because the node accepts two inputs. |
| variable order | first second | %s %s | first second | format string does not use the $ specifier, so the function populates the percent codes in input order. |
| first second | %2$s %1$s | second first | format string uses the $ specifier to display the inputs in a different order than their input order. |  |
| first second | %1$s %1$s %1$s | first first first | format string uses the $ specifier to display the first input multiple times and ignore the second input. |  |
| first second | %2$s %s | error | The first format specifier uses the second input, which causes the next format specifier to want to use a third input. Because there are only two inputs, the node returns an error. |  |

#### Troubleshooting "Too few/many format specifiers" Error

These errors occur when you wire a string to 
 format string that contains a different number of format specifiers than there are input parameters. To fix this mismatch, either resize the node to display the same number of inputs as format specifiers, or modify the number of format specifiers in format string to match the number of inputs.

#### Troubleshooting "Format specifier type mismatch" Error

This error occurs when you wire a string to 
 format string that contains at least one format specifier whose data type specifier is incompatible with the data type of the corresponding input parameter. The text of the error specifies which parameter caused the mismatch. To fix this mismatch, you must change either the data type specifier in the relevant format specifier or wire a compatible data type to the relevant input.

Parent topic:

Storage Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=format-into-string.html language=enus -->
## TOPIC 00033: Format into String

- bundle_id: `daqexpress-api-ref`
- source_path: `format-into-string.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/format-into-string.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Inserts input data into specified locations in a string and formats that data according to your specifications. format string A string that includes a format specifier for each input along with any additional text that you want to appear in the output. A format specifier is a series of characters, i

Format into String

Inserts input data into specified locations in a string and formats that data according to your specifications.

[IMAGE alt='1378' src='FormatIntoString.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### format string

A string that includes a format specifier for each input along with any additional text that you want to appear in the output.

%

Each format specifier uses the following general syntax:

% 
 modifiersspecifier

This input accepts a maximum of 255 characters.

Default value: A string containing the default format specifier for the data type of each input, separated by spaces

##### Specifiers

| Specifier | Definition |
| --- | --- |
| x | hexadecimal integer |
| o | octal integer |
| b | binary integer |
| d | signed decimal integer |
| u | unsigned decimal integer |
| f | floating-point number with fractional format |
| e | floating-point number in scientific notation |
| g | floating-point number in either fractional format (f) or scientific notation (e) depending on the exponent of the number: f—The exponent is greater than -4 and less than the precision specifiede—exponent is less than -4 or greater than the precision specified |
| ^e or ^g | floating-point number in engineering notation |
| p | floating-point number in SI notation |
| T | absolute time, most commonly used to interpret timestamp data |
| t | relative time, most commonly used to interpret numeric data as elapsed seconds |

##### Modifiers for Numeric Specifiers (x, o, b, d, u, f, e, g, p)

If you use multiple modifiers, they must appear in the following order:

%[-][+][#][0][width][.precision || 
 _significantDigits]specifier

| Modifier | Definition | Usage Example | Output for 12345 |
| --- | --- | --- | --- |
| 0 | Pads any excess space to the left of a numeric parameter with zeros rather than with spaces to reach minimum width. | %06_2f | 012000 |
| + | Includes the sign of the number even when the number is positive. | %+6_2f | +12000 |
| # | Removes zeros at the end of the number. |  |  |
| - | Left justifies the output within its width. If the node inserts spaces to create the specified width, the spaces appear to the right of the value. | %-6_2f | 12000_ |
| width | A number specifying the minimum number of characters that the node uses in the output. If the value requires fewer characters, the node pads the output with spaces to meet this width. This width is not a maximum width. The node uses as many characters as necessary to output the value without truncating it. Non-numeric characters, such as a decimal point or negative sign, count toward the total width of an output string. If width is missing or 0, the output uses only as many characters as necessary to contain the formatted value. | %6f | _12345 |
| width . precision | A number specifying how many digits appear to the right of the decimal point in the output. If neither .precision nor _significantDigits is present, the node uses a precision of six digits. If precision is 0, the node rounds the value to the nearest whole number. | %6.2f | 12345.00 |
| width _ significantDigits | A number specifying how many significant digits appear in the output. The node rounds the data only for display purposes, which does not affect the original data. You cannot use .precision and _significantDigits together in a single format specifier. | %6_2f | _12000 |

##### Modifiers for Time Specifiers (t, T)

Use the following syntax to specify which parts of a time you want to format:

%[-]width <time specifier codes>t

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

| Modifier | Definition |
| --- | --- |
| - | Left justifies the output within its width. If the node inserts spaces to create the specified width, the spaces appear to the right of the value. |
| width | A number specifying the minimum number of characters that the node uses in the output. If the value requires fewer characters, the node pads the output with spaces to meet this width. This width is not a maximum width. The node uses as many characters as necessary to output the value without truncating it. If width is missing or 0, the output uses only as many characters as necessary to contain the formatted value. |

##### Modifiers for the String Specifier (s)

Use the following syntax to format a string:

%[-]width s

| Modifier | Definition |
| --- | --- |
| - | Left justifies the output within its width. If the node inserts spaces to create the specified width, the spaces appear to the right of the value. |
| width | A number specifying the minimum number of characters that the node uses in the output. If the value requires fewer characters, the node pads the output with spaces to meet this width. This width is not a maximum width. The node uses as many characters as necessary to output the value without truncating it. If width is missing or 0, the output uses only as many characters as necessary to contain the formatted value. |

##### Modifier for Reordering Inputs

| Modifier | Definition |
| --- | --- |
| number $ | Explicitly specifies which input to use for the containing format specifier. This modifier overrides the default input with the input specified by number. When you use this modifier, the subsequent format specifiers become associated with the inputs that follow the input specified by number. To avoid confusion, National Instruments recommends using this modifier in all format specifiers if you use it in one. |

##### Modifiers for Overriding Units

| Modifier | Definition |
| --- | --- |
| { unit } | Overrides the original unit of a VI when you use a function to convert a physical quantity (a value with an associated unit). You must use a compatible unit. |

##### Syntax for Including Literal Characters in a Format String

Most characters outside of a format specifier appear literally in the output. However, you must use special syntax for the following special characters:

| Syntax | Definition |
| --- | --- |
| \\00 - \\FF | Hex value of an 8-bit character; must be uppercase |
| \\b | Backspace (ASCII BS, equivalent to \\08) |
| \\f | Form feed (ASCII FF, equivalent to \\0C) |
| \\n | Linefeed (ASCII LF, equivalent to \\0A). Format into File automatically converts this code into the platform-dependent end-of-line character. |
| \\r | Carriage return (ASCII CR, equivalent to \\0D) |
| \\t | Tab (ASCII HT, equivalent to \\09) |
| \\s | Space (equivalent to \\20) |
| \\\\ | Backslash (ASCII \\, equivalent to \\5C) |
| %% | Percent sign |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### initial string

A string to which this node appends format string in order to form the 
resulting string.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### input

Input data to be converted to text, as determined by the corresponding format specifier in format string. This node assigns inputs to format specifiers sequentially, such that the first format specifier formats input 1, the second format specifier formats input 2, and so on.

Each input can be a string, path, Boolean, enumerated type, timestamp, or numeric value. You cannot use arrays and clusters with this node.

The number of input parameters must match the number of format specifiers in format string. Furthermore, the data type of each input must be compatible with the associated format specifier. Otherwise, the node returns an error.

Note

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### resulting string

The concatenation of initial string and the formatted output.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Examples

| Syntax element(s) | input | format string | output | Comments |
| --- | --- | --- | --- | --- |
| %g # modifier | 12.00 | %#g | 12 | The node interprets the g specifier as f because the exponent of the input in scientific notation (1) is less than the default precision of 6. The # modifier omits the six zeroes that would normally appear after the decimal based on the default precision of 6. |
| 12000000 | %#g | 1.2E+7 | The node interprets the g specifier as e because the exponent of the input in scientific notation (7) is greater than the default precision of 6. The # modifier omits the six zeroes that would normally appear after the decimal based on the default precision of 6. |  |
| %d literal % | 12.67 | score= %d%% | score= 13% | Because the d specifier produces an integer output, the input is rounded to the nearest integer. %% produces a literal %. |
| width precision literal text | 12.67 | Temp: %5.1f | Temp: 12.7 | The 5 in the format specifier specifies a width of 5, and the 1 specifies the precision, or number of digits to the right of the decimal. |
| overriding units | 12.67 N | %5.3f | 12.670 N | The format specifier does not include the unit override syntax ({ }), so the output contains the original unit. |
| 12.67 N | %5.3{mN}f | 12670.000 mN | {mN} is compatible with N, so the node makes the appropriate conversion. |  |
| 12.67 N | %5.3{kg}f | 12.670 ?kg | {kg} is not compatible with N, so no conversion occurs, and the output includes a ?. |  |
| converting to engineering notation | 12.67 | %.3e | 1.267E+1 | Without the ^ modifier, the e specifier places the decimal to the right of the most significant digit. |
| 12.67 | %^.3e | 12.670E+0 | Adding ^ to the format specifier produces an output in which the exponent is a multiple of 3. This determines the placement of the decimal. |  |
| %p precision vs. significant digits | 12000000 | %.2p | 120.00M | Using the decimal point as part of the format specifier impacts the precision, or number of digits after the decimal point in the output. mega (10^6) is the closest SI prefix to the input value, so the output represents the value as M. |
| 12000000 | %_2p | 120M | Using the _ modifier specifies the number of significant digits in the output. mega (10^6) is the closest SI prefix to the input value, so the output represents the value as M. |  |
| non-decimal numbers (%x, %o, %b) padding with zeroes | 12 | %02x | 0C | The 2 in the format specifier causes the output to contain at least 2 characters. The 0 in the format specifier causes 0's to appear as the extra characters required to meet the width. |
| 12 | %06o | 000014 | The 6 in the format specifier causes the output to contain at least 6 characters. The 0 in the format specifier causes 0's to appear as the extra characters required to meet the width. |  |
| 12 | %b | 1100 | This format specifier omits the width, so the output contains only enough characters to represent the input value as a binary number. |  |
| %s multiple format specifiers | Smith John | Name: %s, %s. | Name: Smith, John. | The format string must contain two format specifiers because the node accepts two inputs. |
| variable order | first second | %s %s | first second | format string does not use the $ specifier, so the function populates the percent codes in input order. |
| first second | %2$s %1$s | second first | format string uses the $ specifier to display the inputs in a different order than their input order. |  |
| first second | %1$s %1$s %1$s | first first first | format string uses the $ specifier to display the first input multiple times and ignore the second input. |  |
| first second | %2$s %s | error | The first format specifier uses the second input, which causes the next format specifier to want to use a third input. Because there are only two inputs, the node returns an error. |  |

#### Troubleshooting "Too few/many format specifiers" Error

These errors occur when you wire a string to 
 format string that contains a different number of format specifiers than there are input parameters. To fix this mismatch, either resize the node to display the same number of inputs as format specifiers, or modify the number of format specifiers in format string to match the number of inputs.

#### Troubleshooting "Format specifier type mismatch" Error

This error occurs when you wire a string to 
 format string that contains at least one format specifier whose data type specifier is incompatible with the data type of the corresponding input parameter. The text of the error specifies which parameter caused the mismatch. To fix this mismatch, you must change either the data type specifier in the relevant format specifier or wire a compatible data type to the relevant input.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=format-value.html language=enus -->
## TOPIC 00034: Format Value

- bundle_id: `daqexpress-api-ref`
- source_path: `format-value.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/format-value.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a number into a regular string and appends the result to the input string. string String to which this node appends the converted string. Default value: Empty string format string Method to convert the value to a string. Use the format string syntax. value Number you want to convert to a st

Format Value

Converts a number into a regular string and appends the result to the input string.

[IMAGE alt='1378' src='FormatValue.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### string

String to which this node appends the converted string.

Default value: Empty string

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### format string

Method to convert the value to a string.

Use the format string syntax.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### value

Number you want to convert to a string.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### output string

Result of converting the value to a string and appending this to the input string.

#### Converting Multiple Values

This node converts a single number each time it executes. The Format Into String node has the same functionality as Format Value but can convert multiple numbers at the same time. Consider using Format Into String instead of this node to simplify your diagram.

Parent topic:

String Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=generate-error-report.html language=enus -->
## TOPIC 00035: Generate Error Report

- bundle_id: `daqexpress-api-ref`
- source_path: `generate-error-report.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/generate-error-report.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates an error report string from an error cluster. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error include divider line A Boolean value that appends a line of hyphen

Generate Error Report

Generates an error report string from an error cluster.

[IMAGE alt='1378' src='Generate_Error_Report.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### include divider line

A Boolean value that appends a line of hyphens as the last line of the generated report.

| True | Appends a line of hyphens to the end of the error report. |
| --- | --- |
| False | Indicates no error report exists. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### error report

A multi-line string that describes the error or warning. This output returns 
Success if no error occurred.

Parent topic:

Error Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=get-current-time.html language=enus -->
## TOPIC 00036: Get Current Time

- bundle_id: `daqexpress-api-ref`
- source_path: `get-current-time.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/get-current-time.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a timestamp of the current time. current time Timestamp of the current time. Converting a Timestamp to a Floating-Point Number Use To Double Precision Float to convert the timestamp value to a lower precision, floating-point number.

Get Current Time

Returns a timestamp of the current time.

[IMAGE alt='1378' src='GetCurrentTime.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### current time

Timestamp of the current time.

#### Converting a Timestamp to a Floating-Point Number

Use To Double Precision Float to convert the timestamp value to a lower precision, floating-point number.

Parent topic:

Timestamp Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=greater-or-equal-to-0.html language=enus -->
## TOPIC 00037: Greater or Equal to 0?

- bundle_id: `daqexpress-api-ref`
- source_path: `greater-or-equal-to-0.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/greater-or-equal-to-0.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns True if a value is greater than or equal to 0. Otherwise, this node returns False. x An input to this operation. This input supports numeric scalar values, clusters, timestamp values, waveforms, and arrays of numbers. For waveforms, the node compares only the y values of this input. Data Typ

Greater or Equal to 0?

Returns True if a value is greater than or equal to 0. Otherwise, this node returns False.

[IMAGE alt='1378' src='IsGreaterOrEqualTo0.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports numeric scalar values, clusters, timestamp values, waveforms, and arrays of numbers.

For waveforms, the node compares only the y values of this input.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### x >= 0?

Boolean result of the operation.

This output assumes the same data type structure as 
 x.

Parent topic:

Comparison Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=greater-than-0.html language=enus -->
## TOPIC 00038: Greater Than 0?

- bundle_id: `daqexpress-api-ref`
- source_path: `greater-than-0.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/greater-than-0.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns True if a value is greater than 0. Otherwise, this node returns False. x An input to this operation. This input supports numeric scalar values, clusters, timestamp values, waveforms, and arrays of numbers. For waveforms, the node compares only the y values of this input. Data Type Changes on

Greater Than 0?

Returns True if a value is greater than 0. Otherwise, this node returns False.

[IMAGE alt='1378' src='IsGreaterThan0.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports numeric scalar values, clusters, timestamp values, waveforms, and arrays of numbers.

For waveforms, the node compares only the y values of this input.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### x > 0?

Boolean result of the operation.

This output assumes the same data type structure as 
 x.

Parent topic:

Comparison Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=hex-digit.html language=enus -->
## TOPIC 00039: Hexadecimal Digit?

- bundle_id: `daqexpress-api-ref`
- source_path: `hex-digit.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/hex-digit.html
- document_id: `daqexpress-api-ref`
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

<!--NI_TOPIC bundle=daqexpress-api-ref path=hexadecimal-string-to-number.html language=enus -->
## TOPIC 00040: Hexadecimal String to Number

- bundle_id: `daqexpress-api-ref`
- source_path: `hexadecimal-string-to-number.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/hexadecimal-string-to-number.html
- document_id: `daqexpress-api-ref`
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

<!--NI_TOPIC bundle=daqexpress-api-ref path=histogram-continuous.html language=enus -->
## TOPIC 00041: Continuous

- bundle_id: `daqexpress-api-ref`
- source_path: `histogram-continuous.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/histogram-continuous.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Finds the continuous histogram of a signal. output representation Representation for the output. sample count Represents the value of each bin as the number of samples in that bin. percent of total Represents the value of each bin as a percentage of the total. Default value: sample count reset A Boo

Continuous

Finds the continuous histogram of a signal.

[IMAGE alt='1378' src='Histogram_(continuous)(Wfm).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### output representation

Representation for the output.

| sample count | Represents the value of each bin as the number of samples in that bin. |
| --- | --- |
| percent of total | Represents the value of each bin as a percentage of the total. |

Default value: sample count

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset

A Boolean to determine initialization of the internal state of the node.

| True | Initializes the internal states to zero. |
| --- | --- |
| False | Initializes the internal states to the final states from the previous call of this node. |

This node automatically initializes the internal state to zero on the first call and runs continuously until this input is True. For a large data sequence consisting of smaller blocks, when this input is True, this node calculates the histogram of the current block only and ignores previous blocks.

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cmsdt.png']

##### signal

Input signal.

This input accepts the following data types:

- Waveform
- 1D array of waveforms
- Double-precision, floating-point number
- 1D array of double-precision, floating-point numbers
- 2D array of double-precision, floating-point numbers

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### number of bins

Number of bins in the histogram.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### maximum

Maximum value to include in the histogram.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### minimum

Minimum value to include in the histogram.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### inclusion

The boundary of each bin to handle.

| lower | Includes the lower boundary. |
| --- | --- |
| upper | Includes the upper boundary. |

Default value: lower

##### Determining the Bin Widths When inclusion Is lower

If inclusion is set to lower, the bin widths are determined according to the following equations.

where

- 
- max is the maximum
- min is the minimum
- m is the number of bins

##### Determining the Bin Widths When inclusion Is upper

If inclusion is set to upper, the bin widths are determined according to the following equations.

where

- 
- max is the maximum
- min is the minimum
- m is the number of bins

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### histogram

The histogram of the input signal.

This input accepts a cluster or a 1D array of clusters.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### x values

An array of the center values of the bins of the histogram.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### histogram h(x)

Discrete histogram of the input signal.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### actual number of bins

Actual number of bins in the histogram.

This output can return a 32-bit signed integer number or a 1D array of 32-bit signed integer numbers.

This output is available only if you wire one of the following data types to signal:

- Waveform
- Array of waveforms
- 1D array of double-precision, floating-point numbers
- 2D array of double-precision, floating-point numbers

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### actual maximum

Actual maximum value in the histogram.

This output can return a double-precision, floating-point number or a 1D array of double-precision, floating-point numbers.

This output is available only if you wire one of the following data types to signal:

- Waveform
- Array of waveforms
- 1D array of double-precision, floating-point numbers
- 2D array of double-precision, floating-point numbers

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### actual minimum

Actual minimum value to include in the histogram.

This output can return a double-precision, floating-point number or a 1D array of double-precision, floating-point numbers.

This output is available only if you wire one of the following data types to signal:

- Waveform
- Array of waveforms
- 1D array of double-precision, floating-point numbers
- 2D array of double-precision, floating-point numbers

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### samples outside

Information about points that do not fall in any bin upon successful execution of the node.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### total

Total number of values in signal that do not fall in any bin upon successful execution.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### below

Number of values in signal below the first bin on the lower boundary.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### above

Number of values in signal above the last bin on the upper boundary.

#### Examples

The following illustration shows the waveform of an input signal.

[IMAGE alt='1378' src='GUID-8118774D-05F6-4D93-8FD1-574E8C3B3449-a5.png']

This example configures the node using the following input values:

- maximum = 6
- minimum = 0
- number of bins = 3

[IMAGE alt='1378' src='GUID-13CE43D4-B39A-4CA4-8831-0CE8B5B73E1A-a5.png']

#### Algorithm for Constructing histogram

The histogram is a frequency count of the number of times that a specified frequency bin occurs in the input sequence. The node constructs histogram as follows.

The following equation calculates the width of the frequency bin Δx.

Δ

x

=

max

−

min

m

Δ

x

=

max

−

min

m

where 
 *max* is the maximum, 
 *min* is the minimum, and m is the number of bins.

The node calculates the center of each frequency bin according to the following equation.

center

[

i

]

=

min

+

0.5

Δ

x

+

i

Δ

x

center

[

i

]

=

min

+

0.5

Δ

x

+

i

Δ

x

The node defines the range of the i<sup>th</sup> frequency bin according to the following definition.

Δ

i

∈

(

center

[

i

]

−

0.5

Δ

x

,

center

[

i

]

+

0.5

Δ

x

)

Δ

i

∈

(

center

[

i

]

−

0.5

Δ

x

,

center

[

i

]

+

0.5

Δ

x

)

for 
 i = 0, 1, 2, ..., 
 m - 1

The node scans the input sequence, calculates the number of samples in each frequency bin from 0 to 
 m - 1, and returns the histogram.

Parent topic:

Histogram

<!--NI_TOPIC bundle=daqexpress-api-ref path=hyperbolic-cotangent.html language=enus -->
## TOPIC 00042: Hyperbolic Cotangent

- bundle_id: `daqexpress-api-ref`
- source_path: `hyperbolic-cotangent.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/hyperbolic-cotangent.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the hyperbolic cotangent in radians of a value you specify(x). x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this input h

Hyperbolic Cotangent

Computes the hyperbolic cotangent in radians of a value you specify(x).

[IMAGE alt='1378' src='HyperbolicCotangent.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### coth

Result of the operation.

This output assumes the same numeric representation as 
 x.

Parent topic:

Hyperbolic Trigonometry Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=in-range-and-coerce.html language=enus -->
## TOPIC 00043: In Range and Coerce

- bundle_id: `daqexpress-api-ref`
- source_path: `in-range-and-coerce.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/in-range-and-coerce.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the input value falls within a range specified by the upper and lower limits and optionally coerces the value to fall within the range. To allow the node to perform coercion, select Elements in the Behavior section of the Item tab. upper limit The upper limit of the range. By defa

In Range and Coerce

Determines whether the input value falls within a range specified by the upper and lower limits and optionally coerces the value to fall within the range.

To allow the node to perform coercion, select 
 Elements in the 
 Behavior section of the 
 **Item** tab.

[IMAGE alt='1378' src='InRangeAndCoerce.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### upper limit

The upper limit of the range.

By default, this node excludes the value of upper limit in the range. You can configure the node to include the value of upper limit in the range by selecting the 
 Include upper limit option in the 
 Behavior section of the 
 Item tab. This option affects only the value of in range?. This node always coerces x to the exact values of upper limit and lower limit, regardless of whether you select this option.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

The value to test in the range and optionally coerce if it does not fall between the upper and lower limits. This input changes to waveform when the data type is a waveform.

This input supports all data types.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### lower limit

The lower limit of the range.

By default, this node includes the value of lower limit in the range. You can configure the node to exclude the value of lower limit in the range by deselecting the 
 Include lower limit option in the 
 Behavior section of the 
 Item tab. This option affects only the value of in range?. This node always coerces x to the exact values of upper limit and lower limit, regardless of whether you select this option.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### in range?

A Boolean value that indicates whether the input value is in range.

| True | x is in range. |
| --- | --- |
| False | x is out of range. This node also returns False if x, upper limit, or lower limit is NaN. |

In 
 Compare Elements mode, the data type structure of in range? matches the data type structure of x, with each scalar replaced by a Boolean value.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### coerced

The coerced or unchanged input value.

##### Comparison Modes and x Value Behavior

If x is within the range set by the upper limit and lower limit or if the node is in 
 Compare Aggregates mode, the value is unchanged. If x is not in range and the node is in 
 Compare Elements mode, the node converts the value to the same value as upper limit or lower limit. If upper limit, x, or lower limit is 
 NaN, coerced is 
 NaN.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

##### Include upper limit

Include the value of upper limit in the range that this node evaluates. This option affects only the value of in range?. The node always coerces x to the exact values of upper limit and lower limit, regardless of whether you select this option.

##### Include lower limit

Include the value of lower limit in the range that this node evaluates. This option affects only the value of in range?. The node always coerces x to the exact values of upper limit and lower limit, regardless of whether you select this option.

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=is-path-and-not-empty.html language=enus -->
## TOPIC 00044: Is Path and Not Empty?

- bundle_id: `daqexpress-api-ref`
- source_path: `is-path-and-not-empty.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/is-path-and-not-empty.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks if the input path is a valid path or an empty path. path Path you want to check. path and not empty? A Boolean that specifies whether or not the input path is empty or <Not A Path>. True The input path is any value other than <Not A Path> or an empty path. False The input path is <Not A Path>

Is Path and Not Empty?

Checks if the input path is a valid path or an empty path.

[IMAGE alt='1378' src='Is_Path_and_Not_Empty.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cpath.png']

##### path

Path you want to check.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### path and not empty?

A Boolean that specifies whether or not the input path is empty or 
<Not A Path>.

| True | The input path is any value other than <Not A Path> or an empty path. |
| --- | --- |
| False | The input path is <Not A Path> or an empty path. |

Parent topic:

Path Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=layouts.html language=enus -->
## TOPIC 00045: Layouts

- bundle_id: `daqexpress-api-ref`
- source_path: `layouts.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/layouts.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Organize the appearance of controls and indicators or display the panel of other VIs. When Should I Use a Tab Control? Tab controls are useful when you have several panel objects that are used together or during a specific phase of operation. For example, you might have a VI that requires the user t

Layouts

Organize the appearance of controls and indicators or display the panel of other VIs.

[IMAGE alt='1378' src='GUID-9D41F51E-FCED-456C-8903-04447CF531FE-a5.png']

#### When Should I Use a Tab Control?

Tab controls are useful when you have several panel objects that are used together or during a specific phase of operation. For example, you might have a VI that requires the user to first configure several settings before a test can start, then allows the user to modify aspects of the test as it progresses, and finally allows the user to display and store only pertinent data.

#### How Do I Use a Panel Container?

Panel containers display the panel of a running VI in the panel of the current VI. To access the panel container on the diagram, you must create a panel container reference. To create a reference, right-click the panel container and select 
 Create reference. Place the panel container reference on the diagram and use the reference with the Panel Container nodes.

<!--NI_TOPIC bundle=daqexpress-api-ref path=less-or-equal-to-0.html language=enus -->
## TOPIC 00046: Less or Equal to 0?

- bundle_id: `daqexpress-api-ref`
- source_path: `less-or-equal-to-0.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/less-or-equal-to-0.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns True if a value is less than or equal to 0. Otherwise, this node returns False. x An input to this operation. This input supports numeric scalar values, clusters, timestamp values, waveforms, and arrays of numbers. For waveforms, the node compares only the y values of this input. Data Type C

Less or Equal to 0?

Returns True if a value is less than or equal to 0. Otherwise, this node returns False.

[IMAGE alt='1378' src='IsLessOrEqualTo0.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports numeric scalar values, clusters, timestamp values, waveforms, and arrays of numbers.

For waveforms, the node compares only the y values of this input.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### x <= 0?

Boolean result of the operation.

This output assumes the same data type structure as 
 x.

Parent topic:

Comparison Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=less-or-equal.html language=enus -->
## TOPIC 00047: Less or Equal?

- bundle_id: `daqexpress-api-ref`
- source_path: `less-or-equal.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/less-or-equal.html
- document_id: `daqexpress-api-ref`
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

<!--NI_TOPIC bundle=daqexpress-api-ref path=less.html language=enus -->
## TOPIC 00048: Less?

- bundle_id: `daqexpress-api-ref`
- source_path: `less.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/less.html
- document_id: `daqexpress-api-ref`
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

<!--NI_TOPIC bundle=daqexpress-api-ref path=match-pattern.html language=enus -->
## TOPIC 00049: Match Pattern

- bundle_id: `daqexpress-api-ref`
- source_path: `match-pattern.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/match-pattern.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Searches for a pattern of characters in a string as specified by a limited set of regular expressions. If this node finds a match, it splits the input string into three substrings: the string that appears before the match, the match itself, and the string that appears after the match. This node perf

Match Pattern

Searches for a pattern of characters in a string as specified by a limited set of regular expressions.

If this node finds a match, it splits the input string into three substrings: the string that appears before the match, the match itself, and the string that appears after the match.

This node performs more quickly than Match Regular Expression but gives you fewer options for matching strings. For example, Match Pattern does not support the parenthesis or vertical bar (|) characters.

[IMAGE alt='1378' src='MatchPattern.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### string

The input string to search.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### regular expression

The pattern for which you want to search in the input string.
 This input is limited to the following regular expression characters: . (period), *, +, ?, [], ^, $, \, \b, \f, \n, \s, \r, \t, and \xx. Furthermore, this input does not support character grouping, alternate pattern matching, backreferences, or non-greedy quantification.

##### Definitions of Special Characters

| Special Character | Description | Examples |
| --- | --- | --- |
| . (period) | Matches any single character except a newline character. Within square brackets, . is literal. | Input String: Welcome to LabVIEW. Regular Expression: t.... Match: to La If you use [z.] as the regular expression, the period is literal and matches either . or z. In this example, [z.] returns . as the match. |
| * | Marks the single preceding character or character class as one that can appear zero or more times in the input. Because an asterisk can mark a pattern as one that appears zero times, regular expressions that include an asterisk can return an empty string if the whole pattern is marked with an asterisk. This quantifier applies to as many characters as possible. | Input String: Hello LabVIEW! Regular Expression: el* Match: ell Expressions such as w* or (welcome)* match an empty string if the node finds no other matches. |
| + | Marks the single preceding character or character class as one that can appear one or more times in the input. This quantifier applies to as many characters as possible. | Input String: Hello LabVIEW! Regular Expression: el+ Match: ell |
| ? | Marks the single preceding character or character class as one that can appear zero or one time in the input. This quantifier applies to as many characters as possible. | Input String: Hello LabVIEW! Regular Expression: el? Match: el |
| [] | Creates a character class, which allows you to match any one of a set of characters that you specify. For example, [abc] matches a, b, or c. This node interprets special characters inside square brackets literally, with the following exceptions: - (dash)—Indicates a range when used between digits, or lowercase or uppercase letters; for example, [0-5], [a-g], or [L-Q]. ~—Matches any character, including non-displayable characters, except for the characters or range of characters in brackets. For example, [~0-9] matches any character other than 0 through 9. ^—Matches any displayable character, including the space character, except the characters or range of characters enclosed in the brackets. For example, [^0-9] matches all displayable characters, including the space character, except 0 through 9. | Input String: version=14.0.1 Regular Expression: [0-9]+\\.[0-9]+\\.[0-9]+ Match: 14.0.1 The expression [0-9] matches any digit. The plus sign matches the previous character class, [0-9], one or more times but as many times as possible. The expression \\. matches a literal . character. The plus sign matches the previous character class, [0-9], one or more times but matches as many times as possible. You can use this regular expression to match a three-part version number. |
| ^ | If ^ is the first character of the specified search string, it anchors the match to the offset in string. The match fails unless the specified search string matches that portion of string that begins with the character at offset. If ^ is not the first character in the regular expression, it is treated as a regular character. | Input String: Hello LabVIEW! Regular Expression: ^[^ ]+ Match: Hello From the beginning of the input string, this regular expression matches as many characters – other than a space character – as possible. You can use this regular expression to isolate the first word, numeral, or other character combination of a string. |
| $ | If $ is the last character of the specified search string, it anchors the match to the last element of string. The match fails unless the specified search string matches up to and including the last character in the string. If $ is not the last character in the regular expression, it is treated as a regular character. | Input String: Hello LabVIEW! Regular Expression: [^ ]+$ Match: LabVIEW! From the end of the input string, this regular expression matches as many characters – other than a space character – as possible. You can use this regular expression to isolate the last word, numeral, or other character combination of a string. |
| \\ | Cancels the interpretation of any special character in this list. For example, \\? matches a question mark, \\. matches a period, and \\\\ matches a backslash. You also can use the following constructions for the following non-displayable characters: \\b—Backspace\\f—Form feed\\n—New line\\s—Space\\r—Carriage return\\t—Tab\\xx—Any character, where xx is the hex code using 0 through 9 and upper case A through F. | Input String: Welcome to the LabVIEW Help! Regular Expression: come\\nto\\tthe\\sLabVIEW\\sHelp\\21 Match: come to the LabVIEW Help! The expression come\\n matches the literal letters followed by a newline character. The expression to\\t matches the literal characters to followed by a tab. The two \\s expressions match the spaces between the and LabVIEW and between LabVIEW and Help!. The expression \\21 matches the exclamation point because 21 is the hexadecimal code for an exclamation point. |

Note

hz+

hz[+]

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### offset

The number of characters into the input string at which this node begins its operation.

The offset of the first character in the input string is 0. If offset is beyond the end of the input string, this node returns an empty string.

Note

16

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### before substring

A string containing all the characters in the input string that occur before the match.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### match substring

First string after the offset that matches the pattern specified by the regular expression.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### after substring

String containing all characters in the input string that follow the match.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### offset past match

The index in the input string of the first character of after substring. If the node does not find a match, this output returns -1.

Note

16

#### Examples

| string | regular expression | offset | match | offset past match | Comments |
| --- | --- | --- | --- | --- | --- |
| cdb | b* | 0 | "" | 0 | The offset input and the offset past match output might be equal when the empty string is a valid match for the regular expression. |
| bbbcd | b* | 0 | bbb | 3 | Notice that offset does not equal offset past match because a longer match than the empty string existed. |

#### What Happens When There Is No Match?

If the node does not find regular expression, match substring is empty, before substring is the entire string, after substring is empty, and offset past match is -1. Match Pattern is compatible with a limited set of regular expressions and does not support character grouping, alternate pattern matching, backreferences, or non-greedy quantification. You can use a specific set of special characters to refine the search.

#### Reducing Performance Burden

Characters in UTF-8 can be multiple bytes so string nodes count the number of characters in a string instead of jumping to a point in memory. Since the length and offset parameters are in units of characters, avoid nesting this node with large strings because that can create exponential functions that carry a higher performance burden.

Parent topic:

String Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=match-regular-expression.html language=enus -->
## TOPIC 00050: Match Regular Expression

- bundle_id: `daqexpress-api-ref`
- source_path: `match-regular-expression.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/match-regular-expression.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Searches for a pattern of characters in a string as specified by a regular expression. If this node finds a match, it splits the string into three substrings and any number of submatches. Resize the node to view additional submatches found in the string. This node does not support null characters in

Match Regular Expression

Searches for a pattern of characters in a string as specified by a regular expression. If this node finds a match, it splits the string into three substrings and any number of submatches. Resize the node to view additional submatches found in the string.

This node does not support null characters in strings. If you include null characters in strings you wire to this node, the node returns an error and may return unexpected results.

This node performs more slowly than Match Pattern but gives you more options for matching strings. For example, Match Regular Expression supports the parenthesis and vertical bar (|) characters.

[IMAGE alt='1378' src='MatchRegularExpression.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### ignore case

Boolean value that determines whether the string search is case sensitive.

| True | The search ignores the letter case of the input. |
| --- | --- |
| False | The search matches the letter case of the input. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### multiline?

A Boolean value that determines whether to treat the text in the input string as a multiple-line string. This affects how the ^ and $ characters handle matches.

| True | ^ matches the beginning of any line in the input string. $ matches the end of any line in the input string. |
| --- | --- |
| False | ^ matches only the beginning of the input string. $ matches only the end of the input string. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### input string

The string that this node searches. This string cannot contain null characters.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### regular expression

The pattern you want to search for in the input string. This string cannot contain null characters. Use Perl Compatible Regular Expressions to refine searches.

##### Definitions of Regular Expressions

Use the following regular expressions to search the input string.

| Regular Expression | Description | Examples |
| --- | --- | --- |
| . (period) | Matches any single character except a newline character. Within square brackets, . is literal. | Input String: Welcome to LabVIEW. Regular Expression: t.... Match: to La If you use [z.] as the regular expression, the period is literal and matches either . or z. In this example, [z.] returns . as the match. |
| * | Marks the single preceding character, character group, or character class as one that can appear zero or more times in the input. Because an asterisk can mark a pattern as one that appears zero times, regular expressions that include an asterisk can return an empty string if the whole pattern is marked with an asterisk. This quantifier applies to as many characters as possible. | Input String: Hello LabVIEW! Regular Expression: el* Match: ell Expressions such as w* or (welcome)* match an empty string if the node finds no other matches. |
| + | Marks the single preceding character, character group, or character class as one that can appear one or more times in the input. This quantifier applies to as many characters as possible. | Input String: Hello LabVIEW! Regular Expression: el+ Match: ell |
| ? | Marks the single preceding character, character group, or character class as one that can appear zero or one time in the input. This quantifier applies to as many characters as possible. When used immediately after a quantifier, ? modifies the quantifier to match as few times as possible. Modifiable quantifiers include *, +, and {}. | Input String: Hello LabVIEW! Regular Expression: el? Match: el |
| Input String: <ul><li>Hello</li><li>LabVIEW</li></ul> Regular Expression: <li>.+?</li> Match: <li>Hello</li> In the second example, if you remove ? from the regular expression, the new match becomes <li>Hello</li><li>LabVIEW</li> because + matches as many characters as possible unless you include ? immediately after +. You can use this regular expression to match any string within <li></li> tags. |  |  |
| {n,N} | Marks the single preceding character, character group, or character class as one that can appear the number of times you specify, where n is the minimum and N is the maximum. You also can specify a single number. If you specify a range, this quantifier matches as many times as possible. | Input String: <ul><li>Hello</li><li>Lab</li><li>VIEW</li><li>!</li></ul> Regular Expression: (<li>.+?</li>){2} Match: <li>Hello</li><li>Lab</li> |
| Input String: <ul><li>Hello</li><li>Lab</li><li>VIEW</li><li>!</li></ul> Regular Expression: (<li>.+?</li>){1,3} Match: <li>Hello</li><li>Lab</li><li>VIEW</li> In the second example, the minimum match limit is one and the maximum is three. Because the regular expression matches as many times as possible within the limit you specify, the regular expression returns three. |  |  |
| [] | Creates a character class, which allows you to match any one of a set of characters that you specify. For example, [abc] matches a, b, or c. You can use - to specify a range of characters. For example, [a-z] matches any single lowercase letter. This node interprets special characters inside square brackets literally, with the exception of ^, -, and \\. | Input string: version=14.0.1 Regular Expression: [0-9]+(\\.[0-9]+)* Match: 14.0.1 The expression [0-9] matches any digit. The plus sign matches the previous character class, [0-9], one or more times but as many times as possible. The parentheses create a character group, which creates a submatch of the . character and all following digits. The expression \\. matches a literal . character. The plus sign matches the previous character class, [0-9], one or more times but matches as many times as possible. The asterisk matches the previous character group, (\\.[0-9]+), zero or more times, so the regular expression still matches integers if there is no . character. You can use this regular expression to match any integer, decimal number, version number, IPv4 address, or other number sequence separated by . characters. |
| () | Creates a character group, which allows you to match an entire set of characters that you specify. A quantifier that immediately follows a character group quantifies the entire group. Parentheses also create submatches where each individual character group returns a submatch. If you nest a character group within another character group, the regular expression creates a submatch for the outer group before the inner group. Expand Match Regular Expression to access submatch outputs. You also can refer back to submatches later in an expression using backreferences. Refer to the Backreferences section for more information about using backreferences in regular expressions. | Input String: Hello LabVIEW! Regular Expression: (el.)..(L..) Match: ello Lab Submatch 1: ell Submatch 2: Lab |
| Input String: Hello LabVIEW! Regular Expression: (.(el.).).(L..) Match: Hello Lab Submatch 1: Hello Submatch 2: ell Submatch 3: Lab |  |  |
| \| | Separates alternate possible matches. This character is useful when you want to match any of a number of character groups. A regular expression that contains \| returns the first match that the node finds in the input string regardless of the order of your possible matches. For example, both regular expressions dog\|cat and cat\|dog match dog in the dog chased the cat. | Input String: value=FALSE total=12.34 token=TRUE Regular Expression: (value\|token)=(TRUE\|FALSE) Match: value=FALSE Submatch 1: value Submatch 2: FALSE The regular expression returns the first possible match in the input string. If token=TRUE appeared before value=FALSE in the input string, the regular expression would match token=TRUE instead. |
| ^ | Anchors a match to the beginning of a string when used as the first character of a pattern. If you set the multiline? input to True on this node, ^ matches the beginning of any line within the string using the line endings of the current platform. You also can match any character not in a given character class by adding ^ to the beginning of a character class. For example, [^0-9] matches any character that is not a digit. [^a-zA-Z0-9] matches any character that is not a lowercase or uppercase letter and also not a digit. | Input String: Hello LabVIEW! Regular Expression: ^[^ ]+ Match: Hello The regular expression matches as many characters as possible – other than a space character – from the beginning of the input string. You can use this regular expression to isolate the first word, numeral, or other character combination of a string. |
| Input String: Hello LabVIEW Regular Expression: ^LabVIEW Match: LabVIEW The regular expression matches LabVIEW only if you set multiline? to True. |  |  |
| $ | Anchors a match at the end of a string when used as the last character of a pattern. If you set the multiline? input to True, $ matches the end of any line within the string using the line endings of the current platform. Referenced a parenthesized item with $n, where n is the index of the parenthesized item. Explicitly insert dollar signs ($) by prefixing them with a backslash (\\). For example, \\$5 represents $5 and $5 represents the 5th parenthesized item. | Input String: Hello LabVIEW! Regular Expression: [^ ]+$ Match: LabVIEW! The regular expression matches as many characters as possible – other than a space character – from the end of the input string. You can use this regular expression to isolate the last word, numeral, or other character combination of a string. |
| Input String: Hello LabVIEW Regular Expression: Hello$ Match: Hello The regular expression matches Hello only if you set multiline? to True. |  |  |
| \\ | Cancels the special meaning of any special character in this list that immediately follows the backslash and instead matches the literal character. The following escaped expressions have special meanings: \\b—Represents a word boundary. A word boundary is a character that is not a word character adjacent to a character that is a word character and vice versa. A word character is an alphanumeric character or an underscore (_). For example, \\bhat matches hat in hatchet but not in that. hat\\b matches hat in that but not in hatchet. \\bhat\\b matches hat in hat but not in that or hatchet. \\c—Matches any control or non-printing character; includes any code point in the character set that does not represent a written symbol \\w—Matches any word character; equivalent to [a-zA-Z0-9_] \\W—Matches any non-word character; equivalent to [^a-zA-Z0-9_] \\d—Matches any digit character; equivalent to [0-9] \\D—Matches any non-digit character; equivalent to [^0-9] \\N—Matches a previous submatch within the same regular expression where N is a digit; refer to the Backreferences section for more information about using \\N \\s—Matches any whitespace character; includes space, newline, tab, carriage return, and so on \\S—Matches any non-whitespace character \\n—Matches a newline character \\t—Matches a tab character \\r—Matches a carriage return character \\f—Matches a formfeed character \\031—Matches an octal character (31 octal in this case) \\x3F—Matches a hexadecimal character (3F hexadecimal in this case) | Input String: total=$12.34 Regular Expression: \\$\\d+(\\.\\d{2})? Match: $12.34 The expression \\$ matches a literal dollar sign because the backslash cancels the special meaning. The expression \\d+ matches as many digits as possible and must match at least one digit. The expression (\\.\\d{2})? matches . and two digits, but ? makes this portion of the regular expression optional to match. You can use this regular expression to match dollar values that use a . character as a decimal separator. Locales that use a different character as a decimal separator must adapt the regular expression. |
| Input String: NEWtoken=FALSE token=TRUE checkFile=TRUE total=12.34 Regular Expression: \\btoken=\\w+\\s\\b\\S* Match: token=TRUE checkFile=TRUE The regular expression does not match token=FALSE in NEWtoken=FALSE because \\b makes the regular expression match token= only at the beginning of a word. The expression \\w+ matches as many word characters as possible and must match at least one. In this example, \\w+ matches TRUE. The expression \\s matches a space character. The expression \\b\\S* matches all non-whitespace characters that begin a word until the function finds another whitespace character. In this example, \\b\\S* matches checkFile=TRUE. |  |  |
| Input String: Welcome to LabVIEW! Regular Expression: come\\n\\S*\\t\\w*\\x21 Match: come to LabVIEW! The expression come\\n matches the literal letters followed by a newline character. The expression \\S* matches as many non-whitespace characters as possible, which is the word to in this case. The expression \\t matches the tab in between to and LabVIEW!. The expression \\w* matches as many word characters as possible, which is LabVIEW in this case. The expression \\x21 matches the exclamation point because 21 is the hexadecimal code for an exclamation point. |  |  |

Tip

^

$

^LabVIEW$

LabVIEW

LabVIEW

LabVIEW!

Hello LabVIEW

##### Specifying Backreferences in the Search String

Use backreferences to refer to previous submatches within the same regular expression. You can use backreferences to create a submatch using a character group in one part of an expression and then match that exact submatch in a later part of the expression.

To specify a backreference, use 
 \1 to refer to the first submatch, 
 \2 to refer to the second, and so on. For example, consider the following regular expression:

(["*$])(\w+)\1\2\1

The first character group contains a character class that matches ", *, or $. The second character group matches one or more word characters. The first backreference, 
 \1, matches the same submatch as the first character group, 
 (["*$]). The second backreference, 
 \2, matches the same submatch as the second character group, 
 (\w+). The third backreference, 
 \1, is identical to the first backreference and matches the same submatch as the first character group.

This example matches strings such as 
 "foo"foo", 
 *bar*bar*, and 
 $baz$baz$, but does not match strings such as 
 "foo$foo" or 
 "foo*bar".

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### offset

The number of characters into the input string at which this node starts searching.

The offset of the first character in the input string is 0. If offset is beyond the end of the input string, this node returns an empty string.

Note

16

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### before match

A string that contains all the characters in input string that occur before the match.

If the node does not find a match, this string contains all of the characters in the input string.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### whole match

All the characters that match the expression entered in regular expression.

submatch

whole match

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### after match

All the characters after the match.

after match

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### offset past match

Index of the first character after the last match the node finds in the input string. If the node does not find a match, offset past match returns -1.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### submatch

Portion of the whole match you capture using character grouping in the regular expression. Capture a submatch by placing parentheses around the portion of a regular expression you want the node to return as a submatch.

For example, the regular expression 
 (el.)..(L..) returns two submatches in the input string 
 Hello LabVIEW!. Each submatch corresponds to a character group in the order that the character group appears in the regular expression. In this example, submatch 1 is 
 ell and submatch 2 is 
 Lab.

##### Submatch Behavior with Nested Character Groups

If you nest a character group within another character group, the regular expression creates a submatch for the outer group before the inner group. For example, the regular expression 
 (.(el.).).(L..) returns three submatches in the input 
 Hello LabVIEW!: 
 Hello, 
 ell, and 
 Lab. In this example, submatch 1 is 
 Hello because the regular expression matches the outer character group before the inner group.

#### Repeated Grouped Expressions and Stack Overflow

| Grouped Regular Expression | Rewritten Expression |
| --- | --- |
| (.\|\\s)*A | (?s).*A or [^A]*A |
| (a*)* | a* |

#### What Happens When There Is No Match?

If the node does not find a match, whole match and after match contain empty strings, before match contains the entire input string, offset past match returns -1, and all submatch outputs return empty strings. Place any substrings you want to search for in parentheses. This node returns any substring expressions it finds in submatch 1..n.

#### Reducing Performance Burden

Characters in UTF-8 can be multiple bytes so string nodes count the number of characters in a string instead of jumping to a point in memory. Since the length and offset parameters are in units of characters, avoid nesting this node with large strings because that can create exponential functions that carry a higher performance burden.

Parent topic:

String Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=max-and-min.html language=enus -->
## TOPIC 00051: Max and Min

- bundle_id: `daqexpress-api-ref`
- source_path: `max-and-min.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/max-and-min.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Compares two values and returns the maximum and minimum values. x The value to compare. x must be of the same data type as y. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time. y T

Max and Min

Compares two values and returns the maximum and minimum values.

[IMAGE alt='1378' src='MaxAndMin.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

The value to compare.

x

y

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### y

The value to compare.

This input also supports waveforms.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### max

The larger value.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### min

The smaller value.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

#### Examples

| Parameters | Compare Elements | Comments | Compare Aggregates | Comments |
| --- | --- | --- | --- | --- |
| First input array (x) | [3,2,3,4] |  | [3,2,3,4] |  |
| Second input array (y) | [2,3,4,5] |  | [2,3,4,5] |  |
| Maximum (max) | [3,3,4,5] | The node returns an array of the maximum elements from the two input arrays. | [3,2,3,4] | Because the first elements of the two input arrays are not equal, and because 3>2, the node stops and returns [3,2,3,4] as the maximum array. |
| Minimum (min) | [2,2,3,4] | The node returns an array of the minimum elements from the two input arrays. | [2,3,4,5] | Because the first elements of the two input arrays are not equal, and because 2<3, the node stops and returns [2,3,4,5] as the minimum array. |

#### Timestamps

This node accepts timestamp values if all inputs are timestamp values. If the inputs are timestamp values, the function returns the later time at the top and the earlier time at the bottom. You can change the comparison mode of this node.

#### Behavior When Comparing NaN Elements

In Compare Elements mode, when one or both inputs are NaN (Not-a-Number), this function produces the following results:

- Both inputs are NaN-Both max and min return NaN
- Only one input is NaN-Both max and min return the non-NaN value
- Inputs are arrays—The node evaluates each pair of elements according to the previous rules

In Compare Aggregates mode, when one or both inputs are NaN (Not-a-Number), this function produces the following results:

- Both inputs are NaN-Both max and min return NaN
- Only one input is NaN- max returns x and min returns y
- Inputs are arrays—If the node encounters a NaN element in either input array, max returns x and min returns y

#### Behavior with Array and Cluster
 Inputs

When using Max and Min to compare arrays and clusters, you can
 select a comparison mode. Note that Max and Min produces a different
 type of output than other Comparison nodes in each of the two comparison modes. In Compare
 Elements mode,Max and Min returns an array or cluster of the maximum
 elements and minimum elements. In Compare Aggregates mode,Max and Min
 returns the maximum and minimum array and cluster.

Parent topic:

Numeric Nodes

Related information:

- Comparison Modes for Array and Cluster Data

<!--NI_TOPIC bundle=daqexpress-api-ref path=merge-errors.html language=enus -->
## TOPIC 00052: Retain First Error

- bundle_id: `daqexpress-api-ref`
- source_path: `merge-errors.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/merge-errors.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks each error input in top-down order and returns the first error encountered. This node looks for errors from top to bottom beginning with the first error in parameter and reports the first error found. If the node finds no errors, it looks for warnings and returns the first warning found. If t

Retain First Error

Checks each error input in top-down order and returns the first error encountered.

This node looks for errors from top to bottom beginning with the first 
 error in parameter and reports the first error found. If the node finds no errors, it looks for warnings and returns the first warning found. If the node finds no warnings, it returns no error.

[IMAGE alt='1378' src='MergeErrors.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

An error cluster that you use to check for errors or warnings.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

The first error found in an 
error in parameter. If this node finds no errors, 
error out contains the first warning found, if any.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Error Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=noise-generator-gaussian.html language=enus -->
## TOPIC 00053: Gaussian

- bundle_id: `daqexpress-api-ref`
- source_path: `noise-generator-gaussian.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/noise-generator-gaussian.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates a signal containing a Gaussian white noise wave. offset DC offset of the signal. Default value: 0 reset A Boolean that controls the reseeding of the noise sample generator after the first call of the node. True Accepts a new state or new seed value and begins producing noise samples based

Gaussian

Generates a signal containing a Gaussian white noise wave.

[IMAGE alt='1378' src='Gaussian_White_Noise_Waveform.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### offset

DC offset of the signal.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset

A Boolean that controls the reseeding of the noise sample generator after the first call of the node.

| True | Accepts a new state or new seed value and begins producing noise samples based on the new state or new seed value. |
| --- | --- |
| False | Maintains the initial internal seed state and resumes producing noise samples as a continuation of the previous noise sequence. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### standard deviation

Standard deviation of the noise you generate.

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### state in

Initial internal state of the noise generator.

This input must be passed from the state out output of another call to this node.

This node uses state in as the initial internal seed state of the noise generator if reset is True or if this is the first call of the node. If state in contains invalid values, this nodes uses seed as the initial internal seed state of the noise generator.

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### random generator state

Initial internal seed state of the random noise generator.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### x seed

Internal x seed.

x seed

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### y seed

Internal y seed.

y seed

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### z seed

Internal z seed.

z seed

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### Gauss state

Internal Gauss state.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### normal preset

Normal preset state for internal use.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### normal preset value

Normal preset value for internal use.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### seed

Number that this node uses to initialize the noise generator.

This node initializes the noise generator using seed when this node meets both of the following conditions:

- This is the first call of this node or reset is True.
- state in is unwired or contains invalid values.

| seed is greater than 0 | Generates noise samples based on the seed value. |
| --- | --- |
| seed is less than or equal to 0 | For the first call, this node generates a random seed value and produces noise samples based on that seed value. For subsequent calls to the node, if seed remains less than or equal to 0, the node maintains the initial internal seed state and produces noise samples as a continuation of the initial noise sequence. |

Default value: -1

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### sample rate

Sample rate in samples per second.

This input is available only if you configure this node to return a waveform.

Default value: 1000

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples

Number of samples in the signal.

samples must be greater than 0. Otherwise, this node returns an error.

This input is available when you configure this node to return a waveform or an array of double-precision, floating-point numbers.

Default value: 1000

[IMAGE alt='datatype_icon' src='/assets/img/ctimestamp.png']

##### t0

Timestamp of the output signal.

This input is available only if you configure this node to return a waveform.

[IMAGE alt='datatype_icon' src='/assets/img/imsdt.png']

##### Gaussian white noise

Gaussian-distributed, pseudorandom pattern.

This output can return the following data types:

- Waveform
- Double-precision, floating-point number
- 1D array of double-precision, floating-point numbers

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### state out

Final internal seed state of the noise generator.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### random generator state

Final internal seed state of the random noise generator.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### x seed

Internal x seed.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### y seed

Internal y seed.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### z seed

Internal z seed.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### Gauss state

Internal Gauss state.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### normal preset

Normal preset state for internal use.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### normal preset value

Normal preset value for internal use.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Algorithm for Generating the Gaussian White Noise

This node generates the Gaussian-distributed pseudorandom sequence using a modified version of the Box-Muller method to transform uniformly distributed random numbers into Gaussian-distributed random numbers. This node generates the uniform pseudorandom numbers using the Wichmann-Hill generator. Given that the probability density function, f(x), of the Gaussian-distributed Gaussian noise pattern is

f

(

x

)

=

1

s

2

π

e

(

(

−

1

2

)

(

x

s

)

2

)

f

(

x

)

=

1

s

2

π

e

(

(

−

1

2

)

(

x

s

)

2

)

where s is the absolute value of standard deviation. You can compute the expected values,

E

{

⋅

}

E

(

x

)

=

∫

−

∞

∞

x

(

f

(

x

)

)

d

x

E

(

x

)

=

∫

−

∞

∞

x

(

f

(

x

)

)

d

x

The following equations define the expected mean value

μ

σ

μ

=

E

{

x

}

=

0

μ

=

E

{

x

}

=

0

σ

=

[

E

{

(

x

−

μ

)

2

}

]

1

/

2

=

s

σ

=

[

E

{

(

x

−

μ

)

2

}

]

1

/

2

=

s

The pseudorandom sequence produces approximately 6.95 * 10<sup>12</sup> samples before the pattern repeats itself. The probability density function (PDF) of the pseudorandom sequence approximates a Gaussian PDF with peak values of at least 6

σ

#### Application of the Gaussian White Noise

Gaussian white noise provides a realistic simulation of some real-world situations. Because of its independent statistical characteristics, Gaussian white noise also often acts as the source of other random number generators. The additive white Gaussian noise (AWGN) channel model is widely used in communications.

Parent topic:

Noise Generator

<!--NI_TOPIC bundle=daqexpress-api-ref path=number-to-boolean-array.html language=enus -->
## TOPIC 00054: Number to Boolean Array

- bundle_id: `daqexpress-api-ref`
- source_path: `number-to-boolean-array.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/number-to-boolean-array.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts an integer to a Boolean array. This node returns an array of 8, 16, 32, or 64 elements, depending on the number of bits in the integer input. The 0th element of the array corresponds to the least significant bit of the two's complement representation of the integer. number A number to conve

Number to Boolean Array

Converts an integer to a Boolean array.
 This node returns an array of 8, 16, 32, or 64 elements, depending on the number of bits in the integer input. The 0th element of the array corresponds to the least significant bit of the two's complement representation of the integer.

[IMAGE alt='1378' src='NumberToBooleanArray.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### number

A number to convert into a Boolean array.

[IMAGE alt='datatype_icon' src='/assets/img/i1dbool.png']

##### Boolean array

8, 16, 32, or 64 elements depending on the integer of number.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=number-to-decimal-string.html language=enus -->
## TOPIC 00055: Number to Decimal String

- bundle_id: `daqexpress-api-ref`
- source_path: `number-to-decimal-string.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/number-to-decimal-string.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a numeric value to a string that shows the number's decimal format. number A number to be converted into a string. This input can also be any data type that contains only numbers, such as an array of numbers or a cluster of numbers. width A number specifying how many characters to use to ex

Number to Decimal String

Converts a numeric value to a string that shows the number's decimal format.

[IMAGE alt='1378' src='NumberToDecimalString.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### number

A number to be converted into a string.

This input can also be any data type that contains only numbers, such as an array of numbers or a cluster of numbers.

[IMAGE alt='datatype_icon' src='/assets/img/ci16.png']

##### width

A number specifying how many characters to use to express number as a string.

If width is less than the number of characters required, this node uses exactly as many characters as needed. If width is greater than the number of characters required, this node adds a space on the left side of the output string for each additional character.

Default value: No value — Exactly as many characters as are needed to represent the number, with no extra padding.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### decimal integer string

The decimal string that represents number.

#### Examples

number

width

decimal integer string

decimal integer string

| number | width | decimal integer string | Comments |
| --- | --- | --- | --- |
| 4.6 | 2 | _5 | Floating-point and fixed-point numbers are rounded to integers. |
| 3.0 | 4 | _ _ _3 | If width is larger than necessary, spaces are added on the left. |
| -311 | 3 | -311 | If width is smaller than necessary, decimal integer string is as large as necessary. |

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=number-to-exponential-string.html language=enus -->
## TOPIC 00056: Number to Exponential String

- bundle_id: `daqexpress-api-ref`
- source_path: `number-to-exponential-string.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/number-to-exponential-string.html
- document_id: `daqexpress-api-ref`
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

<!--NI_TOPIC bundle=daqexpress-api-ref path=number-to-octal-string.html language=enus -->
## TOPIC 00057: Number to Octal String

- bundle_id: `daqexpress-api-ref`
- source_path: `number-to-octal-string.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/number-to-octal-string.html
- document_id: `daqexpress-api-ref`
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

<!--NI_TOPIC bundle=daqexpress-api-ref path=path-to-string.html language=enus -->
## TOPIC 00058: Path to String

- bundle_id: `daqexpress-api-ref`
- source_path: `path-to-string.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/path-to-string.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a path into the string data type. path The path you want to convert to a string. This input can also be any data type that contains only paths, such as an array of paths or a cluster of paths. If path is <Not A Path>, the node returns <Not A Path> as the text of string. string A text repres

Path to String

Converts a path into the string data type.

[IMAGE alt='1378' src='PathToString.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cpath.png']

##### path

The path you want to convert to a string.

This input can also be any data type that contains only paths, such as an array of paths or a cluster of paths.

If 
 path is 
 <Not A Path>, the node returns 
 <Not A Path> as the text of string.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### string

A text representation of 
path.

string

path

path

string

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=pattern-generator-multimode-function.html language=enus -->
## TOPIC 00059: Pattern Generator

- bundle_id: `daqexpress-api-ref`
- source_path: `pattern-generator-multimode-function.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/pattern-generator-multimode-function.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates a signal containing a specific pattern.

Pattern Generator

Generates a signal containing a specific pattern.

Signal Processing Nodes

Ramp Pattern by Increment

Generates a signal containing a ramp pattern with a specific interval between samples.

Ramp Pattern by Samples

Generates a signal containing a ramp pattern of samples.

Parent topic:

Signal Processing Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=pid-p.html language=enus -->
## TOPIC 00060: P

- bundle_id: `daqexpress-api-ref`
- source_path: `pid-p.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/pid-p.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implements a P controller. feedforward input Value of the feedforward control. This input accepts an array of double-precision, floating-point numbers if setpoint is an array. manual control Settings for the manual control mode. This input accepts an array of clusters if setpoint is an array. manual

P

Implements a P controller.

[IMAGE alt='1378' src='P_Continuous_Academic_(DBL).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### feedforward input

Value of the feedforward control.

This input accepts an array of double-precision, floating-point numbers if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### manual control

Settings for the manual control mode.

This input accepts an array of clusters if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### manual

A Boolean that specifies whether to use the manual control mode.

| True | Uses the manual control mode. |
| --- | --- |
| False | Uses the automatic control mode. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### manual input

Value of the control output when you use the manual control mode.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset

A Boolean that specifies whether to reset the internal parameters, such as the integrated error, of the controller.

| True | Resets the internal parameters. |
| --- | --- |
| False | Does not reset the internal parameters. |

Set reset to True if your application must stop and restart the control loop without restarting the entire application.

This input accepts an array of Booleans if setpoint is an array.

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### setpoint

Setpoint value, or desired value, of the process variable.

This input accepts a double-precision, floating-point number or an array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### process variable

Measured value of the process variable.

This input accepts an array of double-precision, floating-point numbers if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### proportional gain

Proportional gain of the controller.

This input accepts a double-precision, floating-point number or an array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### output range

Range for the control output value.

If the control output value is outside output range, this node coerces the value to fall within the range and returns the coerced value as the control output value.

This input accepts an array of clusters if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### output high

Maximum control output value.

Default value: Infinity

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### output low

Minimum control output value.

Default value: -Infinity

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Loop-cycle time, or interval in seconds, at which this node is called.

dt

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### proportional weighting [beta]

Relative emphasis of setpoint tracking to disturbance rejection.

The valid value range is [0, 1]. Use the default value for most applications.

This input accepts an array of double-precision, floating-point numbers if setpoint is an array.

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### output

Control output of the PID algorithm that is applied to the controlled process.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### error

Difference between the setpoint and the process variable.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### actions

Values of the proportional action, the integral action, and the derivative action in the PID algorithm.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### proportional

Value of the proportional action.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### integral

Value of the integral action.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### derivative

Value of the derivative action.

#### Algorithm Definition

The following transfer function represents a P controller:

C

(

s

)

=

K

p

C

(

s

)

=

K

p

where K<sub>p</sub> is the proportional gain.

Parent topic:

PID

<!--NI_TOPIC bundle=daqexpress-api-ref path=pid-pd-parallel.html language=enus -->
## TOPIC 00061: Parallel

- bundle_id: `daqexpress-api-ref`
- source_path: `pid-pd-parallel.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/pid-pd-parallel.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implements a PD controller in the Parallel form. feedforward input Value of the feedforward control. This input accepts an array of double-precision, floating-point numbers if setpoint is an array. manual control Settings for the manual control mode. This input accepts an array of clusters if setpoi

Parallel

Implements a PD controller in the Parallel form.

[IMAGE alt='1378' src='PD_Continuous_Parallel_(DBL).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### feedforward input

Value of the feedforward control.

This input accepts an array of double-precision, floating-point numbers if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### manual control

Settings for the manual control mode.

This input accepts an array of clusters if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### manual

A Boolean that specifies whether to use the manual control mode.

| True | Uses the manual control mode. |
| --- | --- |
| False | Uses the automatic control mode. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### manual input

Value of the control output when you use the manual control mode.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset

A Boolean that specifies whether to reset the internal parameters, such as the integrated error, of the controller.

| True | Resets the internal parameters. |
| --- | --- |
| False | Does not reset the internal parameters. |

Set reset to True if your application must stop and restart the control loop without restarting the entire application.

This input accepts an array of Booleans if setpoint is an array.

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### setpoint

Setpoint value, or desired value, of the process variable.

This input accepts a double-precision, floating-point number or an array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### process variable

Measured value of the process variable.

This input accepts an array of double-precision, floating-point numbers if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### PD gains

Proportional gain and derivative gain parameters of the controller.

This input accepts a cluster or an array of clusters.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### proportional

Proportional gain of the controller.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### derivative

Derivative gain of the controller, in seconds.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### filter coefficient [a]

Derivative lowpass filter coefficient of the controller.

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### output range

Range for the control output value.

If the control output value is outside output range, this node coerces the value to fall within the range and returns the coerced value as the control output value.

This input accepts an array of clusters if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### output high

Maximum control output value.

Default value: Infinity

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### output low

Minimum control output value.

Default value: -Infinity

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Loop-cycle time, or interval in seconds, at which this node is called.

dt

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### setpoint weighting

Corrections to apply to the error values of the controller.

setpoint weighting

This input accepts an array of clusters if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### proportional weighting [beta]

Relative emphasis of setpoint tracking to disturbance rejection.

The valid value range is [0, 1]. Use the default value for most applications.

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### derivative weighting [gamma]

An amount by which to weight the error applied to the derivative action.

The valid value range is [0, 1]. Use the default value to avoid the derivative kick.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### output

Control output of the PID algorithm that is applied to the controlled process.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### error

Difference between the setpoint and the process variable.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### actions

Values of the proportional action, the integral action, and the derivative action in the PID algorithm.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### proportional

Value of the proportional action.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### integral

Value of the integral action.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### derivative

Value of the derivative action.

#### Algorithm Definition

The following transfer function represents a PD controller in the Parallel form:

C

p

(

s

)

=

K

p

′

+

K

d

′

s

α

p

K

d

′

s

+

1

C

p

(

s

)

=

K

p

′

+

K

d

′

s

α

p

K

d

′

s

+

1

where

K

p

′

K

d

′

α

p

Parent topic:

PID

<!--NI_TOPIC bundle=daqexpress-api-ref path=pid-pi-academic.html language=enus -->
## TOPIC 00062: Academic

- bundle_id: `daqexpress-api-ref`
- source_path: `pid-pi-academic.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/pid-pi-academic.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implements a PI controller in the Academic form. feedforward input Value of the feedforward control. This input accepts an array of double-precision, floating-point numbers if setpoint is an array. manual control Settings for the manual control mode. This input accepts an array of clusters if setpoi

Academic

Implements a PI controller in the Academic form.

[IMAGE alt='1378' src='PI_Continuous_Academic_(DBL).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### feedforward input

Value of the feedforward control.

This input accepts an array of double-precision, floating-point numbers if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### manual control

Settings for the manual control mode.

This input accepts an array of clusters if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### manual

A Boolean that specifies whether to use the manual control mode.

| True | Uses the manual control mode. |
| --- | --- |
| False | Uses the automatic control mode. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### manual input

Value of the control output when you use the manual control mode.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset

A Boolean that specifies whether to reset the internal parameters, such as the integrated error, of the controller.

| True | Resets the internal parameters. |
| --- | --- |
| False | Does not reset the internal parameters. |

Set reset to True if your application must stop and restart the control loop without restarting the entire application.

This input accepts an array of Booleans if setpoint is an array.

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### setpoint

Setpoint value, or desired value, of the process variable.

This input accepts a double-precision, floating-point number or an array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### process variable

Measured value of the process variable.

This input accepts an array of double-precision, floating-point numbers if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### PI gains

Proportional gain and integral gain parameters of the controller.

This input accepts a cluster or an array of clusters.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### proportional

Proportional gain of the controller.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### integral

Integral time constant of the controller, in seconds.

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### output range

Range for the control output value.

If the control output value is outside output range, this node coerces the value to fall within the range and returns the coerced value as the control output value. This node implements integrator anti-windup when the control output is saturated at the specified minimum or maximum value.

This input accepts an array of clusters if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### output high

Maximum control output value.

Default value: Infinity

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### output low

Minimum control output value.

Default value: -Infinity

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Loop-cycle time, or interval in seconds, at which this node is called.

dt

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### proportional weighting [beta]

Relative emphasis of setpoint tracking to disturbance rejection.

The valid value range is [0, 1]. Use the default value for most applications.

This input accepts an array of double-precision, floating-point numbers if setpoint is an array.

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### output

Control output of the PID algorithm that is applied to the controlled process.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### error

Difference between the setpoint and the process variable.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### actions

Values of the proportional action, the integral action, and the derivative action in the PID algorithm.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### proportional

Value of the proportional action.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### integral

Value of the integral action.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### derivative

Value of the derivative action.

#### Algorithm Definition

The following transfer function represents a PI controller in the Academic form:

C

i

(

s

)

=

K

c

(

1

+

1

T

i

s

)

C

i

(

s

)

=

K

c

(

1

+

1

T

i

s

)

where K<sub>c</sub> is the proportional gain and T<sub>i</sub> is the integral time constant.

Parent topic:

PID

<!--NI_TOPIC bundle=daqexpress-api-ref path=pid-pi-parallel.html language=enus -->
## TOPIC 00063: Parallel

- bundle_id: `daqexpress-api-ref`
- source_path: `pid-pi-parallel.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/pid-pi-parallel.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implements a PI controller in the Parallel form. feedforward input Value of the feedforward control. This input accepts an array of double-precision, floating-point numbers if setpoint is an array. manual control Settings for the manual control mode. This input accepts an array of clusters if setpoi

Parallel

Implements a PI controller in the Parallel form.

[IMAGE alt='1378' src='PI_Continuous_Parallel_(DBL).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### feedforward input

Value of the feedforward control.

This input accepts an array of double-precision, floating-point numbers if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### manual control

Settings for the manual control mode.

This input accepts an array of clusters if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### manual

A Boolean that specifies whether to use the manual control mode.

| True | Uses the manual control mode. |
| --- | --- |
| False | Uses the automatic control mode. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### manual input

Value of the control output when you use the manual control mode.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset

A Boolean that specifies whether to reset the internal parameters, such as the integrated error, of the controller.

| True | Resets the internal parameters. |
| --- | --- |
| False | Does not reset the internal parameters. |

Set reset to True if your application must stop and restart the control loop without restarting the entire application.

This input accepts an array of Booleans if setpoint is an array.

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### setpoint

Setpoint value, or desired value, of the process variable.

This input accepts a double-precision, floating-point number or an array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### process variable

Measured value of the process variable.

This input accepts an array of double-precision, floating-point numbers if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### PI gains

Proportional gain and integral gain parameters of the controller.

This input accepts a cluster or an array of clusters.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### proportional

Proportional gain of the controller.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### integral

Integral gain of the controller, in Hz.

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### output range

Range for the control output value.

If the control output value is outside output range, this node coerces the value to fall within the range and returns the coerced value as the control output value. This node implements integrator anti-windup when the control output is saturated at the specified minimum or maximum value.

This input accepts an array of clusters if setpoint is an array.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### output high

Maximum control output value.

Default value: Infinity

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### output low

Minimum control output value.

Default value: -Infinity

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Loop-cycle time, or interval in seconds, at which this node is called.

dt

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### proportional weighting [beta]

Relative emphasis of setpoint tracking to disturbance rejection.

The valid value range is [0, 1]. Use the default value for most applications.

This input accepts an array of double-precision, floating-point numbers if setpoint is an array.

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### output

Control output of the PID algorithm that is applied to the controlled process.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### error

Difference between the setpoint and the process variable.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### actions

Values of the proportional action, the integral action, and the derivative action in the PID algorithm.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### proportional

Value of the proportional action.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### integral

Value of the integral action.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### derivative

Value of the derivative action.

#### Algorithm Definition

The following transfer function represents a PI controller in the Parallel form:

C

p

(

s

)

=

K

p

′

+

K

i

′

s

C

p

(

s

)

=

K

p

′

+

K

i

′

s

where

K

p

′

K

i

′

Parent topic:

PID

<!--NI_TOPIC bundle=daqexpress-api-ref path=positive-infinity.html language=enus -->
## TOPIC 00064: Positive Infinity

- bundle_id: `daqexpress-api-ref`
- source_path: `positive-infinity.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/positive-infinity.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the value infinity.

Positive Infinity

Represents the value infinity.

[IMAGE alt='1378' src='Literal.Numeric.Positive_Infinity.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=daqexpress-api-ref path=programming-flow-nodes.html language=enus -->
## TOPIC 00065: Program Flow Nodes

- bundle_id: `daqexpress-api-ref`
- source_path: `programming-flow-nodes.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/programming-flow-nodes.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`

Program Flow Nodes

Call Chain

Returns an array of every VI that calls this node, from the current VI to the top-level VI.

Case Structure

Contains one or more subdiagrams, or cases, exactly one of which executes when the structure executes.

Disable Structure

Contains one or more subdiagrams, or cases, of which only the enabled subdiagram executes.

Elapsed Timer

Indicates the amount of time that has elapsed since the first call of the node or the most recent reset of the node.

Sequence Structure

Consists of one or more subdiagrams, or frames, that execute sequentially.

First Call?

Indicates whether the diagram or subdiagram containing this node is running for the first time since the top-level caller began execution.

For Loop

n

Select

Returns one of two specified values depending on a Boolean value.

System Exec

Executes or launches other Windows-based applications, command-line applications, or batch files.

Timer Count

Returns the value of the timer.

Wait

Waits a specified amount of time.

Wait Until Next Multiple

Waits until the value of the operating system's timer becomes a multiple of a specified amount of time. Use this node to synchronize activities.

While Loop

Repeats the code on its subdiagram until a specific condition occurs.

<!--NI_TOPIC bundle=daqexpress-api-ref path=pulse-time-and-transition-measurements-pulse.html language=enus -->
## TOPIC 00066: Pulse

- bundle_id: `daqexpress-api-ref`
- source_path: `pulse-time-and-transition-measurements-pulse.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/pulse-time-and-transition-measurements-pulse.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns various measurements of a specific pulse in a periodic waveform or an array of periodic waveforms, such as the period, pulse duration, and duty cycle. signal The input signal. This input can be a waveform or an array of waveforms. polarity Value that specifies whether this node measures high

Pulse

Returns various measurements of a specific pulse in a periodic waveform or an array of periodic waveforms, such as the period, pulse duration, and duty cycle.

[IMAGE alt='1378' src='Pulse_Measurements_1_chan.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cmsdt.png']

##### signal

The input signal.

This input can be a waveform or an array of waveforms.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### polarity

Value that specifies whether this node measures high or low pulses.

| low pulse | 0 | Measures low pulses. |
| --- | --- | --- |
| high pulse | 1 | Measures high pulses. |

Default value: low pulse

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### pulse number

Number of the pulse that this node measures.

pulse number

polarity

n

th

n

pulse number

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### reference levels settings

High, middle, and low reference levels of a waveform.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### high ref level

High reference level of the waveform.

After the signal crosses the mid ref level in the rising direction, it must cross the high ref level before the next falling mid ref level crossing can be counted.

Default value: 90

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### mid ref level

Middle reference level of the waveform.

The interval between consecutive rising mid ref level crossings defines one cycle, or period, of the waveform. At least one high or low reference level crossing must separate each mid ref level crossing.

Default value: 50

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### low ref level

Low reference level of the waveform.

After the signal crosses the mid ref level in the falling direction, it must cross the low ref level before the next rising mid ref level crossing can be counted.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### ref units

Units of the high, middle, and low reference levels.

| absolute | 0 | Interprets the reference levels as absolute levels. |
| --- | --- | --- |
| percent | 1 | Interprets the reference levels as a percentage of the full range of the waveform. |

Default value: percent

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### state levels settings

Settings that determine the high and low state levels of a waveform.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### method

Method this node uses to compute the high and low state levels of the waveform.

| histogram | Returns the levels of the histogram bins with the maximum number of hits in the upper and lower regions of the waveform. The upper and lower regions of the waveform include the upper and lower 40%, respectively, of the peak-to-peak range of the waveform. |
| --- | --- |
| peak | Searches the entire waveform for its maximum and minimum levels. |
| auto select | Determines whether the histogram bins that correspond to the high and low state levels each have over 5% of the total hits. If so, this node returns those results. Otherwise, this node uses the peak method. This ensures a reasonable answer for either a square wave (ignoring the overshoot and undershoot) or a triangle wave (where a histogram fails). |

Default value: auto select

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### histogram size

Number of bins in the histogram this node uses to determine the high and low state levels of the waveform.

If you select the peak method, this node ignores this input.

Default value: 256

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### histogram method

Method this node uses to compute the histogram. Currently, mode is the only available histogram method.

| mode | Uses the mode method. |
| --- | --- |

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### reserved

Value reserved for future use.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### period

Time between adjacent middle reference level crossings in the same direction in seconds.

The reciprocal of this value is the signal frequency. The measurement interval includes the pulse you specify in pulse number.

This output returns a double-precision, floating-point number or an array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### pulse duration

Time difference, in seconds, between the first two middle reference level crossings of the specified pulse number.

pulse duration is also known as pulse width.

This output returns a double-precision, floating-point number or an array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### duty cycle

Fraction of a period.

duty cycle is also known as duty factor.

This output returns a double-precision, floating-point number or an array of double-precision, floating-point numbers.

##### Equation for Calculating duty cycle

This node uses the following equation to calculate duty cycle:

In this equation, pulse duration can refer to the high or low portion of the period, depending on whether polarity is high pulse or low pulse.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### measurement info

Pulse-center time of the selected pulse and the absolute reference levels this node uses to define the measurement cycle.

This output can be a cluster or an array of clusters.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### pulse center

Time instant of the midpoint of the specified pulse number.

##### Algorithm Definition

pulse center for a polarity of high pulse is given by the following equation.

where t<sub>c</sub> is the pulse center time, t<sub>f</sub> is the time instant of the falling mid ref level crossing, and t<sub>r</sub> is the time instant of the preceding rising mid ref level crossing.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### ref levels

Three user-defined reference levels of the waveform in absolute units.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### high ref level

The high reference level.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### mid ref level

The middle reference level.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### low ref level

The low reference level.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### ref units

Units of the reference levels.

ref units is always absolute in measurement info.

Parent topic:

Pulse Time and Transition Measurements

<!--NI_TOPIC bundle=daqexpress-api-ref path=pulse-time-and-transition-measurements-transition.html language=enus -->
## TOPIC 00067: Transition

- bundle_id: `daqexpress-api-ref`
- source_path: `pulse-time-and-transition-measurements-transition.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/pulse-time-and-transition-measurements-transition.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Accepts an input signal of a single waveform or an array of waveforms and measures the transition duration, undershoot, and overshoot of a selected positive or negative transition in each waveform. signal The input signal. This input can be a waveform or an array of waveforms. polarity A value speci

Transition

Accepts an input signal of a single waveform or an array of waveforms and measures the transition duration, undershoot, and overshoot of a selected positive or negative transition in each waveform.

[IMAGE alt='1378' src='Transition_Measurements_1_chan.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cmsdt.png']

##### signal

The input signal.

This input can be a waveform or an array of waveforms.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### polarity

A value specifying whether to measure a rising or falling transition.

| Rising | 0 | The node measures a rising transition. |
| --- | --- | --- |
| Falling | 1 | The node measures a falling transition. |

Default value: Rising

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### edge number

The transition to measure. An edge number of n with rising polarity selected indicates that the node measures the n<sup>th</sup> rising transition it detects in the input waveform.

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### reference levels settings

High and low reference levels required to determine the transition interval.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### high ref level

High reference level of the waveform.

A rising high ref level crossing defines the end of a rising transition and a falling high ref level crossing defines the beginning of a falling transition.

Default value: 90

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### mid ref level

Middle reference level of the waveform.

mid ref level is not used in transition measurements.

Default value: 50

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### low ref level

Low reference level of the waveform.

A rising low ref level crossing defines the beginning of a rising transition and a falling low ref level crossing defines the end of a falling transition.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### ref units

Units of the high, middle, and low reference levels.

| absolute | 0 | Interprets the reference levels as absolute levels. |
| --- | --- | --- |
| percent | 1 | Interprets the reference levels as a percentage of the full range of the waveform. |

Default value: percent

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### state levels settings

Settings that determine the high and low state levels of a waveform.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### method

Method this node uses to compute the high and low state levels of the waveform.

| histogram | Returns the levels of the histogram bins with the maximum number of hits in the upper and lower regions of the waveform. The upper and lower regions of the waveform include the upper and lower 40%, respectively, of the peak-to-peak range of the waveform. |
| --- | --- |
| peak | Searches the entire waveform for its maximum and minimum levels. |
| auto select | Determines whether the histogram bins that correspond to the high and low state levels each have over 5% of the total hits. If so, this node returns those results. Otherwise, this node uses the peak method. This ensures a reasonable answer for either a square wave (ignoring the overshoot and undershoot) or a triangle wave (where a histogram fails). |

Default value: auto select

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### histogram size

Number of bins in the histogram this node uses to determine the high and low state levels of the waveform.

If you select the peak method, this node ignores this input.

Default value: 256

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### histogram method

Method this node uses to compute the histogram. Currently, mode is the only available histogram method.

| mode | Uses the mode method. |
| --- | --- |

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### reserved

Value reserved for future use.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### slope

The rate of change of the signal in a transition region between high reference level and low reference level.

This output can return a double-precision, floating-point number or a 1D array of double-precision, floating-point numbers.

The following equation defines slope:

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### transition duration

Time span, in seconds, of the transition.

This output can return a double-precision, floating-point number or a 1D array of double-precision, floating-point numbers.

A rising polarity transition duration is known as rise time, and a falling polarity transition duration is known as fall time, as shown in the following figure:

[IMAGE alt='1378' src='GUID-6898839E-A0B5-4187-B2A9-BCFD55F30894-a5.svg']

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### pre-transition: undershoot

Height of the local minimum preceding a rising or falling transition, which depends on the polarity you specify. Undershoot measures the height as a percentage of the histogram-based amplitude of the signal.

This output can return a double-precision, floating-point number or a 1D array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### pre-transition: overshoot

Height of the local maximum preceding a rising or falling transition, which depends on the polarity you specify. Overshoot measures the height as a percentage of the histogram-based amplitude of the signal.

This output can return a double-precision, floating-point number or a 1D array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### post-transition: undershoot

Height of the local minimum following a rising or falling transition, which depends on the polarity you specify. Undershoot measures the height as a percentage of the histogram-based amplitude of the signal.

This output can return a double-precision, floating-point number or a 1D array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### post-transition: overshoot

Height of the local maximum following a rising or falling transition, which depends on the polarity you specify. Overshoot measures the height as a percentage of the histogram-based amplitude of the signal.

This output can return a double-precision, floating-point number or a 1D array of double-precision, floating-point numbers.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### measurement info

Transition interval end points and the absolute reference levels used to define the transition.

This output can return a cluster or a 1D array of clusters.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### start time

Time of the rising low reference level crossing or falling high reference level crossing that defines the start of the transition to be measured.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### end time

Time of the rising high reference level crossing or falling low reference level crossing that defines the end of the transition to be measured.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### ref levels

Three user-defined reference levels of the waveform in absolute units.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### high ref level

The high reference level.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### mid ref level

The middle reference level.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### low ref level

The low reference level.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### ref units

Units of the reference levels.

ref units is always absolute in measurement info.

#### How polarity Affects Undershoot and Overshoot

The following illustration shows the undershoot and overshoot when polarity is Rising.

[IMAGE alt='1378' src='GUID-E9134D9A-04A9-4FBA-B9E2-DF544EC1D4BB-a5.svg']

The following illustration shows the undershoot and overshoot when polarity is Falling.

[IMAGE alt='1378' src='GUID-4DC3A93A-C4E9-4D32-BBFD-BF549F83CC58-a5.svg']

#### Algorithm for Calculating Pre-transition Outputs

This node calculates pre-transition: undershoot and pre-transition: overshoot according to the following table.

| polarity | pre-transition: undershoot | pre-transition: overshoot |
| --- | --- | --- |
| Rising | 100 * ( low ⁢ state ⁢ ⁢ level ⁢ − local ⁢ ⁢ minimum amplitude ) | 100 * ( local ⁢ ⁢ maximum − low ⁢ state ⁢ level amplitude ) |
| Falling | 100 * ( high ⁢ state ⁢ level − local ⁢ minimum amplitude ) | 100 * ( local ⁢ ⁢ maximum − high ⁢ state ⁢ level amplitude ) |

To calculate pre-transition: undershoot and pre-transition: overshoot, this node searches for a 
 *local minimum* and 
 *local maximum* in the pre-transition aberration region immediately preceding the beginning of the transition specified by edge number and polarity. The pre-transition aberration region is defined as the minimum of 3*(*end time* - 
 *start time*) and (*current transition start time* - 
 *previous transition end time*)/2. If the transition to measure is the first in the waveform, the interval is defined as the minimum of 3*(*end time* - 
 *start time*) and (*start time* - 
 *beginning of the waveform*). This node calculates the 
 *high state level*, 
 *low state level*, and 
 *amplitude* from the input signal.

#### Algorithm for Calculating Post-transition Outputs

This node calculates post-transition: undershoot and post-transition: overshoot according to the following table.

| polarity | post-transition: undershoot | post-transition: overshoot |
| --- | --- | --- |
| Rising | 100 * ( high ⁢ state ⁢ ⁢ level ⁢ − local ⁢ ⁢ minimum amplitude ) | 100 * ( local ⁢ ⁢ maximum − high ⁢ state ⁢ level amplitude ) |
| Falling | 100 * ( low ⁢ state ⁢ ⁢ level ⁢ − local ⁢ ⁢ minimum amplitude ) | 100 * ( local ⁢ ⁢ maximum − low ⁢ state ⁢ level amplitude ) |

To calculate post-transition: undershoot and post-transition: overshoot, this node searches for a 
 *local minimum* and 
 *local maximum* in the post-transition aberration region immediately following the end of the transition specified by edge number and polarity. The post-transition aberration region is defined as the minimum of 3*(*end time* - 
 *start time*) and (*next transition start time* - 
 *current transition end time*)/2. If the transition to measure is the last in the waveform, the interval is defined as the minimum of 3*(*end time* - 
 *start time*) and (*end of the waveform* - 
 *end time*). This node calculates the 
 *high state level*, 
 *low state level*, and 
 *amplitude* from the input signal.

Parent topic:

Pulse Time and Transition Measurements

<!--NI_TOPIC bundle=daqexpress-api-ref path=rotate-string.html language=enus -->
## TOPIC 00068: Rotate String

- bundle_id: `daqexpress-api-ref`
- source_path: `rotate-string.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/rotate-string.html
- document_id: `daqexpress-api-ref`
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

<!--NI_TOPIC bundle=daqexpress-api-ref path=scaling-and-mapping-linear-scale.html language=enus -->
## TOPIC 00069: Linear Scale

- bundle_id: `daqexpress-api-ref`
- source_path: `scaling-and-mapping-linear-scale.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/scaling-and-mapping-linear-scale.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Scales a signal based on a straight line. signal Input signal. This input accepts the following data types: Waveform 1D array of waveforms Double-precision, floating-point number 1D array of double-precision, floating-point numbers 2D array of double-precision, floating-point numbers 1D array of com

Linear Scale

Scales a signal based on a straight line.

[IMAGE alt='1378' src='Linear_Scale_(Wfm).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cmsdt.png']

##### signal

Input signal.

This input accepts the following data types:

- Waveform
- 1D array of waveforms
- Double-precision, floating-point number
- 1D array of double-precision, floating-point numbers
- 2D array of double-precision, floating-point numbers
- 1D array of complex double-precision, floating-point numbers
- 2D array of complex double-precision, floating-point numbers

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### scale

Slope used for linear scaling.

The following equation defines linear scaling: , where m is scale.

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### offset

Intercept used for linear scaling.

The following equation defines linear scaling: , where b is offset.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/imsdt.png']

##### scaled signal

Result of scaling the input signal.

This output can return the following data types:

- Waveform
- 1D array of waveforms
- Double-precision, floating-point number
- 1D array of double-precision, floating-point numbers
- 2D array of double-precision, floating-point numbers
- 1D array of complex double-precision, floating-point numbers
- 2D array of complex double-precision, floating-point numbers

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Scaling and Mapping

<!--NI_TOPIC bundle=daqexpress-api-ref path=scaling-and-mapping-multimode-function.html language=enus -->
## TOPIC 00070: Scaling and Mapping

- bundle_id: `daqexpress-api-ref`
- source_path: `scaling-and-mapping-multimode-function.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/scaling-and-mapping-multimode-function.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Changes the amplitude of a signal by scaling or mapping the signal.

Scaling and Mapping

Changes the amplitude of a signal by scaling or mapping the signal.

Signal Processing Nodes

Linear Scale

Scales a signal based on a straight line.

Map Ranges

Creates a custom scale that scales values proportionally from a range of pre-scaled values to a range of scaled values.

Normalize Range

Transforms a signal so that its maximum value is scaled to a specified high value and its minimum value is scaled to a specified low value.

Parent topic:

Signal Processing Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=scaling-and-mapping-normalize-range.html language=enus -->
## TOPIC 00071: Normalize Range

- bundle_id: `daqexpress-api-ref`
- source_path: `scaling-and-mapping-normalize-range.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/scaling-and-mapping-normalize-range.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Transforms a signal so that its maximum value is scaled to a specified high value and its minimum value is scaled to a specified low value. reset A Boolean that specifies whether to reset the internal state of the node. True Resets the internal state of the node. False Does not reset the internal st

Normalize Range

Transforms a signal so that its maximum value is scaled to a specified high value and its minimum value is scaled to a specified low value.

[IMAGE alt='1378' src='Normalize_Range_(Wfm).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset

A Boolean that specifies whether to reset the internal state of the node.

| True | Resets the internal state of the node. |
| --- | --- |
| False | Does not reset the internal state of the node. |

This input is available only if you wire a double-precision, floating-point number to signal.

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cmsdt.png']

##### signal

Input signal.

This input accepts the following data types:

- Waveform
- 1D array of waveforms
- Double-precision, floating-point number
- 1D array of double-precision, floating-point numbers
- 2D array of double-precision, floating-point numbers

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sample length

Length of each set of data.

The node performs computation for each set of data. sample length must be greater than zero.

This input is available only if you wire a double-precision, floating-point number to signal.

Default value: 100

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### scaled low

Smallest value in the range of scaled values.

Default value: -1

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### scaled high

Largest value in the range of scaled values.

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/imsdt.png']

##### scaled signal

Result of scaling the input signal.

This output can return the following data types:

- Waveform
- 1D array of waveforms
- 1D array of double-precision, floating-point numbers
- 2D array of double-precision, floating-point numbers

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### scale

Scaling factor.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### offset

Offset factor.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Scaling and Mapping

<!--NI_TOPIC bundle=daqexpress-api-ref path=signal-correlation-auto-correlation.html language=enus -->
## TOPIC 00072: Auto Correlation

- bundle_id: `daqexpress-api-ref`
- source_path: `signal-correlation-auto-correlation.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/signal-correlation-auto-correlation.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the auto-correlation of a signal. reset A Boolean that specifies whether to reset the internal state of the node. True Resets the internal state of the node. False Does not reset the internal state of the node. This input is available only if x is a double-precision, floating-point number.

Auto Correlation

Computes the auto-correlation of a signal.

[IMAGE alt='1378' src='1D_Auto_Correlation_(Wfm).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset

A Boolean that specifies whether to reset the internal state of the node.

| True | Resets the internal state of the node. |
| --- | --- |
| False | Does not reset the internal state of the node. |

This input is available only if x is a double-precision, floating-point number.

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cmsdt.png']

##### x

The input signal.

This input supports the following data types.

- Waveform
- 1D array of waveforms
- Double-precision, floating-point number
- 1D array of double-precision, floating-point numbers
- 1D array of complex double-precision, floating-point numbers
- 2D array of double-precision, floating-point numbers

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### normalization

The normalization method to use to compute the auto correlation of the input signal.

This input is available only if x is a waveform or an array.

| none | Does not apply normalization. |
| --- | --- |
| unbiased | Applies unbiased normalization. |
| biased | Applies biased normalization. |

Default value: none

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sample length x

Length of each set of x-values.

sample length x must be greater than 0.

This input is available only if x is a double-precision, floating-point number.

Default value: 100

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### use history data

A Boolean that specifies whether to use the data points before the current block to compute the auto-correlation.

| True | Uses the data points before the current block to compute the auto-correlation. |
| --- | --- |
| False | Does not use the data points before the current block to compute the auto-correlation. |

This input is available only if x is a double-precision, floating-point number.

Default value: True

[IMAGE alt='datatype_icon' src='/assets/img/imsdt.png']

##### Rxx

Autocorrelation of the input signal.

This output can return the following data types:

- Waveform
- 1D array of waveforms
- 1D array of double-precision, floating-point numbers
- 1D array of complex double-precision, floating-point numbers

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Algorithm for Calculating the Auto-Correlation

The auto-correlation Rxx(t) of a function x(t) is defined as

R

x

x

(

t

)

=

x

(

t

)

⊗

x

(

t

)

=

∫

−

∞

∞

x

*

(

τ

)

⋅

x

(

t

+

τ

)

d

τ

R

x

x

(

t

)

=

x

(

t

)

⊗

x

(

t

)

=

∫

−

∞

∞

x

*

(

τ

)

⋅

x

(

t

+

τ

)

d

τ

where the symbol

⊗

For the discrete implementation of this node, let Y represent a sequence whose indexing can be negative, let N be the number of elements in the input sequence x, and assume that the indexed elements of x that lie outside its range are equal to zero, as shown in the following relationship:

x

j

=

0

,

j

<

0

o

r

⁢

j

≥

N

x

j

=

0

,

j

<

0

o

r

⁢

j

≥

N

Then this node obtains the elements of Y using the following formula:

Y

j

=

∑

k

=

0

N

−

1

x

k

*

⋅

x

j

+

k

Y

j

=

∑

k

=

0

N

−

1

x

k

*

⋅

x

j

+

k

for

j

=

−

(

N

−

1

)

,

−

(

N

−

2

)

,

...

⁢

,

−

1

,

0

,

1

,

...

⁢

,

(

N

−

2

)

,

(

N

−

1

)

The elements of the output sequence Rxx are related to the elements in the sequence Y by

R

x

x

i

=

y

i

−

(

N

−

1

)

R

x

x

i

=

y

i

−

(

N

−

1

)

for

i

=

0

,

1

,

2

,

...

⁢

,

2

N

−

2

Notice that the number of elements in the output sequence Rxx is

2

N

−

1

t

N

Rxx

Rxx

N

#### How This Node Applies Unbiased Normalization

This node applies unbiased normalization as follows:

y

j

=

1

N

−

|

j

|

∑

k

=

0

N

−

1

x

k

*

⋅

x

j

+

k

y

j

=

1

N

−

|

j

|

∑

k

=

0

N

−

1

x

k

*

⋅

x

j

+

k

for j = -(N-1), -(N-2), ..., -1, 0, 1, ..., (N-2), (N-1), and

R

x

x

(

u

n

b

i

a

s

e

d

)

i

=

y

i

−

(

N

−

1

)

R

x

x

(

u

n

b

i

a

s

e

d

)

i

=

y

i

−

(

N

−

1

)

for i = 0, 1, 2, ..., 2N-2

#### How This Node Applies Biased Normalization

This node applies biased normalization as follows:

y

j

=

1

N

∑

k

=

0

N

−

1

x

k

*

⋅

x

j

+

k

y

j

=

1

N

∑

k

=

0

N

−

1

x

k

*

⋅

x

j

+

k

for j = -(N-1), -(N-2), ..., -1, 0, 1, ..., (N-2), (N-1), and

R

x

x

(

b

i

a

s

e

d

)

i

=

y

i

−

(

N

−

1

)

R

x

x

(

b

i

a

s

e

d

)

i

=

y

i

−

(

N

−

1

)

for i = 0, 1, 2, ..., 2N-2

Parent topic:

Signal Correlation

<!--NI_TOPIC bundle=daqexpress-api-ref path=signal-correlation-multimode-function.html language=enus -->
## TOPIC 00073: Signal Correlation

- bundle_id: `daqexpress-api-ref`
- source_path: `signal-correlation-multimode-function.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/signal-correlation-multimode-function.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes auto or cross signal correlation.

Signal Correlation

Computes auto or cross signal correlation.

Signal Processing Nodes

Auto Correlation

Computes the auto-correlation of a signal.

Cross Correlation

Computes the cross correlation of two signals.

Parent topic:

Signal Processing Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=signal-processing-nodes.html language=enus -->
## TOPIC 00074: Signal Processing Nodes

- bundle_id: `daqexpress-api-ref`
- source_path: `signal-processing-nodes.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/signal-processing-nodes.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`

Signal Processing Nodes

Amplitude Measurements

Returns signal characteristics such as peak amplitude, pulse level, and cycle average.

Filter

Processes signals through a lowpass, highpass, bandpass, or bandstop filter.

Limit Testing

Performs limit testing on the input signal.

Noise Generator

Generates a signal containing noise with a specific pattern.

Pattern Generator

Generates a signal containing a specific pattern.

Pulse Time and Transition Measurements

Performs pulse time and transition measurements.

Resample

Resamples a signal according to specific delay and sampling interval.

Scaling and Mapping

Changes the amplitude of a signal by scaling or mapping the signal.

Signal Correlation

Computes auto or cross signal correlation.

Wave Generator

Generates a signal containing a wave pattern.

<!--NI_TOPIC bundle=daqexpress-api-ref path=sine-and-cosine.html language=enus -->
## TOPIC 00075: Sine and Cosine

- bundle_id: `daqexpress-api-ref`
- source_path: `sine-and-cosine.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/sine-and-cosine.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes both the sine and cosine of a specified value (x) in radians. Use this node only when you need both results. x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA When you add this node t

Sine and Cosine

Computes both the sine and cosine of a specified value (x) in radians.

Use this node only when you need both results.

[IMAGE alt='1378' src='SineAndCosine.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### sin

Result of the operation.

x

x

x

i

x

sin

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### cos

Result of the operation.

x

x

x

i

x

cos

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

Parent topic:

Trigonometric Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=sine.html language=enus -->
## TOPIC 00076: Sine

- bundle_id: `daqexpress-api-ref`
- source_path: `sine.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/sine.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the sine of a specified value (x) in radians. x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this input has a default data

Sine

Computes the sine of a specified value (x) in radians.

[IMAGE alt='1378' src='Sine.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### sin

Result of the operation.

x

x

x

i

x

sin

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

Parent topic:

Trigonometric Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=statistics-nodes.html language=enus -->
## TOPIC 00077: Statistics Nodes

- bundle_id: `daqexpress-api-ref`
- source_path: `statistics-nodes.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/statistics-nodes.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`

Statistics Nodes

Histogram

Computes a histogram for a signal.

Statistics

Performs statistical calculations on a signal.

<!--NI_TOPIC bundle=daqexpress-api-ref path=string-length.html language=enus -->
## TOPIC 00078: String Length

- bundle_id: `daqexpress-api-ref`
- source_path: `string-length.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/string-length.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of characters in a string. string A string whose number of characters you want to compute. This input also supports any data type that includes only strings, such as an array of strings or a cluster of strings. length Number of characters in a string. The structure of this output

String Length

Returns the number of characters in a string.

[IMAGE alt='1378' src='StringLength.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### string

A string whose number of characters you want to compute.

This input also supports any data type that includes only strings, such as an array of strings or a cluster of strings.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### length

Number of characters in a string.

The structure of this output matches the structure of the string. For example, if you wire an array of strings to string, this output returns an array of integers. Likewise, if you wire a cluster of strings to string, this output returns a cluster of integers.

Note

16

#### Reducing Performance Burden

Characters in UTF-8 can be multiple bytes so string nodes count the number of characters in a string instead of jumping to a point in memory. Since the length and offset parameters are in units of characters, avoid nesting this node with large strings because that can create exponential functions that carry a higher performance burden.

Parent topic:

String Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=string-to-path.html language=enus -->
## TOPIC 00079: String to Path

- bundle_id: `daqexpress-api-ref`
- source_path: `string-to-path.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/string-to-path.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a string that represents a path into the path data type. string The string you want to convert to a path. This input can also be any data type that contains only strings, such as an array of strings or a cluster of strings. If string is <Not A Path>, the node returns the <Not A Path> value

String to Path

Converts a string that represents a path into the path data type.

[IMAGE alt='1378' src='StringToPath.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### string

The string you want to convert to a path.

If 
 string is 
 <Not A Path>, the node returns the 
 <Not A Path> value for path.

[IMAGE alt='datatype_icon' src='/assets/img/ipath.png']

##### path

The path representation of 
string.

path

string

string

path

##### Reasons This Output Returns <Not a Path>

<Not A Path>

- string cannot convert to a valid path
- string contains the text 
 <Not A Path>

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=subtract.html language=enus -->
## TOPIC 00080: Subtract

- bundle_id: `daqexpress-api-ref`
- source_path: `subtract.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/subtract.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the difference between numbers, timestamps, or waveforms. You cannot subtract a timestamp from a numeric value. x The value to subtract from. This input supports scalar numbers, enumerated type values, timestamps, waveforms, and any data type that contains only these data types, such as an

Subtract

Computes the difference between numbers, timestamps, or waveforms.

You cannot subtract a timestamp from a numeric value.

[IMAGE alt='1378' src='Subtract.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

The value to subtract from.

This input supports scalar numbers, enumerated type values, timestamps, waveforms, and any data type that contains only these data types, such as an array or cluster of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### y

The value to subtract from the other input.

This input supports scalar numbers, enumerated type values, timestamps, waveforms, and any data type that contains only these data types, such as an array or cluster of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

This input appears only when you wire a waveform to input.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### x - y

The difference between the two inputs.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

The node produces this output according to standard error behavior.

This output appears only when you wire a waveform to input.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=system-exec.html language=enus -->
## TOPIC 00081: System Exec

- bundle_id: `daqexpress-api-ref`
- source_path: `system-exec.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/system-exec.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Executes or launches other Windows-based applications, command-line applications, or batch files. You can include any parameters within your command string that the executing command supports. expected output size The number of bytes you expect the output of the command to be. Entering a number slig

System Exec

Executes or launches other Windows-based applications, command-line applications, or batch files.

You can include any parameters within your command string that the executing command supports.

[IMAGE alt='1378' src='System_Exec.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### expected output size

The number of bytes you expect the output of the command to be.

Entering a number slightly larger than the output size you expect leads to more efficient memory use. The command runs even if you exceed this size, but memory is used less efficiently.

Default value: 4096

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### wait until completion?

A Boolean value that determines whether this node continues running until the command finishes running.

| True | This node keeps running until the command finishes running. The standard output and standard error values are available when the command finishes running. |
| --- | --- |
| False | This node finishes running immediately after executing the command. The command runs in the background, and the standard output and standard error values are not available when the command finishes running. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### command line

The command this node calls to run a program.

If the executable is not in a directory listed in the PATH environment variable, the command line must contain the full path to the executable. To use a command that must be executed directly from a command prompt window, insert 
 cmd /c before the command.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### standard input

The text to pass to the command line as standard input.

[IMAGE alt='datatype_icon' src='/assets/img/cpath.png']

##### working directory

The file system directory from which you want to execute the command.

Note

working directory

working directory

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### run minimized?

A Boolean value that determines whether the executable program that is called is minimized while running.

| True | The executable program is minimized while running. |
| --- | --- |
| False | The executable program is not minimized while running. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### standard output

The information returned by the executable program.

If wait until completion is set to False, this node returns an empty string.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### standard error

The errors returned by the executable program.

If wait until completion is set to False, this node returns an empty string.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### return code

The system-dependent exit code that the command returns.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Program Flow Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=tangent.html language=enus -->
## TOPIC 00082: Tangent

- bundle_id: `daqexpress-api-ref`
- source_path: `tangent.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/tangent.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the tangent of a specified value (x) in radians. x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this input has a default d

Tangent

Computes the tangent of a specified value (x) in radians.

[IMAGE alt='1378' src='Tangent.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### tan

Result of the operation.

x

x

x

i

x

tan

Parent topic:

Trigonometric Nodes

<!--NI_TOPIC bundle=daqexpress-api-ref path=tdms-close.html language=enus -->
## TOPIC 00083: TDMS Close

- bundle_id: `daqexpress-api-ref`
- source_path: `tdms-close.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/tdms-close.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes a reference to the .tdms file. This node disposes of the reference to the .tdms file once the node closes the reference. © 2017 National Instruments. All rights reserved. tdms file A reference to a .tdms file. Use the TDMS Open node to obtain the reference. error in Error conditions that occu

TDMS Close

Closes a reference to the 
.tdms file.

This node disposes of the reference to the 
 .tdms file once the node closes the reference.

© 2017 National Instruments. All rights reserved.

[IMAGE alt='1378' src='TDMSClose.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### tdms file

A reference to a 
.tdms file. Use the TDMS Open node to obtain the reference.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ipath.png']

##### file path out

Path to the 
.tdms file reference that the node closed.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

TDMS Nodes

Related information:

- http://www.ni.com/white-paper/5696/en/

<!--NI_TOPIC bundle=daqexpress-api-ref path=to-single-precision-float.html language=enus -->
## TOPIC 00084: To Single Precision Float

- bundle_id: `daqexpress-api-ref`
- source_path: `to-single-precision-float.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/to-single-precision-float.html
- document_id: `daqexpress-api-ref`
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

<!--NI_TOPIC bundle=daqexpress-api-ref path=wait-ms.html language=enus -->
## TOPIC 00085: Milliseconds

- bundle_id: `daqexpress-api-ref`
- source_path: `wait-ms.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/wait-ms.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits the specified number of milliseconds and returns the value of the millisecond timer. milliseconds to wait Number of milliseconds to wait. Wiring a value of 0 to this input forces the execution system to check for other available code to execute. Maximum Input before Timer Wrap-Around If the wa

Milliseconds

Waits the specified number of milliseconds and returns the value of the millisecond timer.

[IMAGE alt='1378' src='Wait.Milliseconds.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### milliseconds to wait

Number of milliseconds to wait.

Wiring a value of 0 to this input forces the execution system to check for other available code to execute.

##### Maximum Input before Timer Wrap-Around

If the wait time you specify is greater than the maximum allowed for the 
 Counter size of the Wait node, the expected program wait time wraps around and starts again from zero. You can configure the 
 Counter size of the node in the 
 Item tab.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### millisecond timer value

Value of the operating system's millisecond timer after the wait.

#### Programming Patterns

- Adjusting the Execution Speed of a Loop

#### Timer Accuracy

The accuracy of the timer varies across operating systems.
 If the operating system takes more time to process a request than the time that the input specifies, the actual wait time is longer than the time that the input specifies.

#### When to Use Wait Until Next Multiple instead of Wait

If you need to ensure that an operation waits at least the specified time before completing execution, you can use either a Wait node or a Wait Until Next Multiple node. However, for functions that feedback an output as an input and require consistent timing between iterations to achieve equilibrium, such as a PID node in a loop, use a Wait Until Next Multiple node. Compared to Wait nodes, Wait Until Next Multiple nodes have more periodic spacing between iterations, because even if one iteration finishes late, the following iteration still executes on the multiple of the Wait Until Next Multiple input.

#### Thread Availability During Wait Time

When an active execution system thread in a program reaches a Wait node in the millisecond configuration, the node execution is rescheduled cooperatively and the temporarily available thread is used by any other currently executing code until the wait time expires.

When you use the microsecond or tick configuration of this node, the thread which encounters the Wait node is blocked until the wait time expires.

Parent topic:

Wait

<!--NI_TOPIC bundle=daqexpress-api-ref path=wait-ticks.html language=enus -->
## TOPIC 00086: Ticks

- bundle_id: `daqexpress-api-ref`
- source_path: `wait-ticks.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/wait-ticks.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Causes the diagram or subdiagram to wait a specified number of ticks before completing execution. A single tick represents one nanosecond. ticks to wait Number of ticks to wait. Wiring a value of 0 to this input forces the execution system to check for other available code to execute. Maximum Input

Ticks

Causes the diagram or subdiagram to wait a specified number of ticks before completing execution.
 
 A single tick represents one nanosecond.

[IMAGE alt='1378' src='Wait.Ticks.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### ticks to wait

Number of ticks to wait.

Wiring a value of 0 to this input forces the execution system to check for other available code to execute.

##### Maximum Input before Timer Wrap-Around

If the wait time you specify is greater than the maximum allowed for the 
 Counter size of the Wait node, the expected program wait time wraps around and starts again from zero. You can configure the 
 Counter size of the node in the 
 Item tab.

##### Highest Timer Resolution

The highest timer resolution for this node is one millisecond. Microsecond or tick values are rounded to the nearest millisecond value.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### tick timer value

Value of the operating system's tick timer after the wait.

#### Programming Patterns

- Adjusting the Execution Speed of a Loop

#### Timer Accuracy

The accuracy of the timer varies across operating systems.
 If the operating system takes more time to process a request than the time that the input specifies, the actual wait time is longer than the time that the input specifies.

#### When to Use Wait Until Next Multiple instead of Wait

If you need to ensure that an operation waits at least the specified time before completing execution, you can use either a Wait node or a Wait Until Next Multiple node. However, for functions that feedback an output as an input and require consistent timing between iterations to achieve equilibrium, such as a PID node in a loop, use a Wait Until Next Multiple node. Compared to Wait nodes, Wait Until Next Multiple nodes have more periodic spacing between iterations, because even if one iteration finishes late, the following iteration still executes on the multiple of the Wait Until Next Multiple input.

#### Thread Availability During Wait Time

When an active execution system thread in a program reaches a Wait node in the millisecond configuration, the node execution is rescheduled cooperatively and the temporarily available thread is used by any other currently executing code until the wait time expires.

When you use the microsecond or tick configuration of this node, the thread which encounters the Wait node is blocked until the wait time expires.

Parent topic:

Wait

<!--NI_TOPIC bundle=daqexpress-api-ref path=wave-generator-square.html language=enus -->
## TOPIC 00087: Square

- bundle_id: `daqexpress-api-ref`
- source_path: `wave-generator-square.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/wave-generator-square.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates a signal containing a square wave. offset DC offset of the signal. Default value: 0 reset phase A Boolean that determines the initial phase of the wave. True Sets the initial phase to phase in and sets the initial time to t0 if you configure this node to return a waveform. Sets the initial

Square

Generates a signal containing a square wave.

[IMAGE alt='1378' src='Square_Waveform.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### offset

DC offset of the signal.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset phase

A Boolean that determines the initial phase of the wave.

| True | Sets the initial phase to phase in and sets the initial time to t0 if you configure this node to return a waveform. Sets the initial phase to phase in if you configure this node to return a double-precision, floating-point number or an array of double-precision, floating-point numbers. |
| --- | --- |
| False | Uses the values of phase out and t0 from when the node last executed as the initial phase and time of the wave if you configure this node to return a waveform. Uses the values of phase out from when the node last executed as the initial phase of the wave if you configure this node to return a double-precision, floating-point number or an array of double-precision, floating-point numbers. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### amplitude

Amplitude of the signal.

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### frequency

Frequency of the signal.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### phase in

Initial phase in degrees of the signal when reset phase is True.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### duty cycle

Percentage of time a square wave remains high versus low over one period.

Default value: 50

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### sample rate

Sample rate in samples per second.

Default value: 1000

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples

Number of samples in the signal.

samples must be greater than 0. Otherwise, this node returns an error.

This input is available when you configure this node to return a waveform or an array of double-precision, floating-point numbers.

Default value: 1000

[IMAGE alt='datatype_icon' src='/assets/img/ctimestamp.png']

##### t0

Timestamp of the output signal.

This input is available only if you configure this node to return a waveform.

[IMAGE alt='datatype_icon' src='/assets/img/imsdt.png']

##### square wave

Output square signal.

This output can return the following data types:

- Waveform
- Double-precision, floating-point number
- 1D array of double-precision, floating-point numbers

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### phase out

Phase, in degrees, of the next sample of the output signal.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Algorithm for Simulating a Square Wave

If sequence Y represents a square wave, this node generates the pattern according to the following equation.

y

[

i

]

=

amplitude

×

square

(

phase

[

i

]

)

,

f

o

r

⁢

i

=

0

,

1

,

2

,

...

,

n

−

1

y

[

i

]

=

amplitude

×

square

(

phase

[

i

]

)

,

f

o

r

⁢

i

=

0

,

1

,

2

,

...

,

n

−

1

where n is the number of samples. The node calculates

square

(

phase

[

i

]

)

| p mod [ i ] | square ( phase [ i ] ) |
| --- | --- |
| 0 ≤ p m o d [ i ] < ( 0.01 ⁢ × d u t y ⁢ c y c l e ) × 360 | 1 |
| ( 0.01 ⁢ × d u t y ⁢ c y c l e ) × 360 ≤ p m o d [ i ] ≤ 360 | -1 |

where

p

mod

[

i

]

phase

[

i

]

phase

[

i

]

initial_phase

+

frequency

×

360

×

i

samples per second

initial_phase

+

frequency

×

360

×

i

samples per second

where 
 *initial_phase* is the initial phase of the wave.

Parent topic:

Wave Generator

<!--NI_TOPIC bundle=daqexpress-api-ref path=write-delimited-spreadsheet.html language=enus -->
## TOPIC 00088: Write Delimited Spreadsheet

- bundle_id: `daqexpress-api-ref`
- source_path: `write-delimited-spreadsheet.html`
- source_url: https://docs-be.ni.com/bundle/daqexpress-api-ref/raw/resource/enus/write-delimited-spreadsheet.html
- document_id: `daqexpress-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts data to a text string and writes the string to a file. This node creates a text file readable by most spreadsheet applications. This node opens or creates the file before writing to it and closes it afterwards. format A string that uses format specifiers to determine how to convert the data

Write Delimited Spreadsheet

Converts data to a text string and writes the string to a file.

This node creates a text file readable by most spreadsheet applications. This node opens or creates the file before writing to it and closes it afterwards.

[IMAGE alt='1378' src='Write_Delimited_Spreadsheet_(1D_DBL).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### format

A string that uses format specifiers to determine how to convert the data into what you specify.

Default value: 
 %.3f

##### Syntax Elements for Creating a Format Specifier

Use the following syntax elements to create a format specifier for the input string.

| Syntax Element | Description |
| --- | --- |
| % | Syntax element that begins the format specifier. |
| $ (optional) | Modifier that specifies the order in which to display variables when used within a formatting node. Include the digit that represents the order of the variable immediately before this modifier. |
| - (optional) | Modifier that justifies the parameter to the left, within its width, when used within a formatting node. |
| + (optional) | Modifier that includes mathematical symbols when used within a formatting node. Note The mathematical symbols appear even when the number is positive. |
| ^ (optional) | Modifier that formats the number in engineering notation, where the exponent is always a multiple of three. Note This modifier must be used within a formatting node that has either an e or g conversion code in the format specifier. |
| # (optional) | Modifier that removes trailing zeros when used within a formatting node. If the number has no fractional part, this modifier also removes the description part. |
| 0 (optional) | Modifier that pads any excess space to the left of a numeric parameter with zeros, rather than spaces, to reach a minimum width when used within a formatting node. Note Using the - modifier with 0 nullifies the effect. |
| Width (optional) | Syntax element that specifies an exact field width to use. When used within a formatting node, the Width element specifies the minimum character field with of the output. The field is padded to the left or right of the parameter with spaces, depending on justification. Note As many characters as necessary are used to format the parameter without truncating it. |
| .Precision or _Significant Digits (optional) | Syntax element that controls the number of digits displayed when used within a formatting node. .precision—Yields the number of digits to the right of the decimal point. _Significant Digits—Rounds the data to the number of digits you specify. Note You cannot use precision and significant digits together in a single format specifier. |
| {Unit} (optional) | Syntax element that overrides the original unit of a VI when you use a node to convert a physical quantity. |
| <Embedded Time Format> (optional) | Contains a time-specific format string for use with the T (absolute time) and the t (relative time) conversion codes. Note Only %W, %D, %H, %M, %S, and %u apply to relative time. |
| Conversion Codes | Characters that specify how to scan or format a parameter. x—Hexadecimal integer o—Octal integer b—Binary integer d—Signed decimal integer u—Unsigned decimal integer f—Floating-point number with fractional format e—Floating-point number in scientific notation g—Uses f or e depending on the exponent of the number p—Floating-point number in SI notation s—Scans a string, matching only up to the next white-space character. [ ]—Scans characters in a set, matching a string that contains only the characters specified between the brackets. % [aeiou]—Scans characters in a set, matching any string that contains only lowercase vowels % [0-9a-zA-Z ]— Scans characters in a set, matching a string that contains numbers, letters, or spaces. You can use a hyphen to specify ranges of characters in the set. % [^,;]— Scans characters in a set, matching any string of characters up to but not including the first comma or semicolon. T—Absolute time t—Relative time |
| Localization Codes | Characters that determine whether to use a decimal or a comma to separate the whole number from the decimal part of the number. %,;—Comma decimal separator %.;—Period decimal separator %;—System default separator |
| Backslash (\\) Codes | Characters that specify hex values, spacing, backspaces, and other formatting options. |

##### Format Specifier Examples for Format

| format string | Description |
| --- | --- |
| %.3f | Creates a string to represent the number with three digits to the right of the decimal point. |
| %s | Copies the input string. |
| %d | Converts the data to integer form using as many characters as necessary to contain the entire number. |

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### include time channels

A Boolean value that determines whether the resulting spreadsheet will include a column of time values from the input array of waveforms.

This input becomes available only when you wire an array of waveforms to this node.

[IMAGE alt='datatype_icon' src='/assets/img/cpath.png']

##### file

The file to which this node writes.

If the path is empty, this node uses your default data directory (Documents>>LabVIEW Data).

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### 2D data

Data the node writes to the file.

This input accepts double-precision floating-point numbers, 64-bit integers, strings, and arrays of waveforms. This input changes to waveforms if you wire an array of waveforms to the node.

[IMAGE alt='datatype_icon' src='/assets/img/c1dmsdt.png']

##### waveforms

Array of waveforms whose y values the node writes to the spreadsheet file.

This input becomes available only if you wire an array of waveforms to the node.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### append to file

A Boolean that determines whether to add data to the end of the file you specify. If you do not specify a file, the node creates a new file.

| True | Appends data to the existing file. |
| --- | --- |
| False | Replaces the data in the file. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### delimiter

A character or string of characters used to separate fields in the spreadsheet text. For example, a value of 
, (comma) specifies a single comma as the delimiter.

Default value: 
 \t — single tab character

[IMAGE alt='datatype_icon' src='/assets/img/ipath.png']

##### new file

Path to the newly created file.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Storage Nodes
