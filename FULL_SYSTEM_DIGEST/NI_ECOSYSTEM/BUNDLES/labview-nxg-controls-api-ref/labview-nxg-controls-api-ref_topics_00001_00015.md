# NI DOCUMENT BUNDLE: labview-nxg-controls-api-ref

<!--NI_BUNDLE_CHUNK bundle=labview-nxg-controls-api-ref start=1 end=15 -->
<!--NI_TOPIC bundle=labview-nxg-controls-api-ref path=array-control.html language=enus -->
## TOPIC 00001: Array Controls

- bundle_id: `labview-nxg-controls-api-ref`
- source_path: `array-control.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-controls-api-ref/raw/resource/enus/array-control.html
- source_language: `enus`
- document_id: `labview-nxg-controls-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Group data elements of the same type. Examples An example of a simple array is a 1D text array that lists the eight planets of our solar system in order. Array elements are ordered. An array uses an index so you can readily access any particular element. The index is zero-based, which means it is in

Array Controls

Group data elements of the same type.

[IMAGE alt='1378' src='GUID-AFB17239-0E71-4021-A375-8676CEE39DD2-a5.png']

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

<!--NI_TOPIC bundle=labview-nxg-controls-api-ref path=button-controls.html language=enus -->
## TOPIC 00002: Button Controls

- bundle_id: `labview-nxg-controls-api-ref`
- source_path: `button-controls.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-controls-api-ref/raw/resource/enus/button-controls.html
- source_language: `enus`
- document_id: `labview-nxg-controls-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enter or display true and false data. Which Button Should I Use? Button Type Use Default Mechanical Action Buttons Enter true or false input. Latch when released Checkbox Select an item or items from a list. Switch when released only Switches Enter true or false input in an application. Latch when r

Button Controls

Enter or display true and false data.

[IMAGE alt='1378' src='GUID-67CB3772-DD70-433F-ABD3-1FF5B137E804-a5.png']

#### Which Button Should I Use?

| Button Type | Use | Default Mechanical Action |
| --- | --- | --- |
| Buttons | Enter true or false input. | Latch when released |
| Checkbox | Select an item or items from a list. | Switch when released only |
| Switches | Enter true or false input in an application. | Latch when released |
| LEDs | Indicate true or false data. You must select Show values on the Item tab for content to appear on the LED. | Switch when released |

#### Which Mechanical Action Should I Use?

The mechanical action of the control determines how the control behaves. You classify mechanical actions as either switch actions or latch actions:

| I want my control to behave like a... | Mechanical Action | What This Mechanical Action Does | Caveats |
| --- | --- | --- | --- |
| Power button | Switch when pressed | Changes as soon as you click down on the control without waiting for you to release the mouse. |  |
| On/off switch | Switch when released | Changes the control value only after you release the mouse button within the graphical boundary of the control. | The mechanical action for radio buttons and checkboxes is not configurable; it is always switch when released. |
| Door buzzer | Switch until released | Changes the control value when you press it and retains the new value until you release the mouse button. | The frequency with which the program reads the control does not affect this behavior. You cannot select this behavior for a radio button control or a checkbox control. |
| Circuit breaker | Latch when pressed | Changes the control value when you press it and retains the new value until the program reads it once. | This behavior is useful for getting the program to perform an action only once each time you set the control. You cannot select this behavior for a radio button control or a checkbox control. |
| Dialog box button | Latch when released | Changes the control value only after you press and then release the mouse button within the graphical boundary of the control and retains the new value until the program reads it once. | This behavior is useful for stopping a While Loop. When the program reads the control once, the control reverts to its default value. You cannot select this behavior for a radio button control or a checkbox control. |

<!--NI_TOPIC bundle=labview-nxg-controls-api-ref path=chart-control.html language=enus -->
## TOPIC 00003: Chart Control

