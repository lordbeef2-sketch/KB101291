# NI DOCUMENT BUNDLE: labview-nxg-nodes-api-ref

<!--NI_BUNDLE_CHUNK bundle=labview-nxg-nodes-api-ref start=1 end=250 -->
<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=1d-array-constant.html language=enus -->
## TOPIC 00001: Array Constant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `1d-array-constant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/1d-array-constant.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=abort-vi.html language=enus -->
## TOPIC 00002: Abort VI

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `abort-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/abort-vi.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `lvFunction`
- source_description: Stops the execution of a VI. reference in A reference to a VI. Use Open VI Reference or Static VI Reference to obtain a valid reference for this input. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. No error Standard

Abort VI

Stops the execution of a VI.

[IMAGE alt='connector_pane_image' src='AbortVI.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

#### reference in

A reference to a VI.

Use Open VI Reference or Static VI Reference to obtain a valid reference for this input.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

#### reference out

Unchanged reference to the same VI.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Executing this node on a VI is similar to pressing the 
 Abort button.

The node produces this output according to standard error behavior.

This node can return the following error codes.

| 1000 | This node is called on a subVI. You must call a VI from this node. |
| --- | --- |

Note

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

Execution Control

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=absolute-value.html language=enus -->
## TOPIC 00003: Absolute Value

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `absolute-value.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/absolute-value.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=acquire-device.html language=enus -->
## TOPIC 00004: Acquire Device

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `acquire-device.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/acquire-device.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Returns data about the device connected to the computer. Wire Initialize Device to this node to specify the device data you want to acquire. keyboard in Reference to the keyboard connected to the computer. 0 joystick in Reference to the joystick connected to the computer. This input only appears aft

Acquire Device

Returns data about the device connected to the computer.

###### Programming Patterns

Wire Initialize Device to this node to specify the device data you want to acquire.

[IMAGE alt='connector_pane_image' src='Acquire_Keyboard.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### keyboard in

Reference to the keyboard connected to the computer.

**Default:**0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### joystick in

Reference to the joystick connected to the computer.

This input only appears after you set the 
 Function Configuration of the Initialize Device node to 
 Joystick and wire the **joystick** output of Initialize Joystick to **keyboard in**.

**Default:**0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### mouse in

Reference to the mouse connected to the computer.

This input only appears after you set theFunction Configuration of the Initialize Device node to 
 Mouse and wire the **mouse** output of Initialize Mouse to **keyboard in**.

**Default:**0

[IMAGE alt='datatype_icon' src='/assets/img/cenum.png']

#### key mode

Defines the mouse coordinates in **axis info**.

This input only appears after you set the 
 Function Configuration of the Initialize Device node to 
 Mouse and wire the **mouse** output of Initialize Mouse to **keyboard in**.

| Name | Description |
| --- | --- |
| Relative | Defines the mouse coordinates (axis info) as relative to the last time you called the node. |
| Absolute | Defines the mouse coordinates (axis info) as absolute coordinates relative to the upper left hand corner of the screen. |

**Default:**Absolute

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

#### keyboard out

Reference to the keyboard connected to the computer.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

#### joystick out

Reference to the joystick connected to the computer.

This output only appears after you set the 
 Function Configuration of the Initialize Device node to 
 Joystick and wire the **joystick** output of Initialize Joystick to **keyboard in**.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

#### mouse out

Reference to the mouse connected to the computer.

This output only appears after you set the 
 Function Configuration of the Initialize Device node to 
 Mouse and wire the **mouse** output of Initialize Mouse to **keyboard in**.

[IMAGE alt='datatype_icon' src='/assets/img/i1du16.png']

#### keys pressed

Numeric that provides information about which keys are pressed when the node runs and only returns values associated with US keyboards.

This output only appears after you set the 
 Function Configuration of the Initialize Device node to 
 Keyboard and wire the **keyboard** output of Initialize Keyboard to **keyboard in**.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

#### axis info

Numeric values for the axes. The axis information you have access to varies depending on the device connected to the computer.

This output only appears after you set the 
 Function Configuration of the Initialize Device node to 
 Mouse or 
 Joystick and wire the **mouse** or **joystick** output of Initialize Mouse or Initialize Joystick to **keyboard in**.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### Horizontal

Numeric value of the horizontal axis.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### X axis

Numeric value of the x-axis.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### Vertical

Numeric value of the vertical axis.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### Y axis

Numeric value of the y-axis.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### Scrolling

Numeric value of the scrolling axis if the mouse supports scrolling.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### Z axis

Numeric value of the z-axis.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### X axis rotation

Numeric value of the x-axis rotation.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### Y axis rotation

Numeric value of the y-axis rotation.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### Z axis rotation

Numeric value of the z-axis rotation.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### U axis

Numeric value of the u-axis.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### V axis

Numeric value for the v-axis.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

#### button info

Cluster that contains Boolean values for buttons. The number of buttons you have access to depends on the device connected to the computer and displays up to four buttons for a mouse and 32 buttons for a joystick.

This output only appears after you set the 
 Function Configuration of the Initialize Device node to 
 Mouse or 
 Joystick and wire the **mouse** or **Joystick** output of Initialize Mouse or Initialize Joystick to **keyboard in**.

| True | Button is activated. |
| --- | --- |
| False | Button is not activated. |

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

#### direction info

Numeric values for up to four directions in which you move your joystick.

This output only appears after you set theFunction Configuration of the Initialize Device node to 
 Joystick and wire the **joystick** output of Initialize Joystick to **keyboard in**.

Parent topic:

Input Device Control Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=add-array-elements.html language=enus -->
## TOPIC 00005: Add Array Elements

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `add-array-elements.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/add-array-elements.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=add-header.html language=enus -->
## TOPIC 00006: Add Header

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `add-header.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/add-header.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a header field line to future web requests associated with the client handle. Headers define attributes of the data exchanged between the client and server. client handle Unique value that identifies the web request. You can use the same client handle to wire together multiple HTTP nodes to pre

Add Header

Adds a header field line to future web requests associated with the client handle.
 Headers define attributes of the data exchanged between the client and server.

[IMAGE alt='1378' src='Add_Header.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### client handle

Unique value that identifies the web request.

You can use the same client handle to wire together multiple HTTP nodes to preserve authentication credentials, HTTP headers, and cookies.

Client handles are not required when making web requests without persistent data such as headers or credentials.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### header

Header field that adds all web requests associated with the client handle. The header input provides a pull-down menu with available header fields.

If you specify aheader that already exists, the specified value overwrites the header value.

[IMAGE alt='datatype_icon' src='/assets/img/c1dstr.png']

##### value

Value to assign to the header field.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### client handle out

Unique value that identifies the web request. Use this value to refer to this web request in subsequent node calls.

You can use the same client handle to wire together multiple HTTP nodes to preserve authentication credentials, HTTP headers, and cookies.

Client handles are not required when making independent web requests without persistent data such as headers or credentials.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

HTTP Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=add.html language=enus -->
## TOPIC 00007: Add

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `add.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/add.html
- document_id: `labview-nxg-nodes-api-ref`
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

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.DITA)

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### sum

The sum of the inputs.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

The node produces this output according to standard error behavior.

This output appears only when you wire a waveform to input.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.DITA)

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=align-waveform-timestamps.html language=enus -->
## TOPIC 00008: Align Waveform Timestamps

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `align-waveform-timestamps.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/align-waveform-timestamps.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Replaces the timestamp value (t0) of each waveform in waveform array with the timestamp value of the waveform at the index position you specify. waveforms in Waveform array in which the node replaces the specific value of each element with the corresponding value of the waveform at the index you spe

Align Waveform Timestamps

Replaces the timestamp value (t0) of each waveform in waveform array with the timestamp value of the waveform at the index position you specify.

[IMAGE alt='1378' src='WDT_Align_Waveform_Timestamps_DBL.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1dmsdt.png']

##### waveforms in

Waveform array in which the node replaces the specific value of each element with the corresponding value of the waveform at the index you specify.

This input accepts a 1D array of waveforms or 1D array of digital waveforms.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### index

Specifier of the waveform in the waveform array from which the node obtains the replacement value.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/i1dmsdt.png']

##### waveforms out

Waveform array in which the timestamp values of all waveforms are identical.

This output is a digital waveform array when you wire a digital waveform array to waveforms in.

Parent topic:

Waveform Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=and-array-elements.html language=enus -->
## TOPIC 00009: AND Array Elements

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `and-array-elements.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/and-array-elements.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns True if all the elements in the input array are True or if the array is empty. Otherwise, this node returns False. This node accepts an array of any size but returns only a single value based on all values in the input array. array Array of Boolean elements. logical AND A Boolean value that

AND Array Elements

Returns True if all the elements in the input array are True or if the array is empty. Otherwise, this node returns False.
 This node accepts an array of any size but returns only a single value based on all values in the input array.

[IMAGE alt='1378' src='AndArrayElements.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1dbool.png']

##### array

Array of Boolean elements.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### logical AND

A Boolean value that indicates whether all of the elements in array are True.

| True | All the elements in array are True, or the array is empty. |
| --- | --- |
| False | One or more elements in array are False. |

Parent topic:

Boolean Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=and.html language=enus -->
## TOPIC 00010: AND

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `and.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/and.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the logical AND of the inputs. If all inputs are True, this node returns True. Otherwise, it returns False. This node performs bitwise operations on numeric inputs. input An input to the operation. This input can be any data type that contains only Boolean values, numbers, or error clusters

AND

Computes the logical AND of the inputs. If all inputs are True, this node returns True. Otherwise, it returns False.

This node performs bitwise operations on numeric inputs.

[IMAGE alt='1378' src='LogicalAnd.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### input

An input to the operation.

This input can be any data type that contains only Boolean values, numbers, or error clusters, such as an array of numbers or a cluster of Booleans. If this input is an error cluster, the node uses only the 
 status element of the error cluster.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### logical AND

The logical AND of the inputs.

#### Examples

| input 0 | input 1 | logical AND |
| --- | --- | --- |
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

Parent topic:

Boolean Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=append-true-false-string.html language=enus -->
## TOPIC 00011: Append True Or False String

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `append-true-false-string.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/append-true-false-string.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Appends one of two possible strings, determined by a Boolean value, to another string you specify. string The string to which you want to concatenate another string. Default value: Empty string true string The string you want to concatenate to string if selector is True. false string The string you

Append True Or False String

Appends one of two possible strings, determined by a Boolean value, to another string you specify.

