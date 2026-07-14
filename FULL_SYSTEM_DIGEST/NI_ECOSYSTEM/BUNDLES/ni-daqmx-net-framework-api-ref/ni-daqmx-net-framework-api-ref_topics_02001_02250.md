# NI DOCUMENT BUNDLE: ni-daqmx-net-framework-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-daqmx-net-framework-api-ref start=2001 end=2250 -->
<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-memoryoptimizedreadmultisampleportint32__int-ref-reallocationpolicy-out.html language=enus -->
## TOPIC 02001: MemoryOptimizedReadMultiSamplePortInt32(int, ref int[], ReallocationPolicy, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-memoryoptimizedreadmultisampleportint32__int-ref-reallocationpolicy-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-memoryoptimizedreadmultisampleportint32__int-ref-reallocationpolicy-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more 32-bit integer samples from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic int[] MemoryOptimizedReadMultiSamplePortInt32(int numberOfSamples, ref int[] data, ReallocationPolicy policy, out int actualNumberOfSamplesRead)RemarksIf the data buffer is la

### MemoryOptimizedReadMultiSamplePortInt32(int, ref int[], ReallocationPolicy, out int)

Reads one or more 32-bit integer samples from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int[] MemoryOptimizedReadMultiSamplePortInt32(int numberOfSamples, ref int[] data, ReallocationPolicy policy, out int actualNumberOfSamplesRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref int[] | An initialized 1D array of 32-bit integer samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-memoryoptimizedreadmultisampleportuint16__int-ref-out.html language=enus -->
## TOPIC 02002: MemoryOptimizedReadMultiSamplePortUInt16(int, ref ushort[], out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-memoryoptimizedreadmultisampleportuint16__int-ref-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-memoryoptimizedreadmultisampleportuint16__int-ref-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more 16-bit unsigned integer samples from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic ushort[] MemoryOptimizedReadMultiSamplePortUInt16(int numberOfSamples, ref ushort[] data, out int actualNumberOfSamplesRead)RemarksIf the data buffer is large enough

### MemoryOptimizedReadMultiSamplePortUInt16(int, ref ushort[], out int)

Reads one or more 16-bit unsigned integer samples from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public ushort[] MemoryOptimizedReadMultiSamplePortUInt16(int numberOfSamples, ref ushort[] data, out int actualNumberOfSamplesRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref ushort[] | An initialized 1D array of 16-bit unsigned integer samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized. |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-memoryoptimizedreadmultisampleportuint16__int-ref-reallocationpolicy-out.html language=enus -->
## TOPIC 02003: MemoryOptimizedReadMultiSamplePortUInt16(int, ref ushort[], ReallocationPolicy, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-memoryoptimizedreadmultisampleportuint16__int-ref-reallocationpolicy-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-memoryoptimizedreadmultisampleportuint16__int-ref-reallocationpolicy-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more 16-bit unsigned integer samples from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic ushort[] MemoryOptimizedReadMultiSamplePortUInt16(int numberOfSamples, ref ushort[] data, ReallocationPolicy policy, out int actualNumberOfSamplesRead)RemarksIf the d

### MemoryOptimizedReadMultiSamplePortUInt16(int, ref ushort[], ReallocationPolicy, out int)

Reads one or more 16-bit unsigned integer samples from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public ushort[] MemoryOptimizedReadMultiSamplePortUInt16(int numberOfSamples, ref ushort[] data, ReallocationPolicy policy, out int actualNumberOfSamplesRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref ushort[] | An initialized 1D array of 16-bit unsigned integer samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-memoryoptimizedreadmultisampleportuint32__int-ref-out.html language=enus -->
## TOPIC 02004: MemoryOptimizedReadMultiSamplePortUInt32(int, ref uint[], out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-memoryoptimizedreadmultisampleportuint32__int-ref-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-memoryoptimizedreadmultisampleportuint32__int-ref-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more 32-bit unsigned integer samples from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic uint[] MemoryOptimizedReadMultiSamplePortUInt32(int numberOfSamples, ref uint[] data, out int actualNumberOfSamplesRead)RemarksIf the data buffer is large enough to h

### MemoryOptimizedReadMultiSamplePortUInt32(int, ref uint[], out int)

Reads one or more 32-bit unsigned integer samples from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public uint[] MemoryOptimizedReadMultiSamplePortUInt32(int numberOfSamples, ref uint[] data, out int actualNumberOfSamplesRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref uint[] | An initialized 1D array of 32-bit unsigned integer samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized. |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-memoryoptimizedreadmultisampleportuint32__int-ref-reallocationpolicy-out.html language=enus -->
## TOPIC 02005: MemoryOptimizedReadMultiSamplePortUInt32(int, ref uint[], ReallocationPolicy, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-memoryoptimizedreadmultisampleportuint32__int-ref-reallocationpolicy-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-memoryoptimizedreadmultisampleportuint32__int-ref-reallocationpolicy-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more 32-bit unsigned integer samples from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic uint[] MemoryOptimizedReadMultiSamplePortUInt32(int numberOfSamples, ref uint[] data, ReallocationPolicy policy, out int actualNumberOfSamplesRead)RemarksIf the data

### MemoryOptimizedReadMultiSamplePortUInt32(int, ref uint[], ReallocationPolicy, out int)

Reads one or more 32-bit unsigned integer samples from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public uint[] MemoryOptimizedReadMultiSamplePortUInt32(int numberOfSamples, ref uint[] data, ReallocationPolicy policy, out int actualNumberOfSamplesRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref uint[] | An initialized 1D array of 32-bit unsigned integer samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-memoryoptimizedreadsinglesamplemultiline__bool_arr1.html language=enus -->
## TOPIC 02006: MemoryOptimizedReadSingleSampleMultiLine(bool[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-memoryoptimizedreadsinglesamplemultiline__bool_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-memoryoptimizedreadsinglesamplemultiline__bool_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a single Boolean sample from a single DIChannel in a task. The channel can contain multiple digital lines. SyntaxNamespace: NationalInstruments.DAQmxpublic bool[] MemoryOptimizedReadSingleSampleMultiLine(bool[] data)RemarksIf the data buffer is large enough to hold the number of samples reques

### MemoryOptimizedReadSingleSampleMultiLine(bool[])

Reads a single Boolean sample from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task. The channel can contain multiple digital lines.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool[] MemoryOptimizedReadSingleSampleMultiLine(bool[] data)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| data | bool[] | An initialized 1D array of Boolean samples that contains the read data. Each element in the array corresponds to a digital line in the channel. |

#### Returns

A 1D array of Boolean samples from the task. Each element of the array corresponds to a digital line in the channel.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized. |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-readmultisampleportbyte__int.html language=enus -->
## TOPIC 02007: ReadMultiSamplePortByte(int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-readmultisampleportbyte__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-readmultisampleportbyte__int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more 8-bit unsigned integer samples from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic byte[] ReadMultiSamplePortByte(int numberOfSamples)RemarksUse this method for devices with up to eight lines per port. NI-DAQmx read and write methods time out after t

### ReadMultiSamplePortByte(int)

Reads one or more 8-bit unsigned integer samples from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public byte[] ReadMultiSamplePortByte(int numberOfSamples)

#### Remarks

Use this method for devices with up to eight lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |

#### Returns

A 1D array of 8-bit unsigned integer samples from the task. Each element in the array corresponds to a sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-readmultisampleportint16__int.html language=enus -->
## TOPIC 02008: ReadMultiSamplePortInt16(int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-readmultisampleportint16__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-readmultisampleportint16__int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more 16-bit integer samples from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic short[] ReadMultiSamplePortInt16(int numberOfSamples)RemarksUse this method for devices with up to 16 lines per port. NI-DAQmx read and write methods time out after the amount

### ReadMultiSamplePortInt16(int)

Reads one or more 16-bit integer samples from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public short[] ReadMultiSamplePortInt16(int numberOfSamples)

#### Remarks

Use this method for devices with up to 16 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |

#### Returns

A 1D array of 16-bit integer samples from the task. Each element in the array corresponds to a sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-readmultisampleportint32__int.html language=enus -->
## TOPIC 02009: ReadMultiSamplePortInt32(int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-readmultisampleportint32__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-readmultisampleportint32__int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more 32-bit integer samples from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic int[] ReadMultiSamplePortInt32(int numberOfSamples)RemarksUse this method for devices with up to 32 lines per port. NI-DAQmx read and write methods time out after the amount o

### ReadMultiSamplePortInt32(int)

Reads one or more 32-bit integer samples from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int[] ReadMultiSamplePortInt32(int numberOfSamples)

#### Remarks

Use this method for devices with up to 32 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |

#### Returns

A 1D array of 32-bit integer samples from the task. Each element in the array corresponds to a sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-readmultisampleportuint16__int.html language=enus -->
## TOPIC 02010: ReadMultiSamplePortUInt16(int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-readmultisampleportuint16__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-readmultisampleportuint16__int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more 16-bit unsigned integer samples from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic ushort[] ReadMultiSamplePortUInt16(int numberOfSamples)RemarksUse this method for devices with up to 16 lines per port. NI-DAQmx read and write methods time out after

### ReadMultiSamplePortUInt16(int)

Reads one or more 16-bit unsigned integer samples from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public ushort[] ReadMultiSamplePortUInt16(int numberOfSamples)

#### Remarks

Use this method for devices with up to 16 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |

#### Returns

A 1D array of 16-bit unsigned integer samples from the task. Each element in the array corresponds to a sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-readmultisampleportuint32__int.html language=enus -->
## TOPIC 02011: ReadMultiSamplePortUInt32(int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-readmultisampleportuint32__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-readmultisampleportuint32__int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more 32-bit unsigned integer samples from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic uint[] ReadMultiSamplePortUInt32(int numberOfSamples)RemarksUse this method for devices with up to 32 lines per port. NI-DAQmx read and write methods time out after t

### ReadMultiSamplePortUInt32(int)

Reads one or more 32-bit unsigned integer samples from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public uint[] ReadMultiSamplePortUInt32(int numberOfSamples)

#### Remarks

Use this method for devices with up to 32 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |

#### Returns

A 1D array of 32-bit unsigned integer samples from the task. Each element in the array corresponds to a sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-readsinglesamplemultiline.html language=enus -->
## TOPIC 02012: ReadSingleSampleMultiLine()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-readsinglesamplemultiline.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-readsinglesamplemultiline.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a single Boolean sample from a single DIChannel in a task. The channel can contain multiple digital lines. SyntaxNamespace: NationalInstruments.DAQmxpublic bool[] ReadSingleSampleMultiLine()RemarksNI-DAQmx read and write methods time out after the amount of time specified by the Timeout proper

### ReadSingleSampleMultiLine()

Reads a single Boolean sample from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task. The channel can contain multiple digital lines.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool[] ReadSingleSampleMultiLine()

#### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Returns

A 1D array of Boolean samples from the task. Each element of the array corresponds to a digital line in the channel.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-readsinglesampleportbyte.html language=enus -->
## TOPIC 02013: ReadSingleSamplePortByte()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-readsinglesampleportbyte.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-readsinglesampleportbyte.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a single 8-bit unsigned integer sample from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic byte ReadSingleSamplePortByte()RemarksUse this method for devices with up to eight lines per port. NI-DAQmx read and write methods time out after the amount of time specif

### ReadSingleSamplePortByte()

Reads a single 8-bit unsigned integer sample from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public byte ReadSingleSamplePortByte()

#### Remarks

Use this method for devices with up to eight lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Returns

An 8-bit unsigned integer sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-readsinglesampleportint16.html language=enus -->
## TOPIC 02014: ReadSingleSamplePortInt16()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-readsinglesampleportint16.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-readsinglesampleportint16.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a single 16-bit integer sample from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic short ReadSingleSamplePortInt16()RemarksUse this method for devices with up to 16 lines per port. NI-DAQmx read and write methods time out after the amount of time specified by th

### ReadSingleSamplePortInt16()

Reads a single 16-bit integer sample from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public short ReadSingleSamplePortInt16()

#### Remarks

Use this method for devices with up to 16 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Returns

A 16-bit integer sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-readsinglesampleportint32.html language=enus -->
## TOPIC 02015: ReadSingleSamplePortInt32()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-readsinglesampleportint32.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-readsinglesampleportint32.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a single 32-bit integer sample from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic int ReadSingleSamplePortInt32()RemarksUse this method for devices with up to 32 lines per port. NI-DAQmx read and write methods time out after the amount of time specified by the

### ReadSingleSamplePortInt32()

Reads a single 32-bit integer sample from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int ReadSingleSamplePortInt32()

#### Remarks

Use this method for devices with up to 32 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Returns

A 32-bit integer sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-readsinglesampleportuint16.html language=enus -->
## TOPIC 02016: ReadSingleSamplePortUInt16()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-readsinglesampleportuint16.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-readsinglesampleportuint16.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a single 16-bit unsigned integer sample from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic ushort ReadSingleSamplePortUInt16()RemarksUse this method for devices with up to 16 lines per port. NI-DAQmx read and write methods time out after the amount of time spec

### ReadSingleSamplePortUInt16()

Reads a single 16-bit unsigned integer sample from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public ushort ReadSingleSamplePortUInt16()

#### Remarks

Use this method for devices with up to 16 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Returns

A 16-bit unsigned integer sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-readsinglesampleportuint32.html language=enus -->
## TOPIC 02017: ReadSingleSamplePortUInt32()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-readsinglesampleportuint32.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-readsinglesampleportuint32.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a single 32-bit unsigned integer sample from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic uint ReadSingleSamplePortUInt32()RemarksUse this method for devices with up to 32 lines per port. NI-DAQmx read and write methods time out after the amount of time specif

### ReadSingleSamplePortUInt32()

Reads a single 32-bit unsigned integer sample from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public uint ReadSingleSamplePortUInt32()

#### Remarks

Use this method for devices with up to 32 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Returns

A 32-bit unsigned integer sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-readsinglesamplesingleline.html language=enus -->
## TOPIC 02018: ReadSingleSampleSingleLine()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-readsinglesamplesingleline.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-readsinglesamplesingleline.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a single Boolean sample from a single DIChannel in a task. The task can contain only a single digital line. SyntaxNamespace: NationalInstruments.DAQmxpublic bool ReadSingleSampleSingleLine()RemarksNI-DAQmx read and write methods time out after the amount of time specified by the Timeout proper

### ReadSingleSampleSingleLine()

Reads a single Boolean sample from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task. The task can contain only a single digital line.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool ReadSingleSampleSingleLine()

#### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Returns

A Boolean sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-readwaveform__int.html language=enus -->
## TOPIC 02019: ReadWaveform(int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-readwaveform__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-readwaveform__int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more digital waveform samples from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic DigitalWaveform ReadWaveform(int numberOfSamples)RemarksThe data returned from digital waveform reads is affected by the WaveformAttributeMode property of the DaqStream you

### ReadWaveform(int)

Reads one or more digital waveform samples from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public DigitalWaveform ReadWaveform(int numberOfSamples)

#### Remarks

The data returned from digital waveform reads is affected by the [WaveformAttributeMode](nationalinstruments-daqmx-daqstream-waveformattributemode.html) property of the [DaqStream](nationalinstruments-daqmx-daqstream.html) you are reading from.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |

#### Returns

A DigitalWaveform containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-readwaveform__timespan.html language=enus -->
## TOPIC 02020: ReadWaveform(TimeSpan)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-readwaveform__timespan.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-readwaveform__timespan.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more digital waveform samples from a single DIChannel in a task for a specified duration . SyntaxNamespace: NationalInstruments.DAQmxpublic DigitalWaveform ReadWaveform(TimeSpan duration)RemarksNI-DAQmx scales the read data to the units of the measurement, including any custom scaling y

### ReadWaveform(TimeSpan)

Reads one or more digital waveform samples from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task for a specified *duration* .

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public DigitalWaveform ReadWaveform(TimeSpan duration)

#### Remarks

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units when creating channels using the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](nationalinstruments-daqmx-daqstream-waveformattributemode.html) property of the [DaqStream](nationalinstruments-daqmx-daqstream.html) being read.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the [Stream](nationalinstruments-daqmx-task-stream.html) object used for the reads or writes.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| duration | TimeSpan | The duration of time to read the waveform. The duration specified must be long enough to read at least one sample at the configured SampleClockRate. |

#### Returns

A DigitalWaveform containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If the duration provided was less than Zero. |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-synchronizecallbacks.html language=enus -->
## TOPIC 02021: SynchronizeCallbacks

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-synchronizecallbacks.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-synchronizecallbacks.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how events and callback delegates are invoked. SyntaxNamespace: NationalInstruments.DAQmxpublic bool SynchronizeCallbacks { get; set; }RemarksIn some cases, callbacks and event handlers are executed in a different thread than the rest of the program. Therefore, you must take special care w

### SynchronizeCallbacks

Specifies how events and callback delegates are invoked.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool SynchronizeCallbacks { get; set; }

#### Remarks

In some cases, callbacks and event handlers are executed in a different thread than the rest of the program. Therefore, you must take special care when accessing objects that have thread affinity, such as UI controls, from these callbacks and event handlers. For more information, refer to Events, Callbacks, and Thread Safety in Measurement Studio .NET Class Libraries.

Reading and Writing with NI-DAQmx Streams

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-synchronizingobject.html language=enus -->
## TOPIC 02022: SynchronizingObject

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-synchronizingobject.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-synchronizingobject.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: Use SynchronizeCallbacks to specify that the object marshals callbacks across threads appropriately. Will warn if used Gets or sets the object that marshals event-handler and callback calls. SyntaxNamespace: NationalInstruments.DAQmxpublic ISynchronizeInvoke SynchronizingObject { get; set;

### SynchronizingObject

**Obsolete: Use SynchronizeCallbacks to specify that the object marshals callbacks across threads appropriately. Will warn if used** 
Gets or sets the object that marshals event-handler and callback calls.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public ISynchronizeInvoke SynchronizingObject { get; set; }

#### Remarks

The ISynchronizeInvoke representing the object that marshals the event-handler and callback calls. The default value is null.

null

Note

For more information, refer to Events, Callbacks, and Thread Safety in Measurement Studio .NET Class Libraries.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-tostring.html language=enus -->
## TOPIC 02023: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-tostring.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the object. SyntaxNamespace: NationalInstruments.DAQmxpublic override string ToString()RemarksOverrides ToString. ReturnsA string representation of the object.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ToString()

Returns a string representation of the object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override string ToString()

#### Remarks

Overrides ToString.

#### Returns

A string representation of the object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader.html language=enus -->
## TOPIC 02024: DigitalSingleChannelReader Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains methods for reading samples from the digital input or output channel in a task. Derives fromMarshalByRefObjectISynchronizeCallbacksISupportSynchronizationContextSyntaxNamespace: NationalInstruments.DAQmxpublic class DigitalSingleChannelReader : MarshalByRefObject, ISynchronizeCallbacks, ISu

### DigitalSingleChannelReader Class

Contains methods for reading samples from the digital input or output channel in a task.

#### Derives from

- MarshalByRefObject
- ISynchronizeCallbacks
- ISupportSynchronizationContext

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class DigitalSingleChannelReader : MarshalByRefObject, ISynchronizeCallbacks, ISupportSynchronizationContext

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| DigitalSingleChannelReader(DaqStream) | Creates a new instance of the DigitalSingleChannelReader class to read from the specified DaqStream. |

#### Properties

| Name | Description |
| --- | --- |
| SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |
| SynchronizingObject | Obsolete: Use SynchronizeCallbacks to specify that the object marshals callbacks across threads appropriately. Will warn if usedGets or sets the object that marshals event-handler and callback calls. |

#### Methods

| Name | Description |
| --- | --- |
| BeginMemoryOptimizedReadMultiSamplePortByte(int, AsyncCallback, object, byte[], ReallocationPolicy) | Begins an asynchronous read of one or more 8-bit unsigned integer samples from a single DIChannel in a task. |
| BeginMemoryOptimizedReadMultiSamplePortByte(int, AsyncCallback, object, byte[]) | Begins an asynchronous read of one or more 8-bit unsigned integer samples from a single DIChannel in a task. |
| BeginMemoryOptimizedReadMultiSamplePortInt32(int, AsyncCallback, object, int[]) | Begins an asynchronous read of one or more 32-bit integer samples from a single DIChannel in a task. |
| BeginMemoryOptimizedReadMultiSamplePortInt32(int, AsyncCallback, object, int[], ReallocationPolicy) | Begins an asynchronous read of one or more 32-bit integer samples from a single DIChannel in a task. |
| BeginMemoryOptimizedReadMultiSamplePortUInt16(int, AsyncCallback, object, ushort[], ReallocationPolicy) | Begins an asynchronous read of one or more 16-bit unsigned integer samples from a single DIChannel in a task. |
| BeginMemoryOptimizedReadMultiSamplePortUInt16(int, AsyncCallback, object, ushort[]) | Begins an asynchronous read of one or more 16-bit unsigned integer samples from a single DIChannel in a task. |
| BeginMemoryOptimizedReadMultiSamplePortUInt32(int, AsyncCallback, object, uint[]) | Begins an asynchronous read of one or more 32-bit unsigned integer samples from a single DIChannel in a task. |
| BeginMemoryOptimizedReadMultiSamplePortUInt32(int, AsyncCallback, object, uint[], ReallocationPolicy) | Begins an asynchronous read of one or more 32-bit unsigned integer samples from a single DIChannel in a task. |
| BeginMemoryOptimizedReadSingleSampleMultiLine(AsyncCallback, object, bool[]) | Begins an asynchronous read of a single Boolean sample from a single DIChannel in a task. The channel can contain multiple digital lines. |
| BeginReadMultiSamplePortByte(int, AsyncCallback, object) | Begins an asynchronous read of one or more 8-bit unsigned integer samples from a single DIChannel in a task. |
| BeginReadMultiSamplePortInt16(int, AsyncCallback, object) | Begins an asynchronous read of one or more 16-bit integer samples from a single DIChannel in a task. |
| BeginReadMultiSamplePortInt32(int, AsyncCallback, object) | Begins an asynchronous read of one or more 32-bit integer samples from a single DIChannel in a task. |
| BeginReadMultiSamplePortUInt16(int, AsyncCallback, object) | Begins an asynchronous read of one or more 16-bit unsigned integer samples from a single DIChannel in a task. |
| BeginReadMultiSamplePortUInt32(int, AsyncCallback, object) | Begins an asynchronous read of one or more 32-bit unsigned integer samples from a single DIChannel in a task. |
| BeginReadSingleSampleMultiLine(AsyncCallback, object) | Begins an asynchronous read of a single Boolean sample from a single DIChannel in a task. The channel can contain multiple digital lines. |
| BeginReadSingleSamplePortByte(AsyncCallback, object) | Begins an asynchronous read of a single 8-bit unsigned integer sample from a single DIChannel in a task. |
| BeginReadSingleSamplePortInt16(AsyncCallback, object) | Begins an asynchronous read of a single 16-bit integer sample from a single DIChannel in a task. |
| BeginReadSingleSamplePortInt32(AsyncCallback, object) | Begins an asynchronous read of a single 32-bit integer sample from a single DIChannel in a task. |
| BeginReadSingleSamplePortUInt16(AsyncCallback, object) | Begins an asynchronous read of a single 16-bit unsigned integer sample from a single DIChannel in a task. |
| BeginReadSingleSamplePortUInt32(AsyncCallback, object) | Begins an asynchronous read of a single 32-bit unsigned integer sample from a single DIChannel in a task. |
| BeginReadSingleSampleSingleLine(AsyncCallback, object) | Begins an asynchronous read of a single Boolean sample from a single DIChannel in a task. The task can contain only a single digital line. |
| BeginReadWaveform(int, AsyncCallback, object) | Begins an asynchronous read of one or more digital waveform samples from a single DIChannel in a task. |
| BeginReadWaveform(TimeSpan, AsyncCallback, object) | Begins an asynchronous read of one or more digital waveform samples from a single DIChannel in a task for a specified duration . |
| EndMemoryOptimizedReadMultiSamplePortByte(IAsyncResult, out int) | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePortByte(int, AsyncCallback, object, byte[]) and retrieves the read samples. |
| EndMemoryOptimizedReadMultiSamplePortInt32(IAsyncResult, out int) | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePortInt32(int, AsyncCallback, object, int[, ]) and retrieves the read samples. |
| EndMemoryOptimizedReadMultiSamplePortUInt16(IAsyncResult, out int) | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePortUInt16(int, AsyncCallback, object, ushort[]) and retrieves the read samples. |
| EndMemoryOptimizedReadMultiSamplePortUInt32(IAsyncResult, out int) | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePortUInt32(int, AsyncCallback, object, uint[]) and retrieves the read samples. |
| EndMemoryOptimizedReadSingleSampleMultiLine(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadSingleSampleMultiLine(AsyncCallback, object, bool[]) and retrieves the read samples. |
| EndReadMultiSamplePortByte(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadMultiSamplePortByte(int, AsyncCallback, object) and retrieves the read samples. |
| EndReadMultiSamplePortInt16(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadMultiSamplePortInt16(int, AsyncCallback, object) and retrieves the read samples. |
| EndReadMultiSamplePortInt32(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadMultiSamplePortInt32(int, AsyncCallback, object) and retrieves the read samples. |
| EndReadMultiSamplePortUInt16(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadMultiSamplePortUInt16(int, AsyncCallback, object) and retrieves the read samples. |
| EndReadMultiSamplePortUInt32(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadMultiSamplePortUInt32(int, AsyncCallback, object) and retrieves the read samples. |
| EndReadSingleSampleMultiLine(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadSingleSampleMultiLine(AsyncCallback, object) and retrieves the read samples. |
| EndReadSingleSamplePortByte(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadSingleSamplePortByte(AsyncCallback, object) and retrieves the read samples. |
| EndReadSingleSamplePortInt16(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadSingleSamplePortInt16(AsyncCallback, object) and retrieves the read samples. |
| EndReadSingleSamplePortInt32(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadSingleSamplePortInt32(AsyncCallback, object) and retrieves the read samples. |
| EndReadSingleSamplePortUInt16(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadSingleSamplePortUInt16(AsyncCallback, object) and retrieves the read samples. |
| EndReadSingleSamplePortUInt32(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadSingleSamplePortUInt32(AsyncCallback, object) and retrieves the read samples. |
| EndReadSingleSampleSingleLine(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadSingleSampleSingleLine(AsyncCallback, object) and retrieves the read samples. |
| EndReadWaveform(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadWaveform(int, AsyncCallback, object) and retrieves the read samples. |
| MemoryOptimizedReadMultiSamplePortByte(int, ref byte[], out int) | Reads one or more 8-bit unsigned integer samples from a single DIChannel in a task. |
| MemoryOptimizedReadMultiSamplePortByte(int, ref byte[], ReallocationPolicy, out int) | Reads one or more 8-bit unsigned integer samples from a single DIChannel in a task. |
| MemoryOptimizedReadMultiSamplePortInt32(int, ref int[], out int) | Reads one or more 32-bit integer samples from a single DIChannel in a task. |
| MemoryOptimizedReadMultiSamplePortInt32(int, ref int[], ReallocationPolicy, out int) | Reads one or more 32-bit integer samples from a single DIChannel in a task. |
| MemoryOptimizedReadMultiSamplePortUInt16(int, ref ushort[], ReallocationPolicy, out int) | Reads one or more 16-bit unsigned integer samples from a single DIChannel in a task. |
| MemoryOptimizedReadMultiSamplePortUInt16(int, ref ushort[], out int) | Reads one or more 16-bit unsigned integer samples from a single DIChannel in a task. |
| MemoryOptimizedReadMultiSamplePortUInt32(int, ref uint[], ReallocationPolicy, out int) | Reads one or more 32-bit unsigned integer samples from a single DIChannel in a task. |
| MemoryOptimizedReadMultiSamplePortUInt32(int, ref uint[], out int) | Reads one or more 32-bit unsigned integer samples from a single DIChannel in a task. |
| MemoryOptimizedReadSingleSampleMultiLine(bool[]) | Reads a single Boolean sample from a single DIChannel in a task. The channel can contain multiple digital lines. |
| ReadMultiSamplePortByte(int) | Reads one or more 8-bit unsigned integer samples from a single DIChannel in a task. |
| ReadMultiSamplePortInt16(int) | Reads one or more 16-bit integer samples from a single DIChannel in a task. |
| ReadMultiSamplePortInt32(int) | Reads one or more 32-bit integer samples from a single DIChannel in a task. |
| ReadMultiSamplePortUInt16(int) | Reads one or more 16-bit unsigned integer samples from a single DIChannel in a task. |
| ReadMultiSamplePortUInt32(int) | Reads one or more 32-bit unsigned integer samples from a single DIChannel in a task. |
| ReadSingleSampleMultiLine() | Reads a single Boolean sample from a single DIChannel in a task. The channel can contain multiple digital lines. |
| ReadSingleSamplePortByte() | Reads a single 8-bit unsigned integer sample from a single DIChannel in a task. |
| ReadSingleSamplePortInt16() | Reads a single 16-bit integer sample from a single DIChannel in a task. |
| ReadSingleSamplePortInt32() | Reads a single 32-bit integer sample from a single DIChannel in a task. |
| ReadSingleSamplePortUInt16() | Reads a single 16-bit unsigned integer sample from a single DIChannel in a task. |
| ReadSingleSamplePortUInt32() | Reads a single 32-bit unsigned integer sample from a single DIChannel in a task. |
| ReadSingleSampleSingleLine() | Reads a single Boolean sample from a single DIChannel in a task. The task can contain only a single digital line. |
| ReadWaveform(int) | Reads one or more digital waveform samples from a single DIChannel in a task. |
| ReadWaveform(TimeSpan) | Reads one or more digital waveform samples from a single DIChannel in a task for a specified duration . |
| ToString() | Returns a string representation of the object. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritemultisampleport__bool-byte_arr1-asynccallback-object.html language=enus -->
## TOPIC 02025: BeginWriteMultiSamplePort(bool, byte[], AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritemultisampleport__bool-byte_arr1-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritemultisampleport__bool-byte_arr1-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of one or more 8-bit unsigned integer samples to a single DOChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, byte[] data, AsyncCallback callback, object state)RemarksP

### BeginWriteMultiSamplePort(bool, byte[], AsyncCallback, object)

Begins an asynchronous write of one or more 8-bit unsigned integer samples to a single [DOChannel](nationalinstruments-daqmx-dochannel.html) in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, byte[] data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-digitalsinglechannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

Use this method for devices with up to eight lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | byte[] | A 1D array of samples to write to the task. Each element of the array corresponds to a sample to write to the channel. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritemultisampleport__bool-int_arr1-asynccallback-object.html language=enus -->
## TOPIC 02026: BeginWriteMultiSamplePort(bool, int[], AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritemultisampleport__bool-int_arr1-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritemultisampleport__bool-int_arr1-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of one or more 32-bit integer samples to a single DOChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, int[] data, AsyncCallback callback, object state)RemarksPass the r

### BeginWriteMultiSamplePort(bool, int[], AsyncCallback, object)

Begins an asynchronous write of one or more 32-bit integer samples to a single [DOChannel](nationalinstruments-daqmx-dochannel.html) in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, int[] data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-digitalsinglechannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

Use this method for devices with up to 32 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | int[] | A 1D array of samples to write to the task. Each element of the array corresponds to a sample to write to the channel. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritemultisampleport__bool-short_arr1-asynccallback-object.html language=enus -->
## TOPIC 02027: BeginWriteMultiSamplePort(bool, short[], AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritemultisampleport__bool-short_arr1-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritemultisampleport__bool-short_arr1-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of one or more 32-bit integer samples to a single DOChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, short[] data, AsyncCallback callback, object state)RemarksPass the

### BeginWriteMultiSamplePort(bool, short[], AsyncCallback, object)

Begins an asynchronous write of one or more 32-bit integer samples to a single [DOChannel](nationalinstruments-daqmx-dochannel.html) in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, short[] data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-digitalsinglechannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

Use this method for devices with up to 32 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | short[] | A 1D array of samples to write to the task. Each element of the array corresponds to a sample to write to the channel. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritemultisampleport__bool-uint_arr1-asynccallback-object.html language=enus -->
## TOPIC 02028: BeginWriteMultiSamplePort(bool, uint[], AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritemultisampleport__bool-uint_arr1-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritemultisampleport__bool-uint_arr1-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of one or more 32-bit unsigned integer samples to a single DOChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, uint[] data, AsyncCallback callback, object state)Remarks

### BeginWriteMultiSamplePort(bool, uint[], AsyncCallback, object)

Begins an asynchronous write of one or more 32-bit unsigned integer samples to a single [DOChannel](nationalinstruments-daqmx-dochannel.html) in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, uint[] data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-digitalsinglechannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

Use this method for devices with up to 32 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | uint[] | A 1D array of samples to write to the task. Each element of the array corresponds to a sample to write to the channel. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritemultisampleport__bool-ushort_arr1-asynccallback-object.html language=enus -->
## TOPIC 02029: BeginWriteMultiSamplePort(bool, ushort[], AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritemultisampleport__bool-ushort_arr1-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritemultisampleport__bool-ushort_arr1-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of one or more 16-bit unsigned integer samples to a single DOChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, ushort[] data, AsyncCallback callback, object state)Remar

### BeginWriteMultiSamplePort(bool, ushort[], AsyncCallback, object)

Begins an asynchronous write of one or more 16-bit unsigned integer samples to a single [DOChannel](nationalinstruments-daqmx-dochannel.html) in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, ushort[] data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-digitalsinglechannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

Use this method for devices with up to 16 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | ushort[] | A 1D array of samples to write to the task. Each element of the array corresponds to a sample to write to the channel. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritesinglesamplemultiline__bool-bool_arr1-asynccallback-object.html language=enus -->
## TOPIC 02030: BeginWriteSingleSampleMultiLine(bool, bool[], AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritesinglesamplemultiline__bool-bool_arr1-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritesinglesamplemultiline__bool-bool_arr1-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of a single Boolean sample to a single DOChannel in a task. The channel can contain multiple digital lines. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteSingleSampleMultiLine([MarshalAs(UnmanagedType.U1)] bool autoStart, bool[] data, AsyncCallb

### BeginWriteSingleSampleMultiLine(bool, bool[], AsyncCallback, object)

Begins an asynchronous write of a single Boolean sample to a single [DOChannel](nationalinstruments-daqmx-dochannel.html) in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx). The channel can contain multiple digital lines.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteSingleSampleMultiLine([MarshalAs(UnmanagedType.U1)] bool autoStart, bool[] data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-digitalsinglechannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | bool[] | A 1D array of samples to write to the task. Each element of the array corresponds to a digital line within the channel. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritesinglesampleport__bool-byte-asynccallback-object.html language=enus -->
## TOPIC 02031: BeginWriteSingleSamplePort(bool, byte, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritesinglesampleport__bool-byte-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritesinglesampleport__bool-byte-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of a single 8-bit unsigned integer sample to a single DOChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, byte data, AsyncCallback callback, object state)RemarksPass t

### BeginWriteSingleSamplePort(bool, byte, AsyncCallback, object)

Begins an asynchronous write of a single 8-bit unsigned integer sample to a single [DOChannel](nationalinstruments-daqmx-dochannel.html) in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, byte data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-digitalsinglechannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | byte | A sample to write to the task. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritesinglesampleport__bool-int-asynccallback-object.html language=enus -->
## TOPIC 02032: BeginWriteSingleSamplePort(bool, int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritesinglesampleport__bool-int-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritesinglesampleport__bool-int-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of a single 32-bit integer sample to a single DOChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, int data, AsyncCallback callback, object state)RemarksPass the return

### BeginWriteSingleSamplePort(bool, int, AsyncCallback, object)

Begins an asynchronous write of a single 32-bit integer sample to a single [DOChannel](nationalinstruments-daqmx-dochannel.html) in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, int data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-digitalsinglechannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | int | A sample to write to the task. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritesinglesampleport__bool-short-asynccallback-object.html language=enus -->
## TOPIC 02033: BeginWriteSingleSamplePort(bool, short, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritesinglesampleport__bool-short-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritesinglesampleport__bool-short-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of a single 16-bit integer sample to a single DOChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, short data, AsyncCallback callback, object state)RemarksPass the retu

### BeginWriteSingleSamplePort(bool, short, AsyncCallback, object)

Begins an asynchronous write of a single 16-bit integer sample to a single [DOChannel](nationalinstruments-daqmx-dochannel.html) in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, short data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-digitalsinglechannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | short | A sample to write to the task. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritesinglesampleport__bool-uint-asynccallback-object.html language=enus -->
## TOPIC 02034: BeginWriteSingleSamplePort(bool, uint, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritesinglesampleport__bool-uint-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritesinglesampleport__bool-uint-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of a single 32-bit unsigned integer sample to a single DOChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, uint data, AsyncCallback callback, object state)RemarksPass

### BeginWriteSingleSamplePort(bool, uint, AsyncCallback, object)

Begins an asynchronous write of a single 32-bit unsigned integer sample to a single [DOChannel](nationalinstruments-daqmx-dochannel.html) in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, uint data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-digitalsinglechannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | uint | A sample to write to the task. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritesinglesampleport__bool-ushort-asynccallback-object.html language=enus -->
## TOPIC 02035: BeginWriteSingleSamplePort(bool, ushort, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritesinglesampleport__bool-ushort-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritesinglesampleport__bool-ushort-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of a single 16-bit unsigned integer sample to a single DOChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, ushort data, AsyncCallback callback, object state)RemarksPas

### BeginWriteSingleSamplePort(bool, ushort, AsyncCallback, object)

Begins an asynchronous write of a single 16-bit unsigned integer sample to a single [DOChannel](nationalinstruments-daqmx-dochannel.html) in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, ushort data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-digitalsinglechannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | ushort | A sample to write to the task. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritesinglesamplesingleline__bool-bool-asynccallback-object.html language=enus -->
## TOPIC 02036: BeginWriteSingleSampleSingleLine(bool, bool, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritesinglesamplesingleline__bool-bool-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritesinglesamplesingleline__bool-bool-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of a single Boolean sample to a single digital line in a task. The task can contain only a single digital line. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteSingleSampleSingleLine([MarshalAs(UnmanagedType.U1)] bool autoStart, [MarshalAs(Unmanag

### BeginWriteSingleSampleSingleLine(bool, bool, AsyncCallback, object)

Begins an asynchronous write of a single Boolean sample to a single digital line in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx). The task can contain only a single digital line.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteSingleSampleSingleLine([MarshalAs(UnmanagedType.U1)] bool autoStart, [MarshalAs(UnmanagedType.U1)] bool data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-digitalsinglechannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | bool | A Boolean sample to write to the task. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritewaveform__bool-digitalwaveform-asynccallback-object.html language=enus -->
## TOPIC 02037: BeginWriteWaveform(bool, DigitalWaveform, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritewaveform__bool-digitalwaveform-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritewaveform__bool-digitalwaveform-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of one or more digital waveform samples to a single DOChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteWaveform([MarshalAs(UnmanagedType.U1)] bool autoStart, DigitalWaveform data, AsyncCallback callback, object state)RemarksPass

### BeginWriteWaveform(bool, DigitalWaveform, AsyncCallback, object)

Begins an asynchronous write of one or more digital waveform samples to a single [DOChannel](nationalinstruments-daqmx-dochannel.html) in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteWaveform([MarshalAs(UnmanagedType.U1)] bool autoStart, DigitalWaveform data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-digitalsinglechannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

Digital waveform writes are not affected by the WaveformTiming.SampleInterval or WaveformTiming.StartTime properties on the DigitalWaveform. To configure timing for digital waveform writes, use the Overload:NationalInstruments.DAQmx.Timing.ConfigureSampleClock method.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | DigitalWaveform | A DigitalWaveform to write to the task. The order of the lines in the digital waveform corresponds to the order in which you add the lines to the channel. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelwriter-digitalsinglechannelwriter__daqstream.html language=enus -->
## TOPIC 02038: DigitalSingleChannelWriter(DaqStream)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelwriter-digitalsinglechannelwriter__daqstream.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelwriter-digitalsinglechannelwriter__daqstream.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of the DigitalSingleChannelWriter class to write to the specified DaqStream. SyntaxNamespace: NationalInstruments.DAQmxpublic DigitalSingleChannelWriter(DaqStream stream)RemarksEach Task object contains a Stream property that serves as the connection point for writers to provi

### DigitalSingleChannelWriter(DaqStream)

Creates a new instance of the [DigitalSingleChannelWriter](nationalinstruments-daqmx-digitalsinglechannelwriter.html) class to write to the specified [DaqStream](nationalinstruments-daqmx-daqstream.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public DigitalSingleChannelWriter(DaqStream stream)

#### Remarks

Each [Task](nationalinstruments-daqmx-task.html) object contains a [Stream](nationalinstruments-daqmx-task-stream.html) property that serves as the connection point for writers to provide samples to be generated by that task.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| stream | DaqStream | The DaqStream to write to. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelwriter-endwrite__iasyncresult.html language=enus -->
## TOPIC 02039: EndWrite(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelwriter-endwrite__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelwriter-endwrite__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous write initiated with BeginWriteMultiSamplePort(bool, uint[], AsyncCallback, object), BeginWriteSingleSamplePort(bool, uint, AsyncCallback, object), BeginWriteSingleSampleMultiLine(bool, bool[], AsyncCallback, object), BeginWriteSingleSampleSingleLine(bool, bool, As

### EndWrite(IAsyncResult)

Handles the end of an asynchronous write initiated with [BeginWriteMultiSamplePort(bool, uint[], AsyncCallback, object)](nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritemultisampleport__bool-uint_arr1-asynccallback-object.html), [BeginWriteSingleSamplePort(bool, uint, AsyncCallback, object)](nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritesinglesampleport__bool-uint-asynccallback-object.html), [BeginWriteSingleSampleMultiLine(bool, bool[], AsyncCallback, object)](nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritesinglesamplemultiline__bool-bool_arr1-asynccallback-object.html), [BeginWriteSingleSampleSingleLine(bool, bool, AsyncCallback, object)](nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritesinglesamplesingleline__bool-bool-asynccallback-object.html), or [BeginWriteWaveform(bool, DigitalWaveform, AsyncCallback, object)](nationalinstruments-daqmx-digitalsinglechannelwriter-beginwritewaveform__bool-digitalwaveform-asynccallback-object.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void EndWrite(IAsyncResult asyncResult)

#### Remarks

If you call EndWrite(IAsyncResult) before the asynchronous write represented by the provided IAsyncResult is complete, EndWrite(IAsyncResult) waits for the write to complete before returning. For a write to a buffered task, the write is considered complete when all of the written samples have been transferred to the task buffer. Use [IsDone](nationalinstruments-daqmx-task-isdone.html) or [WaitUntilDone(int)](nationalinstruments-daqmx-task-waituntildone__int.html) on the [Task](nationalinstruments-daqmx-task.html) object to determine if a task has generated all of the data it was configured to generate.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginWriteMultiSamplePort(bool, uint[], AsyncCallback, object), BeginWriteSingleSamplePort(bool, uint, AsyncCallback, object), BeginWriteSingleSampleMultiLine(bool, bool[], AsyncCallback, object), BeginWriteSingleSampleSingleLine(bool, bool, AsyncCallback, object), or BeginWriteWaveform(bool, DigitalWaveform, AsyncCallback, object). |

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginWriteMultiSamplePort(bool, uint[], AsyncCallback, object), BeginWriteSingleSamplePort(bool, uint, AsyncCallback, object), BeginWriteSingleSampleMultiLine(bool, bool[], AsyncCallback, object), BeginWriteSingleSampleSingleLine(bool, bool, AsyncCallback, object), or BeginWriteWaveform(bool, DigitalWaveform, AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| IndexOutOfRangeException | The data passed to BeginWriteMultiSamplePort(bool, uint[], AsyncCallback, object) or BeginWriteSingleSampleMultiLine(bool, bool[], AsyncCallback, object) had a non-zero lower bound. |

Parent topic:

DigitalSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelwriter-synchronizecallbacks.html language=enus -->
## TOPIC 02040: SynchronizeCallbacks

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelwriter-synchronizecallbacks.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelwriter-synchronizecallbacks.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how events and callback delegates are invoked. SyntaxNamespace: NationalInstruments.DAQmxpublic bool SynchronizeCallbacks { get; set; }RemarksIn some cases, callbacks and event handlers are executed in a different thread than the rest of the program. Therefore, you must take special care w

### SynchronizeCallbacks

Specifies how events and callback delegates are invoked.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool SynchronizeCallbacks { get; set; }

#### Remarks

In some cases, callbacks and event handlers are executed in a different thread than the rest of the program. Therefore, you must take special care when accessing objects that have thread affinity, such as UI controls, from these callbacks and event handlers. For more information, refer to Events, Callbacks, and Thread Safety in Measurement Studio .NET Class Libraries.

Reading and Writing with NI-DAQmx Streams

Parent topic:

DigitalSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelwriter-synchronizingobject.html language=enus -->
## TOPIC 02041: SynchronizingObject

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelwriter-synchronizingobject.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelwriter-synchronizingobject.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: Use SynchronizeCallbacks to specify that the object marshals callbacks across threads appropriately. Will warn if used Gets or sets the object that marshals event-handler and callback calls. SyntaxNamespace: NationalInstruments.DAQmxpublic ISynchronizeInvoke SynchronizingObject { get; set;

### SynchronizingObject

**Obsolete: Use SynchronizeCallbacks to specify that the object marshals callbacks across threads appropriately. Will warn if used** 
Gets or sets the object that marshals event-handler and callback calls.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public ISynchronizeInvoke SynchronizingObject { get; set; }

#### Remarks

The ISynchronizeInvoke representing the object that marshals the event-handler and callback calls. The default value is null.

null

Note

For more information, refer to Events, Callbacks, and Thread Safety in Measurement Studio .NET Class Libraries.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelwriter-tostring.html language=enus -->
## TOPIC 02042: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelwriter-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelwriter-tostring.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the object. SyntaxNamespace: NationalInstruments.DAQmxpublic override string ToString()RemarksOverrides ToString. ReturnsA string representation of the object.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ToString()

Returns a string representation of the object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override string ToString()

#### Remarks

Overrides ToString.

#### Returns

A string representation of the object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelwriter-writemultisampleport__bool-byte_arr1.html language=enus -->
## TOPIC 02043: WriteMultiSamplePort(bool, byte[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelwriter-writemultisampleport__bool-byte_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelwriter-writemultisampleport__bool-byte_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more 8-bit unsigned integer samples to a single DOChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, byte[] data)RemarksUse this method for devices with up to eight lines per port. If the task uses

### WriteMultiSamplePort(bool, byte[])

Writes one or more 8-bit unsigned integer samples to a single [DOChannel](nationalinstruments-daqmx-dochannel.html) in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, byte[] data)

#### Remarks

Use this method for devices with up to eight lines per port. If the task uses on-demand timing, this method returns only after the device generates all samples. If the task uses any timing type other than on-demand, this method returns immediately and does not wait for the device to generate all samples. Your application must call the [WaitUntilDone](nationalinstruments-daqmx-task-waituntildone__int.html) method to block until the device has generated all samples.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | byte[] | A 1D array of samples to write to the task. Each element of the array corresponds to a channel in the task. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

Parent topic:

DigitalSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelwriter-writemultisampleport__bool-int_arr1.html language=enus -->
## TOPIC 02044: WriteMultiSamplePort(bool, int[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelwriter-writemultisampleport__bool-int_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelwriter-writemultisampleport__bool-int_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more 32-bit integer samples to a single DOChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, int[] data)RemarksUse this method for devices with up to 32 lines per port. If the task uses on-demand t

### WriteMultiSamplePort(bool, int[])

Writes one or more 32-bit integer samples to a single [DOChannel](nationalinstruments-daqmx-dochannel.html) in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, int[] data)

#### Remarks

Use this method for devices with up to 32 lines per port. If the task uses on-demand timing, this method returns only after the device generates all samples. If the task uses any timing type other than on-demand, this method returns immediately and does not wait for the device to generate all samples. Your application must call the [WaitUntilDone](nationalinstruments-daqmx-task-waituntildone__int.html) method to block until the device has generated all samples.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | int[] | A 1D array of samples to write to the task. Each element of the array corresponds to a channel in the task. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

Parent topic:

DigitalSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelwriter-writemultisampleport__bool-short_arr1.html language=enus -->
## TOPIC 02045: WriteMultiSamplePort(bool, short[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelwriter-writemultisampleport__bool-short_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelwriter-writemultisampleport__bool-short_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more 16-bit integer samples to a single DOChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, short[] data)RemarksUse this method for devices with up to 16 lines per port. If the task uses on-demand

### WriteMultiSamplePort(bool, short[])

Writes one or more 16-bit integer samples to a single [DOChannel](nationalinstruments-daqmx-dochannel.html) in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, short[] data)

#### Remarks

Use this method for devices with up to 16 lines per port. If the task uses on-demand timing, this method returns only after the device generates all samples. If the task uses any timing type other than on-demand, this method returns immediately and does not wait for the device to generate all samples. Your application must call the [WaitUntilDone](nationalinstruments-daqmx-task-waituntildone__int.html) method to block until the device has generated all samples.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | short[] | A 1D array of samples to write to the task. Each element of the array corresponds to a channel in the task. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

Parent topic:

DigitalSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelwriter-writemultisampleport__bool-uint_arr1.html language=enus -->
## TOPIC 02046: WriteMultiSamplePort(bool, uint[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelwriter-writemultisampleport__bool-uint_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelwriter-writemultisampleport__bool-uint_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more 32-bit unsigned integer samples to a single DOChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, uint[] data)RemarksUse this method for devices with up to 32 lines per port. If the task uses o

### WriteMultiSamplePort(bool, uint[])

Writes one or more 32-bit unsigned integer samples to a single [DOChannel](nationalinstruments-daqmx-dochannel.html) in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, uint[] data)

#### Remarks

Use this method for devices with up to 32 lines per port. If the task uses on-demand timing, this method returns only after the device generates all samples. If the task uses any timing type other than on-demand, this method returns immediately and does not wait for the device to generate all samples. Your application must call the [WaitUntilDone](nationalinstruments-daqmx-task-waituntildone__int.html) method to block until the device has generated all samples.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | uint[] | A 1D array of samples to write to the task. Each element of the array corresponds to a channel in the task. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

Parent topic:

DigitalSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelwriter-writemultisampleport__bool-ushort_arr1.html language=enus -->
## TOPIC 02047: WriteMultiSamplePort(bool, ushort[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelwriter-writemultisampleport__bool-ushort_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelwriter-writemultisampleport__bool-ushort_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more 16-bit unsigned integer samples to a single DOChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, ushort[] data)RemarksUse this method for devices with up to 16 lines per port. If the task uses

### WriteMultiSamplePort(bool, ushort[])

Writes one or more 16-bit unsigned integer samples to a single [DOChannel](nationalinstruments-daqmx-dochannel.html) in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, ushort[] data)

#### Remarks

Use this method for devices with up to 16 lines per port. If the task uses on-demand timing, this method returns only after the device generates all samples. If the task uses any timing type other than on-demand, this method returns immediately and does not wait for the device to generate all samples. Your application must call the [WaitUntilDone](nationalinstruments-daqmx-task-waituntildone__int.html) method to block until the device has generated all samples.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | ushort[] | A 1D array of samples to write to the task. Each element of the array corresponds to a channel in the task. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

Parent topic:

DigitalSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelwriter-writesinglesamplemultiline__bool-bool_arr1.html language=enus -->
## TOPIC 02048: WriteSingleSampleMultiLine(bool, bool[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelwriter-writesinglesamplemultiline__bool-bool_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelwriter-writesinglesamplemultiline__bool-bool_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a single Boolean sample to a single DOChannel in a task. The channel can contain multiple digital lines. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteSingleSampleMultiLine([MarshalAs(UnmanagedType.U1)] bool autoStart, bool[] data)RemarksNI-DAQmx read and write methods time out a

### WriteSingleSampleMultiLine(bool, bool[])

Writes a single Boolean sample to a single [DOChannel](nationalinstruments-daqmx-dochannel.html) in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx). The channel can contain multiple digital lines.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteSingleSampleMultiLine([MarshalAs(UnmanagedType.U1)] bool autoStart, bool[] data)

#### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | bool[] | A 1D array of samples to write to the task. Each element of the array corresponds to a digital line within the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

Parent topic:

DigitalSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelwriter-writesinglesampleport__bool-byte.html language=enus -->
## TOPIC 02049: WriteSingleSamplePort(bool, byte)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelwriter-writesinglesampleport__bool-byte.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelwriter-writesinglesampleport__bool-byte.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a single 8-bit unsigned integer sample to a single DOChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, byte data)RemarksUse this method for devices with up to eight lines per port. If the task uses on-d

### WriteSingleSamplePort(bool, byte)

Writes a single 8-bit unsigned integer sample to a single [DOChannel](nationalinstruments-daqmx-dochannel.html) in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, byte data)

#### Remarks

Use this method for devices with up to eight lines per port. If the task uses on-demand timing, this method returns only after the device generates all samples. If the task uses any timing type other than on-demand, this method returns immediately and does not wait for the device to generate all samples. Your application must call the [WaitUntilDone](nationalinstruments-daqmx-task-waituntildone__int.html) method to block until the device has generated all samples.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | byte | A sample to write to the task. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelwriter-writesinglesampleport__bool-int.html language=enus -->
## TOPIC 02050: WriteSingleSamplePort(bool, int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelwriter-writesinglesampleport__bool-int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelwriter-writesinglesampleport__bool-int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a single 32-bit integer sample to a single DOChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, int data)RemarksUse this method for devices with up to 32 lines per port. If the task uses on-demand timing

### WriteSingleSamplePort(bool, int)

Writes a single 32-bit integer sample to a single [DOChannel](nationalinstruments-daqmx-dochannel.html) in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, int data)

#### Remarks

Use this method for devices with up to 32 lines per port. If the task uses on-demand timing, this method returns only after the device generates all samples. If the task uses any timing type other than on-demand, this method returns immediately and does not wait for the device to generate all samples. Your application must call the [WaitUntilDone](nationalinstruments-daqmx-task-waituntildone__int.html) method to block until the device has generated all samples.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | int | A sample to write to the task. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelwriter-writesinglesampleport__bool-short.html language=enus -->
## TOPIC 02051: WriteSingleSamplePort(bool, short)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelwriter-writesinglesampleport__bool-short.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelwriter-writesinglesampleport__bool-short.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a single 16-bit integer sample to a single DOChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, short data)RemarksUse this method for devices with up to 16 lines per port. If the task uses on-demand timi

### WriteSingleSamplePort(bool, short)

Writes a single 16-bit integer sample to a single [DOChannel](nationalinstruments-daqmx-dochannel.html) in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, short data)

#### Remarks

Use this method for devices with up to 16 lines per port. If the task uses on-demand timing, this method returns only after the device generates all samples. If the task uses any timing type other than on-demand, this method returns immediately and does not wait for the device to generate all samples. Your application must call the [WaitUntilDone](nationalinstruments-daqmx-task-waituntildone__int.html) method to block until the device has generated all samples.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | short | A sample to write to the task. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelwriter-writesinglesampleport__bool-uint.html language=enus -->
## TOPIC 02052: WriteSingleSamplePort(bool, uint)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelwriter-writesinglesampleport__bool-uint.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelwriter-writesinglesampleport__bool-uint.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a single 32-bit unsigned integer sample to a single DOChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, uint data)RemarksUse this method for devices with up to 32 lines per port. If the task uses on-dem

### WriteSingleSamplePort(bool, uint)

Writes a single 32-bit unsigned integer sample to a single [DOChannel](nationalinstruments-daqmx-dochannel.html) in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, uint data)

#### Remarks

Use this method for devices with up to 32 lines per port. If the task uses on-demand timing, this method returns only after the device generates all samples. If the task uses any timing type other than on-demand, this method returns immediately and does not wait for the device to generate all samples. Your application must call the [WaitUntilDone](nationalinstruments-daqmx-task-waituntildone__int.html) method to block until the device has generated all samples.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | uint | A sample to write to the task. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelwriter-writesinglesampleport__bool-ushort.html language=enus -->
## TOPIC 02053: WriteSingleSamplePort(bool, ushort)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelwriter-writesinglesampleport__bool-ushort.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelwriter-writesinglesampleport__bool-ushort.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a single 16-bit unsigned integer sample to a single DOChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, ushort data)RemarksUse this method for devices with up to 16 lines per port. If the task uses on-d

### WriteSingleSamplePort(bool, ushort)

Writes a single 16-bit unsigned integer sample to a single [DOChannel](nationalinstruments-daqmx-dochannel.html) in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, ushort data)

#### Remarks

Use this method for devices with up to 16 lines per port. If the task uses on-demand timing, this method returns only after the device generates all samples. If the task uses any timing type other than on-demand, this method returns immediately and does not wait for the device to generate all samples. Your application must call the [WaitUntilDone](nationalinstruments-daqmx-task-waituntildone__int.html) method to block until the device has generated all samples.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | ushort | A sample to write to the task. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelwriter-writesinglesamplesingleline__bool-bool.html language=enus -->
## TOPIC 02054: WriteSingleSampleSingleLine(bool, bool)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelwriter-writesinglesamplesingleline__bool-bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelwriter-writesinglesamplesingleline__bool-bool.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a single Boolean sample to a single digital line in a task. The task can contain only a single digital line. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteSingleSampleSingleLine([MarshalAs(UnmanagedType.U1)] bool autoStart, [MarshalAs(UnmanagedType.U1)] bool data)RemarksNI-DAQmx

### WriteSingleSampleSingleLine(bool, bool)

Writes a single Boolean sample to a single digital line in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx). The task can contain only a single digital line.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteSingleSampleSingleLine([MarshalAs(UnmanagedType.U1)] bool autoStart, [MarshalAs(UnmanagedType.U1)] bool data)

#### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | bool | A Boolean sample to write to the task. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelwriter-writewaveform__bool-digitalwaveform.html language=enus -->
## TOPIC 02055: WriteWaveform(bool, DigitalWaveform)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelwriter-writewaveform__bool-digitalwaveform.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelwriter-writewaveform__bool-digitalwaveform.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more digital waveform samples to a single DOChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteWaveform([MarshalAs(UnmanagedType.U1)] bool autoStart, DigitalWaveform data)RemarksIf the task uses on-demand timing, this method returns only after the device gene

### WriteWaveform(bool, DigitalWaveform)

Writes one or more digital waveform samples to a single [DOChannel](nationalinstruments-daqmx-dochannel.html) in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteWaveform([MarshalAs(UnmanagedType.U1)] bool autoStart, DigitalWaveform data)

#### Remarks

If the task uses on-demand timing, this method returns only after the device generates all samples. If the task uses any timing type other than on-demand, this method returns immediately and does not wait for the device to generate all samples. Your application must call the [WaitUntilDone](nationalinstruments-daqmx-task-waituntildone__int.html) method to block until the device has generated all samples.

Digital waveform writes are not affected by the WaveformTiming.SampleInterval or WaveformTiming.StartTime properties on the DigitalWaveform. To configure timing for digital waveform writes, use the Overload:NationalInstruments.DAQmx.Timing.ConfigureSampleClock method.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | DigitalWaveform | A DigitalWaveform to write to the task. The order of the lines in the digital waveform corresponds to the order in which you add the lines to the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

Parent topic:

DigitalSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelwriter.html language=enus -->
## TOPIC 02056: DigitalSingleChannelWriter Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelwriter.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelwriter.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains methods for writing samples to the digital output channel in a task. Derives fromMarshalByRefObjectISynchronizeCallbacksISupportSynchronizationContextSyntaxNamespace: NationalInstruments.DAQmxpublic class DigitalSingleChannelWriter : MarshalByRefObject, ISynchronizeCallbacks, ISupportSynchr

### DigitalSingleChannelWriter Class

Contains methods for writing samples to the digital output channel in a task.

#### Derives from

- MarshalByRefObject
- ISynchronizeCallbacks
- ISupportSynchronizationContext

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class DigitalSingleChannelWriter : MarshalByRefObject, ISynchronizeCallbacks, ISupportSynchronizationContext

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| DigitalSingleChannelWriter(DaqStream) | Creates a new instance of the DigitalSingleChannelWriter class to write to the specified DaqStream. |

#### Properties

| Name | Description |
| --- | --- |
| SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |
| SynchronizingObject | Obsolete: Use SynchronizeCallbacks to specify that the object marshals callbacks across threads appropriately. Will warn if usedGets or sets the object that marshals event-handler and callback calls. |

#### Methods

| Name | Description |
| --- | --- |
| BeginWriteMultiSamplePort(bool, int[], AsyncCallback, object) | Begins an asynchronous write of one or more 32-bit integer samples to a single DOChannel in a task. |
| BeginWriteMultiSamplePort(bool, ushort[], AsyncCallback, object) | Begins an asynchronous write of one or more 16-bit unsigned integer samples to a single DOChannel in a task. |
| BeginWriteMultiSamplePort(bool, short[], AsyncCallback, object) | Begins an asynchronous write of one or more 32-bit integer samples to a single DOChannel in a task. |
| BeginWriteMultiSamplePort(bool, byte[], AsyncCallback, object) | Begins an asynchronous write of one or more 8-bit unsigned integer samples to a single DOChannel in a task. |
| BeginWriteMultiSamplePort(bool, uint[], AsyncCallback, object) | Begins an asynchronous write of one or more 32-bit unsigned integer samples to a single DOChannel in a task. |
| BeginWriteSingleSampleMultiLine(bool, bool[], AsyncCallback, object) | Begins an asynchronous write of a single Boolean sample to a single DOChannel in a task. The channel can contain multiple digital lines. |
| BeginWriteSingleSamplePort(bool, ushort, AsyncCallback, object) | Begins an asynchronous write of a single 16-bit unsigned integer sample to a single DOChannel in a task. |
| BeginWriteSingleSamplePort(bool, short, AsyncCallback, object) | Begins an asynchronous write of a single 16-bit integer sample to a single DOChannel in a task. |
| BeginWriteSingleSamplePort(bool, int, AsyncCallback, object) | Begins an asynchronous write of a single 32-bit integer sample to a single DOChannel in a task. |
| BeginWriteSingleSamplePort(bool, byte, AsyncCallback, object) | Begins an asynchronous write of a single 8-bit unsigned integer sample to a single DOChannel in a task. |
| BeginWriteSingleSamplePort(bool, uint, AsyncCallback, object) | Begins an asynchronous write of a single 32-bit unsigned integer sample to a single DOChannel in a task. |
| BeginWriteSingleSampleSingleLine(bool, bool, AsyncCallback, object) | Begins an asynchronous write of a single Boolean sample to a single digital line in a task. The task can contain only a single digital line. |
| BeginWriteWaveform(bool, DigitalWaveform, AsyncCallback, object) | Begins an asynchronous write of one or more digital waveform samples to a single DOChannel in a task. |
| EndWrite(IAsyncResult) | Handles the end of an asynchronous write initiated with BeginWriteMultiSamplePort(bool, uint[], AsyncCallback, object), BeginWriteSingleSamplePort(bool, uint, AsyncCallback, object), BeginWriteSingleSampleMultiLine(bool, bool[], AsyncCallback, object), BeginWriteSingleSampleSingleLine(bool, bool, AsyncCallback, object), or BeginWriteWaveform(bool, DigitalWaveform, AsyncCallback, object). |
| ToString() | Returns a string representation of the object. |
| WriteMultiSamplePort(bool, short[]) | Writes one or more 16-bit integer samples to a single DOChannel in a task. |
| WriteMultiSamplePort(bool, byte[]) | Writes one or more 8-bit unsigned integer samples to a single DOChannel in a task. |
| WriteMultiSamplePort(bool, uint[]) | Writes one or more 32-bit unsigned integer samples to a single DOChannel in a task. |
| WriteMultiSamplePort(bool, int[]) | Writes one or more 32-bit integer samples to a single DOChannel in a task. |
| WriteMultiSamplePort(bool, ushort[]) | Writes one or more 16-bit unsigned integer samples to a single DOChannel in a task. |
| WriteSingleSampleMultiLine(bool, bool[]) | Writes a single Boolean sample to a single DOChannel in a task. The channel can contain multiple digital lines. |
| WriteSingleSamplePort(bool, byte) | Writes a single 8-bit unsigned integer sample to a single DOChannel in a task. |
| WriteSingleSamplePort(bool, short) | Writes a single 16-bit integer sample to a single DOChannel in a task. |
| WriteSingleSamplePort(bool, uint) | Writes a single 32-bit unsigned integer sample to a single DOChannel in a task. |
| WriteSingleSamplePort(bool, int) | Writes a single 32-bit integer sample to a single DOChannel in a task. |
| WriteSingleSamplePort(bool, ushort) | Writes a single 16-bit unsigned integer sample to a single DOChannel in a task. |
| WriteSingleSampleSingleLine(bool, bool) | Writes a single Boolean sample to a single digital line in a task. The task can contain only a single digital line. |
| WriteWaveform(bool, DigitalWaveform) | Writes one or more digital waveform samples to a single DOChannel in a task. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digportlogicfamily.html language=enus -->
## TOPIC 02057: DigPortLogicFamily Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digportlogicfamily.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digportlogicfamily.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the digital port logic family to use for acquisition and generation. A logic family corresponds to voltage thresholds that are compatible with a group of voltage standards. Refer to the device documentation for information on the logic high and logic low voltages for these logic families.

### DigPortLogicFamily Enumeration

Specifies the digital port logic family to use for acquisition and generation. A logic family corresponds to voltage thresholds that are compatible with a group of voltage standards. Refer to the device documentation for information on the logic high and logic low voltages for these logic families.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum DigPortLogicFamily

#### Remarks

Specifies the digital port logic family to use for acquisition and generation. A logic family corresponds to voltage thresholds that are compatible with a group of voltage standards. Refer to the device documentation for information on the logic high and logic low voltages for these logic families. Use this enumeration to get or set the value of [DigPortLogicFamily](nationalinstruments-daqmx-physicalchannel-digportlogicfamily.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| OnePointEightVolts | 16184 | Compatible with 1.8 V CMOS signals. |
| TwoPointFiveVolts | 14620 | Compatible with 2.5 V CMOS signals. |
| ThreePointThreeVolts | 14621 | Compatible with LVTTL signals. |
| FiveVolts | 14619 | Compatible with TTL and 5 V CMOS signals. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dilogicfamily.html language=enus -->
## TOPIC 02058: DILogicFamily Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dilogicfamily.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dilogicfamily.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic family to use for acquisition. A logic family corresponds to voltage thresholds that are compatible with a group of voltage standards. Refer to the device documentation for information on the logic high and logic low voltages for these logic families. SyntaxNamespace: NationalIns

### DILogicFamily Enumeration

Specifies the logic family to use for acquisition. A logic family corresponds to voltage thresholds that are compatible with a group of voltage standards. Refer to the device documentation for information on the logic high and logic low voltages for these logic families.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum DILogicFamily

#### Remarks

Specifies the logic family to use for acquisition. A logic family corresponds to voltage thresholds that are compatible with a group of voltage standards. Refer to the device documentation for information on the logic high and logic low voltages for these logic families. Use this enumeration to get or set the value of [LogicFamily](nationalinstruments-daqmx-dichannel-logicfamily.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| OnePointEightVolts | 16184 | Compatible with 1.8 V CMOS signals. |
| TwoPointFiveVolts | 14620 | Compatible with 2.5 V CMOS signals. |
| ThreePointThreeVolts | 14621 | Compatible with LVTTL signals. |
| FiveVolts | 14619 | Compatible with TTL and 5 V CMOS signals. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dochannel-datatransfermechanism.html language=enus -->
## TOPIC 02059: DataTransferMechanism

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dochannel-datatransfermechanism.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dochannel-datatransfermechanism.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the data transfer mode for the device. SyntaxNamespace: NationalInstruments.DAQmxpublic DODataTransferMechanism DataTransferMechanism { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DataTransferMechanism

Specifies the data transfer mode for the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DODataTransferMechanism](nationalinstruments-daqmx-dodatatransfermechanism.html) DataTransferMechanism { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dochannel-datatransferrequestcondition.html language=enus -->
## TOPIC 02060: DataTransferRequestCondition

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dochannel-datatransferrequestcondition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dochannel-datatransferrequestcondition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies under what condition to transfer data from the buffer to the onboard memory of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic DODataTransferRequestCondition DataTransferRequestCondition { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx d

### DataTransferRequestCondition

Specifies under what condition to transfer data from the buffer to the onboard memory of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DODataTransferRequestCondition](nationalinstruments-daqmx-dodatatransferrequestcondition.html) DataTransferRequestCondition { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dochannel-generateon.html language=enus -->
## TOPIC 02061: GenerateOn

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dochannel-generateon.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dochannel-generateon.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge of the sample clock to generate samples. SyntaxNamespace: NationalInstruments.DAQmxpublic DOGenerateOn GenerateOn { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### GenerateOn

Specifies on which edge of the sample clock to generate samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DOGenerateOn](nationalinstruments-daqmx-dogenerateon.html) GenerateOn { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dochannel-invertlines.html language=enus -->
## TOPIC 02062: InvertLines

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dochannel-invertlines.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dochannel-invertlines.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to invert the lines in the channel. If you set this property to true, the lines are at high logic when off and at low logic when on. SyntaxNamespace: NationalInstruments.DAQmxpublic bool InvertLines { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-

### InvertLines

Specifies whether to invert the lines in the channel. If you set this property to true, the lines are at high logic when off and at low logic when on.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool InvertLines { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dochannel-linestatesdonestate.html language=enus -->
## TOPIC 02063: LineStatesDoneState

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dochannel-linestatesdonestate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dochannel-linestatesdonestate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the state of the lines in a digital output task when the task completes execution. SyntaxNamespace: NationalInstruments.DAQmxpublic DOLineStatesDoneState LineStatesDoneState { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### LineStatesDoneState

Specifies the state of the lines in a digital output task when the task [completes execution](/csh?context=nidaqmx_mxcncpts_whentaskdone).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DOLineStatesDoneState](nationalinstruments-daqmx-dolinestatesdonestate.html) LineStatesDoneState { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dochannel-linestatespausedstate.html language=enus -->
## TOPIC 02064: LineStatesPausedState

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dochannel-linestatespausedstate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dochannel-linestatespausedstate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the state of the lines in a digital output task when the task pauses. SyntaxNamespace: NationalInstruments.DAQmxpublic DOLineStatesPausedState LineStatesPausedState { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### LineStatesPausedState

Specifies the state of the lines in a digital output task when the task pauses.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DOLineStatesPausedState](nationalinstruments-daqmx-dolinestatespausedstate.html) LineStatesPausedState { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dochannel-linestatesstartstate.html language=enus -->
## TOPIC 02065: LineStatesStartState

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dochannel-linestatesstartstate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dochannel-linestatesstartstate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the state of the lines in a digital output task when the task starts. SyntaxNamespace: NationalInstruments.DAQmxpublic DOLineStatesStartState LineStatesStartState { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### LineStatesStartState

Specifies the state of the lines in a digital output task when the task starts.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DOLineStatesStartState](nationalinstruments-daqmx-dolinestatesstartstate.html) LineStatesStartState { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dochannel-logicfamily.html language=enus -->
## TOPIC 02066: LogicFamily

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dochannel-logicfamily.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dochannel-logicfamily.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic family to use for generation. A logic family corresponds to voltage thresholds that are compatible with a group of voltage standards. Refer to the device documentation for information on the logic high and logic low voltages for these logic families. SyntaxNamespace: NationalInst

### LogicFamily

Specifies the logic family to use for generation. A logic family corresponds to voltage thresholds that are compatible with a group of voltage standards. Refer to the device documentation for information on the logic high and logic low voltages for these logic families.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DOLogicFamily](nationalinstruments-daqmx-dologicfamily.html) LogicFamily { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dochannel-memorymappingenable.html language=enus -->
## TOPIC 02067: MemoryMappingEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dochannel-memorymappingenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dochannel-memorymappingenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies for NI-DAQmx to map hardware registers to the memory space of the application, if possible. Normally, NI-DAQmx maps hardware registers to memory accessible only to the kernel. Mapping the registers to the memory space of the application increases performance. However, if the application ac

### MemoryMappingEnable

Specifies for NI-DAQmx to map hardware registers to the memory space of the application, if possible. Normally, NI-DAQmx maps hardware registers to memory accessible only to the kernel. Mapping the registers to the memory space of the application increases performance. However, if the application accesses the memory space mapped to the registers, it can adversely affect the operation of the device and possibly result in a system crash.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool MemoryMappingEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dochannel-numberoflines.html language=enus -->
## TOPIC 02068: NumberOfLines

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dochannel-numberoflines.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dochannel-numberoflines.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of digital lines in the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic long NumberOfLines { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### NumberOfLines

Indicates the number of digital lines in the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long NumberOfLines { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dochannel-outputdrivetype.html language=enus -->
## TOPIC 02069: OutputDriveType

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dochannel-outputdrivetype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dochannel-outputdrivetype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the drive type for digital output channels. SyntaxNamespace: NationalInstruments.DAQmxpublic DOOutputDriveType OutputDriveType { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### OutputDriveType

Specifies the drive type for digital output channels.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DOOutputDriveType](nationalinstruments-daqmx-dooutputdrivetype.html) OutputDriveType { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dochannel-overcurrentautoreenable.html language=enus -->
## TOPIC 02070: OvercurrentAutoReenable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dochannel-overcurrentautoreenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dochannel-overcurrentautoreenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to automatically reenable channels after they no longer exceed the current limit specified by OvercurrentLimit. SyntaxNamespace: NationalInstruments.DAQmxpublic bool OvercurrentAutoReenable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx dri

### OvercurrentAutoReenable

Specifies whether to automatically reenable channels after they no longer exceed the current limit specified by [OvercurrentLimit](nationalinstruments-daqmx-dochannel-overcurrentlimit.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool OvercurrentAutoReenable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dochannel-overcurrentlimit.html language=enus -->
## TOPIC 02071: OvercurrentLimit

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dochannel-overcurrentlimit.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dochannel-overcurrentlimit.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the current threshold in Amperes for the channel. A value of 0 means the channel observes no limit. Devices can monitor only a finite number of current thresholds simultaneously. If you attempt to monitor additional thresholds, NI-DAQmx returns an error. SyntaxNamespace: NationalInstrument

### OvercurrentLimit

Specifies the current threshold in Amperes for the channel. A value of 0 means the channel observes no limit. Devices can monitor only a finite number of current thresholds simultaneously. If you attempt to monitor additional thresholds, NI-DAQmx returns an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double OvercurrentLimit { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dochannel-overcurrentreenableperiod.html language=enus -->
## TOPIC 02072: OvercurrentReenablePeriod

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dochannel-overcurrentreenableperiod.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dochannel-overcurrentreenableperiod.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the delay in seconds between the time a channel no longer exceeds the current limit and the reactivation of that channel, if OvercurrentAutoReenable is true. SyntaxNamespace: NationalInstruments.DAQmxpublic double OvercurrentReenablePeriod { get; set; }ExceptionsTypeDescriptionNationalInst

### OvercurrentReenablePeriod

Specifies the delay in seconds between the time a channel no longer exceeds the current limit and the reactivation of that channel, if [OvercurrentAutoReenable](nationalinstruments-daqmx-dochannel-overcurrentautoreenable.html) is true.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double OvercurrentReenablePeriod { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dochannel-tristate.html language=enus -->
## TOPIC 02073: Tristate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dochannel-tristate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dochannel-tristate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to stop driving the channel and set it to a high-impedance state. You must commit the task for this setting to take effect. SyntaxNamespace: NationalInstruments.DAQmxpublic bool Tristate { get; set; }RemarksSetting this property before you commit the task determines whether NI-DAQm

### Tristate

Specifies whether to stop driving the channel and set it to a high-impedance state. You must commit the task for this setting to take effect.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool Tristate { get; set; }

#### Remarks

Setting this property before you [commit](/csh?context=nidaqmx_mxcncpts_committed) the task determines whether NI-DAQmx drives data on the channel or tristates the channel after the task transitions to the committed state.

Use this property when you want to read and write to channels in a task. Set this property to true before you read from the channel and set this property to false before you write to the channel.

When you read from an output channel that is not tristated, the value corresponds to the current value you are driving on the channel.

When you write to a channel that is tristated, no change occurs until you set this property to false. After you set this property to false, the value NI-DAQmx drives on the channel corresponds to the last value written to the channel.

Ensure the channel is tristated before any external devices that you connect to the channel drive data onto the channel. Failure to do so could result in double-driving the channel and damaging the device.

This property is supported only for line-configurable, bidirectional ports.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dochannel-usbtransferrequestcount.html language=enus -->
## TOPIC 02074: UsbTransferRequestCount

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dochannel-usbtransferrequestcount.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dochannel-usbtransferrequestcount.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of simultaneous USB transfers used to stream data. Modify this value to affect performance under different combinations of operating system and device. SyntaxNamespace: NationalInstruments.DAQmxpublic long UsbTransferRequestCount { get; set; }ExceptionsTypeDescriptionNat

### UsbTransferRequestCount

Specifies the maximum number of simultaneous USB transfers used to stream data. Modify this value to affect performance under different combinations of operating system and device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long UsbTransferRequestCount { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dochannel-usbtransferrequestsize.html language=enus -->
## TOPIC 02075: UsbTransferRequestSize

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dochannel-usbtransferrequestsize.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dochannel-usbtransferrequestsize.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum size of a USB transfer request in bytes. Modify this value to affect performance under different combinations of operating system and device. SyntaxNamespace: NationalInstruments.DAQmxpublic long UsbTransferRequestSize { get; set; }ExceptionsTypeDescriptionNationalInstruments.D

### UsbTransferRequestSize

Specifies the maximum size of a USB transfer request in bytes. Modify this value to affect performance under different combinations of operating system and device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long UsbTransferRequestSize { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dochannel-useonlyonboardmemory.html language=enus -->
## TOPIC 02076: UseOnlyOnBoardMemory

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dochannel-useonlyonboardmemory.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dochannel-useonlyonboardmemory.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to write samples directly to the onboard memory of the device, bypassing the memory buffer. Generally, you cannot update onboard memory after you start the task. Onboard memory includes data FIFOs. SyntaxNamespace: NationalInstruments.DAQmxpublic bool UseOnlyOnBoardMemory { get; se

### UseOnlyOnBoardMemory

Specifies whether to write samples directly to the onboard memory of the device, bypassing the memory buffer. Generally, you cannot update onboard memory after you start the task. Onboard memory includes data FIFOs.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool UseOnlyOnBoardMemory { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dochannel.html language=enus -->
## TOPIC 02077: DOChannel Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dochannel.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dochannel.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Encapsulates one or more digital output channels and the properties for a digital output channel. Derives fromChannelIFilteredTypeDescriptorSyntaxNamespace: NationalInstruments.DAQmxpublic class DOChannel : Channel, IFilteredTypeDescriptorRemarksUse the DOChannels property to create or access a digi

### DOChannel Class

Encapsulates one or more digital output channels and the properties for a digital output channel.

#### Derives from

- Channel
- IFilteredTypeDescriptor

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class DOChannel : Channel, IFilteredTypeDescriptor

#### Remarks

DOChannels

DOChannel

DOChannel

DOChannels

DOChannelCollection

DOChannel

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| DataTransferMechanism | Specifies the data transfer mode for the device. |
| DataTransferRequestCondition | Specifies under what condition to transfer data from the buffer to the onboard memory of the device. |
| GenerateOn | Specifies on which edge of the sample clock to generate samples. |
| InvertLines | Specifies whether to invert the lines in the channel. If you set this property to true, the lines are at high logic when off and at low logic when on. |
| LineStatesDoneState | Specifies the state of the lines in a digital output task when the task completes execution. |
| LineStatesPausedState | Specifies the state of the lines in a digital output task when the task pauses. |
| LineStatesStartState | Specifies the state of the lines in a digital output task when the task starts. |
| LogicFamily | Specifies the logic family to use for generation. A logic family corresponds to voltage thresholds that are compatible with a group of voltage standards. Refer to the device documentation for information on the logic high and logic low voltages for these logic families. |
| MemoryMappingEnable | Specifies for NI-DAQmx to map hardware registers to the memory space of the application, if possible. Normally, NI-DAQmx maps hardware registers to memory accessible only to the kernel. Mapping the registers to the memory space of the application increases performance. However, if the application accesses the memory space mapped to the registers, it can adversely affect the operation of the device and possibly result in a system crash. |
| NumberOfLines | Indicates the number of digital lines in the channel. |
| OutputDriveType | Specifies the drive type for digital output channels. |
| OvercurrentAutoReenable | Specifies whether to automatically reenable channels after they no longer exceed the current limit specified by OvercurrentLimit. |
| OvercurrentLimit | Specifies the current threshold in Amperes for the channel. A value of 0 means the channel observes no limit. Devices can monitor only a finite number of current thresholds simultaneously. If you attempt to monitor additional thresholds, NI-DAQmx returns an error. |
| OvercurrentReenablePeriod | Specifies the delay in seconds between the time a channel no longer exceeds the current limit and the reactivation of that channel, if OvercurrentAutoReenable is true. |
| Tristate | Specifies whether to stop driving the channel and set it to a high-impedance state. You must commit the task for this setting to take effect. |
| UsbTransferRequestCount | Specifies the maximum number of simultaneous USB transfers used to stream data. Modify this value to affect performance under different combinations of operating system and device. |
| UsbTransferRequestSize | Specifies the maximum size of a USB transfer request in bytes. Modify this value to affect performance under different combinations of operating system and device. |
| UseOnlyOnBoardMemory | Specifies whether to write samples directly to the onboard memory of the device, bypassing the memory buffer. Generally, you cannot update onboard memory after you start the task. Onboard memory includes data FIFOs. |

#### See Also

- DOChannelCollection

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dochannelcollection-all.html language=enus -->
## TOPIC 02078: All

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dochannelcollection-all.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dochannelcollection-all.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DOChannel that operates on all of the channels in the task. SyntaxNamespace: NationalInstruments.DAQmxpublic DOChannel All { get; }RemarksA DOChannel that operates on all of the channels in a task.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an e

### All

Gets a [DOChannel](nationalinstruments-daqmx-dochannel.html) that operates on all of the channels in the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DOChannel](nationalinstruments-daqmx-dochannel.html) All { get; }

#### Remarks

A [DOChannel](nationalinstruments-daqmx-dochannel.html) that operates on all of the channels in a task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DOChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dochannelcollection-copyto__array-int.html language=enus -->
## TOPIC 02079: CopyTo(Array, int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dochannelcollection-copyto__array-int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dochannelcollection-copyto__array-int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Copies the collection to an array or a portion of an array. This operation is not supported for DOChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic void CopyTo(Array array, int index)ParametersNameTypeDescriptionarrayArrayDestination array for the collection.indexintThe index in th

### CopyTo(Array, int)

Copies the collection to an array or a portion of an array. This operation is not supported for [DOChannelCollection](nationalinstruments-daqmx-dochannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void CopyTo(Array array, int index)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| array | Array | Destination array for the collection. |
| index | int | The index in the target array at which you want to begin copying the collection to. |

#### Exceptions

| Type | Description |
| --- | --- |
| NotSupportedException | This method always throws a NotSupportedException. |

Parent topic:

DOChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dochannelcollection-count.html language=enus -->
## TOPIC 02080: Count

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dochannelcollection-count.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dochannelcollection-count.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of elements in the collection. SyntaxNamespace: NationalInstruments.DAQmxpublic int Count { get; }RemarksThe number of elements contained in the collection.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Count

Gets the number of elements in the collection.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int Count { get; }

#### Remarks

The number of elements contained in the collection.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DOChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dochannelcollection-createchannel__string-string-channellinegrouping.html language=enus -->
## TOPIC 02081: CreateChannel(string, string, ChannelLineGrouping)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dochannelcollection-createchannel__string-string-channellinegrouping.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dochannelcollection-createchannel__string-string-channellinegrouping.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a DOChannel to generate digital signals. This method adds one or more channels to the DOChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic DOChannel CreateChannel(string lines, string nameToAssign, ChannelLineGrouping grouping)RemarksYou can group digital lines into one DOCh

### CreateChannel(string, string, ChannelLineGrouping)

Creates a [DOChannel](nationalinstruments-daqmx-dochannel.html) to [generate digital signals](/csh?context=nidaqmx_daqhelp_diglevelmeasgen). This method adds one or more channels to the [DOChannelCollection](nationalinstruments-daqmx-dochannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DOChannel](nationalinstruments-daqmx-dochannel.html) CreateChannel(string lines, string nameToAssign, ChannelLineGrouping grouping)

#### Remarks

You can group digital lines into one [DOChannel](nationalinstruments-daqmx-dochannel.html) or separate them into multiple [DOChannel](nationalinstruments-daqmx-dochannel.html) objects. If you specify one or more entire ports with *lines*  by using port physical channel names, you cannot separate the ports into multiple channels. To separate ports into multiple channels, use this method multiple times with a different port each time.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateChannel(string, string, ChannelLineGrouping) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| lines | string | The names of the digital lines or ports to use to create the virtual channel. |
| nameToAssign | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| grouping | ChannelLineGrouping | The grouping of digital lines into one or more DOChannel objects. If you specify one or more entire ports with lines , you must set grouping to OneChannelForAllLines. |

#### Returns

The newly created [DOChannel](nationalinstruments-daqmx-dochannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DOChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dochannelcollection-getenumerator.html language=enus -->
## TOPIC 02082: GetEnumerator()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dochannelcollection-getenumerator.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dochannelcollection-getenumerator.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an enumerator that you can use to iterate through the collection. SyntaxNamespace: NationalInstruments.DAQmxpublic IEnumerator GetEnumerator()RemarksFor a detailed explanation of this method, refer to GetEnumerator in the Microsoft .NET Framework documentation. ReturnsEnumerator for the coll

### GetEnumerator()

Returns an enumerator that you can use to iterate through the collection.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IEnumerator GetEnumerator()

#### Remarks

For a detailed explanation of this method, refer to GetEnumerator in the Microsoft .NET Framework documentation.

#### Returns

Enumerator for the collection.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DOChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dochannelcollection-this__long.html language=enus -->
## TOPIC 02083: this[long index]

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dochannelcollection-this__long.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dochannelcollection-this__long.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DOChannel at the specified index. In Visual C#, this property is the indexer. SyntaxNamespace: NationalInstruments.DAQmxpublic DOChannel this[long index] { get; }RemarksThe DOChannel at the specified index. ChannelsParametersNameTypeDescriptionindexlongThe zero-based index of the entry to l

### this[long index]

Gets the [DOChannel](nationalinstruments-daqmx-dochannel.html) at the specified index. In Visual C#, this property is the indexer.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DOChannel](nationalinstruments-daqmx-dochannel.html) this[long index] { get; }

#### Remarks

The [DOChannel](nationalinstruments-daqmx-dochannel.html) at the specified index.

Channels

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| index | long | The zero-based index of the entry to locate in the collection. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

#### See Also

- DOChannel

Parent topic:

DOChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dochannelcollection-this__string.html language=enus -->
## TOPIC 02084: this[string virtualChannelName]

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dochannelcollection-this__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dochannelcollection-this__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DOChannel with the specified virtual channel name. In Visual C#, this property is the indexer. SyntaxNamespace: NationalInstruments.DAQmxpublic DOChannel this[string virtualChannelName] { get; }RemarksThe specified DOChannel. ChannelsBy using a comma or colon in virtualChannelName , you can

### this[string virtualChannelName]

Gets the [DOChannel](nationalinstruments-daqmx-dochannel.html) with the specified virtual channel name. In Visual C#, this property is the indexer.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DOChannel](nationalinstruments-daqmx-dochannel.html) this[string virtualChannelName] { get; }

#### Remarks

The specified [DOChannel](nationalinstruments-daqmx-dochannel.html).

Channels

By using a comma or colon in *virtualChannelName* , you can retrieve more than one channel at a time. For more information refer to [Channels](https://#).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| virtualChannelName | string | One or more virtual channel names that the retrieved DOChannel operates on. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

#### See Also

- DOChannel

Parent topic:

DOChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dochannelcollection-tostring.html language=enus -->
## TOPIC 02085: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dochannelcollection-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dochannelcollection-tostring.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the object. SyntaxNamespace: NationalInstruments.DAQmxpublic override string ToString()RemarksOverrides ToString. ReturnsA string representation of the object.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ToString()

Returns a string representation of the object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override string ToString()

#### Remarks

Overrides ToString.

#### Returns

A string representation of the object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DOChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dochannelcollection.html language=enus -->
## TOPIC 02086: DOChannelCollection Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dochannelcollection.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dochannelcollection.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains the collection of digital output channels for a Task. Derives fromMarshalByRefObjectICollectionSyntaxNamespace: NationalInstruments.DAQmxpublic class DOChannelCollection : MarshalByRefObject, ICollectionRemarksExample applications are located in the <Public Documents>\National Instruments\N

### DOChannelCollection Class

Contains the collection of digital output channels for a [Task](nationalinstruments-daqmx-task.html).

#### Derives from

- MarshalByRefObject
- ICollection

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class DOChannelCollection : MarshalByRefObject, ICollection

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| All | Gets a DOChannel that operates on all of the channels in the task. |
| Count | Gets the number of elements in the collection. |
| this[long index] | Gets the DOChannel at the specified index. In Visual C#, this property is the indexer. |
| this[string virtualChannelName] | Gets the DOChannel with the specified virtual channel name. In Visual C#, this property is the indexer. |

#### Methods

| Name | Description |
| --- | --- |
| CopyTo(Array, int) | Copies the collection to an array or a portion of an array. This operation is not supported for DOChannelCollection. |
| CreateChannel(string, string, ChannelLineGrouping) | Creates a DOChannel to generate digital signals. This method adds one or more channels to the DOChannelCollection. |
| GetEnumerator() | Returns an enumerator that you can use to iterate through the collection. |
| ToString() | Returns a string representation of the object. |

#### See Also

- Task
- DOChannels
- DOChannel

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dodatatransfermechanism.html language=enus -->
## TOPIC 02087: DODataTransferMechanism Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dodatatransfermechanism.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dodatatransfermechanism.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the data transfer mode for the device. SyntaxNamespace: NationalInstruments.DAQmxpublic enum DODataTransferMechanismRemarksSpecifies the data transfer mode for the device. Use this enumeration to get or set the value of DataTransferMechanism.MembersNameValueDescriptionDma10054Direct Memory

### DODataTransferMechanism Enumeration

Specifies the data transfer mode for the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum DODataTransferMechanism

#### Remarks

Specifies the data transfer mode for the device. Use this enumeration to get or set the value of [DataTransferMechanism](nationalinstruments-daqmx-dochannel-datatransfermechanism.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Dma | 10054 | Direct Memory Access. Data transfers take place independently from the application. |
| Interrupts | 10204 | Data transfers take place independently from the application. Using interrupts increases CPU usage because the CPU must service interrupt requests. Typically, you should use interrupts if the device is out of DMA channels. |
| ProgrammedIO | 10264 | Data transfers take place when you call reading from the task or writing to the task. |
| UsbBulk | 12590 | Data transfers take place independently from the application using a USB bulk pipe. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dodatatransferrequestcondition.html language=enus -->
## TOPIC 02088: DODataTransferRequestCondition Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dodatatransferrequestcondition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dodatatransferrequestcondition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies under what condition to transfer data from the buffer to the onboard memory of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic enum DODataTransferRequestConditionRemarksSpecifies under what condition to transfer data from the buffer to the onboard memory of the device. Use thi

### DODataTransferRequestCondition Enumeration

Specifies under what condition to transfer data from the buffer to the onboard memory of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum DODataTransferRequestCondition

#### Remarks

Specifies under what condition to transfer data from the buffer to the onboard memory of the device. Use this enumeration to get or set the value of [DataTransferRequestCondition](nationalinstruments-daqmx-dochannel-datatransferrequestcondition.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| OnBoardMemoryEmpty | 10235 | Transfer data to the device only when there is no data in the onboard memory of the device. |
| OnBoardMemoryHalfFullOrLess | 10239 | Transfer data to the device any time the onboard memory is less than half full. |
| OnBoardMemoryNotFull | 10242 | Transfer data to the device any time the onboard memory of the device is not full. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dogenerateon.html language=enus -->
## TOPIC 02089: DOGenerateOn Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dogenerateon.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dogenerateon.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge of the sample clock to generate samples. SyntaxNamespace: NationalInstruments.DAQmxpublic enum DOGenerateOnRemarksSpecifies on which edge of the sample clock to generate samples. Use this enumeration to get or set the value of GenerateOn.MembersNameValueDescriptionActiveEdge1

### DOGenerateOn Enumeration

Specifies on which edge of the sample clock to generate samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum DOGenerateOn

#### Remarks

Specifies on which edge of the sample clock to generate samples. Use this enumeration to get or set the value of [GenerateOn](nationalinstruments-daqmx-dochannel-generateon.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ActiveEdge | 14617 | Active edges. |
| InactiveEdge | 14618 | Inactive edges. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dolinestatesdonestate.html language=enus -->
## TOPIC 02090: DOLineStatesDoneState Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dolinestatesdonestate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dolinestatesdonestate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the state of the lines in a digital output task when the task completes execution. SyntaxNamespace: NationalInstruments.DAQmxpublic enum DOLineStatesDoneStateRemarksSpecifies the state of the lines in a digital output task when the task completes execution. Use this enumeration to get or s

### DOLineStatesDoneState Enumeration

Specifies the state of the lines in a digital output task when the task [completes execution](/csh?context=nidaqmx_mxcncpts_whentaskdone).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum DOLineStatesDoneState

#### Remarks

Specifies the state of the lines in a digital output task when the task [completes execution](/csh?context=nidaqmx_mxcncpts_whentaskdone). Use this enumeration to get or set the value of [LineStatesDoneState](nationalinstruments-daqmx-dochannel-linestatesdonestate.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| High | 10192 | Logic high. |
| Low | 10214 | Logic low. |
| Tristate | 10310 | High-impedance state. You can select this state only on devices with bidirectional lines. You cannot select this state for dedicated digital output lines. On some devices, you can select this value only for entire ports. |
| NoChange | 10160 | Do not change the state of the lines. On some devices, you can select this value only for entire ports. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dolinestatespausedstate.html language=enus -->
## TOPIC 02091: DOLineStatesPausedState Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dolinestatespausedstate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dolinestatespausedstate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the state of the lines in a digital output task when the task pauses. SyntaxNamespace: NationalInstruments.DAQmxpublic enum DOLineStatesPausedStateRemarksSpecifies the state of the lines in a digital output task when the task pauses. Use this enumeration to get or set the value of LineStat

### DOLineStatesPausedState Enumeration

Specifies the state of the lines in a digital output task when the task pauses.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum DOLineStatesPausedState

#### Remarks

Specifies the state of the lines in a digital output task when the task pauses. Use this enumeration to get or set the value of [LineStatesPausedState](nationalinstruments-daqmx-dochannel-linestatespausedstate.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| High | 10192 | Logic high. |
| Low | 10214 | Logic low. |
| Tristate | 10310 | High-impedance state. You can select this state only on devices with bidirectional lines. You cannot select this state for dedicated digital output lines. On some devices, you can select this value only for entire ports. |
| NoChange | 10160 | Do not change the state of the lines. On some devices, you can select this value only for entire ports. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dolinestatesstartstate.html language=enus -->
## TOPIC 02092: DOLineStatesStartState Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dolinestatesstartstate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dolinestatesstartstate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the state of the lines in a digital output task when the task starts. SyntaxNamespace: NationalInstruments.DAQmxpublic enum DOLineStatesStartStateRemarksSpecifies the state of the lines in a digital output task when the task starts. Use this enumeration to get or set the value of LineState

### DOLineStatesStartState Enumeration

Specifies the state of the lines in a digital output task when the task starts.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum DOLineStatesStartState

#### Remarks

Specifies the state of the lines in a digital output task when the task starts. Use this enumeration to get or set the value of [LineStatesStartState](nationalinstruments-daqmx-dochannel-linestatesstartstate.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| High | 10192 | Logic high. |
| Low | 10214 | Logic low. |
| Tristate | 10310 | High-impedance state. You can select this state only on devices with bidirectional lines. You cannot select this state for dedicated digital output lines. On some devices, you can select this value only for entire ports. |
| NoChange | 10160 | Do not change the state of the lines. On some devices, you can select this value only for entire ports. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dologicfamily.html language=enus -->
## TOPIC 02093: DOLogicFamily Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dologicfamily.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dologicfamily.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic family to use for generation. A logic family corresponds to voltage thresholds that are compatible with a group of voltage standards. Refer to the device documentation for information on the logic high and logic low voltages for these logic families. SyntaxNamespace: NationalInst

### DOLogicFamily Enumeration

Specifies the logic family to use for generation. A logic family corresponds to voltage thresholds that are compatible with a group of voltage standards. Refer to the device documentation for information on the logic high and logic low voltages for these logic families.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum DOLogicFamily

#### Remarks

Specifies the logic family to use for generation. A logic family corresponds to voltage thresholds that are compatible with a group of voltage standards. Refer to the device documentation for information on the logic high and logic low voltages for these logic families. Use this enumeration to get or set the value of [LogicFamily](nationalinstruments-daqmx-dochannel-logicfamily.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| OnePointEightVolts | 16184 | Compatible with 1.8 V CMOS signals. |
| TwoPointFiveVolts | 14620 | Compatible with 2.5 V CMOS signals. |
| ThreePointThreeVolts | 14621 | Compatible with LVTTL signals. |
| FiveVolts | 14619 | Compatible with TTL and 5 V CMOS signals. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dooutputdrivetype.html language=enus -->
## TOPIC 02094: DOOutputDriveType Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dooutputdrivetype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dooutputdrivetype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the drive type for digital output channels. SyntaxNamespace: NationalInstruments.DAQmxpublic enum DOOutputDriveTypeRemarksSpecifies the drive type for digital output channels. Use this enumeration to get or set the value of OutputDriveType.MembersNameValueDescriptionActiveDrive12573Drive t

### DOOutputDriveType Enumeration

Specifies the drive type for digital output channels.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum DOOutputDriveType

#### Remarks

Specifies the drive type for digital output channels. Use this enumeration to get or set the value of [OutputDriveType](nationalinstruments-daqmx-dochannel-outputdrivetype.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ActiveDrive | 12573 | Drive the output pin to approximately 0 V for logic low and +3.3 V or +5 V, depending on the device, for logic high. |
| OpenCollector | 12574 | Drive the output pin to 0 V for logic low. For logic high, the output driver assumes a high-impedance state and does not drive a voltage. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-everynsamplesreadeventargs-checkforexception.html language=enus -->
## TOPIC 02095: CheckForException()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-everynsamplesreadeventargs-checkforexception.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-everynsamplesreadeventargs-checkforexception.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Throws the Exception that occurred, if any exists. SyntaxNamespace: NationalInstruments.DAQmxpublic void CheckForException()RemarksIf the task stops due to an error, the Error property returns an Exception that represents the particular error. If the task did not stop due to an error, the method ret

### CheckForException()

Throws the Exception that occurred, if any exists.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void CheckForException()

#### Remarks

If the task stops due to an error, the [Error](nationalinstruments-daqmx-everynsamplesreadeventargs-error.html) property returns an Exception that represents the particular error. If the task did not stop due to an error, the method returns. As an alternative to calling this method, you can check the [Error](nationalinstruments-daqmx-everynsamplesreadeventargs-error.html) property.

Parent topic:

EveryNSamplesReadEventArgs Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-everynsamplesreadeventargs-error.html language=enus -->
## TOPIC 02096: Error

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-everynsamplesreadeventargs-error.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-everynsamplesreadeventargs-error.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Exception that occurred, if any. SyntaxNamespace: NationalInstruments.DAQmxpublic Exception Error { get; }RemarksIf the task stops due to an error, this property returns an Exception that represents the particular error. If the task did not stop due to an error, this value is null.As an alt

### Error

Gets the Exception that occurred, if any.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public Exception Error { get; }

#### Remarks

If the task stops due to an error, this property returns an Exception that represents the particular error. If the task did not stop due to an error, this value is null.

As an alternative to checking this property, you can call the [CheckForException](nationalinstruments-daqmx-everynsamplesreadeventargs-checkforexception.html) method.

Parent topic:

EveryNSamplesReadEventArgs Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-everynsamplesreadeventargs-everynsamplesreadeventargs__exception.html language=enus -->
## TOPIC 02097: EveryNSamplesReadEventArgs(Exception)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-everynsamplesreadeventargs-everynsamplesreadeventargs__exception.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-everynsamplesreadeventargs-everynsamplesreadeventargs__exception.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the EveryNSamplesReadEventArgs class with the specified exception. SyntaxNamespace: NationalInstruments.DAQmxpublic EveryNSamplesReadEventArgs(Exception exception)ParametersNameTypeDescriptionexceptionExceptionAn Exception that explains why the task stopped, or null if

### EveryNSamplesReadEventArgs(Exception)

Initializes a new instance of the [EveryNSamplesReadEventArgs](nationalinstruments-daqmx-everynsamplesreadeventargs.html) class with the specified exception.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public EveryNSamplesReadEventArgs(Exception exception)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| exception | Exception | An Exception that explains why the task stopped, or null if the task completed successfully. |

Parent topic:

EveryNSamplesReadEventArgs Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-everynsamplesreadeventargs-getobjectdata__serializationinfo-streamingcontext.html language=enus -->
## TOPIC 02098: GetObjectData(SerializationInfo, StreamingContext)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-everynsamplesreadeventargs-getobjectdata__serializationinfo-streamingcontext.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-everynsamplesreadeventargs-getobjectdata__serializationinfo-streamingcontext.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the SerializationInfo object with information about the exception. SyntaxNamespace: NationalInstruments.DAQmxprotected void GetObjectData(SerializationInfo info, StreamingContext context)ParametersNameTypeDescriptioninfoSerializationInfoObject that holds the serialized object data.contextStream

### GetObjectData(SerializationInfo, StreamingContext)

Sets the SerializationInfo object with information about the exception.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

protected void GetObjectData(SerializationInfo info, StreamingContext context)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| info | SerializationInfo | Object that holds the serialized object data. |
| context | StreamingContext | Contextual information about the source or destination. |

Parent topic:

EveryNSamplesReadEventArgs Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-everynsamplesreadeventargs.html language=enus -->
## TOPIC 02099: EveryNSamplesReadEventArgs Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-everynsamplesreadeventargs.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-everynsamplesreadeventargs.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides data for the EveryNSamplesRead event. Derives fromEventArgsISerializableSyntaxNamespace: NationalInstruments.DAQmxpublic class EveryNSamplesReadEventArgs : EventArgs, ISerializableRemarksExample applications are located in the <Public Documents>\National Instruments\NI-DAQ\Examples\DotNET4.

### EveryNSamplesReadEventArgs Class

Provides data for the [EveryNSamplesRead](nationalinstruments-daqmx-task-everynsamplesread.html) event.

#### Derives from

- EventArgs
- ISerializable

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class EveryNSamplesReadEventArgs : EventArgs, ISerializable

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| EveryNSamplesReadEventArgs(Exception) | Initializes a new instance of the EveryNSamplesReadEventArgs class with the specified exception. |

#### Properties

| Name | Description |
| --- | --- |
| Error | Gets the Exception that occurred, if any. |

#### Methods

| Name | Description |
| --- | --- |
| GetObjectData(SerializationInfo, StreamingContext) | Sets the SerializationInfo object with information about the exception. |
| CheckForException() | Throws the Exception that occurred, if any exists. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-everynsamplesreadeventhandler__object-everynsamplesreadeventargs.html language=enus -->
## TOPIC 02100: EveryNSamplesReadEventHandler Delegate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-everynsamplesreadeventhandler__object-everynsamplesreadeventargs.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-everynsamplesreadeventhandler__object-everynsamplesreadeventargs.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the method that handles the EveryNSamplesRead event. SyntaxNamespace: NationalInstrumentspublic delegate void EveryNSamplesReadEventHandler(object sender, EveryNSamplesReadEventArgs e)ParametersNameTypeDescriptionsenderobjectThe Task that caused this event.eEveryNSamplesReadEventArgsAn Ev

### EveryNSamplesReadEventHandler Delegate

Represents the method that handles the [EveryNSamplesRead](nationalinstruments-daqmx-task-everynsamplesread.html) event.

#### Syntax

**Namespace:**NationalInstruments

public delegate void EveryNSamplesReadEventHandler(object sender, EveryNSamplesReadEventArgs e)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sender | object | The Task that caused this event. |
| e | EveryNSamplesReadEventArgs | An EveryNSamplesReadEventArgs that contains the event data. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-everynsampleswritteneventargs-checkforexception.html language=enus -->
## TOPIC 02101: CheckForException()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-everynsampleswritteneventargs-checkforexception.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-everynsampleswritteneventargs-checkforexception.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Throws the Exception that occurred, if any exists. SyntaxNamespace: NationalInstruments.DAQmxpublic void CheckForException()RemarksIf the task stops due to an error, the Error property returns an Exception that represents the particular error. If the task did not stop due to an error, the method ret

### CheckForException()

Throws the Exception that occurred, if any exists.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void CheckForException()

#### Remarks

If the task stops due to an error, the [Error](nationalinstruments-daqmx-everynsampleswritteneventargs-error.html) property returns an Exception that represents the particular error. If the task did not stop due to an error, the method returns. As an alternative to calling this method, you can check the [Error](nationalinstruments-daqmx-everynsampleswritteneventargs-error.html) property.

Parent topic:

EveryNSamplesWrittenEventArgs Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-everynsampleswritteneventargs-error.html language=enus -->
## TOPIC 02102: Error

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-everynsampleswritteneventargs-error.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-everynsampleswritteneventargs-error.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Exception that occurred, if any. SyntaxNamespace: NationalInstruments.DAQmxpublic Exception Error { get; }RemarksIf the task stops due to an error, this property returns an Exception that represents the particular error. If the task did not stop due to an error, this value is null.As an alt

### Error

Gets the Exception that occurred, if any.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public Exception Error { get; }

#### Remarks

If the task stops due to an error, this property returns an Exception that represents the particular error. If the task did not stop due to an error, this value is null.

As an alternative to checking this property, you can call the [CheckForException](nationalinstruments-daqmx-everynsampleswritteneventargs-checkforexception.html) method.

Parent topic:

EveryNSamplesWrittenEventArgs Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-everynsampleswritteneventargs-everynsampleswritteneventargs__exception.html language=enus -->
## TOPIC 02103: EveryNSamplesWrittenEventArgs(Exception)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-everynsampleswritteneventargs-everynsampleswritteneventargs__exception.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-everynsampleswritteneventargs-everynsampleswritteneventargs__exception.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the EveryNSamplesWrittenEventArgs class with the specified exception. SyntaxNamespace: NationalInstruments.DAQmxpublic EveryNSamplesWrittenEventArgs(Exception exception)ParametersNameTypeDescriptionexceptionExceptionAn Exception that explains why the task stopped, or nu

### EveryNSamplesWrittenEventArgs(Exception)

Initializes a new instance of the [EveryNSamplesWrittenEventArgs](nationalinstruments-daqmx-everynsampleswritteneventargs.html) class with the specified exception.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public EveryNSamplesWrittenEventArgs(Exception exception)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| exception | Exception | An Exception that explains why the task stopped, or null if the task completed successfully. |

Parent topic:

EveryNSamplesWrittenEventArgs Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-everynsampleswritteneventargs-getobjectdata__serializationinfo-streamingcontext.html language=enus -->
## TOPIC 02104: GetObjectData(SerializationInfo, StreamingContext)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-everynsampleswritteneventargs-getobjectdata__serializationinfo-streamingcontext.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-everynsampleswritteneventargs-getobjectdata__serializationinfo-streamingcontext.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the SerializationInfo object with information about the exception. SyntaxNamespace: NationalInstruments.DAQmxprotected void GetObjectData(SerializationInfo info, StreamingContext context)ParametersNameTypeDescriptioninfoSerializationInfoObject that holds the serialized object data.contextStream

### GetObjectData(SerializationInfo, StreamingContext)

Sets the SerializationInfo object with information about the exception.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

protected void GetObjectData(SerializationInfo info, StreamingContext context)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| info | SerializationInfo | Object that holds the serialized object data. |
| context | StreamingContext | Contextual information about the source or destination. |

Parent topic:

EveryNSamplesWrittenEventArgs Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-everynsampleswritteneventargs.html language=enus -->
## TOPIC 02105: EveryNSamplesWrittenEventArgs Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-everynsampleswritteneventargs.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-everynsampleswritteneventargs.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides data for the EveryNSamplesWritten event. Derives fromEventArgsISerializableSyntaxNamespace: NationalInstruments.DAQmxpublic class EveryNSamplesWrittenEventArgs : EventArgs, ISerializableRemarksExample applications are located in the <Public Documents>\National Instruments\NI-DAQ\Examples\Do

### EveryNSamplesWrittenEventArgs Class

Provides data for the [EveryNSamplesWritten](nationalinstruments-daqmx-task-everynsampleswritten.html) event.

#### Derives from

- EventArgs
- ISerializable

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class EveryNSamplesWrittenEventArgs : EventArgs, ISerializable

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| EveryNSamplesWrittenEventArgs(Exception) | Initializes a new instance of the EveryNSamplesWrittenEventArgs class with the specified exception. |

#### Properties

| Name | Description |
| --- | --- |
| Error | Gets the Exception that occurred, if any. |

#### Methods

| Name | Description |
| --- | --- |
| GetObjectData(SerializationInfo, StreamingContext) | Sets the SerializationInfo object with information about the exception. |
| CheckForException() | Throws the Exception that occurred, if any exists. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-everynsampleswritteneventhandler__object-everynsampleswritteneventargs.html language=enus -->
## TOPIC 02106: EveryNSamplesWrittenEventHandler Delegate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-everynsampleswritteneventhandler__object-everynsampleswritteneventargs.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-everynsampleswritteneventhandler__object-everynsampleswritteneventargs.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the method that handles the EveryNSamplesWritten event. SyntaxNamespace: NationalInstrumentspublic delegate void EveryNSamplesWrittenEventHandler(object sender, EveryNSamplesWrittenEventArgs e)ParametersNameTypeDescriptionsenderobjectThe Task that caused this event.eEveryNSamplesWrittenEv

### EveryNSamplesWrittenEventHandler Delegate

Represents the method that handles the [EveryNSamplesWritten](nationalinstruments-daqmx-task-everynsampleswritten.html) event.

#### Syntax

**Namespace:**NationalInstruments

public delegate void EveryNSamplesWrittenEventHandler(object sender, EveryNSamplesWrittenEventArgs e)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sender | object | The Task that caused this event. |
| e | EveryNSamplesWrittenEventArgs | An EveryNSamplesWrittenEventArgs that contains the event data. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-excitationidleoutputbehavior.html language=enus -->
## TOPIC 02107: ExcitationIdleOutputBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-excitationidleoutputbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-excitationidleoutputbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether this channel will disable excitation after the task is uncommitted. Setting this to Zero Volts or Amps disables excitation after task uncommit. Setting this attribute to Maintain Existing Value leaves the excitation on after task uncommit. SyntaxNamespace: NationalInstruments.DAQmx

### ExcitationIdleOutputBehavior Enumeration

Specifies whether this channel will disable excitation after the task is uncommitted. Setting this to Zero Volts or Amps disables excitation after task uncommit. Setting this attribute to Maintain Existing Value leaves the excitation on after task uncommit.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum ExcitationIdleOutputBehavior

#### Remarks

Specifies whether this channel will disable excitation after the task is uncommitted. Setting this to Zero Volts or Amps disables excitation after task uncommit. Setting this attribute to Maintain Existing Value leaves the excitation on after task uncommit. Use this enumeration to get or set the value of [ExcitationIdleOutputBehavior](nationalinstruments-daqmx-aichannel-excitationidleoutputbehavior.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ZeroVoltsOrAmps | 12526 | Drive excitation output to zero. |
| MaintainExistingValue | 12528 | Continue generating the current value. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignal.html language=enus -->
## TOPIC 02108: ExportSignal Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of the trigger, clock, or event to export. SyntaxNamespace: NationalInstruments.DAQmxpublic enum ExportSignalMembersNameValueDescriptionAIConvertClock12484Clock that causes an analog-to-digital conversion on an E Series device. One conversion corresponds to a single sample from on

### ExportSignal Enumeration

Specifies the name of the trigger, clock, or event to export.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum ExportSignal

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AIConvertClock | 12484 | Clock that causes an analog-to-digital conversion on an E Series device. One conversion corresponds to a single sample from one channel. |
| Timebase20MHz | 12486 | Output of an oscillator that is the onboard source of the Master Timebase. Other timebases are derived from this clock. |
| SampleClock | 12487 | Clock the device uses to time each sample. |
| AdvanceTrigger | 12488 | Trigger that moves a switch to the next entry in a scan list. |
| ReferenceTrigger | 12490 | Trigger that establishes the reference point between pretrigger and posttrigger samples. |
| StartTrigger | 12491 | Trigger that begins a measurement or generation. |
| AdvanceCompleteEvent | 12492 | Signal a switch product generates after it both executes the command(s) in a scan list entry and waits for the settling time to elapse. |
| AIHoldCompleteEvent | 12493 | Signal an E Series device generates when the device latches analog input data (the ADC enters "hold" mode) and it is safe for any external switching hardware to remove the signal and replace it with the next signal. This event does not indicate the completion of the actual analog-to-digital conversion. |
| CounterOutputEvent | 12494 | Signal a counter generates. Each time the counter reaches terminal count, this signal toggles or pulses. |
| ChangeDetectionEvent | 12511 | The signal that a static DIO device generates when the device detects a rising or falling edge on any of the lines or ports you selected when you configured change detection timing. |
| WatchdogExpiredEvent | 12512 | The signal that a static DIO device generates when the watchdog timer expires. |
| ReferenceClock10MHz | 12536 | Output of an oscillator that you can use to synchronize multiple devices. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-advancecompleteeventdelay.html language=enus -->
## TOPIC 02109: AdvanceCompleteEventDelay

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-advancecompleteeventdelay.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-advancecompleteeventdelay.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output signal delay in periods of the sample clock. SyntaxNamespace: NationalInstruments.DAQmxpublic double AdvanceCompleteEventDelay { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### AdvanceCompleteEventDelay

Specifies the output signal delay in periods of the sample clock.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double AdvanceCompleteEventDelay { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-advancecompleteeventoutputterminal.html language=enus -->
## TOPIC 02110: AdvanceCompleteEventOutputTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-advancecompleteeventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-advancecompleteeventoutputterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the Advance Complete Event. SyntaxNamespace: NationalInstruments.DAQmxpublic string AdvanceCompleteEventOutputTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### AdvanceCompleteEventOutputTerminal

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) to which to route the Advance Complete Event.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string AdvanceCompleteEventOutputTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-advancecompleteeventpulsepolarity.html language=enus -->
## TOPIC 02111: AdvanceCompleteEventPulsePolarity

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-advancecompleteeventpulsepolarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-advancecompleteeventpulsepolarity.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polarity of the exported Advance Complete Event. SyntaxNamespace: NationalInstruments.DAQmxpublic AdvanceCompleteEventPulsePolarity AdvanceCompleteEventPulsePolarity { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### AdvanceCompleteEventPulsePolarity

Specifies the polarity of the exported Advance Complete Event.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AdvanceCompleteEventPulsePolarity](nationalinstruments-daqmx-advancecompleteeventpulsepolarity.html) AdvanceCompleteEventPulsePolarity { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-advancecompleteeventpulsewidth.html language=enus -->
## TOPIC 02112: AdvanceCompleteEventPulseWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-advancecompleteeventpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-advancecompleteeventpulsewidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the width of the exported Advance Complete Event pulse. SyntaxNamespace: NationalInstruments.DAQmxpublic double AdvanceCompleteEventPulseWidth { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### AdvanceCompleteEventPulseWidth

Specifies the width of the exported Advance Complete Event pulse.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double AdvanceCompleteEventPulseWidth { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-advancetriggeroutputterminal.html language=enus -->
## TOPIC 02113: AdvanceTriggerOutputTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-advancetriggeroutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-advancetriggeroutputterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the Advance Trigger. SyntaxNamespace: NationalInstruments.DAQmxpublic string AdvanceTriggerOutputTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### AdvanceTriggerOutputTerminal

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) to which to route the Advance Trigger.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string AdvanceTriggerOutputTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-advancetriggerpulsepolarity.html language=enus -->
## TOPIC 02114: AdvanceTriggerPulsePolarity

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-advancetriggerpulsepolarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-advancetriggerpulsepolarity.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the polarity of the exported Advance Trigger. SyntaxNamespace: NationalInstruments.DAQmxpublic AdvanceTriggerPulsePolarity AdvanceTriggerPulsePolarity { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### AdvanceTriggerPulsePolarity

Indicates the polarity of the exported Advance Trigger.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AdvanceTriggerPulsePolarity](nationalinstruments-daqmx-advancetriggerpulsepolarity.html) AdvanceTriggerPulsePolarity { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-advancetriggerpulsewidth.html language=enus -->
## TOPIC 02115: AdvanceTriggerPulseWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-advancetriggerpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-advancetriggerpulsewidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the width of an exported Advance Trigger pulse. Specify this value in the units you specify with AdvanceTriggerPulseWidthUnits. SyntaxNamespace: NationalInstruments.DAQmxpublic double AdvanceTriggerPulseWidth { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe N

### AdvanceTriggerPulseWidth

Specifies the width of an exported Advance Trigger pulse. Specify this value in the units you specify with [AdvanceTriggerPulseWidthUnits](nationalinstruments-daqmx-exportsignals-advancetriggerpulsewidthunits.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double AdvanceTriggerPulseWidth { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-advancetriggerpulsewidthunits.html language=enus -->
## TOPIC 02116: AdvanceTriggerPulseWidthUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-advancetriggerpulsewidthunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-advancetriggerpulsewidthunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of AdvanceTriggerPulseWidth. SyntaxNamespace: NationalInstruments.DAQmxpublic AdvanceTriggerPulseWidthUnits AdvanceTriggerPulseWidthUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### AdvanceTriggerPulseWidthUnits

Specifies the units of [AdvanceTriggerPulseWidth](nationalinstruments-daqmx-exportsignals-advancetriggerpulsewidth.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AdvanceTriggerPulseWidthUnits](nationalinstruments-daqmx-advancetriggerpulsewidthunits.html) AdvanceTriggerPulseWidthUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-aiconvertclockoutputterminal.html language=enus -->
## TOPIC 02117: AIConvertClockOutputTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-aiconvertclockoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-aiconvertclockoutputterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the AI Convert Clock. SyntaxNamespace: NationalInstruments.DAQmxpublic string AIConvertClockOutputTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### AIConvertClockOutputTerminal

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) to which to route the AI Convert Clock.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string AIConvertClockOutputTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-aiconvertclockpulsepolarity.html language=enus -->
## TOPIC 02118: AIConvertClockPulsePolarity

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-aiconvertclockpulsepolarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-aiconvertclockpulsepolarity.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the polarity of the exported AI Convert Clock. The polarity is fixed and independent of the active edge of the source of the AI Convert Clock. SyntaxNamespace: NationalInstruments.DAQmxpublic AIConvertClockPulsePolarity AIConvertClockPulsePolarity { get; }ExceptionsTypeDescriptionNationalI

### AIConvertClockPulsePolarity

Indicates the polarity of the exported AI Convert Clock. The polarity is fixed and independent of the active edge of the source of the AI Convert Clock.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIConvertClockPulsePolarity](nationalinstruments-daqmx-aiconvertclockpulsepolarity.html) AIConvertClockPulsePolarity { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-aiholdcompleteeventoutputterminal.html language=enus -->
## TOPIC 02119: AIHoldCompleteEventOutputTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-aiholdcompleteeventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-aiholdcompleteeventoutputterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the AI Hold Complete Event. SyntaxNamespace: NationalInstruments.DAQmxpublic string AIHoldCompleteEventOutputTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### AIHoldCompleteEventOutputTerminal

Specifies the terminal to which to route the AI Hold Complete Event.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string AIHoldCompleteEventOutputTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-aiholdcompleteeventpulsepolarity.html language=enus -->
## TOPIC 02120: AIHoldCompleteEventPulsePolarity

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-aiholdcompleteeventpulsepolarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-aiholdcompleteeventpulsepolarity.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polarity of an exported AI Hold Complete Event pulse. SyntaxNamespace: NationalInstruments.DAQmxpublic AIHoldCompleteEventPulsePolarity AIHoldCompleteEventPulsePolarity { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### AIHoldCompleteEventPulsePolarity

Specifies the polarity of an exported AI Hold Complete Event pulse.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIHoldCompleteEventPulsePolarity](nationalinstruments-daqmx-aiholdcompleteeventpulsepolarity.html) AIHoldCompleteEventPulsePolarity { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-changedetectioneventoutputterminal.html language=enus -->
## TOPIC 02121: ChangeDetectionEventOutputTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-changedetectioneventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-changedetectioneventoutputterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the Change Detection Event. SyntaxNamespace: NationalInstruments.DAQmxpublic string ChangeDetectionEventOutputTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ChangeDetectionEventOutputTerminal

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) to which to route the Change Detection Event.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string ChangeDetectionEventOutputTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-changedetectioneventpulsepolarity.html language=enus -->
## TOPIC 02122: ChangeDetectionEventPulsePolarity

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-changedetectioneventpulsepolarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-changedetectioneventpulsepolarity.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polarity of an exported Change Detection Event pulse. SyntaxNamespace: NationalInstruments.DAQmxpublic ChangeDetectionEventPulsePolarity ChangeDetectionEventPulsePolarity { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ChangeDetectionEventPulsePolarity

Specifies the polarity of an exported Change Detection Event pulse.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [ChangeDetectionEventPulsePolarity](nationalinstruments-daqmx-changedetectioneventpulsepolarity.html) ChangeDetectionEventPulsePolarity { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-counteroutputeventidlestate.html language=enus -->
## TOPIC 02123: CounterOutputEventIdleState

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-counteroutputeventidlestate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-counteroutputeventidlestate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the initial state of the output terminal of the counter when CounterOutputEventOutputBehavior is Toggle. The terminal enters this state when NI-DAQmx commits the task. SyntaxNamespace: NationalInstruments.DAQmxpublic CounterOutputEventIdleState CounterOutputEventIdleState { get; set; }Rema

### CounterOutputEventIdleState

Specifies the initial state of the output terminal of the counter when [CounterOutputEventOutputBehavior](nationalinstruments-daqmx-exportsignals-counteroutputeventoutputbehavior.html) is [Toggle](nationalinstruments-daqmx-counteroutputeventoutputbehavior.html). The terminal enters this state when NI-DAQmx [commits](/csh?context=nidaqmx_mxcncpts_committedstate) the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CounterOutputEventIdleState](nationalinstruments-daqmx-counteroutputeventidlestate.html) CounterOutputEventIdleState { get; set; }

#### Remarks

The initial state of the terminal affects whether the first toggle is from low state to high state or from high state to low state.

NI-DAQmx ignores this property if [CounterOutputEventOutputBehavior](nationalinstruments-daqmx-exportsignals-counteroutputeventoutputbehavior.html) is [Pulse](nationalinstruments-daqmx-counteroutputeventoutputbehavior.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-counteroutputeventoutputbehavior.html language=enus -->
## TOPIC 02124: CounterOutputEventOutputBehavior

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-counteroutputeventoutputbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-counteroutputeventoutputbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the exported Counter Output Event pulses or changes from one state to the other when the counter reaches terminal count. SyntaxNamespace: NationalInstruments.DAQmxpublic CounterOutputEventOutputBehavior CounterOutputEventOutputBehavior { get; set; }RemarksUpon reaching terminal cou

### CounterOutputEventOutputBehavior

Specifies whether the exported Counter Output Event pulses or changes from one state to the other when the counter reaches terminal count.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CounterOutputEventOutputBehavior](nationalinstruments-daqmx-counteroutputeventoutputbehavior.html) CounterOutputEventOutputBehavior { get; set; }

#### Remarks

Upon reaching terminal count, the counter can issue a pulse. Use [CounterOutputEventPulsePolarity](nationalinstruments-daqmx-exportsignals-counteroutputeventpulsepolarity.html) to select a high or low pulse.

Upon reaching terminal count, the output terminal of the counter can change state, or toggle. For example, if the terminal is initially at a low state, it changes to high state and stays at the high state until the next terminal count. The terminal then changes to low state. Use [CounterOutputEventIdleState](nationalinstruments-daqmx-exportsignals-counteroutputeventidlestate.html) to select the initial state of the terminal.

When counting up, a counter reaches terminal count when it reaches the maximum value (2^24 - 1 for a 24-bit counter). When counting down, a counter reaches terminal count when it reaches 0.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-counteroutputeventoutputterminal.html language=enus -->
## TOPIC 02125: CounterOutputEventOutputTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-counteroutputeventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-counteroutputeventoutputterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the Counter Output Event. SyntaxNamespace: NationalInstruments.DAQmxpublic string CounterOutputEventOutputTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CounterOutputEventOutputTerminal

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) to which to route the Counter Output Event.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string CounterOutputEventOutputTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-counteroutputeventpulsepolarity.html language=enus -->
## TOPIC 02126: CounterOutputEventPulsePolarity

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-counteroutputeventpulsepolarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-counteroutputeventpulsepolarity.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polarity of the pulses at the output terminal of the counter when CounterOutputEventOutputBehavior is Pulse. NI-DAQmx ignores this property if CounterOutputEventOutputBehavior is Toggle. SyntaxNamespace: NationalInstruments.DAQmxpublic CounterOutputEventPulsePolarity CounterOutputEvent

### CounterOutputEventPulsePolarity

Specifies the polarity of the pulses at the output terminal of the counter when [CounterOutputEventOutputBehavior](nationalinstruments-daqmx-exportsignals-counteroutputeventoutputbehavior.html) is [Pulse](nationalinstruments-daqmx-counteroutputeventoutputbehavior.html). NI-DAQmx ignores this property if [CounterOutputEventOutputBehavior](nationalinstruments-daqmx-exportsignals-counteroutputeventoutputbehavior.html) is [Toggle](nationalinstruments-daqmx-counteroutputeventoutputbehavior.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CounterOutputEventPulsePolarity](nationalinstruments-daqmx-counteroutputeventpulsepolarity.html) CounterOutputEventPulsePolarity { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-dataactiveeventlevelactivelevel.html language=enus -->
## TOPIC 02127: DataActiveEventLevelActiveLevel

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-dataactiveeventlevelactivelevel.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-dataactiveeventlevelactivelevel.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polarity of the exported Data Active Event. SyntaxNamespace: NationalInstruments.DAQmxpublic DataActiveEventLevelActiveLevel DataActiveEventLevelActiveLevel { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DataActiveEventLevelActiveLevel

Specifies the polarity of the exported Data Active Event.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DataActiveEventLevelActiveLevel](nationalinstruments-daqmx-dataactiveeventlevelactivelevel.html) DataActiveEventLevelActiveLevel { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-dataactiveeventoutputterminal.html language=enus -->
## TOPIC 02128: DataActiveEventOutputTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-dataactiveeventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-dataactiveeventoutputterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to export the Data Active Event. SyntaxNamespace: NationalInstruments.DAQmxpublic string DataActiveEventOutputTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DataActiveEventOutputTerminal

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) to which to export the Data Active Event.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string DataActiveEventOutputTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-dividedsampleclocktimebaseoutputterminal.html language=enus -->
## TOPIC 02129: DividedSampleClockTimebaseOutputTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-dividedsampleclocktimebaseoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-dividedsampleclocktimebaseoutputterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the Divided Sample Clock Timebase. SyntaxNamespace: NationalInstruments.DAQmxpublic string DividedSampleClockTimebaseOutputTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DividedSampleClockTimebaseOutputTerminal

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) to which to route the Divided Sample Clock Timebase.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string DividedSampleClockTimebaseOutputTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-exporthardwaresignal__exportsignal-string.html language=enus -->
## TOPIC 02130: ExportHardwareSignal(ExportSignal, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-exporthardwaresignal__exportsignal-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-exporthardwaresignal__exportsignal-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Routes a control signal to the specified terminal. SyntaxNamespace: NationalInstruments.DAQmxpublic void ExportHardwareSignal(ExportSignal signal, string outputTerminal)RemarksBecause the output terminal can reside on the device that generates the control signal or on a different device, you can use

### ExportHardwareSignal(ExportSignal, string)

Routes a control signal to the specified terminal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ExportHardwareSignal(ExportSignal signal, string outputTerminal)

#### Remarks

Because the output terminal can reside on the device that generates the control signal or on a different device, you can use this method to share clocks and triggers between multiple devices.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| signal | ExportSignal | The trigger, clock, or event to export. |
| outputTerminal | string | The destination of the exported signal. You can also specify a comma-delimited list for multiple terminal names. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-handshakeeventdelay.html language=enus -->
## TOPIC 02131: HandshakeEventDelay

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-handshakeeventdelay.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-handshakeeventdelay.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of seconds to delay after the Handshake Trigger deasserts before asserting the Handshake Event. SyntaxNamespace: NationalInstruments.DAQmxpublic double HandshakeEventDelay { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an

### HandshakeEventDelay

Specifies the number of seconds to delay after the Handshake Trigger deasserts before asserting the Handshake Event.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double HandshakeEventDelay { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-handshakeeventinterlockedassertedlevel.html language=enus -->
## TOPIC 02132: HandshakeEventInterlockedAssertedLevel

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-handshakeeventinterlockedassertedlevel.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-handshakeeventinterlockedassertedlevel.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the asserted level of the exported Handshake Event if HandshakeEventOutputBehavior is Interlocked. SyntaxNamespace: NationalInstruments.DAQmxpublic HandshakeEventInterlockedAssertedLevel HandshakeEventInterlockedAssertedLevel { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.

### HandshakeEventInterlockedAssertedLevel

Specifies the asserted level of the exported Handshake Event if [HandshakeEventOutputBehavior](nationalinstruments-daqmx-exportsignals-handshakeeventoutputbehavior.html) is [Interlocked](nationalinstruments-daqmx-handshakeeventoutputbehavior.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [HandshakeEventInterlockedAssertedLevel](nationalinstruments-daqmx-handshakeeventinterlockedassertedlevel.html) HandshakeEventInterlockedAssertedLevel { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-handshakeeventinterlockedassertonstart.html language=enus -->
## TOPIC 02133: HandshakeEventInterlockedAssertOnStart

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-handshakeeventinterlockedassertonstart.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-handshakeeventinterlockedassertonstart.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies to assert the Handshake Event when the task starts if HandshakeEventOutputBehavior is Interlocked. SyntaxNamespace: NationalInstruments.DAQmxpublic bool HandshakeEventInterlockedAssertOnStart { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver re

### HandshakeEventInterlockedAssertOnStart

Specifies to assert the Handshake Event when the task starts if [HandshakeEventOutputBehavior](nationalinstruments-daqmx-exportsignals-handshakeeventoutputbehavior.html) is [Interlocked](nationalinstruments-daqmx-handshakeeventoutputbehavior.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool HandshakeEventInterlockedAssertOnStart { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-handshakeeventinterlockeddeassertdelay.html language=enus -->
## TOPIC 02134: HandshakeEventInterlockedDeassertDelay

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-handshakeeventinterlockeddeassertdelay.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-handshakeeventinterlockeddeassertdelay.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the amount of time to wait after the Handshake Trigger asserts before deasserting the Handshake Event if HandshakeEventOutputBehavior is Interlocked. SyntaxNamespace: NationalInstruments.DAQmxpublic double HandshakeEventInterlockedDeassertDelay { get; set; }ExceptionsTypeDescrip

### HandshakeEventInterlockedDeassertDelay

Specifies in seconds the amount of time to wait after the Handshake Trigger asserts before deasserting the Handshake Event if [HandshakeEventOutputBehavior](nationalinstruments-daqmx-exportsignals-handshakeeventoutputbehavior.html) is [Interlocked](nationalinstruments-daqmx-handshakeeventoutputbehavior.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double HandshakeEventInterlockedDeassertDelay { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-handshakeeventoutputbehavior.html language=enus -->
## TOPIC 02135: HandshakeEventOutputBehavior

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-handshakeeventoutputbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-handshakeeventoutputbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output behavior of the Handshake Event. SyntaxNamespace: NationalInstruments.DAQmxpublic HandshakeEventOutputBehavior HandshakeEventOutputBehavior { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### HandshakeEventOutputBehavior

Specifies the output behavior of the Handshake Event.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [HandshakeEventOutputBehavior](nationalinstruments-daqmx-handshakeeventoutputbehavior.html) HandshakeEventOutputBehavior { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-handshakeeventoutputterminal.html language=enus -->
## TOPIC 02136: HandshakeEventOutputTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-handshakeeventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-handshakeeventoutputterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the Handshake Event. SyntaxNamespace: NationalInstruments.DAQmxpublic string HandshakeEventOutputTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### HandshakeEventOutputTerminal

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) to which to route the Handshake Event.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string HandshakeEventOutputTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-handshakeeventpulsepolarity.html language=enus -->
## TOPIC 02137: HandshakeEventPulsePolarity

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-handshakeeventpulsepolarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-handshakeeventpulsepolarity.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polarity of the exported Handshake Event if HandshakeEventOutputBehavior is Pulse. SyntaxNamespace: NationalInstruments.DAQmxpublic HandshakeEventPulsePolarity HandshakeEventPulsePolarity { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver re

### HandshakeEventPulsePolarity

Specifies the polarity of the exported Handshake Event if [HandshakeEventOutputBehavior](nationalinstruments-daqmx-exportsignals-handshakeeventoutputbehavior.html) is [Pulse](nationalinstruments-daqmx-handshakeeventoutputbehavior.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [HandshakeEventPulsePolarity](nationalinstruments-daqmx-handshakeeventpulsepolarity.html) HandshakeEventPulsePolarity { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-handshakeeventpulsewidth.html language=enus -->
## TOPIC 02138: HandshakeEventPulseWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-handshakeeventpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-handshakeeventpulsewidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the pulse width of the exported Handshake Event if HandshakeEventOutputBehavior is Pulse. SyntaxNamespace: NationalInstruments.DAQmxpublic double HandshakeEventPulseWidth { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an

### HandshakeEventPulseWidth

Specifies in seconds the pulse width of the exported Handshake Event if [HandshakeEventOutputBehavior](nationalinstruments-daqmx-exportsignals-handshakeeventoutputbehavior.html) is [Pulse](nationalinstruments-daqmx-handshakeeventoutputbehavior.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double HandshakeEventPulseWidth { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-pausetriggerlevelactivelevel.html language=enus -->
## TOPIC 02139: PauseTriggerLevelActiveLevel

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-pausetriggerlevelactivelevel.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-pausetriggerlevelactivelevel.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the active level of the exported Pause Trigger. SyntaxNamespace: NationalInstruments.DAQmxpublic PauseTriggerLevelActiveLevel PauseTriggerLevelActiveLevel { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PauseTriggerLevelActiveLevel

Specifies the active level of the exported Pause Trigger.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [PauseTriggerLevelActiveLevel](nationalinstruments-daqmx-pausetriggerlevelactivelevel.html) PauseTriggerLevelActiveLevel { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-pausetriggeroutputterminal.html language=enus -->
## TOPIC 02140: PauseTriggerOutputTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-pausetriggeroutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-pausetriggeroutputterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the Pause Trigger. SyntaxNamespace: NationalInstruments.DAQmxpublic string PauseTriggerOutputTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PauseTriggerOutputTerminal

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) to which to route the Pause Trigger.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string PauseTriggerOutputTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-readyforstarteventlevelactivelevel.html language=enus -->
## TOPIC 02141: ReadyForStartEventLevelActiveLevel

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-readyforstarteventlevelactivelevel.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-readyforstarteventlevelactivelevel.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polarity of the exported Ready for Start Event. SyntaxNamespace: NationalInstruments.DAQmxpublic ReadyForStartEventLevelActiveLevel ReadyForStartEventLevelActiveLevel { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ReadyForStartEventLevelActiveLevel

Specifies the polarity of the exported Ready for Start Event.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [ReadyForStartEventLevelActiveLevel](nationalinstruments-daqmx-readyforstarteventlevelactivelevel.html) ReadyForStartEventLevelActiveLevel { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-readyforstarteventoutputterminal.html language=enus -->
## TOPIC 02142: ReadyForStartEventOutputTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-readyforstarteventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-readyforstarteventoutputterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the Ready for Start Event. SyntaxNamespace: NationalInstruments.DAQmxpublic string ReadyForStartEventOutputTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ReadyForStartEventOutputTerminal

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) to which to route the Ready for Start Event.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string ReadyForStartEventOutputTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-readyfortransfereventdeassertcondition.html language=enus -->
## TOPIC 02143: ReadyForTransferEventDeassertCondition

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-readyfortransfereventdeassertcondition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-readyfortransfereventdeassertcondition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies when the ready for transfer event deasserts. SyntaxNamespace: NationalInstruments.DAQmxpublic ReadyForTransferEventDeassertCondition ReadyForTransferEventDeassertCondition { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ReadyForTransferEventDeassertCondition

Specifies when the ready for transfer event deasserts.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [ReadyForTransferEventDeassertCondition](nationalinstruments-daqmx-readyfortransfereventdeassertcondition.html) ReadyForTransferEventDeassertCondition { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-readyfortransfereventdeassertconditioncustomthreshold.html language=enus -->
## TOPIC 02144: ReadyForTransferEventDeassertConditionCustomThreshold

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-readyfortransfereventdeassertconditioncustomthreshold.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-readyfortransfereventdeassertconditioncustomthreshold.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in samples the threshold below which the Ready for Transfer Event deasserts. This threshold is an amount of space available in the onboard memory of the device. ReadyForTransferEventDeassertCondition must be OnboardMemoryCustomThreshold to use a custom threshold. SyntaxNamespace: NationalI

### ReadyForTransferEventDeassertConditionCustomThreshold

Specifies in samples the threshold below which the Ready for Transfer Event deasserts. This threshold is an amount of space available in the onboard memory of the device. [ReadyForTransferEventDeassertCondition](nationalinstruments-daqmx-exportsignals-readyfortransfereventdeassertcondition.html) must be [OnboardMemoryCustomThreshold](nationalinstruments-daqmx-readyfortransfereventdeassertcondition.html) to use a custom threshold.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long ReadyForTransferEventDeassertConditionCustomThreshold { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-readyfortransfereventlevelactivelevel.html language=enus -->
## TOPIC 02145: ReadyForTransferEventLevelActiveLevel

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-readyfortransfereventlevelactivelevel.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-readyfortransfereventlevelactivelevel.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the active level of the exported Ready for Transfer Event. SyntaxNamespace: NationalInstruments.DAQmxpublic ReadyForTransferEventLevelActiveLevel ReadyForTransferEventLevelActiveLevel { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned a

### ReadyForTransferEventLevelActiveLevel

Specifies the active level of the exported Ready for Transfer Event.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [ReadyForTransferEventLevelActiveLevel](nationalinstruments-daqmx-readyfortransfereventlevelactivelevel.html) ReadyForTransferEventLevelActiveLevel { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-readyfortransfereventoutputterminal.html language=enus -->
## TOPIC 02146: ReadyForTransferEventOutputTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-readyfortransfereventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-readyfortransfereventoutputterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the Ready for Transfer Event. SyntaxNamespace: NationalInstruments.DAQmxpublic string ReadyForTransferEventOutputTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ReadyForTransferEventOutputTerminal

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) to which to route the Ready for Transfer Event.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string ReadyForTransferEventOutputTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-referenceclock10mhzoutputterminal.html language=enus -->
## TOPIC 02147: ReferenceClock10MHzOutputTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-referenceclock10mhzoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-referenceclock10mhzoutputterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the 10MHz Clock. SyntaxNamespace: NationalInstruments.DAQmxpublic string ReferenceClock10MHzOutputTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ReferenceClock10MHzOutputTerminal

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) to which to route the 10MHz Clock.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string ReferenceClock10MHzOutputTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-referencetriggeroutputterminal.html language=enus -->
## TOPIC 02148: ReferenceTriggerOutputTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-referencetriggeroutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-referencetriggeroutputterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the Reference Trigger. SyntaxNamespace: NationalInstruments.DAQmxpublic string ReferenceTriggerOutputTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ReferenceTriggerOutputTerminal

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) to which to route the Reference Trigger.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string ReferenceTriggerOutputTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-referencetriggerpulsepolarity.html language=enus -->
## TOPIC 02149: ReferenceTriggerPulsePolarity

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-referencetriggerpulsepolarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-referencetriggerpulsepolarity.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polarity of the exported Reference Trigger. SyntaxNamespace: NationalInstruments.DAQmxpublic ReferenceTriggerPulsePolarity ReferenceTriggerPulsePolarity { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ReferenceTriggerPulsePolarity

Specifies the polarity of the exported Reference Trigger.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [ReferenceTriggerPulsePolarity](nationalinstruments-daqmx-referencetriggerpulsepolarity.html) ReferenceTriggerPulsePolarity { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-sampleclockdelayoffset.html language=enus -->
## TOPIC 02150: SampleClockDelayOffset

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-sampleclockdelayoffset.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-sampleclockdelayoffset.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the amount of time to offset the exported Sample clock. Refer to timing diagrams for generation applications in the device documentation for more information about this value. SyntaxNamespace: NationalInstruments.DAQmxpublic double SampleClockDelayOffset { get; set; }ExceptionsT

### SampleClockDelayOffset

Specifies in seconds the amount of time to offset the exported Sample clock. Refer to timing diagrams for generation applications in the device documentation for more information about this value.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double SampleClockDelayOffset { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-sampleclockoutputbehavior.html language=enus -->
## TOPIC 02151: SampleClockOutputBehavior

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-sampleclockoutputbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-sampleclockoutputbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the exported Sample Clock issues a pulse at the beginning of a sample or changes to a high state for the duration of the sample. SyntaxNamespace: NationalInstruments.DAQmxpublic SampleClockOutputBehavior SampleClockOutputBehavior { get; set; }RemarksE Series devices might require m

### SampleClockOutputBehavior

Specifies whether the exported Sample Clock issues a pulse at the beginning of a sample or changes to a high state for the duration of the sample.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [SampleClockOutputBehavior](nationalinstruments-daqmx-sampleclockoutputbehavior.html) SampleClockOutputBehavior { get; set; }

#### Remarks

E Series devices might require many AI Convert Clock pulses to acquire one sample. Each pulse of the Sample Clock initiates the acquisition of one sample per channel in the task. Each sample per channel requires a pulse from the AI Convert Clock.

This property is valid for the AI Sample Clock only.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-sampleclockoutputterminal.html language=enus -->
## TOPIC 02152: SampleClockOutputTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-sampleclockoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-sampleclockoutputterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the Sample Clock. SyntaxNamespace: NationalInstruments.DAQmxpublic string SampleClockOutputTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### SampleClockOutputTerminal

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) to which to route the Sample Clock.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string SampleClockOutputTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-sampleclockpulsepolarity.html language=enus -->
## TOPIC 02153: SampleClockPulsePolarity

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-sampleclockpulsepolarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-sampleclockpulsepolarity.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polarity of the exported Sample Clock if SampleClockOutputBehavior is Pulse. SyntaxNamespace: NationalInstruments.DAQmxpublic SampleClockPulsePolarity SampleClockPulsePolarity { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an er

### SampleClockPulsePolarity

Specifies the polarity of the exported Sample Clock if [SampleClockOutputBehavior](nationalinstruments-daqmx-exportsignals-sampleclockoutputbehavior.html) is [Pulse](nationalinstruments-daqmx-sampleclockoutputbehavior.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [SampleClockPulsePolarity](nationalinstruments-daqmx-sampleclockpulsepolarity.html) SampleClockPulsePolarity { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-sampleclocktimebaseoutputterminal.html language=enus -->
## TOPIC 02154: SampleClockTimebaseOutputTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-sampleclocktimebaseoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-sampleclocktimebaseoutputterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the Sample Clock Timebase. SyntaxNamespace: NationalInstruments.DAQmxpublic string SampleClockTimebaseOutputTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### SampleClockTimebaseOutputTerminal

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) to which to route the Sample Clock Timebase.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string SampleClockTimebaseOutputTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-starttriggeroutputterminal.html language=enus -->
## TOPIC 02155: StartTriggerOutputTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-starttriggeroutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-starttriggeroutputterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the Start Trigger. SyntaxNamespace: NationalInstruments.DAQmxpublic string StartTriggerOutputTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### StartTriggerOutputTerminal

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) to which to route the Start Trigger.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string StartTriggerOutputTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-starttriggerpulsepolarity.html language=enus -->
## TOPIC 02156: StartTriggerPulsePolarity

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-starttriggerpulsepolarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-starttriggerpulsepolarity.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polarity of the exported Start Trigger. SyntaxNamespace: NationalInstruments.DAQmxpublic StartTriggerPulsePolarity StartTriggerPulsePolarity { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### StartTriggerPulsePolarity

Specifies the polarity of the exported Start Trigger.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [StartTriggerPulsePolarity](nationalinstruments-daqmx-starttriggerpulsepolarity.html) StartTriggerPulsePolarity { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-synchronizationpulseeventoutputterminal.html language=enus -->
## TOPIC 02157: SynchronizationPulseEventOutputTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-synchronizationpulseeventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-synchronizationpulseeventoutputterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the Synchronization Pulse Event. SyntaxNamespace: NationalInstruments.DAQmxpublic string SynchronizationPulseEventOutputTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### SynchronizationPulseEventOutputTerminal

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) to which to route the Synchronization Pulse Event.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string SynchronizationPulseEventOutputTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-timebase20mhzoutputterminal.html language=enus -->
## TOPIC 02158: Timebase20MHzOutputTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-timebase20mhzoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-timebase20mhzoutputterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the 20MHz Timebase. SyntaxNamespace: NationalInstruments.DAQmxpublic string Timebase20MHzOutputTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Timebase20MHzOutputTerminal

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) to which to route the 20MHz Timebase.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Timebase20MHzOutputTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-tostring.html language=enus -->
## TOPIC 02159: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-tostring.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the object. SyntaxNamespace: NationalInstruments.DAQmxpublic override string ToString()RemarksOverrides ToString. ReturnsA string representation of the object.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ToString()

Returns a string representation of the object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override string ToString()

#### Remarks

Overrides ToString.

#### Returns

A string representation of the object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals-watchdogexpiredeventoutputterminal.html language=enus -->
## TOPIC 02160: WatchdogExpiredEventOutputTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals-watchdogexpiredeventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals-watchdogexpiredeventoutputterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the Watchdog Timer Expired Event. SyntaxNamespace: NationalInstruments.DAQmxpublic string WatchdogExpiredEventOutputTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### WatchdogExpiredEventOutputTerminal

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) to which to route the [Watchdog](nationalinstruments-daqmx-watchdog.html) Timer Expired Event.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string WatchdogExpiredEventOutputTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExportSignals Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-exportsignals.html language=enus -->
## TOPIC 02161: ExportSignals Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-exportsignals.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-exportsignals.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Encapsulates the signals that are available for routing off of the DAQ device, the properties that define which terminal the signals are routed to, and the programmable characteristics of the signals for a Task. Derives fromMarshalByRefObjectIFilteredTypeDescriptorSyntaxNamespace: NationalInstrument

### ExportSignals Class

Encapsulates the signals that are available for routing off of the DAQ device, the properties that define which terminal the signals are routed to, and the [programmable characteristics](/csh?context=nidaqmx_mxcncpts_exportsig) of the signals for a [Task](nationalinstruments-daqmx-task.html).

#### Derives from

- MarshalByRefObject
- IFilteredTypeDescriptor

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class ExportSignals : MarshalByRefObject, IFilteredTypeDescriptor

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| AdvanceCompleteEventDelay | Specifies the output signal delay in periods of the sample clock. |
| AdvanceCompleteEventOutputTerminal | Specifies the terminal to which to route the Advance Complete Event. |
| AdvanceCompleteEventPulsePolarity | Specifies the polarity of the exported Advance Complete Event. |
| AdvanceCompleteEventPulseWidth | Specifies the width of the exported Advance Complete Event pulse. |
| AdvanceTriggerOutputTerminal | Specifies the terminal to which to route the Advance Trigger. |
| AdvanceTriggerPulsePolarity | Indicates the polarity of the exported Advance Trigger. |
| AdvanceTriggerPulseWidth | Specifies the width of an exported Advance Trigger pulse. Specify this value in the units you specify with AdvanceTriggerPulseWidthUnits. |
| AdvanceTriggerPulseWidthUnits | Specifies the units of AdvanceTriggerPulseWidth. |
| AIConvertClockOutputTerminal | Specifies the terminal to which to route the AI Convert Clock. |
| AIConvertClockPulsePolarity | Indicates the polarity of the exported AI Convert Clock. The polarity is fixed and independent of the active edge of the source of the AI Convert Clock. |
| AIHoldCompleteEventOutputTerminal | Specifies the terminal to which to route the AI Hold Complete Event. |
| AIHoldCompleteEventPulsePolarity | Specifies the polarity of an exported AI Hold Complete Event pulse. |
| ChangeDetectionEventOutputTerminal | Specifies the terminal to which to route the Change Detection Event. |
| ChangeDetectionEventPulsePolarity | Specifies the polarity of an exported Change Detection Event pulse. |
| CounterOutputEventIdleState | Specifies the initial state of the output terminal of the counter when CounterOutputEventOutputBehavior is Toggle. The terminal enters this state when NI-DAQmx commits the task. |
| CounterOutputEventOutputBehavior | Specifies whether the exported Counter Output Event pulses or changes from one state to the other when the counter reaches terminal count. |
| CounterOutputEventOutputTerminal | Specifies the terminal to which to route the Counter Output Event. |
| CounterOutputEventPulsePolarity | Specifies the polarity of the pulses at the output terminal of the counter when CounterOutputEventOutputBehavior is Pulse. NI-DAQmx ignores this property if CounterOutputEventOutputBehavior is Toggle. |
| DataActiveEventLevelActiveLevel | Specifies the polarity of the exported Data Active Event. |
| DataActiveEventOutputTerminal | Specifies the terminal to which to export the Data Active Event. |
| DividedSampleClockTimebaseOutputTerminal | Specifies the terminal to which to route the Divided Sample Clock Timebase. |
| HandshakeEventDelay | Specifies the number of seconds to delay after the Handshake Trigger deasserts before asserting the Handshake Event. |
| HandshakeEventInterlockedAssertedLevel | Specifies the asserted level of the exported Handshake Event if HandshakeEventOutputBehavior is Interlocked. |
| HandshakeEventInterlockedAssertOnStart | Specifies to assert the Handshake Event when the task starts if HandshakeEventOutputBehavior is Interlocked. |
| HandshakeEventInterlockedDeassertDelay | Specifies in seconds the amount of time to wait after the Handshake Trigger asserts before deasserting the Handshake Event if HandshakeEventOutputBehavior is Interlocked. |
| HandshakeEventOutputBehavior | Specifies the output behavior of the Handshake Event. |
| HandshakeEventOutputTerminal | Specifies the terminal to which to route the Handshake Event. |
| HandshakeEventPulsePolarity | Specifies the polarity of the exported Handshake Event if HandshakeEventOutputBehavior is Pulse. |
| HandshakeEventPulseWidth | Specifies in seconds the pulse width of the exported Handshake Event if HandshakeEventOutputBehavior is Pulse. |
| PauseTriggerLevelActiveLevel | Specifies the active level of the exported Pause Trigger. |
| PauseTriggerOutputTerminal | Specifies the terminal to which to route the Pause Trigger. |
| ReadyForStartEventLevelActiveLevel | Specifies the polarity of the exported Ready for Start Event. |
| ReadyForStartEventOutputTerminal | Specifies the terminal to which to route the Ready for Start Event. |
| ReadyForTransferEventDeassertCondition | Specifies when the ready for transfer event deasserts. |
| ReadyForTransferEventDeassertConditionCustomThreshold | Specifies in samples the threshold below which the Ready for Transfer Event deasserts. This threshold is an amount of space available in the onboard memory of the device. ReadyForTransferEventDeassertCondition must be OnboardMemoryCustomThreshold to use a custom threshold. |
| ReadyForTransferEventLevelActiveLevel | Specifies the active level of the exported Ready for Transfer Event. |
| ReadyForTransferEventOutputTerminal | Specifies the terminal to which to route the Ready for Transfer Event. |
| ReferenceClock10MHzOutputTerminal | Specifies the terminal to which to route the 10MHz Clock. |
| ReferenceTriggerOutputTerminal | Specifies the terminal to which to route the Reference Trigger. |
| ReferenceTriggerPulsePolarity | Specifies the polarity of the exported Reference Trigger. |
| SampleClockDelayOffset | Specifies in seconds the amount of time to offset the exported Sample clock. Refer to timing diagrams for generation applications in the device documentation for more information about this value. |
| SampleClockOutputBehavior | Specifies whether the exported Sample Clock issues a pulse at the beginning of a sample or changes to a high state for the duration of the sample. |
| SampleClockOutputTerminal | Specifies the terminal to which to route the Sample Clock. |
| SampleClockPulsePolarity | Specifies the polarity of the exported Sample Clock if SampleClockOutputBehavior is Pulse. |
| SampleClockTimebaseOutputTerminal | Specifies the terminal to which to route the Sample Clock Timebase. |
| StartTriggerOutputTerminal | Specifies the terminal to which to route the Start Trigger. |
| StartTriggerPulsePolarity | Specifies the polarity of the exported Start Trigger. |
| SynchronizationPulseEventOutputTerminal | Specifies the terminal to which to route the Synchronization Pulse Event. |
| Timebase20MHzOutputTerminal | Specifies the terminal to which to route the 20MHz Timebase. |
| WatchdogExpiredEventOutputTerminal | Specifies the terminal to which to route the Watchdog Timer Expired Event. |

#### Methods

| Name | Description |
| --- | --- |
| ExportHardwareSignal(ExportSignal, string) | Routes a control signal to the specified terminal. |
| ToString() | Returns a string representation of the object. |

#### See Also

- Task
- ExportSignals

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust1102__double-double.html language=enus -->
## TOPIC 02162: Adjust1102(double, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust1102__double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust1102__double-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SCXI-1102 module. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust1102(double referenceVoltage, double measuredOutput)RemarksYou must connect a known voltage to the module. You must specify the voltage with referenceVoltage and specify th

### Adjust1102(double, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_devcalibrate) constants for an SCXI-1102 module.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust1102(double referenceVoltage, double measuredOutput)

#### Remarks

You must connect a known voltage to the module. You must specify the voltage with *referenceVoltage*  and specify the measured output with *measuredOutput* .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| referenceVoltage | double | The known voltage, in volts, to use as a reference for calibration. |
| measuredOutput | double | The measured output, in volts, for the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust1104__double-double.html language=enus -->
## TOPIC 02163: Adjust1104(double, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust1104__double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust1104__double-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SCXI-1104 module. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust1104(double referenceVoltage, double measuredOutput)RemarksYou must connect a known voltage to the module. You must specify the voltage with referenceVoltage and specify th

### Adjust1104(double, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_devcalibrate) constants for an SCXI-1104 module.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust1104(double referenceVoltage, double measuredOutput)

#### Remarks

You must connect a known voltage to the module. You must specify the voltage with *referenceVoltage*  and specify the measured output with *measuredOutput* .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| referenceVoltage | double | The known voltage, in volts, to use as a reference for calibration. |
| measuredOutput | double | The measured output, in volts, for the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust1112__double-double.html language=enus -->
## TOPIC 02164: Adjust1112(double, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust1112__double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust1112__double-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SCXI-1112 module. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust1112(double referenceVoltage, double measuredOutput)RemarksYou must connect a known voltage to the module. You must specify the voltage with referenceVoltage and specify th

### Adjust1112(double, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_devcalibrate) constants for an SCXI-1112 module.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust1112(double referenceVoltage, double measuredOutput)

#### Remarks

You must connect a known voltage to the module. You must specify the voltage with *referenceVoltage*  and specify the measured output with *measuredOutput* .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| referenceVoltage | double | The known voltage, in volts, to use as a reference for calibration. |
| measuredOutput | double | The measured output, in volts, for the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust1122__double-double.html language=enus -->
## TOPIC 02165: Adjust1122(double, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust1122__double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust1122__double-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SCXI-1122 module. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust1122(double referenceVoltage, double measuredOutput)RemarksYou must connect a known voltage to the module. You must specify the voltage with referenceVoltage and specify th

### Adjust1122(double, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_devcalibrate) constants for an SCXI-1122 module.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust1122(double referenceVoltage, double measuredOutput)

#### Remarks

You must connect a known voltage to the module. You must specify the voltage with *referenceVoltage*  and specify the measured output with *measuredOutput* .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| referenceVoltage | double | The known voltage, in volts, to use as a reference for calibration. |
| measuredOutput | double | The measured output, in volts, for the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust1124__double.html language=enus -->
## TOPIC 02166: Adjust1124(double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust1124__double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust1124__double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SCXI-1124 module. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust1124(double measuredOutput)RemarksYou must connect a known voltage to the module. You must specify the voltage with referenceVoltage and specify the measured output with me

### Adjust1124(double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_devcalibrate) constants for an SCXI-1124 module.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust1124(double measuredOutput)

#### Remarks

You must connect a known voltage to the module. You must specify the voltage with *referenceVoltage*  and specify the measured output with *measuredOutput* .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| measuredOutput | double | A DMM measured reading of the output of the SCXI-1124 after the call. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust1125__double-double.html language=enus -->
## TOPIC 02167: Adjust1125(double, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust1125__double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust1125__double-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SCXI-1125 module. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust1125(double referenceVoltage, double measuredOutput)RemarksYou must connect a known voltage to the module. You must specify the voltage with referenceVoltage and specify th

### Adjust1125(double, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_devcalibrate) constants for an SCXI-1125 module.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust1125(double referenceVoltage, double measuredOutput)

#### Remarks

You must connect a known voltage to the module. You must specify the voltage with *referenceVoltage*  and specify the measured output with *measuredOutput* .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| referenceVoltage | double | The known voltage, in volts, to use as a reference for calibration. |
| measuredOutput | double | The measured output, in volts, for the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust1126__double-double.html language=enus -->
## TOPIC 02168: Adjust1126(double, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust1126__double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust1126__double-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SCXI-1126 module. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust1126(double referenceFrequency, double measuredOutput)RemarksYou must connect a known voltage to the module. You must specify the voltage with referenceVoltage and specify

### Adjust1126(double, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_devcalibrate) constants for an SCXI-1126 module.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust1126(double referenceFrequency, double measuredOutput)

#### Remarks

You must connect a known voltage to the module. You must specify the voltage with *referenceVoltage*  and specify the measured output with *measuredOutput* .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| referenceFrequency | double | The frequency, in Hertz, of the signal to use as a reference for calibration. |
| measuredOutput | double | The measured output, in volts, for the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust1141__double-double.html language=enus -->
## TOPIC 02169: Adjust1141(double, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust1141__double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust1141__double-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SCXI-1141 module. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust1141(double referenceVoltage, double measuredOutput)RemarksYou must connect a known voltage to the module. You must specify the voltage with referenceVoltage and specify th

### Adjust1141(double, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_devcalibrate) constants for an SCXI-1141 module.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust1141(double referenceVoltage, double measuredOutput)

#### Remarks

You must connect a known voltage to the module. You must specify the voltage with *referenceVoltage*  and specify the measured output with *measuredOutput* .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| referenceVoltage | double | The known voltage, in volts, to use as a reference for calibration. |
| measuredOutput | double | The measured output, in volts, for the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust1142__double-double.html language=enus -->
## TOPIC 02170: Adjust1142(double, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust1142__double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust1142__double-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SCXI-1142 module. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust1142(double referenceVoltage, double measuredOutput)RemarksYou must connect a known voltage to the module. You must specify the voltage with referenceVoltage and specify th

### Adjust1142(double, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_devcalibrate) constants for an SCXI-1142 module.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust1142(double referenceVoltage, double measuredOutput)

#### Remarks

You must connect a known voltage to the module. You must specify the voltage with *referenceVoltage*  and specify the measured output with *measuredOutput* .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| referenceVoltage | double | The known voltage, in volts, to use as a reference for calibration. |
| measuredOutput | double | The measured output, in volts, for the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust1143__double-double.html language=enus -->
## TOPIC 02171: Adjust1143(double, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust1143__double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust1143__double-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SCXI-1143 module. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust1143(double referenceVoltage, double measuredOutput)RemarksYou must connect a known voltage to the module. You must specify the voltage with referenceVoltage and specify th

### Adjust1143(double, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_devcalibrate) constants for an SCXI-1143 module.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust1143(double referenceVoltage, double measuredOutput)

#### Remarks

You must connect a known voltage to the module. You must specify the voltage with *referenceVoltage*  and specify the measured output with *measuredOutput* .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| referenceVoltage | double | The known voltage, in volts, to use as a reference for calibration. |
| measuredOutput | double | The measured output, in volts, for the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust11601__string-double.html language=enus -->
## TOPIC 02172: Adjust11601(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust11601__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust11601__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts theexternal calibrationconstants for an NI FD-11601 device bank. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust11601(string physicalChannels, double value)RemarksRefer to thecalibration procedure for your devicefor detailed calibration instructions. After you commit the calibra

### Adjust11601(string, double)

Adjusts the[external calibration](/csh?context=nidaqmx_mxcncpts_calibration)constants for an NI FD-11601 device bank.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust11601(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust11603__string-double.html language=enus -->
## TOPIC 02173: Adjust11603(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust11603__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust11603__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts theexternal calibrationconstants for an NI FD-11603 device bank. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust11603(string physicalChannels, double value)RemarksRefer to thecalibration procedure for your devicefor detailed calibration instructions. After you commit the calibra

### Adjust11603(string, double)

Adjusts the[external calibration](/csh?context=nidaqmx_mxcncpts_calibration)constants for an NI FD-11603 device bank.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust11603(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust11605__string-double.html language=enus -->
## TOPIC 02174: Adjust11605(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust11605__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust11605__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts theexternal calibrationconstants for an NI FD-11605 device bank. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust11605(string physicalChannels, double value)RemarksRefer to thecalibration procedure for your devicefor detailed calibration instructions. After you commit the calibra

### Adjust11605(string, double)

Adjusts the[external calibration](/csh?context=nidaqmx_mxcncpts_calibration)constants for an NI FD-11605 device bank.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust11605(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust11613__string-double.html language=enus -->
## TOPIC 02175: Adjust11613(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust11613__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust11613__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts theexternal calibrationconstants for an NI FD-11613 device bank. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust11613(string physicalChannels, double value)RemarksRefer to thecalibration procedure for your devicefor detailed calibration instructions. After you commit the calibra

### Adjust11613(string, double)

Adjusts the[external calibration](/csh?context=nidaqmx_mxcncpts_calibration)constants for an NI FD-11613 device bank.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust11613(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust11614__string-double.html language=enus -->
## TOPIC 02176: Adjust11614(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust11614__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust11614__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts theexternal calibrationconstants for an NI FD-11614 device bank. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust11614(string physicalChannels, double value)RemarksRefer to thecalibration procedure for your devicefor detailed calibration instructions. After you commit the calibra

### Adjust11614(string, double)

Adjusts the[external calibration](/csh?context=nidaqmx_mxcncpts_calibration)constants for an NI FD-11614 device bank.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust11614(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust11634__string-double.html language=enus -->
## TOPIC 02177: Adjust11634(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust11634__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust11634__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts theexternal calibrationconstants for an NI FD-11634 device bank. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust11634(string physicalChannels, double value)RemarksRefer to thecalibration procedure for your devicefor detailed calibration instructions. After you commit the calibra

### Adjust11634(string, double)

Adjusts the[external calibration](/csh?context=nidaqmx_mxcncpts_calibration)constants for an NI FD-11634 device bank.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust11634(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust11637__double-out-out-out.html language=enus -->
## TOPIC 02178: Adjust11637(double, out double, out double, out double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust11637__double-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust11637__double-out-out-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts theexternal calibrationconstants for an NI FD-11637 device bank. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust11637(double value, out double actualReading, out double asFoundGainError, out double asFoundOffsetError)RemarksRefer to thecalibration procedure for your devicefor de

### Adjust11637(double, out double, out double, out double)

Adjusts the[external calibration](/csh?context=nidaqmx_mxcncpts_calibration)constants for an NI FD-11637 device bank.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust11637(double value, out double actualReading, out double asFoundGainError, out double asFoundOffsetError)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| value | double | Specifies the reference value measured using a calibrator. |
| actualReading | out double | Specifies the reading that the device being calibrated acquired. |
| asFoundGainError | out double | Specifies the gain error found for the device being calibrated. |
| asFoundOffsetError | out double | Specifies the offset error found for the device being calibrated. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust1502__double-double.html language=enus -->
## TOPIC 02179: Adjust1502(double, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust1502__double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust1502__double-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SCXI-1502 module. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust1502(double referenceVoltage, double measuredOutput)RemarksYou must connect a known voltage to the module. You must specify the voltage with referenceVoltage and specify th

### Adjust1502(double, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_devcalibrate) constants for an SCXI-1502 module.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust1502(double referenceVoltage, double measuredOutput)

#### Remarks

You must connect a known voltage to the module. You must specify the voltage with *referenceVoltage*  and specify the measured output with *measuredOutput* .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| referenceVoltage | double | The known voltage, in volts, to use as a reference for calibration. |
| measuredOutput | double | The measured output, in volts, for the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust1503__double-double.html language=enus -->
## TOPIC 02180: Adjust1503(double, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust1503__double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust1503__double-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SCXI-1503 module. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust1503(double referenceVoltage, double measuredOutput)RemarksYou must connect a known voltage to the module. You must specify the voltage with referenceVoltage and specify th

### Adjust1503(double, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_devcalibrate) constants for an SCXI-1503 module.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust1503(double referenceVoltage, double measuredOutput)

#### Remarks

You must connect a known voltage to the module. You must specify the voltage with *referenceVoltage*  and specify the measured output with *measuredOutput* .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| referenceVoltage | double | The known voltage, in volts, to use as a reference for calibration. |
| measuredOutput | double | The measured output, in volts, for the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust1503current__string-double.html language=enus -->
## TOPIC 02181: Adjust1503Current(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust1503current__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust1503current__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SCXI-1503 module. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust1503Current(string physicalChannels, double measuredCurrent)RemarksYou must connect a known voltage to the module. You must specify the voltage with referenceVoltage and sp

### Adjust1503Current(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_devcalibrate) constants for an SCXI-1503 module.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust1503Current(string physicalChannels, double measuredCurrent)

#### Remarks

You must connect a known voltage to the module. You must specify the voltage with *referenceVoltage*  and specify the measured output with *measuredOutput* .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel to calibrate. |
| measuredCurrent | double | Specifies the current measured for the specified channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust15100__double.html language=enus -->
## TOPIC 02182: Adjust15100(double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust15100__double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust15100__double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI TS-15100 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust15100(double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration, you cannot undo it.

### Adjust15100(double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI TS-15100 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust15100(double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust15110__string-double.html language=enus -->
## TOPIC 02183: Adjust15110(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust15110__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust15110__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI TS-15110 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust15110(string physicalChannels, double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibrat

### Adjust15110(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI TS-15110 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust15110(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust15200__string-double-powercalibrationtype.html language=enus -->
## TOPIC 02184: Adjust15200(string, double, PowerCalibrationType)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust15200__string-double-powercalibrationtype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust15200__string-double-powercalibrationtype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI TS-15200 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust15200(string physicalChannels, double referenceValue, PowerCalibrationType calibrationType)RemarksRefer to the calibration procedure for your device for detailed calibrat

### Adjust15200(string, double, PowerCalibrationType)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI TS-15200 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust15200(string physicalChannels, double referenceValue, PowerCalibrationType calibrationType)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| referenceValue | double | Specifies the reference value measured using a calibrator. |
| calibrationType | PowerCalibrationType | Specifies the calibration type. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust1520__double-double.html language=enus -->
## TOPIC 02185: Adjust1520(double, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust1520__double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust1520__double-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SCXI-1520 module. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust1520(double referenceVoltage, double measuredOutput)RemarksYou must connect a known voltage to the module. You must specify the voltage with referenceVoltage and specify th

### Adjust1520(double, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_devcalibrate) constants for an SCXI-1520 module.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust1520(double referenceVoltage, double measuredOutput)

#### Remarks

You must connect a known voltage to the module. You must specify the voltage with *referenceVoltage*  and specify the measured output with *measuredOutput* .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| referenceVoltage | double | The known voltage, in volts, to use as a reference for calibration. |
| measuredOutput | double | The measured output, in volts, for the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust1521__double-double.html language=enus -->
## TOPIC 02186: Adjust1521(double, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust1521__double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust1521__double-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SCXI-1521 module. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust1521(double referenceVoltage, double measuredOutput)RemarksYou must connect a known voltage to the module. You must specify the voltage with referenceVoltage and specify th

### Adjust1521(double, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_devcalibrate) constants for an SCXI-1521 module.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust1521(double referenceVoltage, double measuredOutput)

#### Remarks

You must connect a known voltage to the module. You must specify the voltage with *referenceVoltage*  and specify the measured output with *measuredOutput* .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| referenceVoltage | double | The known voltage, in volts, to use as a reference for calibration. |
| measuredOutput | double | The measured output, in volts, for the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust153x__double-double.html language=enus -->
## TOPIC 02187: Adjust153x(double, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust153x__double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust153x__double-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SCXI-1530 or SCXI-1531 module. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust153x(double referenceVoltage, double measuredOutput)RemarksYou must connect a known voltage to the module. You must specify the voltage with referenceVoltage a

### Adjust153x(double, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_devcalibrate) constants for an SCXI-1530 or SCXI-1531 module.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust153x(double referenceVoltage, double measuredOutput)

#### Remarks

You must connect a known voltage to the module. You must specify the voltage with *referenceVoltage*  and specify the measured output with *measuredOutput* .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| referenceVoltage | double | The known voltage, in volts, to use as a reference for calibration. |
| measuredOutput | double | The measured output, in volts, for the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust1540__double-double-inputcalibrationsource.html language=enus -->
## TOPIC 02188: Adjust1540(double, double, InputCalibrationSource)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust1540__double-double-inputcalibrationsource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust1540__double-double-inputcalibrationsource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SCXI-1540 module. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust1540(double referenceVoltage, double measuredOutput, InputCalibrationSource calibrationSource)RemarksYou must connect a known voltage to the module. You must specify the vo

### Adjust1540(double, double, InputCalibrationSource)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_devcalibrate) constants for an SCXI-1540 module.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust1540(double referenceVoltage, double measuredOutput, InputCalibrationSource calibrationSource)

#### Remarks

You must connect a known voltage to the module. You must specify the voltage with *referenceVoltage*  and specify the measured output with *measuredOutput* .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| referenceVoltage | double | The known voltage, in volts, to use as a reference for calibration. |
| measuredOutput | double | The measured output, in volts, for the channel. |
| calibrationSource | InputCalibrationSource | The calibration source. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust4204__string-double-bool-double.html language=enus -->
## TOPIC 02189: Adjust4204(string, double, bool, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust4204__string-double-bool-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust4204__string-double-bool-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 4204 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust4204(string physicalChannels, double lowpassFilterCutoffFrequency, [MarshalAs(UnmanagedType.U1)] bool sampleAndHoldEnabled, double referenceVoltage)RemarksYou must connect a

### Adjust4204(string, double, bool, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_devcalibrate) constants for an NI 4204 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust4204(string physicalChannels, double lowpassFilterCutoffFrequency, [MarshalAs(UnmanagedType.U1)] bool sampleAndHoldEnabled, double referenceVoltage)

#### Remarks

You must connect a known voltage to the device and specify that voltage with *referenceVoltage* .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | The physical channel(s) to calibrate. |
| lowpassFilterCutoffFrequency | double | The lowpass filter cutoff frequency, in hertz, to calibrate. |
| sampleAndHoldEnabled | bool | Specifies whether to calibrate the channel(s) with the sample and hold circuitry of the channel enabled. |
| referenceVoltage | double | The known voltage, in volts, to use as a reference for calibration. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust4220__string-double-double.html language=enus -->
## TOPIC 02190: Adjust4220(string, double, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust4220__string-double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust4220__string-double-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 4220 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust4220(string physicalChannels, double gain, double referenceVoltage)RemarksThis device requires reference signals of 0.0 volts at gains of 1, 15, 20, and 310 on a particular c

### Adjust4220(string, double, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_devcalibrate) constants for an NI 4220 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust4220(string physicalChannels, double gain, double referenceVoltage)

#### Remarks

This device requires reference signals of 0.0 volts at gains of 1, 15, 20, and 310 on a particular channel in order to perform an offset calibration for that channel. If you do not manually supply those reference signals, the device measures them internally with sample and hold circuitry enabled.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | The physical channel(s) to calibrate. |
| gain | double | The gain setting to calibrate. |
| referenceVoltage | double | The known voltage, in volts, to use as a reference for calibration. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust4224__string-double-double.html language=enus -->
## TOPIC 02191: Adjust4224(string, double, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust4224__string-double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust4224__string-double-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 4224 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust4224(string physicalChannels, double gain, double referenceVoltage)RemarksYou must connect a known voltage to the device and specify that voltage with referenceVoltage .Param

### Adjust4224(string, double, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_devcalibrate) constants for an NI 4224 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust4224(string physicalChannels, double gain, double referenceVoltage)

#### Remarks

You must connect a known voltage to the device and specify that voltage with *referenceVoltage* .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | The physical channel(s) to calibrate. |
| gain | double | The gain setting to calibrate. |
| referenceVoltage | double | The known voltage, in volts, to use as a reference for calibration. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust4225__string-double-double.html language=enus -->
## TOPIC 02192: Adjust4225(string, double, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust4225__string-double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust4225__string-double-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: The Adjust4225 method is deprecated. Will warn if used The Adjust4225(string, double, double) method has been deprecated. Adjusts the external calibration constants for an NI 4225 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust4225(string physicalChannels, double gain,

### Adjust4225(string, double, double)

**Obsolete: The Adjust4225 method is deprecated. Will warn if used** 
The Adjust4225(string, double, double) method has been deprecated. Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_devcalibrate) constants for an NI 4225 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust4225(string physicalChannels, double gain, double referenceVoltage)

#### Remarks

You must connect a known voltage to the device and specify that voltage with *referenceVoltage* .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | The physical channel(s) to calibrate. |
| gain | double | The gain setting to calibrate. |
| referenceVoltage | double | The known voltage, in volts, to use as a reference for calibration. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust4300__double.html language=enus -->
## TOPIC 02193: Adjust4300(double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust4300__double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust4300__double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants on an NI 4300 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust4300(double referenceVoltage)RemarksYou must connect a known voltage to the device and specify that voltage with referenceVoltage .ParametersNameTypeDescriptionreferenceVoltag

### Adjust4300(double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants on an NI 4300 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust4300(double referenceVoltage)

#### Remarks

You must [connect a known voltage to the device](/csh?context=nidaqmx_mxdevconsid_calsigeseries) and specify that voltage with *referenceVoltage* .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| referenceVoltage | double | The known voltage, in volts, to use as a reference for calibration. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust4302__double.html language=enus -->
## TOPIC 02194: Adjust4302(double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust4302__double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust4302__double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 4302. Connect a known voltage to the device and specify that voltage with referenceVoltage . SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust4302(double referenceVoltage)ParametersNameTypeDescriptionreferenceVoltagedoubleSpecifies, in

### Adjust4302(double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 4302. Connect a known voltage to the device and specify that voltage with *referenceVoltage* .

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust4302(double referenceVoltage)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| referenceVoltage | double | Specifies, in volts, the known voltage to use as a reference for calibration. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust4303__double.html language=enus -->
## TOPIC 02195: Adjust4303(double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust4303__double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust4303__double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 4303. Connect a known voltage to the device and specify that voltage with referenceVoltage . SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust4303(double referenceVoltage)ParametersNameTypeDescriptionreferenceVoltagedoubleSpecifies, in

### Adjust4303(double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 4303. Connect a known voltage to the device and specify that voltage with *referenceVoltage* .

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust4303(double referenceVoltage)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| referenceVoltage | double | Specifies, in volts, the known voltage to use as a reference for calibration. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust4304__double.html language=enus -->
## TOPIC 02196: Adjust4304(double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust4304__double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust4304__double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 4304. Connect a known voltage to the device and specify that voltage with referenceVoltage . SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust4304(double referenceVoltage)ParametersNameTypeDescriptionreferenceVoltagedoubleSpecifies, in

### Adjust4304(double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 4304. Connect a known voltage to the device and specify that voltage with *referenceVoltage* .

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust4304(double referenceVoltage)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| referenceVoltage | double | Specifies, in volts, the known voltage to use as a reference for calibration. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust4305__double.html language=enus -->
## TOPIC 02197: Adjust4305(double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust4305__double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust4305__double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 4305. Connect a known voltage to the device and specify that voltage with referenceVoltage . SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust4305(double referenceVoltage)ParametersNameTypeDescriptionreferenceVoltagedoubleSpecifies, in

### Adjust4305(double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 4305. Connect a known voltage to the device and specify that voltage with *referenceVoltage* .

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust4305(double referenceVoltage)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| referenceVoltage | double | Specifies, in volts, the known voltage to use as a reference for calibration. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust4309__double.html language=enus -->
## TOPIC 02198: Adjust4309(double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust4309__double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust4309__double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the calibration constants for a PXIe-4309 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust4309(double referenceVoltage)RemarksYou must connect a known voltage to the device and specify that voltage with referenceVoltage . ParametersNameTypeDescriptionreferenceVoltagedoubl

### Adjust4309(double)

Adjusts the calibration constants for a PXIe-4309 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust4309(double referenceVoltage)

#### Remarks

You must [connect a known voltage to the device](/csh?context=nidaqmx_mxdevconsid_calsigeseries) and specify that voltage with *referenceVoltage* .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| referenceVoltage | double | The known voltage, in volts, to use as a reference for calibration. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust4310__double.html language=enus -->
## TOPIC 02199: Adjust4310(double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust4310__double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust4310__double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the calibration constants for a PXIe-4310 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust4310(double referenceVoltage)RemarksYou must connect a known voltage to the device and specify that voltage with referenceVoltage . ParametersNameTypeDescriptionreferenceVoltagedoubl

### Adjust4310(double)

Adjusts the calibration constants for a PXIe-4310 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust4310(double referenceVoltage)

#### Remarks

You must [connect a known voltage to the device](/csh?context=nidaqmx_mxdevconsid_calsigeseries) and specify that voltage with *referenceVoltage* .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| referenceVoltage | double | The known voltage, in volts, to use as a reference for calibration. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust4311__double-double-double.html language=enus -->
## TOPIC 02200: Adjust4311(double, double, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust4311__double-double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust4311__double-double-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the calibration constants for a PXIe-4311 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust4311(double rangeMaximum, double rangeMinimum, double referenceVoltage)RemarksYou must connect a known voltage to the device and specify that voltage with referenceVoltage . Paramete

### Adjust4311(double, double, double)

Adjusts the calibration constants for a PXIe-4311 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust4311(double rangeMaximum, double rangeMinimum, double referenceVoltage)

#### Remarks

You must [connect a known voltage to the device](/csh?context=nidaqmx_mxdevconsid_calsigeseries) and specify that voltage with *referenceVoltage* .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rangeMaximum | double | The maximum value in the range. |
| rangeMinimum | double | The minimum value in the range. |
| referenceVoltage | double | The known voltage, in volts, to use as a reference for calibration. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust4322__string-double.html language=enus -->
## TOPIC 02201: Adjust4322(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust4322__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust4322__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants on an NI 4322 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust4322(string physicalChannels, double referenceValue)RemarksYou must connect a known voltage to the device and specify that voltage with referenceValue .ParametersNameTypeDescr

### Adjust4322(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants on an NI 4322 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust4322(string physicalChannels, double referenceValue)

#### Remarks

You must [connect a known voltage to the device](/csh?context=nidaqmx_mxdevconsid_calsigeseries) and specify that voltage with *referenceValue* .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| referenceValue | double | The known voltage, in volts, to use as a reference for calibration. |
| physicalChannels | string | The name(s) of the physical channels to calibrate. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust4339__double.html language=enus -->
## TOPIC 02202: Adjust4339(double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust4339__double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust4339__double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI PXIe 4339 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust4339(double referenceVoltage)ParametersNameTypeDescriptionreferenceVoltagedoubleThe voltage across the AI+ and AI- terminals, measured using a DMM.

### Adjust4339(double)

Adjusts the external calibration constants for an NI PXIe 4339 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust4339(double referenceVoltage)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| referenceVoltage | double | The voltage across the AI+ and AI- terminals, measured using a DMM. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust433x__double-double-shuntelementlocation.html language=enus -->
## TOPIC 02203: Adjust433x(double, double, ShuntElementLocation)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust433x__double-double-shuntelementlocation.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust433x__double-double-shuntelementlocation.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants on an NI PXIe-433x device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust433x(double referenceVoltage, double referenceExcitation, ShuntElementLocation shuntLocation)RemarksYou must connect a known voltage to the device and specify that voltag

### Adjust433x(double, double, ShuntElementLocation)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants on an NI PXIe-433x device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust433x(double referenceVoltage, double referenceExcitation, ShuntElementLocation shuntLocation)

#### Remarks

You must [connect a known voltage to the device](/csh?context=nidaqmx_mxdevconsid_calsigeseries) and specify that voltage with *referenceVoltage* .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| referenceVoltage | double | The known voltage, in volts, to use as a reference for calibration. |
| referenceExcitation | double | The known excitation value to use as a reference for calibration. |
| shuntLocation | ShuntElementLocation | Specifies the location of the shunted leg. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust4353__string-double.html language=enus -->
## TOPIC 02204: Adjust4353(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust4353__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust4353__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants on an NI 4353 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust4353(string physicalChannels, double referenceVoltage)ParametersNameTypeDescriptionphysicalChannelsstringThe physical channel(s) to calibrate.referenceVoltagedoubleThe known v

### Adjust4353(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_devcalibrate) constants on an NI 4353 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust4353(string physicalChannels, double referenceVoltage)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | The physical channel(s) to calibrate. |
| referenceVoltage | double | The known voltage, in volts, to use as a reference for calibration. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust4357__string-double_arr1.html language=enus -->
## TOPIC 02205: Adjust4357(string, double[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust4357__string-double_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust4357__string-double_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 4357 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust4357(string physicalChannels, double[] referenceValues)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the c

### Adjust4357(string, double[])

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 4357 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust4357(string physicalChannels, double[] referenceValues)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| referenceValues | double[] | Specifies in volts the known voltages to use as the references for calibration. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust64xx__double.html language=enus -->
## TOPIC 02206: Adjust64xx(double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust64xx__double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust64xx__double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 64xx device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust64xx(double referenceVoltage)RemarksYou must connect a known voltage to the device and specify that voltage with referenceVoltage .ParametersNameTypeDescriptionreferenceVolta

### Adjust64xx(double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 64xx device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust64xx(double referenceVoltage)

#### Remarks

You must connect a known voltage to the device and specify that voltage with *referenceVoltage* .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| referenceVoltage | double | The known voltage, in volts, to use as a reference for calibration. This voltage must be between +6.000 V and +8.500 V. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9201__string-double.html language=enus -->
## TOPIC 02207: Adjust9201(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9201__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9201__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9201 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9201(string physicalChannels, double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration,

### Adjust9201(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9201 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9201(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9202__string-double.html language=enus -->
## TOPIC 02208: Adjust9202(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9202__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9202__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9202 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9202(string physicalChannels, double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration,

### Adjust9202(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9202 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9202(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9203gain__string-double-double-double.html language=enus -->
## TOPIC 02209: Adjust9203Gain(string, double, double, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9203gain__string-double-double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9203gain__string-double-double-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration gain constants for an NI 9203 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9203Gain(string physicalChannels, double rangeMinimum, double rangeMaximum, double value)RemarksRefer to the calibration procedure for your device for detailed calibrati

### Adjust9203Gain(string, double, double, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) gain constants for an NI 9203 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9203Gain(string physicalChannels, double rangeMinimum, double rangeMaximum, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| rangeMinimum | double | Specifies the minimum value for the range, in amps. |
| rangeMaximum | double | Specifies the maximum value for the range, in amps. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9203offset__string-double-double.html language=enus -->
## TOPIC 02210: Adjust9203Offset(string, double, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9203offset__string-double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9203offset__string-double-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration offset constants for an NI 9203 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9203Offset(string physicalChannels, double rangeMinimum, double rangeMaximum)RemarksRefer to the calibration procedure for your device for detailed calibration instruc

### Adjust9203Offset(string, double, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) offset constants for an NI 9203 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9203Offset(string physicalChannels, double rangeMinimum, double rangeMaximum)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| rangeMinimum | double | Specifies the minimum value for the range, in amps. |
| rangeMaximum | double | Specifies the maximum value for the range, in amps. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9204__double.html language=enus -->
## TOPIC 02211: Adjust9204(double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9204__double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9204__double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9204 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9204(double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration, you cannot undo it. If an

### Adjust9204(double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9204 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9204(double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9205__double.html language=enus -->
## TOPIC 02212: Adjust9205(double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9205__double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9205__double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9205 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9205(double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration, you cannot undo it. If an

### Adjust9205(double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9205 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9205(double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9206__double.html language=enus -->
## TOPIC 02213: Adjust9206(double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9206__double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9206__double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9206 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9206(double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration, you cannot undo it. If an

### Adjust9206(double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9206 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9206(double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9207gain__string-double.html language=enus -->
## TOPIC 02214: Adjust9207Gain(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9207gain__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9207gain__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration gain constants for an NI 9207 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9207Gain(string physicalChannels, double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the cali

### Adjust9207Gain(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) gain constants for an NI 9207 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9207Gain(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9207offset__string.html language=enus -->
## TOPIC 02215: Adjust9207Offset(string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9207offset__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9207offset__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration offset constants for an NI 9207 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9207Offset(string physicalChannels)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration, y

### Adjust9207Offset(string)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) offset constants for an NI 9207 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9207Offset(string physicalChannels)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9208gain__string-double.html language=enus -->
## TOPIC 02216: Adjust9208Gain(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9208gain__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9208gain__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration gain constants for an NI 9208 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9208Gain(string physicalChannels, double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the cali

### Adjust9208Gain(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) gain constants for an NI 9208 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9208Gain(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9208offset__string.html language=enus -->
## TOPIC 02217: Adjust9208Offset(string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9208offset__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9208offset__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration offset constants for an NI 9208 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9208Offset(string physicalChannels)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration, y

### Adjust9208Offset(string)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) offset constants for an NI 9208 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9208Offset(string physicalChannels)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9209gain__string-calibrationinputterminalconfiguration9209-double.html language=enus -->
## TOPIC 02218: Adjust9209Gain(string, CalibrationInputTerminalConfiguration9209, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9209gain__string-calibrationinputterminalconfiguration9209-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9209gain__string-calibrationinputterminalconfiguration9209-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration gain constants for an NI 9209 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9209Gain(string physicalChannels, CalibrationInputTerminalConfiguration9209 terminalConfiguration, double value)RemarksRefer to the calibration procedure for your device

### Adjust9209Gain(string, CalibrationInputTerminalConfiguration9209, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) gain constants for an NI 9209 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9209Gain(string physicalChannels, CalibrationInputTerminalConfiguration9209 terminalConfiguration, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| terminalConfiguration | CalibrationInputTerminalConfiguration9209 | The input terminal configuration for the channel. |
| value | double | Specifies the reference value measured using a calibrator. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9209offset__string.html language=enus -->
## TOPIC 02219: Adjust9209Offset(string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9209offset__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9209offset__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration offset constants for an NI 9209 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9209Offset(string physicalChannels)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration, y

### Adjust9209Offset(string)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) offset constants for an NI 9209 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9209Offset(string physicalChannels)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9210__string-double.html language=enus -->
## TOPIC 02220: Adjust9210(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9210__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9210__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9210 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9210(string physicalChannels, double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration,

### Adjust9210(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9210 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9210(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9211__string-double.html language=enus -->
## TOPIC 02221: Adjust9211(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9211__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9211__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9211 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9211(string physicalChannels, double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration,

### Adjust9211(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9211 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9211(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9212__string-double.html language=enus -->
## TOPIC 02222: Adjust9212(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9212__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9212__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9212 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9212(string physicalChannels, double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration,

### Adjust9212(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9212 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9212(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9213__string-double-double-double.html language=enus -->
## TOPIC 02223: Adjust9213(string, double, double, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9213__string-double-double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9213__string-double-double-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9213 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9213(string physicalChannels, double rangeMinimum, double rangeMaximum, double value)RemarksRefer to the calibration procedure for your device for detailed calibration instru

### Adjust9213(string, double, double, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9213 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9213(string physicalChannels, double rangeMinimum, double rangeMaximum, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| rangeMinimum | double | Specifies the minimum value for the range, in volts. |
| rangeMaximum | double | Specifies the maximum value for the range, in volts. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9214__string-double.html language=enus -->
## TOPIC 02224: Adjust9214(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9214__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9214__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9214 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9214(string physicalChannels, double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration,

### Adjust9214(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9214 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9214(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9215__string-double.html language=enus -->
## TOPIC 02225: Adjust9215(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9215__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9215__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9215 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9215(string physicalChannels, double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration,

### Adjust9215(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9215 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9215(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9216__string-double.html language=enus -->
## TOPIC 02226: Adjust9216(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9216__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9216__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9216 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9216(string physicalChannels, double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration,

### Adjust9216(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9216 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9216(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9217__string-double.html language=enus -->
## TOPIC 02227: Adjust9217(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9217__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9217__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9217 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9217(string physicalChannels, double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration,

### Adjust9217(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9217 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9217(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9218__string-double.html language=enus -->
## TOPIC 02228: Adjust9218(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9218__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9218__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9218 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9218(string physicalChannels, double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration,

### Adjust9218(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9218 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9218(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9219__string-double.html language=enus -->
## TOPIC 02229: Adjust9219(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9219__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9219__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9219 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9219(string physicalChannels, double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration,

### Adjust9219(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9219 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9219(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9220__string-double.html language=enus -->
## TOPIC 02230: Adjust9220(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9220__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9220__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9220 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9220(string physicalChannels, double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration,

### Adjust9220(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9220 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9220(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9221__string-double.html language=enus -->
## TOPIC 02231: Adjust9221(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9221__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9221__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9221 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9221(string physicalChannels, double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration,

### Adjust9221(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9221 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9221(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9222__string-double.html language=enus -->
## TOPIC 02232: Adjust9222(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9222__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9222__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9222 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9222(string physicalChannels, double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration,

### Adjust9222(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9222 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9222(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9223__string-double.html language=enus -->
## TOPIC 02233: Adjust9223(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9223__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9223__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9223 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9223(string physicalChannels, double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration,

### Adjust9223(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9223 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9223(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9224__string-double.html language=enus -->
## TOPIC 02234: Adjust9224(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9224__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9224__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9224 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9224(string physicalChannels, double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions.After you commit the calibration, y

### Adjust9224(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9224 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9224(string physicalChannels, double value)

#### Remarks

Refer to the [calibration procedure for your device](https://#) for detailed calibration instructions.

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | The physical channel(s) to calibrate. |
| value | double | The reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9225__string-double.html language=enus -->
## TOPIC 02235: Adjust9225(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9225__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9225__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9225 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9225(string physicalChannels, double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration,

### Adjust9225(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9225 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9225(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9226__string-double.html language=enus -->
## TOPIC 02236: Adjust9226(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9226__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9226__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9226 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9226(string physicalChannels, double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration,

### Adjust9226(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9226 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9226(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9227__string-double.html language=enus -->
## TOPIC 02237: Adjust9227(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9227__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9227__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9227 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9227(string physicalChannels, double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration,

### Adjust9227(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9227 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9227(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9228__string-double.html language=enus -->
## TOPIC 02238: Adjust9228(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9228__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9228__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9228 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9228(string physicalChannels, double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions.After you commit the calibration, y

### Adjust9228(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9228 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9228(string physicalChannels, double value)

#### Remarks

Refer to the [calibration procedure for your device](https://#) for detailed calibration instructions.

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | The physical channel(s) to calibrate. |
| value | double | The reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9229__string-double.html language=enus -->
## TOPIC 02239: Adjust9229(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9229__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9229__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9229 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9229(string physicalChannels, double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration,

### Adjust9229(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9229 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9229(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9230__string-double.html language=enus -->
## TOPIC 02240: Adjust9230(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9230__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9230__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9230 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9230(string physicalChannels, double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration,

### Adjust9230(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9230 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9230(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9231__string-double.html language=enus -->
## TOPIC 02241: Adjust9231(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9231__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9231__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9231 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9231(string physicalChannels, double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration,

### Adjust9231(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9231 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9231(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9232__string-double.html language=enus -->
## TOPIC 02242: Adjust9232(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9232__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9232__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9232 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9232(string physicalChannels, double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration,

### Adjust9232(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9232 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9232(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9234gain__string-double.html language=enus -->
## TOPIC 02243: Adjust9234Gain(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9234gain__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9234gain__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration gain constants for an NI 9234 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9234Gain(string physicalChannels, double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the cali

### Adjust9234Gain(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) gain constants for an NI 9234 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9234Gain(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9234offset__string.html language=enus -->
## TOPIC 02244: Adjust9234Offset(string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9234offset__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9234offset__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration offset constants for an NI 9234 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9234Offset(string physicalChannels)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration, y

### Adjust9234Offset(string)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) offset constants for an NI 9234 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9234Offset(string physicalChannels)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9238__string-double.html language=enus -->
## TOPIC 02245: Adjust9238(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9238__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9238__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9238 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9238(string physicalChannels, double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration,

### Adjust9238(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9238 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9238(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9239__string-double.html language=enus -->
## TOPIC 02246: Adjust9239(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9239__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9239__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9239 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9239(string physicalChannels, double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration,

### Adjust9239(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9239 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9239(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9242__string-double.html language=enus -->
## TOPIC 02247: Adjust9242(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9242__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9242__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9242 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9242(string physicalChannels, double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration,

### Adjust9242(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9242 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9242(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9244__string-double.html language=enus -->
## TOPIC 02248: Adjust9244(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9244__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9244__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9244 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9244(string physicalChannels, double value)RemarksRefer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration,

### Adjust9244(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9244 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9244(string physicalChannels, double value)

#### Remarks

calibration procedure for your device

Note

After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | Specifies the physical channel(s) to calibrate. |
| value | double | Specifies the reference value measured using a calibrator. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9246__string-double.html language=enus -->
## TOPIC 02249: Adjust9246(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9246__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9246__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9246 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9246(string physicalChannels, double value)ParametersNameTypeDescriptionphysicalChannelsstringThe physical channel(s) to calibrate.valuedoubleThe reference value measured usi

### Adjust9246(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9246 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9246(string physicalChannels, double value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | The physical channel(s) to calibrate. |
| value | double | The reference value measured using a calibrator. |

Parent topic:

ExternalCalibrationSession Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-externalcalibrationsession-adjust9247__string-double.html language=enus -->
## TOPIC 02250: Adjust9247(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-externalcalibrationsession-adjust9247__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-externalcalibrationsession-adjust9247__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9247 device. SyntaxNamespace: NationalInstruments.DAQmxpublic void Adjust9247(string physicalChannels, double value)ParametersNameTypeDescriptionphysicalChannelsstringThe physical channel(s) to calibrate.valuedoubleThe reference value measured usi

### Adjust9247(string, double)

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9247 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Adjust9247(string physicalChannels, double value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | The physical channel(s) to calibrate. |
| value | double | The reference value measured using a calibrator. |

Parent topic:

ExternalCalibrationSession Class