- bundle_id: `labview-nxg-controls-api-ref`
- source_path: `chart-control.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-controls-api-ref/raw/resource/enus/chart-control.html
- source_language: `enus`
- document_id: `labview-nxg-controls-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-controls-api-ref path=charts-and-graphs.html language=enus -->
## TOPIC 00004: Charts and Graphs

- bundle_id: `labview-nxg-controls-api-ref`
- source_path: `charts-and-graphs.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-controls-api-ref/raw/resource/enus/charts-and-graphs.html
- source_language: `enus`
- document_id: `labview-nxg-controls-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-controls-api-ref path=cluster-controls.html language=enus -->
## TOPIC 00005: Cluster Controls

- bundle_id: `labview-nxg-controls-api-ref`
- source_path: `cluster-controls.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-controls-api-ref/raw/resource/enus/cluster-controls.html
- source_language: `enus`
- document_id: `labview-nxg-controls-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Group data elements of a mixed type that logically belong together. What Is a Cluster? Clusters group data elements of mixed types. A cluster is similar to a record or a struct in text-based programming languages. Which Cluster Should I Use? You can choose from the following cluster types, and clust

Cluster Controls

Group data elements of a mixed type that logically belong together.

[IMAGE alt='1378' src='GUID-90EA61A3-0E2B-4ED4-8E71-BBD98C7C9C18-a5.png']

#### What Is a Cluster?

Clusters group data elements of mixed types. A cluster is similar to a record or a struct in text-based programming languages.

#### Which Cluster Should I Use?

You can choose from the following cluster types, and clusters can be nested:

| Use | Type |
| --- | --- |
| Groups a checkbox, numeric control, and string control together to input error information. | Error In |
| Groups a checkbox, numeric indicator, and string control together to display error information. | Error Out |
| Groups a timestamp, numeric array, and numeric control together to display waveform data. | Waveform |
| Create a custom group by dragging and dropping controls, such as buttons, graphs, arrays, and so on, into the cluster shell. | Empty Cluster |

#### How Do I Reorder Cluster Elements?

You can reorder cluster elements by using the 
 Data items section on the 
 Item tab or by moving controls inside or outside the cluster. The order of the controls within the cluster is determined by the order in which you add them to the cluster.

#### How Do I Tab Through Cluster Elements?

Press Ctrl-Down Arrow or Ctrl-Up Arrow to tab through cluster elements, even nested clusters.

<!--NI_TOPIC bundle=labview-nxg-controls-api-ref path=data-grid.html language=enus -->
## TOPIC 00006: Data Grid

- bundle_id: `labview-nxg-controls-api-ref`
- source_path: `data-grid.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-controls-api-ref/raw/resource/enus/data-grid.html
- source_language: `enus`
- document_id: `labview-nxg-controls-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-controls-api-ref path=escape-sequences.html language=enus -->
## TOPIC 00007: Escape Sequences

- bundle_id: `labview-nxg-controls-api-ref`
- source_path: `escape-sequences.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-controls-api-ref/raw/resource/enus/escape-sequences.html
- source_language: `enus`
- document_id: `labview-nxg-controls-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists allowable escape sequences for character representations. Escaping characters using hex codes is not supported. Escape Sequence Character Represented \b Backspace \f Form feed \n Newline or line feed \r Carriage return \s Space \t Tab \\ Backslash Use escape sequences to su

Escape Sequences

The following table lists allowable escape sequences for character representations. Escaping characters using hex codes is not supported.

| Escape Sequence | Character Represented |
| --- | --- |
| \\b | Backspace |
| \\f | Form feed |
| \\n | Newline or line feed |
| \\r | Carriage return |
| \\s | Space |
| \\t | Tab |
| \\\\ | Backslash |

Use escape sequences to substitute for reserved characters in string terminals and string constants. On the 
 Item tab, toggle the 
 Show escape sequences checkbox to display escape sequences or character representations.

Parent topic:

Text Controls

Parent topic:

Text Controls