[IMAGE alt='1378' src='Append_True_Or_False_String.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### string

The string to which you want to concatenate another string.

Default value: Empty string

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### true string

The string you want to concatenate to 
string if 
selector is True.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### false string

The string you want to concatenate to 
string if 
selector is False.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### selector

Boolean value that determines the string to concatenate to 
string.

| True | Appends true string. |
| --- | --- |
| False | Appends false string. |

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### output string

The resulting string after the node concatenates either 
true string or 
false string to 
string.

Parent topic:

String Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=array-max-and-min.html language=enus -->
## TOPIC 00012: Array Max and Min

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `array-max-and-min.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/array-max-and-min.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=array-nodes.html language=enus -->
## TOPIC 00013: Array Nodes

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `array-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/array-nodes.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=array-size.html language=enus -->
## TOPIC 00014: Array Size

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `array-size.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/array-size.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=array-subset.html language=enus -->
## TOPIC 00015: Array Subset

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `array-subset.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/array-subset.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=array-to-cluster.html language=enus -->
## TOPIC 00016: Array to Cluster

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `array-to-cluster.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/array-to-cluster.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a 1D array to a cluster of elements of the same type as the array elements. The maximum cluster size for this node is 256. To change the number of elements in the converted cluster, click Array to Cluster and enter the cluster size you want into the Cluster Size field in the Behavior sectio

Array to Cluster

Converts a 1D array to a cluster of elements of the same type as the array elements.

The maximum cluster size for this node is 256. To change the number of elements in the converted cluster, click Array to Cluster and enter the cluster size you want into the 
 Cluster Size field in the 
 Behavior section of the 
 **Item** tab.

[IMAGE alt='1378' src='ArrayToCluster.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### array

A 1D array of any type.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### cluster

The resulting cluster. Each element in the cluster is the same data type and order as the elements in array.

Default value: A cluster of nine elements

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=avogadro.html language=enus -->
## TOPIC 00017: Avogadro Constant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `avogadro.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/avogadro.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value 6.022140857e23. The Avogadro constant is the number of constituent particles, usually atoms or molecules, that are contained in the amount of substance given by one mole.

Avogadro Constant

Returns the value 6.022140857e23. The Avogadro constant is the number of constituent particles, usually atoms or molecules, that are contained in the amount of substance given by one mole.

[IMAGE alt='1378' src='Literal.Numeric.Avogadro_Constant.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=boolean-array-to-number.html language=enus -->
## TOPIC 00018: Boolean Array to Number

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `boolean-array-to-number.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/boolean-array-to-number.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=boolean-constant.html language=enus -->
## TOPIC 00019: Boolean (True or False) Constant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `boolean-constant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/boolean-constant.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a True or False value on the diagram.

Boolean (True or False) Constant

Represents a True or False value on the diagram.

[IMAGE alt='1378' src='Literal.Boolean.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=boolean-nodes.html language=enus -->
## TOPIC 00020: Boolean Nodes

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `boolean-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/boolean-nodes.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`

Boolean Nodes

AND

Computes the logical AND of the inputs. If all inputs are True, this node returns True. Otherwise, it returns False.

AND Array Elements

Returns True if all the elements in the input array are True or if the array is empty. Otherwise, this node returns False.

EXCLUSIVE OR

Computes the logical exclusive or (XOR) of the inputs. If all inputs are True or all inputs are False, this node returns False. Otherwise, it returns True.

Implies

Negates the first input and then computes the logical OR of the second input and the negated input.

NOT

Computes the logical negation of the input. If the input is False, this node returns True. If the input is True, this node returns False.

NOT AND

Computes the logical NAND of the inputs. If all inputs are True, this node returns False. Otherwise, it returns True.

NOT EXCLUSIVE OR

Computes the logical negation of the logical exclusive or (XOR) of the inputs. If all inputs are True or all inputs are False, this node returns True. Otherwise, it returns False.

NOT OR

Computes the logical NOR of the inputs. If all inputs are False, this node returns True. Otherwise, it returns False.

OR

Computes the logical OR of the inputs. If all inputs are False, this node returns False. Otherwise, it returns True.

OR Array Elements

Returns False if all the elements in the input array are False or if the array is empty. Otherwise, this node returns True.

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=boolean-to-integer.html language=enus -->
## TOPIC 00021: Boolean to Integer

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `boolean-to-integer.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/boolean-to-integer.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a Boolean False or True value to a 16-bit integer with a value of 0 or 1, respectively. boolean A scalar, an array, a cluster of Boolean values, an array of clusters of Boolean values, and so on. 0, 1 0 if Boolean is False and 1 if Boolean is True.

Boolean to Integer

Converts a Boolean False or True value to a 16-bit integer with a value of 0 or 1, respectively.

[IMAGE alt='1378' src='BooleanTo0Or1.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### boolean

A scalar, an array, a cluster of Boolean values, an array of clusters of Boolean values, and so on.

[IMAGE alt='datatype_icon' src='/assets/img/ii16.png']

##### 0, 1

0 if 
Boolean is False and 1 if 
Boolean is True.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=build-array.html language=enus -->
## TOPIC 00022: Build Array

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `build-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/build-array.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Concatenates multiple arrays or appends elements to an n-dimensional array. This node constructs the new array differently depending on the dimensionality of the inputs and whether the Concatenate Inputs option is enabled in the Item tab. The following table shows the behavior for Build Array for va

Build Array

Concatenates multiple arrays or appends elements to an 
*n*-dimensional array.

This node constructs the new array differently depending on the dimensionality of the inputs and whether the 
 Concatenate Inputs option is enabled in the 
 **Item** tab. The following table shows the behavior for Build Array for various inputs and configurations.

| Inputs | Concatenate Inputs Option | Behavior | Dimensionality of Output |
| --- | --- | --- | --- |
| Arrays of the same dimension | Concatenate Inputs disabled |  | n+1 |
| Arrays of the same dimension | Concatenate Inputs enabled |  | n |
| An array and a scalar of different dimensions | Concatenate Inputs enabled |  | n |

[IMAGE alt='1378' src='BuildArray.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### element

Any 
n-dimensional array or scalar element. All inputs must be the same base type.

##### Behavior with Empty Array Inputs

If element is an empty array, this node produces an output array of dimension n+1 if the 
 Concatenate Inputs option is not selected. If the 
 Concatenate Inputs option is selected, this node produces an output array of the same dimension as the empty element array.

##### Different Sized Input Arrays

This node displays the following behavior when inputs of the same dimension contain a different number of elements:

- By default, this node pads the smallest input to match the size of the largest input. For example, if element is {1, 2} and element 2 is {3, 4, 5}, Build Array pads element with a trailing 0 and returns {{1, 2, 0}, {3, 4, 5}}.
- If the 
 Concatenate Inputs option is enabled, this node does not pad inputs. For example, if element is {1, 2} and element 2 is {3, 4, 5}, Build array returns {1, 2, 3, 4, 5} without padding.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### appended array

The resulting array.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

##### Concatenate Inputs

Append all inputs in order, forming an output array of the same dimensionality as the array input wired. This option is not available for scalars.

#### Examples

Build Array

Concatenate Inputs

| Inputs | Build Array Default | Concatenate Inputs | Comments |  |
| --- | --- | --- | --- | --- |
| {1, 2} | {3, 4} | {{1, 2}, {3, 4}} | {1, 2, 3, 4} | Because both input arrays are of the same dimension, you can choose which configuration option to use. |
| {1, 2} | {3, 4, 5} | {{1, 2, 0}, {3, 4, 5}} | {1, 2, 3, 4, 5} | Because both input arrays are of the same dimension, you can choose which configuration option to use. By default, this node appends an extra 0 of padding to the first input array in order to make it the same length as the second input. No padding appears for the Concatenate Inputs option. |
| {1, 2} | 3 | N/A | {1, 2, 3} | If the inputs are of different dimensions, Concatenate Inputs is enabled automatically and cannot be disabled. appended array returns the input elements in order, regardless of which has the highest dimension. |
| 3 | {1, 2} | N/A | {3, 1, 2} | If the inputs are of different dimensions, Concatenate Inputs is enabled automatically and cannot be disabled. appended array returns the input elements in order, regardless of which has the highest dimension. |

#### Concatenating Elements

When all element inputs have the same dimension, you can select the 
 Concatenate Inputs option in the 
 Item tab to append all inputs in order, forming an output array of the same dimensionality as the array input wired. This option is not available for scalars. If element inputs have different dimensions, 
 Concatenate Inputs is enabled automatically and cannot be disabled.

#### Building Multidimensional Arrays

element

Build Array

element

n

Note

Build Array

Concatenate Inputs

Parent topic:

Array Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=build-cluster-array.html language=enus -->
## TOPIC 00023: Build Cluster Array

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `build-cluster-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/build-cluster-array.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an array of clusters where each cluster contains an array as its only element. This node provides a way to create a jagged array. You cannot otherwise create an array of arrays. element An array that you want to store as an element within a cluster. created cluster array An array of clusters

Build Cluster Array

Creates an array of clusters where each cluster contains an array as its only element.
 
 This node provides a way to create a jagged array. You cannot otherwise create an array of arrays.

[IMAGE alt='1378' src='BuildClusterArray.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### element

An array that you want to store as an element within a cluster.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### created cluster array

An array of clusters in which each cluster contains a single input array.

#### Examples

#### Illustration of Behavior

[IMAGE alt='1378' src='GUID-6A7A2607-D4DF-4407-B4C4-01ED5AFEEC7E-a5.png']

Parent topic:

Cluster Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=build-cluster.html language=enus -->
## TOPIC 00024: Build Cluster

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `build-cluster.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/build-cluster.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new cluster from individual elements. element Element you want to add to the cluster. This input can be any data type. Resize the node to add more elements to the cluster. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this input has a default data type

Build Cluster

Creates a new cluster from individual elements.

[IMAGE alt='1378' src='BuildCluster.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### element

Element you want to add to the cluster.

This input can be any data type. Resize the node to add more elements to the cluster.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### created cluster

A cluster that contains an element for each input.

The elements in this cluster appear in the same order as the input elements.

Parent topic:

Cluster Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=build-error-cluster.html language=enus -->
## TOPIC 00025: Build Error Cluster

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `build-error-cluster.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/build-error-cluster.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=build-matrix.html language=enus -->
## TOPIC 00026: Build Matrix

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `build-matrix.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/build-matrix.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `lvFunction`
- source_description: Appends elements to a matrix by rows or columns. To add one or more elements to a matrix at a specific location, use Set Matrix Elements. To add a submatrix to a matrix at a specific location, use Set Submatrix. Appending by Rows or Columns Build Matrix has two modes: Append by columns or Append by

Build Matrix

Appends elements to a matrix by rows or columns.

###### Programming Patterns

To add one or more elements to a matrix at a specific location, use Set Matrix Elements. To add a submatrix to a matrix at a specific location, use Set Submatrix.

[IMAGE alt='connector_pane_image' src='BuildMatrix.png']

- Inputs/Outputs
- Details
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

#### element

Numeric scalar or a 1D or 2D array of any numeric type.

To add additional **element** inputs, resize the node.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

#### appended matrix

The resulting matrix.

#### Appending by Rows or Columns

Build Matrix has two modes: 
 Append by columns or 
 Append by rows. The default mode is 
 Append by columns.

Right-click the node and select 
 Build matrix mode»Append by rows to add a new element or matrix to the last row starting in the first column. Right-click the node and select 
 Build matrix mode»Append by columns to add a new element or matrix to the last column starting in the first row.

#### Wiring Empty Input Values

If **element** is an empty array, this node ignores the empty dimensions.

#### Wiring Inputs of Different Numeric Types or Dimensions

The dimensions and data type of **appended matrix** match those of the **element** input with the highest dimension and most precise data type. For example, if you wire a 1D array of numeric double to **element 0** and a 2D array of complex double to **element 1**, additional inputs and outputs default or coerce to 2D arrays of complex double.

When you wire inputs with different dimensions to Build Matrix, this node creates **appended matrix** by padding the smaller input with the scalar default value (0).

Parent topic:

Matrix Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=busy-state-nodes.html language=enus -->
## TOPIC 00027: Busy State Nodes

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `busy-state-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/busy-state-nodes.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=byte-array-to-string.html language=enus -->
## TOPIC 00028: Byte Array To String

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `byte-array-to-string.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/byte-array-to-string.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts an array of unsigned bytes representing encoded characters into a string using the encoding you specify. encoding The character encoding the node uses to convert the input. UTF-8 Converts the input using UTF-8 encoding. UTF-16 Converts the input using UTF-16 encoding. Extended ASCII Convert

Byte Array To String

Converts an array of unsigned bytes representing encoded characters into a string using the encoding you specify.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### encoding

The character encoding the node uses to convert the input.

| UTF-8 | Converts the input using UTF-8 encoding. |
| --- | --- |
| UTF-16 | Converts the input using UTF-16 encoding. |
| Extended ASCII | Converts the input using extended ASCII encoding. |

[IMAGE alt='datatype_icon' src='/assets/img/c1du8.png']

##### unsigned byte array

Array of values you want the node to convert.

Each element in the array represents a single character code.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Default value: No error

Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### string

Result of interpreting each array element as an encoded character and forming a string out of those characters.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=call-by-reference.html language=enus -->
## TOPIC 00029: Call by Reference

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `call-by-reference.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/call-by-reference.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `lvFunction`
- source_description: Calls the VI to which a strictly typed VI reference refers. Like most diagram objects, Call by Reference executes synchronously, preventing data flow from continuing along its output wires until the referenced VI finishes executing. To run the referenced VI asynchronously while the diagram beyond th

Call by Reference

Calls the VI to which a strictly typed VI reference refers. Like most diagram objects, Call by Reference executes synchronously, preventing data flow from continuing along its output wires until the referenced VI finishes executing. To run the referenced VI asynchronously while the diagram beyond the VI call continues executing, use Start Asynchronous Call instead.

[IMAGE alt='connector_pane_image' src='CallByReference.png']

- Inputs/Outputs
- Details
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

#### reference in

The reference associated with a VI that is already open. The reference must be a strictly typed VI reference.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

#### reference out

Unchanged reference associated with the strictly typed VI reference.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

#### Using a VI Reference Instead of a SubVI

Call by Reference

Call by Reference

Open VI Reference

Static VI Reference

#### Accessing Inputs and Outputs of the Referenced VI

When you wire a strictly typed VI reference to the **reference in** input of Call by Reference, the node automatically displays the input and output parameters of the referenced VI. Wire data to the input terminals of Call by Reference to pass the data to the referenced VI. Use the output terminals of Call by Reference to access the data that the referenced VI returns.

Parent topic:

Execution Control

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=call-chain.html language=enus -->
## TOPIC 00030: Call Chain

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `call-chain.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/call-chain.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of every VI that calls this node, from the current VI to the top-level VI. The first element of the output array is the VI that calls this node. Subsequent elements in the output array are VIs that call the VI in the previous element. The last element of the output array is the name

Call Chain

Returns an array of every VI that calls this node, from the current VI to the top-level VI.

The first element of the output array is the VI that calls this node. Subsequent elements in the output array are VIs that call the VI in the previous element. The last element of the output array is the name of the top-level VI.

If the current VI is a subVI, use this node to identify all the VIs that call the subVI.

[IMAGE alt='1378' src='CallChain.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/i1dstr.png']

##### call chain

The chain of calling VIs from the current VI to the top-level VI.

#### An Alternative Tool for Identifying Call Chains

You can also view the chain of callers from a subVI up to the top-level VI in the 
 Call Stack section of the 
 Debugging tab. The 
 Call Stack list populates when you pause a VI that is called in other VIs.

#### Call Chain Behavior for a VI that Is Part of a Component

If a VI in the call chain belongs to a component, this node returns the qualified name of the VI, which includes the component namespace.

Parent topic:

Program Flow Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=call-parent-method.html language=enus -->
## TOPIC 00031: Call Parent Method (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `call-parent-method.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/call-parent-method.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `lvFunction`
- source_description: Calls the implementation of a dynamic dispatch member VI in the nearest parent class in the inheritance hierarchy. You can only use this node on the diagram of a VI on the member list of a class that inherits from a parent class. The VI in the child class must be a dynamic dispatch VI and have the s

Call Parent Method

Calls the implementation of a dynamic dispatch member VI in the nearest parent class in the inheritance hierarchy.

You can only use this node on the diagram of a VI on the member list of a class that inherits from a parent class. The VI in the child class must be a dynamic dispatch VI and have the same name as a VI on the parent class member list. The inputs, outputs, and icon of this node change to match the parent member VI exactly.

[IMAGE alt='connector_pane_image' src='CallParentMethod.png']

- Compatibility

**Where This Node Can Run:**

Desktop OS: Windows

FPGA:

Web Server:

Parent topic:

Classes Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=call-python.html language=enus -->
## TOPIC 00032: Call Python Function (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `call-python.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/call-python.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Calls a function within a Python file and returns the output. The input and output section of Call Python Function is expandable. Supported Data TypesCall Python Function supports the following data types: Single-precision, floating point numbers Double-precision, floating point numbers Integers Str

Call Python Function

Calls a function within a Python file and returns the output.

Note

Call Python Function

[IMAGE alt='connector_pane_image' src='CallPythonFunction.png']

- Inputs/Outputs
- Details
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

#### session in

Reference to the Python session.

[IMAGE alt='datatype_icon' src='/assets/img/cpath.png']

#### module path

Absolute path to the Python module.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

#### function name

Name of the function within the module you want to call.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### return type

Data type to return from the Python function.

Note

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

#### input

Value to pass to an argument of the Python function specified by the
 **function name** input.

Note

Input

output

Supported Data Types

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

#### session out

Reference to the Python session.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

#### return value

Data the Python function returns.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

#### output

Value Python returns after passing an input argument to a function
 parameter.

Note

Input

output

Supported Data Types

#### Supported
 Data Types

Call Python Function

- Single-precision, floating point numbers
- Double-precision, floating point numbers
- Integers
- Strings
- Arrays
- Clusters
- Booleans

Complex and fixed-point numbers are not supported.

Python
 interprets LabVIEW NXG arrays as lists by default. Right-click an input to
 enable marshaling to NumPy arrays.

Python interprets LabVIEW NXG clusters
 as tuples.

**Where This Node Can Run:**

Desktop OS: Windows

FPGA:

Web Server:

Parent topic:

Python Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=carriage-return-constant.html language=enus -->
## TOPIC 00033: Carriage Return Constant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `carriage-return-constant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/carriage-return-constant.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=case-structure.html language=enus -->
## TOPIC 00034: Case Structure

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `case-structure.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/case-structure.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains one or more subdiagrams, or cases, exactly one of which executes when the structure executes. The value wired to the selector terminal determines which case to execute. Case Structures behave similarly to switch statements or if-then-else statements in other programming languages. Selector

Case Structure

Contains one or more subdiagrams, or cases, exactly one of which executes when the structure executes.

The value wired to the selector terminal determines which case to execute.

Case Structures behave similarly to 
 switch statements or 
 if-then-else statements in other programming languages.

#### Inputs/Outputs

##### Selector

Value that determines which case to execute based on the input data.The input data can be a Boolean, string, integer, enumerated type, or error cluster. The data type you wire to the selector terminal determines what cases you can enter in the case selector label.

[IMAGE alt='1378' src='GUID-82A59452-D975-423B-AA71-ACC36FE189C3-a5.png']

##### Case Selector Label

Part of the structure that displays the value(s) for which the associated case executes.

You can specify a single value or a range of values.
 You can also use the case selector label to specify a default case.

[IMAGE alt='1378' src='GUID-58FF114D-8475-4BA5-8B48-50364AD09CA7-a5.png']

##### Tunnel

Point through which data enters or exits a structure.

[IMAGE alt='1378' src='GUID-43DB7847-2DDA-4B38-86E0-27BE4951A189-a5.png']

[IMAGE alt='1378' src='GUID-5871E10B-89AC-4323-A1DB-8A6B79D3A4E0-a5.png']

#### Programming Patterns

- Executing Code Based on a Condition

#### Matching
 Cases from the Items in a Control

Case
 Structure

| Input Data Type | What Value do Cases Match? | Comments |
| --- | --- | --- |
| Ring | Cases match the numeric values of items in the control rather than the string values. | The Case Structure treats values from a ring control identically to a numeric control. |
| Enum | Cases match the string values of items in the control rather than the numeric values. | By default, an enum auto-populates the case selector label with the first two values from the items in the control. To create a case for every item in an enum control, right click the Case Structure and select Cases » Create Case for Every Value. |
| Combo Box | Cases match the string values of items in the control. | The Case Structure treats values from a combo box identically to values of a string control. |

#### Entering Values in the Case Selector Label

You can enter a single value or lists and ranges of values in the case selector label of a Case Structure, as shown in the following table.

| Type of Values | Description |
| --- | --- |
| Numeric ranges | Specify a range as 10..20, meaning all numbers from 10 to 20 inclusively. |
| Open-ended numeric ranges | Specify a range as ..100, meaning all numbers less than or equal to 100, or 100.., meaning all numbers greater than or equal to 100. |
| Lists and ranges | Use commas to separate values, for example ..5, 6, 7..10, 12, 13, 14. |
| String ranges | A range of a..c includes all strings beginning with a or b, but not c. If you want a case to execute for all strings beginning with a, b, and c, define the range as "a".."c", "c". String ranges are case-sensitive by default. For example, a range of "A".."c" matches a different set of strings than "a".."c" because this structure uses code point values to determine a string range. In code point values, all capital letters have a lower numeric representation than all lower-case letters, so "A".."c" matches strings beginning with all capital letters A through Z, as well as lower case a and lower case b. A string value accepts the following backslash codes for non-alphanumeric characters: \\r for a carriage return, \\n for a line feed, \\t for a tab, and \\s for a space. |
| Enumerated values | The values display in quotation marks, for example "red", "green", and "blue". However, you do not need to type the quotation marks when you enter the values unless the string or enumerated value contains a comma or range symbol ("," or ".."). A string value accepts the following backslash codes for non-alphanumeric characters: \\r for a carriage return, \\n for a line feed, \\t for a tab, and \\s for a space. |

#### Case Sensitivity in Strings

By default, string values in the case selector label are case-sensitive. You can disable case sensitivity by right-clicking the Case Structure and selecting 
 Case Insensitive Match.

#### Requirements for Undefined Cases

An edit-time error occurs when there are values of the selector data type that do not correspond to any subdiagram in the Case Structure. You must either define a default case to handle out-of-range values or create a case for every possible input value. For example, if the selector is an integer data type and you specify cases for 1, 2, and 3, you must specify a default case to execute if the input value is 4 or any other unspecified integer value.

#### Troubleshooting an Unexpected Execution of the Default Case

If the default case executes unexpectedly, verify that the input values wired to the selector terminal match the values in the case selector label exactly.

Parent topic:

Program Flow Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=check-for-contained-data-type.html language=enus -->
## TOPIC 00035: Check for Contained Data Type

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `check-for-contained-data-type.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/check-for-contained-data-type.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Checks whether a variant contains the data type you specify. variant Variant data from which you want to retrieve data type information. data type to find Data type you want to find in the variant. check inside refnums A Boolean value that determines whether this node searches any refnums in the var

Check for Contained Data Type

Checks whether a variant contains the data type you specify.

[IMAGE alt='connector_pane_image' src='Check_for_Contained_Data_Type.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cfxdt.png']

#### variant

Variant data from which you want to retrieve data type information.

[IMAGE alt='datatype_icon' src='/assets/img/cu8.png']

#### data type to find

Data type you want to find in the variant.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

#### check inside refnums

A Boolean value that determines whether this node searches any refnums in the variant for the specified data type.

| True | This node searches refnums in the variant for the specified data type. |
| --- | --- |
| False | This node does not search for the specified data type inside refnums. |

**Default:**False

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

#### LabVIEW class qualified name

Specific class you want to find in the variant. You must set **data type to find** to Encapsulated to use this input.

If you search for a class instance by setting **data type to find** to Encapsulated, but leave this input empty, **contains data type to find?** returns True when the variant contains any classes.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

#### contains data type to find?

A Boolean value that indicates whether a variant contains the data type you want to find. This node also searches the data types of cluster or array elements.

| True | The variant contains data type to find. |
| --- | --- |
| False | The variant does not contain data type to find. |

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=class-property.html language=enus -->
## TOPIC 00036: Class Property (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `class-property.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/class-property.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `lvFunction`
- source_description: Provides read and write access to the fields and properties of a class. Access ScopeClass fields are always private, so only property nodes in methods belonging to the class can access fields of the class. Property read and write accessors, which you configure within the class document, each have a

Class Property

Provides read and write access to the fields and properties of a class.

[IMAGE alt='connector_pane_image' src='PropertyNode.Resources_GObject_(property).png']

- Inputs/Outputs
- Details
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/clabview_objectlvclass.png']

#### G object in

Class object you want to access the fields and properties for.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/ilabview_objectlvclass.png']

#### G object out

The class object.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/ivoid.png']

#### (property)

The property of the class object that you want to read or write.

By default, this property is configured to read. To write this property, right-click the property and select 
 Change to Read/Write from the shortcut menu.

To access more properties, resize the node.

#### Access
 Scope

Class fields are always private, so only property nodes in
 methods belonging to the class can access fields of the class. Property read and
 write accessors, which you configure within the class document, each have a
 scope setting. If a property has a public read accessor and a private write
 accessor, property nodes in any VI or CDL that has access to the class has
 access to the read operation while the write operation is available only in
 methods of the class that defines the property.

#### Conditional Error Terminals

A property node has error terminals if it
 accesses only properties or a mix of properties and fields. A property node that
 accesses only fields does not have error terminals.

#### Runtime
 Error Behavior

Errors cascade through property items in a property
 node in order. If the first property access produces an error, that error passes
 into the property accessor for the second property. The G code in the second
 property accessor determines how the error is handled. Runtime errors that
 propagate to field access cause the field access not to execute. If a field read
 receives a runtime error, it does not read the data out of the class and instead
 returns the default value for the field data type.

**Where This Node Can Run:**

Desktop OS: Windows

FPGA:

Web Server:

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=classes-nodes.html language=enus -->
## TOPIC 00037: Classes Nodes

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `classes-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/classes-nodes.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`

Classes Nodes

Class Property

Provides read and write access to the fields and properties of a class.

To More Generic Class

Typecasts a class object or a class reference to a class above the object or reference in the inheritance hierarchy.

To More Specific Class

Typecasts a class object or class reference to a class below the object or reference in the inheritance hierarchy.

Preserve Run-Time Class

Typecasts a class object to a class you specify if both are in the same inheritance hierarchy.

Call Parent Method

Calls the implementation of a dynamic dispatch member VI in the nearest parent class in the inheritance hierarchy.

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=clear-error-cluster.html language=enus -->
## TOPIC 00038: Clear Error Cluster

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `clear-error-cluster.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/clear-error-cluster.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=close-device.html language=enus -->
## TOPIC 00039: Close Device

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `close-device.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/close-device.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Closes the reference to the device you specify in the Initialize Device node. keyboard Reference to the keyboard connected to the computer. joystick Reference to the joystick connected to the computer. This input only appears when you wire joystick out on the Acquire Joystick node to keyboard. mouse

Close Device

Closes the reference to the device you specify in the Initialize Device node.

[IMAGE alt='connector_pane_image' src='Close_Keyboard.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### keyboard

Reference to the keyboard connected to the computer.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### joystick

Reference to the joystick connected to the computer.

This input only appears when you wire **joystick out** on the Acquire Joystick node to **keyboard**.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### mouse

Reference to the mouse connected to the computer.

This input only appears when you wire **mouse out** on the Acquire Mouse node to **keyboard**.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

Input Device Control Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=close-excel-report.html language=enus -->
## TOPIC 00040: Close Excel Report

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `close-excel-report.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/close-excel-report.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Closes the reference to the Excel report. report Reference to the Excel report. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. No error Standard Error Behavior Many nodes provide an error in input and an error out out

Close Excel Report

Closes the reference to the Excel report.

[IMAGE alt='connector_pane_image' src='Close_Excel_Report.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/ilabview_objectlvclass.png']

#### report

Reference to the Excel report.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

Excel Report

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=close-http-handle.html language=enus -->
## TOPIC 00041: Close HTTP Handle

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `close-http-handle.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/close-http-handle.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=close-item.html language=enus -->
## TOPIC 00042: Close Item

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `close-item.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/close-item.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=close-python-session.html language=enus -->
## TOPIC 00043: Close Python Session (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `close-python-session.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/close-python-session.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Closes a Python session. session in Reference to the Python session. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. No error Standard Error Behavior Many nodes provide an error in input and an error out output so that

Close Python Session

Closes a Python session.

[IMAGE alt='connector_pane_image' src='ClosePythonSession.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

#### session in

Reference to the Python session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Where This Node Can Run:**

Desktop OS: Windows

FPGA:

Web Server:

Parent topic:

Python Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=close-reference.html language=enus -->
## TOPIC 00044: Close Reference

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `close-reference.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/close-reference.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes a reference associated with an open VI, component, open application instance, or JavaScript object. reference The reference associated with an open VI, VI object, open application instance, or JavaScript object. This terminal also accepts a 1D array of references. error in Error conditions th

Close Reference

Closes a reference associated with an
 open VI, component, open application instance, or JavaScript object.

[IMAGE alt='1378' src='CloseReference.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### reference

The reference associated with an open VI, VI object, open application instance, or
 JavaScript object. This terminal also accepts a 1D array of references.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR)

#### Releasing a VI Reference from Memory

When you create a reference to a VI, the VI stays in memory until you close the reference and the VI meets the following conditions:

- There are no other open references to the VI.
- The panel of the VI is not open.
- The VI is not a subVI of another VI in memory.
- The VI is not a member of an open project library.

Parent topic:

.NET Nodes

Parent topic:

Execution Control

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=close-registry-key.html language=enus -->
## TOPIC 00045: Close Registry Key

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `close-registry-key.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/close-registry-key.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=close-word-report.html language=enus -->
## TOPIC 00046: Close Word Report (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `close-word-report.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/close-word-report.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Closes the reference to the Word report. report Reference to the Word report. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. No error Standard Error Behavior Many nodes provide an error in input and an error out outpu

Close Word Report

Closes the reference to the Word report.

[IMAGE alt='connector_pane_image' src='Close_Word_Report.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/clabview_objectlvclass.png']

#### report

Reference to the Word report.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Where This Node Can Run:**

Desktop OS: Windows

FPGA:

Web Server:

Parent topic:

Word Report

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=cluster-constant.html language=enus -->
## TOPIC 00047: Cluster Constant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `cluster-constant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/cluster-constant.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a group, or cluster, of mixed-type data elements on the diagram.

Cluster Constant

Represents a group, or cluster, of mixed-type data elements on the diagram.

[IMAGE alt='1378' src='Literal.Cluster.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=cluster-nodes.html language=enus -->
## TOPIC 00048: Cluster Nodes

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `cluster-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/cluster-nodes.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`

Cluster Nodes

Build Cluster

Creates a new cluster from individual elements.

Build Cluster Array

Creates an array of clusters where each cluster contains an array as its only element.

Cluster Properties

Allows you to read and write the elements of a cluster.

Index and Build Cluster Array

i

i

zip

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=cluster-properties.html language=enus -->
## TOPIC 00049: Cluster Properties

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `cluster-properties.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/cluster-properties.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Allows you to read and write the elements of a cluster. cluster in The cluster whose elements you want to access. cluster out The same cluster as cluster in. If you wrote any values to Cluster Properties, the value of cluster out may differ from cluster in. (property) The element of the cluster that

Cluster Properties

Allows you to read and write the elements of a cluster.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### cluster in

The cluster whose elements you want to access.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### cluster out

The same cluster as cluster in.

If you wrote any values to Cluster Properties, the value of cluster out may differ from cluster in.

[IMAGE alt='datatype_icon' src='/assets/img/ivoid.png']

##### (property)

The element of the cluster that you want to read or write.

By default, this element is configured to read. To write this element, right-click the element and select 
 Change to Read/Write from the shortcut menu.

To access more elements, resize the node.

#### Configuring the Node to Read or Write

Change to Read

Change to Write

Parent topic:

Cluster Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=cluster-to-array.html language=enus -->
## TOPIC 00050: Cluster to Array

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `cluster-to-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/cluster-to-array.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a cluster of elements of the same data type to a 1D array. cluster Cluster to convert to an array. cluster cannot contain arrays. array The resulting array. Each element in the array is the same data type and order as the elements in cluster.

Cluster to Array

Converts a cluster of elements of the same data type to a 1D array.

[IMAGE alt='1378' src='ClusterToArray.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### cluster

Cluster to convert to an array. cluster cannot contain arrays.

[IMAGE alt='datatype_icon' src='/assets/img/i1dvoid.png']

##### array

The resulting array. Each element in the array is the same data type and order as the elements in cluster.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=color-constant.html language=enus -->
## TOPIC 00051: Color Constant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `color-constant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/color-constant.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a color you can select on the diagram. Each color corresponds to RGBA color values or a hexadecimal value.

Color Constant

Represents a color you can select on the diagram. Each color corresponds to RGBA
 color values or a hexadecimal value.

[IMAGE alt='1378' src='Literal.Color.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=combo-box-constant.html language=enus -->
## TOPIC 00052: Combo Box Constant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `combo-box-constant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/combo-box-constant.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a list of strings from which you can select on the diagram. Each element in a combo box consists of two strings: a title and a value.

Combo Box Constant

Represents a list of strings from which you can select on the diagram. Each element in a combo box consists of two strings: a title and a value.

[IMAGE alt='1378' src='Literal.ComboBox.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=comment.html language=enus -->
## TOPIC 00053: Comment

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `comment.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/comment.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use to enter comments to document your code.

Comment

Use to enter comments to document your code.

[IMAGE alt='1378' src='Comment.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=comparison-nodes.html language=enus -->
## TOPIC 00054: Comparison Nodes

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `comparison-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/comparison-nodes.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=complex-conjugate.html language=enus -->
## TOPIC 00055: Complex Conjugate

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `complex-conjugate.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/complex-conjugate.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=complex-to-polar.html language=enus -->
## TOPIC 00056: Complex to Polar

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `complex-to-polar.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/complex-to-polar.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=complex-to-real-imaginary.html language=enus -->
## TOPIC 00057: Complex to Real and Imaginary

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `complex-to-real-imaginary.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/complex-to-real-imaginary.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=component-ref-constant.html language=enus -->
## TOPIC 00058: Component Reference Constant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `component-ref-constant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/component-ref-constant.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `lvConstant`
- source_description: Represents a component reference on the diagram.

Component Reference
 Constant

Represents a component reference on the diagram.

[IMAGE alt='connector_pane_image' src='Literal.ComponentReferenceLiteral.png']

- Compatibility

**Where This Node Can Run:**

Desktop OS: Windows

FPGA:

Web Server:

Parent topic:

Execution Control

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=component-reference-properties.html language=enus -->
## TOPIC 00059: Component Reference Properties (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `component-reference-properties.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/component-reference-properties.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `lvFunction`
- source_description: Reads elements of a component reference to a library component. Creating a Plugin-Based Test Application component reference in Component reference for which you want to read properties. error in Error conditions that occur before this node runs. The node responds to this input according to standard

Component Reference
 Properties

Reads elements of a
 component reference to a library component.

###### Programming Patterns

- Creating a Plugin-Based Test Application

[IMAGE alt='connector_pane_image' src='PropertyNode.ComponentReference.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

#### component reference in

Component reference for which you want to read properties.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

#### component reference out

Component reference specified by **component reference
 in**.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

#### Component Information

Information about the component.

Provides the Name, Company, Product, Version, Description, and Runtime Version of the
 component.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

#### Plugin?

Boolean value that indicates whether the library component is a plugin.

To identify a library component as a plugin, open the Library document and enable the
 Identify library as a plugin option in the
 **Document** tab.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

#### Exports

List of all exported files in the component.

**Where This Node Can Run:**

Desktop OS: Windows

FPGA:

Web Server:

Parent topic:

Execution Control

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=concatenate-strings.html language=enus -->
## TOPIC 00060: Concatenate Strings

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `concatenate-strings.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/concatenate-strings.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=constants.html language=enus -->
## TOPIC 00061: Constants

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `constants.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/constants.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`

Constants

Array Constant

Represents an array on the diagram.

Avogadro Constant

Returns the value 6.022140857e23.

Base 10 Logarithm of e

Represents the value 0.43429448190325182.

Boolean (True or False) Constant

Represents a True or False value on the diagram.

Carriage Return Constant

CR

Cluster Constant

Represents a group, or cluster, of mixed-type data elements on the diagram.

Color Constant

Represents a color you can select on the diagram. Each color corresponds to RGBA color values or a hexadecimal value.

Combo Box Constant

Represents a list of strings from which you can select on the diagram. Each element in a combo box consists of two strings: a title and a value.

Comment

Use to enter comments to document your code.

Elementary Charge Constant

Returns the value 1.6021766208e-19.

Empty String Constant

Represents an empty string (length zero) on the diagram.

End of Line Constant

Represents the end-of-line value on the diagram.

Enum Constant

Represents a list of string labels with corresponding integer values you can select on the diagram.

Error Cluster Constant

Represents a constant error on the diagram.

Gravitational Constant

Returns the value 6.67408e-11.

Line Feed Constant

LF

Machine Epsilon

Represents the round-off error for a floating-point number with a given precision.

e

Represents the value 2.7182818284590452.

1/e

Represents the value 0.36787944117144233.

ln10

Represents the value 2.3025850929940459.

ln2

Represents the value 0.6931471805599453.

lnPi

Represents the value 1.1447298858494002.

Molar Gas Constant

Returns the value 8.3144598.

Negative Infinity

Represents the value negative infinity.

Numeric Constant

Represents a number on the diagram.

Pi

Represents the value 3.1415926535897932.

1/Pi

Represents the value 0.31830988618379069.

Pi/2

Represents the value 1.5707963267948966.

Pi*2

Represents the value 6.2831853071795864.

Planck's Constant

Returns the value 6.626070040e-34.

Positive Infinity

Represents the value infinity.

Ring Constant

Represents a list of values you can select on the diagram.

Rydberg Constant

Returns the value 10973731.568508.

Space Constant

Use this constant to supply a one-character space string to the diagram.

Speed of Light Constant

Returns the value 299792458.

String Constant

Represents a text string that you enter on the diagram.

Tab Constant

Consists of a constant string containing the horizontal tab value.

Timestamp Constant

Represents a date and time value on the diagram.

Value Class Constant

Class object with a set of member VIs and encapsulated data you define.

Variant Constant

Represents an empty variant on the diagram.

Waveform Constant

Represents waveform data on the diagram, including the start time for the data, a delta t, and the y-value at each measurement point.

Constants

Related information:

- Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=conversion-nodes.html language=enus -->
## TOPIC 00062: Conversion Nodes

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `conversion-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/conversion-nodes.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=convert-rtd-reading.html language=enus -->
## TOPIC 00063: Convert RTD Reading

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `convert-rtd-reading.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/convert-rtd-reading.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Converts an RTD voltage into a temperature value in degrees Celsius. Ro The RTD resistance at 0 degrees Celsius. 100 Ω voltage The voltage read from the RTD. This input supports waveform and double-precision, floating-point data types. Iex The excitation current used with the RTD. 0.15 µA A A coeffi

Convert RTD Reading

Converts an RTD voltage into a temperature value in degrees Celsius.

[IMAGE alt='connector_pane_image' src='Convert_RTD_Reading_(scalar).gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

#### Ro

The RTD resistance at 0 degrees Celsius.

**Default:**100 Ω

[IMAGE alt='datatype_icon' src='/assets/img/c1dmsdt.png']

#### voltage

The voltage read from the RTD.

This input supports waveform and double-precision, floating-point data types.

[IMAGE alt='datatype_icon' src='/assets/img/csgl.png']

#### Iex

The excitation current used with the RTD.

**Default:**0.15 µA

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

#### A

A coefficient of the Callendar Van-Dusen equation that fits your RTD.

**Default:**0.00390802 — Represents the coefficient for the European curve (also called the DIN 43760 standard).

[IMAGE alt='datatype_icon' src='/assets/img/csgl.png']

#### B

A coefficient of the Callendar Van-Dusen equation that fits your RTD.

**Default:**-5.80195E-07 — Represents the coefficient for the European curve (also called the DIN 43760 standard).

[IMAGE alt='datatype_icon' src='/assets/img/i1dmsdt.png']

#### temperature

The return temperature value in degrees Celsius.

This output returns a waveform or double-precision, floating-point data type depending on the data type of the **voltage** input.

Parent topic:

Numeric Scaling Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=convert-strain-gauge-reading.html language=enus -->
## TOPIC 00064: Convert Strain Gauge Reading

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `convert-strain-gauge-reading.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/convert-strain-gauge-reading.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Converts a strain gauge voltage to units of strain. GF The gauge factor of the strain gauge. 2 v Poisson's ratio. This input is required when bridge configuration is set to the following values: Half Bridge I Full Bridge II Full Bridge III 0 voltage The voltage read from the strain gauge. This input

Convert Strain Gauge Reading

Converts a strain gauge voltage to units of strain.

[IMAGE alt='connector_pane_image' src='Convert_Strain_Gauge_Reading_(scalar).gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

#### GF

The gauge factor of the strain gauge.

**Default:**2

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

#### v

Poisson's ratio. This input is required when **bridge configuration** is set to the following values:

- Half Bridge I
- Full Bridge II
- Full Bridge III

**Default:**0

[IMAGE alt='datatype_icon' src='/assets/img/c1dmsdt.png']

#### voltage

The voltage read from the strain gauge.

This input supports waveform and double-precision, floating-point data types.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

#### bridge configuration

The type of bridge configuration in which the strain gauge is mounted.

| Name | Value | Description |
| --- | --- | --- |
| Qtr Bridge I | 0 | Specifies a Quarter Bridge Type I configuration. |
| Qtr Bridge II | 1 | Specifies a Quarter Bridge Type II configuration. |
| Half Bridge I | 2 | Specifies a Half Bridge Type I configuration. |
| Half Bridge II | 3 | Specifies a Half Bridge Type II configuration. |
| Full Bridge I | 4 | Specifies a Full Bridge Type I configuration. |
| Full Bridge II | 5 | Specifies a Full Bridge Type II configuration. |
| Full Bridge III | 6 | Specifies a Full Bridge Type III configuration. |

**Default:**Half Bridge II

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

#### Vex

The excitation voltage you use.

**Default:**3.33 V

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

#### Rg

The strain gauge nominal resistance value in ohms.

**Default:**120 Ω

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

#### Vinit

The unstrained voltage of the strain gauge after you mount it in its bridge configuration.

Read this voltage at the beginning of your application and save it to pass to this node.

**Default:**0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

#### Rl

The lead resistance. In many cases, the lead resistance is negligible and you can leave this terminal unwired.

This input is used when **bridge configuration** is set to quarter-bridge and half-bridge configurations. This input is ignored when **bridge configuration** is set to full-bridge configurations.

**Default:**0

[IMAGE alt='datatype_icon' src='/assets/img/i1dmsdt.png']

#### strain

The return strain value.

This output returns a waveform or double-precision, floating-point data type depending on the data type of the **voltage** input.

Parent topic:

Numeric Scaling Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=convert-thermistor-reading.html language=enus -->
## TOPIC 00065: Convert Thermistor Reading

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `convert-thermistor-reading.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/convert-thermistor-reading.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Converts a thermistor voltage into a temperature value. type of excitation The voltage and current reference. Voltage Reference 0 Specifies using a voltage reference. Use the voltage reference and R1 inputs only with this option. Current Reference 1 Specifies using a current reference. Use the excit

Convert Thermistor Reading

Converts a thermistor voltage into a temperature value.

[IMAGE alt='connector_pane_image' src='Convert_Thermistor_Reading_(scalar).gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

#### type of excitation

The voltage and current reference.

| Name | Value | Description |
| --- | --- | --- |
| Voltage Reference | 0 | Specifies using a voltage reference. Use the voltage reference and R1 inputs only with this option. |
| Current Reference | 1 | Specifies using a current reference. Use the excitation current input only with this option. |

**Default:**Voltage Reference

[IMAGE alt='datatype_icon' src='/assets/img/c1dmsdt.png']

#### voltage

The voltage read from a thermistor.

This input supports waveform and double-precision, floating-point data types.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

#### voltage reference

The reference you apply across a resistor of known value in series with your thermistor. Use this input only when you set **type of excitation** to 
Voltage Reference.

**Default:**2.5 V

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

#### R1

The value of the resistor in series with your thermistor expressed in ohms. Use this input only when you set **type of excitation** to 
Voltage Reference.

**Default:**5000 Ω

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

#### excitation current

The excitation current applied to the thermistor. Use this input only when you set **type of excitation** to 
Current Reference.

**Default:**100 µA

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

#### temperature units

The units of temperature this node outputs.

| Name | Value | Description |
| --- | --- | --- |
| Celsius | 0 | Returns temperature values in Celsius. |
| Fahrenheit | 1 | Returns temperature values in Fahrenheit. |
| Kelvin | 2 | Returns temperature values in Kelvin. |
| Rankine | 3 | Returns temperature values in Rankine. |

**Default:**Celsius

[IMAGE alt='datatype_icon' src='/assets/img/i1dmsdt.png']

#### temperature

The temperature value in the units specified in **temperature units**.

This output returns a waveform or double-precision, floating-point data type depending on the data type of the **voltage** input.

Parent topic:

Numeric Scaling Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=convert-thermocouple-reading.html language=enus -->
## TOPIC 00066: Convert Thermocouple Reading

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `convert-thermocouple-reading.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/convert-thermocouple-reading.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Converts a thermocouple voltage into a temperature value. type of excitation The voltage and current reference. Voltage Reference 0 Specifies using a voltage reference. Current Reference 1 Specifies using a current reference. Voltage Reference voltage A waveform of voltages read from a thermocouple.

Convert Thermocouple Reading

Converts a thermocouple voltage into a temperature value.

[IMAGE alt='connector_pane_image' src='Convert_Thermocouple_Reading_(scalar).gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

#### type of excitation

The voltage and current reference.

| Name | Value | Description |
| --- | --- | --- |
| Voltage Reference | 0 | Specifies using a voltage reference. |
| Current Reference | 1 | Specifies using a current reference. |

**Default:**Voltage Reference

[IMAGE alt='datatype_icon' src='/assets/img/c1dmsdt.png']

#### voltage

A waveform of voltages read from a thermocouple.

This input supports waveform and double-precision, floating-point data types.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

#### thermocouple type

The type of the thermocouple. Refer to your thermocouple user manual for more information about thermocouple types.

| Name | Value | Description |
| --- | --- | --- |
| B | 0 | Specifies a type B thermocouple. |
| E | 1 | Specifies a type E thermocouple. |
| J | 2 | Specifies a type J thermocouple. |
| K | 3 | Specifies a type K thermocouple. |
| R | 4 | Specifies a type R thermocouple. |
| S | 5 | Specifies a type S thermocouple. |
| T | 6 | Specifies a type T thermocouple. |
| N | 7 | Specifies a type N thermocouple. |

**Default:**J

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

#### CJC voltage

The cold-junction compensation (CJC) reference voltage.

**Default:**0

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

#### CJC sensor

The type of cold-junction compensation (CJC) sensor you are using.

| Name | Value | Description |
| --- | --- | --- |
| IC Sensor | 0 | Specifies an integrated circuit (IC) sensor. |
| Thermistor | 1 | Specifies a thermistor. |

**Default:**IC Sensor

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

#### temperature units

The units of temperature this node outputs.

| Name | Value | Description |
| --- | --- | --- |
| Celsius | 0 | Returns temperature values in Celsius. |
| Fahrenheit | 1 | Returns temperature values in Fahrenheit. |
| Kelvin | 2 | Returns temperature values in Kelvin. |
| Rankine | 3 | Returns temperature values in Rankine. |

**Default:**Celsius

[IMAGE alt='datatype_icon' src='/assets/img/i1dmsdt.png']

#### temperature

The temperature value in the units specified in **temperature units**.

This output returns a waveform or double-precision, floating-point data type depending on the data type of the **voltage** input.

Parent topic:

Numeric Scaling Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=copy-waveform-dt.html language=enus -->
## TOPIC 00067: Copy Waveform dt

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `copy-waveform-dt.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/copy-waveform-dt.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Replaces the dt value of each waveform in the waveform array with the dt value of the waveform at the index position you specify. waveforms in Waveform array in which the node replaces the specific value of each element with the corresponding value of the waveform at the index you specify. This inpu

Copy Waveform dt

Replaces the dt value of each waveform in the waveform array with the dt value of the waveform at the index position you specify.

[IMAGE alt='1378' src='WDT_Copy_Waveform_dt_DBL.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1dmsdt.png']

##### waveforms in

Waveform array in which the node replaces the specific value of each element with the corresponding value of the waveform at the index you specify.

This input accepts a 1D array of waveforms or 1D array of digital waveforms.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### index

Specifier of the waveform in the waveform array from which the node obtains the replacement value.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/i1dmsdt.png']

##### waveforms out

Waveform array in which the dt values of all waveforms are identical.

This output is a digital waveform array when you wire a digital waveform array to waveforms in.

Parent topic:

Waveform Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=cosecant.html language=enus -->
## TOPIC 00068: Cosecant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `cosecant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/cosecant.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the cosecant of a specified value (x) in radians. x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this input has a default

Cosecant

Computes the cosecant of a specified value (x) in radians.

[IMAGE alt='1378' src='Cosecant.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### csc

Result of the operation.

This output assumes the same numeric representation as 
 x.

Parent topic:

Trigonometric Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=cosine.html language=enus -->
## TOPIC 00069: Cosine

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `cosine.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/cosine.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=cotangent.html language=enus -->
## TOPIC 00070: Cotangent

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `cotangent.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/cotangent.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=create-excel-data-sheet-double.html language=enus -->
## TOPIC 00071: Create Excel Data Sheet (Double)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `create-excel-data-sheet-double.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/create-excel-data-sheet-double.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Creates an Excel worksheet with double precision data. sheet name Name of the Excel worksheet you want to contain your data. If you connect a template, LabVIEW NXG will ignore this input. Create Excel Data Sheet will create a new worksheet with this name if one doesn't already exist in the workbook.

Create Excel Data Sheet (Double)

Creates an Excel worksheet with double precision data.

[IMAGE alt='connector_pane_image' src='Create_Excel_Data_Sheet_(DBL).gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

#### sheet name

Name of the Excel worksheet you want to contain your data. If you
 connect a **template**, LabVIEW NXG will ignore this input.
 Create Excel Data Sheet will create a new worksheet with this name if one
 doesn't already exist in the workbook.

Note

**Default:**Report

[IMAGE alt='datatype_icon' src='/assets/img/clabview_objectlvclass.png']

#### report in

Reference to the incoming report.

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

#### 2D data

Floating point data that the node writes to the Excel report.

[IMAGE alt='datatype_icon' src='/assets/img/c1dstr.png']

#### column names

Data column heading. Use column names to identify data in charts. The names must follow the Excel naming conventions of 
**defined names**. If several columns have the same name, Excel displays the values of the last column with this name. The column name comparison is case-insensitive.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/ilabview_objectlvclass.png']

#### report out

Reference to the outgoing report.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

Create Excel Data Sheet

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=create-excel-data-sheet-i64.html language=enus -->
## TOPIC 00072: Create Excel Data Sheet (I64)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `create-excel-data-sheet-i64.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/create-excel-data-sheet-i64.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Creates an Excel worksheet with I64 data. sheet name Name of the Excel worksheet you want to contain your data. If you connect a template, LabVIEW NXG will ignore this input. Create Excel Data Sheet will create a new worksheet with this name if one doesn't already exist in the workbook.If you do not

Create Excel Data Sheet (I64)

Creates an Excel worksheet with I64 data.

[IMAGE alt='connector_pane_image' src='Create_Excel_Data_Sheet_(I64).gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

#### sheet name

Name of the Excel worksheet you want to contain your data. If you
 connect a **template**, LabVIEW NXG will ignore this input.
 Create Excel Data Sheet will create a new worksheet with this name if one
 doesn't already exist in the workbook.

Note

**Default:**Report

[IMAGE alt='datatype_icon' src='/assets/img/clabview_objectlvclass.png']

#### report in

Reference to the incoming report.

[IMAGE alt='datatype_icon' src='/assets/img/c1di64.png']

#### 2D data (I64)

Integer data that the node writes to the Excel report.

[IMAGE alt='datatype_icon' src='/assets/img/c1dstr.png']

#### column names

Data column heading. Use column names to identify data in charts. The names must follow the Excel naming conventions of 
**defined names**. If several columns have the same name, Excel displays the values of the last column with this name. The column name comparison is case-insensitive.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/ilabview_objectlvclass.png']

#### report out

Reference to the outgoing report.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

Create Excel Data Sheet

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=create-excel-data-sheet-string.html language=enus -->
## TOPIC 00073: Create Excel Data Sheet (String)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `create-excel-data-sheet-string.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/create-excel-data-sheet-string.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Creates an Excel worksheet with string data. sheet name Name of the Excel worksheet you want to contain your data. If you connect a template, LabVIEW NXG will ignore this input. Create Excel Data Sheet will create a new worksheet with this name if one doesn't already exist in the workbook.If you do

Create Excel Data Sheet (String)

Creates an Excel worksheet with string data.

[IMAGE alt='connector_pane_image' src='Create_Excel_Data_Sheet_(String).gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

#### sheet name

Name of the Excel worksheet you want to contain your data. If you
 connect a **template**, LabVIEW NXG will ignore this input.
 Create Excel Data Sheet will create a new worksheet with this name if one
 doesn't already exist in the workbook.

Note

**Default:**Report

[IMAGE alt='datatype_icon' src='/assets/img/clabview_objectlvclass.png']

#### report in

Reference to the incoming report.

[IMAGE alt='datatype_icon' src='/assets/img/c1dstr.png']

#### 2D data (string)

String data that the node writes to the Excel report.

[IMAGE alt='datatype_icon' src='/assets/img/c1dstr.png']

#### column names

Data column heading. Use column names to identify data in charts. The names must follow the Excel naming conventions of 
**defined names**. If several columns have the same name, Excel displays the values of the last column with this name. The column name comparison is case-insensitive.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/ilabview_objectlvclass.png']

#### report out

Reference to the outgoing report.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

Create Excel Data Sheet

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=create-excel-data-sheet-time.html language=enus -->
## TOPIC 00074: Create Excel Data Sheet (Time)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `create-excel-data-sheet-time.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/create-excel-data-sheet-time.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Creates an Excel worksheet with time data. sheet name Name of the Excel worksheet you want to contain your data. If you connect a template, LabVIEW NXG will ignore this input. Create Excel Data Sheet will create a new worksheet with this name if one doesn't already exist in the workbook.If you do no

Create Excel Data Sheet (Time)

Creates an Excel worksheet with time data.

[IMAGE alt='connector_pane_image' src='Create_Excel_Data_Sheet_(Time).gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

#### sheet name

Name of the Excel worksheet you want to contain your data. If you
 connect a **template**, LabVIEW NXG will ignore this input.
 Create Excel Data Sheet will create a new worksheet with this name if one
 doesn't already exist in the workbook.

Note

**Default:**Report

[IMAGE alt='datatype_icon' src='/assets/img/clabview_objectlvclass.png']

#### report in

Reference to the incoming report.

[IMAGE alt='datatype_icon' src='/assets/img/c1dtimestamp.png']

#### 2D data (time)

Timestamp data that the node writes to the Excel report.
 .

[IMAGE alt='datatype_icon' src='/assets/img/c1dstr.png']

#### column names

Data column heading. Use column names to identify data in charts. The names must follow the Excel naming conventions of 
**defined names**. If several columns have the same name, Excel displays the values of the last column with this name. The column name comparison is case-insensitive.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/ilabview_objectlvclass.png']

#### report out

Reference to the outgoing report.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

Create Excel Data Sheet

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=create-excel-data-sheet.html language=enus -->
## TOPIC 00075: Create Excel Data Sheet

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `create-excel-data-sheet.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/create-excel-data-sheet.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `multimodeFunction`
- source_description: Creates an Excel worksheet with double, I64, string or time data. If an Excel sheet with the same name already exists, the sheet is overwritten.

Create Excel Data Sheet

Creates an Excel worksheet with double, I64, string or time data. If an Excel sheet with the same name already exists, the sheet is overwritten.

Excel Report

Create, add data to, and close Excel report files.

Create Excel Data Sheet (Double)

Creates an Excel worksheet with double precision data.

Create Excel Data Sheet (I64)

Creates an Excel worksheet with I64 data.

Create Excel Data Sheet (Time)

Creates an Excel worksheet with time data.

Create Excel Data Sheet (String)

Creates an Excel worksheet with string data.

Parent topic:

Excel Report

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=create-registry-key.html language=enus -->
## TOPIC 00076: Create Registry Key

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `create-registry-key.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/create-registry-key.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=create-user-event.html language=enus -->
## TOPIC 00077: Create User Event

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `create-user-event.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/create-user-event.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a reference to a user event with the name and data type you specify. user event data type A cluster of elements or an individual element whose data type defines the data type of the user event. error in Error conditions that occur before this node runs. The node responds to this input accord

Create User Event

Returns a reference to a user event with the name and data type you specify.

[IMAGE alt='1378' src='CreateUserEvent.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### user event data type

A cluster of elements or an individual element whose data type defines the data type of the user event.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### user event out

The resulting user event reference.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

- Executing
 Code Based on a User Event

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=data-exchange-nodes.html language=enus -->
## TOPIC 00078: Data Exchange Nodes

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `data-exchange-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/data-exchange-nodes.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`

Data Exchange Nodes

HTTP Nodes

Build a web client that interacts with servers, web pages, and web services with Hypertext Transfer Protocol (HTTP).

Queue Nodes

Create a queue for communicating data between sections of a diagram or from another VI.

Open URL in Default Browser

Displays a URL or HTML file in the default web browser.

Path to URL

Converts a file path into URL format.

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=data-manipulation-nodes.html language=enus -->
## TOPIC 00079: Data Manipulation Nodes

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `data-manipulation-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/data-manipulation-nodes.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`

Data Manipulation Nodes

Join Numbers

Creates a number from the component bytes or words.

Split Number

Breaks a number into its component bytes or words.

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=date-and-time-to-timestamp.html language=enus -->
## TOPIC 00080: Date and Time to Timestamp

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `date-and-time-to-timestamp.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/date-and-time-to-timestamp.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a timestamp from a set of individual values that specify a date and time. date time record Date and time to convert. fractional second Fractions of a second since the start of the second. Values must be greater than or equal to 0 and less than 1. second Number of complete seconds since the s

Date and Time to Timestamp

Creates a timestamp from a set of individual values that specify a date and time.

[IMAGE alt='1378' src='DateAndTimeToTimestamp.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### date time record

Date and time to convert.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### fractional second

Fractions of a second since the start of the second. Values must be greater than or equal to 0 and less than 1.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### second

Number of complete seconds since the start of the minute. Values can be 0 to 59.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### minute

Number of complete minutes since the start of the hour. Values can be 0 to 59.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### hour

Number of complete hours since midnight. Values can be 0 to 23.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### day of month

Values can be 1 to 31.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### month

Values can be 1 to 12.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### year

Values can be from 1600 to 3000.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### day of week

Values can be 1 to 7, which correspond to Sunday through Saturday, respectively.
 If is UTC? is True, the node ignores day of week.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### day of year

Values can be 1 to 366.
 If 
is UTC? is True, the node ignores 
day of year.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### DST

Value can be 0 for standard or 1 for daylight saving time. You also can set DST to -1 to have the node determine the correct time automatically each time you run the VI. If is UTC? is True, the function ignores the DST setting and uses Universal Time.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### is UTC?

Boolean that determines if date time record is in Universal Time or in the configured time zone for the computer.

| True | date time record is in Universal Time. |
| --- | --- |
| False | date time record is in the configured time zone for the computer. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### timestamp

Timestamp that represents the date and time specified by the individual values in date time record.

If the 
 year and 
 month elements of date time record are out of range, the value of this output is unpredictable.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=decimal-digit.html language=enus -->
## TOPIC 00081: Decimal Digit?

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `decimal-digit.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/decimal-digit.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=decimal-string-to-number.html language=enus -->
## TOPIC 00082: Decimal String to Number

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `decimal-string-to-number.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/decimal-string-to-number.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=decimate-1d-array.html language=enus -->
## TOPIC 00083: Decimate 1D Array

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `decimate-1d-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/decimate-1d-array.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=decrement.html language=enus -->
## TOPIC 00084: Decrement

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `decrement.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/decrement.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Subtracts 1 from the input value. x The value to decrement by 1. This input accepts the following data types: scalar numbers enumerated type values an array or cluster of numbers an array of clusters of numbers waveforms Data Type Changes on FPGA When you add this node to a document targeted to an F

Decrement

Subtracts 1 from the input value.

[IMAGE alt='1378' src='Decrement.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

The value to decrement by 1.

This input accepts the following data types:

- scalar numbers
- enumerated type values
- an array or cluster of numbers
- an array of clusters of numbers
- waveforms

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### x - 1

The result of the decrement operation.

##### Behavior with Timestamps and Enumerated Values

If x is a timestamp value, this node decrements the time by one second. If x is an enumerated type value and you select the first enum value, this node returns the last enum value.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

#### Behavior for Enum Data

All arithmetic functions except Increment and Decrement treat enum data the same as an unsigned integer.
 Decrement changes the first enumerated value to the last value.

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=delete-from-array.html language=enus -->
## TOPIC 00085: Delete from Array

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `delete-from-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/delete-from-array.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes a specified element or subarray of an array. This node returns both the edited array and the deleted element or subarray. array The array from which you want to delete elements, rows, columns, pages, and so on. This input is an n-dimension array of any type. length Number of elements, rows,

Delete from Array

Deletes a specified element or subarray of an array.

This node returns both the edited array and the deleted element or subarray.

[IMAGE alt='1378' src='DeleteFromArray.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### array

The array from which you want to delete elements, rows, columns, pages, and so on. This input is an 
n-dimension array of any type.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### length

Number of elements, rows, columns, or pages to delete.

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### index

The location of the element or subarray to delete from the array.

If index is unwired, this node deletes from the end of the array.

Default value: The index of the last element in the array.

##### Behavior of index inputs for Multidimensional Arrays

When you wire an array to this node, the node resizes automatically to display index inputs for each dimension in the array. This node reduces the array in one dimension only, therefore, you can wire only one index input. For example, to delete a row in a 2D array, wire only the row index. To delete a column, wire only the column index.

##### Relationship between index Inputs and array Dimensions

For multidimensional arrays, index inputs correspond to row-major order. Thus, the first index corresponds last dimension of the array input, and the last index corresponds to the first dimension of the array input. The following table shows the relationship between four index inputs and the dimensions of a 4D array input.

| index Order | Corresponding Dimension in array Input | index Name |
| --- | --- | --- |
| 1 | 4th | volume index |
| 2 | 3rd | page index |
| 3 | 2nd | row index |
| 4 | 1st | column index |

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### array with subset deleted

The array returned with the deleted elements, rows, columns, or pages.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### deleted portion

The deleted element or array.

#### Examples

| Diagram | array | deleted portion | Comments |
| --- | --- | --- | --- |
|  | 1D array | A scalar containing the 2nd element from array | To delete a single element from a 1D array, leave length unwired, and specify the element to delete in index. |
|  | 1D array | 1D array containing only the 4th element from array | To delete one or more elements from a 1D array, specify the number of elements to delete in length, and the index at which to begin the deletion in index. |
|  | 3D array of dimensions 10x4x6 | 3D array of dimensions 2x4x6 containing the last 2 pages from array | The outer dimension size of deleted portion is the value of length, and the inner dimension size(s) match that of array. |
|  | 2D array of dimensions 8x5 | 1D array containing all elements from row 3 of array | If you do not wire a value to length, deleted portion is an array of one less dimension than array containing the portion of the array deleted from array. |
|  | 2D array of dimensions 6x3 | 2D array of dimensions 6x2 | If you wire a value to length and a negative value to the index, deleted portion is an array with an outer dimension size of the value of length subtracted by the absolute value of the index. |

Parent topic:

Array Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=delete-registry-key.html language=enus -->
## TOPIC 00086: Delete Registry Key

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `delete-registry-key.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/delete-registry-key.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=delete-registry-value.html language=enus -->
## TOPIC 00087: Delete Registry Value

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `delete-registry-value.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/delete-registry-value.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes a specific value for a specific key. Incorrectly modifying the registry can damage Windows or prevent you from starting Windows. reference in Reference to the open registry key. value Name of the registry value. error in Error conditions that occur before this node runs. The node responds to

Delete Registry Value

Deletes a specific value for a specific key.

Caution

[IMAGE alt='1378' src='Delete_Registry_Value.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### reference in

Reference to the open registry key.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### value

Name of the registry value.

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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=delete-variant-attribute.html language=enus -->
## TOPIC 00088: Delete Variant Attribute

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `delete-variant-attribute.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/delete-variant-attribute.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=demultiplex-errors.html language=enus -->
## TOPIC 00089: Demultiplex Errors

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `demultiplex-errors.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/demultiplex-errors.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of all of the error clusters that were combined into a single error cluster using Multiplex Errors. error in An error cluster that represents all of the error clusters combined by Multiplex Errors. Standard Error Behavior errors out An array of all the error clusters. If the error c

Demultiplex Errors

Returns an array of all of the error clusters that were combined into a single error cluster using Multiplex Errors.

[IMAGE alt='1378' src='Demultiplex_Errors.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

An error cluster that represents all of the error clusters combined by Multiplex Errors.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### errors out

An array of all the error clusters. If the error clusters were not combined using Multiplex Errors, 
errors out is an empty array.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Error Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=dequeue-element.html language=enus -->
## TOPIC 00090: Dequeue Element

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `dequeue-element.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/dequeue-element.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=destroy-user-event.html language=enus -->
## TOPIC 00091: Destroy User Event

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `destroy-user-event.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/destroy-user-event.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=disable-structure.html language=enus -->
## TOPIC 00092: Disable Structure

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `disable-structure.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/disable-structure.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains one or more subdiagrams, or cases, of which only the enabled subdiagram executes. Use the Disable Structure to disable a section of the diagram. Subdiagram Selector Label Part of the structure that displays the value(s) for which the associated subdiagram executes. You can also use the subd

Disable Structure

Contains one or more subdiagrams, or cases, of which only the enabled subdiagram executes.
 
 Use the Disable Structure to disable a section of the diagram.

#### Inputs/Outputs

##### Subdiagram Selector Label

Part of the structure that displays the value(s) for which the associated subdiagram executes.

You can also use the subdiagram selector label to set a default subdiagram.

[IMAGE alt='1378' src='GUID-EAAC3567-6A01-475B-95C8-14C065FA4D40-a5.png']

##### Tunnel

Point through which data enters or exits a structure.

[IMAGE alt='1378' src='GUID-43DB7847-2DDA-4B38-86E0-27BE4951A189-a5.png']

[IMAGE alt='1378' src='GUID-C924CE10-CF63-4F41-B527-80F1868EFA7E-a5.png']

#### Examples

Search within the programming environment to access the following installed examples:

- Disable Structure

#### Disabling Subdiagrams Based on a Specified Condition

Select 
 Edit Condition for Active Subdiagram in the 
 Item tab to set one or more conditions that, when met, enables a subdiagram in the Disable Structure. For example, you might conditionally enable a subdiagram to run code only on a specific target.

Refer to the following table for a list of available condition symbols and their values.

Note

Disable Structure

| Condition Symbol | Valid Values | Description |
| --- | --- | --- |
| CPU | ARM x64 | The processor on which the subdiagram executes. |
| OS | Linux Win | The operating system on which the subdiagram executes. |
| TARGET_BITNESS | 32 64 | The bitness of the application that executes the subdiagram. |
| TARGET_TYPE | RT Windows FPGA | The platforms or targets on which the subdiagram executes. |

#### Valid Condition Symbols for FPGA Targets

You can only access the symbols in the following table on a VI that is targeted to an FPGA.

| Condition Symbol | Valid Values | Description |
| --- | --- | --- |
| TARGET_TYPE | FPGA | The platforms or targets on which the subdiagram executes. |
| FPGA_TARGET_FAMILY | KINTEX7 | The FPGA family on which the subdiagram executes. |
| FPGA_TARGET_EXECUTION | FPGA_TARGET FPGA_SIMULATION | The location on either the FPGA target or the development computer running in simulation where the subdiagram executes. |
| FPGA_TARGET_CLASS | USRP_294XR__295XR_200_MSPS USRP_294XR__295XR_120_MSPS PXIE_7975R PXIE_7976R | The target class of the FPGA target on which the subdiagram executes. |

Note

Compile Symbols

Item

Parent topic:

Program Flow Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=disconnect-g-types.html language=enus -->
## TOPIC 00093: Disconnect G Types

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `disconnect-g-types.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/disconnect-g-types.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Removes references to G types from the data type stored in a variant. variant in Variant data from which you want to remove references to G types. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. No error Standard Error

Disconnect G Types

Removes references to G types from the data type stored in a variant.

[IMAGE alt='connector_pane_image' src='Disconnect_G_Types.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cfxdt.png']

#### variant in

Variant data from which you want to remove references to G types.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/ifxdt.png']

#### variant out

Variant data stored in **variant in** with all references to G types removed.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=divide.html language=enus -->
## TOPIC 00094: Divide

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `divide.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/divide.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=dotnetnodes.html language=enus -->
## TOPIC 00095: .NET Nodes

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `dotnetnodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/dotnetnodes.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `nodeCollection`

.NET Nodes

Close Reference

Closes a reference associated with an open VI, component, open application instance, or JavaScript object.

Property Node

Reads and/or writes properties of a control reference.

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=downgrade-to-warning.html language=enus -->
## TOPIC 00096: Downgrade to Warning

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `downgrade-to-warning.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/downgrade-to-warning.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=elementary-charge.html language=enus -->
## TOPIC 00097: Elementary Charge Constant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `elementary-charge.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/elementary-charge.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value 1.6021766208e-19. The elementary charge is the electric charge carried by a single proton, or equivalently, the opposite of the electric charge carried by a single electron.

Elementary Charge Constant

Returns the value 1.6021766208e-19. The elementary charge is the electric charge carried by a single proton, or equivalently, the opposite of the electric charge carried by a single electron.

[IMAGE alt='1378' src='Literal.Numeric.Elementary_Charge_Constant.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=empty-array.html language=enus -->
## TOPIC 00098: Empty Array?

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `empty-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/empty-array.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns True if an array is empty. Otherwise, this node returns False. array An n-dimensional array of any type. This input also accepts clusters containing a single array, such as waveforms. This input changes to waveform when the data type is a waveform. Data Type Changes on FPGA When you add this

Empty Array?

Returns True if an array is empty. Otherwise, this node returns False.

[IMAGE alt='1378' src='IsEmptyArray.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### array

An 
n-dimensional array of any type.

This input also accepts clusters containing a single array, such as waveforms. This input changes to waveform when the data type is a waveform.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### empty?

Boolean result of the operation.

Parent topic:

Comparison Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=empty-string-constant.html language=enus -->
## TOPIC 00099: Empty String Constant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `empty-string-constant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/empty-string-constant.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an empty string (length zero) on the diagram.

Empty String Constant

Represents an empty string (length zero) on the diagram.

[IMAGE alt='1378' src='Literal.String.Empty_String_Constant.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=empty-string-path.html language=enus -->
## TOPIC 00100: Empty String or Path?

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `empty-string-path.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/empty-string-path.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=end-of-line-constant.html language=enus -->
## TOPIC 00101: End of Line Constant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `end-of-line-constant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/end-of-line-constant.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=enqueue-element-at-opposite-end.html language=enus -->
## TOPIC 00102: Enqueue Element At Opposite End

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `enqueue-element-at-opposite-end.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/enqueue-element-at-opposite-end.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=enqueue-element.html language=enus -->
## TOPIC 00103: Enqueue Element

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `enqueue-element.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/enqueue-element.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds an element to the back of a queue. If the queue becomes invalid because the queue reference is released, then this node stops waiting and returns an error. queue A reference to a queue. element The element you want to add to the back of the queue. The data type of this input changes to match th

Enqueue Element

Adds an element to the back of a queue.

If the queue becomes invalid because the queue reference is released, then this node stops waiting and returns an error.

[IMAGE alt='1378' src='EnqueueElement.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### queue

A reference to a queue.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### element

The element you want to add to the back of the queue.

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

Transferring Data Between Loops Using Queue Nodes

Parent topic:

Queue Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=enum-constant.html language=enus -->
## TOPIC 00104: Enum Constant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `enum-constant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/enum-constant.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a list of string labels with corresponding integer values you can select on the diagram.

Enum Constant

Represents a list of string labels with corresponding integer values you can select on the diagram.

[IMAGE alt='1378' src='Literal.Enum.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=enum-registry-keys.html language=enus -->
## TOPIC 00105: Enum Registry Keys

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `enum-registry-keys.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/enum-registry-keys.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=enum-registry-values-simple.html language=enus -->
## TOPIC 00106: Enum Registry Values Simple

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `enum-registry-values-simple.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/enum-registry-values-simple.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=equal-to-0.html language=enus -->
## TOPIC 00107: Equal to 0?

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `equal-to-0.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/equal-to-0.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=equal.html language=enus -->
## TOPIC 00108: Equal?

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `equal.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/equal.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=error-cluster-constant.html language=enus -->
## TOPIC 00109: Error Cluster Constant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `error-cluster-constant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/error-cluster-constant.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a constant error on the diagram.

Error Cluster Constant

Represents a constant error on the diagram.

[IMAGE alt='1378' src='Literal.Error.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=error-nodes.html language=enus -->
## TOPIC 00110: Error Nodes

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `error-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/error-nodes.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`

Error Nodes

Build Error Cluster

Creates an error cluster that contains an error or warning with a description and location information.

Clear Error Cluster

Resets an error cluster to no error.

Demultiplex Errors

Returns an array of all of the error clusters that were combined into a single error cluster using Multiplex Errors.

Downgrade to Warning

Changes an error to a warning.

Is Error

Checks an error cluster to see if an error occurred.

Is Error Or Warning

Checks an error cluster to see if an error or warning occurred.

Is Warning

Checks an error cluster to see if a warning occurred.

Retain First Error

Checks each error input in top-down order and returns the first error encountered.

Multiplex Errors

Combines multiple error clusters into a single error cluster.

error out

Read Call Chain

Returns the call chain from where the error or warning occurred.

Read Error Code

Returns the error code of an error cluster.

Read Location

Returns a string that describes where the error or warning occurred.

Upgrade To Error

Changes a warning to an error.

Write Error Code

Replaces the error code in an error cluster.

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=event-loop.html language=enus -->
## TOPIC 00111: Event Loop

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `event-loop.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/event-loop.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an Event Structure within a While Loop.

Event Loop

Creates an Event Structure within a While Loop.

Parent topic:

Program Flow Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=event-structure.html language=enus -->
## TOPIC 00112: Event Structure

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `event-structure.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/event-structure.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits until an event occurs, then executes the appropriate case to handle that event. The Event Structure has one or more subdiagrams, or event cases. Only one event case executes when the structure executes to handle an event. You must place the Event Structure in a While Loop to handle multiple ev

Event Structure

Waits until an event occurs, then executes the appropriate case to handle that event.

The Event Structure has one or more subdiagrams, or event cases. Only one event case executes when the structure executes to handle an event. You must place the Event Structure in a While Loop to handle multiple events.

Configure event cases and events from the 
 **Item** tab. To select the events an event case handles, click 
 Select handled events on the 
 **Item** tab.

#### Inputs/Outputs

##### Event Timeout

Number of milliseconds to wait for an event before timing out.

To enable this terminal, select the Timeout event for at least one event case.

Default value: -1—never time out

[IMAGE alt='1378' src='GUID-946D9B59-4A48-4642-B0DA-433A332B1CCE-a5.png']

##### Event Selector Label

Part of the structure that indicates which events cause the currently displayed case to execute.

Click the drop-down arrow to view available event cases.

[IMAGE alt='1378' src='GUID-64F28156-FA01-46B8-B92D-EFDE3B46B543-a5.png']

##### Dynamic Event

Event registration reference or a cluster of event registration references for dynamic event registration.

To enable this terminal, select 
 Use dynamic events on the 
 Item tab.

Use Register for Events to define events programmatically, and then wire the event registration reference to this terminal to access those events from within the Event Structure.

By default, the dynamic event registration terminal on the right border returns the same event registration reference you wire to the input of the dynamic event registration terminal on the left border. However, if you wire a different event registration reference to the input of the dynamic event registration terminal on the right, the terminal on the right no longer carries the same data as the terminal on the left.

You can use a Register For Events node inside of an event case to modify an existing event registration reference dynamically. To modify an existing event registration reference, you must wire event references to the Register For Events node that contain the same data types as the event references contained in the event registration reference you wire to the Register For Events node.

[IMAGE alt='1378' src='GUID-85D4EEBB-5B72-48FB-BEE6-D3613CBE4E7A-a5.png']

##### Event Data

Border node that identifies the data the Event Structure returns when an event occurs.

Resize the node to view and select data elements. Time and Index are common to all events. Other data elements vary based on the event you configure.

The order of events in the Event Selector Label determines the Index of
 the events in an event case that handles more than one event. When more than one event source
 is configured for an event structure case, Index displays which item in
 the list of sources generated the event currently being handled. Use Control
 Reference to find more information on the source that generated the event.

[IMAGE alt='1378' src='GUID-0CA9F791-E5E3-4017-B4EE-E98B3278310A-a5.png']

##### Event Filter

Border node that identifies the event data you can modify before the user interface can process that data.

This node appears in the Event Structure cases that handle filter events. Resize the node to view inputs available for the filter event you select.

Filter events have names that end with a question mark to help you distinguish them from notify events. Use a filter event if you want to discard the event or interact with data associated with a particular user action on the panel before the Event Structure executes a subdiagram of code.

To change event data, wire and modify data items from the Event Data node to the Event Filter node. You can also change the event data by wiring new values to Event Filter node inputs. To completely discard an event, wire a True value to the Discard? input. If you do not wire a value to a data item of the Event Filter node, that data item remains unchanged.

[IMAGE alt='1378' src='GUID-1D3F89A2-54D7-40D4-8A16-733B26922DAF-a5.png']

##### Tunnel

Point through which data enters or exits a structure.

[IMAGE alt='1378' src='GUID-43DB7847-2DDA-4B38-86E0-27BE4951A189-a5.png']

[IMAGE alt='1378' src='GUID-22751903-51D9-4A17-95AD-675EE1986D77-a5.png']

#### Programming Patterns

- Execute Code Based on a User Event

#### Event Timeout

The Event Structure can time out while waiting for notification of an event. The Event Structure executes the timeout event case you create if the structure times out. The Event Structure does not time out if you do not select the Timeout event for at least one event case.

#### Types of User Interface Events

There are two types of user interface events handled by the Event Structure: notify and filter.

Filter events have names that end with a question mark to help you distinguish them from notify events. In most cases, the VI generates an associated notify event after its corresponding filter event if no event case discarded the event. The notify event has the same name as its corresponding filter event but without the question mark.

The following table describes these types of events and when to use each type:

|  | Notify | Filter |
| --- | --- | --- |
| Description | Informs you that a user action occurred. | Allows you to validate or change the event data before the VI performs the default action associated with that event. You can also discard the event entirely to prevent the change from affecting the VI. |
| Use Case | Use if you want to execute a subdiagram of code when the user performs a particular action on the panel. | Use if you want to discard the event or interact with data associated with a particular user action on the panel before the Event Structure executes a subdiagram of code. |
| Dataflow | The VI sends a copy of the event, in parallel, to each Event Structure configured to handle the event. | The VI sends the event sequentially to each Event Structure configured for the event. The order in which the VI sends the filter event to each Event Structure depends on the order in which you register the events. Each Event Structure must complete the filter event case before the VI can notify the next Event Structure. If an Event Structure case changes any of the event data, the VI passes the changed data to subsequent Event Structures in the chain. If an Event Structure in the chain discards the event, the VI does not pass the event to any Event Structures remaining in the chain. The VI completes processing the user action that triggered the event only after all configured Event Structures handle the event without discarding it. |
| Example | You can configure an Event Structure to execute to handle a Value Change event when the user changes the value of a control. | You can configure an Event Structure to discard the Panel Close? event, preventing the user from interactively closing the panel of the VI. |

#### Event Registration

Register events to specify which events you want an Event Structure to handle.

When you register an event, the VI notifies the Event Structure when that particular event occurs. You can register for an event statically or dynamically. A VI that contains an Event Structure automatically performs static event registration when you run it. Use the Register for Events node to perform event registration for dynamic events.

The following table describes the types of event registration and when to use each type.

|  | Static Event Registration | Dynamic Event Registration |
| --- | --- | --- |
| Description | The VI always queues the event sequentially and notifies the Event Structure when the event occurs. | The VI queues the event sequentially and notifies the Event Structure when the event occurs only if that event occurs as a result of execution of code in your VI. |
| Use Case | You want the VI to generate events only from user interaction on the panel. | You want the VI to generate events as a result of programmatic changes to elements in the VI. |
| Event Generation | Requires user interaction for the VI to generate events. | The VI can generate events without direct user interaction with the panel. You can design an application to make programmatic changes, like updating the value of a control from the diagram, and the VI generates events for these changes. You can control when the VI generates events by registering for events in different parts of an application. At run time, you can change which VIs or controls generate events. To change the objects for which the VI generates events, modify the registration information at run time. |
| Event Handling | Handle events only in the VI where you generate events. You can configure an Event Structure to specify which user interface events on the panel of a VI you want to handle in each Event Structure case. | Handle events in a subVI in addition to the VI where you generate events. For example, in a DAQ application, you can create a subVI to handle all of the user interface events, a subVI to handle all custom events, and a subVI to handle all DAQ events for the entire application rather than handling all events in the VI where the events are generated. |
| Example | If you statically register for a Mouse move event on a panel control, the VI queues this event every time the user moves the mouse over that control. | If you dynamically register for a user event, the VI queues this event when Generate User Event generates the event. |

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=excel-report-nodes.html language=enus -->
## TOPIC 00113: Excel Report (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `excel-report-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/excel-report-nodes.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `nodeCollection`
- source_description: Create, add data to, and close Excel report files.

Excel Report

Create, add data to, and close Excel report files.

Close Excel Report

Closes the reference to the Excel report.

Create Excel Data Sheet

Creates an Excel worksheet with double, I64, string or time data.

Insert Excel Chart

Scatter with Straight Lines

Insert Excel Data

Write data to a specified location in an Excel Sheet.

New Excel Report

Creates an Excel report file.

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=exclusive-or.html language=enus -->
## TOPIC 00114: EXCLUSIVE OR

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `exclusive-or.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/exclusive-or.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the logical exclusive or (XOR) of the inputs. If all inputs are True or all inputs are False, this node returns False. Otherwise, it returns True. This node performs bitwise operations on numeric inputs. input An input to the operation. This input can be any data type that contains only Boo

EXCLUSIVE OR

Computes the logical exclusive or (XOR) of the inputs. If all inputs are True or all inputs are False, this node returns False. Otherwise, it returns True.

This node performs bitwise operations on numeric inputs.

[IMAGE alt='1378' src='LogicalExclusiveOr.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### input

An input to the operation.

This input can be any data type that contains only Boolean values, numbers, or error clusters, such as an array of numbers or a cluster of Booleans. If this input is an error cluster, the node uses only the 
 status element of the error cluster.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### logical XOR

The logical exclusive or (XOR) of the inputs.

#### Examples

| input 0 | input 1 | logical XOR |
| --- | --- | --- |
| T | T | F |
| T | F | T |
| F | T | T |
| F | F | F |

Parent topic:

Boolean Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=execution-control-nodes.html language=enus -->
## TOPIC 00115: Execution Control

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `execution-control-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/execution-control-nodes.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Programmatically configure and control multiple VIs on the local computer. This node collection includes the VI Server Execution nodes.

Execution Control

Programmatically configure and control multiple VIs on the local computer. This node collection includes the VI Server Execution nodes.

Abort VI

Stops the execution of a VI.

Call by Reference

Calls the VI to which a strictly typed VI reference refers.

Component Reference Constant

Represents a component reference on the diagram.

Component Reference Properties

Reads elements of a component reference to a library component.

Close Reference

Closes a reference associated with an open VI, component, open application instance, or JavaScript object.

Get Control Value

Retrieves the value of a named control or indicator as variant data.

Open Component Reference

Returns a reference to a component, such as a library or GLL, you specify with a name string.

Open VI Reference

Returns a reference to a VI you specify with a name string. For a VI exported from a specific library, wire the component reference input.

Run VI

Run

Set Control Value

Specifies the value of a named control or indicator. You can wire a value of any data type to this method.

Start Asynchronous Call

Begins an asynchronous call to the VI you specify with a reference.

Static VI Reference

Maintains a static reference to a VI.

This VI Reference

Returns a static VI reference to the current VI. You can use this reference to access the properties of the VI.

VI Reference Constant

Represents a VI reference on the diagram.

VI Reference Properties

Reads properties of a VI reference.

VI Reference

Passes a VI reference you opened as a parameter to another VI.

Wait on Asynchronous Call

Causes the diagram to wait for an asynchronous call to a target VI to finish executing and then returns the outputs of the target VI.

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=exponential-nodes.html language=enus -->
## TOPIC 00116: Exponential Nodes

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `exponential-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/exponential-nodes.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`

Exponential Nodes

Logarithm Base 10

Computes the base 10 logarithm of a specified input value.

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=first-call.html language=enus -->
## TOPIC 00117: First Call?

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `first-call.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/first-call.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=flatten-to-json.html language=enus -->
## TOPIC 00118: Flatten To JSON

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `flatten-to-json.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/flatten-to-json.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=floating-point-string-to-number.html language=enus -->
## TOPIC 00119: Floating Point String to Number

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `floating-point-string-to-number.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/floating-point-string-to-number.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the characters 0 through 9, plus, minus, e, E, and the decimal point (usually period) in a string to a floating-point number. This node can process strings that use fractional, exponential, or engineering notation. use system decimal point? Boolean specifying whether to use the system decim

Floating Point String to Number

Converts the characters 0 through 9, plus, minus, e, E, and the decimal point (usually period) in a string to a floating-point number.
 This node can process strings that use fractional, exponential, or engineering notation.

[IMAGE alt='1378' src='FloatingPointStringToNumber.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### use system decimal point?

Boolean specifying whether to use the system decimal separator to designate a decimal point.

| True | This node uses the localized decimal separator. |
| --- | --- |
| False | This node uses a period as the decimal separator. |

Default value: FALSE

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

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### default

A numeric value whose representation determines the representation of 
number.

Default value: Extended-precision, floating point

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### offset past number

The index in string of the first character following the number.

If string is an array of strings, offset past number reflects the offset within the last string.

Note

16

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

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

number

| string | offset | default | offset past number | number | Comments |
| --- | --- | --- | --- | --- | --- |
| -4.7e-3x | 0 | 0 | 7 | -0.0047 | x is not allowed, so conversion stops there. |
| +5.3.2 | 0 | 0 | 4 | 5.3 | Second decimal point not allowed, so conversion stops there. |

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=flush-queue.html language=enus -->
## TOPIC 00120: Flush Queue

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `flush-queue.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/flush-queue.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes all elements from a queue and returns the elements as an array. This node does not release the queue reference. queue A reference to a queue. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behav

Flush Queue

Removes all elements from a queue and returns the elements as an array.

Note

[IMAGE alt='1378' src='FlushQueue.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### queue

A reference to a queue.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### queue out

Reference to the queue.

[IMAGE alt='datatype_icon' src='/assets/img/i1dstr.png']

##### remaining elements

An array of elements removed from the queue.

The first element in the array is the element from the front of the queue and the last element in the array is the element from the back of the queue.

The data type of this output changes to match the data type of the queue elements.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

Use Release Queue to release a queue reference from memory.

Parent topic:

Queue Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=for-loop.html language=enus -->
## TOPIC 00121: For Loop

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `for-loop.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/for-loop.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Executes its subdiagram n times. The iteration terminal provides the current loop iteration count, which ranges from 0 to n-1. Iteration Current loop iteration count. The loop count always starts at zero for the first iteration. The maximum number of iterations is 2,147,483,647, or 2^31-1. If you ne

For Loop

Executes its subdiagram 
*n* times.

The iteration terminal provides the current loop iteration count, which ranges from 0 to 
 *n*-1.

#### Inputs/Outputs

##### Iteration

Current loop iteration count. The loop count always starts at zero for the first iteration.

31

If you need to keep count of more than 2,147,483,647 iterations, you can use shift registers with a greater integer range.

[IMAGE alt='1378' src='GUID-5E30A361-66F4-4AF5-9337-BA22F27F4B38-a5.png']

##### Count

Number of times to execute the code inside the For Loop.If you wire 0 or a negative number to the count terminal, the loop does not execute.

This terminal also returns the loop count.

[IMAGE alt='1378' src='GUID-3A11858C-5EAE-4C4B-8119-93159778216C-a5.png']

##### Tunnel

Point through which data enters or exits a structure.

Tunnels can also assume the following types of functionality:

[IMAGE alt='1378' src='GUID-43DB7847-2DDA-4B38-86E0-27BE4951A189-a5.png']

[IMAGE alt='1378' src='GUID-0151FC5F-C6A8-4F4E-B434-909C7DF26499-a5.png']

Append Mode

»

Auto Index Values

[IMAGE alt='1378' src='GUID-50EAB18D-A07F-4B86-B609-A1531BCBF350-a5.png']

Build Array

You can configure a conditional output for any tunnel type by selecting the tunnel and clicking the 
 Conditional checkbox in the 
 Item tab. When the conditional input for a tunnel is True, the loop writes the corresponding value to the tunnel. When the condition input for the tunnel is False, the loop doesn't write the corresponding value to the tunnel.

[IMAGE alt='1378' src='GUID-43DB7847-2DDA-4B38-86E0-27BE4951A189-a5.png']

##### Shift Register

Member of a pair of terminals that passes a value from one iteration of a loop to the next iteration.After the initial loop iteration, the left shift register in the pair returns the value it receives from the right shift register from the previous iteration.

Refer to Accessing Data from the Previous Loop Iteration for more information about passing values from the previous iteration
 to the current iteration.

[IMAGE alt='1378' src='GUID-E948E02A-41FA-479B-955D-15152FA4BA46-a5.png']

##### Create Shift Register

Adds a pair of shift registers to the loop to pass data from one loop iteration to the next.

[IMAGE alt='1378' src='GUID-003DC620-3115-47A9-890E-2F43AB9A320D-a5.png']

#### Examples

The following image shows the output values for a tunnel and shift registers after zero
 loop iterations.

[IMAGE alt='1378' src='GUID-65EFB599-C33A-4ABA-9B0B-C157443EF211-a5.png']

| Output | Panel Indicator | Comments |
| --- | --- | --- |
| A |  | If a For Loop iterates zero times, any output tunnel of the For Loop passes the default value for that tunnel's data type. |
| B |  | Any output shift register passes the value wired to the input of the left shift register. |
| C |  | If the input shift register never contained a value, the output shift register passes the default value for that shift register's data type. |

#### Programming Patterns

- Repeating Operations a Set Number of Times
- Repeating Operations Once for Every Element in an Array

#### Controlling Loop Timing

Refer to Loop Timing for more information about controlling the execution speed of a
 loop.

#### Accessing Data from the Previous Loop Iteration

Refer to Accessing Data from the Previous Loop Iteration for more information about passing values from the previous iteration to
 the current iteration.

#### Tunnel and Shift Register Behavior after Zero Iterations

When you wire data directly through a For Loop that iterates zero times, all output terminals wired to output tunnels display the default value for the data type. All output terminals wired to output shift registers display the data wired to the input shift register. If the input shift register never contained a value, the output shift register displays the default value for that shift register's data type. Refer to the 
 *Examples* section for more information.

#### For Loop Iteration Count Behavior with an Auto-Indexing Input Tunnel

By not wiring a value to the count terminal when auto-indexing is enabled, the loop automatically iterates once for each element in the array.

Wiring a value to the count terminal while auto-indexing is enabled causes the For Loop to use the smallest of the choices between the count terminal and the input array size to determine the number of loop iterations. For example, if an auto-indexed array enters the loop with 10 elements and you wire a value of 15 to the count terminal, the loop executes 10 times.

A For Loop can process multiple arrays one element at a time using multiple auto-indexing input tunnels. In this situation, the loop uses the smallest array size to determine the number of loop iterations. For example, if two auto-indexed arrays enter the loop with 10 and 20 elements respectively, the loop executes 10 times, processing all elements of the first array but only the first 10 elements of the second array.

#### For Loop Auto-Indexing Behavior for Arrays

When you set a tunnel to 
 Auto Index Values, the loop indexes scalar elements from 1D arrays, 1D arrays from 2D arrays, and so on. The opposite occurs at output tunnels. Scalar elements accumulate sequentially into 1D arrays, 1D arrays accumulate into 2D arrays, and so on.

For 2D arrays, indexing occurs at row boundaries, not column boundaries.

Parent topic:

Program Flow Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=format-date-time-string.html language=enus -->
## TOPIC 00122: Format Date and Time String

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `format-date-time-string.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/format-date-time-string.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=format-into-string.html language=enus -->
## TOPIC 00123: Format into String

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `format-into-string.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/format-into-string.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=format-value.html language=enus -->
## TOPIC 00124: Format Value

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `format-value.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/format-value.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=generate-user-event.html language=enus -->
## TOPIC 00125: Generate User Event

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `generate-user-event.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/generate-user-event.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Broadcasts the user event you wire to this node and associated event data to each Event Structure registered to handle the event. If the event is not registered, this node has no effect. user event User event refnum created by a Create User Event node. event data The data associated with an event. T

Generate User Event

Broadcasts the user event you wire to this node and associated event data to each Event Structure registered to handle the event.

If the event is not registered, this node has no effect.

[IMAGE alt='1378' src='GenerateUserEvent.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### user event

User event refnum created by a Create User Event node.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### event data

The data associated with an event. The data type of the event data input must match the data type of the user event data type input on the Create User Event node. For example, if the data type of the user event data type input is a string, the data type of the event data input must also be a string.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### priority

Value that defines how this node enqueues the user event.

| high priority | Enqueues the user event and associated event data into the event queue in front of any previously generated normal priority events. |
| --- | --- |
| normal priority | Enqueues the user event and associated event data into the event queue behind any previously generated events. |

Default value: 
 (0) high priority

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### user event out

The resulting user event reference.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

- Executing
 Code Based on a User Event

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=get-array-info.html language=enus -->
## TOPIC 00126: Get Array Information

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `get-array-info.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/get-array-info.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Retrieves array information from a variant that contains an array data type. This node does not return information about values stored in the array. This node returns an error if the variant does not contain an array. variant Variant data from which you want to retrieve data type information. error

Get Array Information

Retrieves array information from a variant that contains an array data type. This node does not return information about values stored in the array.

This node returns an error if the variant does not contain an array.

[IMAGE alt='connector_pane_image' src='Get_Array_Information.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cfxdt.png']

#### variant

Variant data from which you want to retrieve data type information.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

#### number of dimensions

Number of dimensions in the array stored in the variant.

[IMAGE alt='datatype_icon' src='/assets/img/i1dnclst.png']

#### array lengths

Type and length of each dimension of the array stored in the variant.

[IMAGE alt='datatype_icon' src='/assets/img/ienum.png']

##### Type

Type of each dimension of the array stored in the variant.

| Name | Description |
| --- | --- |
| Variable | The memory of the array dimension can grow or shrink as needed to fit the data size. |
| Fixed | The memory of the array dimension is pre-allocated, and the data length cannot change. |
| Bounded | The memory of the array dimension has a maximum size and can store data with a length less than or equal to this size. |

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### Size

Length of each dimension of the array stored in the variant.

If **Type** is Variable, **Size** returns 0. If **Type** is Fixed or Bounded, **Size** returns the number of elements in each dimension of the array.

[IMAGE alt='datatype_icon' src='/assets/img/ifxdt.png']

#### array element data type

Data type of elements of the array stored in the variant.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=get-cluster-info.html language=enus -->
## TOPIC 00127: Get Cluster Information

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `get-cluster-info.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/get-cluster-info.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Retrieves the data type information of cluster elements from a variant that contains a cluster data type. This node returns an error if the variant does not contain a cluster. variant Variant data from which you want to retrieve data type information. error in Error conditions that occur before this

Get Cluster Information

Retrieves the data type information of cluster elements from a variant that contains a cluster data type.

This node returns an error if the variant does not contain a cluster.

[IMAGE alt='connector_pane_image' src='Get_Cluster_Information.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cfxdt.png']

#### variant

Variant data from which you want to retrieve data type information.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/i1dfxdt.png']

#### cluster elements

An array that contains the data types of cluster elements stored in the variant.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

#### names

Array which contains the names of cluster elements stored in
 **Variant**.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=get-control-value.html language=enus -->
## TOPIC 00128: Get Control Value (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `get-control-value.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/get-control-value.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `lvFunction`
- source_description: Retrieves the value of a named control or indicator as variant data. Use Variant to Data to convert the data to another data type. Using Get Control Value This node requires the referenced VI to have a panel. To use this node to retrieve data from an application, make sure you include the panel when

Get Control Value

Retrieves the value of a named control or indicator as variant data.

Use Variant to Data to convert the data to another data type.

[IMAGE alt='connector_pane_image' src='GetControlValue.png']

- Inputs/Outputs
- Details
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

#### reference in

A reference to a VI.

Use Open VI Reference or Static VI Reference to obtain a valid reference for this input.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

#### control name

Label for the control or indicator whose value you want.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

#### reference out

Unchanged reference to the same VI.

[IMAGE alt='datatype_icon' src='/assets/img/ifxdt.png']

#### control value

Value of the control or indicator.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

#### Using Get Control Value

This node requires the referenced VI to have a panel. To use this node to retrieve data from an application, make sure you include the panel when you build the application.

#### Verifying Valid Data Values

For optimization purposes, the application does not store data values of controls and indicators for any VI until you display the panel or call this node with a reference to the VI.

The first time you use this node to retrieve data from a referenced VI without first opening the panel, this node returns the default values of the control or indicator rather than the actual values. Thereafter, it returns the actual value.

Parent topic:

Execution Control

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=get-current-time.html language=enus -->
## TOPIC 00129: Get Current Time

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `get-current-time.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/get-current-time.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=get-date-and-time-string.html language=enus -->
## TOPIC 00130: Get Date and Time String

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `get-date-and-time-string.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/get-date-and-time-string.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a timestamp value or a number of seconds to a date and time string in the time zone configured for the computer. This node converts a numeric input into a date and time string by interpreting it as the time-zone-independent number of seconds that have elapsed since 12:00 a.m. on January 1,

Get Date and Time String

Converts a timestamp value or a number of seconds to a date and time string in the time zone configured for the computer.

This node converts a numeric input into a date and time string by interpreting it as the time-zone-independent number of seconds that have elapsed since 12:00 a.m. on January 1, 1904, Universal Time.

[IMAGE alt='1378' src='GetDateAndTimeString.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### date format

Appearance of the date string.

Date formats vary with your system configuration. To use a different date format, use Format Date and Time String.

| short | Example: 1/21/94 |
| --- | --- |
| long | Example: Friday, January 21, 1994 |
| abbreviated | Example: Fri, Jan 21, 1994 |

Default value: 
 short

[IMAGE alt='datatype_icon' src='/assets/img/ctimestamp.png']

##### timestamp

The time that you want to convert.

The year in this timestamp must be between 1600 and 3000.

If you wire a numeric value to this input, the node interprets the number as the time-zone-independent number of seconds that have elapsed since 12:00 a.m. on January 1, 1904, Universal Time [01-01-1904 00:00:00]. The node interprets a negative number as the number of seconds before this time.

Default value: The current date and time

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### show seconds?

Boolean that controls the display of seconds in the time string.

| True | Includes seconds in time string |
| --- | --- |
| False | Does not include seconds in time string |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### date string

String of the date from timestamp formatted according to the specified 
date format.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### time string

String of the time from timestamp formatted according to the configured time zone for your computer.

Parent topic:

Timestamp Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=get-final-time-value.html language=enus -->
## TOPIC 00131: Get Final Time Value

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `get-final-time-value.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/get-final-time-value.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the ending time value of the specified waveform. The formula this node uses is xf = x0 + duration of the specified waveform. open interval Interval over which the specified waveform extends. For example, assume a waveform contains 3 data elements at t = {0, dt, 2dt}. An open interval defines

Get Final Time Value

Returns the ending time value of the specified waveform. The formula this node uses is *xf* = *x*0 + 
*duration* of the specified waveform.

[IMAGE alt='1378' src='WDT_Get_Final_Time_Value_DBL.gvi.png']

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

Waveform for which you want to retrieve the final time value.

This input accepts a waveform or a digital waveform.

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### tf

Time value when the final data value was acquired.

Parent topic:

Waveform Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=get-fixed-point-info.html language=enus -->
## TOPIC 00132: Get Fixed-Point Information

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `get-fixed-point-info.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/get-fixed-point-info.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Retrieves fixed-point numeric (FXP) information from a variant that contains a fixed-point numeric data type. This node returns an error if the variant does not contain a fixed-point numeric. variant Variant data from which you want to retrieve data type information. error in Error conditions that o

Get Fixed-Point Information

Retrieves fixed-point numeric (FXP) information from a variant that contains a fixed-point numeric data type.

This node returns an error if the variant does not contain a fixed-point numeric.

[IMAGE alt='connector_pane_image' src='Get_Fixed-Point_Information.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cfxdt.png']

#### variant

Variant data from which you want to retrieve data type information.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

#### FXP representation

Fixed-point information from the fixed-point data type stored in the variant.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### Signed

A Boolean value that indicates whether the fixed-point data type stored in the variant is signed.

| True | The fixed-point data type stored in the variant is signed. |
| --- | --- |
| False | The fixed-point data type stored in the variant is unsigned. |

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### Word Length

Number of bits that this node uses to represent all the possible values of the fixed-point data type stored in the variant.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### Integer Word Length

Number of integer bits, or the number of bits to shift the binary point to the left to reach the most significant bit, for all possible values of the fixed-point data type stored in the variant.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

#### FXP range

Range this node calculates for the fixed-point number stored in the variant.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### Range Min

Minimum value of the range of the fixed-point data type stored in the variant.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### Range Max

Maximum value of the range of the fixed-point data type stored in the variant.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### Delta

Maximum distance between any two sequential numbers in the range of the fixed-point data type stored in the variant.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

#### overflow status included?

A Boolean value that indicates whether the fixed-point number in the variant includes an overflow status.

| True | The fixed-point number in the variant includes an overflow status. This node allocates additional storage space to track whether the fixed-point number is the result of an operation that overflowed. |
| --- | --- |
| False | The fixed-point number in the variant does not include an overflow status. |

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=get-header.html language=enus -->
## TOPIC 00133: Get Header

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `get-header.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/get-header.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value assigned to the header of the client handle. Headers define attributes of the data exchanged between the client and server. client handle Unique value that identifies the web request. You can use the same client handle to wire together multiple HTTP nodes to preserve authentication

Get Header

Returns the value assigned to the header of the client handle.
 Headers define attributes of the data exchanged between the client and server.

[IMAGE alt='1378' src='Get_Header.gvi.png']

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

[IMAGE alt='datatype_icon' src='/assets/img/i1dstr.png']

##### value

Value assigned to the header.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

HTTP Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=get-matrix-diagonal.html language=enus -->
## TOPIC 00134: Get Matrix Diagonal (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `get-matrix-diagonal.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/get-matrix-diagonal.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `lvFunction`
- source_description: Returns the diagonal of matrix beginning at index (row), index (column). Extracting Subdiagonals This node returns a portion of the diagonal, known as a subdiagonal, in certain cases. This node returns subdiagonals as described in the following table. Input Result You wire positive values to index (

Get Matrix Diagonal

Returns the diagonal of **matrix** beginning at **index (row)**, **index (column)**.

[IMAGE alt='connector_pane_image' src='GetMatrixDiagonal.png']

- Inputs/Outputs
- Details
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

#### matrix

2D array of any numeric type.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### index (row)

Starting row index in the output.

Can be an integer or real number.

To add additional **index (row)** inputs, resize the node.

**Default:**0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### index (col)

Starting column index in the output.

Can be an integer or real number.

To add additional **index (col)** inputs, resize the node.

**Default:**0

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

#### diagonal

2D array with one column that contains the diagonal elements in **matrix**. The data type of **diagonal** is the same as the data type of **matrix**.

To add additional **diagonal** outputs, resize the node.

#### Extracting Subdiagonals

| Input | Result |
| --- | --- |
| You wire positive values to index (row) and index (col) that are less than the row and column dimensions of matrix. | This node returns a subdiagonal that includes the diagonal elements starting at (index (row), index (col)) and ending at the last element of the diagonal. |
| You wire a positive value to index (row) that is less than index (col). | diagonal returns a portion of the upper diagonal. |
| You wire a positive value to index (row) that is greater than index (col). | diagonal returns a portion of the lower diagonal. |
| You wire equal values to index (row) and index (col). | diagonal returns a portion of the main diagonal. |

Parent topic:

Matrix Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=get-matrix-elements.html language=enus -->
## TOPIC 00135: Get Matrix Elements (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `get-matrix-elements.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/get-matrix-elements.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `lvFunction`
- source_description: Returns the elements of matrix beginning at index (row), index (col). If you wire scalar values i, j to index (row) and index (col), respectively, this node returns a scalar that contains the element at location (i, j). Output Behavior with 1D Arrays If you wire a 1D array of numeric data to index (

Get Matrix Elements

Returns the elements of **matrix** beginning at **index (row)**, **index (col)**.

###### Programming Patterns

If you wire scalar values 
 i, 
 j to **index (row)** and **index (col)**, respectively, this node returns a scalar that contains the element at location (i, 
 j).

[IMAGE alt='connector_pane_image' src='GetMatrixElements.png']

- Inputs/Outputs
- Details
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

#### matrix

2D array of any numeric type.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### index (row)

Integer, floating-point numeric, 1D array of integers, or 1D array of a floating-point numeric.

To add additional **index (row)** inputs, resize the node.

**Default:**0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### index (col)

Integer, floating-point numeric, 1D array of integers, or 1D array of a floating-point numeric.

To add additional **index (col)** inputs, resize the node.

**Default:**0

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

#### output matrix

Scalar or 2D array that contains the matrix elements. The data type of **output matrix** is the same as the data type of **matrix**.

To add additional **output matrix** outputs, resize the node.

#### Output Behavior with 1D Arrays

If you wire a 1D array of numeric data to **index (row)** or **index (col)**, this node returns one matrix element for each location specified. To determine these locations this node pairs each row index in **index (row)** with each column index in **index (col)**. For example, if you pass the array of integers {1, 2, 4} to **index (row)** and the integer {5} to **index (col)**, this node retrieves matrix elements at indexes (1, 5), (2, 5), and (4, 5). In this case, the output is a column vector, or 3 x 1 matrix.

#### Leaving Inputs Empty or Unwired

If you leave certain inputs empty or unwired, this node returns a portion of **matrix** or invalid operations as described in the following table.

| Input | Result |
| --- | --- |
| You wire an empty matrix to matrix. | output matrix returns an invalid operation value at each exterior location. |
| You wire an empty 1D array to index (row) or index (col). | output matrix returns an empty matrix with 0 in the corresponding row or column dimension. |
| You do not wire index (row) and index (col). | output matrix returns a column vector with the first column of matrix. |

Parent topic:

Matrix Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=get-numeric-info.html language=enus -->
## TOPIC 00136: Get Numeric Information

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `get-numeric-info.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/get-numeric-info.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Retrieves enumeration, unit, and representation information from a variant that contains a numeric data type. This node returns an error if the variant does not contain a numeric. variant Variant data from which you want to retrieve data type information. error in Error conditions that occur before

Get Numeric Information

Retrieves enumeration, unit, and representation information from a variant that contains a numeric data type.

This node returns an error if the variant does not contain a numeric.

[IMAGE alt='connector_pane_image' src='Get_Numeric_Information.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cfxdt.png']

#### variant

Variant data from which you want to retrieve data type information.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/i1dstr.png']

#### enum names

Enumerated values, if the numeric data type stored in the variant is an enumeration. Otherwise, this output returns an empty string.

[IMAGE alt='datatype_icon' src='/assets/img/i1dnclst.png']

#### units

Unit type and exponent, if the numeric data type stored in the variant has units.

[IMAGE alt='datatype_icon' src='/assets/img/ienum.png']

##### Unit Type

Unit type of the numeric data type stored in the variant.

| Name | Description |
| --- | --- |
| Radians | The numeric data type has a unit type of radians. |
| Steradians | The numeric data type has a unit type of steradians. |
| Seconds | The numeric data type has a unit type of seconds. |
| Meters | The numeric data type has a unit type of meters. |
| Kilograms | The numeric data type has a unit type of kilograms. |
| Amperes | The numeric data type has a unit type of amperes. |
| Kelvins | The numeric data type has a unit type of kelvins. |
| Moles | The numeric data type has a unit type of moles. |
| Candelas | The numeric data type has a unit type of candelas. |
| InvalidUnit | The unit type of the numeric data type is invalid. |

[IMAGE alt='datatype_icon' src='/assets/img/ii16.png']

##### Exponent

Exponent of the unit.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

#### representation

Numeric representation of the data type stored in the variant.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=get-queue-status.html language=enus -->
## TOPIC 00137: Get Queue Status

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `get-queue-status.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/get-queue-status.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=get-refnum-info.html language=enus -->
## TOPIC 00138: Get Refnum Information

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `get-refnum-info.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/get-refnum-info.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Retrieves refnum information from a variant that contains a refnum data type. This node returns an error if the variant does not contain a refnum. variant Variant data from which you want to retrieve data type information. error in Error conditions that occur before this node runs. The node responds

Get Refnum Information

Retrieves refnum information from a variant that contains a refnum data type.

This node returns an error if the variant does not contain a refnum.

[IMAGE alt='connector_pane_image' src='Get_Refnum_Information.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cfxdt.png']

#### variant

Variant data from which you want to retrieve data type information.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

#### reference type

Type of the object that is associated with the refnum stored in the variant. For example, if the variant contains a refnum that points to a VI, this output returns a reference type of 
LVObjVI.

[IMAGE alt='datatype_icon' src='/assets/img/ifxdt.png']

#### strict type

Strict type of the refnum stored in the variant, if the refnum is strictly typed. Otherwise, this output returns an empty string.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

#### VI server generic type

VI server class name of the object that is associated with the refnum stored in the variant. This output is valid only if **reference type** is 
LVObjUnknown.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=get-submatrix.html language=enus -->
## TOPIC 00139: Get Submatrix (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `get-submatrix.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/get-submatrix.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `lvFunction`
- source_description: Returns a submatrix of matrix starting at (row 1, column 1) and ending at (row N, column N). Wire inputs to Get Matrix Elements to retrieve elements that are not next to each other in matrix. matrix 2D array of any numeric type. row 1 First row in matrix you want to appear in the output. Must be an

Get Submatrix

Returns a **submatrix** of **matrix** starting at (**row 1**, **column 1**) and ending at (**row N**, **column N**).

###### Programming Patterns

Wire inputs to Get Matrix Elements to retrieve elements that are not next to each other in **matrix**.

[IMAGE alt='connector_pane_image' src='GetSubMatrix.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

#### matrix

2D array of any numeric type.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### row 1

First row in **matrix** you want to appear in the output.

Must be an integer or real numeric.

**Default:**0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### row N

Last row in **matrix** you want to appear in the output.

Must be an integer or real numeric.

**Default:**The index of the last row in **matrix**.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### column 1

First column in **matrix** you want to appear in the output.

Must be an integer or real numeric.

**Default:**0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### column N

Last column in **matrix** you want to appear in the output.

Must be an integer or real numeric.

**Default:**The index of the last column in **matrix**.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

#### submatrix

The resulting submatrix. If **matrix** is an empty matrix, **submatrix** returns **matrix**. The data type of **submatrix** is the same as the data type of **matrix**.

Parent topic:

Matrix Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=get-tag-info.html language=enus -->
## TOPIC 00140: Get Hardware Reference Type Information

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `get-tag-info.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/get-tag-info.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Retrieves hardware reference type information stored in a variant. This node returns an error if the variant does not contain a hardware reference. variant Variant data from which you want to retrieve data type information. error in Error conditions that occur before this node runs. The node respond

Get Hardware Reference Type Information

Retrieves hardware reference type information stored in a variant.

This node returns an error if the variant does not contain a hardware reference.

[IMAGE alt='connector_pane_image' src='Get_Hardware_Reference_Type_Information.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cfxdt.png']

#### variant

Variant data from which you want to retrieve data type information.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

#### tag type

Type of the tag.

For example, a DAQmx Device Name returns a tag type of 
 kDAQmxDeviceTagType.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=get-type-info.html language=enus -->
## TOPIC 00141: Get Type Information

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `get-type-info.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/get-type-info.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Retrieves data type information from a variant. variant Variant data from which you want to retrieve data type information. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. No error Standard Error Behavior Many nodes pr

Get Type Information

Retrieves data type information from a variant.

[IMAGE alt='connector_pane_image' src='Get_Type_Information.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cfxdt.png']

#### variant

Variant data from which you want to retrieve data type information.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/iu8.png']

#### type

Data type stored in the variant.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

#### G Type?

A Boolean value that indicates whether the data type stored in the variant is an instance of a G type.

| True | The data type stored in the variant is an instance of a G type. |
| --- | --- |
| False | The data type stored in the variant is not an instance of a G type. |

An Alternative Way to Detect a G Type

You also can use the Is or Contains G Type? node to determine whether the data type in the variant is an instance of a G type or contains a data type that is an instance of a G type. However, the Is or Contains G Type? node does not return the G type name.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

#### G Type name

Name of the G type. This output returns an empty string if the data type stored in the variant is not an instance of a G type.

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=get-user-defined-refnum-info.html language=enus -->
## TOPIC 00142: Get User-Defined Refnum Information

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `get-user-defined-refnum-info.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/get-user-defined-refnum-info.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Retrieves user-defined refnum information from a variant that contains a user-defined refnum data type. This node returns an error if the variant does not contain a user-defined refnum. variant Variant data from which you want to retrieve data type information. error in Error conditions that occur b

Get User-Defined Refnum Information

Retrieves user-defined refnum information from a variant that contains a user-defined refnum data type.

This node returns an error if the variant does not contain a user-defined refnum.

[IMAGE alt='connector_pane_image' src='Get_User-Defined_Refnum_Information.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cfxdt.png']

#### variant

Variant data from which you want to retrieve data type information.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

#### class name

Class name of the user-defined refnum stored in the variant.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

#### type name

Type of the user-defined refnum stored in the variant.

[IMAGE alt='datatype_icon' src='/assets/img/ifxdt.png']

#### user data

Information stored in the user-defined refnum in the variant.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=get-user-defined-tag-info.html language=enus -->
## TOPIC 00143: Get User-Defined Hardware Reference Type Information

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `get-user-defined-tag-info.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/get-user-defined-tag-info.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Retrieves information in a user-defined hardware reference stored in a variant. This node returns an error if the variant does not contain a user-defined hardware reference. variant Variant data from which you want to retrieve data type information. error in Error conditions that occur before this n

Get User-Defined Hardware Reference Type Information

Retrieves information in a user-defined hardware reference stored in a variant.

This node returns an error if the variant does not contain a user-defined hardware reference.

[IMAGE alt='connector_pane_image' src='Get_User-Defined_Hardware_Reference_Type_Information.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cfxdt.png']

#### variant

Variant data from which you want to retrieve data type information.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

#### class name

Class name of the user-defined tag stored in the variant.

For example, a RIO Device returns a class name of 
 nirioResource.

[IMAGE alt='datatype_icon' src='/assets/img/ifxdt.png']

#### user data

Information stored in the user-defined tag of the variant.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=get-variant-attribute.html language=enus -->
## TOPIC 00144: Get Variant Attribute

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `get-variant-attribute.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/get-variant-attribute.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns either the value of a single variant attribute or the names and values of all variant attributes. To retrieve the names and values of all attributes, select Get All Attributes in the Behavior section of the Item tab. variant The variant data for which you want to retrieve one or all attribut

Get Variant Attribute

Returns either the value of a single variant attribute or the names and values of all variant attributes.

To retrieve the names and values of all attributes, select 
 Get All Attributes in the 
 Behavior section of the 
 **Item** tab.

[IMAGE alt='1378' src='GetVariantAttribute.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cfxdt.png']

##### variant

The variant data for which you want to retrieve one or all attributes.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### name

The name of the attribute whose value you want to retrieve.

Note

Get All Attributes

Behavior

Item

[IMAGE alt='datatype_icon' src='/assets/img/cfxdt.png']

##### default value

A value and data type that you specify. This node returns default value if it does not find the attribute specified in name.

Note

Get All Attributes

Behavior

Item

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ifxdt.png']

##### variant out

variant unchanged.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### found?

A Boolean value that indicates whether the node found the attribute that is specified in name.

| True | The node found the attribute specified in name. |
| --- | --- |
| False | The node did not find the attribute specified in name. |

Note

Get All Attributes

Behavior

Item

[IMAGE alt='datatype_icon' src='/assets/img/i1dstr.png']

##### names

A 1D array containing the names of all attributes associated with the variant.

Sort 1D Array

Note

Get All Attributes

Behavior

Item

[IMAGE alt='datatype_icon' src='/assets/img/ifxdt.png']

##### value

The value associated with the attribute you wire to name in variant format.

Note

Get All Attributes

Behavior

Item

[IMAGE alt='datatype_icon' src='/assets/img/i1dfxdt.png']

##### values

A 1D array containing the values associated with each attribute of the specified variant in variant format. The values in this array appear in the same order as their corresponding names appear in the names output.

You must convert each attribute value to an appropriate data type.

Note

Get All Attributes

Behavior

Item

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Modes of Behavior

This node has two modes of behavior depending on whether you select 
 Get All Attributes in the 
 Behavior section of the 
 Item tab.

| Get All Attributes | Node Behavior |
| --- | --- |
| Selected | The node returns the names of all attributes and their corresponding values in 1D arrays. |
| Not selected | The node searches for only the specified attribute. The names output changes to a Boolean output called found and the values output changes to a variant output called value. If the node does not find the specified attribute(s), or if it cannot convert the attribute(s) to the default value, found is False, and value displays the contents of default value. |

Parent topic:

Variant Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=get-waveform-info.html language=enus -->
## TOPIC 00145: Get Waveform Information

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `get-waveform-info.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/get-waveform-info.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Retrieves the data type of the Y array element from the variant that contains a waveform data type. This node returns an error if the variant does not contain a waveform. variant Variant data from which you want to retrieve data type information. error in Error conditions that occur before this node

Get Waveform Information

Retrieves the data type of the Y array element from the variant that contains a waveform data type.

This node returns an error if the variant does not contain a waveform.

[IMAGE alt='connector_pane_image' src='Get_Waveform_Information.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cfxdt.png']

#### variant

Variant data from which you want to retrieve data type information.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/ifxdt.png']

#### Y array type

Data type of the Y array element of the waveform stored in the variant.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=get-waveform-subset.html language=enus -->
## TOPIC 00146: Get Waveform Subset

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `get-waveform-subset.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/get-waveform-subset.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves a subset of a waveform at a specified time or index. open interval Boolean that determines whether the waveform subset extracted is an open or closed interval. For example, if t0 = 0, dt = 1, Y = {0, 1, 2}, start/duration format is Relative Time, start samples/time is 0, and duration is 2,

Get Waveform Subset

Retrieves a subset of a waveform at a specified time or index.

[IMAGE alt='1378' src='WDT_Get_Waveform_Subset_DBL.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### open interval

Boolean that determines whether the waveform subset extracted is an open or closed interval.

start/duration format

Relative Time

start samples/time

duration

| True | The extracted waveform subset is an open interval. |
| --- | --- |
| False | The extracted waveform subset is a closed interval. |

This input is available when you wire a waveform or digital waveform to waveform.

Default value: True

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### start/duration format

Value that determines whether to retrieve the data value of the specified element or at a specified time.

This input is available when you wire a waveform or digital waveform to waveform.

| Samples | 0 | Returns the data value of the specified element in the waveform data. |
| --- | --- | --- |
| Relative Time | 1 | Returns the data value at a specified time relative to the first point in the waveform. In this mode, the dt of the waveform affects actual start samples/time and actual duration. |

Default value: Samples

[IMAGE alt='datatype_icon' src='/assets/img/cmsdt.png']

##### waveform

Waveform from which you want to retrieve a subset.

This input accepts an array of waveforms or an array of digital waveforms.

This input is available when you wire a waveform or digital waveform data type to digital data. If you wire a digital table to waveform, this input changes to digital data.

[IMAGE alt='datatype_icon' src='/assets/img/cdigtbl.png']

##### digital data

Set of digital data from which you want to retrieve a subset.

This input is available only when you wire a digital table to waveform. If you wire a waveform or digital waveform to digital data, this input changes to waveform.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### start samples/time

Data element or time value where you want to start acquiring a waveform subset.

This input is available when you wire a waveform or digital waveform data type to digital data. If you wire a digital table to waveform, this input changes to start.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### start

Data element or time value where you want to start acquiring a data subset.

This input is available only when you wire a digital table to waveform. If you wire a waveform or digital waveform to digital data, this input changes to start samples/time.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### duration

Amount of time to retrieve data or the number of elements of data you want to retrieve, depending on the start or duration format you select.

This input is available when you wire a waveform or digital waveform data type to digital data. If you wire a digital table to waveform, this input changes to number of samples.

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### number of samples

Number of samples to include in the digital data subset.

This input is available only when you wire a digital table to waveform. If you wire a waveform or digital waveform to digital data, this input changes to duration.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/imsdt.png']

##### waveform subset

Subset of the provided waveform based on the parameters you specify.

This output is a digital waveform when you wire a digital waveform to waveform.

This output is available when you wire a waveform or digital waveform to waveform. If you wire a digital table to waveform, this output changes to digital data subset.

[IMAGE alt='datatype_icon' src='/assets/img/idigtbl.png']

##### digital data subset

Subset of the provided digital data based on the parameters you specify.

This output is available only when you wire a digital table to waveform. If you wire a waveform or digital waveform to digital data, this output changes to waveform subset.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### actual start samples/time

Actual data element when the subset was acquired.

This output is available when you wire a waveform or digital waveform to waveform.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### actual duration

Actual number of elements retrieved or the actual amount of time the data values were acquired.

This output is available when you wire a waveform or digital waveform to waveform.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Waveform Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=get-waveform-time-array.html language=enus -->
## TOPIC 00147: Get Waveform Time Array

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `get-waveform-time-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/get-waveform-time-array.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an array of timestamps based on the specified waveform. waveform Waveform you want to retrieve timestamp information from. This input accepts a waveform or a digital waveform. match transition array Boolean that determines whether the timestamp array output contains a timestamp for every Y v

Get Waveform Time Array

Creates an array of timestamps based on the specified waveform.

[IMAGE alt='1378' src='WDT_Get_Waveform_Time_Array_DBL.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cmsdt.png']

##### waveform

Waveform you want to retrieve timestamp information from.

This input accepts a waveform or a digital waveform.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### match transition array

Boolean that determines whether the timestamp array output contains a timestamp for every Y value in a digital waveform or for only the Y values identified as transitions in a compressed digital waveform.

| True | If the digital waveform is compressed, this node returns the timestamps of the transitional Y values. If the digital waveform is uncompressed, the node treats this input as False. |
| --- | --- |
| False | This node returns the timestamps of all Y values in the digital waveform. |

This input is available when you wire a digital waveform to waveform.

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/i1dtimestamp.png']

##### X array

Array of waveform timestamps.

Parent topic:

Waveform Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=get-xy-value.html language=enus -->
## TOPIC 00148: Get XY Value

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `get-xy-value.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/get-xy-value.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=get.html language=enus -->
## TOPIC 00149: GET

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `get.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/get.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=gravitational.html language=enus -->
## TOPIC 00150: Gravitational Constant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `gravitational.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/gravitational.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value 6.67408e-11. The gravitational constant is an empirical physical constant involved in the calculation of gravitational force between two bodies.

Gravitational Constant

Returns the value 6.67408e-11. The gravitational constant is an empirical physical constant involved in the calculation of gravitational force between two bodies.

[IMAGE alt='1378' src='Literal.Numeric.Gravitational_Constant.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=greater-or-equal-to-0.html language=enus -->
## TOPIC 00151: Greater or Equal to 0?

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `greater-or-equal-to-0.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/greater-or-equal-to-0.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=greater-or-equal.html language=enus -->
## TOPIC 00152: Greater or Equal?

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `greater-or-equal.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/greater-or-equal.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Compares two values and returns True only if the first value is greater than or equal to the second value. This node can also compare an array or cluster of a data type to a scalar of the same data type and produce an array or cluster of Boolean values. x First value to compare. x must be either the

Greater or Equal?

Compares two values and returns True only if the first value is greater than or equal to the second value.

This node can also compare an array or cluster of a data type to a scalar of the same data type and produce an array or cluster of Boolean values.

[IMAGE alt='1378' src='IsGreaterOrEqual.png']

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

##### x >= y?

Boolean result of the operation.

When you compare two arrays, 
 x >= y? is a scalar in 
 Compare Aggregates mode and a Boolean array in 
 Compare Elements mode (default).

#### Behavior with Array Inputs

Compare Aggregates

Compare Aggregates

Parent topic:

Comparison Nodes

Related information:

- Comparison Modes for Array and Cluster Data

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=greater-than-0.html language=enus -->
## TOPIC 00153: Greater Than 0?

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `greater-than-0.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/greater-than-0.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=greater.html language=enus -->
## TOPIC 00154: Greater?

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `greater.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/greater.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=GUID-7466CBBF-27F4-4954-AD04-023B90E2380C.html language=enus -->
## TOPIC 00155: Number of Waveform Samples

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `GUID-7466CBBF-27F4-4954-AD04-023B90E2380C.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/GUID-7466CBBF-27F4-4954-AD04-023B90E2380C.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of data elements in the waveform. You must manually select the polymorphic instance you want to use.

Number of Waveform Samples

Returns the number of data elements in the waveform. You must manually select the polymorphic instance you want to use.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=head.html language=enus -->
## TOPIC 00156: HEAD

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `head.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/head.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=header-exists.html language=enus -->
## TOPIC 00157: Header Exists

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `header-exists.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/header-exists.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=hex-digit.html language=enus -->
## TOPIC 00158: Hexadecimal Digit?

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `hex-digit.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/hex-digit.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=hexadecimal-string-to-number.html language=enus -->
## TOPIC 00159: Hexadecimal String to Number

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `hexadecimal-string-to-number.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/hexadecimal-string-to-number.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=http-nodes.html language=enus -->
## TOPIC 00160: HTTP Nodes

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `http-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/http-nodes.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=hyperbolic-cosecant.html language=enus -->
## TOPIC 00161: Hyperbolic Cosecant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `hyperbolic-cosecant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/hyperbolic-cosecant.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the hyperbolic cosecant in radians of a value you specify(x). x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this input ha

Hyperbolic Cosecant

Computes the hyperbolic cosecant in radians of a value you specify(x).

[IMAGE alt='1378' src='HyperbolicCosecant.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### csch

Result of the operation.

This output assumes the same numeric representation as 
 x.

Parent topic:

Hyperbolic Trigonometry Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=hyperbolic-cosine.html language=enus -->
## TOPIC 00162: Hyperbolic Cosine

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `hyperbolic-cosine.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/hyperbolic-cosine.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the hyperbolic cosine in radians of the value you specify (x). x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this input h

Hyperbolic Cosine

Computes the hyperbolic cosine in radians of the value you specify (x).

[IMAGE alt='1378' src='HyperbolicCosine.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### cosh

Result of the operation.

This output assumes the same numeric representation as 
 x.

Parent topic:

Hyperbolic Trigonometry Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=hyperbolic-cotangent.html language=enus -->
## TOPIC 00163: Hyperbolic Cotangent

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `hyperbolic-cotangent.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/hyperbolic-cotangent.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=hyperbolic-secant.html language=enus -->
## TOPIC 00164: Hyperbolic Secant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `hyperbolic-secant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/hyperbolic-secant.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the hyperbolic secant in radians of a value you specify(x). x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this input has

Hyperbolic Secant

Computes the hyperbolic secant in radians of a value you specify(x).

[IMAGE alt='1378' src='HyperbolicSecant.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### sech

Result of the operation.

This output assumes the same numeric representation as 
 x.

Parent topic:

Hyperbolic Trigonometry Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=hyperbolic-sine.html language=enus -->
## TOPIC 00165: Hyperbolic Sine

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `hyperbolic-sine.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/hyperbolic-sine.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the hyperbolic sine in radians for the value you specify (x). x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this input ha

Hyperbolic Sine

Computes the hyperbolic sine in radians for the value you specify (x).

[IMAGE alt='1378' src='HyperbolicSine.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### sinh

Result of the operation.

This output assumes the same numeric representation as 
 x.

Parent topic:

Hyperbolic Trigonometry Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=hyperbolic-tangent.html language=enus -->
## TOPIC 00166: Hyperbolic Tangent

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `hyperbolic-tangent.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/hyperbolic-tangent.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the hyperbolic tangent in radians of the value you specify(x). x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this input h

Hyperbolic Tangent

Computes the hyperbolic tangent in radians of the value you specify(x).

[IMAGE alt='1378' src='HyperbolicTangent.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### tanh

Result of the operation of the same numeric representation as 
x.

Parent topic:

Hyperbolic Trigonometry Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=hyperbolic-trigonometry-nodes.html language=enus -->
## TOPIC 00167: Hyperbolic Trigonometry Nodes

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `hyperbolic-trigonometry-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/hyperbolic-trigonometry-nodes.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`

Hyperbolic Trigonometry Nodes

Hyperbolic Cosecant

x

Hyperbolic Cosine

x

Hyperbolic Cotangent

x

Hyperbolic Secant

x

Hyperbolic Sine

x

Hyperbolic Tangent

x

Inverse Hyperbolic Cosecant

x

Inverse Hyperbolic Cosine

x

Inverse Hyperbolic Cotangent

x

Inverse Hyperbolic Secant

x

Inverse Hyperbolic Sine

x

Inverse Hyperbolic Tangent

x

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=implies.html language=enus -->
## TOPIC 00168: Implies

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `implies.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/implies.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=in-range-and-coerce.html language=enus -->
## TOPIC 00169: In Range and Coerce

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `in-range-and-coerce.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/in-range-and-coerce.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=increment.html language=enus -->
## TOPIC 00170: Increment

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `increment.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/increment.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds 1 to the input value. x The value to increment by 1. This input accepts the following data types: scalar numbers enumerated type values an array or cluster of numbers an array of clusters of numbers waveforms Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, th

Increment

Adds 1 to the input value.

[IMAGE alt='1378' src='Increment.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

The value to increment by 1.

This input accepts the following data types:

- scalar numbers
- enumerated type values
- an array or cluster of numbers
- an array of clusters of numbers
- waveforms

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### x + 1

The result of the increment operation.

##### Behavior with Timestamps and Enumerated Values

If x is a timestamp value, this node increments the time by one second. If x is an enumerated type value and you select the last enum value, this node returns the first enum value.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

#### Behavior for Enum Data

All arithmetic functions except Increment and Decrement treat enum data the same as an unsigned integer.
 Increment changes the last enumerated value to the first value.

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=index-and-build-cluster-array.html language=enus -->
## TOPIC 00171: Index and Build Cluster Array

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `index-and-build-cluster-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/index-and-build-cluster-array.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indexes a set of arrays and creates a cluster array in which the ith cluster contains the ith element of each input array. This behavior is similar to the zip function in some text-based languages. element An array whose elements you want to separate and redistribute into clusters. created cluster a

Index and Build Cluster Array

Indexes a set of arrays and creates a cluster array in which the 
*i*th cluster contains the 
*i*th element of each input array. This behavior is similar to the 
zip function in some text-based languages.

[IMAGE alt='1378' src='BuildIndexAndBundleClusterArray.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### element

An array whose elements you want to separate and redistribute into clusters.

[IMAGE alt='datatype_icon' src='/assets/img/i1dcclst.png']

##### created cluster array

An array in which each cluster contains one element from each input array. The number of elements in the output array equals the number of elements in the shortest input array.

#### Examples

#### Illustration of Behavior

[IMAGE alt='1378' src='GUID-8E8DD346-9C7F-4A69-8AEC-799F13C25B54-a5.png']

Parent topic:

Cluster Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=index-array.html language=enus -->
## TOPIC 00172: Index Array

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `index-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/index-array.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=index-waveform-array.html language=enus -->
## TOPIC 00173: Index Waveform Array

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `index-waveform-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/index-waveform-array.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=initialize-array.html language=enus -->
## TOPIC 00174: Initialize Array

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `initialize-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/initialize-array.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an n-dimensional array in which every element equals a specified value. element The value used to initialize all elements of initialized array. element can be any scalar type. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this input has a default data ty

Initialize Array

Creates an 
*n*-dimensional array in which every element equals a specified value.

[IMAGE alt='1378' src='InitializeArray.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### element

The value used to initialize all elements of initialized array. element can be any scalar type.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### dimension size

The number of elements in the dimension. This node creates an empty array if any dimension size is less than or equal to 0. You must have 
ndimension size terminals for 
ndimensions.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### initialized array

An array in which every element is initialized to the value of element.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

Parent topic:

Array Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=initialize-device-joystick.html language=enus -->
## TOPIC 00175: Joystick

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `initialize-device-joystick.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/initialize-device-joystick.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Initializes the joystick connected to the computer. device index Index of the joystick you want to initialize. Set device index to 0 if you have only one joystick connected to the computer. 0 error in Error conditions that occur before this node runs. The node responds to this input according to sta

Joystick

Initializes the joystick connected to the computer.

[IMAGE alt='connector_pane_image' src='Initialize_Joystick.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### device index

Index of the joystick you want to initialize. Set device index to 0 if you have only one joystick connected to the computer.

**Default:**0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

#### joystick

Reference to the joystick connected to the computer.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

Initialize Device

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=initialize-device-keyboard.html language=enus -->
## TOPIC 00176: Keyboard

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `initialize-device-keyboard.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/initialize-device-keyboard.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Opens a reference and initializes the keyboard connected to the computer. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. No error Standard Error Behavior Many nodes provide an error in input and an error out output so

Keyboard

Opens a reference and initializes the keyboard connected to the computer.

[IMAGE alt='connector_pane_image' src='Initialize_Keyboard.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

#### keyboard

Reference to the keyboard connected to the computer.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

Initialize Device

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=initialize-device-mouse.html language=enus -->
## TOPIC 00177: Mouse

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `initialize-device-mouse.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/initialize-device-mouse.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Opens a reference and initializes the mouse connected to the computer. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. No error Standard Error Behavior Many nodes provide an error in input and an error out output so th

Mouse

Opens a reference and initializes the mouse connected to the computer.

[IMAGE alt='connector_pane_image' src='Initialize_Mouse.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

#### mouse

Reference to the mouse connected to the computer.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

Initialize Device

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=initialize-device.html language=enus -->
## TOPIC 00178: Initialize Device

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `initialize-device.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/initialize-device.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `multimodeFunction`
- source_description: Initializes the device you specify.

Initialize Device

Initializes the device you specify.

Input Device Control Nodes

Joystick

Initializes the joystick connected to the computer.

Keyboard

Opens a reference and initializes the keyboard connected to the computer.

Mouse

Opens a reference and initializes the mouse connected to the computer.

Parent topic:

Input Device Control Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=input-device-control-nodes.html language=enus -->
## TOPIC 00179: Input Device Control Nodes (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `input-device-control-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/input-device-control-nodes.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `nodeCollection`

Input Device Control Nodes

Acquire Device

Returns data about the device connected to the computer.

Close Device

Initialize Device

Initialize Device

Initializes the device you specify.

Query Input Devices

Obtains information about the devices connected to the computer.

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=insert-excel-chart.html language=enus -->
## TOPIC 00180: Insert Excel Chart

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `insert-excel-chart.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/insert-excel-chart.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Inserts a Scatter with Straight Lines chart to a worksheet of the Excel report. You can add several curves to the default chart by referencing further data columns in x columns or y columns. To display data in other chart types, create your own Excel template and connect it to template of the New Ex

Insert Excel Chart

Inserts a 
**Scatter with Straight Lines** chart to a worksheet of the Excel report. You can add several curves to the default chart by referencing further data columns in **x columns** or **y columns**. To display data in other chart types, create your own Excel template and connect it to **template** of the **New Excel Report** VI.

[IMAGE alt='connector_pane_image' src='Insert_Excel_Chart.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

#### sheet

Name of the Excel worksheet that displays the chart.

[IMAGE alt='datatype_icon' src='/assets/img/clabview_objectlvclass.png']

#### report in

Reference to the incoming report.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

#### x columns

X values of an Excel chart. To reference data for a chart, enter the column name. For example, use 
MyXData to display the data of the column 
MyXData in a chart.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

#### y columns

Y values of an Excel chart. To reference data for a chart, enter the column name. For example, use 
MyYData to display the data of the column 
MyYData in a chart.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

#### range

Position of the chart on the Excel worksheet. Enter the values for the row and the column at the top left and the bottom right corner to determine the position of the chart.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### top left

Top left position of the Excel chart.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

###### row

Excel row number for chart position.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

###### column

Excel column number for chart position.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### bottom right

Bottom right position of the Excel chart.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

###### row

Excel row number for chart position.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

###### column

Excel column number for chart position.

[IMAGE alt='datatype_icon' src='/assets/img/ilabview_objectlvclass.png']

#### report out

Reference to the outgoing report.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

Excel Report

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=insert-excel-data.html language=enus -->
## TOPIC 00181: Insert Excel Data (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `insert-excel-data.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/insert-excel-data.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Write data to a specified location in an Excel Sheet. Not supported Not supported sheet name Name of the Excel worksheet where you want to insert your data. If no worksheets use this name, Insert Excel Data will return an error message. If unwired, LabVIEW NXG will insert data in the first worksheet

Insert Excel Data

Write data to a specified location in an Excel Sheet.

[IMAGE alt='connector_pane_image' src='Insert_Excel_Data_(DBL).gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

#### sheet name

Name of the Excel worksheet where you want to insert your
 data. If no worksheets use this name, Insert Excel
 Data will return an error message. If unwired, LabVIEW NXG will insert data
 in the first worksheet in the workbook.

[IMAGE alt='datatype_icon' src='/assets/img/clabview_objectlvclass.png']

#### report in

Reference to the incoming report.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

#### 2D data

Data to insert into the Excel worksheet.

This input accepts single-precision and double-precision, floating point numbers,
 integers, strings, and timestamps.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

#### location

Target location for data within an Excel Sheet. You can
 specify a single worksheet cell ("C6") or a [defined name](https://support.office.com/en-us/article/define-and-use-names-in-formulas-4d0f13ac-53b7-422e-afd2-abd7ff379c64) as the location for your data. You cannot specify a range ("A1:D8")
 as an input, but you can use a defined name within Excel to specify a range for your data.

Note

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/ilabview_objectlvclass.png']

#### report out

Reference to the outgoing report.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Where This Node Can Run:**

Desktop OS: Windows

FPGA: Not supported

Web Server: Not supported

Parent topic:

Excel Report

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=insert-into-array.html language=enus -->
## TOPIC 00182: Insert into Array

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `insert-into-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/insert-into-array.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Inserts an element or subarray into an array at the index you specify. array The array in which you want to insert an element, row, column, page, and so on. This input is an n-dimension array of any type. index The location in the array where you want to insert the element, row, column, page, and so

Insert into Array

Inserts an element or subarray into an array at the index you specify.

[IMAGE alt='1378' src='InsertIntoArray.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### array

The array in which you want to insert an element, row, column, page, and so on. This input is an 
n-dimension array of any type.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### index

The location in the array where you want to insert the element, row, column, page, and so on. This node automatically provides an index input for each dimension of the array. You can wire only one index input.

If index is larger than the array size, the node does not insert anything into the input array.

Default value: 
 new element or subarray appends to the end of array.

##### Relationship between index Inputs and array Dimensions

For multidimensional arrays, index inputs correspond to row-major order. Thus, the first index corresponds last dimension of the array input, and the last index corresponds to the first dimension of the array input. The following table shows the relationship between four index inputs and the dimensions of a 4D array input.

| index Order | Corresponding Dimension in array Input | index Name |
| --- | --- | --- |
| 1 | 4th | volume index |
| 2 | 3rd | page index |
| 3 | 2nd | row index |
| 4 | 1st | column index |

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### new element or subarray

The element or array that inserts into an element, row, column, or page in the array specified in array.

The data type of the new element or subarray must be the same type as the input array.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### output array

The array with the inserted element(s).

#### Resizing Behavior Based on an Index Input

This node resizes the array along one dimension. Therefore, you can wire only one index input. The index you wire determines the dimension into which you can insert new element or subarray. For example, to insert rows, wire the row index, or to insert columns, wire the column index.

#### Requirements for new element or subarray Dimension

new element or subarray

array

Parent topic:

Array Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=insert-word-data.html language=enus -->
## TOPIC 00183: Insert Word Data (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `insert-word-data.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/insert-word-data.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Adds text to the Word report. report in Reference to the Word report. bookmark Bookmarked location in the Word file to insert report data. This overwrites text at the bookmark in the Word report template. If you place a bookmark in a table, LabVIEW NXG writes data there without changing the table fo

Insert Word Data

Adds text to the Word report.

[IMAGE alt='connector_pane_image' src='Insert_Word_Data.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/clabview_objectlvclass.png']

#### report in

Reference to the Word report.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

#### bookmark

Bookmarked location in the Word file to insert report data.

This overwrites text at the bookmark in the Word report template. If you place a bookmark
 in a table, LabVIEW NXG writes data there without changing the table formatting.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

#### data

Data to insert into the Word report.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/ilabview_objectlvclass.png']

#### report out

Reference to the Word report.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Where This Node Can Run:**

Desktop OS: Windows

FPGA:

Web Server:

Parent topic:

Word Report

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=insert-word-table.html language=enus -->
## TOPIC 00184: Insert Word Table (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `insert-word-table.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/insert-word-table.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Adds a 2D table with data to the Word report. report in Reference to the Word report. bookmark Bookmarked location in the Word file to insert report data. This overwrites text at the bookmark in the Word report template. If you place a bookmark in a table, LabVIEW NXG writes data there without chang

Insert Word Table

Adds a 2D table with data to the Word report.

[IMAGE alt='connector_pane_image' src='Insert_Word_Table.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/clabview_objectlvclass.png']

#### report in

Reference to the Word report.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

#### bookmark

Bookmarked location in the Word file to insert report data.

This overwrites text at the bookmark in the Word report template. If you place a bookmark
 in a table, LabVIEW NXG writes data there without changing the table formatting.

[IMAGE alt='datatype_icon' src='/assets/img/c1dstr.png']

#### table data

Table with data to insert into the Word report.

If you leave **bookmark** unwired, Insert Word
 Table creates a table at the end of the Word report.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/ilabview_objectlvclass.png']

#### report out

Reference to the Word report.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Where This Node Can Run:**

Desktop OS: Windows

FPGA:

Web Server:

Parent topic:

Word Report

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=interleave-1d-array.html language=enus -->
## TOPIC 00185: Interleave 1D Arrays

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `interleave-1d-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/interleave-1d-array.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Interleaves corresponding elements from the input arrays into a single output array. array A 1D array. If the input arrays are not the same size, the number of elements in interleaved array equals the number of elements in the smallest input array multiplied by the number of input arrays. interleave

Interleave 1D Arrays

Interleaves corresponding elements from the input arrays into a single output array.

[IMAGE alt='1378' src='InterleaveArray.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### array

A 1D array. If the input arrays are not the same size, the number of elements in interleaved array equals the number of elements in the smallest input array multiplied by the number of input arrays.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### interleaved array

interleaved array[0] contains array[0], interleaved array[1] contains array 2[0], interleaved array[n-1] contains array n-1[0], interleaved array[n] contains array[1], and so on, where n is the number of input terminals. For example, if array contains {1,2,3} and array 2 contains {9,8,7}, then interleaved array returns {1,9,2,8,3,7}.

Parent topic:

Array Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=interoperability-nodes.html language=enus -->
## TOPIC 00186: Interoperability Nodes

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `interoperability-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/interoperability-nodes.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Integrate communication with local applications.

Interoperability Nodes

Integrate communication with local applications.

Write to System Log

nierrlog

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=interpolate-1d-array.html language=enus -->
## TOPIC 00187: Interpolate 1D Array

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `interpolate-1d-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/interpolate-1d-array.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates a decimal y-value from an array of numbers or points at a specified fractional index or x-value using linear interpolation. array An array containing one of the two following data types: An array of numbers representing y values equally spaced along the x-axis. An array of points where ea

Interpolate 1D Array

Calculates a decimal y-value from an array of numbers or points at a specified fractional index or x-value using linear interpolation.

[IMAGE alt='1378' src='Interpolate1DArray.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### array

An array containing one of the two following data types:

- An array of numbers representing y values equally spaced along the x-axis.
- An array of points where each point is a cluster of x and y coordinates.

If this input is an array of points, the node uses the first element in the cluster (x) to obtain a fractional index by linear interpolation. The node then uses this fractional index to compute the output y value from the second cluster element (y).

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### fractional index or x

The index or x-value at which the node should return a y-value.
 fractional index or x must be located directly on a point or between two points for the node to work correctly.

fractional index or x does not interpolate beyond the bounds of an array or data point set. For example, if the parameter is set lower than the first element or x-value in an array, the node returns the value of the first element or the y-value of the first data point. Similarly, if the parameter is set higher than the last element or x-value in the array, the node returns the value in the final element or the final y-value.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### y value

The interpolated value of the element at the fractional index or the interpolated y-value of the fractional data point in array.

#### Examples

| array | fractional index or x | y value | comments |
| --- | --- | --- | --- |
| [5, 7] | 0.5 | 6.0 | The output is halfway between the values at elements 0 and 1. |
| Array of points [(3,7), (5,9)] | 3.5 | 7.5 | The output is the linearly interpolated value at the x-value corresponding to 3.5. |

#### Interpolating an Array of Numeric Values

If you wire an array of numeric values, Interpolate 1D Array interprets 
 fractional index or x as a reference to the array elements.

#### Interpolating an Array of Data Point Sets

If you wire an array of data point sets, Interpolate 1D Array interprets 
 fractional index or x as a reference to the x-value elements within each data point set.

Note

Parent topic:

Array Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=inverse-cosecant.html language=enus -->
## TOPIC 00188: Inverse Cosecant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `inverse-cosecant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/inverse-cosecant.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the inverse cosecant of a specified value (x) in radians. x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this input has a

Inverse Cosecant

Computes the inverse cosecant of a specified value (x) in radians.

[IMAGE alt='1378' src='InverseCosecant.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### arccsc

Result of the operation.

This output assumes the same numeric representation as 
 x.

Parent topic:

Trigonometric Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=inverse-cosine.html language=enus -->
## TOPIC 00189: Inverse Cosine

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `inverse-cosine.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/inverse-cosine.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=inverse-cotangent.html language=enus -->
## TOPIC 00190: Inverse Cotangent

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `inverse-cotangent.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/inverse-cotangent.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=inverse-hyperbolic-cosecant.html language=enus -->
## TOPIC 00191: Inverse Hyperbolic Cosecant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `inverse-hyperbolic-cosecant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/inverse-hyperbolic-cosecant.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the inverse hyperbolic cosecant in radians of a value you specify(x). x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this

Inverse Hyperbolic Cosecant

Computes the inverse hyperbolic cosecant in radians of a value you specify(x).

[IMAGE alt='1378' src='InverseHyperbolicCosecant.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### arccsch

Result of the operation.

This output assumes the same numeric representation as 
 x.

Parent topic:

Hyperbolic Trigonometry Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=inverse-hyperbolic-cosine.html language=enus -->
## TOPIC 00192: Inverse Hyperbolic Cosine

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `inverse-hyperbolic-cosine.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/inverse-hyperbolic-cosine.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the inverse hyperbolic cosine in radians of a value you specify(x). If x is not complex and is less than 1, the result is not a number (NaN). x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes

Inverse Hyperbolic Cosine

Computes the inverse hyperbolic cosine in radians of a value you specify(x).

If 
 x is not complex and is less than 1, the result is not a number (NaN).

[IMAGE alt='1378' src='InverseHyperbolicCosine.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### arccosh

Result of the operation.

This output assumes the same numeric representation as 
 x.

Parent topic:

Hyperbolic Trigonometry Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=inverse-hyperbolic-cotangent.html language=enus -->
## TOPIC 00193: Inverse Hyperbolic Cotangent

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `inverse-hyperbolic-cotangent.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/inverse-hyperbolic-cotangent.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the inverse hyperbolic cotangent in radians of a value you specify(x). If x is not complex and is greater than -1 and less than 1, the result is not a number (NaN). x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of num

Inverse Hyperbolic Cotangent

Computes the inverse hyperbolic cotangent in radians of a value you specify(x).

If 
 x is not complex and is greater than -1 and less than 1, the result is not a number (NaN).

[IMAGE alt='1378' src='InverseHyperbolicCotangent.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### arccoth

Result of the operation.

This output assumes the same numeric representation as 
 x.

Parent topic:

Hyperbolic Trigonometry Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=inverse-hyperbolic-secant.html language=enus -->
## TOPIC 00194: Inverse Hyperbolic Secant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `inverse-hyperbolic-secant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/inverse-hyperbolic-secant.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the inverse hyperbolic secant in radians of a value you specify(x). If x is not complex and is less than 0 or greater than 1, the result is not a number (NaN). x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

Inverse Hyperbolic Secant

Computes the inverse hyperbolic secant in radians of a value you specify(x).

If 
 x is not complex and is less than 0 or greater than 1, the result is not a number (NaN).

[IMAGE alt='1378' src='InverseHyperbolicSecant.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### arcsech

Result of the operation.

This output assumes the same numeric representation as 
 x.

Parent topic:

Hyperbolic Trigonometry Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=inverse-hyperbolic-sine.html language=enus -->
## TOPIC 00195: Inverse Hyperbolic Sine

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `inverse-hyperbolic-sine.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/inverse-hyperbolic-sine.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the inverse hyperbolic sine in radians of a value you specify (x). x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this inp

Inverse Hyperbolic Sine

Computes the inverse hyperbolic sine in radians of a value you specify (x).

[IMAGE alt='1378' src='InverseHyperbolicSine.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### arcsinh

Result of the operation.

This output assumes the same numeric representation as 
 x.

Parent topic:

Hyperbolic Trigonometry Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=inverse-hyperbolic-tangent.html language=enus -->
## TOPIC 00196: Inverse Hyperbolic Tangent

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `inverse-hyperbolic-tangent.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/inverse-hyperbolic-tangent.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the inverse hyperbolic tangent in radians of a value you specify(x). If x is not complex and is less than -1 or greater than 1, the result is not a number (NaN). x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of number

Inverse Hyperbolic Tangent

Computes the inverse hyperbolic tangent in radians of a value you specify(x).

If 
 x is not complex and is less than -1 or greater than 1, the result is not a number (NaN).

[IMAGE alt='1378' src='InverseHyperbolicTangent.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### arctanh

Result of the operation.

This output assumes the same numeric representation as 
 x.

Parent topic:

Hyperbolic Trigonometry Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=inverse-secant.html language=enus -->
## TOPIC 00197: Inverse Secant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `inverse-secant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/inverse-secant.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=inverse-sine.html language=enus -->
## TOPIC 00198: Inverse Sine

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `inverse-sine.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/inverse-sine.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the arcsine of a specified value (x) in radians. If x is not complex and is less than -1 or greater than 1, the result is not a number (NaN). x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes

Inverse Sine

Computes the arcsine of a specified value (x) in radians.

If 
 x is not complex and is less than -1 or greater than 1, the result is not a number (NaN).

[IMAGE alt='1378' src='InverseSine.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### arcsin

Result of the operation.

x

x

x

i

x

arcsin

Parent topic:

Trigonometric Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=inverse-tangent-2-input.html language=enus -->
## TOPIC 00199: Inverse Tangent (2 Input)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `inverse-tangent-2-input.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/inverse-tangent-2-input.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=inverse-tangent.html language=enus -->
## TOPIC 00200: Inverse Tangent

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `inverse-tangent.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/inverse-tangent.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the arctangent of a specified value (x) in radians. x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this input has a defaul

Inverse Tangent

Computes the arctangent of a specified value (x) in radians.

[IMAGE alt='1378' src='InverseTangent.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### arctan

Result of the operation.

x

x

x

i

x

arctan

Parent topic:

Trigonometric Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=is-error-cluster.html language=enus -->
## TOPIC 00201: Is Error Cluster?

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `is-error-cluster.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/is-error-cluster.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Indicates whether the data type of the input is an error cluster. variant Variant data from which you want to retrieve error cluster information. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. No error Standard Error

Is Error Cluster?

Indicates whether the data type of the input is an error cluster.

[IMAGE alt='connector_pane_image' src='Is_Error_Cluster.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cfxdt.png']

#### variant

Variant data from which you want to retrieve error cluster information.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

#### error cluster?

A Boolean that indicates whether the data type of the input is an error cluster.

| True | The input is an error cluster. |
| --- | --- |
| False | The input is not an error cluster. |

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=is-error-or-warning.html language=enus -->
## TOPIC 00202: Is Error Or Warning

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `is-error-or-warning.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/is-error-or-warning.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks an error cluster to see if an error or warning occurred. error in An error cluster that you use to check for errors or warnings. Standard Error Behavior error or warning? A Boolean that indicates whether the error cluster is an error or warning. True error in contains an error or warning. Fal

Is Error Or Warning

Checks an error cluster to see if an error or warning occurred.

[IMAGE alt='1378' src='Is_Error_Or_Warning.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

An error cluster that you use to check for errors or warnings.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### error or warning?

A Boolean that indicates whether the error cluster is an error or warning.

| True | error in contains an error or warning. |
| --- | --- |
| False | No error or warning occurred. |

Parent topic:

Error Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=is-error.html language=enus -->
## TOPIC 00203: Is Error

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `is-error.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/is-error.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks an error cluster to see if an error occurred. error in An error cluster that you use to check for errors or warnings. Standard Error Behavior error? A Boolean that indicates whether the error cluster contains an error. True error in contains an error. False error in contains a warning or no e

Is Error

Checks an error cluster to see if an error occurred.

[IMAGE alt='1378' src='Is_Error.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

An error cluster that you use to check for errors or warnings.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### error?

A Boolean that indicates whether the error cluster contains an error.

| True | error in contains an error. |
| --- | --- |
| False | error in contains a warning or no error or warning occurred. |

Parent topic:

Error Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=is-or-contains-g-type.html language=enus -->
## TOPIC 00204: Is or Contains G Type?

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `is-or-contains-g-type.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/is-or-contains-g-type.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Checks if the data type stored in a variant is an instance of a G type or contains a data type which is an instance of a G type. The Get Type Information node can retrieve information about the G type. variant Variant data from which you want to retrieve data type information. error in Error conditi

Is or Contains G Type?

Checks if the data type stored in a variant is an instance of a G type or contains a data type which is an instance of a G type.

The Get Type Information node can retrieve information about the G type.

[IMAGE alt='connector_pane_image' src='Is_or_Contains_G_Type.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cfxdt.png']

#### variant

Variant data from which you want to retrieve data type information.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

#### is or contains G Type?

A Boolean value that indicates whether the data type stored in a variant is an instance of a G type or contains a data type which is an instance of a G type.

| True | The data type stored in the variant is an instance of a G type or contains a data type which is an instance of a G type. |
| --- | --- |
| False | The data type stored in the variant is not an instance of a G type, nor does it contain a data type which is an instance of a G type. |

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=is-warning.html language=enus -->
## TOPIC 00205: Is Warning

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `is-warning.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/is-warning.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks an error cluster to see if a warning occurred. error in An error cluster that you use to check for errors or warnings. Standard Error Behavior warning? A Boolean that indicates whether the error cluster contains a warning. True error in contains a warning. False error in contains an error or

Is Warning

Checks an error cluster to see if a warning occurred.

[IMAGE alt='1378' src='Is_Warning.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

An error cluster that you use to check for errors or warnings.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### warning?

A Boolean that indicates whether the error cluster contains a warning.

| True | error in contains a warning. |
| --- | --- |
| False | error in contains an error or no error or warning occurred. |

Parent topic:

Error Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=join-numbers.html language=enus -->
## TOPIC 00206: Join Numbers

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `join-numbers.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/join-numbers.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=less-or-equal-to-0.html language=enus -->
## TOPIC 00207: Less or Equal to 0?

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `less-or-equal-to-0.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/less-or-equal-to-0.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=less-or-equal.html language=enus -->
## TOPIC 00208: Less or Equal?

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `less-or-equal.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/less-or-equal.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=less-than-0.html language=enus -->
## TOPIC 00209: Less Than 0?

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `less-than-0.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/less-than-0.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns True if a value is less than 0. Otherwise, this node returns False. x An input to this operation. This input supports numeric scalar values, clusters, timestamp values, waveforms, and arrays of numbers. For waveforms, the node compares only the y values of this input. Data Type Changes on FP

Less Than 0?

Returns True if a value is less than 0. Otherwise, this node returns False.

[IMAGE alt='1378' src='IsLessThan0.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports numeric scalar values, clusters, timestamp values, waveforms, and arrays of numbers.

For waveforms, the node compares only the y values of this input.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### x < 0?

Boolean result of the operation.

This output assumes the same data type structure as 
 x.

Parent topic:

Comparison Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=less.html language=enus -->
## TOPIC 00210: Less?

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `less.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/less.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=line-feed-constant.html language=enus -->
## TOPIC 00211: Line Feed Constant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `line-feed-constant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/line-feed-constant.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the UTF-8 LF value on the diagram. Use this constant when you do not want to type in the backslash code for the character.

Line Feed Constant

Represents the UTF-8 
LF value on the diagram.

Use this constant when you do not want to type in the backslash code for the character.

[IMAGE alt='1378' src='Literal.String.Line_Feed_Constant.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=list-headers.html language=enus -->
## TOPIC 00212: List Headers

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `list-headers.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/list-headers.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Lists the headers associated with the client handle. Headers define attributes of the data exchanged between the client and server. client handle Unique value that identifies the web request. You can use the same client handle to wire together multiple HTTP nodes to preserve authentication credentia

List Headers

Lists the headers associated with the client handle.
 Headers define attributes of the data exchanged between the client and server.

[IMAGE alt='1378' src='List_Headers.gvi.png']

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

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### client handle out

Unique value that returns data back to the node. You can use the same client handle to wire together multiple HTTP nodes to preserve authentication credentials, HTTP headers, and cookies. Client handles are not required when making independent web requests without persistent data such as headers or credentials.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### headers

Headers associated with the client handle.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

HTTP Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=logarithm-base-10.html language=enus -->
## TOPIC 00213: Logarithm Base 10

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `logarithm-base-10.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/logarithm-base-10.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the base 10 logarithm of a specified input value. If x is 0, log is negative infinity. If x is not complex and is less than 0, log is not a number (NaN). x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data

Logarithm Base 10

Computes the base 10 logarithm of a specified input value.

If 
 x is 0, 
 log is negative infinity. If 
 x is not complex and is less than 0, 
 log is not a number (NaN).

[IMAGE alt='1378' src='LogarithmBase10.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### log

Result of the operation.

x

x

x

x

log

Parent topic:

Exponential Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=lossy-enqueue-element.html language=enus -->
## TOPIC 00214: Lossy Enqueue Element

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `lossy-enqueue-element.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/lossy-enqueue-element.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds an element to the back of a queue. Unlike Enqueue Element, this node does not wait for space in the queue to become available. If no space is available in the queue, this node discards an element from the front of the queue to make space. queue A reference to a queue. element The element you wa

Lossy Enqueue Element

Adds an element to the back of a queue. Unlike Enqueue Element, this node does not wait for space in the queue to become available. If no space is available in the queue, this node discards an element from the front of the queue to make space.

[IMAGE alt='1378' src='LossyEnqueueElement.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### queue

A reference to a queue.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### element

The element you want to add to the back of the queue.

The data type of this input changes to match the data type of the elements in the queue.

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

##### overflow element

The element that this node removed from the front of the queue if the queue was full.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### overflow?

A Boolean value that indicates whether the queue was full and this node had to make space for the element.

| True | The queue was full and this node removed an element to create space. |
| --- | --- |
| False | The queue accepted the element and did not remove an element to make space. |

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

Use Obtain Queue to set the maximum size of the queue.

Parent topic:

Queue Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=machine-epsilon.html language=enus -->
## TOPIC 00215: Machine Epsilon

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `machine-epsilon.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/machine-epsilon.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the round-off error for a floating-point number with a given precision. Use the machine epsilon constant to compare whether two floating-point numbers are equivalent.

Machine Epsilon

Represents the round-off error for a floating-point number with a given precision.
 Use the machine epsilon constant to compare whether two floating-point numbers are equivalent.

[IMAGE alt='1378' src='Literal.Numeric.Machine_Epsilon.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=match-pattern.html language=enus -->
## TOPIC 00216: Match Pattern

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `match-pattern.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/match-pattern.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=matrix-nodes.html language=enus -->
## TOPIC 00217: Matrix Nodes (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `matrix-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/matrix-nodes.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `nodeCollection`
- source_description: Manipulate the elements, diagonals, and submatrices of a matrix. Many of these nodes complement existing array operations but offer functionality for math algorithms based on matrices.

Matrix Nodes

Manipulate the elements, diagonals, and submatrices of a matrix. Many of these nodes complement existing array operations but offer functionality for math algorithms based on matrices.

Build Matrix

Appends elements to a matrix by rows or columns.

Get Matrix Diagonal

matrix

index (row)

index (column)

Get Matrix Elements

matrix

index (row)

index (col)

Get Submatrix

submatrix

matrix

row 1

column 1

row N

column N

Matrix Size

matrix

Resize Matrix

matrix

number of rows

number of columns

Set Matrix Diagonal

matrix

index (row)

index (col)

Set Matrix Elements

matrix

index (row)

index (col)

Set Submatrix

matrix

row 1

column 1

row N

column N

Transpose Matrix

matrix

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=matrix-size.html language=enus -->
## TOPIC 00218: Matrix Size (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `matrix-size.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/matrix-size.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `lvFunction`
- source_description: Returns the dimensions for the number of rows and columns of matrix. matrix 2D array of any numeric type. number of rows Row dimension of the matrix. number of columns Column dimension of the matrix.

Matrix Size

Returns the dimensions for the number of rows and columns of **matrix**.

[IMAGE alt='connector_pane_image' src='MatrixSize.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

#### matrix

2D array of any numeric type.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

#### number of rows

Row dimension of the matrix.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

#### number of columns

Column dimension of the matrix.

Parent topic:

Matrix Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=max-and-min.html language=enus -->
## TOPIC 00219: Max and Min

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `max-and-min.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/max-and-min.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=merge-errors.html language=enus -->
## TOPIC 00220: Retain First Error

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `merge-errors.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/merge-errors.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=molar-gas.html language=enus -->
## TOPIC 00221: Molar Gas Constant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `molar-gas.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/molar-gas.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value 8.3144598. The molar gas constant is a physical constant which is featured in many fundamental equations in the physical sciences, such as the ideal gas law and the Nernst equation.

Molar Gas Constant

Returns the value 8.3144598. The molar gas constant is a physical constant which is featured in many fundamental equations in the physical sciences, such as the ideal gas law and the Nernst equation.

[IMAGE alt='1378' src='Literal.Numeric.Molar_Gas_Constant.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=multiplex-errors.html language=enus -->
## TOPIC 00222: Multiplex Errors

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `multiplex-errors.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/multiplex-errors.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Combines multiple error clusters into a single error cluster. error out is no error if the specified inputs do not contain an error or warning. error in 1 Error cluster that you want to combine. If you want to combine more than three error clusters, create an array of the error clusters you want to

Multiplex Errors

Combines multiple error clusters into a single error cluster.
 error out is no error if the specified inputs do not contain an error or warning.

[IMAGE alt='1378' src='Multiplex_Errors.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in 1

Error cluster that you want to combine.

If you want to combine more than three error clusters, create an array of the error clusters you want to combine and use error array in.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in 2

Error cluster that you want to combine.

If you want to combine more than three error clusters, create an array of the error clusters you want to combine and use error array in.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in 3

Error cluster that you want to combine.

If you want to combine more than three error clusters, create an array of the error clusters you want to combine and use error array in.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/c1derrcodeclst.png']

##### error array in

An array of error clusters.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

A single error cluster that combines all of the errors and warnings specified.

678100

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

Use Demultiplex Errors to recover the individual error clusters that you combine with Multiplex Errors.

Parent topic:

Error Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=multiply-array-elements.html language=enus -->
## TOPIC 00223: Multiply Array Elements

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `multiply-array-elements.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/multiply-array-elements.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the product of all of the elements in a numeric array. array An array of any number of dimensions. This input changes to waveform when the data type is a waveform. waveform The waveform whose array of y values you want to use in this operation. This input becomes available when you wire a wa

Multiply Array Elements

Returns the product of all of the elements in a numeric array.

[IMAGE alt='1378' src='MultiplyArrayElements.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### array

An array of any number of dimensions. This input changes to waveform when the data type is a waveform.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### waveform

The waveform whose array of y values you want to use in this operation. This input becomes available when you wire a waveform to array.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### product

The product of all elements in a numeric array.

##### Behavior with Empty Arrays

If you wire an empty array to array, this node returns a value of 1.

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=multiply.html language=enus -->
## TOPIC 00224: Multiply

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `multiply.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/multiply.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the product of the inputs. A waveform can only be multiplied by either another waveform or a scalar numeric value. input An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, arrays of clusters of numbers, or waveforms. Data Type Changes on FPGA When

Multiply

Returns the product of the inputs.

A waveform can only be multiplied by either another waveform or a scalar numeric value.

[IMAGE alt='1378' src='Multiply.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### input

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, arrays of clusters of numbers, or waveforms.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

This input appears only when you wire a waveform to input.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### product

Product of the inputs.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

The node produces this output according to standard error behavior.

This output appears only when you wire a waveform to input.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=natural-log-base.html language=enus -->
## TOPIC 00225: Base 10 Logarithm of e

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `natural-log-base.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/natural-log-base.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the value 0.43429448190325182.

Base 10 Logarithm of e

Represents the value 0.43429448190325182.

[IMAGE alt='1378' src='Literal.Numeric.Log10e.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=natural-log-of-pi.html language=enus -->
## TOPIC 00226: lnPi

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `natural-log-of-pi.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/natural-log-of-pi.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the value 1.1447298858494002.

lnPi

Represents the value 1.1447298858494002.

[IMAGE alt='1378' src='Literal.Numeric.lnPi.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=natural-log-of-ten.html language=enus -->
## TOPIC 00227: ln10

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `natural-log-of-ten.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/natural-log-of-ten.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the value 2.3025850929940459.

ln10

Represents the value 2.3025850929940459.

[IMAGE alt='1378' src='Literal.Numeric.ln10.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=natural-log-of-two.html language=enus -->
## TOPIC 00228: ln2

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `natural-log-of-two.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/natural-log-of-two.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the value 0.6931471805599453.

ln2

Represents the value 0.6931471805599453.

[IMAGE alt='1378' src='Literal.Numeric.ln2.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=natural-logarithm-base.html language=enus -->
## TOPIC 00229: e

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `natural-logarithm-base.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/natural-logarithm-base.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the value 2.7182818284590452.

e

Represents the value 2.7182818284590452.

[IMAGE alt='1378' src='Literal.Numeric.e.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=negate.html language=enus -->
## TOPIC 00230: Negate

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `negate.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/negate.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=negative-infinity.html language=enus -->
## TOPIC 00231: Negative Infinity

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `negative-infinity.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/negative-infinity.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the value negative infinity.

Negative Infinity

Represents the value negative infinity.

[IMAGE alt='1378' src='Literal.Numeric.Negative_Infinity.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=new-excel-report.html language=enus -->
## TOPIC 00232: New Excel Report

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `new-excel-report.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/new-excel-report.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Creates an Excel report file. The Excel report file contains one sheet named Report by default. sheet name Name of the Excel worksheet you want to create. If you use a template, LabVIEW will ignore sheet name and create worksheets with the worksheet names from the template. Report file Path and name

New Excel Report

Creates an Excel report file.

The Excel report file contains one sheet named 
 Report by default.

[IMAGE alt='connector_pane_image' src='New_Excel_Report.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

#### sheet name

Name of the Excel worksheet you want to create. If you use a
 template, LabVIEW will ignore **sheet name**and create worksheets with
 the worksheet names from the template.

**Default:**Report

[IMAGE alt='datatype_icon' src='/assets/img/cpath.png']

#### file

Path and name of the Excel report file, for example 
D:\MyFile.xlsx. The file extension must be 
*.xlsx.

[IMAGE alt='datatype_icon' src='/assets/img/cpath.png']

#### template

Path and name of the report template you created in Excel. The file extension must be 
*.xlsx, for example, 
D:\MyTemplate.xlsx. Use the template to display data in other chart types.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/ilabview_objectlvclass.png']

#### report

Reference to the Excel report.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

Excel Report

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=new-word-report.html language=enus -->
## TOPIC 00233: New Word Report (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `new-word-report.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/new-word-report.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Creates a Word report. file Path where you want to create a new Word report. The file extension must be .docx. New Word Report will overwrite existing reports at the specified path. template Path to the Word document to use as a template. The file extension must be .docx or .dotx. error in Error con

New Word Report

Creates a Word report.

[IMAGE alt='connector_pane_image' src='New_Word_Report.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cpath.png']

#### file

Path where you want to create a new Word report.

.docx

Note

New Word Report

[IMAGE alt='datatype_icon' src='/assets/img/cpath.png']

#### template

Path to the Word document to use as a template.

The file extension must be
 .docx or .dotx.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/ilabview_objectlvclass.png']

#### report

Reference to the Word report.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Where This Node Can Run:**

Desktop OS: Windows

FPGA:

Web Server:

Parent topic:

Word Report

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=not-a-number-path-refnum.html language=enus -->
## TOPIC 00234: Not a Number/Path/Refnum?

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `not-a-number-path-refnum.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/not-a-number-path-refnum.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns True if a value is not a number, not a path, or not a refnum. Otherwise, this node returns False. number/path/refnum An input to this operation. This input supports scalar numbers, paths, or refnums, or a cluster or array of numbers, paths, or refnums. not a number/path/refnum? Boolean resul

Not a Number/Path/Refnum?

Returns True if a value is not a number, not a path, or not a refnum. Otherwise, this node returns False.

[IMAGE alt='1378' src='IsNotANumberOrPathOrRefnum.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### number/path/refnum

An input to this operation.

This input supports scalar numbers, paths, or refnums, or a cluster or array of numbers, paths, or refnums.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### not a number/path/refnum?

Boolean result of the operation.

This output assumes the same data type structure as number/path/refnum.

Parent topic:

Comparison Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=not-and.html language=enus -->
## TOPIC 00235: NOT AND

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `not-and.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/not-and.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the logical NAND of the inputs. If all inputs are True, this node returns False. Otherwise, it returns True. This node performs bitwise operations on numeric inputs. input An input to the operation. This input can be any data type that contains only Boolean values, numbers, or error cluster

NOT AND

Computes the logical NAND of the inputs. If all inputs are True, this node returns False. Otherwise, it returns True.

This node performs bitwise operations on numeric inputs.

[IMAGE alt='1378' src='LogicalAnd.Not.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### input

An input to the operation.

This input can be any data type that contains only Boolean values, numbers, or error clusters, such as an array of numbers or a cluster of Booleans. If this input is an error cluster, the node uses only the 
 status element of the error cluster.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### logical NAND

The logical NAND of the inputs.

#### Examples

| input 0 | input 1 | logical NAND |
| --- | --- | --- |
| T | T | F |
| T | F | T |
| F | T | T |
| F | F | T |

Parent topic:

Boolean Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=not-equal-to-0.html language=enus -->
## TOPIC 00236: Not Equal to 0?

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `not-equal-to-0.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/not-equal-to-0.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns True if a value is not equal to 0. Otherwise, this node returns False. x An input to this operation. This input supports numeric scalar values, clusters, timestamp values, waveforms, and arrays of numbers. For waveforms, the node compares only the y values of this input. Data Type Changes on

Not Equal to 0?

Returns True if a value is not equal to 0. Otherwise, this node returns False.

[IMAGE alt='1378' src='IsNotEqualTo0.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports numeric scalar values, clusters, timestamp values, waveforms, and arrays of numbers.

For waveforms, the node compares only the y values of this input.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### x != 0?

Boolean result of the operation.

This output assumes the same data type structure as 
 x.

Parent topic:

Comparison Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=not-equal.html language=enus -->
## TOPIC 00237: Not Equal?

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `not-equal.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/not-equal.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=not-exclusive-or.html language=enus -->
## TOPIC 00238: NOT EXCLUSIVE OR

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `not-exclusive-or.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/not-exclusive-or.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the logical negation of the logical exclusive or (XOR) of the inputs. If all inputs are True or all inputs are False, this node returns True. Otherwise, it returns False. This node performs bitwise operations on numeric inputs. input An input to the operation. This input can be any data typ

NOT EXCLUSIVE OR

Computes the logical negation of the logical exclusive or (XOR) of the inputs. If all inputs are True or all inputs are False, this node returns True. Otherwise, it returns False.

This node performs bitwise operations on numeric inputs.

[IMAGE alt='1378' src='LogicalExclusiveOr.Not.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### input

An input to the operation.

This input can be any data type that contains only Boolean values, numbers, or error clusters, such as an array of numbers or a cluster of Booleans. If this input is an error cluster, the node uses only the 
 status element of the error cluster.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### logical NOT XOR

The logical negation of the logical exclusive or (XOR) of the inputs.

#### Examples

| input 0 | input 1 | logical NOT XOR |
| --- | --- | --- |
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | T |

Parent topic:

Boolean Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=not-or.html language=enus -->
## TOPIC 00239: NOT OR

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `not-or.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/not-or.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the logical NOR of the inputs. If all inputs are False, this node returns True. Otherwise, it returns False. This node performs bitwise operations on numeric inputs. input An input to the operation. This input can be any data type that contains only Boolean values, numbers, or error cluster

NOT OR

Computes the logical NOR of the inputs. If all inputs are False, this node returns True. Otherwise, it returns False.

This node performs bitwise operations on numeric inputs.

[IMAGE alt='1378' src='LogicalOr.Not.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### input

An input to the operation.

This input can be any data type that contains only Boolean values, numbers, or error clusters, such as an array of numbers or a cluster of Booleans. If this input is an error cluster, the node uses only the 
 status element of the error cluster.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### logical NOR

The logical NOR of the inputs.

#### Examples

| input 0 | input 1 | logical NOR |
| --- | --- | --- |
| T | T | F |
| T | F | F |
| F | T | F |
| F | F | T |

Parent topic:

Boolean Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=not.html language=enus -->
## TOPIC 00240: NOT

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `not.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/not.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the logical negation of the input. If the input is False, this node returns True. If the input is True, this node returns False. This node performs bitwise operations on numeric inputs. x The value to negate. This input can be any data type that contains only Boolean values, numbers, or err

NOT

Computes the logical negation of the input. If the input is False, this node returns True. If the input is True, this node returns False.

This node performs bitwise operations on numeric inputs.

[IMAGE alt='1378' src='Not.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### x

The value to negate.

This input can be any data type that contains only Boolean values, numbers, or error clusters, such as an array of numbers or a cluster of Booleans. If this input is an error cluster, the node uses only the 
 status element of the error cluster.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### NOT x

The logical negation of 
x.

#### Examples

| x | not x? |
| --- | --- |
| F | T |
| T | F |

Parent topic:

Boolean Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=number-to-boolean-array.html language=enus -->
## TOPIC 00241: Number to Boolean Array

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `number-to-boolean-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/number-to-boolean-array.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=number-to-decimal-string.html language=enus -->
## TOPIC 00242: Number to Decimal String

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `number-to-decimal-string.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/number-to-decimal-string.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=number-to-engineering-string.html language=enus -->
## TOPIC 00243: Number to Engineering String

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `number-to-engineering-string.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/number-to-engineering-string.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=number-to-exponential-string.html language=enus -->
## TOPIC 00244: Number to Exponential String

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `number-to-exponential-string.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/number-to-exponential-string.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=number-to-fractional-string.html language=enus -->
## TOPIC 00245: Number to Fractional String

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `number-to-fractional-string.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/number-to-fractional-string.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a numeric value to an F-format (fractional notation), floating-point string. number An input to this operation. This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Cha

Number to Fractional String

Converts a numeric value to an F-format (fractional notation), floating-point string.

[IMAGE alt='1378' src='NumberToFractionalString.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### number

An input to this operation.

This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

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

Default value: True

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### fractional format string

number represented as a fractional string.

This output can be 
 Inf, 
 -Inf, or 
 NaN if the value you wire to 
 number is infinity or is not a number.

#### Examples

number

width

precision

fractional format string

fractional format string

| number | width | precision | fractional format string | Comments |
| --- | --- | --- | --- | --- |
| 4.911 | 6 | 2 | _ _4.91 | number is rounded, padded with spaces on the left. |
| .003926 | 8 | 4 | _ _0.0039 | number is rounded, padded with spaces on the left. |
| -287.3 | 5 | 0 | _-287 | number is rounded, padded with spaces on the left. |

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=number-to-hexadecimal-string.html language=enus -->
## TOPIC 00246: Number to Hexadecimal String

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `number-to-hexadecimal-string.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/number-to-hexadecimal-string.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a numeric value to a string that shows the number's hexadecimal format. The digits A through F always appear in uppercase in the output string. number A number to be converted into a string. This input can also be any data type that contains only numbers, such as an array of numbers or a cl

Number to Hexadecimal String

Converts a numeric value to a string that shows the number's hexadecimal format.
 The digits 
**A** through 
**F** always appear in uppercase in the output string.

[IMAGE alt='1378' src='NumberToHexadecimalString.png']

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

##### hex integer string

number represented as a hexadecimal string.

#### Examples

number

width

hex integer string

| number | width | hex integer string | Comments |
| --- | --- | --- | --- |
| 3 | 4 | 0003 | If width is larger than needed, zeros are added on the left. |
| 42 | 3 | 02A | — |
| -4.2 | 3 | FFFFFFFC | -4.2 is rounded up to -4 in 64-bit integer format. width is too small to represent the hex version of a negative number, so the field width is extended. |

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=number-to-octal-string.html language=enus -->
## TOPIC 00247: Number to Octal String

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `number-to-octal-string.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/number-to-octal-string.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=numeric-constant.html language=enus -->
## TOPIC 00248: Numeric Constant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `numeric-constant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/numeric-constant.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a number on the diagram. Set this value by clicking inside the constant and typing a value.

Numeric Constant

Represents a number on the diagram.
 Set this value by clicking inside the constant and typing a value.

[IMAGE alt='1378' src='Literal.Numeric.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=numeric-nodes.html language=enus -->
## TOPIC 00249: Numeric Nodes

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `numeric-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/numeric-nodes.html
- document_id: `labview-nxg-nodes-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=numeric-scaling-nodes.html language=enus -->
## TOPIC 00250: Numeric Scaling Nodes (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `numeric-scaling-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/numeric-scaling-nodes.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `nodeCollection`

Numeric Scaling Nodes

Convert RTD Reading

Converts an RTD voltage into a temperature value in degrees Celsius.

Convert Strain Gauge Reading

Converts a strain gauge voltage to units of strain.

Convert Thermistor Reading

Converts a thermistor voltage into a temperature value.

Convert Thermocouple Reading

Converts a thermocouple voltage into a temperature value.
