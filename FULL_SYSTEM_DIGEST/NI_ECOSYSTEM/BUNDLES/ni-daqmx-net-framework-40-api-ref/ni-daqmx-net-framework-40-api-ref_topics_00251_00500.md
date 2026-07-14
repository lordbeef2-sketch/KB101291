# NI DOCUMENT BUNDLE: ni-daqmx-net-framework-40-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-daqmx-net-framework-40-api-ref start=251 end=500 -->
<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_readmultisampleportint32.htm language=enus -->
## TOPIC 00251: DigitalSingleChannelReaderReadMultiSamplePortInt32 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_readmultisampleportint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_readmultisampleportint32.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.ReadMultiSamplePortInt32 Method

### DigitalSingleChannelReaderReadMultiSamplePortInt32 Method

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public int[] ReadMultiSamplePortInt32(
	int numberOfSamples
)
```

```text
Public Function ReadMultiSamplePortInt32 ( 
	numberOfSamples As Integer
) As Integer()
```

###### Parameters

- **numberOfSamples**
  - Type: SystemInt32 The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.

###### Return Value

Int32

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

Use this method for devices with up to 32 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

DigitalSingleChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_readsinglesampleportint16.htm language=enus -->
## TOPIC 00252: DigitalSingleChannelReaderReadSingleSamplePortInt16 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_readsinglesampleportint16.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_readsinglesampleportint16.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.ReadSingleSamplePortInt16 Method

### DigitalSingleChannelReaderReadSingleSamplePortInt16 Method

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public short ReadSingleSamplePortInt16()
```

```text
Public Function ReadSingleSamplePortInt16 As Short
```

###### Return Value

Int16

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

##### See Also

###### Reference

DigitalSingleChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_readsinglesampleportint32.htm language=enus -->
## TOPIC 00253: DigitalSingleChannelReaderReadSingleSamplePortInt32 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_readsinglesampleportint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_readsinglesampleportint32.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.ReadSingleSamplePortInt32 Method

### DigitalSingleChannelReaderReadSingleSamplePortInt32 Method

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public int ReadSingleSamplePortInt32()
```

```text
Public Function ReadSingleSamplePortInt32 As Integer
```

###### Return Value

Int32

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

##### See Also

###### Reference

DigitalSingleChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_readsinglesampleportuint16.htm language=enus -->
## TOPIC 00254: DigitalSingleChannelReaderReadSingleSamplePortUInt16 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_readsinglesampleportuint16.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_readsinglesampleportuint16.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.ReadSingleSamplePortUInt16 Method

### DigitalSingleChannelReaderReadSingleSamplePortUInt16 Method

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public ushort ReadSingleSamplePortUInt16()
```

```text
Public Function ReadSingleSamplePortUInt16 As UShort
```

###### Return Value

UInt16

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

##### See Also

###### Reference

DigitalSingleChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_readsinglesampleportuint32.htm language=enus -->
## TOPIC 00255: DigitalSingleChannelReaderReadSingleSamplePortUInt32 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_readsinglesampleportuint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_readsinglesampleportuint32.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.ReadSingleSamplePortUInt32 Method

### DigitalSingleChannelReaderReadSingleSamplePortUInt32 Method

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public uint ReadSingleSamplePortUInt32()
```

```text
Public Function ReadSingleSamplePortUInt32 As UInteger
```

###### Return Value

UInt32

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

##### See Also

###### Reference

DigitalSingleChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_readsinglesamplesingleline.htm language=enus -->
## TOPIC 00256: DigitalSingleChannelReaderReadSingleSampleSingleLine Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_readsinglesamplesingleline.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_readsinglesamplesingleline.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.ReadSingleSampleSingleLine Method

### DigitalSingleChannelReaderReadSingleSampleSingleLine Method

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool ReadSingleSampleSingleLine()
```

```text
Public Function ReadSingleSampleSingleLine As Boolean
```

###### Return Value

Boolean

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

Timeout

##### See Also

###### Reference

DigitalSingleChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_readwaveform.htm language=enus -->
## TOPIC 00257: DigitalSingleChannelReaderReadWaveform Method (Int32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_readwaveform.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_readwaveform.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.ReadWaveform Method (Int32)

### DigitalSingleChannelReaderReadWaveform Method (Int32)

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public DigitalWaveform ReadWaveform(
	int numberOfSamples
)
```

```text
Public Function ReadWaveform ( 
	numberOfSamples As Integer
) As DigitalWaveform
```

###### Parameters

- **numberOfSamples**
  - Type: SystemInt32 The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.

###### Return Value

DigitalWaveform

DigitalWaveform

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

The data returned from digital waveform reads is affected by the [WaveformAttributeMode](p_nationalinstruments_daqmx_daqstream_waveformattributemode.htm) property of the [DaqStream](t_nationalinstruments_daqmx_daqstream.htm) you are reading from.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

DigitalSingleChannelReader Class

ReadWaveform Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_readwaveform_1.htm language=enus -->
## TOPIC 00258: DigitalSingleChannelReaderReadWaveform Method (TimeSpan)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_readwaveform_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_readwaveform_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.ReadWaveform Method (TimeSpan)

### DigitalSingleChannelReaderReadWaveform Method (TimeSpan)

DIChannel

duration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public DigitalWaveform ReadWaveform(
	TimeSpan duration
)
```

```text
Public Function ReadWaveform ( 
	duration As TimeSpan
) As DigitalWaveform
```

###### Parameters

- **duration**
  - Type: SystemTimeSpanThe duration of time to read the waveform. The duration specified must be long enough to read at least one sample at the configured SampleClockRate.

###### Return Value

DigitalWaveform

DigitalWaveform

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | If the duration provided was less than Zero. |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

DAQ Assistant

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](p_nationalinstruments_daqmx_daqstream_waveformattributemode.htm) property of the [DaqStream](t_nationalinstruments_daqmx_daqstream.htm) being read.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the [Stream](p_nationalinstruments_daqmx_task_stream.htm) object used for the reads or writes.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

DigitalSingleChannelReader Class

ReadWaveform Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_tostring.htm language=enus -->
## TOPIC 00259: DigitalSingleChannelReaderToString Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_tostring.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.ToString Method

### DigitalSingleChannelReaderToString Method

Returns a string representation of the object.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

##### See Also

###### Reference

DigitalSingleChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelwriter__ctor.htm language=enus -->
## TOPIC 00260: DigitalSingleChannelWriter Constructor

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelwriter__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelwriter__ctor.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelWriter Constructor

### DigitalSingleChannelWriter Constructor

DigitalSingleChannelWriter

DaqStream

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public DigitalSingleChannelWriter(
	DaqStream stream
)
```

```text
Public Sub New ( 
	stream As DaqStream
)
```

###### Parameters

- **stream**
  - Type: NationalInstruments.DAQmxDaqStreamThe DaqStream to write to.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Task

Stream

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

##### See Also

###### Reference

DigitalSingleChannelWriter Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelwriter_beginwritesinglesampleport.htm language=enus -->
## TOPIC 00261: DigitalSingleChannelWriterBeginWriteSingleSamplePort Method (Boolean, Byte, AsyncCallback, Object)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelwriter_beginwritesinglesampleport.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelwriter_beginwritesinglesampleport.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelWriter.BeginWriteSingleSamplePort Method (Boolean, Byte, AsyncCallback, Object)

### DigitalSingleChannelWriterBeginWriteSingleSamplePort Method (Boolean, Byte, AsyncCallback, Object)

DOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginWriteSingleSamplePort(
	bool autoStart,
	byte data,
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginWriteSingleSamplePort ( 
	autoStart As Boolean,
	data As Byte,
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemByteA sample to write to the task.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the write is complete. Specify if you do not want a callback when the write is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](m_nationalinstruments_daqmx_digitalsinglechannelwriter_endwrite.htm) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalSingleChannelWriter Class

BeginWriteSingleSamplePort Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelwriter_beginwritesinglesampleport_2.htm language=enus -->
## TOPIC 00262: DigitalSingleChannelWriterBeginWriteSingleSamplePort Method (Boolean, Int32, AsyncCallback, Object)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelwriter_beginwritesinglesampleport_2.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelwriter_beginwritesinglesampleport_2.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelWriter.BeginWriteSingleSamplePort Method (Boolean, Int32, AsyncCallback, Object)

### DigitalSingleChannelWriterBeginWriteSingleSamplePort Method (Boolean, Int32, AsyncCallback, Object)

DOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginWriteSingleSamplePort(
	bool autoStart,
	int data,
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginWriteSingleSamplePort ( 
	autoStart As Boolean,
	data As Integer,
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemInt32A sample to write to the task.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the write is complete. Specify if you do not want a callback when the write is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](m_nationalinstruments_daqmx_digitalsinglechannelwriter_endwrite.htm) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalSingleChannelWriter Class

BeginWriteSingleSamplePort Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelwriter_beginwritesinglesampleport_3.htm language=enus -->
## TOPIC 00263: DigitalSingleChannelWriterBeginWriteSingleSamplePort Method (Boolean, UInt16, AsyncCallback, Object)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelwriter_beginwritesinglesampleport_3.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelwriter_beginwritesinglesampleport_3.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelWriter.BeginWriteSingleSamplePort Method (Boolean, UInt16, AsyncCallback, Object)

### DigitalSingleChannelWriterBeginWriteSingleSamplePort Method (Boolean, UInt16, AsyncCallback, Object)

DOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginWriteSingleSamplePort(
	bool autoStart,
	ushort data,
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginWriteSingleSamplePort ( 
	autoStart As Boolean,
	data As UShort,
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemUInt16A sample to write to the task.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the write is complete. Specify if you do not want a callback when the write is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](m_nationalinstruments_daqmx_digitalsinglechannelwriter_endwrite.htm) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalSingleChannelWriter Class

BeginWriteSingleSamplePort Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelwriter_beginwritesinglesampleport_4.htm language=enus -->
## TOPIC 00264: DigitalSingleChannelWriterBeginWriteSingleSamplePort Method (Boolean, UInt32, AsyncCallback, Object)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelwriter_beginwritesinglesampleport_4.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelwriter_beginwritesinglesampleport_4.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelWriter.BeginWriteSingleSamplePort Method (Boolean, UInt32, AsyncCallback, Object)

### DigitalSingleChannelWriterBeginWriteSingleSamplePort Method (Boolean, UInt32, AsyncCallback, Object)

DOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginWriteSingleSamplePort(
	bool autoStart,
	uint data,
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginWriteSingleSamplePort ( 
	autoStart As Boolean,
	data As UInteger,
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemUInt32A sample to write to the task.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the write is complete. Specify if you do not want a callback when the write is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](m_nationalinstruments_daqmx_digitalsinglechannelwriter_endwrite.htm) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalSingleChannelWriter Class

BeginWriteSingleSamplePort Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelwriter_beginwritesinglesamplesingleline.htm language=enus -->
## TOPIC 00265: DigitalSingleChannelWriterBeginWriteSingleSampleSingleLine Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelwriter_beginwritesinglesamplesingleline.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelwriter_beginwritesinglesamplesingleline.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelWriter.BeginWriteSingleSampleSingleLine Method

### DigitalSingleChannelWriterBeginWriteSingleSampleSingleLine Method

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginWriteSingleSampleSingleLine(
	bool autoStart,
	bool data,
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginWriteSingleSampleSingleLine ( 
	autoStart As Boolean,
	data As Boolean,
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemBooleanA Boolean sample to write to the task.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the write is complete. Specify if you do not want a callback when the write is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](m_nationalinstruments_daqmx_digitalsinglechannelwriter_endwrite.htm) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalSingleChannelWriter Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelwriter_beginwritewaveform.htm language=enus -->
## TOPIC 00266: DigitalSingleChannelWriterBeginWriteWaveform Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelwriter_beginwritewaveform.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelwriter_beginwritewaveform.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelWriter.BeginWriteWaveform Method

### DigitalSingleChannelWriterBeginWriteWaveform Method

DOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginWriteWaveform(
	bool autoStart,
	DigitalWaveform data,
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginWriteWaveform ( 
	autoStart As Boolean,
	data As DigitalWaveform,
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: NationalInstrumentsDigitalWaveformA DigitalWaveform to write to the task. The order of the lines in the digital waveform corresponds to the order in which you add the lines to the channel.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the write is complete. Specify if you do not want a callback when the write is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](m_nationalinstruments_daqmx_digitalsinglechannelwriter_endwrite.htm) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

Digital waveform writes are not affected by the SampleInterval or StartTime properties on the DigitalWaveform. To configure timing for digital waveform writes, use the [ConfigureSampleClock](overload_nationalinstruments_daqmx_timing_configuresampleclock.htm) method.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalSingleChannelWriter Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelwriter_writemultisampleport_3.htm language=enus -->
## TOPIC 00267: DigitalSingleChannelWriterWriteMultiSamplePort Method (Boolean, UInt16)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelwriter_writemultisampleport_3.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelwriter_writemultisampleport_3.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelWriter.WriteMultiSamplePort Method (Boolean, UInt16[])

### DigitalSingleChannelWriterWriteMultiSamplePort Method (Boolean, UInt16)

DOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void WriteMultiSamplePort(
	bool autoStart,
	ushort[] data
)
```

```text
Public Sub WriteMultiSamplePort ( 
	autoStart As Boolean,
	data As UShort()
)
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemUInt16A 1D array of samples to write to the task. Each element of the array corresponds to a channel in the task.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

##### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

##### See Also

###### Reference

DigitalSingleChannelWriter Class

WriteMultiSamplePort Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelwriter_writesinglesampleport_4.htm language=enus -->
## TOPIC 00268: DigitalSingleChannelWriterWriteSingleSamplePort Method (Boolean, UInt32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelwriter_writesinglesampleport_4.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelwriter_writesinglesampleport_4.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelWriter.WriteSingleSamplePort Method (Boolean, UInt32)

### DigitalSingleChannelWriterWriteSingleSamplePort Method (Boolean, UInt32)

DOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void WriteSingleSamplePort(
	bool autoStart,
	uint data
)
```

```text
Public Sub WriteSingleSamplePort ( 
	autoStart As Boolean,
	data As UInteger
)
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemUInt32A sample to write to the task.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

##### See Also

###### Reference

DigitalSingleChannelWriter Class

WriteSingleSamplePort Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_dochannelcollection_getenumerator.htm language=enus -->
## TOPIC 00269: DOChannelCollectionGetEnumerator Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_dochannelcollection_getenumerator.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_dochannelcollection_getenumerator.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DOChannelCollection.GetEnumerator Method

### DOChannelCollectionGetEnumerator Method

Returns an enumerator that you can use to iterate through the collection.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public virtual IEnumerator GetEnumerator()
```

```text
Public Overridable Function GetEnumerator As IEnumerator
```

###### Return Value

IEnumerator

###### Implements

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

##### See Also

###### Reference

DOChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_dochannelcollection_tostring.htm language=enus -->
## TOPIC 00270: DOChannelCollectionToString Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_dochannelcollection_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_dochannelcollection_tostring.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DOChannelCollection.ToString Method

### DOChannelCollectionToString Method

Returns a string representation of the object.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

##### See Also

###### Reference

DOChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust4225.htm language=enus -->
## TOPIC 00271: ExternalCalibrationSessionAdjust4225 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust4225.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust4225.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust4225 Method

### ExternalCalibrationSessionAdjust4225 Method

**Note: This API is now obsolete.**

Adjust4225(String, Double, Double)

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("The Adjust4225 method is deprecated.")]
public void Adjust4225(
	string physicalChannels,
	double gain,
	double referenceVoltage
)
```

```text
<ObsoleteAttribute("The Adjust4225 method is deprecated.")>
Public Sub Adjust4225 ( 
	physicalChannels As String,
	gain As Double,
	referenceVoltage As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringThe physical channel(s) to calibrate.
- **gain**
  - Type: SystemDoubleThe gain setting to calibrate.
- **referenceVoltage**
  - Type: SystemDoubleThe known voltage, in volts, to use as a reference for calibration.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

referenceVoltage

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust4300.htm language=enus -->
## TOPIC 00272: ExternalCalibrationSessionAdjust4300 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust4300.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust4300.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust4300 Method

### ExternalCalibrationSessionAdjust4300 Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust4300(
	double referenceVoltage
)
```

```text
Public Sub Adjust4300 ( 
	referenceVoltage As Double
)
```

###### Parameters

- **referenceVoltage**
  - Type: SystemDoubleThe known voltage, in volts, to use as a reference for calibration.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

connect a known voltage to the device

referenceVoltage

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust4302.htm language=enus -->
## TOPIC 00273: ExternalCalibrationSessionAdjust4302 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust4302.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust4302.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust4302 Method

### ExternalCalibrationSessionAdjust4302 Method

external calibration

referenceVoltage

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust4302(
	double referenceVoltage
)
```

```text
Public Sub Adjust4302 ( 
	referenceVoltage As Double
)
```

###### Parameters

- **referenceVoltage**
  - Type: SystemDouble Specifies, in volts, the known voltage to use as a reference for calibration.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust4303.htm language=enus -->
## TOPIC 00274: ExternalCalibrationSessionAdjust4303 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust4303.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust4303.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust4303 Method

### ExternalCalibrationSessionAdjust4303 Method

external calibration

referenceVoltage

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust4303(
	double referenceVoltage
)
```

```text
Public Sub Adjust4303 ( 
	referenceVoltage As Double
)
```

###### Parameters

- **referenceVoltage**
  - Type: SystemDouble Specifies, in volts, the known voltage to use as a reference for calibration.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust4357.htm language=enus -->
## TOPIC 00275: ExternalCalibrationSessionAdjust4357 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust4357.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust4357.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust4357 Method

### ExternalCalibrationSessionAdjust4357 Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust4357(
	string physicalChannels,
	double[] referenceValues
)
```

```text
Public Sub Adjust4357 ( 
	physicalChannels As String,
	referenceValues As Double()
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemString Specifies the physical channel(s) to calibrate.
- **referenceValues**
  - Type: SystemDouble Specifies in volts the known voltages to use as the references for calibration.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9207gain.htm language=enus -->
## TOPIC 00276: ExternalCalibrationSessionAdjust9207Gain Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9207gain.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9207gain.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust9207Gain Method

### ExternalCalibrationSessionAdjust9207Gain Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust9207Gain(
	string physicalChannels,
	double value
)
```

```text
Public Sub Adjust9207Gain ( 
	physicalChannels As String,
	value As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringSpecifies the physical channel(s) to calibrate.
- **value**
  - Type: SystemDoubleSpecifies the reference value measured using a calibrator.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9207offset.htm language=enus -->
## TOPIC 00277: ExternalCalibrationSessionAdjust9207Offset Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9207offset.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9207offset.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust9207Offset Method

### ExternalCalibrationSessionAdjust9207Offset Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust9207Offset(
	string physicalChannels
)
```

```text
Public Sub Adjust9207Offset ( 
	physicalChannels As String
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringSpecifies the physical channel(s) to calibrate.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9209offset.htm language=enus -->
## TOPIC 00278: ExternalCalibrationSessionAdjust9209Offset Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9209offset.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9209offset.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust9209Offset Method

### ExternalCalibrationSessionAdjust9209Offset Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust9209Offset(
	string physicalChannels
)
```

```text
Public Sub Adjust9209Offset ( 
	physicalChannels As String
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemString Specifies the physical channel(s) to calibrate.

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9211.htm language=enus -->
## TOPIC 00279: ExternalCalibrationSessionAdjust9211 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9211.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9211.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust9211 Method

### ExternalCalibrationSessionAdjust9211 Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust9211(
	string physicalChannels,
	double value
)
```

```text
Public Sub Adjust9211 ( 
	physicalChannels As String,
	value As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringSpecifies the physical channel(s) to calibrate.
- **value**
  - Type: SystemDoubleSpecifies the reference value measured using a calibrator.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9212.htm language=enus -->
## TOPIC 00280: ExternalCalibrationSessionAdjust9212 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9212.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9212.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust9212 Method

### ExternalCalibrationSessionAdjust9212 Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust9212(
	string physicalChannels,
	double value
)
```

```text
Public Sub Adjust9212 ( 
	physicalChannels As String,
	value As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringSpecifies the physical channel(s) to calibrate.
- **value**
  - Type: SystemDoubleSpecifies the reference value measured using a calibrator.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9213.htm language=enus -->
## TOPIC 00281: ExternalCalibrationSessionAdjust9213 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9213.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9213.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust9213 Method

### ExternalCalibrationSessionAdjust9213 Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust9213(
	string physicalChannels,
	double rangeMinimum,
	double rangeMaximum,
	double value
)
```

```text
Public Sub Adjust9213 ( 
	physicalChannels As String,
	rangeMinimum As Double,
	rangeMaximum As Double,
	value As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringSpecifies the physical channel(s) to calibrate.
- **rangeMinimum**
  - Type: SystemDoubleSpecifies the minimum value for the range, in volts.
- **rangeMaximum**
  - Type: SystemDoubleSpecifies the maximum value for the range, in volts.
- **value**
  - Type: SystemDoubleSpecifies the reference value measured using a calibrator.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9215.htm language=enus -->
## TOPIC 00282: ExternalCalibrationSessionAdjust9215 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9215.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9215.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust9215 Method

### ExternalCalibrationSessionAdjust9215 Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust9215(
	string physicalChannels,
	double value
)
```

```text
Public Sub Adjust9215 ( 
	physicalChannels As String,
	value As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringSpecifies the physical channel(s) to calibrate.
- **value**
  - Type: SystemDoubleSpecifies the reference value measured using a calibrator.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9217.htm language=enus -->
## TOPIC 00283: ExternalCalibrationSessionAdjust9217 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9217.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9217.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust9217 Method

### ExternalCalibrationSessionAdjust9217 Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust9217(
	string physicalChannels,
	double value
)
```

```text
Public Sub Adjust9217 ( 
	physicalChannels As String,
	value As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringSpecifies the physical channel(s) to calibrate.
- **value**
  - Type: SystemDoubleSpecifies the reference value measured using a calibrator.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9218.htm language=enus -->
## TOPIC 00284: ExternalCalibrationSessionAdjust9218 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9218.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9218.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust9218 Method

### ExternalCalibrationSessionAdjust9218 Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust9218(
	string physicalChannels,
	double value
)
```

```text
Public Sub Adjust9218 ( 
	physicalChannels As String,
	value As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringSpecifies the physical channel(s) to calibrate.
- **value**
  - Type: SystemDoubleSpecifies the reference value measured using a calibrator.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9219.htm language=enus -->
## TOPIC 00285: ExternalCalibrationSessionAdjust9219 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9219.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9219.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust9219 Method

### ExternalCalibrationSessionAdjust9219 Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust9219(
	string physicalChannels,
	double value
)
```

```text
Public Sub Adjust9219 ( 
	physicalChannels As String,
	value As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringSpecifies the physical channel(s) to calibrate.
- **value**
  - Type: SystemDoubleSpecifies the reference value measured using a calibrator.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9220.htm language=enus -->
## TOPIC 00286: ExternalCalibrationSessionAdjust9220 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9220.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9220.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust9220 Method

### ExternalCalibrationSessionAdjust9220 Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust9220(
	string physicalChannels,
	double value
)
```

```text
Public Sub Adjust9220 ( 
	physicalChannels As String,
	value As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringSpecifies the physical channel(s) to calibrate.
- **value**
  - Type: SystemDoubleSpecifies the reference value measured using a calibrator.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9222.htm language=enus -->
## TOPIC 00287: ExternalCalibrationSessionAdjust9222 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9222.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9222.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust9222 Method

### ExternalCalibrationSessionAdjust9222 Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust9222(
	string physicalChannels,
	double value
)
```

```text
Public Sub Adjust9222 ( 
	physicalChannels As String,
	value As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringSpecifies the physical channel(s) to calibrate.
- **value**
  - Type: SystemDoubleSpecifies the reference value measured using a calibrator.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9231.htm language=enus -->
## TOPIC 00288: ExternalCalibrationSessionAdjust9231 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9231.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9231.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust9231 Method

### ExternalCalibrationSessionAdjust9231 Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust9231(
	string physicalChannels,
	double value
)
```

```text
Public Sub Adjust9231 ( 
	physicalChannels As String,
	value As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringSpecifies the physical channel(s) to calibrate.
- **value**
  - Type: SystemDoubleSpecifies the reference value measured using a calibrator.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9234gain.htm language=enus -->
## TOPIC 00289: ExternalCalibrationSessionAdjust9234Gain Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9234gain.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9234gain.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust9234Gain Method

### ExternalCalibrationSessionAdjust9234Gain Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust9234Gain(
	string physicalChannels,
	double value
)
```

```text
Public Sub Adjust9234Gain ( 
	physicalChannels As String,
	value As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringSpecifies the physical channel(s) to calibrate.
- **value**
  - Type: SystemDoubleSpecifies the reference value measured using a calibrator.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9234offset.htm language=enus -->
## TOPIC 00290: ExternalCalibrationSessionAdjust9234Offset Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9234offset.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9234offset.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust9234Offset Method

### ExternalCalibrationSessionAdjust9234Offset Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust9234Offset(
	string physicalChannels
)
```

```text
Public Sub Adjust9234Offset ( 
	physicalChannels As String
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringSpecifies the physical channel(s) to calibrate.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9238.htm language=enus -->
## TOPIC 00291: ExternalCalibrationSessionAdjust9238 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9238.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9238.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust9238 Method

### ExternalCalibrationSessionAdjust9238 Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust9238(
	string physicalChannels,
	double value
)
```

```text
Public Sub Adjust9238 ( 
	physicalChannels As String,
	value As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringSpecifies the physical channel(s) to calibrate.
- **value**
  - Type: SystemDoubleSpecifies the reference value measured using a calibrator.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9239.htm language=enus -->
## TOPIC 00292: ExternalCalibrationSessionAdjust9239 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9239.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9239.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust9239 Method

### ExternalCalibrationSessionAdjust9239 Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust9239(
	string physicalChannels,
	double value
)
```

```text
Public Sub Adjust9239 ( 
	physicalChannels As String,
	value As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringSpecifies the physical channel(s) to calibrate.
- **value**
  - Type: SystemDoubleSpecifies the reference value measured using a calibrator.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9242.htm language=enus -->
## TOPIC 00293: ExternalCalibrationSessionAdjust9242 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9242.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9242.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust9242 Method

### ExternalCalibrationSessionAdjust9242 Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust9242(
	string physicalChannels,
	double value
)
```

```text
Public Sub Adjust9242 ( 
	physicalChannels As String,
	value As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringSpecifies the physical channel(s) to calibrate.
- **value**
  - Type: SystemDoubleSpecifies the reference value measured using a calibrator.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9244.htm language=enus -->
## TOPIC 00294: ExternalCalibrationSessionAdjust9244 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9244.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9244.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust9244 Method

### ExternalCalibrationSessionAdjust9244 Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust9244(
	string physicalChannels,
	double value
)
```

