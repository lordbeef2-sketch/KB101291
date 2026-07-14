# NI DOCUMENT BUNDLE: labview-nxg-fpga-module-cdl-api-ref

<!--NI_BUNDLE_CHUNK bundle=labview-nxg-fpga-module-cdl-api-ref start=251 end=293 -->
<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=swap-words.html language=enus -->
## TOPIC 00251: Swap Words

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `swap-words.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/swap-words.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Swaps the high-order 16 bits and the low-order 16 bits for every long integer in the specified input (data). data An integer, an array of integers, or a cluster containing integers that you want to word swap. In the case of a cluster that contains integers, this node swaps only the integer elements

Swap Words

Swaps the high-order 16 bits and the low-order 16 bits for every long integer in the specified input (data).

[IMAGE alt='1378' src='SwapWords.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### data

An integer, an array of integers, or a cluster containing integers that you want to word swap. In the case of a cluster that contains integers, this node swaps only the integer elements of the cluster.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### word swapped

An output of this operation with the same data type and structure as data.

Parent topic:

Data Manipulation Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=tag-constant.html language=enus -->
## TOPIC 00252: Tag Constant

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `tag-constant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/tag-constant.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a tag reference on the diagram. Use this constant to select the static tag reference from which to read or to which to write. What Is a Tag? A tag is single-point, latest value data that you can access from multiple documents within a project. A tag can store a single value of any data ty

Tag Constant

Represents a tag reference on the diagram.

Use this constant to select the static tag reference from which to read or to which to write.

[IMAGE alt='1378' src='Literal.IONameConstant.DataComms.TagEndpoint.png']

#### What Is a Tag?

A 
 *tag* is single-point, latest value data that you can access from multiple documents within a project. A tag can store a single value of any data type that represents the state of a process. Tags are similar to global variables in text-based programming languages.

You can create a tag either dynamically, using the Configure and Create Tag node on the diagram, or statically, in the shared resource collection file.

You can create a tag to access the same data from multiple VIs within a project.

#### What Is a Tag Proxy?

A 
 *tag proxy* is a reference that is local to part of the application that mirrors the value of the actual tag to which it is linked in another location in the application. You use a tag proxy to access data that is in another location in the application. You can read from and optionally write to a tag proxy only after the tag proxy links to a tag.

#### Using a Tag Constant

Complete the following steps to statically create and configure a tag.

1. Create or open a shared resource collection document. 
 org.dita.html5/xsl/topic.xsl 455 Note Shared resource collection documents have the 
 .grsc file extension.
2. Expand the 
 Tag section and click 
 Create New .
3. Configure the data type, initial value, and other properties of the tag in the 
 Item tab.

Parent topic:

FPGA Resource Constants

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=tag-nodes-scl.html language=enus -->
## TOPIC 00253: Tag Nodes

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `tag-nodes-scl.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/tag-nodes-scl.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Read from and write to a tag, which is single-point, latest value data that you can access from multiple documents within a project.

Tag Nodes

Read from and write to a tag, which is single-point, latest value data that you can access from multiple documents within a project.

Read Tag

Returns the data value stored in a tag.

Write Tag

Writes a data value to a tag, or to a tag proxy if it is configured to have write access.

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=tick-count-ms.html language=enus -->
## TOPIC 00254: Milliseconds

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `tick-count-ms.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/tick-count-ms.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value of the millisecond timer. millisecond timer value Value of the operating system's millisecond timer. Timer Count Time vs. Real-World Time The base reference time (millisecond zero) for this node is undefined, so you cannot convert the output value to a real-world time or date. Mill

Milliseconds

Returns the value of the millisecond timer.