<!--NI_TOPIC bundle=labview-nxg-controls-api-ref path=graph-control.html language=enus -->
## TOPIC 00008: Graph Control

- bundle_id: `labview-nxg-controls-api-ref`
- source_path: `graph-control.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-controls-api-ref/raw/resource/enus/graph-control.html
- source_language: `enus`
- document_id: `labview-nxg-controls-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Plot numeric, complex, X/Y, or point sample data contained in arrays and analog waveforms. What Types of Data Can I Plot? You can plot numeric, complex, or point sample data contained in arrays and analog waveforms. By default, the graph data type is an array of doubles. You can change the data type

Graph Control

Plot numeric, complex, X/Y, or point sample data contained in arrays and analog waveforms.

[IMAGE alt='1378' src='GUID-CF2EAC4E-EA4D-4A61-B7BB-E209E72CF813-a5.png']

#### What Types of Data Can I Plot?

You can plot numeric, complex, or point sample data contained in arrays and analog waveforms. By default, the graph data type is an array of doubles. You can change the data type on the diagram.

The waveform data type carries the start time (t0), delta t (dt), and y-values (Y) of a waveform. When you wire waveform data to a graph, the graph automatically plots a waveform based on the start time, delta t, and y-values of the waveform.

For data contained in arrays, the graph displays a general-purpose Cartesian graph that plots any set of points, evenly sampled or not.

The following table describes how graphs plot different types of array data.

| Data Type | Plot Behavior |
| --- | --- |
| 1D array of numeric values | The array is a single plot. X-value: Array index Y-value: Array element |
| 1D array of complex or cluster values | The array is a single plot. The cluster must be a two-element cluster. X-value: First element of the complex number or cluster Y-value: Second element of the complex number or cluster |
| Cluster of two 1D arrays of numeric values | The cluster is a single plot. X-value: Elements of the first array Y-value: Elements of the second array |
| 1D array of waveforms | Each waveform is a separate plot. |
| 2D array of numeric values | Each row of the array is a separate plot. |
| 2D array of complex or cluster values | Each row of the array is a separate plot. The cluster must be a two-element cluster.X-value: First element of the complex number or clusterY-value: Second element of the complex number or cluster |
| 1D array of clusters of 1D arrays | Each cluster of arrays is a separate plot. Arrays within a cluster must be the same size, but arrays in different clusters can be different sizes. |
| Cluster of two numeric values and a 1D array | The cluster is a single plot.X-value: An initial x value incremented by a delta x. The first numeric value represents the initial x value, and the second numeric value represents the delta x valueY-value: Elements of the arrayThis data type is not supported. |

Parent topic:

Charts and Graphs

<!--NI_TOPIC bundle=labview-nxg-controls-api-ref path=intensity-graph-control.html language=enus -->
## TOPIC 00009: Intensity Graph Control

- bundle_id: `labview-nxg-controls-api-ref`
- source_path: `intensity-graph-control.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-controls-api-ref/raw/resource/enus/intensity-graph-control.html
- source_language: `enus`
- document_id: `labview-nxg-controls-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Plot 3D data on a 2D plot by using color to display the values of the third dimension. For example, you can use an intensity graph to display patterned data, such as terrain, where the magnitude represents altitude. What Types of Data Can I Plot? Intensity graphs accept 2D arrays of numeric values.

Intensity Graph Control

Plot 3D data on a 2D plot by using color to display the values of the third dimension. For example, you can use an intensity graph to display patterned data, such as terrain, where the magnitude represents altitude.

[IMAGE alt='1378' src='GUID-95977A16-0963-4A2A-9D95-DF05B3E9702B-a5.png']

#### What Types of Data Can I Plot?

Intensity graphs accept 2D arrays of numeric values. Each number in the array represents a specific color. The array indexes correspond to the center of the color block. The row index of the array is the x-value, and the column index of the array is the y-value. The color block has a unit area, which is the area between the two points, as defined by the array indexes.