```text
Public Sub Adjust9244 ( 
	physicalChannels As String,
	value As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringSpecifies the physical channel(s) to calibrate.
- **value**
  - Type: SystemDoubleSpecifies the reference value measured using a calibrator.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9246.htm language=enus -->
## TOPIC 00295: ExternalCalibrationSessionAdjust9246 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9246.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9246.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust9246 Method

### ExternalCalibrationSessionAdjust9246 Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust9246(
	string physicalChannels,
	double value
)
```

```text
Public Sub Adjust9246 ( 
	physicalChannels As String,
	value As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemString The physical channel(s) to calibrate.
- **value**
  - Type: SystemDouble The reference value measured using a calibrator.

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9247.htm language=enus -->
## TOPIC 00296: ExternalCalibrationSessionAdjust9247 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9247.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9247.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust9247 Method

### ExternalCalibrationSessionAdjust9247 Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust9247(
	string physicalChannels,
	double value
)
```

```text
Public Sub Adjust9247 ( 
	physicalChannels As String,
	value As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemString The physical channel(s) to calibrate.
- **value**
  - Type: SystemDouble The reference value measured using a calibrator.

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjusteseries.htm language=enus -->
## TOPIC 00297: ExternalCalibrationSessionAdjustESeries Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjusteseries.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjusteseries.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.AdjustESeries Method

### ExternalCalibrationSessionAdjustESeries Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void AdjustESeries(
	double referenceVoltage
)
```

```text
Public Sub AdjustESeries ( 
	referenceVoltage As Double
)
```

###### Parameters

- **referenceVoltage**
  - Type: SystemDoubleThe known voltage to use as a reference for calibration. This voltage must be between +6.000 V and +9.999 V.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

connect a known voltage to the device

referenceVoltage

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjustscbaseboard.htm language=enus -->
## TOPIC 00298: ExternalCalibrationSessionAdjustSCBaseboard Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjustscbaseboard.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjustscbaseboard.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.AdjustSCBaseboard Method

### ExternalCalibrationSessionAdjustSCBaseboard Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void AdjustSCBaseboard(
	double referenceVoltage
)
```

```text
Public Sub AdjustSCBaseboard ( 
	referenceVoltage As Double
)
```

###### Parameters

- **referenceVoltage**
  - Type: SystemDoubleThe known voltage to use as a reference for calibration. This voltage must be between +6.000 V and +9.999 V.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

referenceVoltage

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjusttiotimebase.htm language=enus -->
## TOPIC 00299: ExternalCalibrationSessionAdjustTioTimebase Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjusttiotimebase.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjusttiotimebase.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.AdjustTioTimebase Method

### ExternalCalibrationSessionAdjustTioTimebase Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void AdjustTioTimebase(
	double referenceFrequency
)
```

```text
Public Sub AdjustTioTimebase ( 
	referenceFrequency As Double
)
```

###### Parameters

- **referenceFrequency**
  - Type: SystemDoubleThe frequency, in hertz, of the signal to use as a reference for calibration.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

You must connect a sinusoidal signal with a known frequency to the device. You cannot calibrate PXI-6608 devices with this function. Refer to KnowledgeBase 40KGCD2F for more information.

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_connectscexpresscalibrationaccessorychannels.htm language=enus -->
## TOPIC 00300: ExternalCalibrationSessionConnectSCExpressCalibrationAccessoryChannels Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_connectscexpresscalibrationaccessorychannels.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_connectscexpresscalibrationaccessorychannels.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.ConnectSCExpressCalibrationAccessoryChannels Method

### ExternalCalibrationSessionConnectSCExpressCalibrationAccessoryChannels Method

Configures a connection on the SC Express accessory for the specified physical channel(s).

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConnectSCExpressCalibrationAccessoryChannels(
	string physicalChannels,
	string connection
)
```

```text
Public Sub ConnectSCExpressCalibrationAccessoryChannels ( 
	physicalChannels As String,
	connection As String
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemString The physical channel(s) to calibrate.
- **connection**
  - Type: SystemString Specifies how channels on the SC Express accessory should be configured. The resulting configuration connects channels to a particular external signal or to an onboard terminal. The supported connections depend on the accessory.

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_dsasetcalibrationtemperature.htm language=enus -->
## TOPIC 00301: ExternalCalibrationSessionDsaSetCalibrationTemperature Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_dsasetcalibrationtemperature.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_dsasetcalibrationtemperature.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.DsaSetCalibrationTemperature Method

### ExternalCalibrationSessionDsaSetCalibrationTemperature Method

Specifies the temperature of a DSA device for the current external calibration session.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void DsaSetCalibrationTemperature(
	double temperature
)
```

```text
Public Sub DsaSetCalibrationTemperature ( 
	temperature As Double
)
```

###### Parameters

- **temperature**
  - Type: SystemDoubleThe temperature of the device, in degrees Celsius.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_fielddaqsetcalibrationtemperature.htm language=enus -->
## TOPIC 00302: ExternalCalibrationSessionFieldDAQSetCalibrationTemperature Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_fielddaqsetcalibrationtemperature.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_fielddaqsetcalibrationtemperature.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.FieldDAQSetCalibrationTemperature Method

### ExternalCalibrationSessionFieldDAQSetCalibrationTemperature Method

Specifies the temperature of a FieldDAQ device for the current external calibration session.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void FieldDAQSetCalibrationTemperature(
	double temperature
)
```

```text
Public Sub FieldDAQSetCalibrationTemperature ( 
	temperature As Double
)
```

###### Parameters

- **temperature**
  - Type: SystemDoubleSpecifies the temperature of the device, in degrees Celsius.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get11601adjustmentpoints.htm language=enus -->
## TOPIC 00303: ExternalCalibrationSessionGet11601AdjustmentPoints Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get11601adjustmentpoints.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get11601adjustmentpoints.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Get11601AdjustmentPoints Method

### ExternalCalibrationSessionGet11601AdjustmentPoints Method

Returns the reference voltage values to be used by a reference device to create a reference signal.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] Get11601AdjustmentPoints()
```

```text
Public Function Get11601AdjustmentPoints As Double()
```

###### Return Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get11603adjustmentpoints.htm language=enus -->
## TOPIC 00304: ExternalCalibrationSessionGet11603AdjustmentPoints Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get11603adjustmentpoints.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get11603adjustmentpoints.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Get11603AdjustmentPoints Method

### ExternalCalibrationSessionGet11603AdjustmentPoints Method

Returns the reference voltage values to be used by a reference device to create a reference signal.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] Get11603AdjustmentPoints()
```

```text
Public Function Get11603AdjustmentPoints As Double()
```

###### Return Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get11605adjustmentpoints.htm language=enus -->
## TOPIC 00305: ExternalCalibrationSessionGet11605AdjustmentPoints Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get11605adjustmentpoints.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get11605adjustmentpoints.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Get11605AdjustmentPoints Method

### ExternalCalibrationSessionGet11605AdjustmentPoints Method

Returns the reference voltage values to be used by a reference device to create a reference signal.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] Get11605AdjustmentPoints()
```

```text
Public Function Get11605AdjustmentPoints As Double()
```

###### Return Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get11613adjustmentpoints.htm language=enus -->
## TOPIC 00306: ExternalCalibrationSessionGet11613AdjustmentPoints Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get11613adjustmentpoints.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get11613adjustmentpoints.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Get11613AdjustmentPoints Method

### ExternalCalibrationSessionGet11613AdjustmentPoints Method

Returns the reference voltage values to be used by a reference device to create a reference signal.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] Get11613AdjustmentPoints()
```

```text
Public Function Get11613AdjustmentPoints As Double()
```

###### Return Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get11634adjustmentpoints.htm language=enus -->
## TOPIC 00307: ExternalCalibrationSessionGet11634AdjustmentPoints Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get11634adjustmentpoints.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get11634adjustmentpoints.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Get11634AdjustmentPoints Method

### ExternalCalibrationSessionGet11634AdjustmentPoints Method

Returns the reference voltage values to be used by a reference device to create a reference signal.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] Get11634AdjustmentPoints()
```

```text
Public Function Get11634AdjustmentPoints As Double()
```

###### Return Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9216adjustmentpoints.htm language=enus -->
## TOPIC 00308: ExternalCalibrationSessionGet9216AdjustmentPoints Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9216adjustmentpoints.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9216adjustmentpoints.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Get9216AdjustmentPoints Method

### ExternalCalibrationSessionGet9216AdjustmentPoints Method

Returns the reference voltage values to be used by a reference device to create a reference signal.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] Get9216AdjustmentPoints()
```

```text
Public Function Get9216AdjustmentPoints As Double()
```

###### Return Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9220adjustmentpoints.htm language=enus -->
## TOPIC 00309: ExternalCalibrationSessionGet9220AdjustmentPoints Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9220adjustmentpoints.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9220adjustmentpoints.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Get9220AdjustmentPoints Method

### ExternalCalibrationSessionGet9220AdjustmentPoints Method

Returns the reference voltage values to be used by a reference device to create a reference signal.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] Get9220AdjustmentPoints()
```

```text
Public Function Get9220AdjustmentPoints As Double()
```

###### Return Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9225adjustmentpoints.htm language=enus -->
## TOPIC 00310: ExternalCalibrationSessionGet9225AdjustmentPoints Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9225adjustmentpoints.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9225adjustmentpoints.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Get9225AdjustmentPoints Method

### ExternalCalibrationSessionGet9225AdjustmentPoints Method

Returns the reference voltage values to be used by a reference device to create a reference signal.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] Get9225AdjustmentPoints()
```

```text
Public Function Get9225AdjustmentPoints As Double()
```

###### Return Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9227adjustmentpoints.htm language=enus -->
## TOPIC 00311: ExternalCalibrationSessionGet9227AdjustmentPoints Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9227adjustmentpoints.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9227adjustmentpoints.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Get9227AdjustmentPoints Method

### ExternalCalibrationSessionGet9227AdjustmentPoints Method

Returns the reference current values to be used by a reference device to create a reference signal.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] Get9227AdjustmentPoints()
```

```text
Public Function Get9227AdjustmentPoints As Double()
```

###### Return Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9234adjustmentpoints.htm language=enus -->
## TOPIC 00312: ExternalCalibrationSessionGet9234AdjustmentPoints Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9234adjustmentpoints.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9234adjustmentpoints.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Get9234AdjustmentPoints Method

### ExternalCalibrationSessionGet9234AdjustmentPoints Method

Returns the reference voltage values to be used by a reference device to create a reference signal.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] Get9234AdjustmentPoints()
```

```text
Public Function Get9234AdjustmentPoints As Double()
```

###### Return Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9239adjustmentpoints.htm language=enus -->
## TOPIC 00313: ExternalCalibrationSessionGet9239AdjustmentPoints Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9239adjustmentpoints.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9239adjustmentpoints.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Get9239AdjustmentPoints Method

### ExternalCalibrationSessionGet9239AdjustmentPoints Method

Returns the reference voltage values to be used by a reference device to create a reference signal.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] Get9239AdjustmentPoints()
```

```text
Public Function Get9239AdjustmentPoints As Double()
```

###### Return Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9242adjustmentpoints.htm language=enus -->
## TOPIC 00314: ExternalCalibrationSessionGet9242AdjustmentPoints Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9242adjustmentpoints.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9242adjustmentpoints.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Get9242AdjustmentPoints Method

### ExternalCalibrationSessionGet9242AdjustmentPoints Method

Returns the reference voltage values to be used by a reference device to create a reference signal.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] Get9242AdjustmentPoints()
```

```text
Public Function Get9242AdjustmentPoints As Double()
```

###### Return Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9244adjustmentpoints.htm language=enus -->
## TOPIC 00315: ExternalCalibrationSessionGet9244AdjustmentPoints Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9244adjustmentpoints.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9244adjustmentpoints.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Get9244AdjustmentPoints Method

### ExternalCalibrationSessionGet9244AdjustmentPoints Method

Returns the reference voltage values to be used by a reference device to create a reference signal.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] Get9244AdjustmentPoints()
```

```text
Public Function Get9244AdjustmentPoints As Double()
```

###### Return Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9246adjustmentpoints.htm language=enus -->
## TOPIC 00316: ExternalCalibrationSessionGet9246AdjustmentPoints Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9246adjustmentpoints.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9246adjustmentpoints.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Get9246AdjustmentPoints Method

### ExternalCalibrationSessionGet9246AdjustmentPoints Method

Returns the reference values to be used by a reference device to create a reference signal.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] Get9246AdjustmentPoints()
```

```text
Public Function Get9246AdjustmentPoints As Double()
```

###### Return Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9247adjustmentpoints.htm language=enus -->
## TOPIC 00317: ExternalCalibrationSessionGet9247AdjustmentPoints Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9247adjustmentpoints.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9247adjustmentpoints.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Get9247AdjustmentPoints Method

### ExternalCalibrationSessionGet9247AdjustmentPoints Method

Returns the reference values to be used by a reference device to create a reference signal.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] Get9247AdjustmentPoints()
```

```text
Public Function Get9247AdjustmentPoints As Double()
```

###### Return Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9250adjustmentpoints.htm language=enus -->
## TOPIC 00318: ExternalCalibrationSessionGet9250AdjustmentPoints Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9250adjustmentpoints.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9250adjustmentpoints.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Get9250AdjustmentPoints Method

### ExternalCalibrationSessionGet9250AdjustmentPoints Method

Returns the reference voltage values to be used by a reference device to create a reference signal.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] Get9250AdjustmentPoints()
```

```text
Public Function Get9250AdjustmentPoints As Double()
```

###### Return Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9251adjustmentpoints.htm language=enus -->
## TOPIC 00319: ExternalCalibrationSessionGet9251AdjustmentPoints Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9251adjustmentpoints.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9251adjustmentpoints.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Get9251AdjustmentPoints Method

### ExternalCalibrationSessionGet9251AdjustmentPoints Method

Returns the reference voltage values to be used by a reference device to create a reference signal.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] Get9251AdjustmentPoints()
```

```text
Public Function Get9251AdjustmentPoints As Double()
```

###### Return Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9252adjustmentpoints.htm language=enus -->
## TOPIC 00320: ExternalCalibrationSessionGet9252AdjustmentPoints Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9252adjustmentpoints.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9252adjustmentpoints.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Get9252AdjustmentPoints Method

### ExternalCalibrationSessionGet9252AdjustmentPoints Method

Returns the reference voltage values to be used by a reference device to create a reference signal.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] Get9252AdjustmentPoints()
```

```text
Public Function Get9252AdjustmentPoints As Double()
```

###### Return Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9253adjustmentpoints.htm language=enus -->
## TOPIC 00321: ExternalCalibrationSessionGet9253AdjustmentPoints Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9253adjustmentpoints.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9253adjustmentpoints.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Get9253AdjustmentPoints Method

### ExternalCalibrationSessionGet9253AdjustmentPoints Method

Returns the reference values to be used by a reference device to create a reference signal.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] Get9253AdjustmentPoints()
```

```text
Public Function Get9253AdjustmentPoints As Double()
```

###### Return Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9262adjustmentpoints.htm language=enus -->
## TOPIC 00322: ExternalCalibrationSessionGet9262AdjustmentPoints Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9262adjustmentpoints.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_get9262adjustmentpoints.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Get9262AdjustmentPoints Method

### ExternalCalibrationSessionGet9262AdjustmentPoints Method

Returns the reference voltage values to be measured by a reference device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public int[] Get9262AdjustmentPoints()
```

```text
Public Function Get9262AdjustmentPoints As Integer()
```

###### Return Value

Int32

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1102.htm language=enus -->
## TOPIC 00323: ExternalCalibrationSessionSetup1102 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1102.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1102.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Setup1102 Method

### ExternalCalibrationSessionSetup1102 Method