[IMAGE alt='1378' src='TickCount.Milliseconds.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### millisecond timer value

Value of the operating system's millisecond timer.

#### Timer Count Time vs. Real-World Time

The base reference time (millisecond zero) for this node is undefined, so you cannot convert the output value to a real-world time or date.

#### Millisecond Timer Wrap Behavior

Be careful when you use this node in comparisons because the value of the millisecond timer wraps from 
 (2^32)-1 to 
 0. You can also change the value at which the millisecond timer wraps by changing the size of the output integer.

Parent topic:

Timer Count

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=tick-count-ticks.html language=enus -->
## TOPIC 00255: Ticks

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `tick-count-ticks.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/tick-count-ticks.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value of the tick timer. tick timer value Value of the operating system's tick timer. Timer Count Time vs. Real-World Time The base reference time (tick zero) for this node is undefined, so you cannot convert the output value to a real-world time or date. Tick Timer Wrap Behavior Be care

Ticks

Returns the value of the tick timer.

[IMAGE alt='1378' src='TickCount.Ticks.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### tick timer value

Value of the operating system's tick timer.

#### Timer Count Time vs. Real-World Time

The base reference time (tick zero) for this node is undefined, so you cannot convert the output value to a real-world time or date.

#### Tick Timer Wrap Behavior

Be careful when you use this node in comparisons because the value of the tick timer wraps from 
 (2^32)-1 to 
 0. You can also change the value at which the tick timer wraps by changing the size of the output integer.

Parent topic:

Timer Count

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=tick-count-us.html language=enus -->
## TOPIC 00256: Microseconds

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `tick-count-us.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/tick-count-us.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
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

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=tick-count.html language=enus -->
## TOPIC 00257: Timer Count

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `tick-count.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/tick-count.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value of the timer. Conref <swabstract> from the G Dataflow topic: GUID-82577A1B-A741-40A0-ABD3-16AF18F2AC60

Timer Count

Returns the value of the timer. Conref <swabstract> from the G Dataflow topic: GUID-82577A1B-A741-40A0-ABD3-16AF18F2AC60

Program Flow Nodes

Microseconds

Returns the value of the microsecond timer.

Milliseconds

Returns the value of the millisecond timer.

Ticks

Returns the value of the tick timer.

Parent topic:

Program Flow Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=to-complex-fixed-point.html language=enus -->
## TOPIC 00258: To Complex Fixed-Point

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `to-complex-fixed-point.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/to-complex-fixed-point.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts any number to complex fixed-point representation. complex fixed-point type The complex fixed-point data type to which you want to convert the input data. The software ignores the actual value of the constant or control that you wire to this input. number Any number. complex fixed-point The

To Complex Fixed-Point

Converts any number to complex fixed-point representation.

[IMAGE alt='1378' src='ToComplexFixedPoint.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cfxp.png']

##### complex fixed-point type

The complex fixed-point data type to which you want to convert the input data. The software ignores the actual value of the constant or control that you wire to this input.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### number

Any number.

[IMAGE alt='datatype_icon' src='/assets/img/ifxp.png']

##### complex fixed-point

The input data scaled to the complex fixed-point data type specified by complex fixed-point type.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### overflow

A Boolean that describes whether the result of the operation is outside the range of values that the output type can represent.

| True | Overflow occurred. Note For complex numbers, the output is True if either the real or imaginary parts overflow. |
| --- | --- |
| False | Overflow did not occur. |

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=to-double-precision-float.html language=enus -->
## TOPIC 00259: To Double Precision Float

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `to-double-precision-float.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/to-double-precision-float.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a number to a double-precision, floating-point number. number An input to this operation. This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. double precision float Result of th

To Double Precision Float

Converts a number to a double-precision, floating-point number.

[IMAGE alt='1378' src='ToDoublePrecisionFloat.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### number

An input to this operation.

This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### double precision float

Result of the conversion.

This output assumes the same data type structure as 
 number.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=to-fixed-point.html language=enus -->
## TOPIC 00260: To Fixed-Point

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `to-fixed-point.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/to-fixed-point.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts any non-complex number to fixed-point representation. If you do not wire a value to the fixed-point type input or configure the output settings of this function, the data type of the fixed-point output adapts to the data you wire to the number input. For example, if you wire an 8-bit unsign

To Fixed-Point

Converts any non-complex number to fixed-point representation.

If you do not wire a value to the 
 fixed-point type input or configure the output settings of this function, the data type of the 
 fixed-point output adapts to the data you wire to the 
 number input. For example, if you wire an 8-bit unsigned integer to the 
 number input, the program returns an 8-bit unsigned fixed-point number with 8 integer bits. This function saturates the number by default if overflow occurs.

[IMAGE alt='1378' src='ToFixedPoint.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### number

Any non-complex number.

[IMAGE alt='datatype_icon' src='/assets/img/cfxp.png']

##### fixed-point type

The fixed-point data type to which you want to convert the integer data. The program ignores any data in the constant or control that you wire to 
fixed-point type.

[IMAGE alt='datatype_icon' src='/assets/img/ifxp.png']

##### fixed-point

Is the input data scaled to the requested fixed-point data type.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### overflow

A Boolean that describes whether the result of the operation is outside the range of values that the output type can represent.

| True | Overflow occurred. Note For complex numbers, the output is True if either the real or imaginary parts overflow. |
| --- | --- |
| False | Overflow did not occur. |

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=to-more-generic-class.html language=enus -->
## TOPIC 00261: To More Generic Class

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `to-more-generic-class.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/to-more-generic-class.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Typecasts a class object or a class reference to a class above the object or reference in the inheritance hierarchy. You can use this node to typecast any object or reference in a class hierarchy, including VI Server references, .NET/ActiveX references, and classes you create. reference Class refere

To More Generic Class

Typecasts a class object or a class reference to a class above the object or reference in the inheritance hierarchy.

You can use this node to typecast any object or reference in a class hierarchy, including VI Server references, .NET/ActiveX references, and classes you create.

[IMAGE alt='1378' src='ToMoreGenericClass.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/clabview_objectlvclass.png']

##### reference

Class reference or class object you want to typecast to a target class within the inheritance hierarchy.

[IMAGE alt='datatype_icon' src='/assets/img/clabview_objectlvclass.png']

##### target class

Class you want reference to match.

[IMAGE alt='datatype_icon' src='/assets/img/ilabview_objectlvclass.png']

##### generic class reference

Class reference or class object typecast to the target class.

#### Typecasting Classes

Typecasting changes the data type of an input to that of the class you specify. This allows you to access the object or reference you input as if it is the target class you specify.

Parent topic:

Classes Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=to-more-specific-class.html language=enus -->
## TOPIC 00262: To More Specific Class

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `to-more-specific-class.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/to-more-specific-class.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Typecasts a class object or class reference to a class below the object or reference in the inheritance hierarchy. You can use this node to typecast any object or reference in a class hierarchy, including VI Server references, .NET/ActiveX references, and classes you create. reference Class referenc

To More Specific Class

Typecasts a class object or class reference to a class below the object or reference in the inheritance hierarchy.

You can use this node to typecast any object or reference in a class hierarchy, including VI Server references, .NET/ActiveX references, and classes you create.

[IMAGE alt='1378' src='ToMoreSpecificClass.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/clabview_objectlvclass.png']

##### reference

Class reference or class object you want to typecast to a target class within the inheritance hierarchy.

[IMAGE alt='datatype_icon' src='/assets/img/clabview_objectlvclass.png']

##### target class

Class you want reference to match.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ilabview_objectlvclass.png']

##### specific class reference

Class reference or class object typecast to the target class.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Typecasting Classes

Typecasting changes the data type of an input to that of the class you specify. This allows you to access the object or reference you input as if it is the target class you specify.

Parent topic:

Classes Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=to-signed-16-bit-integer.html language=enus -->
## TOPIC 00263: To Signed 16-bit Integer

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `to-signed-16-bit-integer.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/to-signed-16-bit-integer.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a number to a 16-bit integer in the range -32,768 to 32,767. number An input to this operation. This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. 16-bit integer Result of the

To Signed 16-bit Integer

Converts a number to a 16-bit integer in the range -32,768 to 32,767.

[IMAGE alt='1378' src='ToSigned16BitInteger.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### number

An input to this operation.

This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

[IMAGE alt='datatype_icon' src='/assets/img/ii16.png']

##### 16-bit integer

Result of the conversion.

This output assumes the same data type structure as 
 number.

#### Wrapping Behavior for Out-of-Range Values

If this node receives an input value that falls outside of the range of values that the output can represent, the node returns a value that wraps to the other end of the range. This differs from the behavior for nodes that convert values to unsigned integers.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=to-signed-32-bit-integer.html language=enus -->
## TOPIC 00264: To Signed 32-bit Integer

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `to-signed-32-bit-integer.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/to-signed-32-bit-integer.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a number to a 32-bit integer in the range -(2^31) to (2^31)-1. number An input to this operation. This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. 32-bit integer Result of th

To Signed 32-bit Integer

Converts a number to a 32-bit integer in the range -(2<sup>31</sup>) to (2<sup>31</sup>)-1.

[IMAGE alt='1378' src='ToSigned32BitInteger.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### number

An input to this operation.

This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### 32-bit integer

Result of the conversion.

This output assumes the same data type structure as 
 number.

#### Wrapping Behavior for Out-of-Range Values

If this node receives an input value that falls outside of the range of values that the output can represent, the node returns a value that wraps to the other end of the range. This differs from the behavior for nodes that convert values to unsigned integers.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=to-signed-64-bit-integer.html language=enus -->
## TOPIC 00265: To Signed 64-bit Integer

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `to-signed-64-bit-integer.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/to-signed-64-bit-integer.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a number to a 64-bit integer in the range -(2^63) to (2^63)-1. number An input to this operation. This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. 64-bit integer Result of th

To Signed 64-bit Integer

Converts a number to a 64-bit integer in the range -(2<sup>63</sup>) to (2<sup>63</sup>)-1.

[IMAGE alt='1378' src='ToSigned64BitInteger.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### number

An input to this operation.

This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

[IMAGE alt='datatype_icon' src='/assets/img/ii64.png']

##### 64-bit integer

Result of the conversion.

This output assumes the same data type structure as 
 number.

#### Wrapping Behavior for Out-of-Range Values

If this node receives an input value that falls outside of the range of values that the output can represent, the node returns a value that wraps to the other end of the range. This differs from the behavior for nodes that convert values to unsigned integers.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=to-signed-8-bit-integer.html language=enus -->
## TOPIC 00266: To Signed 8-bit Integer

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `to-signed-8-bit-integer.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/to-signed-8-bit-integer.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a number to an 8-bit integer in the range -128 to 127. number An input to this operation. This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. 8-bit integer Result of the convers

To Signed 8-bit Integer

Converts a number to an 8-bit integer in the range -128 to 127.

[IMAGE alt='1378' src='ToSigned8BitInteger.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### number

An input to this operation.

This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

[IMAGE alt='datatype_icon' src='/assets/img/ii8.png']

##### 8-bit integer

Result of the conversion.

This output assumes the same data type structure as 
 number.

#### Wrapping Behavior for Out-of-Range Values

If this node receives an input value that falls outside of the range of values that the output can represent, the node returns a value that wraps to the other end of the range. This differs from the behavior for nodes that convert values to unsigned integers.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=to-single-precision-float.html language=enus -->
## TOPIC 00267: To Single Precision Float

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `to-single-precision-float.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/to-single-precision-float.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a number to a single-precision, floating-point number. number An input to this operation. This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. single precision float Result of th

To Single Precision Float

Converts a number to a single-precision, floating-point number.

[IMAGE alt='1378' src='ToSinglePrecisionFloat.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### number

An input to this operation.

This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

[IMAGE alt='datatype_icon' src='/assets/img/isgl.png']

##### single precision float

Result of the conversion.

This output assumes the same data type structure as 
 number.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=to-unsigned-16-bit-integer.html language=enus -->
## TOPIC 00268: To Unsigned 16-bit Integer

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `to-unsigned-16-bit-integer.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/to-unsigned-16-bit-integer.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a number to a 16-bit unsigned integer in the range 0 to 65,535. number An input to this operation. This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. unsigned 16-bit integer Re

To Unsigned 16-bit Integer

Converts a number to a 16-bit unsigned integer in the range 0 to 65,535.

[IMAGE alt='1378' src='ToUnsigned16BitInteger.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### number

An input to this operation.

This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### unsigned 16-bit integer

Result of the conversion.

This output assumes the same data type structure as 
 number.

#### Rounding Behavior for Out-of-Range Values

If this node receives an input that falls outside the range of values that the output can represent, the node rounds the value to the closer end of the range. This differs from the out-of-range behavior for nodes that convert values to signed integers.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=to-unsigned-32-bit-integer.html language=enus -->
## TOPIC 00269: To Unsigned 32-bit Integer

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `to-unsigned-32-bit-integer.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/to-unsigned-32-bit-integer.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a number to a 32-bit unsigned integer in the range 0 to (2^32)-1. number An input to this operation. This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. unsigned 32-bit integer

To Unsigned 32-bit Integer

Converts a number to a 32-bit unsigned integer in the range 0 to (2^32)-1.

[IMAGE alt='1378' src='ToUnsigned32BitInteger.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### number

An input to this operation.

This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### unsigned 32-bit integer

Result of the conversion.

This output assumes the same data type structure as 
 number.

#### Rounding Behavior for Out-of-Range Values

If this node receives an input that falls outside the range of values that the output can represent, the node rounds the value to the closer end of the range. This differs from the out-of-range behavior for nodes that convert values to signed integers.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=to-unsigned-64-bit-integer.html language=enus -->
## TOPIC 00270: To Unsigned 64-bit Integer

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `to-unsigned-64-bit-integer.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/to-unsigned-64-bit-integer.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a number to a 64-bit integer in the range -(2^63) to (2^63)-1. number An input to this operation. This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. unsigned 64-bit integer Res

To Unsigned 64-bit Integer

Converts a number to a 64-bit integer in the range -(2<sup>63</sup>) to (2<sup>63</sup>)-1.

[IMAGE alt='1378' src='ToUnsigned64BitInteger.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### number

An input to this operation.

This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

##### unsigned 64-bit integer

Result of the conversion.

This output assumes the same data type structure as 
 number.

#### Rounding Behavior for Out-of-Range Values

If this node receives an input that falls outside the range of values that the output can represent, the node rounds the value to the closer end of the range. This differs from the out-of-range behavior for nodes that convert values to signed integers.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=to-unsigned-8-bit-integer.html language=enus -->
## TOPIC 00271: To Unsigned 8-bit Integer

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `to-unsigned-8-bit-integer.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/to-unsigned-8-bit-integer.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a number to an 8-bit unsigned integer in the range 0 to 255. number An input to this operation. This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. unsigned 8-bit integer Result

To Unsigned 8-bit Integer

Converts a number to an 8-bit unsigned integer in the range 0 to 255.

[IMAGE alt='1378' src='ToUnsigned8BitInteger.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### number

An input to this operation.

This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

[IMAGE alt='datatype_icon' src='/assets/img/iu8.png']

##### unsigned 8-bit integer

Result of the conversion.

This output assumes the same data type structure as 
 number.

#### Rounding Behavior for Out-of-Range Values

If this node receives an input that falls outside the range of values that the output can represent, the node rounds the value to the closer end of the range. This differs from the out-of-range behavior for nodes that convert values to signed integers.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=video-on-screen-display.html language=enus -->
## TOPIC 00272: Video On-Screen Display

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `video-on-screen-display.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/video-on-screen-display.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides a video processing block for alpha blending and compositing as well as simple text and graphics generation. This node supports up to eight layers using a combination of external video inputs (from frame buffer) and internal graphics controllers (including text generators). Image sizes are s

Video On-Screen Display

Provides a video processing block for alpha blending and compositing as well as simple text and graphics generation.

This node supports up to eight layers using a combination of external video inputs (from frame buffer) and internal graphics controllers (including text generators). Image sizes are supported up to 4k×4k with YUVA 4:4:4 or 4:2:2, and RGBA image formats up to 1080p 60fps. The core is programmable through a comprehensive register interface for setting and controlling screen size, background color, layer position, and more using logic or a microprocessor. Interrupt status bits are provided for processor monitoring. The LogiCORE has two different interfaces: General Purpose Processor and EDK Pcore (including device driver).

On the 
 **Item** tab, click 
 Configure Xilinx IP to configure inputs and outputs for this node.

Need License: Yes

Interface: AXI4, AXI4-Stream

Parent topic:

Xilinx Video and Image Processing Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=video-scaler.html language=enus -->
## TOPIC 00273: Video Scaler

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `video-scaler.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/video-scaler.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Spatially scales video streams in real time. It supports all SD and HD resolutions. The scaler is implemented as a polyphase filter that supports 2-12 H/V taps with programmable coefficients. You can select either a parameterizable dynamically-configurable AXI4-Lite netlist or a Constant interface n

Video Scaler

Spatially scales video streams in real time. It supports all SD and HD resolutions.
 The scaler is implemented as a polyphase filter that supports 2-12 H/V taps with programmable coefficients. You can select either a parameterizable dynamically-configurable AXI4-Lite netlist or a Constant interface netlist. The AXI4-Lite core enables a microprocessor or external state-machine to program scalar parameters and load coefficient sets in real time.

On the 
 **Item** tab, click 
 Configure Xilinx IP to configure inputs and outputs for this node.

Need License: Yes

Interface: AXI4-Stream, AXI4-Lite

[IMAGE alt='1378' src='XIPIN.VideoScale.png']

Parent topic:

Xilinx Video and Image Processing Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=video-timing-controller.html language=enus -->
## TOPIC 00274: Video Timing Controller

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `video-timing-controller.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/video-timing-controller.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides a general purpose video timing generator and detector. The controller provides automatic detection of horizontal and vertical front and back porches, sync pulses, and active video pixels along with sync and blank pulse polarity detection. The controller generates horizontal and vertical bla

Video Timing Controller

Provides a general purpose video timing generator and detector.
 The controller provides automatic detection of horizontal and vertical front and back porches, sync pulses, and active video pixels along with sync and blank pulse polarity detection. The controller generates horizontal and vertical blanking and sync pulses, including support for programmable pulse polarity. You can program the core through a comprehensive register set, which allows you to control various timing generation parameters, including horizontal and vertical front and back porch start, active video start, sync start, and more. A comprehensive set of interrupt status bits is provided for processor monitoring.

On the 
 **Item** tab, click 
 Configure Xilinx IP to configure inputs and outputs for this node.

Need License: Yes

Interface: AXI4-Lite

[IMAGE alt='1378' src='XIPIN.VideoTimControl.png']

Parent topic:

Xilinx Video and Image Processing Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=viterbi-decoder.html language=enus -->
## TOPIC 00275: Viterbi Decoder

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `viterbi-decoder.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/viterbi-decoder.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implements a fully synchronous Viterbi decoder, using a single clock. Options include parameterizable constraint length, convolutional codes, and traceback length. You can use various architectures including parallel, serial, multi-channel, and dual decoding. The core is delivered through the Xilinx

Viterbi Decoder

Implements a fully synchronous Viterbi decoder, using a single clock.
 Options include parameterizable constraint length, convolutional codes, and traceback length. You can use various architectures including parallel, serial, multi-channel, and dual decoding. The core is delivered through the Xilinx CORE Generator System and integrates with the Xilinx design flow.

On the 
 **Item** tab, click 
 Configure Xilinx IP to configure inputs and outputs for this node.

Need License: Yes

Interface: AXI4-Stream

[IMAGE alt='1378' src='XIPIN.ViterbiDec.png']

Parent topic:

Xilinx Communication and Networking Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=write-fifo.html language=enus -->
## TOPIC 00276: Write FIFO

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `write-fifo.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/write-fifo.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes an element to a FIFO. reference in Reference to the FIFO. data Data element to write to the FIFO. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error input valid Boole

Write FIFO

Writes an element to a FIFO.

[IMAGE alt='1378' src='FIFOWrite.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### reference in

Reference to the FIFO.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### data

Data element to write to the FIFO.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### input valid

Boolean value that describes whether the next data element has arrived for
 processing. Wire the output valid output of an upstream node to
 this input to transfer data from the upstream node to this node.

| True | The next data element has arrived for processing. |
| --- | --- |
| False | The next data element has not arrived for processing. |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### reference out

Reference to the FIFO.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### ready for input

Boolean value that indicates whether this node is ready to accept new input data.

Use Feedback Node to wire this output to the ready for
 output output of an upstream node.

| True | The node is ready to accept new input data. |
| --- | --- |
| False | The node is not ready to accept new input data. |

Note

input valid

#### Programming Patterns

[Transferring Data between Clock Domains Using FIFOs](/csh?topicname=transferring-data-clock-domains-fifo.html)

Parent topic:

FIFO Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=write-handshake.html language=enus -->
## TOPIC 00277: Write Handshake

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `write-handshake.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/write-handshake.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes an element of data to a handshake item. If the ready for input terminal returns False during a given cycle, this node discards any data that other nodes send to this node during the following cycle. This node discards this data even if input valid is True during the following cycle. reference

Write Handshake

Writes an element of data to a handshake item.

If the ready for input terminal returns False during a given cycle, this node discards any data that other nodes send to this node during the following cycle. This node discards this data even if input valid is True during the following cycle.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### reference in

Reference to a handshake item.

reference out

Handshake

reference in

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### data

The data to transfer using the handshake item.

data

Create Handshake

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### input valid

A Boolean that determines whether the next data point has arrived for processing. Wire the output valid output of an upstream node to this input to transfer data from the upstream node to this node.

| True | The next data point has arrived for processing. |
| --- | --- |
| False | The next data point has not arrived for processing. |

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### reference out

The same handshake reference wired into this node.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### ready for input

A Boolean that indicates whether the previous write operation is complete and the node is ready to accept data.

ready for output

| True | The previous write operation is complete and the node is ready to accept new input data. |
| --- | --- |
| False | The previous write operation is not complete and the node discards any data that other nodes send to this node during the following cycle. |

Parent topic:

Handshake Nodes

Related information:

- Handshaking Signals in Clock-Driven Logic

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=write-io.html language=enus -->
## TOPIC 00278: Write I/O

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `write-io.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/write-io.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a given value to the specified I/O resource. reference in Reference to an FPGA I/O item, used to specify a hardware resource. data The data to be written to the specified FPGA I/O resource. reference out Reference to an FPGA I/O item, used to specify a hardware resource.

Write I/O

Writes a given value to the specified I/O resource.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### reference in

Reference to an FPGA I/O item, used to specify a hardware resource.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### data

The data to be written to the specified FPGA I/O resource.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### reference out

Reference to an FPGA I/O item, used to specify a hardware resource.

Parent topic:

I/O Channels

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=write-memory.html language=enus -->
## TOPIC 00279: Write Memory

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `write-memory.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/write-memory.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes to memory available on the FPGA target. If you implement the memory item using block memory or look-up tables, you can read data only from the clock domain in which the memory is written. In these implementations, optimize your code by using only one writer node and one reader node for each m

Write Memory

Writes to memory available on the FPGA target.

If you implement the memory item using block memory or look-up tables,
 you can read data only from the clock domain in which the memory is written. In
 these implementations, optimize your code by using only one writer node and one
 reader node for each memory item. To read and write in a separate clock domain, use
 FIFOs or registers.

[IMAGE alt='1378' src='MemoryWrite.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### reference in

Reference to the memory item.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### address

Location to write data in memory on the FPGA target.

The valid address range depends on the requested number of elements you specify when creating the input memory item. For example, if you specify a requested number of elements of 65536, the valid address range is 0–65535. If address exceeds the address range, this node returns an error.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### data

Data to write to the memory on the FPGA target.

If the input memory item was configured as read-only, this node does not write the data to the memory.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### reference out

Reference to the memory item.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

[Transferring Data Using a Memory Item](/csh?topicname=accessing-stored-data-using-memory.html)

Parent topic:

Memory Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=write-register.html language=enus -->
## TOPIC 00280: Write Register

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `write-register.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/write-register.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a single value to a register available on the FPGA target. reference in Reference to the register item. data Data to write to the register on the FPGA target. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Stan

Write Register

Writes a single value to a register available on the FPGA target.

[IMAGE alt='1378' src='RegisterWrite.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### reference in

Reference to the register item.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### data

Data to write to the register on the FPGA target.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### reference out

Reference to the register item.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

[Transferring Data between Clock Domains Using Registers](/csh?topicname=transferring-data-clock-domians-registers.html)

Parent topic:

Register Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=write-tag.html language=enus -->
## TOPIC 00281: Write Tag

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `write-tag.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/write-tag.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a data value to a tag, or to a tag proxy if it is configured to have write access. tag/proxy ref in The reference to the tag endpoint, or tag proxy endpoint if configured to have write access, to which to write a data value. value The data value that this node writes to the tag or tag proxy.

Write Tag

Writes a data value to a tag, or to a tag proxy if it is configured to have write access.

[IMAGE alt='1378' src='TagWrite.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### tag/proxy ref in

The reference to the tag endpoint, or tag proxy endpoint if configured to have write access, to which to write a data value.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### value

The data value that this node writes to the tag or tag proxy.

##### Data Type of value

tag/proxy ref in

[IMAGE alt='datatype_icon' src='/assets/img/ctimestamp.png']

##### timestamp

The timestamp you want to associate with the data value that this node writes to the tag.

This input is available only if all of the following conditions are met:

- When you create the tag, you enable the 
 Has Timestamps? property.
- You wire a reference to that tag to tag ref in .

If you do not wire this input and 
 Has Timestamps? is enabled, this node automatically generates the current timestamp and associates it with the data value in the tag.

##### Associating Timestamps with Tag Data

Complete the following steps to associate a timestamp with the data value stored in a tag.

1. Navigate to the shared resource collection document where you created the tag and select the tag you want to modify. 
 org.dita.html5/xsl/topic.xsl 455 Note Shared resource collection documents have the 
 .grsc file extension.
2. On the 
 Item tab, enable the 
 Has Timestamps? checkbox.

If the tag contains an initial value, the tag now associates that value with the timestamp when the tag was created.

You can also associate a custom timestamp to the data value that you write to a tag. If you wire a timestamp to the Write Tag node when writing a new data value to a tag, the node then associates that timestamp with the new data value.

Note

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### tag/proxy ref out

The reference to the tag endpoint or tag proxy endpoint to which this node wrote a data value.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### What Is a Tag?

A 
 *tag* is single-point, latest value data that you can access from multiple documents within a project. A tag can store a single value of any data type that represents the state of a process. Tags are similar to global variables in text-based programming languages.

You can create a tag either dynamically, using the Configure and Create Tag node on the diagram, or statically, in the shared resource collection file.

You can create a tag to access the same data from multiple VIs within a project.

#### What Is a Tag Proxy?

A 
 *tag proxy* is a reference that is local to part of the application that mirrors the value of the actual tag to which it is linked in another location in the application. You use a tag proxy to access data that is in another location in the application. You can read from and optionally write to a tag proxy only after the tag proxy links to a tag.

#### Using a Tag Constant

Complete the following steps to statically create and configure a tag.

1. Create or open a shared resource collection document. 
 org.dita.html5/xsl/topic.xsl 455 Note Shared resource collection documents have the 
 .grsc file extension.
2. Expand the 
 Tag section and click 
 Create New .
3. Configure the data type, initial value, and other properties of the tag in the 
 Item tab.

Parent topic:

Tag Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=write-to-dram-byte-enables.html language=enus -->
## TOPIC 00282: Write to DRAM with Byte Enables

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `write-to-dram-byte-enables.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/write-to-dram-byte-enables.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes to DRAM memory available on the FPGA target. reference in Reference to a DRAM memory item. address Location to write data in memory on the FPGA target. The valid address range depends on the requested number of elements you specify when creating the input memory item. For example, if you spec

Write to DRAM with Byte Enables

Writes to DRAM memory available on the FPGA target.

[IMAGE alt='1378' src='DramWriteByteEnables.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### reference in

Reference to a DRAM memory item.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### address

Location to write data in memory on the FPGA target.

The valid address range depends on the requested number of elements you specify when creating the input memory item. For example, if you specify a requested number of elements of 65536, the valid address range is 0–65535. If address exceeds the address range, this node returns an error.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### data

The data to write to the DRAM memory on the FPGA target.

[IMAGE alt='datatype_icon' src='/assets/img/cu64.png']

##### byte enables

Bytes of memory at the 
address to overwrite with 
data. Each bit of the binary representation of the integer corresponds to a byte of data at the 
address. If the bit is 
1, the node overwrites the corresponding byte of memory. If the bit is 
0, the corresponding byte retains the previous value. If the memory is only 256 bits wide, the node only processes the lower 32 bits of the 
byte enables.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### input valid

Boolean value that specifies whether the next data point is valid and can be processed.

Wire output valid of an upstream node to this input to transfer data from the upstream node to this node.

| True | The data point is valid and can be processed. |
| --- | --- |
| False | The data point is not valid. |

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### reference out

Reference to a DRAM memory item.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### ready for input

Boolean value that indicates whether this node is ready to accept new input data.

Use Feedback Node to wire this output to the ready for
 output output of an upstream node.

| True | The node is ready to accept new input data. |
| --- | --- |
| False | The node is not ready to accept new input data. |

Note

input valid

Parent topic:

DRAM Memory Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=write-to-dram.html language=enus -->
## TOPIC 00283: Write to DRAM

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `write-to-dram.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/write-to-dram.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes to DRAM memory available on the FPGA target. reference in Reference to a DRAM memory item. address Location to write data in memory on the FPGA target. The valid address range depends on the requested number of elements you specify when creating the input memory item. For example, if you spec

Write to DRAM

Writes to DRAM memory available on the FPGA target.

[IMAGE alt='1378' src='DramWrite.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### reference in

Reference to a DRAM memory item.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### address

Location to write data in memory on the FPGA target.

The valid address range depends on the requested number of elements you specify when creating the input memory item. For example, if you specify a requested number of elements of 65536, the valid address range is 0–65535. If address exceeds the address range, this node returns an error.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### data

The data to write to the DRAM memory on the FPGA target.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### input valid

Boolean value that specifies whether the next data point is valid and can be processed.

Wire output valid of an upstream node to this input to transfer data from the upstream node to this node.

| True | The data point is valid and can be processed. |
| --- | --- |
| False | The data point is not valid. |

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### reference out

Reference to a DRAM memory item.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### ready for input

Boolean value that indicates whether this node is ready to accept new input data.

Use Feedback Node to wire this output to the ready for
 output output of an upstream node.

| True | The node is ready to accept new input data. |
| --- | --- |
| False | The node is not ready to accept new input data. |

Note

input valid

Parent topic:

DRAM Memory Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=xilinx-axi-infra.html language=enus -->
## TOPIC 00284: Xilinx AXI Infrastructure Nodes

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `xilinx-axi-infra.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/xilinx-axi-infra.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Build AXI-based applications or systems.

Xilinx AXI Infrastructure Nodes

Build AXI-based applications or systems.

Xilinx CORE Generator IP Nodes

Implement various Xilinx IP functions.

AXI4-Stream Subset Converter

Provides the infrastructure to change the AXI4-Stream interface characteristics between an AXI4-Stream master and slave.

AXI4-Stream Broadcaster

Provides the ability to replicate one SI stream onto multiple MI stream channels.

AXI4-Stream Combiner

Provides the ability to merge multiple SI streams onto one MI stream channel.

AXI4-Stream Data FIFO

Provides the infrastructure to insert buffering between an AXI4-Stream master and slave.

AXI4-Stream Data Width Converter

Provides the infrastructure to change the data path width between an AXI4-Stream master and slave.

AXI4-Stream Protocol Checker

Monitors AXI interfaces. When attached to an interface, this node actively checks for protocol violations and provides an indication of which violation occurred.

AXI4-Stream Register Slice

Provides the infrastructure to insert a pipeline stage between an AXI4-Stream master and slave.

AXI4-Stream Switch

Provides the infrastructure to connect multiple AXI4-Stream masters and slaves.

Parent topic:

Xilinx CORE Generator IP Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=xilinx-comm-network.html language=enus -->
## TOPIC 00285: Xilinx Communication and Networking Nodes

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `xilinx-comm-network.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/xilinx-comm-network.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implement IP related to telecommunication and wireless applications.

Xilinx Communication and Networking Nodes

Implement IP related to telecommunication and wireless applications.

Xilinx CORE Generator IP Nodes

Implement various Xilinx IP functions.

Convolution Encoder

Implements a high-speed, compact convolutional encoder with a puncturing option.

Interleaver/De-interleaver

Implements either the Forney Convolutional or Rectangular Block type architecture.

Peak Cancellation Crest Factor Reduction

Provides a flexible and highly efficient solution to reduce the peak to average power ratio (PAR) of complex multi-carrier waveforms.

Reed-Solomon Decoder

Implements many different Reed-Solomon coding standards.

Reed-Solomon Encoder

Implements many different Reed-Solomon coding standards.

Viterbi Decoder

Implements a fully synchronous Viterbi decoder, using a single clock.

Xilinx 3GPP Nodes

Implement IP related to 3GPP standards.

Xilinx LTE Nodes

Implement IP related to LTE standards.

Parent topic:

Xilinx CORE Generator IP Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=xilinx-data-storage.html language=enus -->
## TOPIC 00286: Xilinx IP Data Storage

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `xilinx-data-storage.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/xilinx-data-storage.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implement IP related to FIFOs, RAMs, and ROMs.

Xilinx IP Data Storage

Implement IP related to FIFOs, RAMs, and ROMs.

Xilinx CORE Generator IP Nodes

Implement various Xilinx IP functions.

Block Memory Generator

Replaces the Dual Port Block Memory and Single Port Block Memory LogiCOREs, but is not a direct drop-in replacement. Use this generator in all new Xilinx designs.

Distributed Memory Generator

Creates area and performance optimized ROM blocks, single and dual port distributed memories, and SRL16-based memories for Xilinx FPGAs.

FIFO Generator

Generates resource and performance optimized FIFOs with common or independent read/write clock domains, and optional fixed or programmable full and empty flags and handshaking signals.

RAM-based Shift Register

Generates fast, compact FIFO-style registers, delay lines, or time-skew buffers up to 256 bits wide and up to 1024 words deep using Select RAM in SRL16 or SRLC32 mode.

Parent topic:

Xilinx CORE Generator IP Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=xilinx-math.html language=enus -->
## TOPIC 00287: Xilinx Math Nodes

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `xilinx-math.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/xilinx-math.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implement IP for various mathematical and floating-point operations.

Xilinx Math Nodes

Implement IP for various mathematical and floating-point operations.

Xilinx CORE Generator IP Nodes

Implement various Xilinx IP functions.

Accumulator

Generates adder-, subtractor-, and adder/subtractor-based accumulators operating on signed or unsigned input.

Adder Subtracter

Creates adders, subtracters, and adders/subtracters that operate on signed or unsigned data.

Complex Multiplier

Represents all operands and results as signed two's-complement data.

CORDIC

Generates the generalized coordinate rotational digital computer (CORDIC) algorithm that iteratively solves trigonometric, hyperbolic, and square root equations.

Divider Generator

Provides division using the Radix-2 or High Radix algorithms.

DSP48 macro

Allows you to specify multiple operations using arithmetic expressions you define to abstract the XtremeDSP Slice configuration and simplify its dynamic operation.

Floating-point

Provides a range of floating-point operations, such as addition, subtraction, multiplication, division, reciprocal, square-root, reciprocal-square-root, absolute value, logarithm, compare, and conversion operations.

Multiplier

Generates parallel and constant-coefficient multipliers.

Multiply Adder

TM

Parent topic:

Xilinx CORE Generator IP Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=xilinx-nodes.html language=enus -->
## TOPIC 00288: Xilinx CORE Generator IP Nodes

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `xilinx-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/xilinx-nodes.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implement various Xilinx IP functions.

Xilinx CORE Generator IP Nodes

Implement various Xilinx IP functions.

Xilinx AXI Infrastructure Nodes

Build AXI-based applications or systems.

Xilinx Communication and Networking Nodes

Implement IP related to telecommunication and wireless applications.

Xilinx IP Data Storage

Implement IP related to FIFOs, RAMs, and ROMs.

Xilinx Math Nodes

Implement IP for various mathematical and floating-point operations.

Xilinx Signal Generation Nodes

Implement IP related to signal generation.

Xilinx Signal Processing Nodes

Implement IP such as filters, transforms, and modulation.

Video Connectivity

Implement IP related to streaming video.

Xilinx Video and Image Processing Nodes

Implement IP such as color correction, video timing, and color space conversion.

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=xilinx-sig-gen.html language=enus -->
## TOPIC 00289: Xilinx Signal Generation Nodes

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `xilinx-sig-gen.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/xilinx-sig-gen.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implement IP related to signal generation.

Xilinx Signal Generation Nodes

Implement IP related to signal generation.

Xilinx CORE Generator IP Nodes

Implement various Xilinx IP functions.

Binary Counter

Creates up counters, down counters, and up/down counters with output widths ranging up to 256 bits.

DDS Compiler

Provides Direct Digital Synthesizers (DDS) and optionally either Phase Generator or Sine/Cosine Lookup Table constituent parts as independent cores.

Parent topic:

Xilinx CORE Generator IP Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=xilinx-sig-proc.html language=enus -->
## TOPIC 00290: Xilinx Signal Processing Nodes

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `xilinx-sig-proc.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/xilinx-sig-proc.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implement IP such as filters, transforms, and modulation.

Xilinx Signal Processing Nodes

Implement IP such as filters, transforms, and modulation.

Xilinx CORE Generator IP Nodes

Implement various Xilinx IP functions.

CIC Compiler

Designs and implements Cascaded Integrator-Comb (CIC) filters for a variety of Xilinx FPGA devices.

Discrete Fourier Transform

Performs a discrete Fourier transform as defined by the LTE standard, in terms of point sizes, low latency, and resource requirements.

DUC/DDC Compiler

Implements Digital Up Converters (DUCs) and Digital Down Converters (DDCs) for a range of wireless interface standards based on system-level parameters.

Fast Fourier Transform

Computes the Discrete Fourier Transform (DFT).

FIR Compiler

Generates configurable high-speed, compact filter implementations.

Parent topic:

Xilinx CORE Generator IP Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=xilinx-video-connect.html language=enus -->
## TOPIC 00291: Video Connectivity

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `xilinx-video-connect.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/xilinx-video-connect.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implement IP related to streaming video.

Video Connectivity

Implement IP related to streaming video.

Xilinx CORE Generator IP Nodes

Implement various Xilinx IP functions.

ST2022-56 De-packetizer

Implement IP using ST2022-56 protocols.

ST2022-56 Packetizer

Implement IP using ST2022-56 protocols.

Parent topic:

Xilinx CORE Generator IP Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=xilinx-video-image-proc.html language=enus -->
## TOPIC 00292: Xilinx Video and Image Processing Nodes

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `xilinx-video-image-proc.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/xilinx-video-image-proc.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implement IP such as color correction, video timing, and color space conversion.

Xilinx Video and Image Processing Nodes

Implement IP such as color correction, video timing, and color space conversion.

Xilinx CORE Generator IP Nodes

Implement various Xilinx IP functions.

AXI Video Direct Memory Access

Provides an interface for controlling and synchronizing video frame stores from external memory.

Color Correction Matrix

Corrects color operations, such as white balance, color cast, brightness, or contrast in an RGB image.

Color Filter Array Interpolation

Reconstructs RGB data from color image sensors equipped with a Bayer Color Filter Array.

Gamma Correction

Manipulates pixel values.

Image Edge Enhancement

Provides edge enhancement of each frame of video data being processed.

RGB to YCrCb Color-Space Converter

Provides built-in support for 5 formats and 3 range standards.

Video On-Screen Display

Provides a video processing block for alpha blending and compositing as well as simple text and graphics generation.

Video Scaler

Spatially scales video streams in real time. It supports all SD and HD resolutions.

Video Timing Controller

Provides a general purpose video timing generator and detector.

YCrCb to RGB Color-Space Converter

Provides built-in support for 4 video standards and 3 input ranges.

Parent topic:

Xilinx CORE Generator IP Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-api-ref path=ycrcb-to-rgb-color-space-converter.html language=enus -->
## TOPIC 00293: YCrCb to RGB Color-Space Converter

- bundle_id: `labview-nxg-fpga-module-cdl-api-ref`
- source_path: `ycrcb-to-rgb-color-space-converter.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-api-ref/raw/resource/enus/ycrcb-to-rgb-color-space-converter.html
- document_id: `labview-nxg-fpga-module-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides built-in support for 4 video standards and 3 input ranges. The implementation is a simplified 3x3 constant coefficient matrix multiplier, which uses only 4 multipliers exploiting the inter-relations of color-space conversion coefficients. The module is optimized to take advantage of multipl

YCrCb to RGB Color-Space Converter

Provides built-in support for 4 video standards and 3 input ranges.
 The implementation is a simplified 3x3 constant coefficient matrix multiplier, which uses only 4 multipliers exploiting the inter-relations of color-space conversion coefficients. The module is optimized to take advantage of multiply-add capabilities of DSP slices.

On the 
 **Item** tab, click 
 Configure Xilinx IP to configure inputs and outputs for this node.

Need License: No

Interface: AXI4-Stream, AXI4-Lite

[IMAGE alt='1378' src='XIPIN.YCrCbtoRGB.png']

Parent topic:

Xilinx Video and Image Processing Nodes