Rows of the array appear as columns on the graph and vice-versa. If you want rows to appear as rows on the graph, use Transpose 2D Array before wiring the array to the graph.

#### Configuring the Color Scale

When you set the color mapping for an intensity graph, you configure the color scale of the graph. The color scale consists of at least two markers, each with a numeric value and a corresponding display color. The colors displayed on an intensity graph correspond to the numeric values associated with the specified colors. Color mapping is useful for visually indicating data ranges, such as when plot data exceeds a threshold value.

Click 
 Color scale on the 
 Item tab to set the color mapping. Lower and upper out-of-range colors are specified as 
 High color and 
 Low color and are displayed on the graph.

Parent topic:

Charts and Graphs

<!--NI_TOPIC bundle=labview-nxg-controls-api-ref path=ISHPUBLMODULEMISSING.html language=dede -->
## TOPIC 00010: Topic Missing

- bundle_id: `labview-nxg-controls-api-ref`
- source_path: `ISHPUBLMODULEMISSING.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-controls-api-ref/raw/resource/dede/ISHPUBLMODULEMISSING.html
- source_language: `dede`
- document_id: `labview-nxg-controls-api-ref`
- page_type: `leaf`
- content_type: `topic`
- source_description: This object is not available in the repository.

Topic Missing

This object is not available in the repository.

Parent topic:

Topic Missing

Parent topic:

Graphen und Diagramme

Related information:

- Erzeugen einer EXE-Datei aus Programmcode
- Erstellen einer Bibliothek

<!--NI_TOPIC bundle=labview-nxg-controls-api-ref path=layouts.html language=enus -->
## TOPIC 00011: Layouts

- bundle_id: `labview-nxg-controls-api-ref`
- source_path: `layouts.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-controls-api-ref/raw/resource/enus/layouts.html
- source_language: `enus`
- document_id: `labview-nxg-controls-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-controls-api-ref path=numerics.7.html language=enus -->
## TOPIC 00012: Numeric Controls

- bundle_id: `labview-nxg-controls-api-ref`
- source_path: `numerics.7.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-controls-api-ref/raw/resource/enus/numerics.7.html
- source_language: `enus`
- document_id: `labview-nxg-controls-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enter and display numeric data. Which Numeric Should I Use? Control Use Numeric control and indicator Enter or display numeric data. Slider Display numeric data in a vertical or horizontal slide with a customizable scale and a pointer that helps you see the exact value. Gauge, meter, and knob Enter

Numeric Controls

Enter and display numeric data.

[IMAGE alt='1378' src='GUID-74555973-64B7-4E3F-BEB9-6C5F34CC6707-a5.png']

#### Which Numeric Should I Use?

| Control | Use |
| --- | --- |
| Numeric control and indicator | Enter or display numeric data. |
| Slider | Display numeric data in a vertical or horizontal slide with a customizable scale and a pointer that helps you see the exact value. |
| Gauge, meter, and knob | Enter or display numeric data in a rotary scale. |
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

<!--NI_TOPIC bundle=labview-nxg-controls-api-ref path=selector-controls.4.html language=enus -->
## TOPIC 00013: Selector Controls

- bundle_id: `labview-nxg-controls-api-ref`
- source_path: `selector-controls.4.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-controls-api-ref/raw/resource/enus/selector-controls.4.html
- source_language: `enus`
- document_id: `labview-nxg-controls-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create a list that a user can cycle through to make selections. Types of Selector Controls Control Description Ring A ring control is a numeric input that presents a set of choices associated with numeric values. Enumerated type, or Enum The enum control is an object that presents a set of choices a

Selector Controls

Create a list that a user can cycle through to make selections.

[IMAGE alt='1378' src='GUID-8478A9F3-AA87-4ECC-8E3F-D0353E55DBEC-a5.png']

#### Types of Selector Controls

| Control | Description |
| --- | --- |
| Ring | A ring control is a numeric input that presents a set of choices associated with numeric values. |
| Enumerated type, or Enum | The enum control is an object that presents a set of choices associated with an enumerated data type. The enumerated data type consists of a set of named constants. |
| Radio Button Group | The radio button group control is an object that presents a set of mutually exclusive choices associated with an enumerated data type. The enumerated data type consists of a set of named constants. |
| Combo Box | The combo box control is an object that presents a list of names associated with string values. Users may select from items in a predefined list or enter new values directly, at edit time or run time. |
| Listbox | The listbox control is an object that presents a set of items. Users may select single or multiple items at run time. |
| Color Selector | The color selector control is an object that presents a color selection. Each color corresponds to RGBA color values or a hexadecimal value. |

#### Which Selector Control Should I Use?

Selector controls all contain a list of items from which the user can make a selection.

| Control | When to Use | Examples: E-Commerce Application |
| --- | --- | --- |
| Ring | Use a ring when you want to provide a list of choices that represent numeric values. The ring control is a numeric input that allows the user to choose from a list of meaningful, human-readable values instead of numeric values. If the logic of your program prefers numeric values to string values, use a ring. | You want to present users with a list of product names, each of which corresponds to a unique product number. You can specify the products' numbers as their respective numeric values. You can then cross-reference those numeric values to find the prices of the items. |
| Enum and Radio Button Group | Use an enum or a radio button group when you want to provide a list of choices associated with an enumerated data type. If you want your program to deal with a fixed set of constants instead of arbitrary numeric data, use an enum or radio button group. In general, use a radio button group when you have less than five options for the user to select from. A radio button group can help the user quickly scan the options. | You want to present users with a list of shipping speed options for the item they want to order. The numeric values assigned to each of the options are automatically defined. You cannot edit the numeric values. You can use the enumerated data type in the enum control to drive the logic of your program. For example, because the names of the choices are part of the data type, you can use them to populate the cases of a Case Structure. This ensures that only valid states are used in your program. Figure 1. Enum Figure 3. Radio Button Group |
| Combo Box | Use a combo box when you want to provide a list of items for users to cycle through while also providing the option to type new values into the menu at edit time or run time. If the logic of your program requires string values rather than numeric values, use a combo box. | You want to present users with a list of previous shipping addresses, while also allowing them to enter a new shipping address for this purchase. |
| Listbox | Use a listbox when you want to provide a list of items in which users can select items at run time. | You want to present users with a list of products in which they can select one or more items. You can also allow users to select zero items by checking the Allow no selection checkbox. For example, you can allow users to deselect all items. |

#### Assigning Specific Values to Selector Controls

Unlike the strings listed in rings, enums, and radio button groups, the strings listed in a combo box and listbox have no numeric representation. Additionally, enums and radio button groups require these numeric values to be sequential, unsigned integer values, while rings allow for much more freedom in assigning a numeric value.

1. Select the control to which you want to assign specific values.
2. On the 
 Item tab, in the 
 Items group, assign and arrange specific values as desired.

#### Enabling a Combo Box to Accept New Values from the User at Edit Time or Run Time

1. Select the combo box control.
2. On the 
 Item tab, in the 
 Items group, select 
 Allow entry of unlabeled values .

<!--NI_TOPIC bundle=labview-nxg-controls-api-ref path=text-controls.3.html language=enus -->
## TOPIC 00014: Text Controls

- bundle_id: `labview-nxg-controls-api-ref`
- source_path: `text-controls.3.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-controls-api-ref/raw/resource/enus/text-controls.3.html
- source_language: `enus`
- document_id: `labview-nxg-controls-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create text entry boxes and labels or enter or return the location of a file or directory. Which Text Control Should I Use? Use Control Enter string data. String Control Display string data. String Indicator Enter the location of a file or directory. Path Control Display the location of a file or di

Text Controls

Create text entry boxes and labels or enter or return the location of a file or directory.

[IMAGE alt='1378' src='GUID-0EA6EEA1-3393-4B2A-BAFD-9A84FFE65F68-a5.png']

#### Which Text Control Should I Use?

| Use | Control |
| --- | --- |
| Enter string data. | String Control |
| Display string data. | String Indicator |
| Enter the location of a file or directory. | Path Control |
| Display the location of a file or directory. | Path Indicator |
| Create free floating text that you can use as a label or annotation. | Text |
| Enter or display a URL hyperlink. | Hyperlink Control |
| Enter string data in masked display. | Masked Input Control Note This control only masks the text visually. When you read the string data from the diagram, you read the actual data the user entered. Any mechanism that can examine the memory of the program can also read the actual data. |

#### When Does My Entered Text Pass to the Diagram?

By default, new or changed text does not pass to the diagram until you terminate the edit session by clicking elsewhere on the panel or by pressing Ctrl-Enter.

You can change the behavior of the Enter key for a String control by clicking the control on the panel and selecting a new 
 Enter key behavior in the 
 Item tab.

| Option | Behavior |
| --- | --- |
| Commits text | Pressing Enter terminates the edit session. You can also terminate the edit session by clicking elsewhere on the panel. Carriage returns are not allowed. |
| Enters new line (default) | Pressing Enter inserts a carriage return. You can terminate the edit session by clicking elsewhere on the panel or pressing Ctrl-Enter. |

#### Should I Use an Absolute or Relative Path?

If possible, use a relative path. A relative path describes the location of a file or directory relative to an arbitrary location in the file system. By using a relative path, you avoid having to rework the paths if you build an application or run the code on a different computer.

<!--NI_TOPIC bundle=labview-nxg-controls-api-ref path=tree-control.html language=enus -->
## TOPIC 00015: Tree

- bundle_id: `labview-nxg-controls-api-ref`
- source_path: `tree-control.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-controls-api-ref/raw/resource/enus/tree-control.html
- source_language: `enus`
- document_id: `labview-nxg-controls-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Group string data as a hierarchical list of items in multiple columns. The tree control is a 1D array of clusters. Each row of the tree is one cluster. The first element in the row represents the hierarchical location of the item in the tree, and subsequent elements represent data to display in each

Tree

Group string data as a hierarchical list of items in multiple columns.

The tree control is a 1D array of clusters. Each row of the tree is one cluster. The first element in the row represents the hierarchical location of the item in the tree, and subsequent elements represent data to display in each column of the tree.

Use tree properties to write the column header or read and write selected items of the tree control.

[IMAGE alt='1378' src='GUID-FFBC1FA4-4F9F-48A5-9C84-4ECDE63E95E3-a5.png']

#### How Do I Select Items in a Tree?

You can allow your users to select one or multiple items in the tree by placing a checkmark in the 
 Allow selection checkbox on the 
 Item tab. Use the Selection property to return information about the selected item(s).

#### How Do I Define the Hierarchy of a Tree?

You populate items in a tree using an array of clusters, as shown in the following figure.

[IMAGE alt='1378' src='GUID-36550D72-2847-4334-B64D-E2C77411AE0B-a5.png']

The first element of each cluster is the hierarchical location of the item. The hierarchical location is a backslash-delimited string, where each segment of the delimited string denotes a level of hierarchy in the tree. Use the following general syntax to define a hierarchical location:

| Syntax | Definition |
| --- | --- |
| <empty string> or \\ | An empty string or backslash represents the root of the tree. |
| \\parent\\child or parent\\child | A leading backslash is equivalent to a location in the tree without a leading backslash. |
| parent\\child\\ or parent\\child | A trailing backslash is equivalent to a location in the tree without a trailing backslash. |
| Escape sequence or double backslash | Escape sequences for character representations, such as \\s to represent a space character, are not permitted. |

Parent topic:

Array Controls