Configures the calibration task for an SCXI-1102 module.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Setup1102(
	string physicalChannels,
	double gain
)
```

```text
Public Sub Setup1102 ( 
	physicalChannels As String,
	gain As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringThe physical channel(s) to calibrate.
- **gain**
  - Type: SystemDoubleThe gain setting to calibrate.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

| Note |
| --- |
| The terminal on which to measure module output depends on the configuration of the module in MAX. National Instruments recommends cabling the module to the digitizer so that the output appears on the MCH0± pins of the rear signal connector. Refer to the SCXI-1102/B/C User Manual for more information on the routing of module output. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1104.htm language=enus -->
## TOPIC 00324: ExternalCalibrationSessionSetup1104 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1104.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1104.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Setup1104 Method

### ExternalCalibrationSessionSetup1104 Method

Configures the calibration task for an SCXI-1104 module.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Setup1104(
	string physicalChannels
)
```

```text
Public Sub Setup1104 ( 
	physicalChannels As String
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringThe physical channel(s) to calibrate.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

| Note |
| --- |
| The terminal on which to measure module output depends on the configuration of the module in MAX. National Instruments recommends cabling the module to the digitizer so that the output appears on the MCH0± pins of the rear signal connector. Refer to the SCXI-1104 User Manual for more information on the routing of module output. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1112.htm language=enus -->
## TOPIC 00325: ExternalCalibrationSessionSetup1112 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1112.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1112.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Setup1112 Method

### ExternalCalibrationSessionSetup1112 Method

Configures the calibration task for an SCXI-1112 module.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Setup1112(
	string physicalChannels
)
```

```text
Public Sub Setup1112 ( 
	physicalChannels As String
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringThe physical channel(s) to calibrate.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

| Note |
| --- |
| The terminal on which to measure module output depends on the configuration of the module in MAX. National Instruments recommends cabling the module to the digitizer so that the output appears on the MCH0± pins of the rear signal connector. Refer to the SCXI-1112 User Manual for more information on the routing of module output. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1122.htm language=enus -->
## TOPIC 00326: ExternalCalibrationSessionSetup1122 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1122.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1122.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Setup1122 Method

### ExternalCalibrationSessionSetup1122 Method

Configures the calibration task for an SCXI-1122 module.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Setup1122(
	string physicalChannels,
	double gain
)
```

```text
Public Sub Setup1122 ( 
	physicalChannels As String,
	gain As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringThe physical channel(s) to calibrate.
- **gain**
  - Type: SystemDoubleThe gain setting to calibrate.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

| Note |
| --- |
| The terminal on which to measure module output depends on the configuration of the module in MAX. National Instruments recommends cabling the module to the digitizer so that the output appears on the MCH0± pins of the rear signal connector. Refer to the SCXI-1122 User Manual for more information on the routing of module output. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1124.htm language=enus -->
## TOPIC 00327: ExternalCalibrationSessionSetup1124 Method (String, Scxi1124Range, Int64)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1124.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1124.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Setup1124 Method (String, Scxi1124Range, Int64)

### ExternalCalibrationSessionSetup1124 Method (String, Scxi1124Range, Int64)

Configures the calibration task for an SCXI-1124 module.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Setup1124(
	string physicalChannels,
	Scxi1124Range range,
	long dacValue
)
```

```text
Public Sub Setup1124 ( 
	physicalChannels As String,
	range As Scxi1124Range,
	dacValue As Long
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringThe physical channel(s) to calibrate.
- **range**
  - Type: NationalInstruments.DAQmxScxi1124RangeThe range of the calibration.
- **dacValue**
  - Type: SystemInt64The binary value to be written out to the specified channels DAC at the specified range.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

ExternalCalibrationSession Class

Setup1124 Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1124_1.htm language=enus -->
## TOPIC 00328: ExternalCalibrationSessionSetup1124 Method (String, Scxi1124Range, UInt32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1124_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1124_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Setup1124 Method (String, Scxi1124Range, UInt32)

### ExternalCalibrationSessionSetup1124 Method (String, Scxi1124Range, UInt32)

Configures the calibration task for an SCXI-1124 module.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Setup1124(
	string physicalChannels,
	Scxi1124Range range,
	uint dacValue
)
```

```text
Public Sub Setup1124 ( 
	physicalChannels As String,
	range As Scxi1124Range,
	dacValue As UInteger
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringThe physical channel(s) to calibrate.
- **range**
  - Type: NationalInstruments.DAQmxScxi1124RangeThe range of the calibration.
- **dacValue**
  - Type: SystemUInt32The binary value to be written out to the specified channels DAC at the specified range.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

ExternalCalibrationSession Class

Setup1124 Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1125.htm language=enus -->
## TOPIC 00329: ExternalCalibrationSessionSetup1125 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1125.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1125.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Setup1125 Method

### ExternalCalibrationSessionSetup1125 Method

Configures the calibration task for an SCXI-1125 module.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Setup1125(
	string physicalChannels,
	double gain
)
```

```text
Public Sub Setup1125 ( 
	physicalChannels As String,
	gain As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringThe physical channel(s) to calibrate.
- **gain**
  - Type: SystemDoubleThe gain setting to calibrate.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

| Note |
| --- |
| The terminal on which to measure module output depends on the configuration of the module in MAX. National Instruments recommends cabling the module to the digitizer so that the output appears on the MCH0± pins of the rear signal connector. Refer to the SCXI-1125 User Manual for more information on the routing of module output. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1126.htm language=enus -->
## TOPIC 00330: ExternalCalibrationSessionSetup1126 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1126.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1126.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Setup1126 Method

### ExternalCalibrationSessionSetup1126 Method

Configures the channel and range for an SCXI-1126 module calibration task.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Setup1126(
	string physicalChannels,
	double upperFrequencyLimit
)
```

```text
Public Sub Setup1126 ( 
	physicalChannels As String,
	upperFrequencyLimit As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringThe physical channel(s) to calibrate.
- **upperFrequencyLimit**
  - Type: SystemDoubleThe upper frequency limit.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

| Note |
| --- |
| The terminal where you can measure module output depends on the configuration of the module in MAX. National Instruments recommends cabling the module to the digitizer so that the output appears on the MCH0± pins of the rear signal connector. Refer to the SCXI-1126 User Manual for more information on the routing of module output. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1141.htm language=enus -->
## TOPIC 00331: ExternalCalibrationSessionSetup1141 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1141.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1141.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Setup1141 Method

### ExternalCalibrationSessionSetup1141 Method

Configures the gain value for an SCXI-1141 module calibration task.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Setup1141(
	string physicalChannels,
	double gain
)
```

```text
Public Sub Setup1141 ( 
	physicalChannels As String,
	gain As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringThe physical channel(s) to calibrate.
- **gain**
  - Type: SystemDoubleThe gain setting to calibrate.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

| Note |
| --- |
| The terminal on which to measure module output depends on the configuration of the module in MAX. National Instruments recommends cabling the module to the digitizer so that the output appears on the MCH0± pins of the rear signal connector. Refer to the SCXI-1141/1142/1143 User Manual for more information on the routing of module output. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1142.htm language=enus -->
## TOPIC 00332: ExternalCalibrationSessionSetup1142 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1142.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1142.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Setup1142 Method

### ExternalCalibrationSessionSetup1142 Method

Configures the gain value for an SCXI-1142 module calibration task.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Setup1142(
	string physicalChannels,
	double gain
)
```

```text
Public Sub Setup1142 ( 
	physicalChannels As String,
	gain As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringThe physical channel(s) to calibrate.
- **gain**
  - Type: SystemDoubleThe gain setting to calibrate.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

| Note |
| --- |
| The terminal on which to measure module output depends on the configuration of the module in MAX. National Instruments recommends cabling the module to the digitizer so that the output appears on the MCH0± pins of the rear signal connector. Refer to the SCXI-1141/1142/1143 User Manual for more information on the routing of module output. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1143.htm language=enus -->
## TOPIC 00333: ExternalCalibrationSessionSetup1143 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1143.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1143.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Setup1143 Method

### ExternalCalibrationSessionSetup1143 Method

Configures the gain value for an SCXI-1143 module calibration task.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Setup1143(
	string physicalChannels,
	double gain
)
```

```text
Public Sub Setup1143 ( 
	physicalChannels As String,
	gain As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringThe physical channel(s) to calibrate.
- **gain**
  - Type: SystemDoubleThe gain setting to calibrate.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

| Note |
| --- |
| The terminal on which to measure module output depends on the configuration of the module in MAX. National Instruments recommends cabling the module to the digitizer so that the output appears on the MCH0± pins of the rear signal connector. Refer to the SCXI-1141/1142/1143 User Manual for more information on the routing of module output. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup11605.htm language=enus -->
## TOPIC 00334: ExternalCalibrationSessionSetup11605 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup11605.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup11605.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Setup11605 Method

### ExternalCalibrationSessionSetup11605 Method

Sets up external calibration for an FD 11605 device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Setup11605(
	double rangeMinimum,
	double rangeMaximum
)
```

```text
Public Sub Setup11605 ( 
	rangeMinimum As Double,
	rangeMaximum As Double
)
```

###### Parameters

- **rangeMinimum**
  - Type: SystemDoubleThe minimum value in the range.
- **rangeMaximum**
  - Type: SystemDoubleThe maximum value in the range.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup11634.htm language=enus -->
## TOPIC 00335: ExternalCalibrationSessionSetup11634 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup11634.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup11634.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Setup11634 Method

### ExternalCalibrationSessionSetup11634 Method

Sets up external calibration for an FD 11634 device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Setup11634(
	double rangeMinimum,
	double rangeMaximum
)
```

```text
Public Sub Setup11634 ( 
	rangeMinimum As Double,
	rangeMaximum As Double
)
```

###### Parameters

- **rangeMinimum**
  - Type: SystemDoubleThe minimum value in the range.
- **rangeMaximum**
  - Type: SystemDoubleThe maximum value in the range.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup11637.htm language=enus -->
## TOPIC 00336: ExternalCalibrationSessionSetup11637 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup11637.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup11637.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Setup11637 Method

### ExternalCalibrationSessionSetup11637 Method

Sets up external calibration for an FD 11637 device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Setup11637(
	string physicalChannels,
	AIBridgeConfiguration11637 bridgeConfiguration,
	double excitationValue
)
```

```text
Public Sub Setup11637 ( 
	physicalChannels As String,
	bridgeConfiguration As AIBridgeConfiguration11637,
	excitationValue As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringSpecifies the name of the physical channel to use to create the virtual channel. The DAQmx physical channel constant lists all physical channels for devices installed in the system. You cannot specify more than one physical channel.
- **bridgeConfiguration**
  - Type: NationalInstruments.DAQmxAIBridgeConfiguration11637The type of Wheatstone bridge the sensor is.
- **excitationValue**
  - Type: SystemDoubleSpecifies the excitation value for the current channel and bridge configuration.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1502.htm language=enus -->
## TOPIC 00337: ExternalCalibrationSessionSetup1502 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1502.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1502.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Setup1502 Method

### ExternalCalibrationSessionSetup1502 Method

Configures the calibration task for an SCXI-1502 module.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Setup1502(
	string physicalChannels,
	double gain
)
```

```text
Public Sub Setup1502 ( 
	physicalChannels As String,
	gain As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringThe physical channel(s) to calibrate.
- **gain**
  - Type: SystemDoubleThe gain setting to calibrate.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

| Note |
| --- |
| The terminal on which to measure module output depends on the configuration of the module in MAX. National Instruments recommends cabling the module to the digitizer so that the output appears on the MCH0± pins of the rear signal connector. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1503.htm language=enus -->
## TOPIC 00338: ExternalCalibrationSessionSetup1503 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1503.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1503.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Setup1503 Method

### ExternalCalibrationSessionSetup1503 Method

Configures the calibration task for an SCXI-1503 module.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Setup1503(
	string physicalChannels,
	double gain
)
```

```text
Public Sub Setup1503 ( 
	physicalChannels As String,
	gain As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringThe physical channel(s) to calibrate.
- **gain**
  - Type: SystemDoubleThe gain setting to calibrate.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

| Note |
| --- |
| The terminal on which to measure module output depends on the configuration of the module in MAX. National Instruments recommends cabling the module to the digitizer so that the output appears on the MCH0± pins of the rear signal connector. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1520.htm language=enus -->
## TOPIC 00339: ExternalCalibrationSessionSetup1520 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1520.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1520.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Setup1520 Method

### ExternalCalibrationSessionSetup1520 Method

Configures the calibration task for an SCXI-1520 module.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Setup1520(
	string physicalChannels,
	double gain
)
```

```text
Public Sub Setup1520 ( 
	physicalChannels As String,
	gain As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringThe physical channel(s) to calibrate.
- **gain**
  - Type: SystemDoubleThe gain setting to calibrate.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

| Note |
| --- |
| The terminal on which to measure module output depends on the configuration of the module in MAX. National Instruments recommends cabling the module to the digitizer so that the output appears on the MCH0± pins of the rear signal connector. Refer to the SCXI-1520 User Manual for more information on the routing of module output. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1521.htm language=enus -->
## TOPIC 00340: ExternalCalibrationSessionSetup1521 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1521.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1521.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Setup1521 Method

### ExternalCalibrationSessionSetup1521 Method

Configures the calibration task for an SCXI-1521 module.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Setup1521(
	string physicalChannels
)
```

```text
Public Sub Setup1521 ( 
	physicalChannels As String
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringThe physical channel(s) to calibrate.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

| Note |
| --- |
| The terminal on which to measure module output depends on the configuration of the module in MAX. National Instruments recommends cabling the module to the digitizer so that the output appears on the MCH0± pins of the rear signal connector. Refer to the SCXI-1521 User Manual for more information on the routing of module output. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup153x.htm language=enus -->
## TOPIC 00341: ExternalCalibrationSessionSetup153x Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup153x.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup153x.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Setup153x Method

### ExternalCalibrationSessionSetup153x Method

Configures the gain value for an SCXI-1530 or SCXI-1531 module calibration task.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Setup153x(
	string physicalChannels,
	double gain
)
```

```text
Public Sub Setup153x ( 
	physicalChannels As String,
	gain As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringThe physical channel(s) to calibrate.
- **gain**
  - Type: SystemDoubleThe gain setting to calibrate.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

| Note |
| --- |
| The terminal on which to measure module output depends on the configuration of the module in MAX. National Instruments recommends cabling the module to the digitizer so that the output appears on the MCH0± pins of the rear signal connector. Refer to the SCXI-1530/1531 User Manual for more information on the routing of module output. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1540.htm language=enus -->
## TOPIC 00342: ExternalCalibrationSessionSetup1540 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1540.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup1540.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Setup1540 Method

### ExternalCalibrationSessionSetup1540 Method

Configures the gain value for an SCXI-1540 module calibration task.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Setup1540(
	string physicalChannels,
	double excitationRmsValue,
	double excitationFrequency
)
```

```text
Public Sub Setup1540 ( 
	physicalChannels As String,
	excitationRmsValue As Double,
	excitationFrequency As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringThe physical channel(s) to calibrate.
- **excitationRmsValue**
  - Type: SystemDoubleThe excitation root mean square value.
- **excitationFrequency**
  - Type: SystemDoubleThe excitation frequency.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

| Note |
| --- |
| The terminal on which to measure module output depends on the configuration of the module in MAX. National Instruments recommends cabling the module to the digitizer so that the output appears on the MCH0± pins of the rear signal connector. Refer to the SCXI-1540 User Manual for more information on the routing of module output. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup4302.htm language=enus -->
## TOPIC 00343: ExternalCalibrationSessionSetup4302 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup4302.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup4302.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Setup4302 Method

### ExternalCalibrationSessionSetup4302 Method

Initializes an NI PXIe-4302 device with the specified range for calibration.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Setup4302(
	string physicalChannels,
	double rangeMinimum,
	double rangeMaximum
)
```

```text
Public Sub Setup4302 ( 
	physicalChannels As String,
	rangeMinimum As Double,
	rangeMaximum As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemString The physical channel(s) to calibrate.
- **rangeMinimum**
  - Type: SystemDouble The minimum value in the range.
- **rangeMaximum**
  - Type: SystemDouble The maximum value in the range.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup4304.htm language=enus -->
## TOPIC 00344: ExternalCalibrationSessionSetup4304 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup4304.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup4304.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Setup4304 Method

### ExternalCalibrationSessionSetup4304 Method

Initializes an NI PXIe-4304 device with the specified range for calibration.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Setup4304(
	string physicalChannels,
	double rangeMinimum,
	double rangeMaximum
)
```

```text
Public Sub Setup4304 ( 
	physicalChannels As String,
	rangeMinimum As Double,
	rangeMaximum As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemString The physical channel(s) to calibrate.
- **rangeMinimum**
  - Type: SystemDouble The minimum value in the range.
- **rangeMaximum**
  - Type: SystemDouble The maximum value in the range.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup4322.htm language=enus -->
## TOPIC 00345: ExternalCalibrationSessionSetup4322 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup4322.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup4322.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Setup4322 Method

### ExternalCalibrationSessionSetup4322 Method

Configures the calibration task for an NI 4322 device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Setup4322(
	string physicalChannels,
	AOOutputType outputType,
	double outputValue
)
```

```text
Public Sub Setup4322 ( 
	physicalChannels As String,
	outputType As AOOutputType,
	outputValue As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringThe physical channel(s) to calibrate.
- **outputType**
  - Type: NationalInstruments.DAQmxAOOutputTypeThe output type.
- **outputValue**
  - Type: SystemDoubleThe value for calibration.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup433x.htm language=enus -->
## TOPIC 00346: ExternalCalibrationSessionSetup433x Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup433x.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup433x.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Setup433x Method

### ExternalCalibrationSessionSetup433x Method

Configures the calibration task for an NI PXIe-433x device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Setup433x(
	string physicalChannels,
	double excitationVoltage
)
```

```text
Public Sub Setup433x ( 
	physicalChannels As String,
	excitationVoltage As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringThe physical channel(s) to calibrate.
- **excitationVoltage**
  - Type: SystemDoubleThe voltage value for calibration.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup9219.htm language=enus -->
## TOPIC 00347: ExternalCalibrationSessionSetup9219 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup9219.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup9219.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Setup9219 Method

### ExternalCalibrationSessionSetup9219 Method

Sets up external calibration for an NI 9219 device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Setup9219(
	string physicalChannels,
	double rangeMinimum,
	double rangeMaximum,
	AIMeasurementType measurementType,
	AIBridgeConfiguration bridgeConfiguration
)
```

```text
Public Sub Setup9219 ( 
	physicalChannels As String,
	rangeMinimum As Double,
	rangeMaximum As Double,
	measurementType As AIMeasurementType,
	bridgeConfiguration As AIBridgeConfiguration
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringSpecifies the name of the physical channel to use to create the virtual channel. The DAQmx physical channel constant lists all physical channels for devices installed in the system. You cannot specify more than one physical channel.
- **rangeMinimum**
  - Type: SystemDoubleThe minimum value in the range, in the units of the measurement type specified by measurementType. If your measurementType is RTD, you must specify your minimum range in ohms.
- **rangeMaximum**
  - Type: SystemDoubleThe maximum value in the range, in the units of the measurement type specified by measurementType. If your measurementType is RTD, you must specify your maximum range in ohms.
- **measurementType**
  - Type: NationalInstruments.DAQmxAIMeasurementTypeThe type of measurement for the device.
- **bridgeConfiguration**
  - Type: NationalInstruments.DAQmxAIBridgeConfigurationThe type of Wheatstone bridge the sensor is.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup9242.htm language=enus -->
## TOPIC 00348: ExternalCalibrationSessionSetup9242 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup9242.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup9242.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Setup9242 Method

### ExternalCalibrationSessionSetup9242 Method

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Setup9242(
	string physicalChannels,
	double adjustmentPoint
)
```

```text
Public Sub Setup9242 ( 
	physicalChannels As String,
	adjustmentPoint As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringSpecifies the name of the physical channel(s) to calibrate. The DAQmx physical channel constant lists all physical channels for devices installed in the system.
- **adjustmentPoint**
  - Type: SystemDoubleThe binary number to read from the ADC.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup9244.htm language=enus -->
## TOPIC 00349: ExternalCalibrationSessionSetup9244 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup9244.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup9244.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Setup9244 Method

### ExternalCalibrationSessionSetup9244 Method

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Setup9244(
	string physicalChannels,
	double adjustmentPoint
)
```

```text
Public Sub Setup9244 ( 
	physicalChannels As String,
	adjustmentPoint As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringSpecifies the name of the physical channel to use to create the virtual channel. The DAQmx physical channel constant lists all physical channels for devices installed in the system. You cannot specify more than one physical channel.
- **adjustmentPoint**
  - Type: SystemDoubleThe binary number to read from the ADC.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup9266.htm language=enus -->
## TOPIC 00350: ExternalCalibrationSessionSetup9266 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup9266.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup9266.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Setup9266 Method

### ExternalCalibrationSessionSetup9266 Method

Applies the specified DAC value to the AO channels, such that it can then be measured by a DMM

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Setup9266(
	string physicalChannels,
	int value
)
```

```text
Public Sub Setup9266 ( 
	physicalChannels As String,
	value As Integer
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringSpecifies the name of the physical channel to use to create the virtual channel. The DAQmx physical channel constant lists all physical channels for devices installed in the system. You cannot specify more than one physical channel.
- **value**
  - Type: SystemInt32The binary number to write to the DAC.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setupdsa4463.htm language=enus -->
## TOPIC 00351: ExternalCalibrationSessionSetupDsa4463 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setupdsa4463.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setupdsa4463.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.SetupDsa4463 Method

### ExternalCalibrationSessionSetupDsa4463 Method

Generates a specified voltage from the DSA device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void SetupDsa4463(
	string physicalChannels,
	CalibrationInputTerminalConfiguration4463 terminalConfiguration,
	double gain,
	double outputVoltage
)
```

```text
Public Sub SetupDsa4463 ( 
	physicalChannels As String,
	terminalConfiguration As CalibrationInputTerminalConfiguration4463,
	gain As Double,
	outputVoltage As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemString The physical channel(s) to calibrate.
- **terminalConfiguration**
  - Type: NationalInstruments.DAQmxCalibrationInputTerminalConfiguration4463 The input terminal configuration of the device.
- **gain**
  - Type: SystemDouble The gain setting to calibrate.
- **outputVoltage**
  - Type: SystemDouble The output voltage to generate, in Hz.

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setupdsa4480.htm language=enus -->
## TOPIC 00352: ExternalCalibrationSessionSetupDsa4480 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setupdsa4480.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setupdsa4480.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.SetupDsa4480 Method

### ExternalCalibrationSessionSetupDsa4480 Method

Generates a specified voltage from the DSA device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void SetupDsa4480(
	string physicalChannels,
	CalibrationMode4480 calibrationMode
)
```

```text
Public Sub SetupDsa4480 ( 
	physicalChannels As String,
	calibrationMode As CalibrationMode4480
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemString The physical channel(s) to calibrate.
- **calibrationMode**
  - Type: NationalInstruments.DAQmxCalibrationMode4480 The calibration mode for the device.

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setupdsaaotimebase.htm language=enus -->
## TOPIC 00353: ExternalCalibrationSessionSetupDsaAOTimebase Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setupdsaaotimebase.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setupdsaaotimebase.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.SetupDsaAOTimebase Method

### ExternalCalibrationSessionSetupDsaAOTimebase Method

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double SetupDsaAOTimebase()
```

```text
Public Function SetupDsaAOTimebase As Double
```

###### Return Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_tostring.htm language=enus -->
## TOPIC 00354: ExternalCalibrationSessionToString Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_tostring.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.ToString Method

### ExternalCalibrationSessionToString Method

Returns a string representation of the object.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_handshaketrigger_configureinterlockedtrigger.htm language=enus -->
## TOPIC 00355: HandshakeTriggerConfigureInterlockedTrigger Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_handshaketrigger_configureinterlockedtrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_handshaketrigger_configureinterlockedtrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

HandshakeTrigger.ConfigureInterlockedTrigger Method

### HandshakeTriggerConfigureInterlockedTrigger Method

analog signal reaches the level you specify

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureInterlockedTrigger(
	string source,
	InterlockedHandshakeTriggerAssertedLevel assertedLevel
)
```

```text
Public Sub ConfigureInterlockedTrigger ( 
	source As String,
	assertedLevel As InterlockedHandshakeTriggerAssertedLevel
)
```

###### Parameters

- **source**
  - Type: SystemString The name of a virtual channel or terminal where there is an analog signal to use as the source of the trigger. For E Series devices, if you use a virtual channel, it must be the only channel in the task. The only terminal you can use for E Series devices is PFI0.
- **assertedLevel**
  - Type: NationalInstruments.DAQmxInterlockedHandshakeTriggerAssertedLevel The value of the desired HandshakeEventInterlockedAssertedLevel.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

ConfigureInterlockedTrigger(String, InterlockedHandshakeTriggerAssertedLevel)

Task

Control(TaskAction)

Verify

##### See Also

###### Reference

HandshakeTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_handshaketrigger_configurenone.htm language=enus -->
## TOPIC 00356: HandshakeTriggerConfigureNone Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_handshaketrigger_configurenone.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_handshaketrigger_configurenone.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

HandshakeTrigger.ConfigureNone Method

### HandshakeTriggerConfigureNone Method

handshake triggering

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureNone()
```

```text
Public Sub ConfigureNone
```

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Task

Control(TaskAction)

Verify

##### See Also

###### Reference

HandshakeTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_handshaketrigger_tostring.htm language=enus -->
## TOPIC 00357: HandshakeTriggerToString Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_handshaketrigger_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_handshaketrigger_tostring.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

HandshakeTrigger.ToString Method

### HandshakeTriggerToString Method

Returns a string representation of the object.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

##### See Also

###### Reference

HandshakeTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_ifilteredtypedescriptor_getfilteredtypedescriptor.htm language=enus -->
## TOPIC 00358: IFilteredTypeDescriptorGetFilteredTypeDescriptor Method (PropertyFilterType)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_ifilteredtypedescriptor_getfilteredtypedescriptor.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_ifilteredtypedescriptor_getfilteredtypedescriptor.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

IFilteredTypeDescriptor.GetFilteredTypeDescriptor Method (PropertyFilterType)

### IFilteredTypeDescriptorGetFilteredTypeDescriptor Method (PropertyFilterType)

Task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
ICustomTypeDescriptor GetFilteredTypeDescriptor(
	PropertyFilterType filterType
)
```

```text
Function GetFilteredTypeDescriptor ( 
	filterType As PropertyFilterType
) As ICustomTypeDescriptor
```

###### Parameters

- **filterType**
  - Type: NationalInstruments.DAQmxPropertyFilterTypeThe type of filtering to perform.

###### Return Value

ICustomTypeDescriptor

ICustomTypeDescriptor

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | An invalid enumeration value was passed as an argument to the function. |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Property filtering is a mechanism whereby you can programmatically retrieve a list of properties that are applicable to a specific task's subobject, based on the filtering type.

You can call the GetProperties method on the returned ICustomTypeDescriptor in order to access the list of properties as a PropertyDescriptorCollection. When GetProperties(Attribute) is called with an attribute array as a filter, the returned properties are filtered as if they all have the BrowsableAttribute set to .

##### See Also

###### Reference

IFilteredTypeDescriptor Interface

GetFilteredTypeDescriptor Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_ifilteredtypedescriptor_getfilteredtypedescriptor_1.htm language=enus -->
## TOPIC 00359: IFilteredTypeDescriptorGetFilteredTypeDescriptor Method (PropertyFilterType, PropertyFilterFlags)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_ifilteredtypedescriptor_getfilteredtypedescriptor_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_ifilteredtypedescriptor_getfilteredtypedescriptor_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

IFilteredTypeDescriptor.GetFilteredTypeDescriptor Method (PropertyFilterType, PropertyFilterFlags)

### IFilteredTypeDescriptorGetFilteredTypeDescriptor Method (PropertyFilterType, PropertyFilterFlags)

Task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
ICustomTypeDescriptor GetFilteredTypeDescriptor(
	PropertyFilterType filterType,
	PropertyFilterFlags filterFlags
)
```

```text
Function GetFilteredTypeDescriptor ( 
	filterType As PropertyFilterType,
	filterFlags As PropertyFilterFlags
) As ICustomTypeDescriptor
```

###### Parameters

- **filterType**
  - Type: NationalInstruments.DAQmxPropertyFilterTypeThe type of filtering to perform.
- **filterFlags**
  - Type: NationalInstruments.DAQmxPropertyFilterFlagsThe filtering options.

###### Return Value

ICustomTypeDescriptor

ICustomTypeDescriptor

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | An invalid enumeration value was passed as an argument to the function. |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Property filtering is a mechanism whereby you can programmatically retrieve a list of properties that are applicable to a specific task's subobject, based on the filtering type.

You can call the GetProperties method on the returned ICustomTypeDescriptor in order to access the list of properties as a PropertyDescriptorCollection. When GetProperties(Attribute) is called with an attribute array as a filter, the returned properties are filtered as if they all have the BrowsableAttribute set to .

##### See Also

###### Reference

IFilteredTypeDescriptor Interface

GetFilteredTypeDescriptor Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_interlockedhandshaketrigger_tostring.htm language=enus -->
## TOPIC 00360: InterlockedHandshakeTriggerToString Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_interlockedhandshaketrigger_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_interlockedhandshaketrigger_tostring.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

InterlockedHandshakeTrigger.ToString Method

### InterlockedHandshakeTriggerToString Method

Returns a string representation of the object.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

##### See Also

###### Reference

InterlockedHandshakeTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_linearscale__ctor.htm language=enus -->
## TOPIC 00361: LinearScale Constructor

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_linearscale__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_linearscale__ctor.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

LinearScale Constructor

### LinearScale Constructor

LinearScale

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public LinearScale(
	string name,
	double slope,
	double yIntercept
)
```

```text
Public Sub New ( 
	name As String,
	slope As Double,
	yIntercept As Double
)
```

###### Parameters

- **name**
  - Type: SystemStringThe name of the custom scale for later use, such as when you create a virtual channel.
- **slope**
  - Type: SystemDoubleThe slope, m, in the equation.
- **yIntercept**
  - Type: SystemDoubleThe y-intercept, b, in the equation.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

The equation is identical for input and output. If the equation is in the form x = my + b, you must first solve for y in terms of x.

##### See Also

###### Reference

LinearScale Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_pausetrigger_configureanalogleveltrigger.htm language=enus -->
## TOPIC 00362: PauseTriggerConfigureAnalogLevelTrigger Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_pausetrigger_configureanalogleveltrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_pausetrigger_configureanalogleveltrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

PauseTrigger.ConfigureAnalogLevelTrigger Method

### PauseTriggerConfigureAnalogLevelTrigger Method

above or below a level you specify

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureAnalogLevelTrigger(
	string source,
	AnalogLevelPauseTriggerCondition condition,
	double level
)
```

```text
Public Sub ConfigureAnalogLevelTrigger ( 
	source As String,
	condition As AnalogLevelPauseTriggerCondition,
	level As Double
)
```

###### Parameters

- **source**
  - Type: SystemString The name of a virtual channel or terminal where there is an analog signal to use as the source of the trigger.
- **condition**
  - Type: NationalInstruments.DAQmxAnalogLevelPauseTriggerCondition Specifies if the task pauses acquiring and generating samples when the signal is below level or above level.
- **level**
  - Type: SystemDoubleThe analog threshold level, in the units of the measurement or generation. Use condition to specify if the task pauses above or below this threshold.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

ConfigureAnalogLevelTrigger(String, AnalogLevelPauseTriggerCondition, Double)

Task

Control(TaskAction)

Verify

##### See Also

###### Reference

PauseTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_pausetrigger_configureanalogwindowtrigger.htm language=enus -->
## TOPIC 00363: PauseTriggerConfigureAnalogWindowTrigger Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_pausetrigger_configureanalogwindowtrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_pausetrigger_configureanalogwindowtrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

PauseTrigger.ConfigureAnalogWindowTrigger Method

### PauseTriggerConfigureAnalogWindowTrigger Method

inside or outside of a range you specify

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureAnalogWindowTrigger(
	string source,
	AnalogWindowPauseTriggerCondition condition,
	double top,
	double bottom
)
```

```text
Public Sub ConfigureAnalogWindowTrigger ( 
	source As String,
	condition As AnalogWindowPauseTriggerCondition,
	top As Double,
	bottom As Double
)
```

###### Parameters

- **source**
  - Type: SystemString The name of a virtual channel or terminal where there is an analog signal to use as the source of the trigger.
- **condition**
  - Type: NationalInstruments.DAQmxAnalogWindowPauseTriggerConditionSpecifies if the task pauses acquiring and generating samples when the signal is inside the window or outside the window. Use bottom and top to specify the limits of the window.
- **top**
  - Type: SystemDoubleThe upper limit of the voltage window, in the units of the measurement or generation.
- **bottom**
  - Type: SystemDoubleThe lower limit of the voltage window, in the units of the measurement or generation.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

ConfigureAnalogWindowTrigger(String, AnalogWindowPauseTriggerCondition, Double, Double)

Task

Control(TaskAction)

Verify

##### See Also

###### Reference

PauseTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_pausetrigger_configuredigitalpatterntrigger.htm language=enus -->
## TOPIC 00364: PauseTriggerConfigureDigitalPatternTrigger Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_pausetrigger_configuredigitalpatterntrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_pausetrigger_configuredigitalpatterntrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

PauseTrigger.ConfigureDigitalPatternTrigger Method

### PauseTriggerConfigureDigitalPatternTrigger Method

digital pattern

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureDigitalPatternTrigger(
	string source,
	string pattern,
	DigitalPatternPauseTriggerCondition condition
)
```

```text
Public Sub ConfigureDigitalPatternTrigger ( 
	source As String,
	pattern As String,
	condition As DigitalPatternPauseTriggerCondition
)
```

###### Parameters

- **source**
  - Type: SystemString The physical channels to use for pattern matching. The order of the physical channels determines the order of the pattern. If a port is included, the order of the physical channels within the port is in ascending order.
- **pattern**
  - Type: SystemString The digital pattern that must be met for the trigger to occur.
- **condition**
  - Type: NationalInstruments.DAQmxDigitalPatternPauseTriggerConditionThe condition under which the trigger occurs.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

ConfigureDigitalPatternTrigger(String, String, DigitalPatternPauseTriggerCondition)

Task

Control(TaskAction)

Verify

##### See Also

###### Reference

PauseTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_pausetrigger_configurenone.htm language=enus -->
## TOPIC 00365: PauseTriggerConfigureNone Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_pausetrigger_configurenone.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_pausetrigger_configurenone.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

PauseTrigger.ConfigureNone Method

### PauseTriggerConfigureNone Method

pause triggering

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureNone()
```

```text
Public Sub ConfigureNone
```

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Task

Control(TaskAction)

Verify

##### See Also

###### Reference

PauseTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_pausetrigger_tostring.htm language=enus -->
## TOPIC 00366: PauseTriggerToString Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_pausetrigger_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_pausetrigger_tostring.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

PauseTrigger.ToString Method

### PauseTriggerToString Method

Returns a string representation of the object.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

##### See Also

###### Reference

PauseTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_physicalchannel_clearteds.htm language=enus -->
## TOPIC 00367: PhysicalChannelClearTeds Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_physicalchannel_clearteds.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_physicalchannel_clearteds.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

PhysicalChannel.ClearTeds Method

### PhysicalChannelClearTeds Method

TEDS

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ClearTeds()
```

```text
Public Sub ClearTeds
```

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This method temporarily overrides any TEDS configuration for the physical channel that you performed in Measurement Automation Explorer (MAX).

##### See Also

###### Reference

PhysicalChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_physicalchannel_configureteds.htm language=enus -->
## TOPIC 00368: PhysicalChannelConfigureTeds Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_physicalchannel_configureteds.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_physicalchannel_configureteds.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

PhysicalChannel.ConfigureTeds Method

### PhysicalChannelConfigureTeds Method

TEDS

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureTeds()
```

```text
Public Sub ConfigureTeds
```

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This method temporarily overrides any TEDS configuration for the physical channel that you performed in Measurement Automation Explorer (MAX).

##### See Also

###### Reference

PhysicalChannel Class

ConfigureTeds Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_physicalchannel_configureteds_1.htm language=enus -->
## TOPIC 00369: PhysicalChannelConfigureTeds Method (String)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_physicalchannel_configureteds_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_physicalchannel_configureteds_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

PhysicalChannel.ConfigureTeds Method (String)

### PhysicalChannelConfigureTeds Method (String)

TEDS

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureTeds(
	string virtualTedsFile
)
```

```text
Public Sub ConfigureTeds ( 
	virtualTedsFile As String
)
```

###### Parameters

- **virtualTedsFile**
  - Type: SystemStringThe path to a virtual TEDS file that you want to associate with the physical channel. If you specify Empty for this parameter, this method attempts to find a TEDS sensor connected to the physical channel.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This method temporarily overrides any TEDS configuration for the physical channel that you performed in Measurement Automation Explorer (MAX).

##### See Also

###### Reference

PhysicalChannel Class

ConfigureTeds Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_physicalchannel_dispose.htm language=enus -->
## TOPIC 00370: PhysicalChannelDispose Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_physicalchannel_dispose.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_physicalchannel_dispose.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

PhysicalChannel.Dispose Method

### PhysicalChannelDispose Method

PhysicalChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Dispose()
```

```text
Public Sub Dispose
```

###### Implements

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Use this method only if the application you create runs on a low memory system.

##### See Also

###### Reference

PhysicalChannel Class

Dispose Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_physicalchannel_dispose_1.htm language=enus -->
## TOPIC 00371: PhysicalChannelDispose Method (Boolean)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_physicalchannel_dispose_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_physicalchannel_dispose_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

PhysicalChannel.Dispose Method (Boolean)

### PhysicalChannelDispose Method (Boolean)

PhysicalChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
protected virtual void Dispose(
	bool A_0
)
```

```text
Protected Overridable Sub Dispose ( 
	A_0 As Boolean
)
```

###### Parameters

- **A_0**
  - Type: SystemBoolean

##### Remarks

Cleaning Up Unmanaged Resources

IDisposable

##### See Also

###### Reference

PhysicalChannel Class

Dispose Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_physicalchannel_tostring.htm language=enus -->
## TOPIC 00372: PhysicalChannelToString Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_physicalchannel_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_physicalchannel_tostring.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

PhysicalChannel.ToString Method

### PhysicalChannelToString Method

Returns a string representation of the object.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

##### See Also

###### Reference

PhysicalChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_physicalchannel_writetedsdata.htm language=enus -->
## TOPIC 00373: PhysicalChannelWriteTedsData Method (Byte, BasicTedsDataOption)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_physicalchannel_writetedsdata.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_physicalchannel_writetedsdata.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

PhysicalChannel.WriteTedsData Method (Byte[], BasicTedsDataOption)

### PhysicalChannelWriteTedsData Method (Byte, BasicTedsDataOption)

TEDS

Byte

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void WriteTedsData(
	byte[] bitStream,
	BasicTedsDataOption basicTedsDataOption
)
```

```text
Public Sub WriteTedsData ( 
	bitStream As Byte(),
	basicTedsDataOption As BasicTedsDataOption
)
```

###### Parameters

- **bitStream**
  - Type: SystemByteThe bitstream to write to the sensor. This bitstream must be constructed according to the IEEE 1451.4 specification.
- **basicTedsDataOption**
  - Type: NationalInstruments.DAQmxBasicTedsDataOptionA value that specifies how to handle basic TEDS data in the bitstream.

##### See Also

###### Reference

PhysicalChannel Class

WriteTedsData Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_physicalchannel_writetedsdata_1.htm language=enus -->
## TOPIC 00374: PhysicalChannelWriteTedsData Method (String, BasicTedsDataOption)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_physicalchannel_writetedsdata_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_physicalchannel_writetedsdata_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

PhysicalChannel.WriteTedsData Method (String, BasicTedsDataOption)

### PhysicalChannelWriteTedsData Method (String, BasicTedsDataOption)

TEDS

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void WriteTedsData(
	string virtualTedsFile,
	BasicTedsDataOption basicTedsDataOption
)
```

```text
Public Sub WriteTedsData ( 
	virtualTedsFile As String,
	basicTedsDataOption As BasicTedsDataOption
)
```

###### Parameters

- **virtualTedsFile**
  - Type: SystemStringThe path to a virtual TEDS file that contains the bitstream to write to the sensor.
- **basicTedsDataOption**
  - Type: NationalInstruments.DAQmxBasicTedsDataOptionA value that specifies how to handle basic TEDS data in the bitstream.

##### See Also

###### Reference

PhysicalChannel Class

WriteTedsData Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_polynomialscale__ctor.htm language=enus -->
## TOPIC 00375: PolynomialScale Constructor (String, PolynomialDirection, Double, Double, Double)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_polynomialscale__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_polynomialscale__ctor.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

PolynomialScale Constructor (String, PolynomialDirection, Double[], Double, Double)

### PolynomialScale Constructor (String, PolynomialDirection, Double, Double, Double)

PolynomialScale

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public PolynomialScale(
	string name,
	PolynomialDirection direction,
	double[] coefficients,
	double rangeMinimum,
	double rangeMaximum
)
```

```text
Public Sub New ( 
	name As String,
	direction As PolynomialDirection,
	coefficients As Double(),
	rangeMinimum As Double,
	rangeMaximum As Double
)
```

###### Parameters

- **name**
  - Type: SystemString The name of the custom scale for later use, such as when you create a virtual channel.
- **direction**
  - Type: NationalInstruments.DAQmxPolynomialDirection The conversion direction of the specified polynomial. The opposite polynomial is computed by the PolynomialScale.
- **coefficients**
  - Type: SystemDouble The array of coefficients of a polynomial. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9x3. This polynomial is used as either the forward or reverse polynomial depending on the direction specified.
- **rangeMinimum**
  - Type: SystemDouble The minimum of the range over which the polynomial specified is valid or of interest.
- **rangeMaximum**
  - Type: SystemDouble The maximum of the range over which the polynomial specified is valid or of interest.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

PolynomialScale Class

PolynomialScale Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_polynomialscale__ctor_1.htm language=enus -->
## TOPIC 00376: PolynomialScale Constructor (String, PolynomialDirection, Double, Double, Double, Int32, Int32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_polynomialscale__ctor_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_polynomialscale__ctor_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

PolynomialScale Constructor (String, PolynomialDirection, Double[], Double, Double, Int32, Int32)

### PolynomialScale Constructor (String, PolynomialDirection, Double, Double, Double, Int32, Int32)

PolynomialScale

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public PolynomialScale(
	string name,
	PolynomialDirection direction,
	double[] coefficients,
	double rangeMinimum,
	double rangeMaximum,
	int numberOfPointsInFit,
	int orderOfFit
)
```

```text
Public Sub New ( 
	name As String,
	direction As PolynomialDirection,
	coefficients As Double(),
	rangeMinimum As Double,
	rangeMaximum As Double,
	numberOfPointsInFit As Integer,
	orderOfFit As Integer
)
```

###### Parameters

- **name**
  - Type: SystemString The name of the custom scale for later use, such as when you create a virtual channel.
- **direction**
  - Type: NationalInstruments.DAQmxPolynomialDirection The conversion direction of the specified polynomial. The opposite polynomial is computed by the PolynomialScale.
- **coefficients**
  - Type: SystemDouble The array of coefficients of a polynomial. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9x3. This polynomial is used as either the forward or reverse polynomial depending on the direction specified.
- **rangeMinimum**
  - Type: SystemDouble The minimum of the range over which the polynomial specified is valid or of interest.
- **rangeMaximum**
  - Type: SystemDouble The maximum of the range over which the polynomial specified is valid or of interest.
- **numberOfPointsInFit**
  - Type: SystemInt32 The number of points to evaluate for computing the polynomial of the opposite direction.
- **orderOfFit**
  - Type: SystemInt32 The order of polynomial to compute for the opposite polynomial to the one provided. Specify -1 to use the same order as the forward polynomial.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

PolynomialScale Class

PolynomialScale Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_polynomialscale__ctor_2.htm language=enus -->
## TOPIC 00377: PolynomialScale Constructor (String, Double, Double)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_polynomialscale__ctor_2.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_polynomialscale__ctor_2.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

PolynomialScale Constructor (String, Double[], Double[])

### PolynomialScale Constructor (String, Double, Double)

PolynomialScale

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public PolynomialScale(
	string name,
	double[] forwardCoefficients,
	double[] reverseCoefficients
)
```

```text
Public Sub New ( 
	name As String,
	forwardCoefficients As Double(),
	reverseCoefficients As Double()
)
```

###### Parameters

- **name**
  - Type: SystemStringThe name of the custom scale for later use, such as when you create a virtual channel.
- **forwardCoefficients**
  - Type: SystemDouble The array of the forward coefficients of the polynomial. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9x3.
- **reverseCoefficients**
  - Type: SystemDoubleThe array of the reverse coefficients of the polynomial. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9y3.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

PolynomialScale Class

PolynomialScale Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_rangemapscale__ctor.htm language=enus -->
## TOPIC 00378: RangeMapScale Constructor

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_rangemapscale__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_rangemapscale__ctor.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

RangeMapScale Constructor

### RangeMapScale Constructor

RangeMapScale

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public RangeMapScale(
	string name,
	double prescaledMinimum,
	double prescaledMaximum,
	double scaledMinimum,
	double scaledMaximum
)
```

```text
Public Sub New ( 
	name As String,
	prescaledMinimum As Double,
	prescaledMaximum As Double,
	scaledMinimum As Double,
	scaledMaximum As Double
)
```

###### Parameters

- **name**
  - Type: SystemStringThe name of the custom scale for later use, such as when you create a virtual channel.
- **prescaledMinimum**
  - Type: SystemDoubleThe smallest value in the range of prescaled values.
- **prescaledMaximum**
  - Type: SystemDoubleThe largest value in the range of prescaled values.
- **scaledMinimum**
  - Type: SystemDoubleThe smallest value in the range of scaled values.
- **scaledMaximum**
  - Type: SystemDoubleThe largest value in the range of scaled values.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

RangeMapScale Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_referencetrigger_configureanalogedgetrigger.htm language=enus -->
## TOPIC 00379: ReferenceTriggerConfigureAnalogEdgeTrigger Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_referencetrigger_configureanalogedgetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_referencetrigger_configureanalogedgetrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ReferenceTrigger.ConfigureAnalogEdgeTrigger Method

### ReferenceTriggerConfigureAnalogEdgeTrigger Method

analog signal reaches the level you specify

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureAnalogEdgeTrigger(
	string source,
	AnalogEdgeReferenceTriggerSlope slope,
	double level,
	long pretriggerSamples
)
```

```text
Public Sub ConfigureAnalogEdgeTrigger ( 
	source As String,
	slope As AnalogEdgeReferenceTriggerSlope,
	level As Double,
	pretriggerSamples As Long
)
```

###### Parameters

- **source**
  - Type: SystemString The name of a virtual channel or terminal where there is an analog signal to use as the source of the trigger. For E Series devices, if you use a virtual channel, it must be the only channel in the task. The only terminal you can use for E Series devices is PFI0.
- **slope**
  - Type: NationalInstruments.DAQmxAnalogEdgeReferenceTriggerSlope The slope of the signal on which the reference trigger occurs.
- **level**
  - Type: SystemDouble The threshold, in the units of the measurement or generation, to trigger. Use slope to specify on which slope to trigger at this threshold.
- **pretriggerSamples**
  - Type: SystemInt64 The minimum number of samples per channel to acquire before recognizing the reference trigger.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

The number of post-trigger samples is equal to the value of [SamplesPerChannel](p_nationalinstruments_daqmx_timing_samplesperchannel.htm) minus the value of pretriggerSamples. If pretriggerSamples equals [SamplesPerChannel](p_nationalinstruments_daqmx_timing_samplesperchannel.htm), the measurement or generation stops when the reference trigger occurs.

When you use a [Reference Trigger](/csh?topicname=mxcncpts/;), the default value of the [ReadRelativeTo](p_nationalinstruments_daqmx_daqstream_readrelativeto.htm) property is [FirstPretriggerSample](t_nationalinstruments_daqmx_readrelativeto.htm) with a [ReadOffset](p_nationalinstruments_daqmx_daqstream_readoffset.htm) value of 0.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. ConfigureAnalogEdgeTrigger(String, AnalogEdgeReferenceTriggerSlope, Double, Int64) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

ReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_referencetrigger_configureanalogmultiedgetrigger.htm language=enus -->
## TOPIC 00380: ReferenceTriggerConfigureAnalogMultiEdgeTrigger Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_referencetrigger_configureanalogmultiedgetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_referencetrigger_configureanalogmultiedgetrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ReferenceTrigger.ConfigureAnalogMultiEdgeTrigger Method

### ReferenceTriggerConfigureAnalogMultiEdgeTrigger Method

Configures the task to stop the acquisition when the device acquires all pretrigger samples, any of the configured analog signals reaches the levels you specify, and the device acquires all post-trigger samples.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureAnalogMultiEdgeTrigger(
	string sources,
	AnalogMultiEdgeReferenceTriggerSlope[] slopes,
	double[] levels,
	long pretriggerSamples
)
```

```text
Public Sub ConfigureAnalogMultiEdgeTrigger ( 
	sources As String,
	slopes As AnalogMultiEdgeReferenceTriggerSlope(),
	levels As Double(),
	pretriggerSamples As Long
)
```

###### Parameters

- **sources**
  - Type: SystemStringA string specifying a list of terminals, physical channel names, or ranges of physical channels where there are analog signals to use as the sources of the trigger.
- **slopes**
  - Type: NationalInstruments.DAQmxAnalogMultiEdgeReferenceTriggerSlopeAn array containing the slopes of the signals to start acquiring or generating samples when the respective signal crosses the respective trigger level. Each element corresponds to the sources specified in sources and elements in the other array parameters.
- **levels**
  - Type: SystemDoubleAn array containing the thresholds at which to start acquiring or generating samples. Each element corresponds to the sources specified in sources and elements in the other array parameters. Specify these values in the units of the measurement or generation. Use slopes to specify on which slopes to trigger at the respective thresholds.
- **pretriggerSamples**
  - Type: SystemInt64The minimum number of samples per channel to acquire before recognizing the reference trigger. The number of posttrigger samples per channel is equal to SamplesPerChannel minus pretriggerSamples.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

ReferenceTrigger

ReadRelativeTo

FirstPretriggerSample

ReadOffset

The number of trigger sources represented by sources and the number of elements in slopes and levels must all be the same.

##### See Also

###### Reference

ReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_referencetrigger_configureanalogwindowtrigger.htm language=enus -->
## TOPIC 00381: ReferenceTriggerConfigureAnalogWindowTrigger Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_referencetrigger_configureanalogwindowtrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_referencetrigger_configureanalogwindowtrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ReferenceTrigger.ConfigureAnalogWindowTrigger Method

### ReferenceTriggerConfigureAnalogWindowTrigger Method

analog signal enters or leaves a range you specify

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureAnalogWindowTrigger(
	string source,
	AnalogWindowReferenceTriggerCondition condition,
	double top,
	double bottom,
	long pretriggerSamples
)
```

```text
Public Sub ConfigureAnalogWindowTrigger ( 
	source As String,
	condition As AnalogWindowReferenceTriggerCondition,
	top As Double,
	bottom As Double,
	pretriggerSamples As Long
)
```

###### Parameters

- **source**
  - Type: SystemString The name of a virtual channel or terminal where there is an analog signal to use as the source of the trigger. For E Series devices, if you use a virtual channel, it must be the only channel in the task. The only terminal you can use for E Series devices is PFI0.
- **condition**
  - Type: NationalInstruments.DAQmxAnalogWindowReferenceTriggerCondition Specifies if the reference trigger occurs when the signal enters the window or leaves the window. Use bottom and top to specify the limits of the window.
- **top**
  - Type: SystemDoubleThe upper limit of the voltage window, in the units of the measurement or generation.
- **bottom**
  - Type: SystemDoubleThe lower limit of the voltage window, in the units of the measurement or generation.
- **pretriggerSamples**
  - Type: SystemInt64 The minimum number of samples per channel to acquire before recognizing the reference trigger.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

The number of post-trigger samples is equal to the value of [SamplesPerChannel](p_nationalinstruments_daqmx_timing_samplesperchannel.htm) minus the value of pretriggerSamples. If pretriggerSamples equals [SamplesPerChannel](p_nationalinstruments_daqmx_timing_samplesperchannel.htm), the measurement or generation stops when the reference trigger occurs.

When you use a [Reference Trigger](/csh?topicname=mxcncpts/;), the default value of the [ReadRelativeTo](p_nationalinstruments_daqmx_daqstream_readrelativeto.htm) property is [FirstPretriggerSample](t_nationalinstruments_daqmx_readrelativeto.htm) with a [ReadOffset](p_nationalinstruments_daqmx_daqstream_readoffset.htm) value of 0.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. ConfigureAnalogWindowTrigger(String, AnalogWindowReferenceTriggerCondition, Double, Double, Int64) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

ReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_referencetrigger_configuredigitaledgetrigger.htm language=enus -->
## TOPIC 00382: ReferenceTriggerConfigureDigitalEdgeTrigger Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_referencetrigger_configuredigitaledgetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_referencetrigger_configuredigitaledgetrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ReferenceTrigger.ConfigureDigitalEdgeTrigger Method

### ReferenceTriggerConfigureDigitalEdgeTrigger Method

detects a rising or falling edge of a digital signal

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureDigitalEdgeTrigger(
	string source,
	DigitalEdgeReferenceTriggerEdge edge,
	long pretriggerSamples
)
```

```text
Public Sub ConfigureDigitalEdgeTrigger ( 
	source As String,
	edge As DigitalEdgeReferenceTriggerEdge,
	pretriggerSamples As Long
)
```

###### Parameters

- **source**
  - Type: SystemStringThe name of the terminal where there is a digital signal to use as the source of the trigger.
- **edge**
  - Type: NationalInstruments.DAQmxDigitalEdgeReferenceTriggerEdgeThe edge of the digital signal on which the reference trigger occurs.
- **pretriggerSamples**
  - Type: SystemInt64The minimum number of samples to acquire per channel before recognizing the reference trigger.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

The number of post-trigger samples is equal to the value of [SamplesPerChannel](p_nationalinstruments_daqmx_timing_samplesperchannel.htm) minus the value of pretriggerSamples. If pretriggerSamples equals [SamplesPerChannel](p_nationalinstruments_daqmx_timing_samplesperchannel.htm), the measurement or generation stops when the reference trigger occurs.

When you use a [Reference Trigger](/csh?topicname=mxcncpts/;), the default value of the [ReadRelativeTo](p_nationalinstruments_daqmx_daqstream_readrelativeto.htm) property is [FirstPretriggerSample](t_nationalinstruments_daqmx_readrelativeto.htm) with a [ReadOffset](p_nationalinstruments_daqmx_daqstream_readoffset.htm) value of 0.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. ConfigureDigitalEdgeTrigger(String, DigitalEdgeReferenceTriggerEdge, Int64) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

ReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_referencetrigger_configuredigitalpatterntrigger.htm language=enus -->
## TOPIC 00383: ReferenceTriggerConfigureDigitalPatternTrigger Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_referencetrigger_configuredigitalpatterntrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_referencetrigger_configuredigitalpatterntrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ReferenceTrigger.ConfigureDigitalPatternTrigger Method

### ReferenceTriggerConfigureDigitalPatternTrigger Method

digital pattern

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureDigitalPatternTrigger(
	string source,
	string pattern,
	DigitalPatternReferenceTriggerCondition condition,
	long pretriggerSamples
)
```

```text
Public Sub ConfigureDigitalPatternTrigger ( 
	source As String,
	pattern As String,
	condition As DigitalPatternReferenceTriggerCondition,
	pretriggerSamples As Long
)
```

###### Parameters

- **source**
  - Type: SystemString The physical channels to use for pattern matching. The order of the physical channels determines the order of the pattern. If a port is included, the order of the physical channels within the port is in ascending order.
- **pattern**
  - Type: SystemString The digital pattern that must be met for the trigger to occur.
- **condition**
  - Type: NationalInstruments.DAQmxDigitalPatternReferenceTriggerConditionThe condition under which the trigger occurs.
- **pretriggerSamples**
  - Type: SystemInt64The minimum number of samples to acquire per channel before recognizing the reference trigger.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

ConfigureDigitalPatternTrigger(String, String, DigitalPatternReferenceTriggerCondition, Int64)

Task

Control(TaskAction)

Verify

##### See Also

###### Reference

ReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_referencetrigger_configurenone.htm language=enus -->
## TOPIC 00384: ReferenceTriggerConfigureNone Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_referencetrigger_configurenone.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_referencetrigger_configurenone.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ReferenceTrigger.ConfigureNone Method

### ReferenceTriggerConfigureNone Method

reference triggering

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureNone()
```

```text
Public Sub ConfigureNone
```

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Task

Control(TaskAction)

Verify

##### See Also

###### Reference

ReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_referencetrigger_tostring.htm language=enus -->
## TOPIC 00385: ReferenceTriggerToString Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_referencetrigger_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_referencetrigger_tostring.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ReferenceTrigger.ToString Method

### ReferenceTriggerToString Method

Returns a string representation of the object.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

##### See Also

###### Reference

ReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_sampleclockeventargs_getobjectdata.htm language=enus -->
## TOPIC 00386: SampleClockEventArgsGetObjectData Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_sampleclockeventargs_getobjectdata.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_sampleclockeventargs_getobjectdata.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SampleClockEventArgs.GetObjectData Method

### SampleClockEventArgsGetObjectData Method

SerializationInfo

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
protected virtual void GetObjectData(
	SerializationInfo info,
	StreamingContext context
)
```

```text
Protected Overridable Sub GetObjectData ( 
	info As SerializationInfo,
	context As StreamingContext
)
```

###### Parameters

- **info**
  - Type: System.Runtime.SerializationSerializationInfo Object that holds the serialized object data.
- **context**
  - Type: System.Runtime.SerializationStreamingContext Contextual information about the source or destination.

##### See Also

###### Reference

SampleClockEventArgs Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_samplecompleteeventargs_getobjectdata.htm language=enus -->
## TOPIC 00387: SampleCompleteEventArgsGetObjectData Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_samplecompleteeventargs_getobjectdata.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_samplecompleteeventargs_getobjectdata.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SampleCompleteEventArgs.GetObjectData Method

### SampleCompleteEventArgsGetObjectData Method

SerializationInfo

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
protected virtual void GetObjectData(
	SerializationInfo info,
	StreamingContext context
)
```

```text
Protected Overridable Sub GetObjectData ( 
	info As SerializationInfo,
	context As StreamingContext
)
```

###### Parameters

- **info**
  - Type: System.Runtime.SerializationSerializationInfo Object that holds the serialized object data.
- **context**
  - Type: System.Runtime.SerializationStreamingContext Contextual information about the source or destination.

##### See Also

###### Reference

SampleCompleteEventArgs Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_savedchannelinfo_dispose.htm language=enus -->
## TOPIC 00388: SavedChannelInfoDispose Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_savedchannelinfo_dispose.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_savedchannelinfo_dispose.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SavedChannelInfo.Dispose Method

### SavedChannelInfoDispose Method

SavedChannelInfo

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Dispose()
```

```text
Public Sub Dispose
```

###### Implements

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

SavedChannelInfo Class

Dispose Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_savedchannelinfo_dispose_1.htm language=enus -->
## TOPIC 00389: SavedChannelInfoDispose Method (Boolean)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_savedchannelinfo_dispose_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_savedchannelinfo_dispose_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SavedChannelInfo.Dispose Method (Boolean)

### SavedChannelInfoDispose Method (Boolean)

SavedChannelInfo

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
protected virtual void Dispose(
	bool A_0
)
```

```text
Protected Overridable Sub Dispose ( 
	A_0 As Boolean
)
```

###### Parameters

- **A_0**
  - Type: SystemBoolean

##### Remarks

Cleaning Up Unmanaged Resources

IDisposable

##### See Also

###### Reference

SavedChannelInfo Class

Dispose Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_savedchannelinfo_tostring.htm language=enus -->
## TOPIC 00390: SavedChannelInfoToString Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_savedchannelinfo_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_savedchannelinfo_tostring.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SavedChannelInfo.ToString Method

### SavedChannelInfoToString Method

Returns a string representation of the object.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

##### See Also

###### Reference

SavedChannelInfo Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_savedscaleinfo_dispose.htm language=enus -->
## TOPIC 00391: SavedScaleInfoDispose Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_savedscaleinfo_dispose.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_savedscaleinfo_dispose.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SavedScaleInfo.Dispose Method

### SavedScaleInfoDispose Method

SavedScaleInfo

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Dispose()
```

```text
Public Sub Dispose
```

###### Implements

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

SavedScaleInfo Class

Dispose Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_savedscaleinfo_dispose_1.htm language=enus -->
## TOPIC 00392: SavedScaleInfoDispose Method (Boolean)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_savedscaleinfo_dispose_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_savedscaleinfo_dispose_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SavedScaleInfo.Dispose Method (Boolean)

### SavedScaleInfoDispose Method (Boolean)

SavedScaleInfo

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
protected virtual void Dispose(
	bool A_0
)
```

```text
Protected Overridable Sub Dispose ( 
	A_0 As Boolean
)
```

###### Parameters

- **A_0**
  - Type: SystemBoolean

##### Remarks

Cleaning Up Unmanaged Resources

IDisposable

##### See Also

###### Reference

SavedScaleInfo Class

Dispose Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_savedscaleinfo_tostring.htm language=enus -->
## TOPIC 00393: SavedScaleInfoToString Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_savedscaleinfo_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_savedscaleinfo_tostring.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SavedScaleInfo.ToString Method

### SavedScaleInfoToString Method

Returns a string representation of the object.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

##### See Also

###### Reference

SavedScaleInfo Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_savedtaskinfo_dispose.htm language=enus -->
## TOPIC 00394: SavedTaskInfoDispose Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_savedtaskinfo_dispose.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_savedtaskinfo_dispose.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SavedTaskInfo.Dispose Method

### SavedTaskInfoDispose Method

SavedTaskInfo

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Dispose()
```

```text
Public Sub Dispose
```

###### Implements

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

SavedTaskInfo Class

Dispose Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_savedtaskinfo_dispose_1.htm language=enus -->
## TOPIC 00395: SavedTaskInfoDispose Method (Boolean)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_savedtaskinfo_dispose_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_savedtaskinfo_dispose_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SavedTaskInfo.Dispose Method (Boolean)

### SavedTaskInfoDispose Method (Boolean)

SavedTaskInfo

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
protected virtual void Dispose(
	bool A_0
)
```

```text
Protected Overridable Sub Dispose ( 
	A_0 As Boolean
)
```

###### Parameters

- **A_0**
  - Type: SystemBoolean

##### Remarks

Cleaning Up Unmanaged Resources

IDisposable

##### See Also

###### Reference

SavedTaskInfo Class

Dispose Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_savedtaskinfo_tostring.htm language=enus -->
## TOPIC 00396: SavedTaskInfoToString Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_savedtaskinfo_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_savedtaskinfo_tostring.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SavedTaskInfo.ToString Method

### SavedTaskInfoToString Method

Returns a string representation of the object.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

##### See Also

###### Reference

SavedTaskInfo Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_scale__ctor.htm language=enus -->
## TOPIC 00397: Scale Constructor

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_scale__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_scale__ctor.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Scale Constructor

### Scale Constructor

Scale

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
protected Scale(
	string name
)
```

```text
Protected Sub New ( 
	name As String
)
```

###### Parameters

- **name**
  - Type: SystemStringThe name of the scale.

##### Remarks

Scale

LoadScale(String)

Local

DaqSystem

##### See Also

###### Reference

Scale Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_scale_dispose.htm language=enus -->
## TOPIC 00398: ScaleDispose Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_scale_dispose.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_scale_dispose.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Scale.Dispose Method

### ScaleDispose Method

Scale

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Dispose()
```

```text
Public Sub Dispose
```

###### Implements

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Use this method only if the application you create runs on a low memory system.

##### See Also

###### Reference

Scale Class

Dispose Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_scale_dispose_1.htm language=enus -->
## TOPIC 00399: ScaleDispose Method (Boolean)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_scale_dispose_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_scale_dispose_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Scale.Dispose Method (Boolean)

### ScaleDispose Method (Boolean)

Scale

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
protected virtual void Dispose(
	bool A_0
)
```

```text
Protected Overridable Sub Dispose ( 
	A_0 As Boolean
)
```

###### Parameters

- **A_0**
  - Type: SystemBoolean

##### Remarks

Cleaning Up Unmanaged Resources

IDisposable

##### See Also

###### Reference

Scale Class

Dispose Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_scale_tostring.htm language=enus -->
## TOPIC 00400: ScaleToString Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_scale_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_scale_tostring.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Scale.ToString Method

### ScaleToString Method

Returns a string representation of the object.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

##### See Also

###### Reference

Scale Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_singlepoint_tostring.htm language=enus -->
## TOPIC 00401: SinglePointToString Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_singlepoint_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_singlepoint_tostring.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SinglePoint.ToString Method

### SinglePointToString Method

Returns a string representation of the object.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

##### See Also

###### Reference

SinglePoint Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_singlepoint_waitfornextsampleclock.htm language=enus -->
## TOPIC 00402: SinglePointWaitForNextSampleClock Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_singlepoint_waitfornextsampleclock.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_singlepoint_waitfornextsampleclock.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SinglePoint.WaitForNextSampleClock Method

### SinglePointWaitForNextSampleClock Method

sample clock

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool WaitForNextSampleClock()
```

```text
Public Function WaitForNextSampleClock As Boolean
```

###### Return Value

Boolean

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

If an extra sample clock pulse occurs between calls to this method, the second call returns an error or warning and waits for the next sample clock pulse. Use the [ConvertLateErrorsToWarnings](p_nationalinstruments_daqmx_singlepoint_convertlateerrorstowarnings.htm) property to specify whether this method returns errors or warnings.

Use this method to ensure [I/O cycles](/csh?topicname=mxcncpts/;) complete within sample clock periods. National Instruments recommends you use this method for certain applications only.

##### See Also

###### Reference

SinglePoint Class

WaitForNextSampleClock Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_singlepoint_waitfornextsampleclock_1.htm language=enus -->
## TOPIC 00403: SinglePointWaitForNextSampleClock Method (Double)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_singlepoint_waitfornextsampleclock_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_singlepoint_waitfornextsampleclock_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SinglePoint.WaitForNextSampleClock Method (Double)

### SinglePointWaitForNextSampleClock Method (Double)

sample clock

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool WaitForNextSampleClock(
	double timeout
)
```

```text
Public Function WaitForNextSampleClock ( 
	timeout As Double
) As Boolean
```

###### Parameters

- **timeout**
  - Type: SystemDouble The maximum amount of time, in seconds, to wait for the next sample clock pulse. If the time elapses, this method returns an error. If you set timeout to -1, this method waits indefinitely.

###### Return Value

Boolean

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

If an extra sample clock pulse occurs between calls to this method, the second call returns an error or warning and waits for the next sample clock pulse. Use the [ConvertLateErrorsToWarnings](p_nationalinstruments_daqmx_singlepoint_convertlateerrorstowarnings.htm) property to specify whether this method returns errors or warnings.

Use this method to ensure [I/O cycles](/csh?topicname=mxcncpts/;) complete within sample clock periods. National Instruments recommends you use this method for certain applications only.

##### See Also

###### Reference

SinglePoint Class

WaitForNextSampleClock Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_starttrigger_configureanalogedgetrigger.htm language=enus -->
## TOPIC 00404: StartTriggerConfigureAnalogEdgeTrigger Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_starttrigger_configureanalogedgetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_starttrigger_configureanalogedgetrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

StartTrigger.ConfigureAnalogEdgeTrigger Method

### StartTriggerConfigureAnalogEdgeTrigger Method

analog signal crosses the level you specify

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureAnalogEdgeTrigger(
	string source,
	AnalogEdgeStartTriggerSlope slope,
	double level
)
```

```text
Public Sub ConfigureAnalogEdgeTrigger ( 
	source As String,
	slope As AnalogEdgeStartTriggerSlope,
	level As Double
)
```

###### Parameters

- **source**
  - Type: SystemString The name of a virtual channel or terminal where there is a digital signal to use as the source of the trigger. For E Series devices, if you use a channel name, the channel must be the first channel in the task. The only terminal you can use for E Series devices is PFI0.
- **slope**
  - Type: NationalInstruments.DAQmxAnalogEdgeStartTriggerSlope The slope of the signal to start acquiring or generating samples when the signal crosses level.
- **level**
  - Type: SystemDoubleThe threshold to start acquiring or generating samples, in the units of the measurement or generation. Use slope to specify on which slope to trigger at this threshold.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

ConfigureAnalogEdgeTrigger(String, AnalogEdgeStartTriggerSlope, Double)

Task

Control(TaskAction)

Verify

##### See Also

###### Reference

StartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_starttrigger_configureanalogmultiedgetrigger.htm language=enus -->
## TOPIC 00405: StartTriggerConfigureAnalogMultiEdgeTrigger Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_starttrigger_configureanalogmultiedgetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_starttrigger_configureanalogmultiedgetrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

StartTrigger.ConfigureAnalogMultiEdgeTrigger Method

### StartTriggerConfigureAnalogMultiEdgeTrigger Method

Configures the task to start acquiring or generating samples when any of the configured analog signals cross the respective levels you specify.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureAnalogMultiEdgeTrigger(
	string sources,
	AnalogMultiEdgeStartTriggerSlope[] slopes,
	double[] levels
)
```

```text
Public Sub ConfigureAnalogMultiEdgeTrigger ( 
	sources As String,
	slopes As AnalogMultiEdgeStartTriggerSlope(),
	levels As Double()
)
```

###### Parameters

- **sources**
  - Type: SystemStringA string specifying a list of terminals, physical channel names, or ranges of physical channels where there are analog signals to use as the sources of the trigger.
- **slopes**
  - Type: NationalInstruments.DAQmxAnalogMultiEdgeStartTriggerSlopeAn array containing the slopes of the signals to start acquiring or generating samples when the respective signal crosses the respective trigger level. Each element corresponds to the sources specified in sources and elements in the other array parameters.
- **levels**
  - Type: SystemDoubleAn array containing the thresholds at which to start acquiring or generating samples. Each element corresponds to the sources specified in sources and elements in the other array parameters. Specify these values in the units of the measurement or generation. Use slopes to specify on which slopes to trigger at the respective thresholds.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

The number of trigger sources represented by sources and the number of elements in slopes and levels must all be the same.

##### See Also

###### Reference

StartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_starttrigger_configureanalogwindowtrigger.htm language=enus -->
## TOPIC 00406: StartTriggerConfigureAnalogWindowTrigger Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_starttrigger_configureanalogwindowtrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_starttrigger_configureanalogwindowtrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

StartTrigger.ConfigureAnalogWindowTrigger Method

### StartTriggerConfigureAnalogWindowTrigger Method

analog signal enters or leaves a range you specify

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureAnalogWindowTrigger(
	string source,
	AnalogWindowStartTriggerCondition condition,
	double top,
	double bottom
)
```

```text
Public Sub ConfigureAnalogWindowTrigger ( 
	source As String,
	condition As AnalogWindowStartTriggerCondition,
	top As Double,
	bottom As Double
)
```

###### Parameters

- **source**
  - Type: SystemString The name of a virtual channel or terminal where there is a digital signal to use as the source of the trigger. For E Series devices, if you use a channel name, the channel must be the first channel in the task. The only terminal you can use for E Series devices is PFI0.
- **condition**
  - Type: NationalInstruments.DAQmxAnalogWindowStartTriggerCondition Specifies if the reference trigger occurs when the signal enters the window or leaves the window. Use bottom and top to specify the limits of the window.
- **top**
  - Type: SystemDoubleThe upper limit of the voltage window, in the units of the measurement or generation.
- **bottom**
  - Type: SystemDoubleThe lower limit of the voltage window, in the units of the measurement or generation.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

ConfigureAnalogWindowTrigger(String, AnalogWindowStartTriggerCondition, Double, Double)

Task

Control(TaskAction)

Verify

##### See Also

###### Reference

StartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_starttrigger_configuredigitaledgetrigger.htm language=enus -->
## TOPIC 00407: StartTriggerConfigureDigitalEdgeTrigger Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_starttrigger_configuredigitaledgetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_starttrigger_configuredigitaledgetrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

StartTrigger.ConfigureDigitalEdgeTrigger Method

### StartTriggerConfigureDigitalEdgeTrigger Method

rising or falling edge of a digital signal

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureDigitalEdgeTrigger(
	string source,
	DigitalEdgeStartTriggerEdge edge
)
```

```text
Public Sub ConfigureDigitalEdgeTrigger ( 
	source As String,
	edge As DigitalEdgeStartTriggerEdge
)
```

###### Parameters

- **source**
  - Type: SystemString The name of a terminal where there is a digital signal to use as the source of the trigger.
- **edge**
  - Type: NationalInstruments.DAQmxDigitalEdgeStartTriggerEdge The edge of the digital signal to start acquiring or generating samples.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

ConfigureDigitalEdgeTrigger(String, DigitalEdgeStartTriggerEdge)

Task

Control(TaskAction)

Verify

##### See Also

###### Reference

StartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_starttrigger_configuredigitalpatterntrigger.htm language=enus -->
## TOPIC 00408: StartTriggerConfigureDigitalPatternTrigger Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_starttrigger_configuredigitalpatterntrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_starttrigger_configuredigitalpatterntrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

StartTrigger.ConfigureDigitalPatternTrigger Method

### StartTriggerConfigureDigitalPatternTrigger Method

digital pattern

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureDigitalPatternTrigger(
	string source,
	string pattern,
	DigitalPatternStartTriggerCondition condition
)
```

```text
Public Sub ConfigureDigitalPatternTrigger ( 
	source As String,
	pattern As String,
	condition As DigitalPatternStartTriggerCondition
)
```

###### Parameters

- **source**
  - Type: SystemString The physical channels to use for pattern matching. The order of the physical channels determines the order of the pattern. If a port is included, the order of the physical channels within the port is in ascending order.
- **pattern**
  - Type: SystemString The digital pattern that must be met for the trigger to occur.
- **condition**
  - Type: NationalInstruments.DAQmxDigitalPatternStartTriggerConditionThe condition under which the trigger occurs.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

ConfigureDigitalPatternTrigger(String, String, DigitalPatternStartTriggerCondition)

Task

Control(TaskAction)

Verify

##### See Also

###### Reference

StartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_starttrigger_configurenone.htm language=enus -->
## TOPIC 00409: StartTriggerConfigureNone Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_starttrigger_configurenone.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_starttrigger_configurenone.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

StartTrigger.ConfigureNone Method

### StartTriggerConfigureNone Method

Configures the task to start acquiring or generating samples immediately upon starting the task.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureNone()
```

```text
Public Sub ConfigureNone
```

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Task

Control(TaskAction)

Verify

##### See Also

###### Reference

StartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_starttrigger_configuretimetrigger.htm language=enus -->
## TOPIC 00410: StartTriggerConfigureTimeTrigger Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_starttrigger_configuretimetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_starttrigger_configuretimetrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

StartTrigger.ConfigureTimeTrigger Method

### StartTriggerConfigureTimeTrigger Method

triggerTime

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureTimeTrigger(
	PrecisionDateTime triggerTime,
	TimeStartTriggerTimescale timescale
)
```

```text
Public Sub ConfigureTimeTrigger ( 
	triggerTime As PrecisionDateTime,
	timescale As TimeStartTriggerTimescale
)
```

###### Parameters

- **triggerTime**
  - Type: NationalInstrumentsPrecisionDateTimeThe start trigger time.
- **timescale**
  - Type: NationalInstruments.DAQmxTimeStartTriggerTimescaleThe timescale of the triggerTime. For more information, see TimeStartTriggerTimescale.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

| Note |
| --- |
| The trigger time is represented by a PrecisionDateTime expressed as a UTC time. To set a trigger time based on the current system time, use UtcNow, adding an offset, rather than Now. |

##### See Also

###### Reference

StartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_starttrigger_tostring.htm language=enus -->
## TOPIC 00411: StartTriggerToString Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_starttrigger_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_starttrigger_tostring.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

StartTrigger.ToString Method

### StartTriggerToString Method

Returns a string representation of the object.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

##### See Also

###### Reference

StartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_switch_settopologyandreset.htm language=enus -->
## TOPIC 00412: SwitchSetTopologyAndReset Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_switch_settopologyandreset.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_switch_settopologyandreset.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Switch.SetTopologyAndReset Method

### SwitchSetTopologyAndReset Method

topology

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void SetTopologyAndReset(
	string newTopology
)
```

```text
Public Sub SetTopologyAndReset ( 
	newTopology As String
)
```

###### Parameters

- **newTopology**
  - Type: SystemStringThe switch topology to use on the device.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

newTopology

##### See Also

###### Reference

Switch Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_switch_tostring.htm language=enus -->
## TOPIC 00413: SwitchToString Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_switch_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_switch_tostring.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Switch.ToString Method

### SwitchToString Method

Returns a string representation of the object.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

##### See Also

###### Reference

Switch Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_switch_waitforsettling.htm language=enus -->
## TOPIC 00414: SwitchWaitForSettling Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_switch_waitforsettling.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_switch_waitforsettling.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Switch.WaitForSettling Method

### SwitchWaitForSettling Method

Waits for the settling time on the device to expire.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void WaitForSettling()
```

```text
Public Sub WaitForSettling
```

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

The settling time is reset and begins counting down upon a switch operation. Therefore, this method might return immediately if no operation happened recently.

##### See Also

###### Reference

Switch Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_switchchannel_dispose.htm language=enus -->
## TOPIC 00415: SwitchChannelDispose Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_switchchannel_dispose.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_switchchannel_dispose.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchChannel.Dispose Method

### SwitchChannelDispose Method

SwitchChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Dispose()
```

```text
Public Sub Dispose
```

###### Implements

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Use this method only if the application you create runs on a low memory system.

##### See Also

###### Reference

SwitchChannel Class

Dispose Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_switchchannel_dispose_1.htm language=enus -->
## TOPIC 00416: SwitchChannelDispose Method (Boolean)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_switchchannel_dispose_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_switchchannel_dispose_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchChannel.Dispose Method (Boolean)

### SwitchChannelDispose Method (Boolean)

SwitchChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
protected virtual void Dispose(
	bool A_0
)
```

```text
Protected Overridable Sub Dispose ( 
	A_0 As Boolean
)
```

###### Parameters

- **A_0**
  - Type: SystemBoolean

##### Remarks

Cleaning Up Unmanaged Resources

IDisposable

##### See Also

###### Reference

SwitchChannel Class

Dispose Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_switchchannel_tostring.htm language=enus -->
## TOPIC 00417: SwitchChannelToString Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_switchchannel_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_switchchannel_tostring.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchChannel.ToString Method

### SwitchChannelToString Method

Returns a string representation of the object.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

##### See Also

###### Reference

SwitchChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_switchscan_tostring.htm language=enus -->
## TOPIC 00418: SwitchScanToString Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_switchscan_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_switchscan_tostring.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchScan.ToString Method

### SwitchScanToString Method

Returns a string representation of the object.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

##### See Also

###### Reference

SwitchScan Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_tablescale__ctor.htm language=enus -->
## TOPIC 00419: TableScale Constructor

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_tablescale__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_tablescale__ctor.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

TableScale Constructor

### TableScale Constructor

TableScale

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public TableScale(
	string name,
	double[] preScaledValues,
	double[] scaledValues
)
```

```text
Public Sub New ( 
	name As String,
	preScaledValues As Double(),
	scaledValues As Double()
)
```

###### Parameters

- **name**
  - Type: SystemStringThe name of the custom scale for later use, such as when you create a virtual channel.
- **preScaledValues**
  - Type: SystemDoubleAn array of prescaled values that map to the scaled values in scaledValues.
- **scaledValues**
  - Type: SystemDoubleAn array of scaled values that map to the prescaled values in prescaledValues.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

TableScale Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task__ctor.htm language=enus -->
## TOPIC 00420: Task Constructor

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task__ctor.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Task Constructor

### Task Constructor

Task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public Task()
```

```text
Public Sub New
```

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

LoadTask(String)

Local

DaqSystem

##### See Also

###### Reference

Task Class

Task Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task__ctor_1.htm language=enus -->
## TOPIC 00421: Task Constructor (String)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task__ctor_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task__ctor_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Task Constructor (String)

### Task Constructor (String)

Task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public Task(
	string name
)
```

```text
Public Sub New ( 
	name As String
)
```

###### Parameters

- **name**
  - Type: SystemStringThe name of the task to create. If you specify Empty or , the NI-DAQmx driver assigns a unique name to the new task.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

LoadTask(String)

Local

DaqSystem

##### See Also

###### Reference

Task Class

Task Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_addglobalchannel.htm language=enus -->
## TOPIC 00422: TaskAddGlobalChannel Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_addglobalchannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_addglobalchannel.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Task.AddGlobalChannel Method

### TaskAddGlobalChannel Method

Adds a preconfigured, global channel to the task.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public Channel AddGlobalChannel(
	string channelName
)
```

```text
Public Function AddGlobalChannel ( 
	channelName As String
) As Channel
```

###### Parameters

- **channelName**
  - Type: SystemStringThe name of the global channel to add to the task.

###### Return Value

Channel

Channel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

A task can contain global or local channels. Global channels are accessible to all tasks on the system. Local channels are accessible only to the task you use to create them.

Use local channels in a typical application. Use the create channel methods on [AIChannels](p_nationalinstruments_daqmx_task_aichannels.htm),
[AOChannels](p_nationalinstruments_daqmx_task_aochannels.htm), 
[DIChannels](p_nationalinstruments_daqmx_task_dichannels.htm), 
[DOChannels](p_nationalinstruments_daqmx_task_dochannels.htm),
[CIChannels](p_nationalinstruments_daqmx_task_cichannels.htm), or
[COChannels](p_nationalinstruments_daqmx_task_cochannels.htm) to create local channels and add them to the task. 
Use Measurement & Automation Explorer (MAX) to create, configure, and store global channels.

##### See Also

###### Reference

Task Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_configurelogging.htm language=enus -->
## TOPIC 00423: TaskConfigureLogging Method (String, TdmsLoggingOperation, LoggingMode)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_configurelogging.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_configurelogging.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Task.ConfigureLogging Method (String, TdmsLoggingOperation, LoggingMode)

### TaskConfigureLogging Method (String, TdmsLoggingOperation, LoggingMode)

Configures logging to a .tdms file when the acquisition starts.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureLogging(
	string filePath,
	TdmsLoggingOperation loggingOperation,
	LoggingMode loggingMode
)
```

```text
Public Sub ConfigureLogging ( 
	filePath As String,
	loggingOperation As TdmsLoggingOperation,
	loggingMode As LoggingMode
)
```

###### Parameters

- **filePath**
  - Type: SystemStringThe path to the .tdms file to which you want to log data. If you use this method to create a new file, the file extension of the filename you specify in filePath must be .tdms. Otherwise, this method automatically appends .tdms to the filename you specify. If you use this method to open or update an existing file, you do not have to ensure that the file extension is .tdms.
- **loggingOperation**
  - Type: NationalInstruments.DAQmxTdmsLoggingOperationA TdmsLoggingOperation value that specifies how to open the .tdms file.
- **loggingMode**
  - Type: NationalInstruments.DAQmxLoggingModeA LoggingMode value that specifies how to log data.

##### Remarks

TDMS Streaming

##### See Also

###### Reference

Task Class

ConfigureLogging Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_configurelogging_1.htm language=enus -->
## TOPIC 00424: TaskConfigureLogging Method (String, TdmsLoggingOperation, LoggingMode, String)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_configurelogging_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_configurelogging_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Task.ConfigureLogging Method (String, TdmsLoggingOperation, LoggingMode, String)

### TaskConfigureLogging Method (String, TdmsLoggingOperation, LoggingMode, String)

Configures logging to a .tdms file when the acquisition starts with the specified TDMS channel group name.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureLogging(
	string filePath,
	TdmsLoggingOperation loggingOperation,
	LoggingMode loggingMode,
	string groupName
)
```

```text
Public Sub ConfigureLogging ( 
	filePath As String,
	loggingOperation As TdmsLoggingOperation,
	loggingMode As LoggingMode,
	groupName As String
)
```

###### Parameters

- **filePath**
  - Type: SystemStringThe path to the .tdms file to which you want to log data. If you use this method to create a new file, the file extension of the filename you specify in filePath must be .tdms. Otherwise, this method automatically appends .tdms to the filename you specify. If you use this method to open or update an existing file, you do not have to ensure that the file extension is .tdms.
- **loggingOperation**
  - Type: NationalInstruments.DAQmxTdmsLoggingOperationA TdmsLoggingOperation value which specifies how to open the .tdms file.
- **loggingMode**
  - Type: NationalInstruments.DAQmxLoggingModeA LoggingMode value which specifies how to log data.
- **groupName**
  - Type: SystemStringThe name of the channel group to create within the .tdms file for data from this task. When set to , Empty, or a string with only white space, the driver sets the TDMS channel group name to the task name.

##### Remarks

TDMS Streaming

##### See Also

###### Reference

Task Class

ConfigureLogging Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_control.htm language=enus -->
## TOPIC 00425: TaskControl Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_control.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_control.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Task.Control Method

### TaskControl Method

state

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Control(
	TaskAction mode
)
```

```text
Public Sub Control ( 
	mode As TaskAction
)
```

###### Parameters

- **mode**
  - Type: NationalInstruments.DAQmxTaskActionThe action to use to alter the state of the task.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

To start a task more quickly, set mode to [Commit](t_nationalinstruments_daqmx_taskaction.htm) to program the hardware with all parameters of the task prior to starting it.

If the task is in the running state and an asynchronous read or write on the task is in progress, calling Control(TaskAction) to move the task out of the running state does not return until the data from the pending read or write has been transferred to or from the task buffer. However, if mode is [Abort](t_nationalinstruments_daqmx_taskaction.htm), then Control(TaskAction) does not wait for the asynchronous read or write callback methods to finish. The pending asynchronous call stops immediately and raises a [DaqException](t_nationalinstruments_daqmx_daqexception.htm).

##### See Also

###### Reference

Task Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_dispose.htm language=enus -->
## TOPIC 00426: TaskDispose Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_dispose.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_dispose.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Task.Dispose Method

### TaskDispose Method

Task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Dispose()
```

```text
Public Sub Dispose
```

###### Implements

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Task Class

Dispose Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_dispose_1.htm language=enus -->
## TOPIC 00427: TaskDispose Method (Boolean)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_dispose_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_dispose_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Task.Dispose Method (Boolean)

### TaskDispose Method (Boolean)

Task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
protected virtual void Dispose(
	bool A_0
)
```

```text
Protected Overridable Sub Dispose ( 
	A_0 As Boolean
)
```

###### Parameters

- **A_0**
  - Type: SystemBoolean

##### Remarks

Cleaning Up Unmanaged Resources

IDisposable

##### See Also

###### Reference

Task Class

Dispose Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_oncounteroutput.htm language=enus -->
## TOPIC 00428: TaskOnCounterOutput Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_oncounteroutput.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_oncounteroutput.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Task.OnCounterOutput Method

### TaskOnCounterOutput Method

CounterOutput

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
protected virtual void OnCounterOutput(
	CounterOutputEventArgs e
)
```

```text
Protected Overridable Sub OnCounterOutput ( 
	e As CounterOutputEventArgs
)
```

###### Parameters

- **e**
  - Type: NationalInstruments.DAQmxCounterOutputEventArgsA CounterOutputEventArgs that contains the event data.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Task Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_ondigitalchangedetection.htm language=enus -->
## TOPIC 00429: TaskOnDigitalChangeDetection Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_ondigitalchangedetection.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_ondigitalchangedetection.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Task.OnDigitalChangeDetection Method

### TaskOnDigitalChangeDetection Method

DigitalChangeDetection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
protected virtual void OnDigitalChangeDetection(
	DigitalChangeDetectionEventArgs e
)
```

```text
Protected Overridable Sub OnDigitalChangeDetection ( 
	e As DigitalChangeDetectionEventArgs
)
```

###### Parameters

- **e**
  - Type: NationalInstruments.DAQmxDigitalChangeDetectionEventArgsA DigitalChangeDetectionEventArgs that contains the event data.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Task Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_ondone.htm language=enus -->
## TOPIC 00430: TaskOnDone Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_ondone.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_ondone.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Task.OnDone Method

### TaskOnDone Method

Done

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
protected virtual void OnDone(
	TaskDoneEventArgs e
)
```

```text
Protected Overridable Sub OnDone ( 
	e As TaskDoneEventArgs
)
```

###### Parameters

- **e**
  - Type: NationalInstruments.DAQmxTaskDoneEventArgsA TaskDoneEventArgs that contains the event data.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Task Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_oneverynsamplesread.htm language=enus -->
## TOPIC 00431: TaskOnEveryNSamplesRead Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_oneverynsamplesread.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_oneverynsamplesread.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Task.OnEveryNSamplesRead Method

### TaskOnEveryNSamplesRead Method

EveryNSamplesRead

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
protected virtual void OnEveryNSamplesRead(
	EveryNSamplesReadEventArgs e
)
```

```text
Protected Overridable Sub OnEveryNSamplesRead ( 
	e As EveryNSamplesReadEventArgs
)
```

###### Parameters

- **e**
  - Type: NationalInstruments.DAQmxEveryNSamplesReadEventArgsAn EveryNSamplesReadEventArgs that contains the event data.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Task Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_oneverynsampleswritten.htm language=enus -->
## TOPIC 00432: TaskOnEveryNSamplesWritten Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_oneverynsampleswritten.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_oneverynsampleswritten.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Task.OnEveryNSamplesWritten Method

### TaskOnEveryNSamplesWritten Method

EveryNSamplesWritten

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
protected virtual void OnEveryNSamplesWritten(
	EveryNSamplesWrittenEventArgs e
)
```

```text
Protected Overridable Sub OnEveryNSamplesWritten ( 
	e As EveryNSamplesWrittenEventArgs
)
```

###### Parameters

- **e**
  - Type: NationalInstruments.DAQmxEveryNSamplesWrittenEventArgsAn EveryNSamplesWrittenEventArgs that contains the event data.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Task Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_onsampleclock.htm language=enus -->
## TOPIC 00433: TaskOnSampleClock Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_onsampleclock.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_onsampleclock.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Task.OnSampleClock Method

### TaskOnSampleClock Method

SampleClock

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
protected virtual void OnSampleClock(
	SampleClockEventArgs e
)
```

```text
Protected Overridable Sub OnSampleClock ( 
	e As SampleClockEventArgs
)
```

###### Parameters

- **e**
  - Type: NationalInstruments.DAQmxSampleClockEventArgsA SampleClockEventArgs that contains the event data.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Task Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_onsamplecomplete.htm language=enus -->
## TOPIC 00434: TaskOnSampleComplete Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_onsamplecomplete.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_onsamplecomplete.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Task.OnSampleComplete Method

### TaskOnSampleComplete Method

SampleComplete

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
protected virtual void OnSampleComplete(
	SampleCompleteEventArgs e
)
```

```text
Protected Overridable Sub OnSampleComplete ( 
	e As SampleCompleteEventArgs
)
```

###### Parameters

- **e**
  - Type: NationalInstruments.DAQmxSampleCompleteEventArgsA SampleCompleteEventArgs that contains the event data.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Task Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_start.htm language=enus -->
## TOPIC 00435: TaskStart Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_start.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_start.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Task.Start Method

### TaskStart Method

state

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Start()
```

```text
Public Sub Start
```

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

autoStart

When Should You Use the Start Function

##### See Also

###### Reference

Task Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_startnewfile.htm language=enus -->
## TOPIC 00436: TaskStartNewFile Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_startnewfile.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_startnewfile.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Task.StartNewFile Method

### TaskStartNewFile Method

Starts a new TDMS file the next time data is written to disk.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void StartNewFile(
	string filePath
)
```

```text
Public Sub StartNewFile ( 
	filePath As String
)
```

###### Parameters

- **filePath**
  - Type: SystemString The path to the TDMS file to which you want to log data.

##### See Also

###### Reference

Task Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_stop.htm language=enus -->
## TOPIC 00437: TaskStop Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_stop.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_stop.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Task.Stop Method

### TaskStop Method

state

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Stop()
```

```text
Public Sub Stop
```

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

If you do not use this method, the read method ends a measurement task automatically before returning. How you set the autoStart parameter of the write method determines if calling the write method automatically ends a generation task before returning. If you do not use [Start](m_nationalinstruments_daqmx_task_start.htm) and Stop when you use a read or write method multiple times, the task starts and stops repeatedly, which reduces the performance of the application.

If an asynchronous read or write on the task is in progress, Stop does not return until the data from the pending read or write has been transferred to or from the task buffer. Stop does not wait for read or write asynchronous callback methods to finish, however.

You may pass [Abort](t_nationalinstruments_daqmx_taskaction.htm) to the [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) method stop the task immediately, without waiting for any currently running operation to complete.

##### See Also

###### Reference

Task Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_tostring.htm language=enus -->
## TOPIC 00438: TaskToString Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_tostring.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Task.ToString Method

### TaskToString Method

Returns a string representation of the object.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

##### See Also

###### Reference

Task Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_waitforvalidtimestamp.htm language=enus -->
## TOPIC 00439: TaskWaitForValidTimestamp Method (TimestampEvent)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_waitforvalidtimestamp.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_waitforvalidtimestamp.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Task.WaitForValidTimestamp Method (TimestampEvent)

### TaskWaitForValidTimestamp Method (TimestampEvent)

timestampEvent

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public PrecisionDateTime WaitForValidTimestamp(
	TimestampEvent timestampEvent
)
```

```text
Public Function WaitForValidTimestamp ( 
	timestampEvent As TimestampEvent
) As PrecisionDateTime
```

###### Parameters

- **timestampEvent**
  - Type: NationalInstruments.DAQmxTimestampEventSpecifies the timestamp event type to wait on. For more information see TimestampEvent.

###### Return Value

PrecisionDateTime

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

To use this method, you must first enable timestamps for the timestamp event type specified by timestampEvent. The following code demonstrates how to do this for [StartTrigger](t_nationalinstruments_daqmx_timestampevent.htm).

##### Examples

C#

```text
// Using an instance of Task called 'myTask'.
myTask.Triggers.StartTrigger.TimestampEnable = true;
myTask.Start();
myTimestamp = myTask.WaitForValidTimestamp(TimestampEvent.StartTrigger);
```

##### Examples

VB

```text
' Using an instance of Task called 'myTask'.
myTask.Triggers.StartTrigger.TimestampEnable = True
myTask.Start()
myTimestamp = myTask.WaitForValidTimestamp(TimestampEvent.StartTrigger)
```

##### See Also

###### Reference

Task Class

WaitForValidTimestamp Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_waituntildone.htm language=enus -->
## TOPIC 00440: TaskWaitUntilDone Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_waituntildone.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_waituntildone.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Task.WaitUntilDone Method

### TaskWaitUntilDone Method

Waits for the measurement or generation to complete, regardless of the amount of time needed, and returns if it has completed execution.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void WaitUntilDone()
```

```text
Public Sub WaitUntilDone
```

###### Return Value

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Timing

IAsyncResult

##### See Also

###### Reference

Task Class

WaitUntilDone Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_waituntildone_1.htm language=enus -->
## TOPIC 00441: TaskWaitUntilDone Method (Int32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_waituntildone_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_waituntildone_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Task.WaitUntilDone Method (Int32)

### TaskWaitUntilDone Method (Int32)

Waits for the measurement or generation to complete and returns if it has completed execution before the specified time elapses.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void WaitUntilDone(
	int millisecToWait
)
```

```text
Public Sub WaitUntilDone ( 
	millisecToWait As Integer
)
```

###### Parameters

- **millisecToWait**
  - Type: SystemInt32The maximum amount of time in milliseconds to wait for the measurement or generation to complete. This method returns an error if the time elapses. If you set the timeout to -1, the method always waits for the task to complete, regardless of the amount of time needed.

###### Return Value

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

WaitUntilDone(Int32)

Timing

WaitUntilDone(Int32)

IAsyncResult

##### See Also

###### Reference

Task Class

WaitUntilDone Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_waituntildone_2.htm language=enus -->
## TOPIC 00442: TaskWaitUntilDone Method (TimeSpan)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_waituntildone_2.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_task_waituntildone_2.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Task.WaitUntilDone Method (TimeSpan)

### TaskWaitUntilDone Method (TimeSpan)

TimeSpan

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void WaitUntilDone(
	TimeSpan timeout
)
```

```text
Public Sub WaitUntilDone ( 
	timeout As TimeSpan
)
```

###### Parameters

- **timeout**
  - Type: SystemTimeSpan The maximum TimeSpan to wait for the measurement or generation to complete. This method returns an error if the time elapses.

###### Return Value

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

WaitUntilDone(TimeSpan)

Timing

WaitUntilDone(TimeSpan)

IAsyncResult

##### See Also

###### Reference

Task Class

WaitUntilDone Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_taskdoneeventargs_checkforexception.htm language=enus -->
## TOPIC 00443: TaskDoneEventArgsCheckForException Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_taskdoneeventargs_checkforexception.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_taskdoneeventargs_checkforexception.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

TaskDoneEventArgs.CheckForException Method

### TaskDoneEventArgsCheckForException Method

Exception

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void CheckForException()
```

```text
Public Sub CheckForException
```

##### Remarks

Exception

Error

##### See Also

###### Reference

TaskDoneEventArgs Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_taskdoneeventargs_getobjectdata.htm language=enus -->
## TOPIC 00444: TaskDoneEventArgsGetObjectData Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_taskdoneeventargs_getobjectdata.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_taskdoneeventargs_getobjectdata.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

TaskDoneEventArgs.GetObjectData Method

### TaskDoneEventArgsGetObjectData Method

SerializationInfo

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
protected virtual void GetObjectData(
	SerializationInfo info,
	StreamingContext context
)
```

```text
Protected Overridable Sub GetObjectData ( 
	info As SerializationInfo,
	context As StreamingContext
)
```

###### Parameters

- **info**
  - Type: System.Runtime.SerializationSerializationInfo Object that holds the serialized object data.
- **context**
  - Type: System.Runtime.SerializationStreamingContext Contextual information about the source or destination.

##### See Also

###### Reference

TaskDoneEventArgs Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_timearmstarttrigger_tostring.htm language=enus -->
## TOPIC 00445: TimeArmStartTriggerToString Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_timearmstarttrigger_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_timearmstarttrigger_tostring.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

TimeArmStartTrigger.ToString Method

### TimeArmStartTriggerToString Method

Returns a string representation of the object.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### See Also

###### Reference

TimeArmStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_timestarttrigger_tostring.htm language=enus -->
## TOPIC 00446: TimeStartTriggerToString Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_timestarttrigger_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_timestarttrigger_tostring.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

TimeStartTrigger.ToString Method

### TimeStartTriggerToString Method

Returns a string representation of the object.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### See Also

###### Reference

TimeStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_timing_configurechangedetection_1.htm language=enus -->
## TOPIC 00447: TimingConfigureChangeDetection Method (String, String, SampleQuantityMode, Int32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_timing_configurechangedetection_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_timing_configurechangedetection_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.ConfigureChangeDetection Method (String, String, SampleQuantityMode, Int32)

### TimingConfigureChangeDetection Method (String, String, SampleQuantityMode, Int32)

Configures the task to acquire samples on the rising and/or falling edges of the specified lines or ports and sets the number of samples to acquire.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureChangeDetection(
	string diRisingEdgePhysicalChannels,
	string diFallingEdgePhysicalChannels,
	SampleQuantityMode sampleMode,
	int samplesPerChannel
)
```

```text
Public Sub ConfigureChangeDetection ( 
	diRisingEdgePhysicalChannels As String,
	diFallingEdgePhysicalChannels As String,
	sampleMode As SampleQuantityMode,
	samplesPerChannel As Integer
)
```

###### Parameters

- **diRisingEdgePhysicalChannels**
  - Type: SystemStringThe names of the digital lines or ports on which to detect rising edges. The lines or ports must be contained in the task. You can specify a string that defines a list or range of channels for this parameter.
- **diFallingEdgePhysicalChannels**
  - Type: SystemStringThe names of the digital lines or ports on which to detect falling edges. The lines or ports must be contained in the task. You can specify a string that defines a list or range of channels for this parameter.
- **sampleMode**
  - Type: NationalInstruments.DAQmxSampleQuantityModeThe duration of the task. A task is either finite and stops when the specified number of samples have been acquired, or it is continuous and continues to acquire samples until the task is explicitly stopped.
- **samplesPerChannel**
  - Type: SystemInt32The number of samples to acquire from each channel in the task if sampleMode is FiniteSamples. If sampleMode is ContinuousSamples, NI-DAQmx uses this value to determine the buffer size.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

change detection timing

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

You cannot apply this method to a subset of devices in the task, and you must apply this method to the task as a whole. You must call this method on the instance of [Timing](t_nationalinstruments_daqmx_timing.htm) returned from the [Timing](p_nationalinstruments_daqmx_task_timing.htm) property on the [Task](t_nationalinstruments_daqmx_task.htm) class. Accessing this method on instances of [Timing](t_nationalinstruments_daqmx_timing.htm) returned from the [ItemString](p_nationalinstruments_daqmx_timing_item.htm) property throws an exception.

##### See Also

###### Reference

Timing Class

ConfigureChangeDetection Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_timing_configurehandshaking.htm language=enus -->
## TOPIC 00448: TimingConfigureHandshaking Method (SampleQuantityMode)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_timing_configurehandshaking.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_timing_configurehandshaking.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.ConfigureHandshaking Method (SampleQuantityMode)

### TimingConfigureHandshaking Method (SampleQuantityMode)

digital handshaking

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureHandshaking(
	SampleQuantityMode sampleMode
)
```

```text
Public Sub ConfigureHandshaking ( 
	sampleMode As SampleQuantityMode
)
```

###### Parameters

- **sampleMode**
  - Type: NationalInstruments.DAQmxSampleQuantityModeThe duration of the task. A task is either finite and stops once the specified number of samples has been acquired or generated, or it is continuous and continues to acquire or generate samples until the task is explicitly stopped.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Use this method for continuous operations. These [devices](/csh?topicname=mxdevconsid/;) support handshake timing.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

You cannot apply this method to a subset of devices in the task, and you must apply this method to the task as a whole. You must call this method on the instance of [Timing](t_nationalinstruments_daqmx_timing.htm) returned from the [Timing](p_nationalinstruments_daqmx_task_timing.htm) property on the [Task](t_nationalinstruments_daqmx_task.htm) class. Accessing this method on instances of [Timing](t_nationalinstruments_daqmx_timing.htm) returned from the [ItemString](p_nationalinstruments_daqmx_timing_item.htm) property throws an exception.

##### See Also

###### Reference

Timing Class

ConfigureHandshaking Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_timing_configureimplicit.htm language=enus -->
## TOPIC 00449: TimingConfigureImplicit Method (SampleQuantityMode)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_timing_configureimplicit.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_timing_configureimplicit.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.ConfigureImplicit Method (SampleQuantityMode)

### TimingConfigureImplicit Method (SampleQuantityMode)

Sets only the duration of the task without specifying timing.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureImplicit(
	SampleQuantityMode sampleMode
)
```

```text
Public Sub ConfigureImplicit ( 
	sampleMode As SampleQuantityMode
)
```

###### Parameters

- **sampleMode**
  - Type: NationalInstruments.DAQmxSampleQuantityModeThe duration of the task. A task is either finite and stops once the specified number of samples have been acquired or generated, or it is continuous and continues to acquire or generate samples until the task is explicitly stopped.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Typically, you use [implicit timing](/csh?topicname=mxcncpts/;) when sample timing is not required for the task, such as for a task that uses counters for buffered frequency measurement, buffered period measurement, or pulse train generation. Use this method for continuous operations.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

You cannot apply this method to a subset of devices in the task, and you must apply this method to the task as a whole. You must call this method on the instance of [Timing](t_nationalinstruments_daqmx_timing.htm) returned from the [Timing](p_nationalinstruments_daqmx_task_timing.htm) property on the [Task](t_nationalinstruments_daqmx_task.htm) class. Accessing this method on instances of [Timing](t_nationalinstruments_daqmx_timing.htm) returned from the [ItemString](p_nationalinstruments_daqmx_timing_item.htm) property throws an exception.

##### See Also

###### Reference

Timing Class

ConfigureImplicit Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_timing_configuresampleclock.htm language=enus -->
## TOPIC 00450: TimingConfigureSampleClock Method (String, Double, SampleClockActiveEdge, SampleQuantityMode)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_timing_configuresampleclock.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_timing_configuresampleclock.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.ConfigureSampleClock Method (String, Double, SampleClockActiveEdge, SampleQuantityMode)

### TimingConfigureSampleClock Method (String, Double, SampleClockActiveEdge, SampleQuantityMode)

sample clock

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureSampleClock(
	string signalSource,
	double rate,
	SampleClockActiveEdge activeEdge,
	SampleQuantityMode sampleMode
)
```

```text
Public Sub ConfigureSampleClock ( 
	signalSource As String,
	rate As Double,
	activeEdge As SampleClockActiveEdge,
	sampleMode As SampleQuantityMode
)
```

###### Parameters

- **signalSource**
  - Type: SystemStringThe source terminal of the clock. To use the internal clock of the device, set this value to Empty.
- **rate**
  - Type: SystemDoubleThe sampling rate in samples per second. If you use an external source for the sample clock, set this input to the maximum expected rate of that clock.
- **activeEdge**
  - Type: NationalInstruments.DAQmxSampleClockActiveEdgeThe edges of sample clock pulses on which to acquire or generate samples.
- **sampleMode**
  - Type: NationalInstruments.DAQmxSampleQuantityModeThe duration of the task. A task is either finite and stops once the specified number of samples have been acquired or generated, or it is continuous and continues to acquire or generate samples until the task is explicitly stopped.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Task

Control(TaskAction)

Verify

You cannot apply this method to a subset of devices in the task, and you must apply this method to the task as a whole. You must call this method on the instance of [Timing](t_nationalinstruments_daqmx_timing.htm) returned from the [Timing](p_nationalinstruments_daqmx_task_timing.htm) property on the [Task](t_nationalinstruments_daqmx_task.htm) class. Accessing this method on instances of [Timing](t_nationalinstruments_daqmx_timing.htm) returned from the [ItemString](p_nationalinstruments_daqmx_timing_item.htm) property throws an exception.

| Note |
| --- |
| Before calling this method, you must configure channels on the task using one of the channel collection properties (for example, CreateVoltageChannel(String, String, AITerminalConfiguration, Double, Double, String) on AIChannels). |

##### See Also

###### Reference

Timing Class

ConfigureSampleClock Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_timing_configuresampleclock_1.htm language=enus -->
## TOPIC 00451: TimingConfigureSampleClock Method (String, Double, SampleClockActiveEdge, SampleQuantityMode, Int32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_timing_configuresampleclock_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_timing_configuresampleclock_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.ConfigureSampleClock Method (String, Double, SampleClockActiveEdge, SampleQuantityMode, Int32)

### TimingConfigureSampleClock Method (String, Double, SampleClockActiveEdge, SampleQuantityMode, Int32)

sample clock

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureSampleClock(
	string signalSource,
	double rate,
	SampleClockActiveEdge activeEdge,
	SampleQuantityMode sampleMode,
	int samplesPerChannel
)
```

```text
Public Sub ConfigureSampleClock ( 
	signalSource As String,
	rate As Double,
	activeEdge As SampleClockActiveEdge,
	sampleMode As SampleQuantityMode,
	samplesPerChannel As Integer
)
```

###### Parameters

- **signalSource**
  - Type: SystemStringThe source terminal of the clock. To use the internal clock of the device, set this value to Empty.
- **rate**
  - Type: SystemDoubleThe sampling rate in samples per second. If you use an external source for the sample clock, set this input to the maximum expected rate of that clock.
- **activeEdge**
  - Type: NationalInstruments.DAQmxSampleClockActiveEdgeThe edges of sample clock pulses on which to acquire or generate samples.
- **sampleMode**
  - Type: NationalInstruments.DAQmxSampleQuantityModeThe duration of the task. A task is either finite and stops once the specified number of samples have been acquired or generated, or it is continuous and continues to acquire or generate samples until the task is explicitly stopped.
- **samplesPerChannel**
  - Type: SystemInt32The number of samples to acquire or generate if sampleMode is FiniteSamples. If sample mode is ContinuousSamples, NI-DAQmx uses this value to determine the buffer size.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Task

Control(TaskAction)

Verify

You cannot apply this method to a subset of devices in the task, and you must apply this method to the task as a whole. You must call this method on the instance of [Timing](t_nationalinstruments_daqmx_timing.htm) returned from the [Timing](p_nationalinstruments_daqmx_task_timing.htm) property on the [Task](t_nationalinstruments_daqmx_task.htm) class. Accessing this method on instances of [Timing](t_nationalinstruments_daqmx_timing.htm) returned from the [ItemString](p_nationalinstruments_daqmx_timing_item.htm) property throws an exception.

| Note |
| --- |
| Before calling this method, you must configure channels on the task using one of the channel collection properties (for example, CreateVoltageChannel(String, String, AITerminalConfiguration, Double, Double, String) on AIChannels). |

##### See Also

###### Reference

Timing Class

ConfigureSampleClock Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_triggers_tostring.htm language=enus -->
## TOPIC 00452: TriggersToString Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_triggers_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_triggers_tostring.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Triggers.ToString Method

### TriggersToString Method

Returns a string representation of the object.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

##### See Also

###### Reference

Triggers Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_watchdog_clearexpiration.htm language=enus -->
## TOPIC 00453: WatchdogClearExpiration Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_watchdog_clearexpiration.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_watchdog_clearexpiration.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Watchdog.ClearExpiration Method

### WatchdogClearExpiration Method

watchdog timer

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ClearExpiration()
```

```text
Public Sub ClearExpiration
```

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Watchdog Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_watchdog_getaoexpirationstate.htm language=enus -->
## TOPIC 00454: WatchdogGetAOExpirationState Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_watchdog_getaoexpirationstate.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_watchdog_getaoexpirationstate.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Watchdog.GetAOExpirationState Method

### WatchdogGetAOExpirationState Method

Specifies the state to set the analog output physical channels when the watchdog task expires.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double GetAOExpirationState(
	string physicalChannelName
)
```

```text
Public Function GetAOExpirationState ( 
	physicalChannelName As String
) As Double
```

###### Parameters

- **physicalChannelName**
  - Type: SystemStringThe physical channel name for which to retrieve the setting.

###### Return Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Watchdog Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_watchdog_setaoexpirationstate.htm language=enus -->
## TOPIC 00455: WatchdogSetAOExpirationState Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_watchdog_setaoexpirationstate.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_watchdog_setaoexpirationstate.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Watchdog.SetAOExpirationState Method

### WatchdogSetAOExpirationState Method

Specifies the state to set the analog output physical channels when the watchdog task expires.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void SetAOExpirationState(
	string physicalChannelName,
	double value
)
```

```text
Public Sub SetAOExpirationState ( 
	physicalChannelName As String,
	value As Double
)
```

###### Parameters

- **physicalChannelName**
  - Type: SystemStringThe physical channel name to which to apply value.
- **value**
  - Type: SystemDoubleThe setting to apply to the given physical channel.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Watchdog Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_watchdog_tostring.htm language=enus -->
## TOPIC 00456: WatchdogToString Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_watchdog_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_watchdog_tostring.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Watchdog.ToString Method

### WatchdogToString Method

Returns a string representation of the object.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

##### See Also

###### Reference

Watchdog Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_watchdogexpirationtrigger_configuredigitaledgetrigger.htm language=enus -->
## TOPIC 00457: WatchdogExpirationTriggerConfigureDigitalEdgeTrigger Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_watchdogexpirationtrigger_configuredigitaledgetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_watchdogexpirationtrigger_configuredigitaledgetrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

WatchdogExpirationTrigger.ConfigureDigitalEdgeTrigger Method

### WatchdogExpirationTriggerConfigureDigitalEdgeTrigger Method

watchdog timer

rising or falling edge of a digital signal

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureDigitalEdgeTrigger(
	string source,
	DigitalEdgeWatchdogExpirationTriggerEdge edge
)
```

```text
Public Sub ConfigureDigitalEdgeTrigger ( 
	source As String,
	edge As DigitalEdgeWatchdogExpirationTriggerEdge
)
```

###### Parameters

- **source**
  - Type: SystemStringThe terminal of the trigger signal.
- **edge**
  - Type: NationalInstruments.DAQmxDigitalEdgeWatchdogExpirationTriggerEdgeThe edge of the trigger signal that causes a watchdog expiration trigger to occur.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

ConfigureDigitalEdgeTrigger(String, DigitalEdgeWatchdogExpirationTriggerEdge)

Task

Control(TaskAction)

Verify

##### See Also

###### Reference

WatchdogExpirationTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_watchdogexpirationtrigger_configurenone.htm language=enus -->
## TOPIC 00458: WatchdogExpirationTriggerConfigureNone Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_watchdogexpirationtrigger_configurenone.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_watchdogexpirationtrigger_configurenone.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

WatchdogExpirationTrigger.ConfigureNone Method

### WatchdogExpirationTriggerConfigureNone Method

watchdog expiration triggering

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureNone()
```

```text
Public Sub ConfigureNone
```

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Task

Control(TaskAction)

Verify

##### See Also

###### Reference

WatchdogExpirationTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_watchdogexpirationtrigger_tostring.htm language=enus -->
## TOPIC 00459: WatchdogExpirationTriggerToString Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_watchdogexpirationtrigger_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_watchdogexpirationtrigger_tostring.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

WatchdogExpirationTrigger.ToString Method

### WatchdogExpirationTriggerToString Method

Returns a string representation of the object.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

##### See Also

###### Reference

WatchdogExpirationTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_advancetrigger.htm language=enus -->
## TOPIC 00460: AdvanceTrigger Methods

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_advancetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_advancetrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AdvanceTrigger Methods

### AdvanceTrigger Methods

The [AdvanceTrigger](t_nationalinstruments_daqmx_advancetrigger.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureDigitalEdgeTrigger | Configures a task to advance to the next entry in a scan list upon a rising or falling edge of a digital signal. |
|  | ConfigureNone | Disables advance triggering for the task. |
|  | ConfigureSoftwareTrigger | Configures a task to advance to the next entry in a scan list upon a software trigger. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | SendSoftwareTrigger | Sends a notification to the hardware from the running program to advance to the next entry in the switch scan list. |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### See Also

###### Reference

AdvanceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_analogsinglechannelreader.htm language=enus -->
## TOPIC 00461: AnalogSingleChannelReader Methods

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_analogsinglechannelreader.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_analogsinglechannelreader.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogSingleChannelReader Methods

### AnalogSingleChannelReader Methods

The [AnalogSingleChannelReader](t_nationalinstruments_daqmx_analogsinglechannelreader.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | BeginMemoryOptimizedReadMultiSample(Int32, AsyncCallback, Object, Double) | Begins an asynchronous read of one or more floating-point samples from a single AIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSample(Int32, AsyncCallback, Object, Double, ReallocationPolicy) | Begins an asynchronous read of one or more floating-point samples from a single AIChannel in a task. |
|  | BeginMemoryOptimizedReadWaveform(Int32, AsyncCallback, Object, AnalogWaveformDouble) | Begins an asynchronous read of one or more analog waveform samples from a single AIChannel in a task. |
|  | BeginMemoryOptimizedReadWaveform(TimeSpan, AsyncCallback, Object, AnalogWaveformDouble) | Begins an asynchronous, memory-optimized read of one or more analog waveform samples from a single AIChannel object in a task for a specified duration. |
|  | BeginMemoryOptimizedReadWaveform(Int32, AsyncCallback, Object, AnalogWaveformDouble, ReallocationPolicy) | Begins an asynchronous read of one or more analog waveform samples from a single AIChannel in a task. |
|  | BeginMemoryOptimizedReadWaveform(TimeSpan, AsyncCallback, Object, AnalogWaveformDouble, ReallocationPolicy) | Begins an asynchronous, memory-optimized read of one or more analog waveform samples from a single AIChannel object in a task for a specified duration. |
|  | BeginReadMultiSample | Begins an asynchronous read of one or more floating-point samples from a single AIChannel in a task. |
|  | BeginReadSingleSample | Begins an asynchronous read of a single floating-point sample from a single AIChannel in a task. |
|  | BeginReadWaveform(Int32, AsyncCallback, Object) | Begins an asynchronous read of one or more analog waveform samples from a single AIChannel in a task. |
|  | BeginReadWaveform(TimeSpan, AsyncCallback, Object) | Begins an asynchronous read of one or more analog waveform samples from a single AIChannel object in a task for a specified duration. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | EndMemoryOptimizedReadMultiSample | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSample(Int32, AsyncCallback, Object, Double) and retrieves the read samples. |
|  | EndMemoryOptimizedReadWaveform | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadWaveform(Int32, AsyncCallback, Object, AnalogWaveformDouble) and retrieves the read samples. |
|  | EndReadMultiSample | Handles the end of an asynchronous read initiated with BeginReadMultiSample(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSample | Handles the end of an asynchronous read initiated with BeginReadSingleSample(AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadWaveform | Handles the end of an asynchronous read initiated with BeginReadWaveform(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | MemoryOptimizedReadMultiSample(Int32, Double, Int32) | Reads one or more floating-point samples from a single AIChannel in a task. |
|  | MemoryOptimizedReadMultiSample(Int32, Double, ReallocationPolicy, Int32) | Reads one or more floating-point samples from a single AIChannel in a task. |
|  | MemoryOptimizedReadWaveform(Int32, AnalogWaveformDouble) | Reads one or more analog waveform samples from a single AIChannel in a task. |
|  | MemoryOptimizedReadWaveform(TimeSpan, AnalogWaveformDouble) | Performs a memory-optimized read of one or more analog waveform samples from a single AIChannel object in a task for a specified duration. |
|  | MemoryOptimizedReadWaveform(Int32, AnalogWaveformDouble, ReallocationPolicy) | Reads one or more analog waveform samples from a singleAIChannelin a task. |
|  | MemoryOptimizedReadWaveform(TimeSpan, AnalogWaveformDouble, ReallocationPolicy) | Performs a memory-optimized read of one or more analog waveform samples from a single AIChannel object in a task for a specified duration. |
|  | ReadMultiSample | Reads one or more floating-point samples from a single AIChannel in a task. |
|  | ReadSingleSample | Reads a single floating-point sample from a single AIChannel in a task. |
|  | ReadWaveform(Int32) | Reads one or more analog waveform samples from a single AIChannel in a task. |
|  | ReadWaveform(TimeSpan) | Reads one or more analog waveform samples from a single AIChannel object in a task for a specified duration. |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### See Also

###### Reference

AnalogSingleChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_analogsinglechannelwriter.htm language=enus -->
## TOPIC 00462: AnalogSingleChannelWriter Methods

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_analogsinglechannelwriter.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_analogsinglechannelwriter.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogSingleChannelWriter Methods

### AnalogSingleChannelWriter Methods

The [AnalogSingleChannelWriter](t_nationalinstruments_daqmx_analogsinglechannelwriter.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | BeginWriteMultiSample | Begins an asynchronous write of one or more floating-point samples to a single AOChannel in a task. |
|  | BeginWriteSingleSample | Begins an asynchronous write of a floating-point sample to a single AOChannel in a task. |
|  | BeginWriteWaveformTData | Writes one or more analog waveform samples to a single AOChannel in a task. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | EndWrite | Handles the end of an asynchronous write initiated with BeginWriteMultiSample(Boolean, Double, AsyncCallback, Object) or BeginWriteSingleSample(Boolean, Double, AsyncCallback, Object). |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |
|  | WriteMultiSample | Writes one or more floating-point samples to a single AOChannel in a task. |
|  | WriteSingleSample | Writes a floating-point sample to a single AOChannel in a task. |
|  | WriteWaveformTData | Writes one or more analog waveform samples to a single AOChannel in a task. |

Top

##### See Also

###### Reference

AnalogSingleChannelWriter Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_analogunscaledreader.htm language=enus -->
## TOPIC 00463: AnalogUnscaledReader Methods

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_analogunscaledreader.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_analogunscaledreader.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogUnscaledReader Methods

### AnalogUnscaledReader Methods

The [AnalogUnscaledReader](t_nationalinstruments_daqmx_analogunscaledreader.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | BeginReadInt16 | Begins an asynchronous read of one or more unscaled 16-bit integer samples from one or more AIChannel objects in a task. |
|  | BeginReadInt32 | Begins an asynchronous read of one or more unscaled 32-bit integer samples from one or more AIChannel objects in a task. |
|  | BeginReadUInt16 | Begins an asynchronous read of one or more unscaled 16-bit unsigned integer samples from one or more AIChannel objects in a task. |
|  | BeginReadUInt32 | Begins an asynchronous read of one or more unscaled 32-bit unsigned integer samples from one or more AIChannel objects in a task. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | EndReadInt16 | Handles the end of an asynchronous read initiated with BeginReadInt16(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadInt32 | Handles the end of an asynchronous read initiated with BeginReadInt32(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadUInt16 | Handles the end of an asynchronous read initiated with BeginReadUInt16(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadUInt32 | Handles the end of an asynchronous read initiated with BeginReadUInt32(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ReadInt16 | Reads one or more unscaled 16-bit integer samples from one or more AIChannel objects in a task. |
|  | ReadInt32 | Reads one or more unscaled 32-bit integer samples from one or more AIChannel objects in a task. |
|  | ReadUInt16 | Reads one or more unscaled 16-bit unsigned integer samples from one or more AIChannel objects in a task. |
|  | ReadUInt32 | Reads one or more unscaled 32-bit unsigned integer samples from one or more AIChannel objects in a task. |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### See Also

###### Reference

AnalogUnscaledReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_analogwindowstarttrigger.htm language=enus -->
## TOPIC 00464: AnalogWindowStartTrigger Methods

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_analogwindowstarttrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_analogwindowstarttrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogWindowStartTrigger Methods

### AnalogWindowStartTrigger Methods

The [AnalogWindowStartTrigger](t_nationalinstruments_daqmx_analogwindowstarttrigger.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### See Also

###### Reference

AnalogWindowStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_aochannel.htm language=enus -->
## TOPIC 00465: AOChannel Methods

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_aochannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_aochannel.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AOChannel Methods

### AOChannel Methods

The [AOChannel](t_nationalinstruments_daqmx_aochannel.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Dispose | Releases all resources used by Channel. (Inherited from Channel.) |
|  | Dispose(Boolean) | Releases the managed and unmanaged resources used by Channel or optionally releases only the unmanaged resources. (Inherited from Channel.) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Inherited from Channel.) |

Top

##### See Also

###### Reference

AOChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_codatatime.htm language=enus -->
## TOPIC 00466: CODataTime Methods

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_codatatime.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_codatatime.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CODataTime Methods

### CODataTime Methods

The [CODataTime](t_nationalinstruments_daqmx_codatatime.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals(Object) | Returns a value indicating if this instance is equal to the specified object. (Overrides ValueTypeEquals(Object).) |
|  | Equals(CODataTime) | Returns a value indicating if this instance is equal to the specified CODataTime object. |
|  | Equals(CODataTime, CODataTime) | Returns a value indicating if two specified instances of CODataTime are equal. |
|  | GetHashCode | Returns a hash code for the CODataTime object. (Overrides ValueTypeGetHashCode.) |
|  | GetObjectData | Sets the SerializationInfo object with information about the exception. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns the fully qualified type name of this instance. (Inherited from ValueType.) |

Top

##### See Also

###### Reference

CODataTime Structure

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_countermultichannelreader.htm language=enus -->
## TOPIC 00467: CounterMultiChannelReader Methods

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_countermultichannelreader.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_countermultichannelreader.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterMultiChannelReader Methods

### CounterMultiChannelReader Methods

The [CounterMultiChannelReader](t_nationalinstruments_daqmx_countermultichannelreader.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | BeginMemoryOptimizedReadMultiSampleDouble(Int32, AsyncCallback, Object, Double) | Begins an asynchronous read of one or more Double samples from one or more CIChannel objects in a task. |
|  | BeginMemoryOptimizedReadMultiSampleDouble(Int32, AsyncCallback, Object, Double, ReallocationPolicy) | Begins an asynchronous read of one or more Double samples from one or more CIChannel objects in a task. |
|  | BeginMemoryOptimizedReadMultiSampleInt32(Int32, AsyncCallback, Object, Int32) | Begins an asynchronous read of one or more Int32 samples from one or more CIChannel objects in a task. |
|  | BeginMemoryOptimizedReadMultiSampleInt32(Int32, AsyncCallback, Object, Int32, ReallocationPolicy) | Begins an asynchronous read of one or more Int32 samples from one or more CIChannel objects in a task. |
|  | BeginMemoryOptimizedReadMultiSampleUInt32(Int32, AsyncCallback, Object, UInt32) | Begins an asynchronous read of one or more UInt32 samples from one or more CIChannel objects in a task. |
|  | BeginMemoryOptimizedReadMultiSampleUInt32(Int32, AsyncCallback, Object, UInt32, ReallocationPolicy) | Begins an asynchronous read of one or more UInt32 samples from one or more CIChannel objects in a task. |
|  | BeginReadMultiSampleDouble | Begins an asynchronous read of one or more Double samples from one or more CIChannel objects in a task. |
|  | BeginReadMultiSampleInt32 | Begins an asynchronous read of one or more Int32 samples from one or more CIChannel objects in a task. |
|  | BeginReadMultiSampleUInt32 | Begins an asynchronous read of one or more UInt32 samples from one or more CIChannel objects in a task. |
|  | BeginReadSingleSampleDouble | Begins an asynchronous read of a single Double sample from one or more CIChannel objects in a task. |
|  | BeginReadSingleSampleInt32 | Begins an asynchronous read of a single Int32 sample from one or more CIChannel objects in a task. |
|  | BeginReadSingleSampleUInt32 | Begins an asynchronous read of a single UInt32 sample from one or more CIChannel objects in a task. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | EndMemoryOptimizedReadMultiSampleDouble | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSampleDouble(Int32, AsyncCallback, Object, Double) and retrieves the read samples. |
|  | EndMemoryOptimizedReadMultiSampleInt32 | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSampleInt32(Int32, AsyncCallback, Object, Int32) and retrieves the read samples. |
|  | EndMemoryOptimizedReadMultiSampleUInt32 | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSampleUInt32(Int32, AsyncCallback, Object, UInt32) and retrieves the read samples. |
|  | EndReadMultiSampleDouble | Handles the end of an asynchronous read initiated with BeginReadMultiSampleDouble(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadMultiSampleInt32 | Handles the end of an asynchronous read initiated with BeginReadMultiSampleInt32(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadMultiSampleUInt32 | Handles the end of an asynchronous read initiated with BeginReadMultiSampleUInt32(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSampleDouble | Handles the end of an asynchronous read initiated with BeginReadSingleSampleDouble(AsyncCallback, Object) and retrieves the read sample. |
|  | EndReadSingleSampleInt32 | Handles the end of an asynchronous read initiated with BeginReadSingleSampleInt32(AsyncCallback, Object) and retrieves the read sample. |
|  | EndReadSingleSampleUInt32 | Handles the end of an asynchronous read initiated with BeginReadSingleSampleUInt32(AsyncCallback, Object) and retrieves the read sample. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | MemoryOptimizedReadMultiSampleDouble(Int32, Double, Int32) | Reads one or more Double samples from one or more CIChannel objects in a task. |
|  | MemoryOptimizedReadMultiSampleDouble(Int32, Double, ReallocationPolicy, Int32) | Reads one or more Double samples from one or more CIChannel objects in a task. |
|  | MemoryOptimizedReadMultiSampleInt32(Int32, Int32, Int32) | Reads one or more Int32 samples from one or more CIChannel objects in a task. |
|  | MemoryOptimizedReadMultiSampleInt32(Int32, Int32, ReallocationPolicy, Int32) | Reads one or more Int32 samples from one or more CIChannel objects in a task. |
|  | MemoryOptimizedReadMultiSampleUInt32(Int32, UInt32, Int32) | Reads one or more UInt32 samples from one or more CIChannel objects in a task. |
|  | MemoryOptimizedReadMultiSampleUInt32(Int32, UInt32, ReallocationPolicy, Int32) | Reads one or more UInt32 samples from one or more CIChannel objects in a task. |
|  | ReadMultiSampleDouble | Reads one or more Double samples from one or more CIChannel objects in a task. |
|  | ReadMultiSampleInt32 | Reads one or more Int32 samples from one or more CIChannel objects in a task. |
|  | ReadMultiSampleUInt32 | Reads one or more UInt32 samples from one or more CIChannel objects in a task. |
|  | ReadSingleSampleDouble | Reads a single Double sample from one or more CIChannel objects in a task. |
|  | ReadSingleSampleInt32 | Reads a single Int32 sample from one or more CIChannel objects in a task. |
|  | ReadSingleSampleUInt32 | Reads a single UInt32 sample from one or more CIChannel objects in a task. |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### See Also

###### Reference

CounterMultiChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_countersinglechannelwriter.htm language=enus -->
## TOPIC 00468: CounterSingleChannelWriter Methods

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_countersinglechannelwriter.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_countersinglechannelwriter.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelWriter Methods

### CounterSingleChannelWriter Methods

The [CounterSingleChannelWriter](t_nationalinstruments_daqmx_countersinglechannelwriter.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | BeginWriteMultiSample(Boolean, CODataFrequency, AsyncCallback, Object) | Begins an asynchronous write of one or more frequency samples to a single COChannel in a counter output task. |
|  | BeginWriteMultiSample(Boolean, CODataTicks, AsyncCallback, Object) | Begins an asynchronous write of one or more ticks samples to a single COChannel in a counter output task. |
|  | BeginWriteMultiSample(Boolean, CODataTime, AsyncCallback, Object) | Begins an asynchronous write of one or more time samples to a single COChannel in a counter output task. |
|  | BeginWriteSingleSample(Boolean, CODataFrequency, AsyncCallback, Object) | Begins an asynchronous write of a frequency sample to a single COChannel in a counter output task. |
|  | BeginWriteSingleSample(Boolean, CODataTicks, AsyncCallback, Object) | Begins an asynchronous write of a ticks sample to a single COChannel in a counter output task. |
|  | BeginWriteSingleSample(Boolean, CODataTime, AsyncCallback, Object) | Begins an asynchronous write of a time sample to a single COChannel in a counter output task. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | EndWrite | Handles the end of an asynchronous write initiated with any of the counter asynchronous write methods, such as BeginWriteSingleSample(Boolean, CODataFrequency, AsyncCallback, Object). |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |
|  | WriteMultiSample(Boolean, CODataFrequency) | Writes one or more frequency samples to a single COChannel in a counter output task. |
|  | WriteMultiSample(Boolean, CODataTicks) | Writes one or more ticks samples to a single COChannel in a counter output task. |
|  | WriteMultiSample(Boolean, CODataTime) | Writes one or more time samples to a single COChannel in a counter output task. |
|  | WriteSingleSample(Boolean, CODataFrequency) | Writes a frequency sample to a single COChannel in a counter output task. |
|  | WriteSingleSample(Boolean, CODataTicks) | Writes a ticks sample to a single COChannel in a counter output task. |
|  | WriteSingleSample(Boolean, CODataTime) | Writes a time sample to a single COChannel in a counter output task. |

Top

##### See Also

###### Reference

CounterSingleChannelWriter Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_daqbuffer.htm language=enus -->
## TOPIC 00469: DaqBuffer Methods

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_daqbuffer.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_daqbuffer.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqBuffer Methods

### DaqBuffer Methods

The [DaqBuffer](t_nationalinstruments_daqmx_daqbuffer.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### See Also

###### Reference

DaqBuffer Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_daqexception.htm language=enus -->
## TOPIC 00470: DaqException Methods

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_daqexception.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_daqexception.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqException Methods

### DaqException Methods

The [DaqException](t_nationalinstruments_daqmx_daqexception.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetBaseException | When overridden in a derived class, returns the Exception that is the root cause of one or more subsequent exceptions. (Inherited from Exception.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetObjectData | Sets the SerializationInfo object with information about the exception. (Overrides ExceptionGetObjectData(SerializationInfo, StreamingContext).) |
|  | GetType | Gets the runtime type of the current instance. (Inherited from Exception.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Creates and returns a string representation of the current exception. (Inherited from Exception.) |

Top

##### See Also

###### Reference

DaqException Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_daqstream.htm language=enus -->
## TOPIC 00471: DaqStream Methods

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_daqstream.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_daqstream.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream Methods

### DaqStream Methods

The [DaqStream](t_nationalinstruments_daqmx_daqstream.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureInputBuffer | Overrides the automatic input buffer allocation that NI-DAQmx performs. |
|  | ConfigureOutputBuffer | Overrides the automatic output buffer allocation that NI-DAQmx performs. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ReadRaw | Reads raw, unprocessed samples from the channels in the task. |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |
|  | WriteRaw | Writes raw, unprocessed samples to the channels in the task. |

Top

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_daqsystem.htm language=enus -->
## TOPIC 00472: DaqSystem Methods

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_daqsystem.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_daqsystem.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem Methods

### DaqSystem Methods

The [DaqSystem](t_nationalinstruments_daqmx_daqsystem.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | AddCDaqSynchronizationConnection | Adds a cDAQ Sync connection between devices. The connection is not verified. |
|  | AddNetworkDevice(String, String, Double) | Adds a Network cDAQ device to the system. This method does not attempt to reserve the device after the device is successfully added. |
|  | AddNetworkDevice(String, String, Boolean, Double) | Adds a Network cDAQ device to the system and, if specified, attempts to reserve it. |
|  | AutoConfigureCDaqSynchronizationConnections | Detects and configures cDAQ Sync connections between devices. |
|  | ClearLastDaqWarning | Clears the value of the LastDaqWarning property, by setting the error code to zero and the error string to a blank string. |
|  | CloseSwitchRelays | Obsolete. Closes the specified relays. |
|  | ConnectSwitchChannels(String, Boolean) | Obsolete. Makes one or more connections between switch channels as specified by the connection list. |
|  | ConnectSwitchChannels(String, String, Boolean) | Obsolete. Makes a connection between two switch channels. |
|  | ConnectTerminals(String, String) | Creates a route between a source and destination terminal. |
|  | ConnectTerminals(String, String, SignalRoutingModifiers) | Creates a route between a source and destination terminal with the specified signal modification. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | CreateSwitchScanTask | Obsolete. Creates a new switch scanning task with the sequence specified in the scan list. |
|  | CreateWatchdogTimerTask | Creates a task to configure and control the watchdog timer of a static DIO device. The timer activates when you start the task. |
|  | DeleteGlobalChannel | Deletes the specified global channel that is stored in Measurement Automation Explorer (MAX). |
|  | DeleteScale | Deletes the specified custom scale that is stored in Measurement Automation Explorer (MAX). |
|  | DeleteTask | Deletes the specified task that is stored in Measurement Automation Explorer (MAX). |
|  | DisconnectAll | Obsolete. Terminates all active connections on the device, which places the relays into the topology reset state. |
|  | DisconnectSwitchChannels(String, Boolean) | Obsolete. Terminates one or more connections between switch channels as specified by the disconnection list. |
|  | DisconnectSwitchChannels(String, String, Boolean) | Obsolete. Terminates a connection between two channels. |
|  | DisconnectTerminals | Removes signal routes you created by using ConnectTerminals(String, String, SignalRoutingModifiers). |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetAnalogPowerUpStatesWithOutputType | Gets the states that analog physical channels on a device are set to when the device powers up or when the device is reset. |
|  | GetDevicePowerUpState(String, String, DigitalPowerUpState) | Gets the power up states for digital physical lines. |
|  | GetDevicePowerUpState(String, String, DigitalPullUpPullDownResistorState) | Gets the resistor level for lines when they are in tristate logic. |
|  | GetDevicePowerUpState(String, String, Double, String, Double) | Gets the power up states for analog physical channels. |
|  | GetDisconnectedCDaqSynchronizationPorts | Verifies configured cDAQ Sync connections between devices. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetLogicFamilyPowerUpState | Gets the digital logic family for a device. |
|  | GetPhysicalChannels | Gets an array that contains the physical channel names of devices installed in the system. |
|  | GetSavedChannelInfo | Creates a SavedChannelInfo object that you can use to retrieve information about the specified global channel stored in Measurement Automation Explorer (MAX). |
|  | GetSavedScaleInfo | Creates a SavedScaleInfo object that you can use to retrieve information about the specified custom scale stored in Measurement Automation Explorer (MAX). |
|  | GetSavedTaskInfo | Creates a SavedTaskInfo object that you can use to retrieve information about the specified task stored in Measurement Automation Explorer (MAX). |
|  | GetSwitchRelayCount | Obsolete. Returns the number of times a relay has actuated on switches that support querying the relay count. |
|  | GetSwitchRelayCounts | Obsolete. Returns the number of times a set of relays have actuated. |
|  | GetSwitchRelayPosition | Obsolete. Returns the current position of a single relay. |
|  | GetSwitchRelayPositions | Obsolete. Returns the current position of a set of relays. |
|  | GetTerminals | Gets an array that contains the terminal names of devices installed in the system. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | LoadDevice | Creates a Device that you can use to control the specified device or get information about that device. |
|  | LoadPhysicalChannel | Creates a PhysicalChannel that you can use to configure and retrieve TEDS information for the specified physical channel. |
|  | LoadScale | Loads a scale that is stored in Measurement Automation Explorer (MAX). |
|  | LoadSwitchChannel | Obsolete. Creates a SwitchChannel that you can use to get the switch channel capabilities and set the usage type for the switch channel. |
|  | LoadTask | Loads a task that is stored in Measurement Automation Explorer (MAX). |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | OnDaqWarning | Objects in the NI-DAQmx API call this method to indicate that a warning condition occurred. To get notification of warnings, attach an event handler to the DaqWarning event. |
|  | OpenSwitchRelays | Obsolete. Opens the specified relays. |
|  | RemoveCDaqSynchronizationConnection | Removes a cDAQ Sync connection between devices. The connection is not verified. |
|  | SaveGlobalChannel(Channel) | Saves the specified local or global channel to Measurement Automation Explorer (MAX) as a global channel, under the virtual name it was given when it was created. |
|  | SaveGlobalChannel(Channel, String, SaveOptions) | Saves the specified local or global channel to Measurement Automation Explorer (MAX) as a global channel, under the virtual name it was given when it was created and with specified author and options values. |
|  | SaveGlobalChannelAs(Channel, String) | Saves the local or global channel to Measurement Automation Explorer (MAX) as a global channel, under the specified name. |
|  | SaveGlobalChannelAs(Channel, String, String, SaveOptions) | Saves the local or global channel to Measurement Automation Explorer (MAX) as a global channel, under the specified name and specified author and options values. |
|  | SaveScale(Scale) | Saves the specified custom scale to Measurement Automation Explorer (MAX) under the name it was given when it was created. |
|  | SaveScale(Scale, String, SaveOptions) | Saves the specified custom scale to Measurement Automation Explorer (MAX) under the name it was given when it was created and with specified author and options values. |
|  | SaveScaleAs(Scale, String) | Saves the specified custom scale to Measurement Automation Explorer (MAX) under the specified name. |
|  | SaveScaleAs(Scale, String, String, SaveOptions) | Saves the specified custom scale to Measurement Automation Explorer (MAX) under the specified name and with specified author and options values. |
|  | SaveTask(Task) | Saves the specified task and any local channels it contains to Measurement Automation Explorer (MAX) under the name it was given when it was created. |
|  | SaveTask(Task, String, SaveOptions) | Saves the specified task and any local channels it contains to Measurement Automation Explorer (MAX) under the name it was given when it was created, with specifed author and options values. |
|  | SaveTaskAs(Task, String) | Saves the task and any local channels it contains to Measurement Automation Explorer (MAX) under the specified name. |
|  | SaveTaskAs(Task, String, String, SaveOptions) | Saves the task and any local channels it contains to Measurement Automation Explorer (MAX) under the specified name and with specified author and options values. |
|  | SetAnalogPowerUpStatesWithOutputType | Sets the states that analog physical channels on a device are set to when the device powers up or when the device is reset. |
|  | SetDevicePowerUpState(String, String, DigitalPowerUpState) | Updates the power up states to which to set digital physical channels on a device when the device powers up or when you reset the device. |
|  | SetDevicePowerUpState(String, String, DigitalPullUpPullDownResistorState) | Sets the resistor level for lines when they are in tristate logic. |
|  | SetDevicePowerUpState(String, String, Double, String, Double) | Updates the power up states to which to set analog physical channels on a device when the device powers up or when you reset the device. |
|  | SetLogicFamilyPowerUpState | Sets the digital logic family to use when the device powers up. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |
|  | TristateOutputTerminal | Sets a terminal to high-impedance state. |

Top

##### See Also

###### Reference

DaqSystem Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_dichannel.htm language=enus -->
## TOPIC 00473: DIChannel Methods

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_dichannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_dichannel.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DIChannel Methods

### DIChannel Methods

The [DIChannel](t_nationalinstruments_daqmx_dichannel.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Dispose | Releases all resources used by Channel. (Inherited from Channel.) |
|  | Dispose(Boolean) | Releases the managed and unmanaged resources used by Channel or optionally releases only the unmanaged resources. (Inherited from Channel.) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Inherited from Channel.) |

Top

##### See Also

###### Reference

DIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_digitalchangedetectioneventargs.htm language=enus -->
## TOPIC 00474: DigitalChangeDetectionEventArgs Methods

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_digitalchangedetectioneventargs.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_digitalchangedetectioneventargs.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalChangeDetectionEventArgs Methods

### DigitalChangeDetectionEventArgs Methods

The [DigitalChangeDetectionEventArgs](t_nationalinstruments_daqmx_digitalchangedetectioneventargs.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetObjectData | Sets the SerializationInfo object with information about the exception. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

DigitalChangeDetectionEventArgs Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_digitaledgearmstarttrigger.htm language=enus -->
## TOPIC 00475: DigitalEdgeArmStartTrigger Methods

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_digitaledgearmstarttrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_digitaledgearmstarttrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalEdgeArmStartTrigger Methods

### DigitalEdgeArmStartTrigger Methods

The [DigitalEdgeArmStartTrigger](t_nationalinstruments_daqmx_digitaledgearmstarttrigger.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### See Also

###### Reference

DigitalEdgeArmStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_digitaledgereferencetrigger.htm language=enus -->
## TOPIC 00476: DigitalEdgeReferenceTrigger Methods

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_digitaledgereferencetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_digitaledgereferencetrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalEdgeReferenceTrigger Methods

### DigitalEdgeReferenceTrigger Methods

The [DigitalEdgeReferenceTrigger](t_nationalinstruments_daqmx_digitaledgereferencetrigger.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### See Also

###### Reference

DigitalEdgeReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_digitaledgestarttrigger.htm language=enus -->
## TOPIC 00477: DigitalEdgeStartTrigger Methods

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_digitaledgestarttrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_digitaledgestarttrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalEdgeStartTrigger Methods

### DigitalEdgeStartTrigger Methods

The [DigitalEdgeStartTrigger](t_nationalinstruments_daqmx_digitaledgestarttrigger.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### See Also

###### Reference

DigitalEdgeStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_digitaledgewatchdogexpirationtrigger.htm language=enus -->
## TOPIC 00478: DigitalEdgeWatchdogExpirationTrigger Methods

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_digitaledgewatchdogexpirationtrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_digitaledgewatchdogexpirationtrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalEdgeWatchdogExpirationTrigger Methods

### DigitalEdgeWatchdogExpirationTrigger Methods

The [DigitalEdgeWatchdogExpirationTrigger](t_nationalinstruments_daqmx_digitaledgewatchdogexpirationtrigger.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### See Also

###### Reference

DigitalEdgeWatchdogExpirationTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_digitallevelpausetrigger.htm language=enus -->
## TOPIC 00479: DigitalLevelPauseTrigger Methods

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_digitallevelpausetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_digitallevelpausetrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalLevelPauseTrigger Methods

### DigitalLevelPauseTrigger Methods

The [DigitalLevelPauseTrigger](t_nationalinstruments_daqmx_digitallevelpausetrigger.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### See Also

###### Reference

DigitalLevelPauseTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_digitalmultichannelreader.htm language=enus -->
## TOPIC 00480: DigitalMultiChannelReader Methods

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_digitalmultichannelreader.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_digitalmultichannelreader.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader Methods

### DigitalMultiChannelReader Methods

The [DigitalMultiChannelReader](t_nationalinstruments_daqmx_digitalmultichannelreader.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | BeginMemoryOptimizedReadMultiSamplePortByte(Int32, AsyncCallback, Object, Byte) | Begins an asynchronous read of one or more 8-bit unsigned integer samples from one or more DIChannel objects in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePortByte(Int32, AsyncCallback, Object, Byte, ReallocationPolicy) | Begins an asynchronous read of one or more 8-bit unsigned integer samples from one or more DIChannel objects in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePortInt32(Int32, AsyncCallback, Object, Int32) | Begins an asynchronous read of one or more 32-bit integer samples from one or more DIChannel objects in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePortInt32(Int32, AsyncCallback, Object, Int32, ReallocationPolicy) | Begins an asynchronous read of one or more 32-bit integer samples from one or more DIChannel objects in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePortUInt16(Int32, AsyncCallback, Object, UInt16) | Begins an asynchronous read of one or more 16-bit unsigned integer samples from one or more DIChannel objects in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePortUInt16(Int32, AsyncCallback, Object, UInt16, ReallocationPolicy) | Begins an asynchronous read of one or more 16-bit unsigned integer samples from one or more DIChannel objects in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePortUInt32(Int32, AsyncCallback, Object, UInt32) | Begins an asynchronous read of one or more 32-bit unsigned integer samples from one or more DIChannel objects in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePortUInt32(Int32, AsyncCallback, Object, UInt32, ReallocationPolicy) | Begins an asynchronous read of one or more 32-bit unsigned integer samples from one or more DIChannel objects in a task. |
|  | BeginMemoryOptimizedReadSingleSampleMultiLine | Begins an asynchronous read of a single sample containing Boolean values from one or more DIChannel objects in a task. Each channel can contain multiple digital lines. |
|  | BeginReadMultiSamplePortByte | Begins an asynchronous read of one or more 8-bit unsigned integer samples from one or more DIChannel objects in a task. |
|  | BeginReadMultiSamplePortInt16 | Begins an asynchronous read of one or more 16-bit integer samples from one or more DIChannel objects in a task. |
|  | BeginReadMultiSamplePortInt32 | Begins an asynchronous read of one or more 32-bit integer samples from one or more DIChannel objects in a task. |
|  | BeginReadMultiSamplePortUInt16 | Begins an asynchronous read of one or more 16-bit unsigned integer samples from one or more DIChannel objects in a task. |
|  | BeginReadMultiSamplePortUInt32 | Begins an asynchronous read of one or more 32-bit unsigned integer samples from one or more DIChannel objects in a task. |
|  | BeginReadSingleSampleMultiLine | Begins an asynchronous read of a single sample containing Boolean values from one or more DIChannel objects in a task. Each channel can contain multiple digital lines. |
|  | BeginReadSingleSamplePortByte | Begins an asynchronous read of a single 8-bit unsigned integer sample from one or more DIChannel objects in a task. |
|  | BeginReadSingleSamplePortInt16 | Begins an asynchronous read of a single 16-bit integer sample from one or more DIChannel objects in a task. |
|  | BeginReadSingleSamplePortInt32 | Begins an asynchronous read of a single 32-bit integer sample from one or more DIChannel objects in a task. |
|  | BeginReadSingleSamplePortUInt16 | Begins an asynchronous read of a single 16-bit unsigned integer sample from one or more DIChannel objects in a task. |
|  | BeginReadSingleSamplePortUInt32 | Begins an asynchronous read of a single 32-bit unsigned integer sample from one or more DIChannel objects in a task. |
|  | BeginReadSingleSampleSingleLine | Begins an asynchronous read of a single Boolean sample from one or more DIChannel objects in a task. Each channel can contain a single digital line. |
|  | BeginReadWaveform(Int32, AsyncCallback, Object) | Begins an asynchronous read of one or more digital waveform samples from one or more DIChannel objects in a task. |
|  | BeginReadWaveform(TimeSpan, AsyncCallback, Object) | Begins an asynchronous read of one or more digital waveform samples from one or more DIChannel objects in a task for a specified duration. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | EndMemoryOptimizedReadMultiSamplePortByte | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePortByte(Int32, AsyncCallback, Object, Byte) and retrieves the read samples. |
|  | EndMemoryOptimizedReadMultiSamplePortInt32 | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePortInt32(Int32, AsyncCallback, Object, Int32) and retrieves the read samples. |
|  | EndMemoryOptimizedReadMultiSamplePortUInt16 | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePortUInt16(Int32, AsyncCallback, Object, UInt16) and retrieves the read samples. |
|  | EndMemoryOptimizedReadMultiSamplePortUInt32 | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePortUInt32(Int32, AsyncCallback, Object, UInt32) and retrieves the read samples. |
|  | EndMemoryOptimizedReadSingleSampleMultiLine | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadSingleSampleMultiLine(AsyncCallback, Object, Boolean) and retrieves the read samples. |
|  | EndReadMultiSamplePortByte | Handles the end of an asynchronous read initiated with BeginReadMultiSamplePortByte(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadMultiSamplePortInt16 | Handles the end of an asynchronous read initiated with BeginReadMultiSamplePortInt16(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadMultiSamplePortInt32 | Handles the end of an asynchronous read initiated with BeginReadMultiSamplePortInt32(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadMultiSamplePortUInt16 | Handles the end of an asynchronous read initiated with BeginReadMultiSamplePortUInt16(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadMultiSamplePortUInt32 | Handles the end of an asynchronous read initiated with BeginReadMultiSamplePortUInt32(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSampleMultiLine | Handles the end of an asynchronous read initiated with BeginReadSingleSampleMultiLine(AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSamplePortByte | Handles the end of an asynchronous read initiated with BeginReadSingleSamplePortByte(AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSamplePortInt16 | Handles the end of an asynchronous read initiated with BeginReadSingleSamplePortInt16(AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSamplePortInt32 | Handles the end of an asynchronous read initiated with BeginReadSingleSamplePortInt32(AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSamplePortUInt16 | Handles the end of an asynchronous read initiated with BeginReadSingleSamplePortUInt16(AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSamplePortUInt32 | Handles the end of an asynchronous read initiated with BeginReadSingleSamplePortUInt32(AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSampleSingleLine | Handles the end of an asynchronous read initiated with BeginReadSingleSampleSingleLine(AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadWaveform | Handles the end of an asynchronous read initiated with BeginReadWaveform(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | MemoryOptimizedReadMultiSamplePortByte(Int32, Byte, Int32) | Reads one or more 8-bit unsigned integer samples from one or more DIChannel objects in a task. |
|  | MemoryOptimizedReadMultiSamplePortByte(Int32, Byte, ReallocationPolicy, Int32) | Reads one or more 8-bit unsigned integer samples from one or more DIChannel objects in a task. |
|  | MemoryOptimizedReadMultiSamplePortInt32(Int32, Int32, Int32) | Reads one or more 32-bit integer samples from one or more DIChannel objects in a task. |
|  | MemoryOptimizedReadMultiSamplePortInt32(Int32, Int32, ReallocationPolicy, Int32) | Reads one or more 32-bit integer samples from one or more DIChannel objects in a task. |
|  | MemoryOptimizedReadMultiSamplePortUInt16(Int32, UInt16, Int32) | Reads one or more 16-bit unsigned integer samples from one or more DIChannel objects in a task. |
|  | MemoryOptimizedReadMultiSamplePortUInt16(Int32, UInt16, ReallocationPolicy, Int32) | Reads one or more 16-bit unsigned integer samples from one or more DIChannel objects in a task. |
|  | MemoryOptimizedReadMultiSamplePortUInt32(Int32, UInt32, Int32) | Reads one or more 32-bit unsigned integer samples from one or more DIChannel objects in a task. |
|  | MemoryOptimizedReadMultiSamplePortUInt32(Int32, UInt32, ReallocationPolicy, Int32) | Reads one or more 32-bit unsigned integer samples from one or more DIChannel objects in a task. |
|  | MemoryOptimizedReadSingleSampleMultiLine | Reads a single sample containing Boolean values from one or more DIChannel objects in a task. Each channel can contain multiple digital lines. |
|  | ReadMultiSamplePortByte | Reads one or more 8-bit unsigned integer samples from one or more DIChannel objects in a task. |
|  | ReadMultiSamplePortInt16 | Reads one or more 16-bit integer samples from one or more DIChannel objects in a task. |
|  | ReadMultiSamplePortInt32 | Reads one or more 32-bit integer samples from one or more DIChannel objects in a task. |
|  | ReadMultiSamplePortUInt16 | Reads one or more 16-bit unsigned integer samples from one or more DIChannel objects in a task. |
|  | ReadMultiSamplePortUInt32 | Reads one or more 32-bit unsigned integer samples from one or more DIChannel objects in a task. |
|  | ReadSingleSampleMultiLine | Reads a single sample containing Boolean values from one or more DIChannel objects in a task. Each channel can contain multiple digital lines. |
|  | ReadSingleSamplePortByte | Reads a single 8-bit unsigned integer sample from one or more DIChannel objects in a task. |
|  | ReadSingleSamplePortInt16 | Reads a single 16-bit integer sample from one or more DIChannel objects in a task. |
|  | ReadSingleSamplePortInt32 | Reads a single 32-bit integer sample from one or more DIChannel objects in a task. |
|  | ReadSingleSamplePortUInt16 | Reads a single 16-bit unsigned integer sample from one or more DIChannel objects in a task. |
|  | ReadSingleSamplePortUInt32 | Reads a single 32-bit unsigned integer sample from one or more DIChannel objects in a task. |
|  | ReadSingleSampleSingleLine | Reads a single Boolean sample from one or more DIChannel objects in a task. Each channel can contain a single digital line. |
|  | ReadWaveform(Int32) | Reads one or more digital waveform samples from one or more DIChannel objects in a task. |
|  | ReadWaveform(TimeSpan) | Reads one or more digital waveform samples from one or more DIChannel objects in a task for a specified duration. |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_starttrigger.htm language=enus -->
## TOPIC 00481: StartTrigger Methods

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_starttrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_starttrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

StartTrigger Methods

### StartTrigger Methods

The [StartTrigger](t_nationalinstruments_daqmx_starttrigger.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAnalogEdgeTrigger | Configures the task to start acquiring or generating samples when an analog signal crosses the level you specify. |
|  | ConfigureAnalogMultiEdgeTrigger | Configures the task to start acquiring or generating samples when any of the configured analog signals cross the respective levels you specify. |
|  | ConfigureAnalogWindowTrigger | Configures the task to start acquiring or generating samples when an analog signal enters or leaves a range you specify. |
|  | ConfigureDigitalEdgeTrigger | Configures the task to start acquiring or generating samples on a rising or falling edge of a digital signal. |
|  | ConfigureDigitalPatternTrigger | Configures the task to start acquiring or generating samples when a digital pattern is matched. |
|  | ConfigureNone | Configures the task to start acquiring or generating samples immediately upon starting the task. |
|  | ConfigureTimeTrigger | Configures the task to start acquiring or generating samples at a the specified triggerTime. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### See Also

###### Reference

StartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_timearmstarttrigger.htm language=enus -->
## TOPIC 00482: TimeArmStartTrigger Methods

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_timearmstarttrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/methods_t_nationalinstruments_daqmx_timearmstarttrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

TimeArmStartTrigger Methods

### TimeArmStartTrigger Methods

The [TimeArmStartTrigger](t_nationalinstruments_daqmx_timearmstarttrigger.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### See Also

###### Reference

TimeArmStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/operators_t_nationalinstruments_daqmx_cidatafrequency.htm language=enus -->
## TOPIC 00483: CIDataFrequency Operators

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/operators_t_nationalinstruments_daqmx_cidatafrequency.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/operators_t_nationalinstruments_daqmx_cidatafrequency.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CIDataFrequency Operators

### CIDataFrequency Operators

The [CIDataFrequency](t_nationalinstruments_daqmx_cidatafrequency.htm) type exposes the following members.

##### Operators

|  | Name | Description |
| --- | --- | --- |
|  | Equality | Returns if two CIDataFrequency objects are equal. |
|  | Inequality | Returns if two CIDataFrequency objects are not equal. |

Top

##### See Also

###### Reference

CIDataFrequency Structure

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/operators_t_nationalinstruments_daqmx_cidatatime.htm language=enus -->
## TOPIC 00484: CIDataTime Operators

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/operators_t_nationalinstruments_daqmx_cidatatime.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/operators_t_nationalinstruments_daqmx_cidatatime.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CIDataTime Operators

### CIDataTime Operators

The [CIDataTime](t_nationalinstruments_daqmx_cidatatime.htm) type exposes the following members.

##### Operators

|  | Name | Description |
| --- | --- | --- |
|  | Equality | Returns if two CIDataTime objects are equal. |
|  | Inequality | Returns if two CIDataTime objects are not equal. |

Top

##### See Also

###### Reference

CIDataTime Structure

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/operators_t_nationalinstruments_daqmx_codataticks.htm language=enus -->
## TOPIC 00485: CODataTicks Operators

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/operators_t_nationalinstruments_daqmx_codataticks.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/operators_t_nationalinstruments_daqmx_codataticks.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CODataTicks Operators

### CODataTicks Operators

The [CODataTicks](t_nationalinstruments_daqmx_codataticks.htm) type exposes the following members.

##### Operators

|  | Name | Description |
| --- | --- | --- |
|  | Equality | Returns true if two CODataTicks objects are equal. |
|  | Inequality | Returns true if two CODataTicks objects are not equal. |

Top

##### See Also

###### Reference

CODataTicks Structure

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createaccelerationchargechannel.htm language=enus -->
## TOPIC 00486: AIChannelCollectionCreateAccelerationChargeChannel Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createaccelerationchargechannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createaccelerationchargechannel.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateAccelerationChargeChannel Method

### AIChannelCollectionCreateAccelerationChargeChannel Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | CreateAccelerationChargeChannel(String, String, AITerminalConfiguration, Double, Double, AIAccelerationUnits, Double, AIAccelerationChargeSensitivityUnits) | Creates channel(s) that use an accelerometer to measure acceleration and adds the channel(s) to the task you specify with taskHandle. |
|  | CreateAccelerationChargeChannel(String, String, AITerminalConfiguration, Double, Double, String, Double, AIAccelerationChargeSensitivityUnits) | Creates channel(s) that use an accelerometer to measure acceleration and adds the channel(s) to the task you specify with taskHandle. |

Top

##### See Also

###### Reference

AIChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createbridgechannel.htm language=enus -->
## TOPIC 00487: AIChannelCollectionCreateBridgeChannel Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createbridgechannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createbridgechannel.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateBridgeChannel Method

### AIChannelCollectionCreateBridgeChannel Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | CreateBridgeChannel(String, String, Double, Double, AIBridgeUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double) | Creates an AIChannel that measures voltage ratios from a Wheatstone bridge. Use this instance with bridge-based sensors that measure phenomena other than strain, force, pressure, or torque, or that scale data to physical units NI-DAQmx does not support. This method adds one or more physical channels to the AIChannelCollection. Use a custom scale or other scaling code to convert the voltage ratios to physical units. |
|  | CreateBridgeChannel(String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double) | Creates an AIChannel that measures voltage ratios from a Wheatstone bridge, with the specified custom scale. Use this instance with bridge-based sensors that measure phenomena other than strain, force, pressure, or torque, or that scale data to physical units NI-DAQmx does not support. This method adds one or more physical channels to the AIChannelCollection. Use a custom scale or other scaling code to convert the voltage ratios to physical units. |

Top

##### See Also

###### Reference

AIChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createchargechannel.htm language=enus -->
## TOPIC 00488: AIChannelCollectionCreateChargeChannel Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createchargechannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createchargechannel.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateChargeChannel Method

### AIChannelCollectionCreateChargeChannel Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | CreateChargeChannel(String, String, AITerminalConfiguration, Double, Double, AIChargeUnits) | Creates an AIChannel to measure acceleration using a charge-based sensor. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateChargeChannel(String, String, AITerminalConfiguration, Double, Double, String) | Creates an AIChannel to measure acceleration using a charge-based sensor. This method adds one or more physical channels to the AIChannelCollection. |

Top

##### See Also

###### Reference

AIChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createforcebridgetwopointlinearchannel.htm language=enus -->
## TOPIC 00489: AIChannelCollectionCreateForceBridgeTwoPointLinearChannel Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createforcebridgetwopointlinearchannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createforcebridgetwopointlinearchannel.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateForceBridgeTwoPointLinearChannel Method

### AIChannelCollectionCreateForceBridgeTwoPointLinearChannel Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | CreateForceBridgeTwoPointLinearChannel(String, String, Double, Double, AIForceUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, Double, Double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure force or load. Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points of electrical and physical values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateForceBridgeTwoPointLinearChannel(String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, Double, Double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure force or load, with the specified custom scale. Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points of electrical and physical values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values. This method adds one or more physical channels to the AIChannelCollection. |

Top

##### See Also

###### Reference

AIChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createforceiepechannel.htm language=enus -->
## TOPIC 00490: AIChannelCollectionCreateForceIepeChannel Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createforceiepechannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createforceiepechannel.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateForceIepeChannel Method

### AIChannelCollectionCreateForceIepeChannel Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | CreateForceIepeChannel(String, String, AITerminalConfiguration, Double, Double, AIForceUnits, Double, AIForceIepeSensorSensitivityUnits, AIExcitationSource, Double) | Creates an AIChannel that uses an IEPE force sensor to measure force or load. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateForceIepeChannel(String, String, AITerminalConfiguration, Double, Double, String, Double, AIForceIepeSensorSensitivityUnits, AIExcitationSource, Double) | Creates an AIChannel that uses an IEPE force sensor to measure force or load, with the specified custom scale. This method adds one or more physical channels to the AIChannelCollection. |

Top

##### See Also

###### Reference

AIChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createfrequencyvoltagechannel.htm language=enus -->
## TOPIC 00491: AIChannelCollectionCreateFrequencyVoltageChannel Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createfrequencyvoltagechannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createfrequencyvoltagechannel.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateFrequencyVoltageChannel Method

### AIChannelCollectionCreateFrequencyVoltageChannel Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | CreateFrequencyVoltageChannel(String, String, Double, Double, Double, Double, AIFrequencyUnits) | Creates an AIChannel to measure frequency using a frequency-to-voltage converter. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateFrequencyVoltageChannel(String, String, Double, Double, Double, Double, String) | Creates an AIChannel with the specified custom scale to measure frequency using a frequency-to-voltage converter. This method adds one or more physical channels to the AIChannelCollection. |

Top

##### See Also

###### Reference

AIChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createlvdtchannel.htm language=enus -->
## TOPIC 00492: AIChannelCollectionCreateLvdtChannel Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createlvdtchannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createlvdtchannel.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateLvdtChannel Method

### AIChannelCollectionCreateLvdtChannel Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | CreateLvdtChannel(String, String, Double, Double, Double, AILvdtSensitivityUnits, AIExcitationSource, Double, Double, AIACExcitationWireMode, AILvdtUnits) | Creates an AIChannel that uses an LVDT to measure linear position. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateLvdtChannel(String, String, Double, Double, Double, AILvdtSensitivityUnits, AIExcitationSource, Double, Double, AIACExcitationWireMode, String) | Creates an AIChannel with the specified custom scale that uses an LVDT to measure linear position. This method adds one or more physical channels to the AIChannelCollection. |

Top

##### See Also

###### Reference

AIChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createpressurebridgepolynomialchannel.htm language=enus -->
## TOPIC 00493: AIChannelCollectionCreatePressureBridgePolynomialChannel Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createpressurebridgepolynomialchannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createpressurebridgepolynomialchannel.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreatePressureBridgePolynomialChannel Method

### AIChannelCollectionCreatePressureBridgePolynomialChannel Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | CreatePressureBridgePolynomialChannel(String, String, Double, Double, AIPressureUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure pressure. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electrical values to physical values (forward), as well as coefficients for a polynomial that converts physical values to electrical values (reverse). If you only know one set of coefficients, use PolynomialScale to generate the other set. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreatePressureBridgePolynomialChannel(String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure pressure, with the specified custom scale. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electrical values to physical values (forward), as well as coefficients for a polynomial that converts physical values to electrical values (reverse). If you only know one set of coefficients, use PolynomialScale to generate the other set. This method adds one or more physical channels to the AIChannelCollection. |

Top

##### See Also

###### Reference

AIChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createpressurebridgetablechannel.htm language=enus -->
## TOPIC 00494: AIChannelCollectionCreatePressureBridgeTableChannel Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createpressurebridgetablechannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createpressurebridgetablechannel.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreatePressureBridgeTableChannel Method

### AIChannelCollectionCreatePressureBridgeTableChannel Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | CreatePressureBridgeTableChannel(String, String, Double, Double, AIPressureUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, AIBridgeElectricalUnits, Double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure pressure. Use this instance with sensors whose specifications provide a table of electrical values and the corresponding physical values. When you use this scaling type, NI-DAQmx performs linear scaling between each pair of electrical and physical values. The input limits specified with the minimum value and maximum value parameters must fall within the smallest and largest physical values. For any data outside those endpoints, NI-DAQmx coerces that data to the endpoints. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreatePressureBridgeTableChannel(String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, AIBridgeElectricalUnits, Double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure pressure, with the specified custom scale. Use this instance with sensors whose specifications provide a table of electrical values and the corresponding physical values. When you use this scaling type, NI-DAQmx performs linear scaling between each pair of electrical and physical values. The input limits specified with the minimum value and maximum value parameters must fall within the smallest and largest physical values. For any data outside those endpoints, NI-DAQmx coerces that data to the endpoints. This method adds one or more physical channels to the AIChannelCollection. |

Top

##### See Also

###### Reference

AIChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_countermultichannelreader_memoryoptimizedreadmultisampleuint32.htm language=enus -->
## TOPIC 00495: CounterMultiChannelReaderMemoryOptimizedReadMultiSampleUInt32 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_countermultichannelreader_memoryoptimizedreadmultisampleuint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_countermultichannelreader_memoryoptimizedreadmultisampleuint32.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterMultiChannelReader.MemoryOptimizedReadMultiSampleUInt32 Method

### CounterMultiChannelReaderMemoryOptimizedReadMultiSampleUInt32 Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | MemoryOptimizedReadMultiSampleUInt32(Int32, UInt32, Int32) | Reads one or more UInt32 samples from one or more CIChannel objects in a task. |
|  | MemoryOptimizedReadMultiSampleUInt32(Int32, UInt32, ReallocationPolicy, Int32) | Reads one or more UInt32 samples from one or more CIChannel objects in a task. |

Top

##### See Also

###### Reference

CounterMultiChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_countermultichannelwriter_beginwritesinglesample.htm language=enus -->
## TOPIC 00496: CounterMultiChannelWriterBeginWriteSingleSample Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_countermultichannelwriter_beginwritesinglesample.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_countermultichannelwriter_beginwritesinglesample.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterMultiChannelWriter.BeginWriteSingleSample Method

### CounterMultiChannelWriterBeginWriteSingleSample Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | BeginWriteSingleSample(Boolean, CODataFrequency, AsyncCallback, Object) | Begins an asynchronous write of a single frequency sample to one or more COChannel objects in a counter output task. |
|  | BeginWriteSingleSample(Boolean, CODataTicks, AsyncCallback, Object) | Begins an asynchronous write of a single ticks sample to one or more COChannel objects in a counter output task. |
|  | BeginWriteSingleSample(Boolean, CODataTime, AsyncCallback, Object) | Begins an asynchronous write of a single time sample to one or more COChannel objects in a counter output task. |

Top

##### See Also

###### Reference

CounterMultiChannelWriter Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_countersinglechannelreader_memoryoptimizedreadmultisamplepulseticks.htm language=enus -->
## TOPIC 00497: CounterSingleChannelReaderMemoryOptimizedReadMultiSamplePulseTicks Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_countersinglechannelreader_memoryoptimizedreadmultisamplepulseticks.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_countersinglechannelreader_memoryoptimizedreadmultisamplepulseticks.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelReader.MemoryOptimizedReadMultiSamplePulseTicks Method

### CounterSingleChannelReaderMemoryOptimizedReadMultiSamplePulseTicks Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | MemoryOptimizedReadMultiSamplePulseTicks(Int32, CIDataTicks, Int32) | Reads one or more CIDataTicks samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSamplePulseTicks(Int32, CIDataTicks, ReallocationPolicy, Int32) | Reads one or more CIDataTicks samples from a single CIChannel in a task. |

Top

##### See Also

###### Reference

CounterSingleChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_countersinglechannelreader_memoryoptimizedreadmultisamplepulsetime.htm language=enus -->
## TOPIC 00498: CounterSingleChannelReaderMemoryOptimizedReadMultiSamplePulseTime Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_countersinglechannelreader_memoryoptimizedreadmultisamplepulsetime.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_countersinglechannelreader_memoryoptimizedreadmultisamplepulsetime.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelReader.MemoryOptimizedReadMultiSamplePulseTime Method

### CounterSingleChannelReaderMemoryOptimizedReadMultiSamplePulseTime Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | MemoryOptimizedReadMultiSamplePulseTime(Int32, CIDataTime, Int32) | Reads one or more CIDataTime samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSamplePulseTime(Int32, CIDataTime, ReallocationPolicy, Int32) | Reads one or more CIDataTime samples from a single CIChannel in a task. |

Top

##### See Also

###### Reference

CounterSingleChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_countersinglechannelreader_memoryoptimizedreadmultisampleuint32.htm language=enus -->
## TOPIC 00499: CounterSingleChannelReaderMemoryOptimizedReadMultiSampleUInt32 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_countersinglechannelreader_memoryoptimizedreadmultisampleuint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_countersinglechannelreader_memoryoptimizedreadmultisampleuint32.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelReader.MemoryOptimizedReadMultiSampleUInt32 Method

### CounterSingleChannelReaderMemoryOptimizedReadMultiSampleUInt32 Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | MemoryOptimizedReadMultiSampleUInt32(Int32, UInt32, Int32) | Reads one or more UInt32 samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSampleUInt32(Int32, UInt32, ReallocationPolicy, Int32) | Reads one or more UInt32 samples from a single CIChannel in a task. |

Top

##### See Also

###### Reference

CounterSingleChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_countersinglechannelwriter_beginwritemultisample.htm language=enus -->
## TOPIC 00500: CounterSingleChannelWriterBeginWriteMultiSample Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_countersinglechannelwriter_beginwritemultisample.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/overload_nationalinstruments_daqmx_countersinglechannelwriter_beginwritemultisample.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelWriter.BeginWriteMultiSample Method

### CounterSingleChannelWriterBeginWriteMultiSample Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | BeginWriteMultiSample(Boolean, CODataFrequency, AsyncCallback, Object) | Begins an asynchronous write of one or more frequency samples to a single COChannel in a counter output task. |
|  | BeginWriteMultiSample(Boolean, CODataTicks, AsyncCallback, Object) | Begins an asynchronous write of one or more ticks samples to a single COChannel in a counter output task. |
|  | BeginWriteMultiSample(Boolean, CODataTime, AsyncCallback, Object) | Begins an asynchronous write of one or more time samples to a single COChannel in a counter output task. |

Top

##### See Also

###### Reference

CounterSingleChannelWriter Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.
