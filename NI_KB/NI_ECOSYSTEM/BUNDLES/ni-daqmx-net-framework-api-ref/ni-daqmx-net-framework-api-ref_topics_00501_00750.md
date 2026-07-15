# NI DOCUMENT BUNDLE: ni-daqmx-net-framework-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-daqmx-net-framework-api-ref start=501 end=750 -->
<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-beginreadwaveform__timespan-asynccallback-object.html language=enus -->
## TOPIC 00501: BeginReadWaveform(TimeSpan, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-beginreadwaveform__timespan-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-beginreadwaveform__timespan-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more analog waveform samples from one or more AIChannel objects in a task for a specified duration . SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadWaveform(TimeSpan duration, AsyncCallback callback, object state)RemarksTo get the read da

### BeginReadWaveform(TimeSpan, AsyncCallback, object)

Begins an asynchronous read of one or more analog waveform samples from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task for a specified *duration* .

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadWaveform(TimeSpan duration, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadWaveform(TimeSpan, AsyncCallback, object), call [EndReadWaveform(IAsyncResult)](nationalinstruments-daqmx-analogmultichannelreader-endreadwaveform__iasyncresult.html), passing the returned IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units when creating channels using the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](nationalinstruments-daqmx-daqstream-waveformattributemode.html) property of the [DaqStream](nationalinstruments-daqmx-daqstream.html) being read.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the [Stream](nationalinstruments-daqmx-task-stream.html) object used for the reads or writes.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| duration | TimeSpan | The duration of time to read the waveform. The duration specified must be long enough to read at least one sample at the configured SampleClockRate. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-endmemoryoptimizedreadmultisample__iasyncresult-out.html language=enus -->
## TOPIC 00502: EndMemoryOptimizedReadMultiSample(IAsyncResult, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-endmemoryoptimizedreadmultisample__iasyncresult-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-endmemoryoptimizedreadmultisample__iasyncresult-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSample(int, AsyncCallback, object, double[, ]) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic double[,] EndMemoryOptimizedReadMultiSample(IAsyncResult asyncResult, out int actualNumb

### EndMemoryOptimizedReadMultiSample(IAsyncResult, out int)

Handles the end of an asynchronous read initiated with [BeginMemoryOptimizedReadMultiSample(int, AsyncCallback, object, double[, ])](nationalinstruments-daqmx-analogmultichannelreader-beginmemoryoptimizedreadmultisample__int-asynccallback-object-double_arr2.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[,] EndMemoryOptimizedReadMultiSample(IAsyncResult asyncResult, out int actualNumberOfSamplesPerChannelRead)

#### Remarks

If you call this method before the asynchronous read IAsyncResult is complete, it waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadMultiSample(int, AsyncCallback, object, double[, ]). |
| actualNumberOfSamplesPerChannelRead | out int | The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A 2D array of floating-point samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples; or For asynchronous reads, if asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadMultiSample(int, AsyncCallback, object, double[, ]). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-endmemoryoptimizedreadmultisamplepower__iasyncresult-out.html language=enus -->
## TOPIC 00503: EndMemoryOptimizedReadMultiSamplePower(IAsyncResult, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-endmemoryoptimizedreadmultisamplepower__iasyncresult-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-endmemoryoptimizedreadmultisamplepower__iasyncresult-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePower(int, AsyncCallback, object, AIPowerMeasurement[, ]) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic AIPowerMeasurement[,] EndMemoryOptimizedReadMultiSamplePower(IAsyncResu

### EndMemoryOptimizedReadMultiSamplePower(IAsyncResult, out int)

Handles the end of an asynchronous read initiated with [BeginMemoryOptimizedReadMultiSamplePower(int, AsyncCallback, object, AIPowerMeasurement[, ])](nationalinstruments-daqmx-analogmultichannelreader-beginmemoryoptimizedreadmultisamplepower__int-asynccallback-object-aipowermeasurement_arr2.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIPowerMeasurement](nationalinstruments-daqmx-aipowermeasurement.html)[,] EndMemoryOptimizedReadMultiSamplePower(IAsyncResult asyncResult, out int actualNumberOfSamplesPerChannelRead)

#### Remarks

If you call this method before the asynchronous read IAsyncResult is complete, it waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadMultiSamplePower(int, AsyncCallback, object, AIPowerMeasurement[, ]). |
| actualNumberOfSamplesPerChannelRead | out int | The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A 2D array of power samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples; or For asynchronous reads, if asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadMultiSamplePower(int, AsyncCallback, object, AIPowerMeasurement[, ]). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-endmemoryoptimizedreadwaveform__iasyncresult.html language=enus -->
## TOPIC 00504: EndMemoryOptimizedReadWaveform(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-endmemoryoptimizedreadwaveform__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-endmemoryoptimizedreadwaveform__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadWaveform(int, AsyncCallback, object, AnalogWaveform<double>[]) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogWaveform< double >[] EndMemoryOptimizedReadWaveform(IAsyncResult asyncR

### EndMemoryOptimizedReadWaveform(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginMemoryOptimizedReadWaveform(int, AsyncCallback, object, AnalogWaveform<double>[])](nationalinstruments-daqmx-analogmultichannelreader-beginmemoryoptimizedreadwaveform__int-asynccallback-object-analogwaveform_double__arr1.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public AnalogWaveform< double >[] EndMemoryOptimizedReadWaveform(IAsyncResult asyncResult)

#### Remarks

If you call EndMemoryOptimizedReadWaveform(IAsyncResult) before the asynchronous read IAsyncResult is complete, EndMemoryOptimizedReadWaveform(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadWaveform(int, AsyncCallback, object, AnalogWaveform<double>[]) |

#### Returns

A 1D array of AnalogWaveformTData objects containing samples from the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If the first dimension of data does not match the number of channels. If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. For asynchronous reads, if asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadWaveform(int, AsyncCallback, object, AnalogWaveform<double>[]). For reads that take a TimeSpan duration, if the duration provided was less than Zero. |
| NationalInstruments.DAQmx.DaqException | If data is null or is uninitialized. If one of the elements of data is null. The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-endreadmultisample__iasyncresult.html language=enus -->
## TOPIC 00505: EndReadMultiSample(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-endreadmultisample__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-endreadmultisample__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadMultiSample(int, AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic double[,] EndReadMultiSample(IAsyncResult asyncResult)RemarksIf you call EndReadMultiSample(IAsyncResult) before th

### EndReadMultiSample(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadMultiSample(int, AsyncCallback, object)](nationalinstruments-daqmx-analogmultichannelreader-beginreadmultisample__int-asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[,] EndReadMultiSample(IAsyncResult asyncResult)

#### Remarks

If you call EndReadMultiSample(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadMultiSample(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadMultiSample(int, AsyncCallback, object) . |

#### Returns

A 2D array of floating-point samples from the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadMultiSample(int, AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-endreadmultisamplepower__iasyncresult.html language=enus -->
## TOPIC 00506: EndReadMultiSamplePower(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-endreadmultisamplepower__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-endreadmultisamplepower__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadMultiSamplePower(int, AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic AIPowerMeasurement[,] EndReadMultiSamplePower(IAsyncResult asyncResult)RemarksIf you call EndReadMultiSamplePo

### EndReadMultiSamplePower(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadMultiSamplePower(int, AsyncCallback, object)](nationalinstruments-daqmx-analogmultichannelreader-beginreadmultisamplepower__int-asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIPowerMeasurement](nationalinstruments-daqmx-aipowermeasurement.html)[,] EndReadMultiSamplePower(IAsyncResult asyncResult)

#### Remarks

If you call EndReadMultiSamplePower(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadMultiSamplePower(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadMultiSamplePower(int, AsyncCallback, object) . |

#### Returns

A 2D array of power samples from the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadMultiSamplePower(int, AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-endreadsinglesample__iasyncresult.html language=enus -->
## TOPIC 00507: EndReadSingleSample(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-endreadsinglesample__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-endreadsinglesample__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadSingleSample(AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] EndReadSingleSample(IAsyncResult asyncResult)RemarksIf you call EndReadSingleSample(IAsyncResult) before the a

### EndReadSingleSample(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadSingleSample(AsyncCallback, object)](nationalinstruments-daqmx-analogmultichannelreader-beginreadsinglesample__asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] EndReadSingleSample(IAsyncResult asyncResult)

#### Remarks

If you call EndReadSingleSample(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSample(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSample(AsyncCallback, object). |

#### Returns

A 1D array of floating-point samples from the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadSingleSample(AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-endreadsinglesamplepower__iasyncresult.html language=enus -->
## TOPIC 00508: EndReadSingleSamplePower(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-endreadsinglesamplepower__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-endreadsinglesamplepower__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadSingleSamplePower(AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic AIPowerMeasurement[] EndReadSingleSamplePower(IAsyncResult asyncResult)RemarksIf you call EndReadSingleSamplePower

### EndReadSingleSamplePower(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadSingleSamplePower(AsyncCallback, object)](nationalinstruments-daqmx-analogmultichannelreader-beginreadsinglesamplepower__asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIPowerMeasurement](nationalinstruments-daqmx-aipowermeasurement.html)[] EndReadSingleSamplePower(IAsyncResult asyncResult)

#### Remarks

If you call EndReadSingleSamplePower(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSamplePower(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSamplePower(AsyncCallback, object). |

#### Returns

A 1D array of power samples from the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadSingleSamplePower(AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-endreadwaveform__iasyncresult.html language=enus -->
## TOPIC 00509: EndReadWaveform(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-endreadwaveform__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-endreadwaveform__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadWaveform(int, AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogWaveform< double >[] EndReadWaveform(IAsyncResult asyncResult)RemarksIf you call EndReadWaveform(IAsyncResult) b

### EndReadWaveform(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadWaveform(int, AsyncCallback, object)](nationalinstruments-daqmx-analogmultichannelreader-beginreadwaveform__int-asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public AnalogWaveform< double >[] EndReadWaveform(IAsyncResult asyncResult)

#### Remarks

If you call EndReadWaveform(IAsyncResult) before the asynchronous read IAsyncResult is complete, [EndReadWaveform(IAsyncResult)](nationalinstruments-daqmx-digitalmultichannelreader-endreadwaveform__iasyncresult.html) waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadWaveform(int, AsyncCallback, object). |

#### Returns

A 1D array of AnalogWaveformTData objects containing samples from the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadWaveform(int, AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-memoryoptimizedreadmultisample__int-ref-out.html language=enus -->
## TOPIC 00510: MemoryOptimizedReadMultiSample(int, ref double, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-memoryoptimizedreadmultisample__int-ref-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-memoryoptimizedreadmultisample__int-ref-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more floating-point samples from one or more AIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic double[,] MemoryOptimizedReadMultiSample(int samplesPerChannel, ref double[,] data, out int actualNumberOfSamplesPerChannelRead)RemarksIf the data buffer is large e

### MemoryOptimizedReadMultiSample(int, ref double, out int)

Reads one or more floating-point samples from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[,] MemoryOptimizedReadMultiSample(int samplesPerChannel, ref double[,] data, out int actualNumberOfSamplesPerChannelRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help)

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref double | An initialized 2D array of floating-point samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |
| actualNumberOfSamplesPerChannelRead | out int | The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-memoryoptimizedreadmultisample__int-ref-reallocationpolicy-out.html language=enus -->
## TOPIC 00511: MemoryOptimizedReadMultiSample(int, ref double, ReallocationPolicy, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-memoryoptimizedreadmultisample__int-ref-reallocationpolicy-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-memoryoptimizedreadmultisample__int-ref-reallocationpolicy-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more floating-point samples from one or more AIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic double[,] MemoryOptimizedReadMultiSample(int samplesPerChannel, ref double[,] data, ReallocationPolicy policy, out int actualNumberOfSamplesPerChannelRead)RemarksIf

### MemoryOptimizedReadMultiSample(int, ref double, ReallocationPolicy, out int)

Reads one or more floating-point samples from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[,] MemoryOptimizedReadMultiSample(int samplesPerChannel, ref double[,] data, ReallocationPolicy policy, out int actualNumberOfSamplesPerChannelRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref double | An initialized 2D array of floating-point samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |
| actualNumberOfSamplesPerChannelRead | out int | The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-memoryoptimizedreadmultisamplepower__int-ref-out.html language=enus -->
## TOPIC 00512: MemoryOptimizedReadMultiSamplePower(int, ref AIPowerMeasurement, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-memoryoptimizedreadmultisamplepower__int-ref-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-memoryoptimizedreadmultisamplepower__int-ref-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more power samples from one or more AIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic AIPowerMeasurement[,] MemoryOptimizedReadMultiSamplePower(int samplesPerChannel, ref AIPowerMeasurement[,] data, out int actualNumberOfSamplesPerChannelRead)RemarksIf the da

### MemoryOptimizedReadMultiSamplePower(int, ref AIPowerMeasurement, out int)

Reads one or more power samples from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIPowerMeasurement](nationalinstruments-daqmx-aipowermeasurement.html)[,] MemoryOptimizedReadMultiSamplePower(int samplesPerChannel, ref AIPowerMeasurement[,] data, out int actualNumberOfSamplesPerChannelRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help)

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref AIPowerMeasurement | An initialized 2D array of power samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |
| actualNumberOfSamplesPerChannelRead | out int | The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-memoryoptimizedreadmultisamplepower__int-ref-reallocationpolicy-out.html language=enus -->
## TOPIC 00513: MemoryOptimizedReadMultiSamplePower(int, ref AIPowerMeasurement, ReallocationPolicy, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-memoryoptimizedreadmultisamplepower__int-ref-reallocationpolicy-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-memoryoptimizedreadmultisamplepower__int-ref-reallocationpolicy-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more power samples from one or more AIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic AIPowerMeasurement[,] MemoryOptimizedReadMultiSamplePower(int samplesPerChannel, ref AIPowerMeasurement[,] data, ReallocationPolicy policy, out int actualNumberOfSamplesPerC

### MemoryOptimizedReadMultiSamplePower(int, ref AIPowerMeasurement, ReallocationPolicy, out int)

Reads one or more power samples from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIPowerMeasurement](nationalinstruments-daqmx-aipowermeasurement.html)[,] MemoryOptimizedReadMultiSamplePower(int samplesPerChannel, ref AIPowerMeasurement[,] data, ReallocationPolicy policy, out int actualNumberOfSamplesPerChannelRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref AIPowerMeasurement | An initialized 2D array of power samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |
| actualNumberOfSamplesPerChannelRead | out int | The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-memoryoptimizedreadwaveform__int-analogwaveform_double__arr1-reallocationpolicy.html language=enus -->
## TOPIC 00514: MemoryOptimizedReadWaveform(int, AnalogWaveform< double >[], ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-memoryoptimizedreadwaveform__int-analogwaveform_double__arr1-reallocationpolicy.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-memoryoptimizedreadwaveform__int-analogwaveform_double__arr1-reallocationpolicy.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more analog waveform samples from one or more AIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogWaveform< double >[] MemoryOptimizedReadWaveform(int samplesPerChannel, AnalogWaveform< double >[] data, ReallocationPolicy policy)RemarksIf the data buffer

### MemoryOptimizedReadWaveform(int, AnalogWaveform< double >[], ReallocationPolicy)

Reads one or more analog waveform samples from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public AnalogWaveform< double >[] MemoryOptimizedReadWaveform(int samplesPerChannel, AnalogWaveform< double >[] data, ReallocationPolicy policy)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing AnalogWaveformTData objects and their corresponding memory to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](nationalinstruments-daqmx-daqstream-waveformattributemode.html) property of the [DaqStream](nationalinstruments-daqmx-daqstream.html) you are reading from.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | AnalogWaveform< double >[] | An initialized 1D array of AnalogWaveformTData that contains the read data. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-memoryoptimizedreadwaveform__int-analogwaveform_double__arr1.html language=enus -->
## TOPIC 00515: MemoryOptimizedReadWaveform(int, AnalogWaveform< double >[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-memoryoptimizedreadwaveform__int-analogwaveform_double__arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-memoryoptimizedreadwaveform__int-analogwaveform_double__arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more analog waveform samples from one or more AIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogWaveform< double >[] MemoryOptimizedReadWaveform(int samplesPerChannel, AnalogWaveform< double >[] data)RemarksIf the data buffer is large enough to hold the

### MemoryOptimizedReadWaveform(int, AnalogWaveform< double >[])

Reads one or more analog waveform samples from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public AnalogWaveform< double >[] MemoryOptimizedReadWaveform(int samplesPerChannel, AnalogWaveform< double >[] data)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing AnalogWaveformTData objects and their corresponding memory to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](nationalinstruments-daqmx-daqstream-waveformattributemode.html) property of the [DaqStream](nationalinstruments-daqmx-daqstream.html) you are reading from.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | AnalogWaveform< double >[] | An initialized 1D array of AnalogWaveformTData that contains the read data. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-memoryoptimizedreadwaveform__timespan-analogwaveform_double__arr1-reallocationpolicy.html language=enus -->
## TOPIC 00516: MemoryOptimizedReadWaveform(TimeSpan, AnalogWaveform< double >[], ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-memoryoptimizedreadwaveform__timespan-analogwaveform_double__arr1-reallocationpolicy.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-memoryoptimizedreadwaveform__timespan-analogwaveform_double__arr1-reallocationpolicy.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a memory-optimized read of one or more analog waveform samples from one or more AIChannel objects in a task for a specified duration . SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogWaveform< double >[] MemoryOptimizedReadWaveform(TimeSpan duration, AnalogWaveform< double >[] data,

### MemoryOptimizedReadWaveform(TimeSpan, AnalogWaveform< double >[], ReallocationPolicy)

Performs a memory-optimized read of one or more analog waveform samples from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task for a specified *duration* .

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public AnalogWaveform< double >[] MemoryOptimizedReadWaveform(TimeSpan duration, AnalogWaveform< double >[] data, ReallocationPolicy policy)

#### Remarks

If the *data*  waveform is large enough to hold the number of samples requested, this overload attempts to reuse the existing AnalogWaveformTData objects' memory to store acquired data. This results in more efficient memory allocation when performing subsequent reads with a continuous analog input task, if each subsequent read acquires the same or fewer number of samples.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units when creating channels using the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](nationalinstruments-daqmx-daqstream-waveformattributemode.html) property of the [DaqStream](nationalinstruments-daqmx-daqstream.html) being read.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the [Stream](nationalinstruments-daqmx-task-stream.html) object used for the reads or writes.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| duration | TimeSpan | The duration of time to read the waveform. The duration specified must be long enough to read at least one sample at the configured SampleClockRate. |
| data | AnalogWaveform< double >[] | An initialized 1D array of AnalogWaveformTData that contains the read data. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If the first dimension of data does not match the number of channels. If the duration provided was less than Zero. If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| NationalInstruments.DAQmx.DaqException | If data is null or is uninitialized. If one of the elements of data is null. The NI-DAQmx driver returned an error. |

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-memoryoptimizedreadwaveform__timespan-analogwaveform_double__arr1.html language=enus -->
## TOPIC 00517: MemoryOptimizedReadWaveform(TimeSpan, AnalogWaveform< double >[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-memoryoptimizedreadwaveform__timespan-analogwaveform_double__arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-memoryoptimizedreadwaveform__timespan-analogwaveform_double__arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a memory-optimized read of one or more analog waveform samples from one or more AIChannel objects in a task for a specified duration . SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogWaveform< double >[] MemoryOptimizedReadWaveform(TimeSpan duration, AnalogWaveform< double >[] data)R

### MemoryOptimizedReadWaveform(TimeSpan, AnalogWaveform< double >[])

Performs a memory-optimized read of one or more analog waveform samples from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task for a specified *duration* .

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public AnalogWaveform< double >[] MemoryOptimizedReadWaveform(TimeSpan duration, AnalogWaveform< double >[] data)

#### Remarks

If the *data*  waveform is large enough to hold the number of samples requested, this overload attempts to reuse the existing AnalogWaveformTData objects' memory to store acquired data. This results in more efficient memory allocation when performing subsequent reads with a continuous analog input task, if each subsequent read acquires the same or fewer number of samples.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units when creating channels using the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](nationalinstruments-daqmx-daqstream-waveformattributemode.html) property of the [DaqStream](nationalinstruments-daqmx-daqstream.html) being read.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the [Stream](nationalinstruments-daqmx-task-stream.html) object used for the reads or writes.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| duration | TimeSpan | The duration of time to read the waveform. The duration specified must be long enough to read at least one sample at the configured SampleClockRate. |
| data | AnalogWaveform< double >[] | An initialized 1D array of AnalogWaveformTData that contains the read data. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If the first dimension of data does not match the number of channels. If the duration provided was less than Zero. |
| NationalInstruments.DAQmx.DaqException | If data is null or is uninitialized. If one of the elements of data is null. The NI-DAQmx driver returned an error. |

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-readmultisample__int.html language=enus -->
## TOPIC 00518: ReadMultiSample(int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-readmultisample__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-readmultisample__int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more floating-point samples from one or more AIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic double[,] ReadMultiSample(int samplesPerChannel)RemarksNI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to

### ReadMultiSample(int)

Reads one or more floating-point samples from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[,] ReadMultiSample(int samplesPerChannel)

#### Remarks

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |

#### Returns

A 2D array of floating-point samples from the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-readmultisamplepower__int.html language=enus -->
## TOPIC 00519: ReadMultiSamplePower(int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-readmultisamplepower__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-readmultisamplepower__int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more power samples from one or more AIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic AIPowerMeasurement[,] ReadMultiSamplePower(int samplesPerChannel)RemarksNI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you a

### ReadMultiSamplePower(int)

Reads one or more power samples from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIPowerMeasurement](nationalinstruments-daqmx-aipowermeasurement.html)[,] ReadMultiSamplePower(int samplesPerChannel)

#### Remarks

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |

#### Returns

A 2D array of power samples from the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-readsinglesample.html language=enus -->
## TOPIC 00520: ReadSingleSample()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-readsinglesample.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-readsinglesample.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a single floating-point sample from one or more AIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] ReadSingleSample()RemarksNI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify

### ReadSingleSample()

Reads a single floating-point sample from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] ReadSingleSample()

#### Remarks

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Returns

A 1D array of floating-point samples from the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-readsinglesamplepower.html language=enus -->
## TOPIC 00521: ReadSingleSamplePower()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-readsinglesamplepower.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-readsinglesamplepower.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a single power sample from one or more AIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic AIPowerMeasurement[] ReadSingleSamplePower()RemarksNI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You

### ReadSingleSamplePower()

Reads a single power sample from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIPowerMeasurement](nationalinstruments-daqmx-aipowermeasurement.html)[] ReadSingleSamplePower()

#### Remarks

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Returns

A 1D array of power samples from the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-readwaveform__int.html language=enus -->
## TOPIC 00522: ReadWaveform(int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-readwaveform__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-readwaveform__int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more analog waveform samples from one or more AIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogWaveform< double >[] ReadWaveform(int samplesPerChannel)RemarksNI-DAQmx scales the returned data to the units of the measurement, including any custom scalin

### ReadWaveform(int)

Reads one or more analog waveform samples from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public AnalogWaveform< double >[] ReadWaveform(int samplesPerChannel)

#### Remarks

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](nationalinstruments-daqmx-daqstream-waveformattributemode.html) property of the [DaqStream](nationalinstruments-daqmx-daqstream.html) you are reading from.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |

#### Returns

A 1D array of AnalogWaveformTData objects containing samples from the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-readwaveform__timespan.html language=enus -->
## TOPIC 00523: ReadWaveform(TimeSpan)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-readwaveform__timespan.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-readwaveform__timespan.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more analog waveform samples from one or more AIChannel objects in a task for a specified duration . SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogWaveform< double >[] ReadWaveform(TimeSpan duration)RemarksNI-DAQmx scales the read data to the units of the measurement, including

### ReadWaveform(TimeSpan)

Reads one or more analog waveform samples from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task for a specified *duration* .

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public AnalogWaveform< double >[] ReadWaveform(TimeSpan duration)

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

A 1D array of AnalogWaveformTData objects containing samples from the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If the duration provided was less than Zero. |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-synchronizecallbacks.html language=enus -->
## TOPIC 00524: SynchronizeCallbacks

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-synchronizecallbacks.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-synchronizecallbacks.html
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

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-synchronizingobject.html language=enus -->
## TOPIC 00525: SynchronizingObject

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-synchronizingobject.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-synchronizingobject.html
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

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-tostring.html language=enus -->
## TOPIC 00526: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-tostring.html
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

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader.html language=enus -->
## TOPIC 00527: AnalogMultiChannelReader Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains methods for reading samples from one or more analog input channels in a task. Derives fromMarshalByRefObjectISynchronizeCallbacksISupportSynchronizationContextSyntaxNamespace: NationalInstruments.DAQmxpublic class AnalogMultiChannelReader : MarshalByRefObject, ISynchronizeCallbacks, ISuppor

### AnalogMultiChannelReader Class

Contains methods for reading samples from one or more analog input channels in a task.

#### Derives from

- MarshalByRefObject
- ISynchronizeCallbacks
- ISupportSynchronizationContext

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class AnalogMultiChannelReader : MarshalByRefObject, ISynchronizeCallbacks, ISupportSynchronizationContext

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| AnalogMultiChannelReader(DaqStream) | Creates a new instance of the AnalogMultiChannelReader class to read from the specified DaqStream. |

#### Properties

| Name | Description |
| --- | --- |
| SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |
| SynchronizingObject | Obsolete: Use SynchronizeCallbacks to specify that the object marshals callbacks across threads appropriately. Will warn if usedGets or sets the object that marshals event-handler and callback calls. |

#### Methods

| Name | Description |
| --- | --- |
| BeginMemoryOptimizedReadMultiSample(int, AsyncCallback, object, double, ReallocationPolicy) | Begins an asynchronous read of one or more floating-point samples from one or more AIChannel objects in a task. |
| BeginMemoryOptimizedReadMultiSample(int, AsyncCallback, object, double) | Begins an asynchronous read of one or more floating-point samples from one or more AIChannel objects in a task. |
| BeginMemoryOptimizedReadMultiSamplePower(int, AsyncCallback, object, AIPowerMeasurement, ReallocationPolicy) | Begins an asynchronous read of one or more power samples from one or more AIChannel objects in a task. |
| BeginMemoryOptimizedReadMultiSamplePower(int, AsyncCallback, object, AIPowerMeasurement) | Begins an asynchronous read of one or more power samples from one or more AIChannel objects in a task. |
| BeginMemoryOptimizedReadWaveform(TimeSpan, AsyncCallback, object, AnalogWaveform< double >[]) | Begins an asynchronous, memory-optimized read of one or more analog waveform samples from one or more AIChannel objects in a task for a specified duration . |
| BeginMemoryOptimizedReadWaveform(int, AsyncCallback, object, AnalogWaveform< double >[], ReallocationPolicy) | Begins an asynchronous read of one or more analog waveform samples from one or more AIChannel objects in a task. |
| BeginMemoryOptimizedReadWaveform(TimeSpan, AsyncCallback, object, AnalogWaveform< double >[], ReallocationPolicy) | Begins an asynchronous, memory-optimized read of one or more analog waveform samples from one or more AIChannel objects in a task for a specified duration . |
| BeginMemoryOptimizedReadWaveform(int, AsyncCallback, object, AnalogWaveform< double >[]) | Begins an asynchronous read of one or more analog waveform samples from one or more AIChannel objects in a task. |
| BeginReadMultiSample(int, AsyncCallback, object) | Begins an asynchronous read of one or more floating-point samples from one or more AIChannel objects in a task. |
| BeginReadMultiSamplePower(int, AsyncCallback, object) | Begins an asynchronous read of one or more power samples from one or more AIChannel objects in a task. |
| BeginReadSingleSample(AsyncCallback, object) | Begins an asynchronous read of a single floating-point sample from one or more AIChannel objects in a task. |
| BeginReadSingleSamplePower(AsyncCallback, object) | Begins an asynchronous read of a single power sample from one or more AIChannel objects in a task. |
| BeginReadWaveform(TimeSpan, AsyncCallback, object) | Begins an asynchronous read of one or more analog waveform samples from one or more AIChannel objects in a task for a specified duration . |
| BeginReadWaveform(int, AsyncCallback, object) | Begins an asynchronous read of one or more analog waveform samples from one or more AIChannel objects in a task. |
| EndMemoryOptimizedReadMultiSample(IAsyncResult, out int) | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSample(int, AsyncCallback, object, double[, ]) and retrieves the read samples. |
| EndMemoryOptimizedReadMultiSamplePower(IAsyncResult, out int) | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePower(int, AsyncCallback, object, AIPowerMeasurement[, ]) and retrieves the read samples. |
| EndMemoryOptimizedReadWaveform(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadWaveform(int, AsyncCallback, object, AnalogWaveform<double>[]) and retrieves the read samples. |
| EndReadMultiSample(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadMultiSample(int, AsyncCallback, object) and retrieves the read samples. |
| EndReadMultiSamplePower(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadMultiSamplePower(int, AsyncCallback, object) and retrieves the read samples. |
| EndReadSingleSample(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadSingleSample(AsyncCallback, object) and retrieves the read samples. |
| EndReadSingleSamplePower(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadSingleSamplePower(AsyncCallback, object) and retrieves the read samples. |
| EndReadWaveform(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadWaveform(int, AsyncCallback, object) and retrieves the read samples. |
| MemoryOptimizedReadMultiSample(int, ref double, out int) | Reads one or more floating-point samples from one or more AIChannel objects in a task. |
| MemoryOptimizedReadMultiSample(int, ref double, ReallocationPolicy, out int) | Reads one or more floating-point samples from one or more AIChannel objects in a task. |
| MemoryOptimizedReadMultiSamplePower(int, ref AIPowerMeasurement, ReallocationPolicy, out int) | Reads one or more power samples from one or more AIChannel objects in a task. |
| MemoryOptimizedReadMultiSamplePower(int, ref AIPowerMeasurement, out int) | Reads one or more power samples from one or more AIChannel objects in a task. |
| MemoryOptimizedReadWaveform(int, AnalogWaveform< double >[], ReallocationPolicy) | Reads one or more analog waveform samples from one or more AIChannel objects in a task. |
| MemoryOptimizedReadWaveform(TimeSpan, AnalogWaveform< double >[], ReallocationPolicy) | Performs a memory-optimized read of one or more analog waveform samples from one or more AIChannel objects in a task for a specified duration . |
| MemoryOptimizedReadWaveform(int, AnalogWaveform< double >[]) | Reads one or more analog waveform samples from one or more AIChannel objects in a task. |
| MemoryOptimizedReadWaveform(TimeSpan, AnalogWaveform< double >[]) | Performs a memory-optimized read of one or more analog waveform samples from one or more AIChannel objects in a task for a specified duration . |
| ReadMultiSample(int) | Reads one or more floating-point samples from one or more AIChannel objects in a task. |
| ReadMultiSamplePower(int) | Reads one or more power samples from one or more AIChannel objects in a task. |
| ReadSingleSample() | Reads a single floating-point sample from one or more AIChannel objects in a task. |
| ReadSingleSamplePower() | Reads a single power sample from one or more AIChannel objects in a task. |
| ReadWaveform(int) | Reads one or more analog waveform samples from one or more AIChannel objects in a task. |
| ReadWaveform(TimeSpan) | Reads one or more analog waveform samples from one or more AIChannel objects in a task for a specified duration . |
| ToString() | Returns a string representation of the object. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelwriter-analogmultichannelwriter__daqstream.html language=enus -->
## TOPIC 00528: AnalogMultiChannelWriter(DaqStream)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelwriter-analogmultichannelwriter__daqstream.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelwriter-analogmultichannelwriter__daqstream.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of the AnalogMultiChannelWriter class to write to the specified DaqStream. SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogMultiChannelWriter(DaqStream stream)RemarksEach Task object contains a Stream property that serves as the connection point for writers to provide s

### AnalogMultiChannelWriter(DaqStream)

Creates a new instance of the [AnalogMultiChannelWriter](nationalinstruments-daqmx-analogmultichannelwriter.html) class to write to the specified [DaqStream](nationalinstruments-daqmx-daqstream.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public AnalogMultiChannelWriter(DaqStream stream)

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

AnalogMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelwriter-beginwritemultisample__bool-double_arr2-asynccallback-object.html language=enus -->
## TOPIC 00529: BeginWriteMultiSample(bool, double, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelwriter-beginwritemultisample__bool-double_arr2-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelwriter-beginwritemultisample__bool-double_arr2-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of one or more floating-point samples to one or more AOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteMultiSample([MarshalAs(UnmanagedType.U1)] bool autoStart, double[,] data, AsyncCallback callback, object state)Remark

### BeginWriteMultiSample(bool, double, AsyncCallback, object)

Begins an asynchronous write of one or more floating-point samples to one or more [AOChannel](nationalinstruments-daqmx-aochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteMultiSample([MarshalAs(UnmanagedType.U1)] bool autoStart, double[,] data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-analogmultichannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

NI-DAQmx scales the generated data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to the [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | double | A 2D array of samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array corresponds to the order in which you add the channels to the task. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelwriter-beginwritesinglesample__bool-double_arr1-asynccallback-object.html language=enus -->
## TOPIC 00530: BeginWriteSingleSample(bool, double[], AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelwriter-beginwritesinglesample__bool-double_arr1-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelwriter-beginwritesinglesample__bool-double_arr1-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of a single floating-point sample to one or more AOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteSingleSample([MarshalAs(UnmanagedType.U1)] bool autoStart, double[] data, AsyncCallback callback, object state)RemarksPas

### BeginWriteSingleSample(bool, double[], AsyncCallback, object)

Begins an asynchronous write of a single floating-point sample to one or more [AOChannel](nationalinstruments-daqmx-aochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteSingleSample([MarshalAs(UnmanagedType.U1)] bool autoStart, double[] data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-analogmultichannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

NI-DAQmx scales the generated data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | double[] | A 1D array of samples to write to the task. Each element of the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelwriter-beginwritewaveform_tdata___bool-analogwaveform_tdata__arr1-asynccallback-object.html language=enus -->
## TOPIC 00531: BeginWriteWaveform< TData >(bool, AnalogWaveform< TData >[], AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelwriter-beginwritewaveform_tdata___bool-analogwaveform_tdata__arr1-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelwriter-beginwritewaveform_tdata___bool-analogwaveform_tdata__arr1-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of one or more analog waveform samples to one or more AOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteWaveform< TData >([MarshalAs(UnmanagedType.U1)] bool autoStart, AnalogWaveform< TData >[] data, AsyncCallback callba

### BeginWriteWaveform< TData >(bool, AnalogWaveform< TData >[], AsyncCallback, object)

Begins an asynchronous write of one or more analog waveform samples to one or more [AOChannel](nationalinstruments-daqmx-aochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteWaveform< TData >([MarshalAs(UnmanagedType.U1)] bool autoStart, AnalogWaveform< TData >[] data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-analogmultichannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

Analog waveform writes are not affected by the WaveformTiming.SampleInterval or WaveformTiming.StartTime properties on AnalogWaveformTData. To configure timing for analog waveform writes, use the [ConfigureSampleClock(string, double, SampleClockActiveEdge, SampleQuantityMode, int)](nationalinstruments-daqmx-timing-configuresampleclock__string-double-sampleclockactiveedge-samplequantitymode-int.html) method.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) in the *NI Measurement Studio Help*and Generics in the .NET Framework in the *.NET Framework Developer's Guide* for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If you set autoStart to true, BeginWriteWaveform automatically calls Start if you do not explicitly call Start. You cannot set this parameter to true if you have installed events on the task. |
| data | AnalogWaveform< TData >[] | A 1D array of AnalogWaveformTData objects to write to the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task. The order of the lines in the analog waveform corresponds to the order in which you add the lines to the channel. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelwriter-endwrite__iasyncresult.html language=enus -->
## TOPIC 00532: EndWrite(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelwriter-endwrite__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelwriter-endwrite__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous write initiated with BeginWriteMultiSample(bool, double[, ], AsyncCallback, object) or BeginWriteSingleSample(bool, double[], AsyncCallback, object). SyntaxNamespace: NationalInstruments.DAQmxpublic void EndWrite(IAsyncResult asyncResult)RemarksIf you call EndWrite

### EndWrite(IAsyncResult)

Handles the end of an asynchronous write initiated with [BeginWriteMultiSample(bool, double[, ], AsyncCallback, object)](nationalinstruments-daqmx-analogmultichannelwriter-beginwritemultisample__bool-double_arr2-asynccallback-object.html) or [BeginWriteSingleSample(bool, double[], AsyncCallback, object)](nationalinstruments-daqmx-analogmultichannelwriter-beginwritesinglesample__bool-double_arr1-asynccallback-object.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void EndWrite(IAsyncResult asyncResult)

#### Remarks

If you call EndWrite(IAsyncResult) before the asynchronous write represented by the provided IAsyncResult is complete, EndWrite(IAsyncResult) waits for the write to complete before returning. For a write to a buffered task, the write is considered complete when all of the written samples have been transferred to the task buffer. Use [IsDone](nationalinstruments-daqmx-task-isdone.html) or [WaitUntilDone(TimeSpan)](nationalinstruments-daqmx-task-waituntildone__timespan.html) on the [Task](nationalinstruments-daqmx-task.html) object to determine if a task has generated all of the data it was configured to generate.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginWriteMultiSample(bool, double[, ], AsyncCallback, object) or BeginWriteSingleSample(bool, double[], AsyncCallback, object). |

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginWriteMultiSample(bool, double[, ], AsyncCallback, object) or BeginWriteSingleSample(bool, double[], AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| IndexOutOfRangeException | The data provided to BeginWriteMultiSample(bool, double[, ], AsyncCallback, object) or BeginWriteSingleSample(bool, double[], AsyncCallback, object) has a non-zero lower bound. |

Parent topic:

AnalogMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelwriter-synchronizecallbacks.html language=enus -->
## TOPIC 00533: SynchronizeCallbacks

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelwriter-synchronizecallbacks.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelwriter-synchronizecallbacks.html
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

AnalogMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelwriter-synchronizingobject.html language=enus -->
## TOPIC 00534: SynchronizingObject

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelwriter-synchronizingobject.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelwriter-synchronizingobject.html
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

For more information, refer to Events, Callbacks, and Thread Safety in Measurement Studio .NET Class Libraries and [Asynchronous Reads and Writes](https://#).

Asynchronous Reads and Writes

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelwriter-tostring.html language=enus -->
## TOPIC 00535: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelwriter-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelwriter-tostring.html
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

AnalogMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelwriter-writemultisample__bool-double_arr2.html language=enus -->
## TOPIC 00536: WriteMultiSample(bool, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelwriter-writemultisample__bool-double_arr2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelwriter-writemultisample__bool-double_arr2.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more floating-point samples to one or more AOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteMultiSample([MarshalAs(UnmanagedType.U1)] bool autoStart, double[,] data)RemarksNI-DAQmx scales the generated data to the units of the measurement, includi

### WriteMultiSample(bool, double)

Writes one or more floating-point samples to one or more [AOChannel](nationalinstruments-daqmx-aochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteMultiSample([MarshalAs(UnmanagedType.U1)] bool autoStart, double[,] data)

#### Remarks

NI-DAQmx scales the generated data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

If the task uses on-demand timing, this method returns only after the device generates all samples. If the task uses any timing type other than on-demand, this method returns immediately and does not wait for the device to generate all samples. Your application must call the [WaitUntilDone](nationalinstruments-daqmx-task-waituntildone__int.html) method to block until the device has generated all samples.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | double | A 2D array of samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array corresponds to the order in which you add the channels to the task. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

Parent topic:

AnalogMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelwriter-writesinglesample__bool-double_arr1.html language=enus -->
## TOPIC 00537: WriteSingleSample(bool, double[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelwriter-writesinglesample__bool-double_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelwriter-writesinglesample__bool-double_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a single floating-point sample to one or more AOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteSingleSample([MarshalAs(UnmanagedType.U1)] bool autoStart, double[] data)RemarksNI-DAQmx scales the generated data to the units of the measurement, including a

### WriteSingleSample(bool, double[])

Writes a single floating-point sample to one or more [AOChannel](nationalinstruments-daqmx-aochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteSingleSample([MarshalAs(UnmanagedType.U1)] bool autoStart, double[] data)

#### Remarks

NI-DAQmx scales the generated data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | double[] | A 1D array of samples to write to the task. Each element of the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

Parent topic:

AnalogMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelwriter-writewaveform_tdata___bool-analogwaveform_tdata__arr1.html language=enus -->
## TOPIC 00538: WriteWaveform< TData >(bool, AnalogWaveform< TData >[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelwriter-writewaveform_tdata___bool-analogwaveform_tdata__arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelwriter-writewaveform_tdata___bool-analogwaveform_tdata__arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more analog waveform samples to one or more AOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteWaveform< TData >([MarshalAs(UnmanagedType.U1)] bool autoStart, AnalogWaveform< TData >[] data)RemarksIf the task uses on-demand timing, the WriteWaveform

### WriteWaveform< TData >(bool, AnalogWaveform< TData >[])

Writes one or more analog waveform samples to one or more [AOChannel](nationalinstruments-daqmx-aochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteWaveform< TData >([MarshalAs(UnmanagedType.U1)] bool autoStart, AnalogWaveform< TData >[] data)

#### Remarks

If the task uses on-demand timing, the **WriteWaveform** method returns only after the device generates all samples. If the task uses any timing type other than on-demand, **WriteWaveform** returns immediately and does not wait for the device to generate all samples. Your application must call the [WaitUntilDone](nationalinstruments-daqmx-task-waituntildone__int.html) method to wait until the device has generated all samples.

Analog waveform writes are not affected by the WaveformTiming.SampleInterval or WaveformTiming.StartTime properties on AnalogWaveformTData. To configure timing for analog waveform writes, use the [ConfigureSampleClock(string, double, SampleClockActiveEdge, SampleQuantityMode, int)](nationalinstruments-daqmx-timing-configuresampleclock__string-double-sampleclockactiveedge-samplequantitymode-int.html) method.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If you set autoStart to true, WriteWaveform automatically calls Start if you do not explicitly call Start. You cannot set this parameter to true if you have installed events on the task. |
| data | AnalogWaveform< TData >[] | A 1D array of AnalogWaveformTData objects to write to the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task. The order of the lines in the analog waveform corresponds to the order in which you add the lines to the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

Parent topic:

AnalogMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelwriter.html language=enus -->
## TOPIC 00539: AnalogMultiChannelWriter Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelwriter.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelwriter.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains methods for writing samples to one or more analog output channels in a task. Derives fromMarshalByRefObjectISynchronizeCallbacksISupportSynchronizationContextSyntaxNamespace: NationalInstruments.DAQmxpublic class AnalogMultiChannelWriter : MarshalByRefObject, ISynchronizeCallbacks, ISupport

### AnalogMultiChannelWriter Class

Contains methods for writing samples to one or more analog output channels in a task.

#### Derives from

- MarshalByRefObject
- ISynchronizeCallbacks
- ISupportSynchronizationContext

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class AnalogMultiChannelWriter : MarshalByRefObject, ISynchronizeCallbacks, ISupportSynchronizationContext

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| AnalogMultiChannelWriter(DaqStream) | Creates a new instance of the AnalogMultiChannelWriter class to write to the specified DaqStream. |

#### Properties

| Name | Description |
| --- | --- |
| SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |
| SynchronizingObject | Obsolete: Use SynchronizeCallbacks to specify that the object marshals callbacks across threads appropriately. Will warn if usedGets or sets the object that marshals event-handler and callback calls. |

#### Methods

| Name | Description |
| --- | --- |
| BeginWriteMultiSample(bool, double, AsyncCallback, object) | Begins an asynchronous write of one or more floating-point samples to one or more AOChannel objects in a task. |
| BeginWriteSingleSample(bool, double[], AsyncCallback, object) | Begins an asynchronous write of a single floating-point sample to one or more AOChannel objects in a task. |
| BeginWriteWaveform< TData >(bool, AnalogWaveform< TData >[], AsyncCallback, object) | Begins an asynchronous write of one or more analog waveform samples to one or more AOChannel objects in a task. |
| EndWrite(IAsyncResult) | Handles the end of an asynchronous write initiated with BeginWriteMultiSample(bool, double[, ], AsyncCallback, object) or BeginWriteSingleSample(bool, double[], AsyncCallback, object). |
| ToString() | Returns a string representation of the object. |
| WriteMultiSample(bool, double) | Writes one or more floating-point samples to one or more AOChannel objects in a task. |
| WriteSingleSample(bool, double[]) | Writes a single floating-point sample to one or more AOChannel objects in a task. |
| WriteWaveform< TData >(bool, AnalogWaveform< TData >[]) | Writes one or more analog waveform samples to one or more AOChannel objects in a task. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultiedgereferencetrigger-couplings.html language=enus -->
## TOPIC 00540: Couplings

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultiedgereferencetrigger-couplings.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultiedgereferencetrigger-couplings.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array that describes the couplings for the corresponding source signal of the trigger if the source is a terminal rather than a virtual channel. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arr

### Couplings

Specifies an array that describes the couplings for the corresponding source signal of the trigger if the source is a terminal rather than a virtual channel. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AnalogMultiEdgeReferenceTriggerCoupling](nationalinstruments-daqmx-analogmultiedgereferencetriggercoupling.html)[] Couplings { get; set; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogMultiEdgeReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultiedgereferencetrigger-hystereses.html language=enus -->
## TOPIC 00541: Hystereses

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultiedgereferencetrigger-hystereses.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultiedgereferencetrigger-hystereses.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of hysteresis levels in the units of the measurement or generation. If the corresponding element of Ref.AnlgMultiEdge.Slopes is Rising, the trigger does not deassert until the source signal passes below the corresponding element of Ref.AnlgMultiEdge.Lvls minus the hysteresis. If R

### Hystereses

Specifies an array of hysteresis levels in the units of the measurement or generation. If the corresponding element of Ref.AnlgMultiEdge.Slopes is Rising, the trigger does not deassert until the source signal passes below the corresponding element of Ref.AnlgMultiEdge.Lvls minus the hysteresis. If Ref.AnlgEdge.Slope is Falling, the trigger does not deassert until the source signal passes above Ref.AnlgEdge.Lvl plus the hysteresis. Hysteresis is always enabled. Set this property to a non-zero value to use hysteresis. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] Hystereses { get; set; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogMultiEdgeReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultiedgereferencetrigger-levels.html language=enus -->
## TOPIC 00542: Levels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultiedgereferencetrigger-levels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultiedgereferencetrigger-levels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of thresholds in the units of the measurement or generation to start acquiring or generating samples. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty. SyntaxNam

### Levels

Specifies an array of thresholds in the units of the measurement or generation to start acquiring or generating samples. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] Levels { get; set; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogMultiEdgeReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultiedgereferencetrigger-slopes.html language=enus -->
## TOPIC 00543: Slopes

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultiedgereferencetrigger-slopes.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultiedgereferencetrigger-slopes.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of slopes on which to trigger task to start generating or acquiring samples. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty. SyntaxNamespace: NationalInstrumen

### Slopes

Specifies an array of slopes on which to trigger task to start generating or acquiring samples. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AnalogMultiEdgeReferenceTriggerSlope](nationalinstruments-daqmx-analogmultiedgereferencetriggerslope.html)[] Slopes { get; set; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogMultiEdgeReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultiedgereferencetrigger-sources.html language=enus -->
## TOPIC 00544: Sources

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultiedgereferencetrigger-sources.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultiedgereferencetrigger-sources.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a List and/or range of analog sources that are going to be used for Analog triggering. Each source corresponds to an element in each of the Analog Multi Edge property arrays, if they are not empty. SyntaxNamespace: NationalInstruments.DAQmxpublic string Sources { get; set; }ExceptionsTypeD

### Sources

Specifies a List and/or range of analog sources that are going to be used for Analog triggering. Each source corresponds to an element in each of the Analog Multi Edge property arrays, if they are not empty.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Sources { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogMultiEdgeReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultiedgereferencetrigger-tostring.html language=enus -->
## TOPIC 00545: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultiedgereferencetrigger-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultiedgereferencetrigger-tostring.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the object. SyntaxNamespace: NationalInstruments.DAQmxpublic override string ToString()

### ToString()

Returns a string representation of the object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override string ToString()

Parent topic:

AnalogMultiEdgeReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultiedgereferencetrigger.html language=enus -->
## TOPIC 00546: AnalogMultiEdgeReferenceTrigger Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultiedgereferencetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultiedgereferencetrigger.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides properties for configuring analog multi-edge reference triggers. Derives fromMarshalByRefObjectIFilteredTypeDescriptorSyntaxNamespace: NationalInstruments.DAQmxpublic class AnalogMultiEdgeReferenceTrigger : MarshalByRefObject, IFilteredTypeDescriptorRemarksUse this class to configure the ta

### AnalogMultiEdgeReferenceTrigger Class

Provides properties for configuring analog multi-edge reference triggers.

#### Derives from

- MarshalByRefObject
- IFilteredTypeDescriptor

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class AnalogMultiEdgeReferenceTrigger : MarshalByRefObject, IFilteredTypeDescriptor

#### Remarks

ConfigureAnalogMultiEdgeTrigger(string, AnalogMultiEdgeReferenceTriggerSlope[], double[], long)

AnalogMultiEdge

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

Analog triggering

Reference triggers

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Couplings | Specifies an array that describes the couplings for the corresponding source signal of the trigger if the source is a terminal rather than a virtual channel. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty. |
| Hystereses | Specifies an array of hysteresis levels in the units of the measurement or generation. If the corresponding element of Ref.AnlgMultiEdge.Slopes is Rising, the trigger does not deassert until the source signal passes below the corresponding element of Ref.AnlgMultiEdge.Lvls minus the hysteresis. If Ref.AnlgEdge.Slope is Falling, the trigger does not deassert until the source signal passes above Ref.AnlgEdge.Lvl plus the hysteresis. Hysteresis is always enabled. Set this property to a non-zero value to use hysteresis. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty. |
| Levels | Specifies an array of thresholds in the units of the measurement or generation to start acquiring or generating samples. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty. |
| Slopes | Specifies an array of slopes on which to trigger task to start generating or acquiring samples. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty. |
| Sources | Specifies a List and/or range of analog sources that are going to be used for Analog triggering. Each source corresponds to an element in each of the Analog Multi Edge property arrays, if they are not empty. |

#### Methods

| Name | Description |
| --- | --- |
| ToString() | Returns a string representation of the object. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultiedgereferencetriggercoupling.html language=enus -->
## TOPIC 00547: AnalogMultiEdgeReferenceTriggerCoupling Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultiedgereferencetriggercoupling.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultiedgereferencetriggercoupling.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array that describes the couplings for the corresponding source signal of the trigger if the source is a terminal rather than a virtual channel. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arr

### AnalogMultiEdgeReferenceTriggerCoupling Enumeration

Specifies an array that describes the couplings for the corresponding source signal of the trigger if the source is a terminal rather than a virtual channel. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AnalogMultiEdgeReferenceTriggerCoupling

#### Remarks

Specifies an array that describes the couplings for the corresponding source signal of the trigger if the source is a terminal rather than a virtual channel. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty. Use this enumeration to get or set the value of [Couplings](nationalinstruments-daqmx-analogmultiedgereferencetrigger-couplings.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AC | 10045 | Alternating Current. |
| DC | 10050 | Direct Current. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultiedgereferencetriggerslope.html language=enus -->
## TOPIC 00548: AnalogMultiEdgeReferenceTriggerSlope Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultiedgereferencetriggerslope.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultiedgereferencetriggerslope.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of slopes on which to trigger task to start generating or acquiring samples. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty. SyntaxNamespace: NationalInstrumen

### AnalogMultiEdgeReferenceTriggerSlope Enumeration

Specifies an array of slopes on which to trigger task to start generating or acquiring samples. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AnalogMultiEdgeReferenceTriggerSlope

#### Remarks

Specifies an array of slopes on which to trigger task to start generating or acquiring samples. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty. Use this enumeration to get or set the value of [Slopes](nationalinstruments-daqmx-analogmultiedgereferencetrigger-slopes.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rising | 10280 | Trigger on the rising slope of the signal. |
| Falling | 10171 | Trigger on the falling slope of the signal. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultiedgestarttrigger-couplings.html language=enus -->
## TOPIC 00549: Couplings

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultiedgestarttrigger-couplings.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultiedgestarttrigger-couplings.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array that describes the couplings for the corresponding source signal of the trigger if the source is a terminal rather than a virtual channel. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property a

### Couplings

Specifies an array that describes the couplings for the corresponding source signal of the trigger if the source is a terminal rather than a virtual channel. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AnalogMultiEdgeStartTriggerCoupling](nationalinstruments-daqmx-analogmultiedgestarttriggercoupling.html)[] Couplings { get; set; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogMultiEdgeStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultiedgestarttrigger-hystereses.html language=enus -->
## TOPIC 00550: Hystereses

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultiedgestarttrigger-hystereses.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultiedgestarttrigger-hystereses.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of hysteresis levels in the units of the measurement or generation. If the corresponding element of Start.AnlgMultiEdge.Slopes is Rising, the trigger does not deassert until the source signal passes below the corresponding element of Start.AnlgMultiEdge.Lvls minus the hysteresis.

### Hystereses

Specifies an array of hysteresis levels in the units of the measurement or generation. If the corresponding element of Start.AnlgMultiEdge.Slopes is Rising, the trigger does not deassert until the source signal passes below the corresponding element of Start.AnlgMultiEdge.Lvls minus the hysteresis. If Start.AnlgEdge.Slope is Falling, the trigger does not deassert until the source signal passes above Start.AnlgEdge.Lvl plus the hysteresis. Hysteresis is always enabled. Set this property to a non-zero value to use hysteresis. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] Hystereses { get; set; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogMultiEdgeStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultiedgestarttrigger-levels.html language=enus -->
## TOPIC 00551: Levels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultiedgestarttrigger-levels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultiedgestarttrigger-levels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of thresholds in the units of the measurement or generation to start acquiring or generating samples. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty. SyntaxN

### Levels

Specifies an array of thresholds in the units of the measurement or generation to start acquiring or generating samples. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] Levels { get; set; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogMultiEdgeStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultiedgestarttrigger-slopes.html language=enus -->
## TOPIC 00552: Slopes

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultiedgestarttrigger-slopes.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultiedgestarttrigger-slopes.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of slopes on which to trigger task to start generating or acquiring samples. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty. SyntaxNamespace: NationalInstrum

### Slopes

Specifies an array of slopes on which to trigger task to start generating or acquiring samples. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AnalogMultiEdgeStartTriggerSlope](nationalinstruments-daqmx-analogmultiedgestarttriggerslope.html)[] Slopes { get; set; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogMultiEdgeStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultiedgestarttrigger-sources.html language=enus -->
## TOPIC 00553: Sources

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultiedgestarttrigger-sources.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultiedgestarttrigger-sources.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a list and/or range of analog sources that are going to be used for Analog triggering. Each source corresponds to an element in each of the Analog Multi Edge property arrays, if they are not empty. SyntaxNamespace: NationalInstruments.DAQmxpublic string Sources { get; set; }ExceptionsTypeD

### Sources

Specifies a list and/or range of analog sources that are going to be used for Analog triggering. Each source corresponds to an element in each of the Analog Multi Edge property arrays, if they are not empty.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Sources { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogMultiEdgeStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultiedgestarttrigger-tostring.html language=enus -->
## TOPIC 00554: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultiedgestarttrigger-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultiedgestarttrigger-tostring.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the object. SyntaxNamespace: NationalInstruments.DAQmxpublic override string ToString()

### ToString()

Returns a string representation of the object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override string ToString()

Parent topic:

AnalogMultiEdgeStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultiedgestarttrigger.html language=enus -->
## TOPIC 00555: AnalogMultiEdgeStartTrigger Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultiedgestarttrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultiedgestarttrigger.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides properties for configuring analog multi-edge start triggers. Derives fromMarshalByRefObjectIFilteredTypeDescriptorSyntaxNamespace: NationalInstruments.DAQmxpublic class AnalogMultiEdgeStartTrigger : MarshalByRefObject, IFilteredTypeDescriptorRemarksUse this class to configure the task to st

### AnalogMultiEdgeStartTrigger Class

Provides properties for configuring analog multi-edge start triggers.

#### Derives from

- MarshalByRefObject
- IFilteredTypeDescriptor

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class AnalogMultiEdgeStartTrigger : MarshalByRefObject, IFilteredTypeDescriptor

#### Remarks

ConfigureAnalogMultiEdgeTrigger(string, AnalogMultiEdgeStartTriggerSlope[], double[])

AnalogMultiEdge

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

Analog triggering

Start triggers

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Couplings | Specifies an array that describes the couplings for the corresponding source signal of the trigger if the source is a terminal rather than a virtual channel. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty. |
| Hystereses | Specifies an array of hysteresis levels in the units of the measurement or generation. If the corresponding element of Start.AnlgMultiEdge.Slopes is Rising, the trigger does not deassert until the source signal passes below the corresponding element of Start.AnlgMultiEdge.Lvls minus the hysteresis. If Start.AnlgEdge.Slope is Falling, the trigger does not deassert until the source signal passes above Start.AnlgEdge.Lvl plus the hysteresis. Hysteresis is always enabled. Set this property to a non-zero value to use hysteresis. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty. |
| Levels | Specifies an array of thresholds in the units of the measurement or generation to start acquiring or generating samples. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty. |
| Slopes | Specifies an array of slopes on which to trigger task to start generating or acquiring samples. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty. |
| Sources | Specifies a list and/or range of analog sources that are going to be used for Analog triggering. Each source corresponds to an element in each of the Analog Multi Edge property arrays, if they are not empty. |

#### Methods

| Name | Description |
| --- | --- |
| ToString() | Returns a string representation of the object. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultiedgestarttriggercoupling.html language=enus -->
## TOPIC 00556: AnalogMultiEdgeStartTriggerCoupling Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultiedgestarttriggercoupling.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultiedgestarttriggercoupling.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array that describes the couplings for the corresponding source signal of the trigger if the source is a terminal rather than a virtual channel. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property a

### AnalogMultiEdgeStartTriggerCoupling Enumeration

Specifies an array that describes the couplings for the corresponding source signal of the trigger if the source is a terminal rather than a virtual channel. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AnalogMultiEdgeStartTriggerCoupling

#### Remarks

Specifies an array that describes the couplings for the corresponding source signal of the trigger if the source is a terminal rather than a virtual channel. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty. Use this enumeration to get or set the value of [Couplings](nationalinstruments-daqmx-analogmultiedgestarttrigger-couplings.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AC | 10045 | Alternating Current. |
| DC | 10050 | Direct Current. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultiedgestarttriggerslope.html language=enus -->
## TOPIC 00557: AnalogMultiEdgeStartTriggerSlope Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultiedgestarttriggerslope.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultiedgestarttriggerslope.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of slopes on which to trigger task to start generating or acquiring samples. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty. SyntaxNamespace: NationalInstrum

### AnalogMultiEdgeStartTriggerSlope Enumeration

Specifies an array of slopes on which to trigger task to start generating or acquiring samples. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AnalogMultiEdgeStartTriggerSlope

#### Remarks

Specifies an array of slopes on which to trigger task to start generating or acquiring samples. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty. Use this enumeration to get or set the value of [Slopes](nationalinstruments-daqmx-analogmultiedgestarttrigger-slopes.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rising | 10280 | Trigger on the rising slope of the signal. |
| Falling | 10171 | Trigger on the falling slope of the signal. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-analogsinglechannelreader__daqstream.html language=enus -->
## TOPIC 00558: AnalogSingleChannelReader(DaqStream)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-analogsinglechannelreader__daqstream.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-analogsinglechannelreader__daqstream.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of the AnalogSingleChannelReader class to read from the specified DaqStream. SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogSingleChannelReader(DaqStream stream)RemarksEach Task object contains a Stream property that serves as the connection point for readers to access

### AnalogSingleChannelReader(DaqStream)

Creates a new instance of the [AnalogSingleChannelReader](nationalinstruments-daqmx-analogsinglechannelreader.html) class to read from the specified [DaqStream](nationalinstruments-daqmx-daqstream.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public AnalogSingleChannelReader(DaqStream stream)

#### Remarks

Each [Task](nationalinstruments-daqmx-task.html) object contains a [Stream](nationalinstruments-daqmx-task-stream.html) property that serves as the connection point for readers to access the samples generated by that task.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| stream | DaqStream | The DaqStream to read. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-beginmemoryoptimizedreadmultisample__int-asynccallback-object-double_arr1-reallocationpolicy.html language=enus -->
## TOPIC 00559: BeginMemoryOptimizedReadMultiSample(int, AsyncCallback, object, double[], ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-beginmemoryoptimizedreadmultisample__int-asynccallback-object-double_arr1-reallocationpolicy.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-beginmemoryoptimizedreadmultisample__int-asynccallback-object-double_arr1-reallocationpolicy.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more floating-point samples from a single AIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSample(int numberOfSamples, AsyncCallback callback, object state, double[] data, ReallocationPolicy policy)R

### BeginMemoryOptimizedReadMultiSample(int, AsyncCallback, object, double[], ReallocationPolicy)

Begins an asynchronous read of one or more floating-point samples from a single [AIChannel](nationalinstruments-daqmx-aichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSample(int numberOfSamples, AsyncCallback callback, object state, double[] data, ReallocationPolicy policy)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSample(IAsyncResult, out int)](nationalinstruments-daqmx-analogsinglechannelreader-endmemoryoptimizedreadmultisample__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | double[] | An initialized 1D array of floating-point samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-beginmemoryoptimizedreadmultisample__int-asynccallback-object-double_arr1.html language=enus -->
## TOPIC 00560: BeginMemoryOptimizedReadMultiSample(int, AsyncCallback, object, double[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-beginmemoryoptimizedreadmultisample__int-asynccallback-object-double_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-beginmemoryoptimizedreadmultisample__int-asynccallback-object-double_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more floating-point samples from a single AIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSample(int numberOfSamples, AsyncCallback callback, object state, double[] data)RemarksIf the data buffer is

### BeginMemoryOptimizedReadMultiSample(int, AsyncCallback, object, double[])

Begins an asynchronous read of one or more floating-point samples from a single [AIChannel](nationalinstruments-daqmx-aichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSample(int numberOfSamples, AsyncCallback callback, object state, double[] data)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSample(IAsyncResult, out int)](nationalinstruments-daqmx-analogsinglechannelreader-endmemoryoptimizedreadmultisample__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to – 1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to – 1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. Setting numberOfSamples to – 1 returns all available samples or 2 31– 1 samples, whichever is smaller. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | double[] | An initialized 1D array of floating-point samples that contains the read data. Each element in the array corresponds to a sample from the channel. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-beginmemoryoptimizedreadmultisamplepower__int-asynccallback-object-aipowermeasurement_arr1-reallocationpolicy.html language=enus -->
## TOPIC 00561: BeginMemoryOptimizedReadMultiSamplePower(int, AsyncCallback, object, AIPowerMeasurement[], ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-beginmemoryoptimizedreadmultisamplepower__int-asynccallback-object-aipowermeasurement_arr1-reallocationpolicy.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-beginmemoryoptimizedreadmultisamplepower__int-asynccallback-object-aipowermeasurement_arr1-reallocationpolicy.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more power samples from a single AIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSamplePower(int numberOfSamples, AsyncCallback callback, object state, AIPowerMeasurement[] data, ReallocationPolicy

### BeginMemoryOptimizedReadMultiSamplePower(int, AsyncCallback, object, AIPowerMeasurement[], ReallocationPolicy)

Begins an asynchronous read of one or more power samples from a single [AIChannel](nationalinstruments-daqmx-aichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSamplePower(int numberOfSamples, AsyncCallback callback, object state, AIPowerMeasurement[] data, ReallocationPolicy policy)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSamplePower(IAsyncResult, out int)](nationalinstruments-daqmx-analogsinglechannelreader-endmemoryoptimizedreadmultisamplepower__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | AIPowerMeasurement[] | An initialized 1D array of power samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-beginmemoryoptimizedreadmultisamplepower__int-asynccallback-object-aipowermeasurement_arr1.html language=enus -->
## TOPIC 00562: BeginMemoryOptimizedReadMultiSamplePower(int, AsyncCallback, object, AIPowerMeasurement[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-beginmemoryoptimizedreadmultisamplepower__int-asynccallback-object-aipowermeasurement_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-beginmemoryoptimizedreadmultisamplepower__int-asynccallback-object-aipowermeasurement_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more power samples from a single AIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSamplePower(int numberOfSamples, AsyncCallback callback, object state, AIPowerMeasurement[] data)RemarksIf the data b

### BeginMemoryOptimizedReadMultiSamplePower(int, AsyncCallback, object, AIPowerMeasurement[])

Begins an asynchronous read of one or more power samples from a single [AIChannel](nationalinstruments-daqmx-aichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSamplePower(int numberOfSamples, AsyncCallback callback, object state, AIPowerMeasurement[] data)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSamplePower(IAsyncResult, out int)](nationalinstruments-daqmx-analogsinglechannelreader-endmemoryoptimizedreadmultisamplepower__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to – 1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to – 1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. Setting numberOfSamples to – 1 returns all available samples or 2 31– 1 samples, whichever is smaller. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | AIPowerMeasurement[] | An initialized 1D array of power samples that contains the read data. Each element in the array corresponds to a sample from the channel. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-beginmemoryoptimizedreadwaveform__int-asynccallback-object-analogwaveform_double..html language=enus -->
## TOPIC 00563: BeginMemoryOptimizedReadWaveform(int, AsyncCallback, object, AnalogWaveform< double >)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-beginmemoryoptimizedreadwaveform__int-asynccallback-object-analogwaveform_double..html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-beginmemoryoptimizedreadwaveform__int-asynccallback-object-analogwaveform_double..html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more analog waveform samples from a single AIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadWaveform(int numberOfSamples, AsyncCallback callback, object state, AnalogWaveform< double > data)RemarksIf the

### BeginMemoryOptimizedReadWaveform(int, AsyncCallback, object, AnalogWaveform< double >)

Begins an asynchronous read of one or more analog waveform samples from a single [AIChannel](nationalinstruments-daqmx-aichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadWaveform(int numberOfSamples, AsyncCallback callback, object state, AnalogWaveform< double > data)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing AnalogWaveformTData objects and their corresponding memory to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginMemoryOptimizedReadWaveform(int, AsyncCallback, object, AnalogWaveform<double>), call [EndMemoryOptimizedReadWaveform(IAsyncResult)](nationalinstruments-daqmx-analogsinglechannelreader-endmemoryoptimizedreadwaveform__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](nationalinstruments-daqmx-daqstream-waveformattributemode.html) property of the [DaqStream](nationalinstruments-daqmx-daqstream.html) you are reading from.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | AnalogWaveform< double > | An initialized AnalogWaveformTData that contains the read data. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-beginmemoryoptimizedreadwaveform__int-asynccallback-object-analogwaveform_double_-reallocationpolicy.html language=enus -->
## TOPIC 00564: BeginMemoryOptimizedReadWaveform(int, AsyncCallback, object, AnalogWaveform< double >, ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-beginmemoryoptimizedreadwaveform__int-asynccallback-object-analogwaveform_double_-reallocationpolicy.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-beginmemoryoptimizedreadwaveform__int-asynccallback-object-analogwaveform_double_-reallocationpolicy.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more analog waveform samples from a single AIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadWaveform(int numberOfSamples, AsyncCallback callback, object state, AnalogWaveform< double > data, ReallocationP

### BeginMemoryOptimizedReadWaveform(int, AsyncCallback, object, AnalogWaveform< double >, ReallocationPolicy)

Begins an asynchronous read of one or more analog waveform samples from a single [AIChannel](nationalinstruments-daqmx-aichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadWaveform(int numberOfSamples, AsyncCallback callback, object state, AnalogWaveform< double > data, ReallocationPolicy policy)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing AnalogWaveformTData objects and their corresponding memory to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with [BeginMemoryOptimizedReadWaveform(int, AsyncCallback, object, AnalogWaveform<double>)](nationalinstruments-daqmx-analogsinglechannelreader-beginmemoryoptimizedreadwaveform__int-asynccallback-object-analogwaveform_double..html) , call [EndMemoryOptimizedReadWaveform(IAsyncResult)](nationalinstruments-daqmx-analogsinglechannelreader-endmemoryoptimizedreadwaveform__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](nationalinstruments-daqmx-daqstream-waveformattributemode.html) property of the [DaqStream](nationalinstruments-daqmx-daqstream.html) you are reading from.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | AnalogWaveform< double > | An initialized AnalogWaveformTData that contains the read data. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-beginmemoryoptimizedreadwaveform__timespan-asynccallback-object-analogwaveform_double..html language=enus -->
## TOPIC 00565: BeginMemoryOptimizedReadWaveform(TimeSpan, AsyncCallback, object, AnalogWaveform< double >)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-beginmemoryoptimizedreadwaveform__timespan-asynccallback-object-analogwaveform_double..html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-beginmemoryoptimizedreadwaveform__timespan-asynccallback-object-analogwaveform_double..html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous, memory-optimized read of one or more analog waveform samples from a single AIChannel object in a task for a specified duration . SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadWaveform(TimeSpan duration, AsyncCallback callback, object st

### BeginMemoryOptimizedReadWaveform(TimeSpan, AsyncCallback, object, AnalogWaveform< double >)

Begins an asynchronous, memory-optimized read of one or more analog waveform samples from a single [AIChannel](nationalinstruments-daqmx-aichannel.html) object in a task for a specified *duration* .

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadWaveform(TimeSpan duration, AsyncCallback callback, object state, AnalogWaveform< double > data)

#### Remarks

If the *data*  waveform is large enough to hold the number of samples requested, this overload attempts to reuse the existing AnalogWaveformTData object's memory to store acquired data. This results in more efficient memory allocation when performing subsequent reads with a continuous analog input task, if each subsequent read acquires the same or fewer number of samples.

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginMemoryOptimizedReadWaveform(TimeSpan, AsyncCallback, object, AnalogWaveform<double>), call [EndMemoryOptimizedReadWaveform(IAsyncResult)](nationalinstruments-daqmx-analogsinglechannelreader-endmemoryoptimizedreadwaveform__iasyncresult.html), passing the returned IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units when creating channels using the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](nationalinstruments-daqmx-daqstream-waveformattributemode.html) property of the [DaqStream](nationalinstruments-daqmx-daqstream.html) being read.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the [Stream](nationalinstruments-daqmx-task-stream.html) object used for the reads or writes.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| duration | TimeSpan | The duration of time to read the waveform. The duration specified must be long enough to read at least one sample at the configured SampleClockRate. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | AnalogWaveform< double > | An initialized AnalogWaveformTData that contains the read data. If data is not large enough to hold all samples read, a new AnalogWaveformTData is allocated to hold the data. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-beginmemoryoptimizedreadwaveform__timespan-asynccallback-object-analogwaveform_double_-reallocationpolicy.html language=enus -->
## TOPIC 00566: BeginMemoryOptimizedReadWaveform(TimeSpan, AsyncCallback, object, AnalogWaveform< double >, ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-beginmemoryoptimizedreadwaveform__timespan-asynccallback-object-analogwaveform_double_-reallocationpolicy.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-beginmemoryoptimizedreadwaveform__timespan-asynccallback-object-analogwaveform_double_-reallocationpolicy.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous, memory-optimized read of one or more analog waveform samples from a single AIChannel object in a task for a specified duration . SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadWaveform(TimeSpan duration, AsyncCallback callback, object st

### BeginMemoryOptimizedReadWaveform(TimeSpan, AsyncCallback, object, AnalogWaveform< double >, ReallocationPolicy)

Begins an asynchronous, memory-optimized read of one or more analog waveform samples from a single [AIChannel](nationalinstruments-daqmx-aichannel.html) object in a task for a specified *duration* .

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadWaveform(TimeSpan duration, AsyncCallback callback, object state, AnalogWaveform< double > data, ReallocationPolicy policy)

#### Remarks

If the *data*  waveform is large enough to hold the number of samples requested, this overload attempts to reuse the existing AnalogWaveformTData object's memory to store acquired data. This results in more efficient memory allocation when performing subsequent reads with a continuous analog input task, if each subsequent read acquires the same or fewer number of samples.

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginMemoryOptimizedReadWaveform(TimeSpan, AsyncCallback, object, AnalogWaveform<double>, ReallocationPolicy), call [EndMemoryOptimizedReadWaveform(IAsyncResult)](nationalinstruments-daqmx-analogsinglechannelreader-endmemoryoptimizedreadwaveform__iasyncresult.html), passing the returned IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units when creating channels using the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](nationalinstruments-daqmx-daqstream-waveformattributemode.html) property of the [DaqStream](nationalinstruments-daqmx-daqstream.html) being read.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the [Stream](nationalinstruments-daqmx-task-stream.html) object used for the reads or writes.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| duration | TimeSpan | The duration of time to read the waveform. The duration specified must be long enough to read at least one sample at the configured SampleClockRate. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | AnalogWaveform< double > | An initialized AnalogWaveformTData that contains the read data. If data is not large enough to hold all samples read, a new AnalogWaveformTData may be allocated to hold the data depending on the specified policy . |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-beginreadmultisample__int-asynccallback-object.html language=enus -->
## TOPIC 00567: BeginReadMultiSample(int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-beginreadmultisample__int-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-beginreadmultisample__int-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more floating-point samples from a single AIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadMultiSample(int numberOfSamples, AsyncCallback callback, object state)RemarksTo get the read data or any exceptions that occurre

### BeginReadMultiSample(int, AsyncCallback, object)

Begins an asynchronous read of one or more floating-point samples from a single [AIChannel](nationalinstruments-daqmx-aichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadMultiSample(int numberOfSamples, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadMultiSample(int, AsyncCallback, object), call [EndReadMultiSample(IAsyncResult)](nationalinstruments-daqmx-analogsinglechannelreader-endreadmultisample__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-beginreadmultisamplepower__int-asynccallback-object.html language=enus -->
## TOPIC 00568: BeginReadMultiSamplePower(int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-beginreadmultisamplepower__int-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-beginreadmultisamplepower__int-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more power samples from a single AIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadMultiSamplePower(int numberOfSamples, AsyncCallback callback, object state)RemarksTo get the read data or any exceptions that occurred du

### BeginReadMultiSamplePower(int, AsyncCallback, object)

Begins an asynchronous read of one or more power samples from a single [AIChannel](nationalinstruments-daqmx-aichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadMultiSamplePower(int numberOfSamples, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadMultiSamplePower(int, AsyncCallback, object), call [EndReadMultiSamplePower(IAsyncResult)](nationalinstruments-daqmx-analogsinglechannelreader-endreadmultisamplepower__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-beginreadsinglesample__asynccallback-object.html language=enus -->
## TOPIC 00569: BeginReadSingleSample(AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-beginreadsinglesample__asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-beginreadsinglesample__asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of a single floating-point sample from a single AIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadSingleSample(AsyncCallback callback, object state)RemarksTo get the read data or any exceptions that occurred during an asynchronous

### BeginReadSingleSample(AsyncCallback, object)

Begins an asynchronous read of a single floating-point sample from a single [AIChannel](nationalinstruments-daqmx-aichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadSingleSample(AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSample(AsyncCallback, object), call [EndReadSingleSample(IAsyncResult)](nationalinstruments-daqmx-analogsinglechannelreader-endreadsinglesample__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-beginreadsinglesamplepower__asynccallback-object.html language=enus -->
## TOPIC 00570: BeginReadSingleSamplePower(AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-beginreadsinglesamplepower__asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-beginreadsinglesamplepower__asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of a single power sample from a single AIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadSingleSamplePower(AsyncCallback callback, object state)RemarksTo get the read data or any exceptions that occurred during an asynchronous rea

### BeginReadSingleSamplePower(AsyncCallback, object)

Begins an asynchronous read of a single power sample from a single [AIChannel](nationalinstruments-daqmx-aichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadSingleSamplePower(AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSamplePower(AsyncCallback, object), call [EndReadSingleSamplePower(IAsyncResult)](nationalinstruments-daqmx-analogsinglechannelreader-endreadsinglesamplepower__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-beginreadwaveform__int-asynccallback-object.html language=enus -->
## TOPIC 00571: BeginReadWaveform(int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-beginreadwaveform__int-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-beginreadwaveform__int-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more analog waveform samples from a single AIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadWaveform(int numberOfSamples, AsyncCallback callback, object state)RemarksTo get the read data or any exceptions that occurred

### BeginReadWaveform(int, AsyncCallback, object)

Begins an asynchronous read of one or more analog waveform samples from a single [AIChannel](nationalinstruments-daqmx-aichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadWaveform(int numberOfSamples, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadWaveform(int, AsyncCallback, object), call [EndReadWaveform(IAsyncResult)](nationalinstruments-daqmx-analogsinglechannelreader-endreadwaveform__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](nationalinstruments-daqmx-daqstream-waveformattributemode.html) property of the [DaqStream](nationalinstruments-daqmx-daqstream.html) you are reading from.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-beginreadwaveform__timespan-asynccallback-object.html language=enus -->
## TOPIC 00572: BeginReadWaveform(TimeSpan, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-beginreadwaveform__timespan-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-beginreadwaveform__timespan-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more analog waveform samples from a single AIChannel object in a task for a specified duration . SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadWaveform(TimeSpan duration, AsyncCallback callback, object state)RemarksTo get the read data o

### BeginReadWaveform(TimeSpan, AsyncCallback, object)

Begins an asynchronous read of one or more analog waveform samples from a single [AIChannel](nationalinstruments-daqmx-aichannel.html) object in a task for a specified *duration* .

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadWaveform(TimeSpan duration, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadWaveform(TimeSpan, AsyncCallback, object), call [EndReadWaveform(IAsyncResult)](nationalinstruments-daqmx-analogsinglechannelreader-endreadwaveform__iasyncresult.html), passing the returned IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units when creating channels using the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](nationalinstruments-daqmx-daqstream-waveformattributemode.html) property of the [DaqStream](nationalinstruments-daqmx-daqstream.html) being read.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the [Stream](nationalinstruments-daqmx-task-stream.html) object used for the reads or writes.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| duration | TimeSpan | The duration of time to read the waveform. The duration specified must be long enough to read at least one sample at the configured SampleClockRate. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-endmemoryoptimizedreadmultisample__iasyncresult-out.html language=enus -->
## TOPIC 00573: EndMemoryOptimizedReadMultiSample(IAsyncResult, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-endmemoryoptimizedreadmultisample__iasyncresult-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-endmemoryoptimizedreadmultisample__iasyncresult-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSample(int, AsyncCallback, object, double[]) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] EndMemoryOptimizedReadMultiSample(IAsyncResult asyncResult, out int actualNumberO

### EndMemoryOptimizedReadMultiSample(IAsyncResult, out int)

Handles the end of an asynchronous read initiated with [BeginMemoryOptimizedReadMultiSample(int, AsyncCallback, object, double[])](nationalinstruments-daqmx-analogsinglechannelreader-beginmemoryoptimizedreadmultisample__int-asynccallback-object-double_arr1.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] EndMemoryOptimizedReadMultiSample(IAsyncResult asyncResult, out int actualNumberOfSamplesRead)

#### Remarks

If you call this method before the asynchronous read is complete, it waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadMultiSample(int, AsyncCallback, object, double[]). |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A 1D array of floating-point samples that contains the read data. Each element in the array corresponds to a sample from the channel.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples; or For asynchronous reads, if asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadMultiSample(int, AsyncCallback, object, double[]). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-endmemoryoptimizedreadmultisamplepower__iasyncresult-out.html language=enus -->
## TOPIC 00574: EndMemoryOptimizedReadMultiSamplePower(IAsyncResult, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-endmemoryoptimizedreadmultisamplepower__iasyncresult-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-endmemoryoptimizedreadmultisamplepower__iasyncresult-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePower(int, AsyncCallback, object, AIPowerMeasurement[]) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic AIPowerMeasurement[] EndMemoryOptimizedReadMultiSamplePower(IAsyncResult

### EndMemoryOptimizedReadMultiSamplePower(IAsyncResult, out int)

Handles the end of an asynchronous read initiated with [BeginMemoryOptimizedReadMultiSamplePower(int, AsyncCallback, object, AIPowerMeasurement[])](nationalinstruments-daqmx-analogsinglechannelreader-beginmemoryoptimizedreadmultisamplepower__int-asynccallback-object-aipowermeasurement_arr1.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIPowerMeasurement](nationalinstruments-daqmx-aipowermeasurement.html)[] EndMemoryOptimizedReadMultiSamplePower(IAsyncResult asyncResult, out int actualNumberOfSamplesRead)

#### Remarks

If you call this method before the asynchronous read is complete, it waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadMultiSamplePower(int, AsyncCallback, object, AIPowerMeasurement[]). |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A 1D array of power samples that contains the read data. Each element in the array corresponds to a sample from the channel.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples; or For asynchronous reads, if asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadMultiSamplePower(int, AsyncCallback, object, AIPowerMeasurement[]). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-endmemoryoptimizedreadwaveform__iasyncresult.html language=enus -->
## TOPIC 00575: EndMemoryOptimizedReadWaveform(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-endmemoryoptimizedreadwaveform__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-endmemoryoptimizedreadwaveform__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadWaveform(int, AsyncCallback, object, AnalogWaveform<double>) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogWaveform< double > EndMemoryOptimizedReadWaveform(IAsyncResult asyncResul

### EndMemoryOptimizedReadWaveform(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginMemoryOptimizedReadWaveform(int, AsyncCallback, object, AnalogWaveform<double>)](nationalinstruments-daqmx-analogsinglechannelreader-beginmemoryoptimizedreadwaveform__int-asynccallback-object-analogwaveform_double..html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public AnalogWaveform< double > EndMemoryOptimizedReadWaveform(IAsyncResult asyncResult)

#### Remarks

If you call EndMemoryOptimizedReadWaveform(IAsyncResult) before the asynchronous read is complete, EndMemoryOptimizedReadWaveform(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadWaveform(int, AsyncCallback, object, AnalogWaveform<double>). |

#### Returns

An AnalogWaveformTData containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. For asynchronous reads, if asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadWaveform(int, AsyncCallback, object, AnalogWaveform<double>[]). For reads that take a TimeSpan duration, if the duration provided was less than Zero. |
| NationalInstruments.DAQmx.DaqException | If data is null or is uninitialized. The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-endreadmultisample__iasyncresult.html language=enus -->
## TOPIC 00576: EndReadMultiSample(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-endreadmultisample__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-endreadmultisample__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadMultiSample(int, AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] EndReadMultiSample(IAsyncResult asyncResult)RemarksIf you call EndReadMultiSample(IAsyncResult) before the

### EndReadMultiSample(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadMultiSample(int, AsyncCallback, object)](nationalinstruments-daqmx-analogsinglechannelreader-beginreadmultisample__int-asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] EndReadMultiSample(IAsyncResult asyncResult)

#### Remarks

If you call EndReadMultiSample(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadMultiSample(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadMultiSample(int, AsyncCallback, object). |

#### Returns

A 1D array of floating-point samples from the task. Each element in the array corresponds to a sample from the channel.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadMultiSample(int, AsyncCallback, object) . |
| OutOfMemoryException | There is not enough memory to carry out this operation. |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-endreadmultisamplepower__iasyncresult.html language=enus -->
## TOPIC 00577: EndReadMultiSamplePower(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-endreadmultisamplepower__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-endreadmultisamplepower__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadMultiSamplePower(int, AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic AIPowerMeasurement[] EndReadMultiSamplePower(IAsyncResult asyncResult)RemarksIf you call EndReadMultiSamplePow

### EndReadMultiSamplePower(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadMultiSamplePower(int, AsyncCallback, object)](nationalinstruments-daqmx-analogsinglechannelreader-beginreadmultisamplepower__int-asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIPowerMeasurement](nationalinstruments-daqmx-aipowermeasurement.html)[] EndReadMultiSamplePower(IAsyncResult asyncResult)

#### Remarks

If you call EndReadMultiSamplePower(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadMultiSamplePower(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadMultiSamplePower(int, AsyncCallback, object). |

#### Returns

A 1D array of power samples from the task. Each element in the array corresponds to a sample from the channel.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadMultiSamplePower(int, AsyncCallback, object) . |
| OutOfMemoryException | There is not enough memory to carry out this operation. |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-endreadsinglesample__iasyncresult.html language=enus -->
## TOPIC 00578: EndReadSingleSample(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-endreadsinglesample__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-endreadsinglesample__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadSingleSample(AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic double EndReadSingleSample(IAsyncResult asyncResult)RemarksIf you call EndReadSingleSample(IAsyncResult) before the asy

### EndReadSingleSample(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadSingleSample(AsyncCallback, object)](nationalinstruments-daqmx-analogsinglechannelreader-beginreadsinglesample__asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double EndReadSingleSample(IAsyncResult asyncResult)

#### Remarks

If you call EndReadSingleSample(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSample(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSample(AsyncCallback, object). |

#### Returns

A single floating-point sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadSingleSample(AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-endreadsinglesamplepower__iasyncresult.html language=enus -->
## TOPIC 00579: EndReadSingleSamplePower(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-endreadsinglesamplepower__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-endreadsinglesamplepower__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadSingleSamplePower(AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic AIPowerMeasurement EndReadSingleSamplePower(IAsyncResult asyncResult)RemarksIf you call EndReadSingleSamplePower(I

### EndReadSingleSamplePower(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadSingleSamplePower(AsyncCallback, object)](nationalinstruments-daqmx-analogsinglechannelreader-beginreadsinglesamplepower__asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIPowerMeasurement](nationalinstruments-daqmx-aipowermeasurement.html) EndReadSingleSamplePower(IAsyncResult asyncResult)

#### Remarks

If you call EndReadSingleSamplePower(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSamplePower(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSamplePower(AsyncCallback, object). |

#### Returns

A single power sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadSingleSamplePower(AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-endreadwaveform__iasyncresult.html language=enus -->
## TOPIC 00580: EndReadWaveform(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-endreadwaveform__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-endreadwaveform__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadWaveform(int, AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogWaveform< double > EndReadWaveform(IAsyncResult asyncResult)RemarksIf you call EndReadWaveform(IAsyncResult) bef

### EndReadWaveform(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadWaveform(int, AsyncCallback, object)](nationalinstruments-daqmx-analogsinglechannelreader-beginreadwaveform__int-asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public AnalogWaveform< double > EndReadWaveform(IAsyncResult asyncResult)

#### Remarks

If you call EndReadWaveform(IAsyncResult) before the asynchronous read is complete, EndReadWaveform(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadWaveform(int, AsyncCallback, object). |

#### Returns

An AnalogWaveformTData containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadWaveform(int, AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-memoryoptimizedreadmultisample__int-ref-out.html language=enus -->
## TOPIC 00581: MemoryOptimizedReadMultiSample(int, ref double[], out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-memoryoptimizedreadmultisample__int-ref-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-memoryoptimizedreadmultisample__int-ref-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more floating-point samples from a single AIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] MemoryOptimizedReadMultiSample(int numberOfSamples, ref double[] data, out int actualNumberOfSamplesRead)RemarksIf the data buffer is large enough to hold the number

### MemoryOptimizedReadMultiSample(int, ref double[], out int)

Reads one or more floating-point samples from a single [AIChannel](nationalinstruments-daqmx-aichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] MemoryOptimizedReadMultiSample(int numberOfSamples, ref double[] data, out int actualNumberOfSamplesRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref double[] | An initialized 1D array of floating-point samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-memoryoptimizedreadmultisample__int-ref-reallocationpolicy-out.html language=enus -->
## TOPIC 00582: MemoryOptimizedReadMultiSample(int, ref double[], ReallocationPolicy, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-memoryoptimizedreadmultisample__int-ref-reallocationpolicy-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-memoryoptimizedreadmultisample__int-ref-reallocationpolicy-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more floating-point samples from a single AIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] MemoryOptimizedReadMultiSample(int numberOfSamples, ref double[] data, ReallocationPolicy policy, out int actualNumberOfSamplesRead)RemarksIf the data buffer is large

### MemoryOptimizedReadMultiSample(int, ref double[], ReallocationPolicy, out int)

Reads one or more floating-point samples from a single [AIChannel](nationalinstruments-daqmx-aichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] MemoryOptimizedReadMultiSample(int numberOfSamples, ref double[] data, ReallocationPolicy policy, out int actualNumberOfSamplesRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref double[] | An initialized 1D array of floating-point samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-memoryoptimizedreadmultisamplepower__int-ref-out.html language=enus -->
## TOPIC 00583: MemoryOptimizedReadMultiSamplePower(int, ref AIPowerMeasurement[], out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-memoryoptimizedreadmultisamplepower__int-ref-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-memoryoptimizedreadmultisamplepower__int-ref-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more power samples from a single AIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic AIPowerMeasurement[] MemoryOptimizedReadMultiSamplePower(int numberOfSamples, ref AIPowerMeasurement[] data, out int actualNumberOfSamplesRead)RemarksIf the data buffer is large enough

### MemoryOptimizedReadMultiSamplePower(int, ref AIPowerMeasurement[], out int)

Reads one or more power samples from a single [AIChannel](nationalinstruments-daqmx-aichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIPowerMeasurement](nationalinstruments-daqmx-aipowermeasurement.html)[] MemoryOptimizedReadMultiSamplePower(int numberOfSamples, ref AIPowerMeasurement[] data, out int actualNumberOfSamplesRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref AIPowerMeasurement[] | An initialized 1D array of power samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-memoryoptimizedreadmultisamplepower__int-ref-reallocationpolicy-out.html language=enus -->
## TOPIC 00584: MemoryOptimizedReadMultiSamplePower(int, ref AIPowerMeasurement[], ReallocationPolicy, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-memoryoptimizedreadmultisamplepower__int-ref-reallocationpolicy-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-memoryoptimizedreadmultisamplepower__int-ref-reallocationpolicy-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more power samples from a single AIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic AIPowerMeasurement[] MemoryOptimizedReadMultiSamplePower(int numberOfSamples, ref AIPowerMeasurement[] data, ReallocationPolicy policy, out int actualNumberOfSamplesRead)RemarksIf the

### MemoryOptimizedReadMultiSamplePower(int, ref AIPowerMeasurement[], ReallocationPolicy, out int)

Reads one or more power samples from a single [AIChannel](nationalinstruments-daqmx-aichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIPowerMeasurement](nationalinstruments-daqmx-aipowermeasurement.html)[] MemoryOptimizedReadMultiSamplePower(int numberOfSamples, ref AIPowerMeasurement[] data, ReallocationPolicy policy, out int actualNumberOfSamplesRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref AIPowerMeasurement[] | An initialized 1D array of power samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-memoryoptimizedreadwaveform__int-analogwaveform_double..html language=enus -->
## TOPIC 00585: MemoryOptimizedReadWaveform(int, AnalogWaveform< double >)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-memoryoptimizedreadwaveform__int-analogwaveform_double..html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-memoryoptimizedreadwaveform__int-analogwaveform_double..html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more analog waveform samples from a single AIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogWaveform< double > MemoryOptimizedReadWaveform(int numberOfSamples, AnalogWaveform< double > data)RemarksIf the data buffer is large enough to hold the number of sample

### MemoryOptimizedReadWaveform(int, AnalogWaveform< double >)

Reads one or more analog waveform samples from a single [AIChannel](nationalinstruments-daqmx-aichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public AnalogWaveform< double > MemoryOptimizedReadWaveform(int numberOfSamples, AnalogWaveform< double > data)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing AnalogWaveformTData objects and their corresponding memory to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](nationalinstruments-daqmx-daqstream-waveformattributemode.html) property of the [DaqStream](nationalinstruments-daqmx-daqstream.html) you are reading from.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | AnalogWaveform< double > | An initialized AnalogWaveformTData that contains the read data. |

#### Returns

An AnalogWaveformTData containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-memoryoptimizedreadwaveform__int-analogwaveform_double_-reallocationpolicy.html language=enus -->
## TOPIC 00586: MemoryOptimizedReadWaveform(int, AnalogWaveform< double >, ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-memoryoptimizedreadwaveform__int-analogwaveform_double_-reallocationpolicy.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-memoryoptimizedreadwaveform__int-analogwaveform_double_-reallocationpolicy.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more analog waveform samples from a singleAIChannelin a task. SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogWaveform< double > MemoryOptimizedReadWaveform(int numberOfSamples, AnalogWaveform< double > data, ReallocationPolicy policy)RemarksIf the data buffer is large enough to

### MemoryOptimizedReadWaveform(int, AnalogWaveform< double >, ReallocationPolicy)

Reads one or more analog waveform samples from a single[AIChannel](nationalinstruments-daqmx-aichannel.html)in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public AnalogWaveform< double > MemoryOptimizedReadWaveform(int numberOfSamples, AnalogWaveform< double > data, ReallocationPolicy policy)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing AnalogWaveformTData objects and their corresponding memory to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](nationalinstruments-daqmx-daqstream-waveformattributemode.html) property of the [DaqStream](nationalinstruments-daqmx-daqstream.html) you are reading from.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | AnalogWaveform< double > | An initialized AnalogWaveformTData that contains the read data. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |

#### Returns

An AnalogWaveformTData containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-memoryoptimizedreadwaveform__timespan-analogwaveform_double..html language=enus -->
## TOPIC 00587: MemoryOptimizedReadWaveform(TimeSpan, AnalogWaveform< double >)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-memoryoptimizedreadwaveform__timespan-analogwaveform_double..html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-memoryoptimizedreadwaveform__timespan-analogwaveform_double..html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a memory-optimized read of one or more analog waveform samples from a single AIChannel object in a task for a specified duration . SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogWaveform< double > MemoryOptimizedReadWaveform(TimeSpan duration, AnalogWaveform< double > data)RemarksIf

### MemoryOptimizedReadWaveform(TimeSpan, AnalogWaveform< double >)

Performs a memory-optimized read of one or more analog waveform samples from a single [AIChannel](nationalinstruments-daqmx-aichannel.html) object in a task for a specified *duration* .

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public AnalogWaveform< double > MemoryOptimizedReadWaveform(TimeSpan duration, AnalogWaveform< double > data)

#### Remarks

If the *data*  waveform is large enough to hold the number of samples requested, this overload attempts to reuse the existing AnalogWaveformTData objects' memory to store acquired data. This results in more efficient memory allocation when performing subsequent reads with a continuous analog input task, if each subsequent read acquires the same or fewer number of samples.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units when creating channels using the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](nationalinstruments-daqmx-daqstream-waveformattributemode.html) property of the [DaqStream](nationalinstruments-daqmx-daqstream.html) being read.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the [Stream](nationalinstruments-daqmx-task-stream.html) object used for the reads or writes.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| duration | TimeSpan | The duration of time to read the waveform. The duration specified must be long enough to read at least one sample at the configured SampleClockRate. |
| data | AnalogWaveform< double > | An initialized AnalogWaveformTData that contains the read data. If data is not large enough to hold all samples read, a new AnalogWaveformTData is allocated to hold the data. |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If the duration provided was less than Zero. |
| NationalInstruments.DAQmx.DaqException | If data is null or is uninitialized. The NI-DAQmx driver returned an error. |

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-memoryoptimizedreadwaveform__timespan-analogwaveform_double_-reallocationpolicy.html language=enus -->
## TOPIC 00588: MemoryOptimizedReadWaveform(TimeSpan, AnalogWaveform< double >, ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-memoryoptimizedreadwaveform__timespan-analogwaveform_double_-reallocationpolicy.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-memoryoptimizedreadwaveform__timespan-analogwaveform_double_-reallocationpolicy.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a memory-optimized read of one or more analog waveform samples from a single AIChannel object in a task for a specified duration . SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogWaveform< double > MemoryOptimizedReadWaveform(TimeSpan duration, AnalogWaveform< double > data, Realloca

### MemoryOptimizedReadWaveform(TimeSpan, AnalogWaveform< double >, ReallocationPolicy)

Performs a memory-optimized read of one or more analog waveform samples from a single [AIChannel](nationalinstruments-daqmx-aichannel.html) object in a task for a specified *duration* .

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public AnalogWaveform< double > MemoryOptimizedReadWaveform(TimeSpan duration, AnalogWaveform< double > data, ReallocationPolicy policy)

#### Remarks

If the *data*  waveform is large enough to hold the number of samples requested, this overload attempts to reuse the existing AnalogWaveformTData objects' memory to store acquired data. This results in more efficient memory allocation when performing subsequent reads with a continuous analog input task, if each subsequent read acquires the same or fewer number of samples.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units when creating channels using the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](nationalinstruments-daqmx-daqstream-waveformattributemode.html) property of the [DaqStream](nationalinstruments-daqmx-daqstream.html) being read.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the [Stream](nationalinstruments-daqmx-task-stream.html) object used for the reads or writes.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| duration | TimeSpan | The duration of time to read the waveform. The duration specified must be long enough to read at least one sample at the configured SampleClockRate. |
| data | AnalogWaveform< double > | An initialized AnalogWaveformTData that contains the read data. If data is not large enough to hold all samples read, a new AnalogWaveformTData may be allocated to hold the data depending on the specified policy . |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If the duration provided was less than Zero. If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| NationalInstruments.DAQmx.DaqException | If data is null or is uninitialized. The NI-DAQmx driver returned an error. |

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-readmultisample__int.html language=enus -->
## TOPIC 00589: ReadMultiSample(int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-readmultisample__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-readmultisample__int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more floating-point samples from a single AIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] ReadMultiSample(int numberOfSamples)RemarksNI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. Y

### ReadMultiSample(int)

Reads one or more floating-point samples from a single [AIChannel](nationalinstruments-daqmx-aichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] ReadMultiSample(int numberOfSamples)

#### Remarks

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |

#### Returns

A 1D array of floating-point samples from the task. Each element in the array corresponds to a sample from the channel.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-readmultisamplepower__int.html language=enus -->
## TOPIC 00590: ReadMultiSamplePower(int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-readmultisamplepower__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-readmultisamplepower__int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more power samples from a single AIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic AIPowerMeasurement[] ReadMultiSamplePower(int numberOfSamples)RemarksNI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the ch

### ReadMultiSamplePower(int)

Reads one or more power samples from a single [AIChannel](nationalinstruments-daqmx-aichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIPowerMeasurement](nationalinstruments-daqmx-aipowermeasurement.html)[] ReadMultiSamplePower(int numberOfSamples)

#### Remarks

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |

#### Returns

A 1D array of power samples from the task. Each element in the array corresponds to a sample from the channel.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-readsinglesample.html language=enus -->
## TOPIC 00591: ReadSingleSample()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-readsinglesample.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-readsinglesample.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a single floating-point sample from a single AIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic double ReadSingleSample()RemarksNI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units w

### ReadSingleSample()

Reads a single floating-point sample from a single [AIChannel](nationalinstruments-daqmx-aichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double ReadSingleSample()

#### Remarks

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Returns

A single floating-point sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-readsinglesamplepower.html language=enus -->
## TOPIC 00592: ReadSingleSamplePower()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-readsinglesamplepower.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-readsinglesamplepower.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a single power sample from a single AIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic AIPowerMeasurement ReadSingleSamplePower()RemarksNI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these

### ReadSingleSamplePower()

Reads a single power sample from a single [AIChannel](nationalinstruments-daqmx-aichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIPowerMeasurement](nationalinstruments-daqmx-aipowermeasurement.html) ReadSingleSamplePower()

#### Remarks

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Returns

A single power sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-readwaveform__int.html language=enus -->
## TOPIC 00593: ReadWaveform(int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-readwaveform__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-readwaveform__int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more analog waveform samples from a single AIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogWaveform< double > ReadWaveform(int numberOfSamples)RemarksNI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to

### ReadWaveform(int)

Reads one or more analog waveform samples from a single [AIChannel](nationalinstruments-daqmx-aichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public AnalogWaveform< double > ReadWaveform(int numberOfSamples)

#### Remarks

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](nationalinstruments-daqmx-daqstream-waveformattributemode.html) property of the [DaqStream](nationalinstruments-daqmx-daqstream.html) you are reading from.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |

#### Returns

An AnalogWaveformTData containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-readwaveform__timespan.html language=enus -->
## TOPIC 00594: ReadWaveform(TimeSpan)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-readwaveform__timespan.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-readwaveform__timespan.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more analog waveform samples from a single AIChannel object in a task for a specified duration . SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogWaveform< double > ReadWaveform(TimeSpan duration)RemarksNI-DAQmx scales the read data to the units of the measurement, including any c

### ReadWaveform(TimeSpan)

Reads one or more analog waveform samples from a single [AIChannel](nationalinstruments-daqmx-aichannel.html) object in a task for a specified *duration* .

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public AnalogWaveform< double > ReadWaveform(TimeSpan duration)

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

An AnalogWaveformTData containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If the duration provided was less than Zero. |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-synchronizecallbacks.html language=enus -->
## TOPIC 00595: SynchronizeCallbacks

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-synchronizecallbacks.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-synchronizecallbacks.html
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

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-synchronizingobject.html language=enus -->
## TOPIC 00596: SynchronizingObject

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-synchronizingobject.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-synchronizingobject.html
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

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader-tostring.html language=enus -->
## TOPIC 00597: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader-tostring.html
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

AnalogSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelreader.html language=enus -->
## TOPIC 00598: AnalogSingleChannelReader Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelreader.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelreader.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains methods for reading samples from the analog input channel in a task. Derives fromMarshalByRefObjectISynchronizeCallbacksISupportSynchronizationContextSyntaxNamespace: NationalInstruments.DAQmxpublic class AnalogSingleChannelReader : MarshalByRefObject, ISynchronizeCallbacks, ISupportSynchro

### AnalogSingleChannelReader Class

Contains methods for reading samples from the analog input channel in a task.

#### Derives from

- MarshalByRefObject
- ISynchronizeCallbacks
- ISupportSynchronizationContext

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class AnalogSingleChannelReader : MarshalByRefObject, ISynchronizeCallbacks, ISupportSynchronizationContext

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| AnalogSingleChannelReader(DaqStream) | Creates a new instance of the AnalogSingleChannelReader class to read from the specified DaqStream. |

#### Properties

| Name | Description |
| --- | --- |
| SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |
| SynchronizingObject | Obsolete: Use SynchronizeCallbacks to specify that the object marshals callbacks across threads appropriately. Will warn if usedGets or sets the object that marshals event-handler and callback calls. |

#### Methods

| Name | Description |
| --- | --- |
| BeginMemoryOptimizedReadMultiSample(int, AsyncCallback, object, double[], ReallocationPolicy) | Begins an asynchronous read of one or more floating-point samples from a single AIChannel in a task. |
| BeginMemoryOptimizedReadMultiSample(int, AsyncCallback, object, double[]) | Begins an asynchronous read of one or more floating-point samples from a single AIChannel in a task. |
| BeginMemoryOptimizedReadMultiSamplePower(int, AsyncCallback, object, AIPowerMeasurement[], ReallocationPolicy) | Begins an asynchronous read of one or more power samples from a single AIChannel in a task. |
| BeginMemoryOptimizedReadMultiSamplePower(int, AsyncCallback, object, AIPowerMeasurement[]) | Begins an asynchronous read of one or more power samples from a single AIChannel in a task. |
| BeginMemoryOptimizedReadWaveform(TimeSpan, AsyncCallback, object, AnalogWaveform< double >) | Begins an asynchronous, memory-optimized read of one or more analog waveform samples from a single AIChannel object in a task for a specified duration . |
| BeginMemoryOptimizedReadWaveform(int, AsyncCallback, object, AnalogWaveform< double >, ReallocationPolicy) | Begins an asynchronous read of one or more analog waveform samples from a single AIChannel in a task. |
| BeginMemoryOptimizedReadWaveform(TimeSpan, AsyncCallback, object, AnalogWaveform< double >, ReallocationPolicy) | Begins an asynchronous, memory-optimized read of one or more analog waveform samples from a single AIChannel object in a task for a specified duration . |
| BeginMemoryOptimizedReadWaveform(int, AsyncCallback, object, AnalogWaveform< double >) | Begins an asynchronous read of one or more analog waveform samples from a single AIChannel in a task. |
| BeginReadMultiSample(int, AsyncCallback, object) | Begins an asynchronous read of one or more floating-point samples from a single AIChannel in a task. |
| BeginReadMultiSamplePower(int, AsyncCallback, object) | Begins an asynchronous read of one or more power samples from a single AIChannel in a task. |
| BeginReadSingleSample(AsyncCallback, object) | Begins an asynchronous read of a single floating-point sample from a single AIChannel in a task. |
| BeginReadSingleSamplePower(AsyncCallback, object) | Begins an asynchronous read of a single power sample from a single AIChannel in a task. |
| BeginReadWaveform(TimeSpan, AsyncCallback, object) | Begins an asynchronous read of one or more analog waveform samples from a single AIChannel object in a task for a specified duration . |
| BeginReadWaveform(int, AsyncCallback, object) | Begins an asynchronous read of one or more analog waveform samples from a single AIChannel in a task. |
| EndMemoryOptimizedReadMultiSample(IAsyncResult, out int) | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSample(int, AsyncCallback, object, double[]) and retrieves the read samples. |
| EndMemoryOptimizedReadMultiSamplePower(IAsyncResult, out int) | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePower(int, AsyncCallback, object, AIPowerMeasurement[]) and retrieves the read samples. |
| EndMemoryOptimizedReadWaveform(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadWaveform(int, AsyncCallback, object, AnalogWaveform<double>) and retrieves the read samples. |
| EndReadMultiSample(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadMultiSample(int, AsyncCallback, object) and retrieves the read samples. |
| EndReadMultiSamplePower(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadMultiSamplePower(int, AsyncCallback, object) and retrieves the read samples. |
| EndReadSingleSample(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadSingleSample(AsyncCallback, object) and retrieves the read samples. |
| EndReadSingleSamplePower(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadSingleSamplePower(AsyncCallback, object) and retrieves the read samples. |
| EndReadWaveform(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadWaveform(int, AsyncCallback, object) and retrieves the read samples. |
| MemoryOptimizedReadMultiSample(int, ref double[], out int) | Reads one or more floating-point samples from a single AIChannel in a task. |
| MemoryOptimizedReadMultiSample(int, ref double[], ReallocationPolicy, out int) | Reads one or more floating-point samples from a single AIChannel in a task. |
| MemoryOptimizedReadMultiSamplePower(int, ref AIPowerMeasurement[], ReallocationPolicy, out int) | Reads one or more power samples from a single AIChannel in a task. |
| MemoryOptimizedReadMultiSamplePower(int, ref AIPowerMeasurement[], out int) | Reads one or more power samples from a single AIChannel in a task. |
| MemoryOptimizedReadWaveform(int, AnalogWaveform< double >, ReallocationPolicy) | Reads one or more analog waveform samples from a singleAIChannelin a task. |
| MemoryOptimizedReadWaveform(TimeSpan, AnalogWaveform< double >, ReallocationPolicy) | Performs a memory-optimized read of one or more analog waveform samples from a single AIChannel object in a task for a specified duration . |
| MemoryOptimizedReadWaveform(int, AnalogWaveform< double >) | Reads one or more analog waveform samples from a single AIChannel in a task. |
| MemoryOptimizedReadWaveform(TimeSpan, AnalogWaveform< double >) | Performs a memory-optimized read of one or more analog waveform samples from a single AIChannel object in a task for a specified duration . |
| ReadMultiSample(int) | Reads one or more floating-point samples from a single AIChannel in a task. |
| ReadMultiSamplePower(int) | Reads one or more power samples from a single AIChannel in a task. |
| ReadSingleSample() | Reads a single floating-point sample from a single AIChannel in a task. |
| ReadSingleSamplePower() | Reads a single power sample from a single AIChannel in a task. |
| ReadWaveform(int) | Reads one or more analog waveform samples from a single AIChannel in a task. |
| ReadWaveform(TimeSpan) | Reads one or more analog waveform samples from a single AIChannel object in a task for a specified duration . |
| ToString() | Returns a string representation of the object. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelwriter-analogsinglechannelwriter__daqstream.html language=enus -->
## TOPIC 00599: AnalogSingleChannelWriter(DaqStream)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelwriter-analogsinglechannelwriter__daqstream.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelwriter-analogsinglechannelwriter__daqstream.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of the AnalogSingleChannelWriter class to write to the specified DaqStream. SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogSingleChannelWriter(DaqStream stream)RemarksEach Task object contains a Stream property that serves as the connection point for writers to provide

### AnalogSingleChannelWriter(DaqStream)

Creates a new instance of the [AnalogSingleChannelWriter](nationalinstruments-daqmx-analogsinglechannelwriter.html) class to write to the specified [DaqStream](nationalinstruments-daqmx-daqstream.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public AnalogSingleChannelWriter(DaqStream stream)

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

AnalogSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelwriter-beginwritemultisample__bool-double_arr1-asynccallback-object.html language=enus -->
## TOPIC 00600: BeginWriteMultiSample(bool, double[], AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelwriter-beginwritemultisample__bool-double_arr1-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelwriter-beginwritemultisample__bool-double_arr1-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of one or more floating-point samples to a single AOChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteMultiSample([MarshalAs(UnmanagedType.U1)] bool autoStart, double[] data, AsyncCallback callback, object state)RemarksPass the re

### BeginWriteMultiSample(bool, double[], AsyncCallback, object)

Begins an asynchronous write of one or more floating-point samples to a single [AOChannel](nationalinstruments-daqmx-aochannel.html) in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteMultiSample([MarshalAs(UnmanagedType.U1)] bool autoStart, double[] data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-analogsinglechannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

NI-DAQmx scales the generated data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | double[] | A 1D array of samples to write to the task. Each element of the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelwriter-beginwritesinglesample__bool-double-asynccallback-object.html language=enus -->
## TOPIC 00601: BeginWriteSingleSample(bool, double, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelwriter-beginwritesinglesample__bool-double-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelwriter-beginwritesinglesample__bool-double-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of a floating-point sample to a single AOChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteSingleSample([MarshalAs(UnmanagedType.U1)] bool autoStart, double data, AsyncCallback callback, object state)RemarksPass the returned IAsyn

### BeginWriteSingleSample(bool, double, AsyncCallback, object)

Begins an asynchronous write of a floating-point sample to a single [AOChannel](nationalinstruments-daqmx-aochannel.html) in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteSingleSample([MarshalAs(UnmanagedType.U1)] bool autoStart, double data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-analogsinglechannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

NI-DAQmx scales the generated data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | double | A sample to write to the task. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelwriter-beginwritewaveform_tdata___bool-analogwaveform_tdata_-asynccallback-object.html language=enus -->
## TOPIC 00602: BeginWriteWaveform< TData >(bool, AnalogWaveform< TData >, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelwriter-beginwritewaveform_tdata___bool-analogwaveform_tdata_-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelwriter-beginwritewaveform_tdata___bool-analogwaveform_tdata_-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more analog waveform samples to a single AOChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteWaveform< TData >([MarshalAs(UnmanagedType.U1)] bool autoStart, AnalogWaveform< TData > data, AsyncCallback callback, object state)RemarksIf the task us

### BeginWriteWaveform< TData >(bool, AnalogWaveform< TData >, AsyncCallback, object)

Writes one or more analog waveform samples to a single [AOChannel](nationalinstruments-daqmx-aochannel.html) in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteWaveform< TData >([MarshalAs(UnmanagedType.U1)] bool autoStart, AnalogWaveform< TData > data, AsyncCallback callback, object state)

#### Remarks

If the task uses on-demand timing, the **BeginWriteWaveform** method returns only after the device generates all samples. If the task uses any timing type other than on-demand, **BeginWriteWaveform** returns immediately and does not wait for the device to generate all samples. Your application must call the [WaitUntilDone](nationalinstruments-daqmx-task-waituntildone__int.html) method to wait until the device has generated all samples.

Digital waveform writes are not affected by the WaveformTiming.SampleInterval or WaveformTiming.StartTime properties on AnalogWaveformTData. To configure timing for analog waveform writes, use the [ConfigureSampleClock(string, double, SampleClockActiveEdge, SampleQuantityMode, int)](nationalinstruments-daqmx-timing-configuresampleclock__string-double-sampleclockactiveedge-samplequantitymode-int.html) method.

Refer to [Asynchronous Reads and Writes](https://#) in the *NI Measurement Studio Help*and Generics in the .NET Framework in the *.NET Framework Developer's Guide* for additional information.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If you set autoStart to true, the BeginWriteWaveform method automatically calls Start if you do not explicitly call Start. You cannot set this parameter to true if you have installed events on the task. |
| data | AnalogWaveform< TData > | An AnalogWaveformTData to write to the task. The order of the lines in the analog waveform corresponds to the order in which you add the lines to the channel. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

Parent topic:

AnalogSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelwriter-endwrite__iasyncresult.html language=enus -->
## TOPIC 00603: EndWrite(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelwriter-endwrite__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelwriter-endwrite__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous write initiated with BeginWriteMultiSample(bool, double[], AsyncCallback, object) or BeginWriteSingleSample(bool, double, AsyncCallback, object). SyntaxNamespace: NationalInstruments.DAQmxpublic void EndWrite(IAsyncResult asyncResult)RemarksIf you call EndWrite(IAs

### EndWrite(IAsyncResult)

Handles the end of an asynchronous write initiated with [BeginWriteMultiSample(bool, double[], AsyncCallback, object)](nationalinstruments-daqmx-analogsinglechannelwriter-beginwritemultisample__bool-double_arr1-asynccallback-object.html) or [BeginWriteSingleSample(bool, double, AsyncCallback, object)](nationalinstruments-daqmx-analogsinglechannelwriter-beginwritesinglesample__bool-double-asynccallback-object.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void EndWrite(IAsyncResult asyncResult)

#### Remarks

If you call EndWrite(IAsyncResult) before the asynchronous write represented by the provided IAsyncResult is complete, EndWrite(IAsyncResult) waits for the write to complete before returning. For a write to a buffered task, the write is considered complete when all of the written samples have been transferred to the task buffer. Use [IsDone](nationalinstruments-daqmx-task-isdone.html) or [WaitUntilDone(int)](nationalinstruments-daqmx-task-waituntildone__int.html) on the [Task](nationalinstruments-daqmx-task.html) object to determine if a task has generated all of the data it was configured to generate.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginWriteMultiSample(bool, double[], AsyncCallback, object) or BeginWriteSingleSample(bool, double, AsyncCallback, object). |

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginWriteMultiSample(bool, double[], AsyncCallback, object) or BeginWriteSingleSample(bool, double, AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| IndexOutOfRangeException | The data provided to BeginWriteMultiSample(bool, double[], AsyncCallback, object) has a non-zero lower bound. |

Parent topic:

AnalogSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelwriter-synchronizecallbacks.html language=enus -->
## TOPIC 00604: SynchronizeCallbacks

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelwriter-synchronizecallbacks.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelwriter-synchronizecallbacks.html
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

AnalogSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelwriter-synchronizingobject.html language=enus -->
## TOPIC 00605: SynchronizingObject

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelwriter-synchronizingobject.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelwriter-synchronizingobject.html
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

AnalogSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelwriter-tostring.html language=enus -->
## TOPIC 00606: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelwriter-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelwriter-tostring.html
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

AnalogSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelwriter-writemultisample__bool-double_arr1.html language=enus -->
## TOPIC 00607: WriteMultiSample(bool, double[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelwriter-writemultisample__bool-double_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelwriter-writemultisample__bool-double_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more floating-point samples to a single AOChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteMultiSample([MarshalAs(UnmanagedType.U1)] bool autoStart, double[] data)RemarksNI-DAQmx scales the generated data to the units of the measurement, including any custo

### WriteMultiSample(bool, double[])

Writes one or more floating-point samples to a single [AOChannel](nationalinstruments-daqmx-aochannel.html) in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteMultiSample([MarshalAs(UnmanagedType.U1)] bool autoStart, double[] data)

#### Remarks

NI-DAQmx scales the generated data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

If the task uses on-demand timing, this method returns only after the device generates all samples. If the task uses any timing type other than on-demand, this method returns immediately and does not wait for the device to generate all samples. Your application must call the [WaitUntilDone](nationalinstruments-daqmx-task-waituntildone__int.html) method to block until the device has generated all samples.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | double[] | A 1D array of samples to write to the task. Each element of the array corresponds to a sample to write to the channel. The order of the channels in the array corresponds to the order in which you add the channels to the task. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

Parent topic:

AnalogSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelwriter-writesinglesample__bool-double.html language=enus -->
## TOPIC 00608: WriteSingleSample(bool, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelwriter-writesinglesample__bool-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelwriter-writesinglesample__bool-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a floating-point sample to a single AOChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteSingleSample([MarshalAs(UnmanagedType.U1)] bool autoStart, double data)RemarksNI-DAQmx scales the generated data to the units of the measurement, including any custom scaling yo

### WriteSingleSample(bool, double)

Writes a floating-point sample to a single [AOChannel](nationalinstruments-daqmx-aochannel.html) in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteSingleSample([MarshalAs(UnmanagedType.U1)] bool autoStart, double data)

#### Remarks

NI-DAQmx scales the generated data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | double | A sample to write to the task. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelwriter-writewaveform_tdata___bool-analogwaveform_tdata..html language=enus -->
## TOPIC 00609: WriteWaveform< TData >(bool, AnalogWaveform< TData >)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelwriter-writewaveform_tdata___bool-analogwaveform_tdata..html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelwriter-writewaveform_tdata___bool-analogwaveform_tdata..html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more analog waveform samples to a single AOChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteWaveform< TData >([MarshalAs(UnmanagedType.U1)] bool autoStart, AnalogWaveform< TData > data)RemarksIf the task uses on-demand timing, the WriteWaveform method retur

### WriteWaveform< TData >(bool, AnalogWaveform< TData >)

Writes one or more analog waveform samples to a single [AOChannel](nationalinstruments-daqmx-aochannel.html) in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteWaveform< TData >([MarshalAs(UnmanagedType.U1)] bool autoStart, AnalogWaveform< TData > data)

#### Remarks

If the task uses on-demand timing, the **WriteWaveform** method returns only after the device generates all samples. If the task uses any timing type other than on-demand, **WriteWaveform** returns immediately and does not wait for the device to generate all samples. Your application must call the [WaitUntilDone](nationalinstruments-daqmx-task-waituntildone__int.html) method to wait until the device has generated all samples.

Digital waveform writes are not affected by the WaveformTiming.SampleInterval or WaveformTiming.StartTime properties on AnalogWaveformTData. To configure timing for analog waveform writes, use the [ConfigureSampleClock(string, double, SampleClockActiveEdge, SampleQuantityMode, int)](nationalinstruments-daqmx-timing-configuresampleclock__string-double-sampleclockactiveedge-samplequantitymode-int.html) method.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If you set autoStart to true, the WriteWaveform method automatically calls Start if you do not explicitly call Start. You cannot set this parameter to true if you have installed events on the task. |
| data | AnalogWaveform< TData > | An AnalogWaveformTData to write to the task. The order of the lines in the analog waveform corresponds to the order in which you add the lines to the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

Parent topic:

AnalogSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogsinglechannelwriter.html language=enus -->
## TOPIC 00610: AnalogSingleChannelWriter Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogsinglechannelwriter.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogsinglechannelwriter.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains methods for writing samples to the analog output channel in a task. Derives fromMarshalByRefObjectISynchronizeCallbacksISupportSynchronizationContextSyntaxNamespace: NationalInstruments.DAQmxpublic class AnalogSingleChannelWriter : MarshalByRefObject, ISynchronizeCallbacks, ISupportSynchron

### AnalogSingleChannelWriter Class

Contains methods for writing samples to the analog output channel in a task.

#### Derives from

- MarshalByRefObject
- ISynchronizeCallbacks
- ISupportSynchronizationContext

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class AnalogSingleChannelWriter : MarshalByRefObject, ISynchronizeCallbacks, ISupportSynchronizationContext

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| AnalogSingleChannelWriter(DaqStream) | Creates a new instance of the AnalogSingleChannelWriter class to write to the specified DaqStream. |

#### Properties

| Name | Description |
| --- | --- |
| SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |
| SynchronizingObject | Obsolete: Use SynchronizeCallbacks to specify that the object marshals callbacks across threads appropriately. Will warn if usedGets or sets the object that marshals event-handler and callback calls. |

#### Methods

| Name | Description |
| --- | --- |
| BeginWriteMultiSample(bool, double[], AsyncCallback, object) | Begins an asynchronous write of one or more floating-point samples to a single AOChannel in a task. |
| BeginWriteSingleSample(bool, double, AsyncCallback, object) | Begins an asynchronous write of a floating-point sample to a single AOChannel in a task. |
| BeginWriteWaveform< TData >(bool, AnalogWaveform< TData >, AsyncCallback, object) | Writes one or more analog waveform samples to a single AOChannel in a task. |
| EndWrite(IAsyncResult) | Handles the end of an asynchronous write initiated with BeginWriteMultiSample(bool, double[], AsyncCallback, object) or BeginWriteSingleSample(bool, double, AsyncCallback, object). |
| ToString() | Returns a string representation of the object. |
| WriteMultiSample(bool, double[]) | Writes one or more floating-point samples to a single AOChannel in a task. |
| WriteSingleSample(bool, double) | Writes a floating-point sample to a single AOChannel in a task. |
| WriteWaveform< TData >(bool, AnalogWaveform< TData >) | Writes one or more analog waveform samples to a single AOChannel in a task. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogunscaledreader-analogunscaledreader__daqstream.html language=enus -->
## TOPIC 00611: AnalogUnscaledReader(DaqStream)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogunscaledreader-analogunscaledreader__daqstream.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogunscaledreader-analogunscaledreader__daqstream.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of the AnalogUnscaledReader class to read from the specified DaqStream. SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogUnscaledReader(DaqStream stream)RemarksEach Task object contains a Stream property that serves as the connection point for readers to access the sampl

### AnalogUnscaledReader(DaqStream)

Creates a new instance of the [AnalogUnscaledReader](nationalinstruments-daqmx-analogunscaledreader.html) class to read from the specified [DaqStream](nationalinstruments-daqmx-daqstream.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public AnalogUnscaledReader(DaqStream stream)

#### Remarks

Each [Task](nationalinstruments-daqmx-task.html) object contains a [Stream](nationalinstruments-daqmx-task-stream.html) property that serves as the connection point for readers to access the samples generated by that task.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| stream | DaqStream | The DaqStream to read. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogUnscaledReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogunscaledreader-beginreadint16__int-asynccallback-object.html language=enus -->
## TOPIC 00612: BeginReadInt16(int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogunscaledreader-beginreadint16__int-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogunscaledreader-beginreadint16__int-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more unscaled 16-bit integer samples from one or more AIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadInt16(int samplesPerChannel, AsyncCallback callback, object state)RemarksTo get the read data or any excepti

### BeginReadInt16(int, AsyncCallback, object)

Begins an asynchronous read of one or more [unscaled](/csh?context=nidaqmx_mxcncpts_unscaleddata) 16-bit integer samples from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadInt16(int samplesPerChannel, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadInt16(int, AsyncCallback, object), call [EndReadInt16(IAsyncResult)](nationalinstruments-daqmx-analogunscaledreader-endreadint16__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogUnscaledReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogunscaledreader-beginreadint16power__int-asynccallback-object.html language=enus -->
## TOPIC 00613: BeginReadInt16Power(int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogunscaledreader-beginreadint16power__int-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogunscaledreader-beginreadint16power__int-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more unscaled 16-bit integer samples from one or more AIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadInt16Power(int samplesPerChannel, AsyncCallback callback, object state)RemarksTo get the read data or any ex

### BeginReadInt16Power(int, AsyncCallback, object)

Begins an asynchronous read of one or more [unscaled](/csh?context=nidaqmx_mxcncpts_unscaleddata) 16-bit integer samples from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadInt16Power(int samplesPerChannel, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadInt16Power(int, AsyncCallback, object), call [EndReadInt16Power(IAsyncResult)](nationalinstruments-daqmx-analogunscaledreader-endreadint16power__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogUnscaledReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogunscaledreader-beginreadint32__int-asynccallback-object.html language=enus -->
## TOPIC 00614: BeginReadInt32(int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogunscaledreader-beginreadint32__int-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogunscaledreader-beginreadint32__int-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more unscaled 32-bit integer samples from one or more AIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadInt32(int samplesPerChannel, AsyncCallback callback, object state)RemarksTo get the read data or any excepti

### BeginReadInt32(int, AsyncCallback, object)

Begins an asynchronous read of one or more [unscaled](/csh?context=nidaqmx_mxcncpts_unscaleddata) 32-bit integer samples from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadInt32(int samplesPerChannel, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadInt32(int, AsyncCallback, object), call [EndReadInt32(IAsyncResult)](nationalinstruments-daqmx-analogunscaledreader-endreadint32__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogUnscaledReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogunscaledreader-beginreaduint16__int-asynccallback-object.html language=enus -->
## TOPIC 00615: BeginReadUInt16(int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogunscaledreader-beginreaduint16__int-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogunscaledreader-beginreaduint16__int-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more unscaled 16-bit unsigned integer samples from one or more AIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadUInt16(int samplesPerChannel, AsyncCallback callback, object state)RemarksTo get the read data or a

### BeginReadUInt16(int, AsyncCallback, object)

Begins an asynchronous read of one or more [unscaled](/csh?context=nidaqmx_mxcncpts_unscaleddata) 16-bit unsigned integer samples from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadUInt16(int samplesPerChannel, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadUInt16(int, AsyncCallback, object), call [EndReadUInt16(IAsyncResult)](nationalinstruments-daqmx-analogunscaledreader-endreaduint16__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogUnscaledReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogunscaledreader-beginreaduint32__int-asynccallback-object.html language=enus -->
## TOPIC 00616: BeginReadUInt32(int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogunscaledreader-beginreaduint32__int-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogunscaledreader-beginreaduint32__int-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more unscaled 32-bit unsigned integer samples from one or more AIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadUInt32(int samplesPerChannel, AsyncCallback callback, object state)RemarksTo get the read data or a

### BeginReadUInt32(int, AsyncCallback, object)

Begins an asynchronous read of one or more [unscaled](/csh?context=nidaqmx_mxcncpts_unscaleddata) 32-bit unsigned integer samples from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadUInt32(int samplesPerChannel, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadUInt32(int, AsyncCallback, object), call [EndReadUInt32(IAsyncResult)](nationalinstruments-daqmx-analogunscaledreader-endreaduint32__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogUnscaledReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogunscaledreader-endreadint16__iasyncresult.html language=enus -->
## TOPIC 00617: EndReadInt16(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogunscaledreader-endreadint16__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogunscaledreader-endreadint16__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadInt16(int, AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic short[,] EndReadInt16(IAsyncResult asyncResult)RemarksIf you call EndReadInt16(IAsyncResult) before the asynchronous read

### EndReadInt16(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadInt16(int, AsyncCallback, object)](nationalinstruments-daqmx-analogunscaledreader-beginreadint16__int-asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public short[,] EndReadInt16(IAsyncResult asyncResult)

#### Remarks

If you call EndReadInt16(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadInt16(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadInt16(int, AsyncCallback, object). |

#### Returns

A 2D array of unscaled 16-bit integer samples from the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from that channel. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadInt16(int, AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogUnscaledReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogunscaledreader-endreadint16power__iasyncresult.html language=enus -->
## TOPIC 00618: EndReadInt16Power(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogunscaledreader-endreadint16power__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogunscaledreader-endreadint16power__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadInt16Power(int, AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic AIUnscaledPowerMeasurement[,] EndReadInt16Power(IAsyncResult asyncResult)RemarksIf you call EndReadInt16Power(IAsync

### EndReadInt16Power(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadInt16Power(int, AsyncCallback, object)](nationalinstruments-daqmx-analogunscaledreader-beginreadint16power__int-asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIUnscaledPowerMeasurement](nationalinstruments-daqmx-aiunscaledpowermeasurement.html)[,] EndReadInt16Power(IAsyncResult asyncResult)

#### Remarks

If you call EndReadInt16Power(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadInt16Power(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadInt16Power(int, AsyncCallback, object). |

#### Returns

A 2D array of unscaled 16-bit integer samples from the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from that channel. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadInt16Power(int, AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogUnscaledReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogunscaledreader-endreadint32__iasyncresult.html language=enus -->
## TOPIC 00619: EndReadInt32(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogunscaledreader-endreadint32__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogunscaledreader-endreadint32__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadInt32(int, AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic int[,] EndReadInt32(IAsyncResult asyncResult)RemarksIf you call EndReadInt32(IAsyncResult) before the asynchronous read r

### EndReadInt32(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadInt32(int, AsyncCallback, object)](nationalinstruments-daqmx-analogunscaledreader-beginreadint32__int-asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int[,] EndReadInt32(IAsyncResult asyncResult)

#### Remarks

If you call EndReadInt32(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadInt32(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadInt32(int, AsyncCallback, object). |

#### Returns

A 2D array of unscaled 32-bit integer samples from the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from that channel. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadInt32(int, AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogUnscaledReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogunscaledreader-endreaduint16__iasyncresult.html language=enus -->
## TOPIC 00620: EndReadUInt16(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogunscaledreader-endreaduint16__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogunscaledreader-endreaduint16__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadUInt16(int, AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic ushort[,] EndReadUInt16(IAsyncResult asyncResult)RemarksIf you call EndReadUInt16(IAsyncResult) before the asynchronous

### EndReadUInt16(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadUInt16(int, AsyncCallback, object)](nationalinstruments-daqmx-analogunscaledreader-beginreaduint16__int-asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public ushort[,] EndReadUInt16(IAsyncResult asyncResult)

#### Remarks

If you call EndReadUInt16(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadUInt16(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadUInt16(int, AsyncCallback, object). |

#### Returns

A 2D array of unscaled 16-bit unsigned integer samples from the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from that channel. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadUInt16(int, AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogUnscaledReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogunscaledreader-endreaduint32__iasyncresult.html language=enus -->
## TOPIC 00621: EndReadUInt32(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogunscaledreader-endreaduint32__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogunscaledreader-endreaduint32__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadUInt32(int, AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic uint[,] EndReadUInt32(IAsyncResult asyncResult)RemarksIf you call EndReadUInt32(IAsyncResult) before the asynchronous re

### EndReadUInt32(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadUInt32(int, AsyncCallback, object)](nationalinstruments-daqmx-analogunscaledreader-beginreaduint32__int-asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public uint[,] EndReadUInt32(IAsyncResult asyncResult)

#### Remarks

If you call EndReadUInt32(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadUInt32(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadUInt32(int, AsyncCallback, object). |

#### Returns

A 2D array of unscaled 32-bit unsigned integer samples from the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from that channel. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadUInt32(int, AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogUnscaledReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogunscaledreader-readint16__int.html language=enus -->
## TOPIC 00622: ReadInt16(int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogunscaledreader-readint16__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogunscaledreader-readint16__int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more unscaled 16-bit integer samples from one or more AIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic short[,] ReadInt16(int samplesPerChannel)RemarksNI-DAQmx read and write methods time out after the amount of time specified by the Timeout property on the

### ReadInt16(int)

Reads one or more [unscaled](/csh?context=nidaqmx_mxcncpts_unscaleddata) 16-bit integer samples from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public short[,] ReadInt16(int samplesPerChannel)

#### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |

#### Returns

A 2D array of unscaled 16-bit integer samples from the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from that channel. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogUnscaledReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogunscaledreader-readint16power__int.html language=enus -->
## TOPIC 00623: ReadInt16Power(int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogunscaledreader-readint16power__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogunscaledreader-readint16power__int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more unscaled 16-bit integer samples from one or more AIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic AIUnscaledPowerMeasurement[,] ReadInt16Power(int samplesPerChannel)RemarksNI-DAQmx read and write methods time out after the amount of time specified by th

### ReadInt16Power(int)

Reads one or more [unscaled](/csh?context=nidaqmx_mxcncpts_unscaleddata) 16-bit integer samples from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIUnscaledPowerMeasurement](nationalinstruments-daqmx-aiunscaledpowermeasurement.html)[,] ReadInt16Power(int samplesPerChannel)

#### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |

#### Returns

A 2D array of unscaled 16-bit integer samples from the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from that channel. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogUnscaledReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogunscaledreader-readint32__int.html language=enus -->
## TOPIC 00624: ReadInt32(int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogunscaledreader-readint32__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogunscaledreader-readint32__int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more unscaled 32-bit integer samples from one or more AIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic int[,] ReadInt32(int samplesPerChannel)RemarksNI-DAQmx read and write methods time out after the amount of time specified by the Timeout property on the ta

### ReadInt32(int)

Reads one or more [unscaled](/csh?context=nidaqmx_mxcncpts_unscaleddata) 32-bit integer samples from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int[,] ReadInt32(int samplesPerChannel)

#### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |

#### Returns

A 2D array of unscaled 32-bit integer samples from the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from that channel. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogUnscaledReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogunscaledreader-readuint16__int.html language=enus -->
## TOPIC 00625: ReadUInt16(int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogunscaledreader-readuint16__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogunscaledreader-readuint16__int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more unscaled 16-bit unsigned integer samples from one or more AIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic ushort[,] ReadUInt16(int samplesPerChannel)RemarksNI-DAQmx read and write methods time out after the amount of time specified by the Timeout prope

### ReadUInt16(int)

Reads one or more [unscaled](/csh?context=nidaqmx_mxcncpts_unscaleddata) 16-bit unsigned integer samples from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public ushort[,] ReadUInt16(int samplesPerChannel)

#### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |

#### Returns

A 2D array of unscaled 16-bit unsigned integer samples from the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from that channel. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogUnscaledReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogunscaledreader-readuint32__int.html language=enus -->
## TOPIC 00626: ReadUInt32(int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogunscaledreader-readuint32__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogunscaledreader-readuint32__int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more unscaled 32-bit unsigned integer samples from one or more AIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic uint[,] ReadUInt32(int samplesPerChannel)RemarksNI-DAQmx read and write methods time out after the amount of time specified by the Timeout propert

### ReadUInt32(int)

Reads one or more [unscaled](/csh?context=nidaqmx_mxcncpts_unscaleddata) 32-bit unsigned integer samples from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public uint[,] ReadUInt32(int samplesPerChannel)

#### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |

#### Returns

A 2D array of unscaled 32-bit unsigned integer samples from the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from that channel. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

AnalogUnscaledReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogunscaledreader-synchronizecallbacks.html language=enus -->
## TOPIC 00627: SynchronizeCallbacks

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogunscaledreader-synchronizecallbacks.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogunscaledreader-synchronizecallbacks.html
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

In some cases, callbacks and event handlers are executed in a different thread than the rest of the program. Therefore, you must take special care when accessing objects that have thread affinity, such as UI controls, from these callbacks and event handlers. For more information, refer to

Events, Callbacks, and Thread Safety in Measurement Studio .NET Class Libraries.

Reading and Writing with NI-DAQmx Streams

Parent topic:

AnalogUnscaledReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogunscaledreader-synchronizingobject.html language=enus -->
## TOPIC 00628: SynchronizingObject

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogunscaledreader-synchronizingobject.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogunscaledreader-synchronizingobject.html
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

For more information, refer to

Events, Callbacks, and Thread Safety in Measurement Studio .NET Class Libraries.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogUnscaledReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogunscaledreader-tostring.html language=enus -->
## TOPIC 00629: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogunscaledreader-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogunscaledreader-tostring.html
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

AnalogUnscaledReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogunscaledreader.html language=enus -->
## TOPIC 00630: AnalogUnscaledReader Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogunscaledreader.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogunscaledreader.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains methods that read unscaled samples from a task. Derives fromMarshalByRefObjectISynchronizeCallbacksISupportSynchronizationContextSyntaxNamespace: NationalInstruments.DAQmxpublic class AnalogUnscaledReader : MarshalByRefObject, ISynchronizeCallbacks, ISupportSynchronizationContextRemarksExam

### AnalogUnscaledReader Class

Contains methods that read unscaled samples from a task.

#### Derives from

- MarshalByRefObject
- ISynchronizeCallbacks
- ISupportSynchronizationContext

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class AnalogUnscaledReader : MarshalByRefObject, ISynchronizeCallbacks, ISupportSynchronizationContext

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| AnalogUnscaledReader(DaqStream) | Creates a new instance of the AnalogUnscaledReader class to read from the specified DaqStream. |

#### Properties

| Name | Description |
| --- | --- |
| SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |
| SynchronizingObject | Obsolete: Use SynchronizeCallbacks to specify that the object marshals callbacks across threads appropriately. Will warn if usedGets or sets the object that marshals event-handler and callback calls. |

#### Methods

| Name | Description |
| --- | --- |
| BeginReadInt16(int, AsyncCallback, object) | Begins an asynchronous read of one or more unscaled 16-bit integer samples from one or more AIChannel objects in a task. |
| BeginReadInt16Power(int, AsyncCallback, object) | Begins an asynchronous read of one or more unscaled 16-bit integer samples from one or more AIChannel objects in a task. |
| BeginReadInt32(int, AsyncCallback, object) | Begins an asynchronous read of one or more unscaled 32-bit integer samples from one or more AIChannel objects in a task. |
| BeginReadUInt16(int, AsyncCallback, object) | Begins an asynchronous read of one or more unscaled 16-bit unsigned integer samples from one or more AIChannel objects in a task. |
| BeginReadUInt32(int, AsyncCallback, object) | Begins an asynchronous read of one or more unscaled 32-bit unsigned integer samples from one or more AIChannel objects in a task. |
| EndReadInt16(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadInt16(int, AsyncCallback, object) and retrieves the read samples. |
| EndReadInt16Power(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadInt16Power(int, AsyncCallback, object) and retrieves the read samples. |
| EndReadInt32(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadInt32(int, AsyncCallback, object) and retrieves the read samples. |
| EndReadUInt16(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadUInt16(int, AsyncCallback, object) and retrieves the read samples. |
| EndReadUInt32(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadUInt32(int, AsyncCallback, object) and retrieves the read samples. |
| ReadInt16(int) | Reads one or more unscaled 16-bit integer samples from one or more AIChannel objects in a task. |
| ReadInt16Power(int) | Reads one or more unscaled 16-bit integer samples from one or more AIChannel objects in a task. |
| ReadInt32(int) | Reads one or more unscaled 32-bit integer samples from one or more AIChannel objects in a task. |
| ReadUInt16(int) | Reads one or more unscaled 16-bit unsigned integer samples from one or more AIChannel objects in a task. |
| ReadUInt32(int) | Reads one or more unscaled 32-bit unsigned integer samples from one or more AIChannel objects in a task. |
| ToString() | Returns a string representation of the object. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogunscaledwriter-analogunscaledwriter__daqstream.html language=enus -->
## TOPIC 00631: AnalogUnscaledWriter(DaqStream)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogunscaledwriter-analogunscaledwriter__daqstream.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogunscaledwriter-analogunscaledwriter__daqstream.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of the AnalogUnscaledWriter class to write to the specified DaqStream. SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogUnscaledWriter(DaqStream stream)RemarksEach Task object contains a Stream property that serves as the connection point for writers to provide samples t

### AnalogUnscaledWriter(DaqStream)

Creates a new instance of the [AnalogUnscaledWriter](nationalinstruments-daqmx-analogunscaledwriter.html) class to write to the specified [DaqStream](nationalinstruments-daqmx-daqstream.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public AnalogUnscaledWriter(DaqStream stream)

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

AnalogUnscaledWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogunscaledwriter-beginwrite__bool-int_arr2-asynccallback-object.html language=enus -->
## TOPIC 00632: BeginWrite(bool, int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogunscaledwriter-beginwrite__bool-int_arr2-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogunscaledwriter-beginwrite__bool-int_arr2-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of one or more unscaled 32-bit integer samples to one or more AOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWrite([MarshalAs(UnmanagedType.U1)] bool autoStart, int[,] data, AsyncCallback callback, object state)RemarksPass

### BeginWrite(bool, int, AsyncCallback, object)

Begins an asynchronous write of one or more [unscaled](/csh?context=nidaqmx_mxcncpts_unscaleddata) 32-bit integer samples to one or more [AOChannel](nationalinstruments-daqmx-aochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWrite([MarshalAs(UnmanagedType.U1)] bool autoStart, int[,] data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-analogunscaledwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. |
| data | int | A 2D array of samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array corresponds to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogUnscaledWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogunscaledwriter-beginwrite__bool-short_arr2-asynccallback-object.html language=enus -->
## TOPIC 00633: BeginWrite(bool, short, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogunscaledwriter-beginwrite__bool-short_arr2-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogunscaledwriter-beginwrite__bool-short_arr2-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of one or more unscaled 16-bit integer samples to one or more AOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWrite([MarshalAs(UnmanagedType.U1)] bool autoStart, short[,] data, AsyncCallback callback, object state)RemarksPa

### BeginWrite(bool, short, AsyncCallback, object)

Begins an asynchronous write of one or more [unscaled](/csh?context=nidaqmx_mxcncpts_unscaleddata) 16-bit integer samples to one or more [AOChannel](nationalinstruments-daqmx-aochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWrite([MarshalAs(UnmanagedType.U1)] bool autoStart, short[,] data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-analogunscaledwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. |
| data | short | A 2D array of samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array corresponds to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogUnscaledWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogunscaledwriter-beginwrite__bool-uint_arr2-asynccallback-object.html language=enus -->
## TOPIC 00634: BeginWrite(bool, uint, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogunscaledwriter-beginwrite__bool-uint_arr2-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogunscaledwriter-beginwrite__bool-uint_arr2-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of one or more unscaled 32-bit unsigned integer samples to one or more AOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWrite([MarshalAs(UnmanagedType.U1)] bool autoStart, uint[,] data, AsyncCallback callback, object state)R

### BeginWrite(bool, uint, AsyncCallback, object)

Begins an asynchronous write of one or more [unscaled](/csh?context=nidaqmx_mxcncpts_unscaleddata) 32-bit unsigned integer samples to one or more [AOChannel](nationalinstruments-daqmx-aochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWrite([MarshalAs(UnmanagedType.U1)] bool autoStart, uint[,] data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-analogunscaledwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. |
| data | uint | A 2D array of samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array corresponds to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogUnscaledWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogunscaledwriter-beginwrite__bool-ushort_arr2-asynccallback-object.html language=enus -->
## TOPIC 00635: BeginWrite(bool, ushort, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogunscaledwriter-beginwrite__bool-ushort_arr2-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogunscaledwriter-beginwrite__bool-ushort_arr2-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of one or more unscaled 16-bit unsigned integer samples to one or more AOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWrite([MarshalAs(UnmanagedType.U1)] bool autoStart, ushort[,] data, AsyncCallback callback, object state

### BeginWrite(bool, ushort, AsyncCallback, object)

Begins an asynchronous write of one or more [unscaled](/csh?context=nidaqmx_mxcncpts_unscaleddata) 16-bit unsigned integer samples to one or more [AOChannel](nationalinstruments-daqmx-aochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWrite([MarshalAs(UnmanagedType.U1)] bool autoStart, ushort[,] data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-analogunscaledwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. |
| data | ushort | A 2D array of samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array corresponds to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogUnscaledWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogunscaledwriter-endwrite__iasyncresult.html language=enus -->
## TOPIC 00636: EndWrite(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogunscaledwriter-endwrite__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogunscaledwriter-endwrite__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous write initiated with BeginWrite(bool, ushort[, ], AsyncCallback, object). SyntaxNamespace: NationalInstruments.DAQmxpublic void EndWrite(IAsyncResult asyncResult)RemarksIf you call EndWrite(IAsyncResult) before the asynchronous write represented by the provided IAs

### EndWrite(IAsyncResult)

Handles the end of an asynchronous write initiated with [BeginWrite(bool, ushort[, ], AsyncCallback, object)](nationalinstruments-daqmx-analogunscaledwriter-beginwrite__bool-ushort_arr2-asynccallback-object.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void EndWrite(IAsyncResult asyncResult)

#### Remarks

If you call EndWrite(IAsyncResult) before the asynchronous write represented by the provided IAsyncResult is complete, EndWrite(IAsyncResult) waits for the write to complete before returning. For a write to a buffered task, the write is considered complete when all of the written samples have been transferred to the task buffer. Use [IsDone](nationalinstruments-daqmx-task-isdone.html) or [WaitUntilDone(TimeSpan)](nationalinstruments-daqmx-task-waituntildone__timespan.html) on the [Task](nationalinstruments-daqmx-task.html) object to determine if a task has generated all of the data it was configured to generate.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginWrite(bool, ushort[, ], AsyncCallback, object). |

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginWrite(bool, ushort[, ], AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| IndexOutOfRangeException | The data provided to BeginWrite(bool, ushort[, ], AsyncCallback, object) had a non-zero lower bound. |

Parent topic:

AnalogUnscaledWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogunscaledwriter-synchronizecallbacks.html language=enus -->
## TOPIC 00637: SynchronizeCallbacks

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogunscaledwriter-synchronizecallbacks.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogunscaledwriter-synchronizecallbacks.html
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

AnalogUnscaledWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogunscaledwriter-synchronizingobject.html language=enus -->
## TOPIC 00638: SynchronizingObject

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogunscaledwriter-synchronizingobject.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogunscaledwriter-synchronizingobject.html
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

AnalogUnscaledWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogunscaledwriter-tostring.html language=enus -->
## TOPIC 00639: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogunscaledwriter-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogunscaledwriter-tostring.html
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

AnalogUnscaledWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogunscaledwriter-write__bool-int_arr2.html language=enus -->
## TOPIC 00640: Write(bool, int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogunscaledwriter-write__bool-int_arr2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogunscaledwriter-write__bool-int_arr2.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more unscaled 32-bit integer samples to one or more AOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic void Write([MarshalAs(UnmanagedType.U1)] bool autoStart, int[,] data)RemarksIf the task uses on-demand timing, this method returns only after the device gen

### Write(bool, int)

Writes one or more [unscaled](/csh?context=nidaqmx_mxcncpts_unscaleddata) 32-bit integer samples to one or more [AOChannel](nationalinstruments-daqmx-aochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Write([MarshalAs(UnmanagedType.U1)] bool autoStart, int[,] data)

#### Remarks

If the task uses on-demand timing, this method returns only after the device generates all samples. If the task uses any timing type other than on-demand, this method returns immediately and does not wait for the device to generate all samples. Your application must call the [WaitUntilDone](nationalinstruments-daqmx-task-waituntildone__int.html) method to block until the device has generated all samples.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. |
| data | int | A 2D array of samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array corresponds to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

Parent topic:

AnalogUnscaledWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogunscaledwriter-write__bool-short_arr2.html language=enus -->
## TOPIC 00641: Write(bool, short)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogunscaledwriter-write__bool-short_arr2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogunscaledwriter-write__bool-short_arr2.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more unscaled 16-bit integer samples to one or more AOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic void Write([MarshalAs(UnmanagedType.U1)] bool autoStart, short[,] data)RemarksIf the task uses on-demand timing, this method returns only after the device g

### Write(bool, short)

Writes one or more [unscaled](/csh?context=nidaqmx_mxcncpts_unscaleddata) 16-bit integer samples to one or more [AOChannel](nationalinstruments-daqmx-aochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Write([MarshalAs(UnmanagedType.U1)] bool autoStart, short[,] data)

#### Remarks

If the task uses on-demand timing, this method returns only after the device generates all samples. If the task uses any timing type other than on-demand, this method returns immediately and does not wait for the device to generate all samples. Your application must call the [WaitUntilDone](nationalinstruments-daqmx-task-waituntildone__int.html) method to block until the device has generated all samples.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. |
| data | short | A 2D array of samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array corresponds to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

Parent topic:

AnalogUnscaledWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogunscaledwriter-write__bool-uint_arr2.html language=enus -->
## TOPIC 00642: Write(bool, uint)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogunscaledwriter-write__bool-uint_arr2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogunscaledwriter-write__bool-uint_arr2.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more unscaled 32-bit unsigned integer samples to one or more AOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic void Write([MarshalAs(UnmanagedType.U1)] bool autoStart, uint[,] data)RemarksIf the task uses on-demand timing, this method returns only after the

### Write(bool, uint)

Writes one or more [unscaled](/csh?context=nidaqmx_mxcncpts_unscaleddata) 32-bit unsigned integer samples to one or more [AOChannel](nationalinstruments-daqmx-aochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Write([MarshalAs(UnmanagedType.U1)] bool autoStart, uint[,] data)

#### Remarks

If the task uses on-demand timing, this method returns only after the device generates all samples. If the task uses any timing type other than on-demand, this method returns immediately and does not wait for the device to generate all samples. Your application must call the [WaitUntilDone](nationalinstruments-daqmx-task-waituntildone__int.html) method to block until the device has generated all samples.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. |
| data | uint | A 2D array of samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array corresponds to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

Parent topic:

AnalogUnscaledWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogunscaledwriter-write__bool-ushort_arr2.html language=enus -->
## TOPIC 00643: Write(bool, ushort)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogunscaledwriter-write__bool-ushort_arr2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogunscaledwriter-write__bool-ushort_arr2.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more unscaled 16-bit unsigned integer samples to one or more AOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic void Write([MarshalAs(UnmanagedType.U1)] bool autoStart, ushort[,] data)RemarksIf the task uses on-demand timing, this method returns only after th

### Write(bool, ushort)

Writes one or more [unscaled](/csh?context=nidaqmx_mxcncpts_unscaleddata) 16-bit unsigned integer samples to one or more [AOChannel](nationalinstruments-daqmx-aochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Write([MarshalAs(UnmanagedType.U1)] bool autoStart, ushort[,] data)

#### Remarks

If the task uses on-demand timing, this method returns only after the device generates all samples. If the task uses any timing type other than on-demand, this method returns immediately and does not wait for the device to generate all samples. Your application must call the [WaitUntilDone](nationalinstruments-daqmx-task-waituntildone__int.html) method to block until the device has generated all samples.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. |
| data | ushort | A 2D array of samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array corresponds to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

Parent topic:

AnalogUnscaledWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogunscaledwriter.html language=enus -->
## TOPIC 00644: AnalogUnscaledWriter Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogunscaledwriter.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogunscaledwriter.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains methods that write unscaled samples to a task. Derives fromMarshalByRefObjectISynchronizeCallbacksISupportSynchronizationContextSyntaxNamespace: NationalInstruments.DAQmxpublic class AnalogUnscaledWriter : MarshalByRefObject, ISynchronizeCallbacks, ISupportSynchronizationContextRemarksExamp

### AnalogUnscaledWriter Class

Contains methods that write unscaled samples to a task.

#### Derives from

- MarshalByRefObject
- ISynchronizeCallbacks
- ISupportSynchronizationContext

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class AnalogUnscaledWriter : MarshalByRefObject, ISynchronizeCallbacks, ISupportSynchronizationContext

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| AnalogUnscaledWriter(DaqStream) | Creates a new instance of the AnalogUnscaledWriter class to write to the specified DaqStream. |

#### Properties

| Name | Description |
| --- | --- |
| SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |
| SynchronizingObject | Obsolete: Use SynchronizeCallbacks to specify that the object marshals callbacks across threads appropriately. Will warn if usedGets or sets the object that marshals event-handler and callback calls. |

#### Methods

| Name | Description |
| --- | --- |
| BeginWrite(bool, short, AsyncCallback, object) | Begins an asynchronous write of one or more unscaled 16-bit integer samples to one or more AOChannel objects in a task. |
| BeginWrite(bool, ushort, AsyncCallback, object) | Begins an asynchronous write of one or more unscaled 16-bit unsigned integer samples to one or more AOChannel objects in a task. |
| BeginWrite(bool, int, AsyncCallback, object) | Begins an asynchronous write of one or more unscaled 32-bit integer samples to one or more AOChannel objects in a task. |
| BeginWrite(bool, uint, AsyncCallback, object) | Begins an asynchronous write of one or more unscaled 32-bit unsigned integer samples to one or more AOChannel objects in a task. |
| EndWrite(IAsyncResult) | Handles the end of an asynchronous write initiated with BeginWrite(bool, ushort[, ], AsyncCallback, object). |
| ToString() | Returns a string representation of the object. |
| Write(bool, int) | Writes one or more unscaled 32-bit integer samples to one or more AOChannel objects in a task. |
| Write(bool, ushort) | Writes one or more unscaled 16-bit unsigned integer samples to one or more AOChannel objects in a task. |
| Write(bool, uint) | Writes one or more unscaled 32-bit unsigned integer samples to one or more AOChannel objects in a task. |
| Write(bool, short) | Writes one or more unscaled 16-bit integer samples to one or more AOChannel objects in a task. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowpausetrigger-condition.html language=enus -->
## TOPIC 00645: Condition

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowpausetrigger-condition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowpausetrigger-condition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the task pauses while the trigger signal is inside or outside the window you specify with WindowBottom and WindowTop. SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogWindowPauseTriggerCondition Condition { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExce

### Condition

Specifies whether the task pauses while the trigger signal is inside or outside the window you specify with [WindowBottom](nationalinstruments-daqmx-analogwindowpausetrigger-windowbottom.html) and [WindowTop](nationalinstruments-daqmx-analogwindowpausetrigger-windowtop.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AnalogWindowPauseTriggerCondition](nationalinstruments-daqmx-analogwindowpausetriggercondition.html) Condition { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogWindowPauseTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowpausetrigger-coupling.html language=enus -->
## TOPIC 00646: Coupling

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowpausetrigger-coupling.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowpausetrigger-coupling.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the coupling for the source signal of the terminal if the source is a terminal rather than a virtual channel. SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogWindowPauseTriggerCoupling Coupling { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx

### Coupling

Specifies the coupling for the source signal of the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) if the source is a terminal rather than a [virtual channel](/csh?context=nidaqmx_mxcncpts_chans).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AnalogWindowPauseTriggerCoupling](nationalinstruments-daqmx-analogwindowpausetriggercoupling.html) Coupling { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogWindowPauseTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowpausetrigger-digitalfilterenable.html language=enus -->
## TOPIC 00647: DigitalFilterEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowpausetrigger-digitalfilterenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowpausetrigger-digitalfilterenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay within the trigger window for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that tr

### DigitalFilterEnable

Specifies whether to apply a digital [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay within the trigger window for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the window rapidly.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool DigitalFilterEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogWindowPauseTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowpausetrigger-digitalfilterminimumpulsewidth.html language=enus -->
## TOPIC 00648: DigitalFilterMinimumPulseWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowpausetrigger-digitalfilterminimumpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowpausetrigger-digitalfilterminimumpulsewidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. SyntaxNamespace: NationalInstruments.DAQmxpublic double DigitalFilterMinimumPulseWidth { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterMinimumPulseWidth

Specifies in seconds the minimum pulse width the [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) recognizes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DigitalFilterMinimumPulseWidth { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogWindowPauseTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowpausetrigger-digitalfiltertimebaserate.html language=enus -->
## TOPIC 00649: DigitalFilterTimebaseRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowpausetrigger-digitalfiltertimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowpausetrigger-digitalfiltertimebaserate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double DigitalFilterTimebaseRate { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver r

### DigitalFilterTimebaseRate

Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DigitalFilterTimebaseRate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogWindowPauseTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowpausetrigger-digitalfiltertimebasesource.html language=enus -->
## TOPIC 00650: DigitalFilterTimebaseSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowpausetrigger-digitalfiltertimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowpausetrigger-digitalfiltertimebasesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the timebase of the digital filter. SyntaxNamespace: NationalInstruments.DAQmxpublic string DigitalFilterTimebaseSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterTimebaseSource

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the signal to use as the timebase of the digital filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string DigitalFilterTimebaseSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogWindowPauseTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowpausetrigger-digitalsynchronizationenable.html language=enus -->
## TOPIC 00651: DigitalSynchronizationEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowpausetrigger-digitalsynchronizationenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowpausetrigger-digitalsynchronizationenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic bool DigitalSynchronizationEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returne

### DigitalSynchronizationEnable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool DigitalSynchronizationEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogWindowPauseTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowpausetrigger-source.html language=enus -->
## TOPIC 00652: Source

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowpausetrigger-source.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowpausetrigger-source.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the trigger. SyntaxNamespace: NationalInstruments.DAQmxpublic string Source { get; set; }RemarksFor E Series devices, if you use a channel name, the channel must be the only channel in the tas

### Source

Specifies the name of a [virtual channel](/csh?context=nidaqmx_mxcncpts_chans) or [terminal](/csh?context=nidaqmx_mxcncpts_terminal) where there is an analog signal to use as the source of the trigger.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Source { get; set; }

#### Remarks

For E Series devices, if you use a channel name, the channel must be the only channel in the task. The only terminal you can use for E Series devices is PFI0.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogWindowPauseTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowpausetrigger-tostring.html language=enus -->
## TOPIC 00653: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowpausetrigger-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowpausetrigger-tostring.html
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

AnalogWindowPauseTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowpausetrigger-windowbottom.html language=enus -->
## TOPIC 00654: WindowBottom

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowpausetrigger-windowbottom.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowpausetrigger-windowbottom.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the lower limit of the window. Specify this value in the units of the measurement or generation. SyntaxNamespace: NationalInstruments.DAQmxpublic double WindowBottom { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### WindowBottom

Specifies the lower limit of the window. Specify this value in the units of the measurement or generation.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double WindowBottom { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogWindowPauseTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowpausetrigger-windowtop.html language=enus -->
## TOPIC 00655: WindowTop

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowpausetrigger-windowtop.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowpausetrigger-windowtop.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the upper limit of the window. Specify this value in the units of the measurement or generation. SyntaxNamespace: NationalInstruments.DAQmxpublic double WindowTop { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### WindowTop

Specifies the upper limit of the window. Specify this value in the units of the measurement or generation.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double WindowTop { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogWindowPauseTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowpausetrigger.html language=enus -->
## TOPIC 00656: AnalogWindowPauseTrigger Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowpausetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowpausetrigger.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains properties to configure analog window pause triggers. For more information, refer to PauseTrigger. Derives fromMarshalByRefObjectIFilteredTypeDescriptorSyntaxNamespace: NationalInstruments.DAQmxpublic class AnalogWindowPauseTrigger : MarshalByRefObject, IFilteredTypeDescriptorRemarksExample

### AnalogWindowPauseTrigger Class

Contains properties to configure [analog window](/csh?context=nidaqmx_mxcncpts_algwindowtrig) [pause triggers](/csh?context=nidaqmx_mxcncpts_pausetrigger). For more information, refer to [PauseTrigger](nationalinstruments-daqmx-pausetrigger.html).

#### Derives from

- MarshalByRefObject
- IFilteredTypeDescriptor

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class AnalogWindowPauseTrigger : MarshalByRefObject, IFilteredTypeDescriptor

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Condition | Specifies whether the task pauses while the trigger signal is inside or outside the window you specify with WindowBottom and WindowTop. |
| Coupling | Specifies the coupling for the source signal of the terminal if the source is a terminal rather than a virtual channel. |
| DigitalFilterEnable | Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay within the trigger window for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the window rapidly. |
| DigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
| DigitalFilterTimebaseRate | Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
| DigitalFilterTimebaseSource | Specifies the terminal of the signal to use as the timebase of the digital filter. |
| DigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
| Source | Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the trigger. |
| WindowBottom | Specifies the lower limit of the window. Specify this value in the units of the measurement or generation. |
| WindowTop | Specifies the upper limit of the window. Specify this value in the units of the measurement or generation. |

#### Methods

| Name | Description |
| --- | --- |
| ToString() | Returns a string representation of the object. |

#### See Also

- PauseTrigger
- AnalogWindow

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowpausetriggercondition.html language=enus -->
## TOPIC 00657: AnalogWindowPauseTriggerCondition Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowpausetriggercondition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowpausetriggercondition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the task pauses while the trigger signal is inside or outside the window you specify with WindowBottom and WindowTop. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AnalogWindowPauseTriggerConditionRemarksSpecifies whether the task pauses while the trigger signal is inside o

### AnalogWindowPauseTriggerCondition Enumeration

Specifies whether the task pauses while the trigger signal is inside or outside the window you specify with [WindowBottom](nationalinstruments-daqmx-analogwindowpausetrigger-windowbottom.html) and [WindowTop](nationalinstruments-daqmx-analogwindowpausetrigger-windowtop.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AnalogWindowPauseTriggerCondition

#### Remarks

Specifies whether the task pauses while the trigger signal is inside or outside the window you specify with [WindowBottom](nationalinstruments-daqmx-analogwindowpausetrigger-windowbottom.html) and [WindowTop](nationalinstruments-daqmx-analogwindowpausetrigger-windowtop.html). Use this enumeration to get or set the value of [Condition](nationalinstruments-daqmx-analogwindowpausetrigger-condition.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| InsideWindow | 10199 | Pause the measurement or generation while the trigger is inside the window. |
| OutsideWindow | 10251 | Pause the measurement or generation while the signal is outside the window. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowpausetriggercoupling.html language=enus -->
## TOPIC 00658: AnalogWindowPauseTriggerCoupling Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowpausetriggercoupling.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowpausetriggercoupling.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the coupling for the source signal of the terminal if the source is a terminal rather than a virtual channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AnalogWindowPauseTriggerCouplingRemarksSpecifies the coupling for the source signal of the terminal if the source is a termina

### AnalogWindowPauseTriggerCoupling Enumeration

Specifies the coupling for the source signal of the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) if the source is a terminal rather than a [virtual channel](/csh?context=nidaqmx_mxcncpts_chans).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AnalogWindowPauseTriggerCoupling

#### Remarks

Specifies the coupling for the source signal of the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) if the source is a terminal rather than a [virtual channel](/csh?context=nidaqmx_mxcncpts_chans). Use this enumeration to get or set the value of [Coupling](nationalinstruments-daqmx-analogwindowpausetrigger-coupling.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AC | 10045 | Alternating Current. |
| DC | 10050 | Direct Current. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowreferencetrigger-condition.html language=enus -->
## TOPIC 00659: Condition

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowreferencetrigger-condition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowreferencetrigger-condition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the Reference Trigger occurs when the source signal enters the window or when it leaves the window. Use WindowBottom and WindowTop to specify the window. SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogWindowReferenceTriggerCondition Condition { get; set; }ExceptionsTypeDesc

### Condition

Specifies whether the [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger) occurs when the source signal enters the window or when it leaves the window. Use [WindowBottom](nationalinstruments-daqmx-analogwindowreferencetrigger-windowbottom.html) and [WindowTop](nationalinstruments-daqmx-analogwindowreferencetrigger-windowtop.html) to specify the window.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AnalogWindowReferenceTriggerCondition](nationalinstruments-daqmx-analogwindowreferencetriggercondition.html) Condition { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogWindowReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowreferencetrigger-coupling.html language=enus -->
## TOPIC 00660: Coupling

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowreferencetrigger-coupling.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowreferencetrigger-coupling.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel. SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogWindowReferenceTriggerCoupling Coupling { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQ

### Coupling

Specifies the coupling for the source signal of the trigger if the source is a [terminal](/csh?context=nidaqmx_mxcncpts_terminal) rather than a [virtual channel](/csh?context=nidaqmx_mxcncpts_chans).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AnalogWindowReferenceTriggerCoupling](nationalinstruments-daqmx-analogwindowreferencetriggercoupling.html) Coupling { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogWindowReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowreferencetrigger-digitalfilterenable.html language=enus -->
## TOPIC 00661: DigitalFilterEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowreferencetrigger-digitalfilterenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowreferencetrigger-digitalfilterenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay within the trigger window for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that tr

### DigitalFilterEnable

Specifies whether to apply a digital [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay within the trigger window for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the window rapidly.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool DigitalFilterEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogWindowReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowreferencetrigger-digitalfilterminimumpulsewidth.html language=enus -->
## TOPIC 00662: DigitalFilterMinimumPulseWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowreferencetrigger-digitalfilterminimumpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowreferencetrigger-digitalfilterminimumpulsewidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. SyntaxNamespace: NationalInstruments.DAQmxpublic double DigitalFilterMinimumPulseWidth { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterMinimumPulseWidth

Specifies in seconds the minimum pulse width the [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) recognizes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DigitalFilterMinimumPulseWidth { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogWindowReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowreferencetrigger-digitalfiltertimebaserate.html language=enus -->
## TOPIC 00663: DigitalFilterTimebaseRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowreferencetrigger-digitalfiltertimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowreferencetrigger-digitalfiltertimebaserate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double DigitalFilterTimebaseRate { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver r

### DigitalFilterTimebaseRate

Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DigitalFilterTimebaseRate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogWindowReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowreferencetrigger-digitalfiltertimebasesource.html language=enus -->
## TOPIC 00664: DigitalFilterTimebaseSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowreferencetrigger-digitalfiltertimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowreferencetrigger-digitalfiltertimebasesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the timebase of the digital filter. SyntaxNamespace: NationalInstruments.DAQmxpublic string DigitalFilterTimebaseSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterTimebaseSource

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the signal to use as the timebase of the digital filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string DigitalFilterTimebaseSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogWindowReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowreferencetrigger-digitalsynchronizationenable.html language=enus -->
## TOPIC 00665: DigitalSynchronizationEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowreferencetrigger-digitalsynchronizationenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowreferencetrigger-digitalsynchronizationenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic bool DigitalSynchronizationEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returne

### DigitalSynchronizationEnable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool DigitalSynchronizationEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogWindowReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowreferencetrigger-source.html language=enus -->
## TOPIC 00666: Source

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowreferencetrigger-source.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowreferencetrigger-source.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the Reference Trigger. SyntaxNamespace: NationalInstruments.DAQmxpublic string Source { get; set; }RemarksFor E Series devices, if you use a channel name, the channel must be the only channel

### Source

Specifies the name of a [virtual channel](/csh?context=nidaqmx_mxcncpts_chans) or [terminal](/csh?context=nidaqmx_mxcncpts_terminal) where there is an analog signal to use as the source of the [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Source { get; set; }

#### Remarks

For E Series devices, if you use a channel name, the channel must be the only channel in the task. The only terminal you can use for E Series devices is PFI0.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogWindowReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowreferencetrigger-tostring.html language=enus -->
## TOPIC 00667: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowreferencetrigger-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowreferencetrigger-tostring.html
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

AnalogWindowReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowreferencetrigger-windowbottom.html language=enus -->
## TOPIC 00668: WindowBottom

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowreferencetrigger-windowbottom.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowreferencetrigger-windowbottom.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the lower limit of the window. Specify this value in the units of the measurement. SyntaxNamespace: NationalInstruments.DAQmxpublic double WindowBottom { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### WindowBottom

Specifies the lower limit of the [window](/csh?context=nidaqmx_mxcncpts_algwindowtrig). Specify this value in the units of the measurement.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double WindowBottom { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogWindowReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowreferencetrigger-windowtop.html language=enus -->
## TOPIC 00669: WindowTop

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowreferencetrigger-windowtop.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowreferencetrigger-windowtop.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the upper limit of the window. Specify this value in the units of the measurement. SyntaxNamespace: NationalInstruments.DAQmxpublic double WindowTop { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### WindowTop

Specifies the upper limit of the [window](/csh?context=nidaqmx_mxcncpts_algwindowtrig). Specify this value in the units of the measurement.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double WindowTop { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogWindowReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowreferencetrigger.html language=enus -->
## TOPIC 00670: AnalogWindowReferenceTrigger Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowreferencetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowreferencetrigger.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains properties to configure analog window reference triggers. For more information, refer to ReferenceTrigger. Derives fromMarshalByRefObjectIFilteredTypeDescriptorSyntaxNamespace: NationalInstruments.DAQmxpublic class AnalogWindowReferenceTrigger : MarshalByRefObject, IFilteredTypeDescriptorRe

### AnalogWindowReferenceTrigger Class

Contains properties to configure [analog window](/csh?context=nidaqmx_mxcncpts_algwindowtrig) [reference triggers](/csh?context=nidaqmx_mxcncpts_referencetrigger). For more information, refer to [ReferenceTrigger](nationalinstruments-daqmx-referencetrigger.html).

#### Derives from

- MarshalByRefObject
- IFilteredTypeDescriptor

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class AnalogWindowReferenceTrigger : MarshalByRefObject, IFilteredTypeDescriptor

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Condition | Specifies whether the Reference Trigger occurs when the source signal enters the window or when it leaves the window. Use WindowBottom and WindowTop to specify the window. |
| Coupling | Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel. |
| DigitalFilterEnable | Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay within the trigger window for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the window rapidly. |
| DigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
| DigitalFilterTimebaseRate | Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
| DigitalFilterTimebaseSource | Specifies the terminal of the signal to use as the timebase of the digital filter. |
| DigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
| Source | Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the Reference Trigger. |
| WindowBottom | Specifies the lower limit of the window. Specify this value in the units of the measurement. |
| WindowTop | Specifies the upper limit of the window. Specify this value in the units of the measurement. |

#### Methods

| Name | Description |
| --- | --- |
| ToString() | Returns a string representation of the object. |

#### See Also

- ReferenceTrigger
- AnalogWindow

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowreferencetriggercondition.html language=enus -->
## TOPIC 00671: AnalogWindowReferenceTriggerCondition Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowreferencetriggercondition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowreferencetriggercondition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the Reference Trigger occurs when the source signal enters the window or when it leaves the window. Use WindowBottom and WindowTop to specify the window. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AnalogWindowReferenceTriggerConditionRemarksSpecifies whether the Referenc

### AnalogWindowReferenceTriggerCondition Enumeration

Specifies whether the [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger) occurs when the source signal enters the window or when it leaves the window. Use [WindowBottom](nationalinstruments-daqmx-analogwindowreferencetrigger-windowbottom.html) and [WindowTop](nationalinstruments-daqmx-analogwindowreferencetrigger-windowtop.html) to specify the window.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AnalogWindowReferenceTriggerCondition

#### Remarks

Specifies whether the [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger) occurs when the source signal enters the window or when it leaves the window. Use [WindowBottom](nationalinstruments-daqmx-analogwindowreferencetrigger-windowbottom.html) and [WindowTop](nationalinstruments-daqmx-analogwindowreferencetrigger-windowtop.html) to specify the window. Use this enumeration to get or set the value of [Condition](nationalinstruments-daqmx-analogwindowreferencetrigger-condition.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| EnteringWindow | 10163 | Trigger when the signal enters the window. |
| LeavingWindow | 10208 | Trigger when the signal leaves the window. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowreferencetriggercoupling.html language=enus -->
## TOPIC 00672: AnalogWindowReferenceTriggerCoupling Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowreferencetriggercoupling.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowreferencetriggercoupling.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AnalogWindowReferenceTriggerCouplingRemarksSpecifies the coupling for the source signal of the trigger if the source is a termi

### AnalogWindowReferenceTriggerCoupling Enumeration

Specifies the coupling for the source signal of the trigger if the source is a [terminal](/csh?context=nidaqmx_mxcncpts_terminal) rather than a [virtual channel](/csh?context=nidaqmx_mxcncpts_chans).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AnalogWindowReferenceTriggerCoupling

#### Remarks

Specifies the coupling for the source signal of the trigger if the source is a [terminal](/csh?context=nidaqmx_mxcncpts_terminal) rather than a [virtual channel](/csh?context=nidaqmx_mxcncpts_chans). Use this enumeration to get or set the value of [Coupling](nationalinstruments-daqmx-analogwindowreferencetrigger-coupling.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AC | 10045 | Alternating Current. |
| DC | 10050 | Direct Current. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowstarttrigger-condition.html language=enus -->
## TOPIC 00673: Condition

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowstarttrigger-condition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowstarttrigger-condition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the task starts acquiring or generating samples when the signal enters or leaves the window you specify with WindowBottom and WindowTop. SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogWindowStartTriggerCondition Condition { get; set; }ExceptionsTypeDescriptionNationalInstru

### Condition

Specifies whether the task starts acquiring or generating samples when the signal enters or leaves the window you specify with [WindowBottom](nationalinstruments-daqmx-analogwindowstarttrigger-windowbottom.html) and [WindowTop](nationalinstruments-daqmx-analogwindowstarttrigger-windowtop.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AnalogWindowStartTriggerCondition](nationalinstruments-daqmx-analogwindowstarttriggercondition.html) Condition { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogWindowStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowstarttrigger-coupling.html language=enus -->
## TOPIC 00674: Coupling

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowstarttrigger-coupling.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowstarttrigger-coupling.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel. SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogWindowStartTriggerCoupling Coupling { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx d

### Coupling

Specifies the coupling for the source signal of the trigger if the source is a [terminal](/csh?context=nidaqmx_mxcncpts_terminal) rather than a [virtual channel](/csh?context=nidaqmx_mxcncpts_chans).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AnalogWindowStartTriggerCoupling](nationalinstruments-daqmx-analogwindowstarttriggercoupling.html) Coupling { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogWindowStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowstarttrigger-digitalfilterenable.html language=enus -->
## TOPIC 00675: DigitalFilterEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowstarttrigger-digitalfilterenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowstarttrigger-digitalfilterenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay within the trigger window for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that tr

### DigitalFilterEnable

Specifies whether to apply a digital [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay within the trigger window for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the window rapidly.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool DigitalFilterEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogWindowStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowstarttrigger-digitalfilterminimumpulsewidth.html language=enus -->
## TOPIC 00676: DigitalFilterMinimumPulseWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowstarttrigger-digitalfilterminimumpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowstarttrigger-digitalfilterminimumpulsewidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. SyntaxNamespace: NationalInstruments.DAQmxpublic double DigitalFilterMinimumPulseWidth { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterMinimumPulseWidth

Specifies in seconds the minimum pulse width the [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) recognizes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DigitalFilterMinimumPulseWidth { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogWindowStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowstarttrigger-digitalfiltertimebaserate.html language=enus -->
## TOPIC 00677: DigitalFilterTimebaseRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowstarttrigger-digitalfiltertimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowstarttrigger-digitalfiltertimebaserate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double DigitalFilterTimebaseRate { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver r

### DigitalFilterTimebaseRate

Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DigitalFilterTimebaseRate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogWindowStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowstarttrigger-digitalfiltertimebasesource.html language=enus -->
## TOPIC 00678: DigitalFilterTimebaseSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowstarttrigger-digitalfiltertimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowstarttrigger-digitalfiltertimebasesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the timebase of the digital filter. SyntaxNamespace: NationalInstruments.DAQmxpublic string DigitalFilterTimebaseSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterTimebaseSource

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the signal to use as the timebase of the digital filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string DigitalFilterTimebaseSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogWindowStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowstarttrigger-digitalsynchronizationenable.html language=enus -->
## TOPIC 00679: DigitalSynchronizationEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowstarttrigger-digitalsynchronizationenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowstarttrigger-digitalsynchronizationenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic bool DigitalSynchronizationEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returne

### DigitalSynchronizationEnable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool DigitalSynchronizationEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogWindowStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowstarttrigger-source.html language=enus -->
## TOPIC 00680: Source

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowstarttrigger-source.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowstarttrigger-source.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the Start Trigger. SyntaxNamespace: NationalInstruments.DAQmxpublic string Source { get; set; }RemarksFor E Series devices, if you use a channel name, the channel must be the first one in the

### Source

Specifies the name of a [virtual channel](/csh?context=nidaqmx_mxcncpts_chans) or [terminal](/csh?context=nidaqmx_mxcncpts_terminal) where there is an analog signal to use as the source of the Start Trigger.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Source { get; set; }

#### Remarks

For E Series devices, if you use a channel name, the channel must be the first one in the task. The only terminal you can use for E Series devices is PFI0.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogWindowStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowstarttrigger-tostring.html language=enus -->
## TOPIC 00681: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowstarttrigger-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowstarttrigger-tostring.html
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

AnalogWindowStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowstarttrigger-windowbottom.html language=enus -->
## TOPIC 00682: WindowBottom

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowstarttrigger-windowbottom.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowstarttrigger-windowbottom.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the lower limit of the window. Specify this value in the units of the measurement or generation. SyntaxNamespace: NationalInstruments.DAQmxpublic double WindowBottom { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### WindowBottom

Specifies the lower limit of the [window](/csh?context=nidaqmx_mxcncpts_algwindowtrig). Specify this value in the units of the measurement or generation.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double WindowBottom { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogWindowStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowstarttrigger-windowtop.html language=enus -->
## TOPIC 00683: WindowTop

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowstarttrigger-windowtop.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowstarttrigger-windowtop.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the upper limit of the window. Specify this value in the units of the measurement or generation. SyntaxNamespace: NationalInstruments.DAQmxpublic double WindowTop { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### WindowTop

Specifies the upper limit of the [window](/csh?context=nidaqmx_mxcncpts_algwindowtrig). Specify this value in the units of the measurement or generation.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double WindowTop { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogWindowStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowstarttrigger.html language=enus -->
## TOPIC 00684: AnalogWindowStartTrigger Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowstarttrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowstarttrigger.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains properties to configure analog window start triggers. For more information, refer to StartTrigger. Derives fromMarshalByRefObjectIFilteredTypeDescriptorSyntaxNamespace: NationalInstruments.DAQmxpublic class AnalogWindowStartTrigger : MarshalByRefObject, IFilteredTypeDescriptorRemarksExample

### AnalogWindowStartTrigger Class

Contains properties to configure [analog window](/csh?context=nidaqmx_mxcncpts_algwindowtrig) [start triggers](/csh?context=nidaqmx_mxcncpts_starttrig). For more information, refer to [StartTrigger](nationalinstruments-daqmx-starttrigger.html).

#### Derives from

- MarshalByRefObject
- IFilteredTypeDescriptor

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class AnalogWindowStartTrigger : MarshalByRefObject, IFilteredTypeDescriptor

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Condition | Specifies whether the task starts acquiring or generating samples when the signal enters or leaves the window you specify with WindowBottom and WindowTop. |
| Coupling | Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel. |
| DigitalFilterEnable | Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay within the trigger window for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the window rapidly. |
| DigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
| DigitalFilterTimebaseRate | Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
| DigitalFilterTimebaseSource | Specifies the terminal of the signal to use as the timebase of the digital filter. |
| DigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
| Source | Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the Start Trigger. |
| WindowBottom | Specifies the lower limit of the window. Specify this value in the units of the measurement or generation. |
| WindowTop | Specifies the upper limit of the window. Specify this value in the units of the measurement or generation. |

#### Methods

| Name | Description |
| --- | --- |
| ToString() | Returns a string representation of the object. |

#### See Also

- StartTrigger
- AnalogWindow

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowstarttriggercondition.html language=enus -->
## TOPIC 00685: AnalogWindowStartTriggerCondition Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowstarttriggercondition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowstarttriggercondition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the task starts acquiring or generating samples when the signal enters or leaves the window you specify with WindowBottom and WindowTop. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AnalogWindowStartTriggerConditionRemarksSpecifies whether the task starts acquiring or gene

### AnalogWindowStartTriggerCondition Enumeration

Specifies whether the task starts acquiring or generating samples when the signal enters or leaves the window you specify with [WindowBottom](nationalinstruments-daqmx-analogwindowstarttrigger-windowbottom.html) and [WindowTop](nationalinstruments-daqmx-analogwindowstarttrigger-windowtop.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AnalogWindowStartTriggerCondition

#### Remarks

Specifies whether the task starts acquiring or generating samples when the signal enters or leaves the window you specify with [WindowBottom](nationalinstruments-daqmx-analogwindowstarttrigger-windowbottom.html) and [WindowTop](nationalinstruments-daqmx-analogwindowstarttrigger-windowtop.html). Use this enumeration to get or set the value of [Condition](nationalinstruments-daqmx-analogwindowstarttrigger-condition.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| EnteringWindow | 10163 | Trigger when the signal enters the window. |
| LeavingWindow | 10208 | Trigger when the signal leaves the window. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogwindowstarttriggercoupling.html language=enus -->
## TOPIC 00686: AnalogWindowStartTriggerCoupling Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogwindowstarttriggercoupling.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogwindowstarttriggercoupling.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AnalogWindowStartTriggerCouplingRemarksSpecifies the coupling for the source signal of the trigger if the source is a terminal

### AnalogWindowStartTriggerCoupling Enumeration

Specifies the coupling for the source signal of the trigger if the source is a [terminal](/csh?context=nidaqmx_mxcncpts_terminal) rather than a [virtual channel](/csh?context=nidaqmx_mxcncpts_chans).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AnalogWindowStartTriggerCoupling

#### Remarks

Specifies the coupling for the source signal of the trigger if the source is a [terminal](/csh?context=nidaqmx_mxcncpts_terminal) rather than a [virtual channel](/csh?context=nidaqmx_mxcncpts_chans). Use this enumeration to get or set the value of [Coupling](nationalinstruments-daqmx-analogwindowstarttrigger-coupling.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AC | 10045 | Alternating Current. |
| DC | 10050 | Direct Current. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-commonmodeoffset.html language=enus -->
## TOPIC 00687: CommonModeOffset

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-commonmodeoffset.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-commonmodeoffset.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the common-mode offset of the AO channel. Use the property only when Terminal Configuration is set to Differential. SyntaxNamespace: NationalInstruments.DAQmxpublic double CommonModeOffset { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver retur

### CommonModeOffset

Specifies the common-mode offset of the AO channel. Use the property only when Terminal Configuration is set to Differential.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double CommonModeOffset { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-currentunits.html language=enus -->
## TOPIC 00688: CurrentUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-currentunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-currentunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in what units to generate current on the channel. Write data to the channel in the units you select. SyntaxNamespace: NationalInstruments.DAQmxpublic AOCurrentUnits CurrentUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an erro

### CurrentUnits

Specifies in what units to generate current on the channel. Write data to the channel in the units you select.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AOCurrentUnits](nationalinstruments-daqmx-aocurrentunits.html) CurrentUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-customscalename.html language=enus -->
## TOPIC 00689: CustomScaleName

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-customscalename.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-customscalename.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of a custom scale for the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic string CustomScaleName { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CustomScaleName

Specifies the name of a [custom scale](/csh?context=nidaqmx_mxcncpts_customscales) for the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string CustomScaleName { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-dacallowconnectreferencetoground.html language=enus -->
## TOPIC 00690: DacAllowConnectReferenceToGround

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-dacallowconnectreferencetoground.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-dacallowconnectreferencetoground.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to allow grounding the internal DAC reference at run time. You must set this property to true and set DacReferenceSource to Internal before you can set DacConnectReferenceToGround to true. SyntaxNamespace: NationalInstruments.DAQmxpublic bool DacAllowConnectReferenceToGround { get;

### DacAllowConnectReferenceToGround

Specifies whether to allow grounding the internal DAC reference at run time. You must set this property to true and set [DacReferenceSource](nationalinstruments-daqmx-aochannel-dacreferencesource.html) to [Internal](nationalinstruments-daqmx-aodacreferencesource.html) before you can set [DacConnectReferenceToGround](nationalinstruments-daqmx-aochannel-dacconnectreferencetoground.html) to true.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool DacAllowConnectReferenceToGround { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-dacconnectreferencetoground.html language=enus -->
## TOPIC 00691: DacConnectReferenceToGround

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-dacconnectreferencetoground.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-dacconnectreferencetoground.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to ground the internal DAC reference. Grounding the internal DAC reference has the effect of grounding all analog output channels and stopping waveform generation across all analog output channels regardless of whether the channels belong to the current task. You can ground the int

### DacConnectReferenceToGround

Specifies whether to ground the internal DAC reference. Grounding the internal DAC reference has the effect of grounding all analog output channels and stopping waveform generation across all analog output channels regardless of whether the channels belong to the current task. You can ground the internal DAC reference only when [DacReferenceSource](nationalinstruments-daqmx-aochannel-dacreferencesource.html) is [Internal](nationalinstruments-daqmx-aodacreferencesource.html) and [DacAllowConnectReferenceToGround](nationalinstruments-daqmx-aochannel-dacallowconnectreferencetoground.html) is true.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool DacConnectReferenceToGround { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-dacoffsetexternalsource.html language=enus -->
## TOPIC 00692: DacOffsetExternalSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-dacoffsetexternalsource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-dacoffsetexternalsource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source of the DAC offset voltage if DacOffsetSource is External. The valid sources for this signal vary by device. SyntaxNamespace: NationalInstruments.DAQmxpublic string DacOffsetExternalSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx dr

### DacOffsetExternalSource

Specifies the source of the DAC offset voltage if [DacOffsetSource](nationalinstruments-daqmx-aochannel-dacoffsetsource.html) is [External](nationalinstruments-daqmx-aodacoffsetsource.html). The valid sources for this signal [vary by device](/csh?context=nidaqmx_mxdevconsid_mseriesextrefsrc).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string DacOffsetExternalSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-dacoffsetsource.html language=enus -->
## TOPIC 00693: DacOffsetSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-dacoffsetsource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-dacoffsetsource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source of the DAC offset voltage. The value of this voltage source determines the full-scale value of the DAC. SyntaxNamespace: NationalInstruments.DAQmxpublic AODacOffsetSource DacOffsetSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx dri

### DacOffsetSource

Specifies the source of the DAC offset voltage. The value of this voltage source determines the full-scale value of the DAC.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AODacOffsetSource](nationalinstruments-daqmx-aodacoffsetsource.html) DacOffsetSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-dacoffsetvalue.html language=enus -->
## TOPIC 00694: DacOffsetValue

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-dacoffsetvalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-dacoffsetvalue.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in volts the value of the DAC offset voltage. To achieve best accuracy, the DAC offset value should be hand calibrated. SyntaxNamespace: NationalInstruments.DAQmxpublic double DacOffsetValue { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver ret

### DacOffsetValue

Specifies in volts the value of the DAC offset voltage. To achieve best accuracy, the DAC offset value should be hand calibrated.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DacOffsetValue { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-dacrangehigh.html language=enus -->
## TOPIC 00695: DacRangeHigh

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-dacrangehigh.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-dacrangehigh.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the upper limit of the output range of the device. This value is in the native units of the device. On E Series devices, for example, the native units is volts. SyntaxNamespace: NationalInstruments.DAQmxpublic double DacRangeHigh { get; set; }ExceptionsTypeDescriptionNationalInstruments.DA

### DacRangeHigh

Specifies the upper limit of the output range of the device. This value is in the native units of the device. On E Series devices, for example, the native units is volts.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DacRangeHigh { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-dacrangelow.html language=enus -->
## TOPIC 00696: DacRangeLow

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-dacrangelow.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-dacrangelow.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the lower limit of the output range of the device. This value is in the native units of the device. On E Series devices, for example, the native units is volts. SyntaxNamespace: NationalInstruments.DAQmxpublic double DacRangeLow { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQ

### DacRangeLow

Specifies the lower limit of the output range of the device. This value is in the native units of the device. On E Series devices, for example, the native units is volts.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DacRangeLow { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-dacreferenceexternalsource.html language=enus -->
## TOPIC 00697: DacReferenceExternalSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-dacreferenceexternalsource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-dacreferenceexternalsource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source of the DAC reference voltage if DacReferenceSource is External. The valid sources for this signal vary by device. SyntaxNamespace: NationalInstruments.DAQmxpublic string DacReferenceExternalSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI

### DacReferenceExternalSource

Specifies the source of the DAC reference voltage if [DacReferenceSource](nationalinstruments-daqmx-aochannel-dacreferencesource.html) is [External](nationalinstruments-daqmx-aodacreferencesource.html). The valid sources for this signal [vary by device](/csh?context=nidaqmx_mxdevconsid_mseriesextrefsrc).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string DacReferenceExternalSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-dacreferencesource.html language=enus -->
## TOPIC 00698: DacReferenceSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-dacreferencesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-dacreferencesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source of the DAC reference voltage. The value of this voltage source determines the full-scale value of the DAC. SyntaxNamespace: NationalInstruments.DAQmxpublic AODacReferenceSource DacReferenceSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-

### DacReferenceSource

Specifies the source of the DAC reference voltage. The value of this voltage source determines the full-scale value of the DAC.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AODacReferenceSource](nationalinstruments-daqmx-aodacreferencesource.html) DacReferenceSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-dacreferencevalue.html language=enus -->
## TOPIC 00699: DacReferenceValue

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-dacreferencevalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-dacreferencevalue.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in volts the value of the DAC reference voltage. This voltage determines the full-scale range of the DAC. Smaller reference voltages result in smaller ranges, but increased resolution. SyntaxNamespace: NationalInstruments.DAQmxpublic double DacReferenceValue { get; set; }ExceptionsTypeDesc

### DacReferenceValue

Specifies in volts the value of the DAC reference voltage. This voltage determines the full-scale range of the DAC. Smaller reference voltages result in smaller ranges, but increased resolution.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DacReferenceValue { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-datatransfermechanism.html language=enus -->
## TOPIC 00700: DataTransferMechanism

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-datatransfermechanism.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-datatransfermechanism.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the data transfer mode for the device. SyntaxNamespace: NationalInstruments.DAQmxpublic AODataTransferMechanism DataTransferMechanism { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DataTransferMechanism

Specifies the data transfer mode for the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AODataTransferMechanism](nationalinstruments-daqmx-aodatatransfermechanism.html) DataTransferMechanism { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-datatransferrequestcondition.html language=enus -->
## TOPIC 00701: DataTransferRequestCondition

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-datatransferrequestcondition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-datatransferrequestcondition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies under what condition to transfer data from the buffer to the onboard memory of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic AODataTransferRequestCondition DataTransferRequestCondition { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx d

### DataTransferRequestCondition

Specifies under what condition to transfer data from the buffer to the onboard memory of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AODataTransferRequestCondition](nationalinstruments-daqmx-aodatatransferrequestcondition.html) DataTransferRequestCondition { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-devicescalingcoefficients.html language=enus -->
## TOPIC 00702: DeviceScalingCoefficients

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-devicescalingcoefficients.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-devicescalingcoefficients.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the coefficients of a linear equation that NI-DAQmx uses to scale values from a voltage to the native format of the device. Each element of the array corresponds to a term of the equation. The first element of the array corresponds to the y-intercept, and the second element corresponds to

### DeviceScalingCoefficients

Indicates the coefficients of a linear equation that NI-DAQmx uses to scale values from a voltage to the native format of the device. Each element of the array corresponds to a term of the equation. The first element of the array corresponds to the y-intercept, and the second element corresponds to the slope. Scaling coefficients do not account for any custom scales that may be applied to the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] DeviceScalingCoefficients { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-enhancedimagerejectionenable.html language=enus -->
## TOPIC 00703: EnhancedImageRejectionEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-enhancedimagerejectionenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-enhancedimagerejectionenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the DAC interpolation filter. Disable the interpolation filter to improve DAC signal-to-noise ratio at the expense of degraded image rejection. SyntaxNamespace: NationalInstruments.DAQmxpublic bool EnhancedImageRejectionEnable { get; set; }ExceptionsTypeDescriptionNationa

### EnhancedImageRejectionEnable

Specifies whether to enable the DAC interpolation filter. Disable the interpolation filter to improve DAC signal-to-noise ratio at the expense of degraded image rejection.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool EnhancedImageRejectionEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-filterdelay.html language=enus -->
## TOPIC 00704: FilterDelay

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-filterdelay.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-filterdelay.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the amount of time between when the sample is written by the host device and when the sample is output by the DAC. This value is in the units you specify with FilterDelayUnits. SyntaxNamespace: NationalInstruments.DAQmxpublic double FilterDelay { get; set; }ExceptionsTypeDescriptionNationa

### FilterDelay

Specifies the amount of time between when the sample is written by the host device and when the sample is output by the DAC. This value is in the units you specify with [FilterDelayUnits](nationalinstruments-daqmx-aochannel-filterdelayunits.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double FilterDelay { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-filterdelayadjustment.html language=enus -->
## TOPIC 00705: FilterDelayAdjustment

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-filterdelayadjustment.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-filterdelayadjustment.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an additional amount of time to wait between when the sample is written by the host device and when the sample is output by the DAC. This delay adjustment is in addition to the value indicated by FilterDelay. This delay adjustment is in the units you specify with FilterDelayUnits. SyntaxNa

### FilterDelayAdjustment

Specifies an additional amount of time to wait between when the sample is written by the host device and when the sample is output by the DAC. This delay adjustment is in addition to the value indicated by [FilterDelay](nationalinstruments-daqmx-aochannel-filterdelay.html). This delay adjustment is in the units you specify with [FilterDelayUnits](nationalinstruments-daqmx-aochannel-filterdelayunits.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double FilterDelayAdjustment { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-filterdelayunits.html language=enus -->
## TOPIC 00706: FilterDelayUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-filterdelayunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-filterdelayunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of FilterDelay and FilterDelayAdjustment. SyntaxNamespace: NationalInstruments.DAQmxpublic AOFilterDelayUnits FilterDelayUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### FilterDelayUnits

Specifies the units of [FilterDelay](nationalinstruments-daqmx-aochannel-filterdelay.html) and [FilterDelayAdjustment](nationalinstruments-daqmx-aochannel-filterdelayadjustment.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AOFilterDelayUnits](nationalinstruments-daqmx-aofilterdelayunits.html) FilterDelayUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-functiongenerationamplitude.html language=enus -->
## TOPIC 00707: FunctionGenerationAmplitude

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-functiongenerationamplitude.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-functiongenerationamplitude.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the zero-to-peak amplitude of the waveform to generate in volts. Zero and negative values are valid. SyntaxNamespace: NationalInstruments.DAQmxpublic double FunctionGenerationAmplitude { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned

### FunctionGenerationAmplitude

Specifies the zero-to-peak amplitude of the waveform to generate in volts. Zero and negative values are valid.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double FunctionGenerationAmplitude { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-functiongenerationfmdeviation.html language=enus -->
## TOPIC 00708: FunctionGenerationFMDeviation

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-functiongenerationfmdeviation.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-functiongenerationfmdeviation.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the FM deviation in hertz per volt when FunctionGenerationModulationType is FM. SyntaxNamespace: NationalInstruments.DAQmxpublic double FunctionGenerationFMDeviation { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### FunctionGenerationFMDeviation

Specifies the FM deviation in hertz per volt when [FunctionGenerationModulationType](nationalinstruments-daqmx-aochannel-functiongenerationmodulationtype.html) is [FM](nationalinstruments-daqmx-aofunctiongenerationmodulationtype.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double FunctionGenerationFMDeviation { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-functiongenerationfrequency.html language=enus -->
## TOPIC 00709: FunctionGenerationFrequency

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-functiongenerationfrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-functiongenerationfrequency.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency of the waveform to generate in hertz. SyntaxNamespace: NationalInstruments.DAQmxpublic double FunctionGenerationFrequency { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### FunctionGenerationFrequency

Specifies the frequency of the waveform to generate in hertz.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double FunctionGenerationFrequency { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-functiongenerationmodulationtype.html language=enus -->
## TOPIC 00710: FunctionGenerationModulationType

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-functiongenerationmodulationtype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-functiongenerationmodulationtype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies if the device generates a modulated version of the waveform using the original waveform as a carrier and input from an external terminal as the signal. SyntaxNamespace: NationalInstruments.DAQmxpublic AOFunctionGenerationModulationType FunctionGenerationModulationType { get; set; }Exceptio

### FunctionGenerationModulationType

Specifies if the device generates a modulated version of the waveform using the original waveform as a carrier and input from an external terminal as the signal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AOFunctionGenerationModulationType](nationalinstruments-daqmx-aofunctiongenerationmodulationtype.html) FunctionGenerationModulationType { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-functiongenerationoffset.html language=enus -->
## TOPIC 00711: FunctionGenerationOffset

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-functiongenerationoffset.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-functiongenerationoffset.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the voltage offset of the waveform to generate. SyntaxNamespace: NationalInstruments.DAQmxpublic double FunctionGenerationOffset { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### FunctionGenerationOffset

Specifies the voltage offset of the waveform to generate.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double FunctionGenerationOffset { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-functiongenerationsquaredutycycle.html language=enus -->
## TOPIC 00712: FunctionGenerationSquareDutyCycle

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-functiongenerationsquaredutycycle.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-functiongenerationsquaredutycycle.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the square wave duty cycle of the waveform to generate. SyntaxNamespace: NationalInstruments.DAQmxpublic double FunctionGenerationSquareDutyCycle { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### FunctionGenerationSquareDutyCycle

Specifies the square wave duty cycle of the waveform to generate.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double FunctionGenerationSquareDutyCycle { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-functiongenerationstartphase.html language=enus -->
## TOPIC 00713: FunctionGenerationStartPhase

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-functiongenerationstartphase.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-functiongenerationstartphase.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the starting phase in degrees of the waveform to generate. SyntaxNamespace: NationalInstruments.DAQmxpublic double FunctionGenerationStartPhase { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### FunctionGenerationStartPhase

Specifies the starting phase in degrees of the waveform to generate.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double FunctionGenerationStartPhase { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-functiongenerationtype.html language=enus -->
## TOPIC 00714: FunctionGenerationType

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-functiongenerationtype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-functiongenerationtype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the kind of the waveform to generate. SyntaxNamespace: NationalInstruments.DAQmxpublic AOFunctionGenerationType FunctionGenerationType { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### FunctionGenerationType

Specifies the kind of the waveform to generate.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AOFunctionGenerationType](nationalinstruments-daqmx-aofunctiongenerationtype.html) FunctionGenerationType { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-gain.html language=enus -->
## TOPIC 00715: Gain

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-gain.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-gain.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in decibels the gain factor to apply to the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic double Gain { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Gain

Specifies in decibels the gain factor to apply to the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double Gain { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-idleoutputbehavior.html language=enus -->
## TOPIC 00716: IdleOutputBehavior

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-idleoutputbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-idleoutputbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the state of the channel when no generation is in progress. SyntaxNamespace: NationalInstruments.DAQmxpublic AOIdleOutputBehavior IdleOutputBehavior { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### IdleOutputBehavior

Specifies the state of the channel when no generation is in progress.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AOIdleOutputBehavior](nationalinstruments-daqmx-aoidleoutputbehavior.html) IdleOutputBehavior { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-loadimpedance.html language=enus -->
## TOPIC 00717: LoadImpedance

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-loadimpedance.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-loadimpedance.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in ohms the load impedance connected to the analog output channel. SyntaxNamespace: NationalInstruments.DAQmxpublic double LoadImpedance { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### LoadImpedance

Specifies in ohms the load impedance connected to the analog output channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double LoadImpedance { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-maximum.html language=enus -->
## TOPIC 00718: Maximum

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-maximum.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-maximum.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum value you expect to generate. The value is in the units you specify with a units property. If you try to write a value larger than the maximum value, NI-DAQmx generates an error. NI-DAQmx might coerce this value to a smaller value if other task settings restrict the device from

### Maximum

Specifies the maximum value you expect to generate. The value is in the units you specify with a units property. If you try to write a value larger than the maximum value, NI-DAQmx generates an error. NI-DAQmx might coerce this value to a smaller value if other task settings restrict the device from generating the desired maximum.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double Maximum { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-memorymappingenable.html language=enus -->
## TOPIC 00719: MemoryMappingEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-memorymappingenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-memorymappingenable.html
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

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-minimum.html language=enus -->
## TOPIC 00720: Minimum

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-minimum.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-minimum.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the minimum value you expect to generate. The value is in the units you specify with a units property. If you try to write a value smaller than the minimum value, NI-DAQmx generates an error. NI-DAQmx might coerce this value to a larger value if other task settings restrict the device from

### Minimum

Specifies the minimum value you expect to generate. The value is in the units you specify with a units property. If you try to write a value smaller than the minimum value, NI-DAQmx generates an error. NI-DAQmx might coerce this value to a larger value if other task settings restrict the device from generating the desired minimum.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double Minimum { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-outputimpedance.html language=enus -->
## TOPIC 00721: OutputImpedance

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-outputimpedance.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-outputimpedance.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in ohms the impedance of the analog output stage of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic double OutputImpedance { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### OutputImpedance

Specifies in ohms the impedance of the analog output stage of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double OutputImpedance { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-outputtype.html language=enus -->
## TOPIC 00722: OutputType

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-outputtype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-outputtype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the channel generates voltage, current, or a waveform. SyntaxNamespace: NationalInstruments.DAQmxpublic AOOutputType OutputType { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### OutputType

Indicates whether the channel generates voltage, current, or a waveform.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AOOutputType](nationalinstruments-daqmx-aooutputtype.html) OutputType { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-reglitchenable.html language=enus -->
## TOPIC 00723: ReglitchEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-reglitchenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-reglitchenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable reglitching. The output of a DAC normally glitches whenever the DAC is updated with a new value. The amount of glitching differs from code to code and is generally largest at major code transitions. Reglitching generates uniform glitch energy at each code transition and p

### ReglitchEnable

Specifies whether to enable reglitching. The output of a DAC normally glitches whenever the DAC is updated with a new value. The amount of glitching differs from code to code and is generally largest at major code transitions. Reglitching generates uniform glitch energy at each code transition and provides for more uniform glitches. Uniform glitch energy makes it easier to filter out the noise introduced from glitching during spectrum analysis.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool ReglitchEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-resolution.html language=enus -->
## TOPIC 00724: Resolution

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-resolution.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-resolution.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the resolution of the digital-to-analog converter of the channel. This value is in the units you specify with ResolutionUnits. SyntaxNamespace: NationalInstruments.DAQmxpublic double Resolution { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver retur

### Resolution

Indicates the resolution of the digital-to-analog converter of the channel. This value is in the units you specify with [ResolutionUnits](nationalinstruments-daqmx-aochannel-resolutionunits.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double Resolution { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-resolutionunits.html language=enus -->
## TOPIC 00725: ResolutionUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-resolutionunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-resolutionunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of Resolution. SyntaxNamespace: NationalInstruments.DAQmxpublic AOResolutionUnits ResolutionUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ResolutionUnits

Specifies the units of [Resolution](nationalinstruments-daqmx-aochannel-resolution.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AOResolutionUnits](nationalinstruments-daqmx-aoresolutionunits.html) ResolutionUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-terminalconfiguration.html language=enus -->
## TOPIC 00726: TerminalConfiguration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-terminalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-terminalconfiguration.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal configuration of the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic AOTerminalConfiguration TerminalConfiguration { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### TerminalConfiguration

Specifies the terminal configuration of the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AOTerminalConfiguration](nationalinstruments-daqmx-aoterminalconfiguration.html) TerminalConfiguration { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-usbtransferrequestcount.html language=enus -->
## TOPIC 00727: UsbTransferRequestCount

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-usbtransferrequestcount.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-usbtransferrequestcount.html
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

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-usbtransferrequestsize.html language=enus -->
## TOPIC 00728: UsbTransferRequestSize

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-usbtransferrequestsize.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-usbtransferrequestsize.html
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

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-useonlyonboardmemory.html language=enus -->
## TOPIC 00729: UseOnlyOnBoardMemory

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-useonlyonboardmemory.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-useonlyonboardmemory.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to write samples directly to the onboard memory of the device, bypassing the memory buffer. Generally, you cannot update onboard memory directly after you start the task. Onboard memory includes data FIFOs. SyntaxNamespace: NationalInstruments.DAQmxpublic bool UseOnlyOnBoardMemory

### UseOnlyOnBoardMemory

Specifies whether to write samples directly to the onboard memory of the device, bypassing the memory buffer. Generally, you cannot update onboard memory directly after you start the task. Onboard memory includes data FIFOs.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool UseOnlyOnBoardMemory { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-voltagecurrentlimit.html language=enus -->
## TOPIC 00730: VoltageCurrentLimit

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-voltagecurrentlimit.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-voltagecurrentlimit.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the current limit, in amperes, for the voltage channel. SyntaxNamespace: NationalInstruments.DAQmxpublic double VoltageCurrentLimit { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### VoltageCurrentLimit

Specifies the current limit, in amperes, for the voltage channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double VoltageCurrentLimit { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel-voltageunits.html language=enus -->
## TOPIC 00731: VoltageUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel-voltageunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel-voltageunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in what units to generate voltage on the channel. Write data to the channel in the units you select. SyntaxNamespace: NationalInstruments.DAQmxpublic AOVoltageUnits VoltageUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an erro

### VoltageUnits

Specifies in what units to generate voltage on the channel. Write data to the channel in the units you select.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AOVoltageUnits](nationalinstruments-daqmx-aovoltageunits.html) VoltageUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannel.html language=enus -->
## TOPIC 00732: AOChannel Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannel.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannel.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Encapsulates one or more analog output channels and the properties for an analog output channel. Derives fromChannelIFilteredTypeDescriptorSyntaxNamespace: NationalInstruments.DAQmxpublic class AOChannel : Channel, IFilteredTypeDescriptorRemarksUse the AOChannels property to create or access an anal

### AOChannel Class

Encapsulates one or more analog output channels and the properties for an analog output channel.

#### Derives from

- Channel
- IFilteredTypeDescriptor

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class AOChannel : Channel, IFilteredTypeDescriptor

#### Remarks

AOChannels

AOChannel

AOChannel

AOChannels

AOChannelCollection

AOChannel

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| CommonModeOffset | Specifies the common-mode offset of the AO channel. Use the property only when Terminal Configuration is set to Differential. |
| CurrentUnits | Specifies in what units to generate current on the channel. Write data to the channel in the units you select. |
| CustomScaleName | Specifies the name of a custom scale for the channel. |
| DacAllowConnectReferenceToGround | Specifies whether to allow grounding the internal DAC reference at run time. You must set this property to true and set DacReferenceSource to Internal before you can set DacConnectReferenceToGround to true. |
| DacConnectReferenceToGround | Specifies whether to ground the internal DAC reference. Grounding the internal DAC reference has the effect of grounding all analog output channels and stopping waveform generation across all analog output channels regardless of whether the channels belong to the current task. You can ground the internal DAC reference only when DacReferenceSource is Internal and DacAllowConnectReferenceToGround is true. |
| DacOffsetExternalSource | Specifies the source of the DAC offset voltage if DacOffsetSource is External. The valid sources for this signal vary by device. |
| DacOffsetSource | Specifies the source of the DAC offset voltage. The value of this voltage source determines the full-scale value of the DAC. |
| DacOffsetValue | Specifies in volts the value of the DAC offset voltage. To achieve best accuracy, the DAC offset value should be hand calibrated. |
| DacRangeHigh | Specifies the upper limit of the output range of the device. This value is in the native units of the device. On E Series devices, for example, the native units is volts. |
| DacRangeLow | Specifies the lower limit of the output range of the device. This value is in the native units of the device. On E Series devices, for example, the native units is volts. |
| DacReferenceExternalSource | Specifies the source of the DAC reference voltage if DacReferenceSource is External. The valid sources for this signal vary by device. |
| DacReferenceSource | Specifies the source of the DAC reference voltage. The value of this voltage source determines the full-scale value of the DAC. |
| DacReferenceValue | Specifies in volts the value of the DAC reference voltage. This voltage determines the full-scale range of the DAC. Smaller reference voltages result in smaller ranges, but increased resolution. |
| DataTransferMechanism | Specifies the data transfer mode for the device. |
| DataTransferRequestCondition | Specifies under what condition to transfer data from the buffer to the onboard memory of the device. |
| DeviceScalingCoefficients | Indicates the coefficients of a linear equation that NI-DAQmx uses to scale values from a voltage to the native format of the device. Each element of the array corresponds to a term of the equation. The first element of the array corresponds to the y-intercept, and the second element corresponds to the slope. Scaling coefficients do not account for any custom scales that may be applied to the channel. |
| EnhancedImageRejectionEnable | Specifies whether to enable the DAC interpolation filter. Disable the interpolation filter to improve DAC signal-to-noise ratio at the expense of degraded image rejection. |
| FilterDelay | Specifies the amount of time between when the sample is written by the host device and when the sample is output by the DAC. This value is in the units you specify with FilterDelayUnits. |
| FilterDelayAdjustment | Specifies an additional amount of time to wait between when the sample is written by the host device and when the sample is output by the DAC. This delay adjustment is in addition to the value indicated by FilterDelay. This delay adjustment is in the units you specify with FilterDelayUnits. |
| FilterDelayUnits | Specifies the units of FilterDelay and FilterDelayAdjustment. |
| FunctionGenerationAmplitude | Specifies the zero-to-peak amplitude of the waveform to generate in volts. Zero and negative values are valid. |
| FunctionGenerationFMDeviation | Specifies the FM deviation in hertz per volt when FunctionGenerationModulationType is FM. |
| FunctionGenerationFrequency | Specifies the frequency of the waveform to generate in hertz. |
| FunctionGenerationModulationType | Specifies if the device generates a modulated version of the waveform using the original waveform as a carrier and input from an external terminal as the signal. |
| FunctionGenerationOffset | Specifies the voltage offset of the waveform to generate. |
| FunctionGenerationSquareDutyCycle | Specifies the square wave duty cycle of the waveform to generate. |
| FunctionGenerationStartPhase | Specifies the starting phase in degrees of the waveform to generate. |
| FunctionGenerationType | Specifies the kind of the waveform to generate. |
| Gain | Specifies in decibels the gain factor to apply to the channel. |
| IdleOutputBehavior | Specifies the state of the channel when no generation is in progress. |
| LoadImpedance | Specifies in ohms the load impedance connected to the analog output channel. |
| Maximum | Specifies the maximum value you expect to generate. The value is in the units you specify with a units property. If you try to write a value larger than the maximum value, NI-DAQmx generates an error. NI-DAQmx might coerce this value to a smaller value if other task settings restrict the device from generating the desired maximum. |
| MemoryMappingEnable | Specifies for NI-DAQmx to map hardware registers to the memory space of the application, if possible. Normally, NI-DAQmx maps hardware registers to memory accessible only to the kernel. Mapping the registers to the memory space of the application increases performance. However, if the application accesses the memory space mapped to the registers, it can adversely affect the operation of the device and possibly result in a system crash. |
| Minimum | Specifies the minimum value you expect to generate. The value is in the units you specify with a units property. If you try to write a value smaller than the minimum value, NI-DAQmx generates an error. NI-DAQmx might coerce this value to a larger value if other task settings restrict the device from generating the desired minimum. |
| OutputImpedance | Specifies in ohms the impedance of the analog output stage of the device. |
| OutputType | Indicates whether the channel generates voltage, current, or a waveform. |
| ReglitchEnable | Specifies whether to enable reglitching. The output of a DAC normally glitches whenever the DAC is updated with a new value. The amount of glitching differs from code to code and is generally largest at major code transitions. Reglitching generates uniform glitch energy at each code transition and provides for more uniform glitches. Uniform glitch energy makes it easier to filter out the noise introduced from glitching during spectrum analysis. |
| Resolution | Indicates the resolution of the digital-to-analog converter of the channel. This value is in the units you specify with ResolutionUnits. |
| ResolutionUnits | Specifies the units of Resolution. |
| TerminalConfiguration | Specifies the terminal configuration of the channel. |
| UsbTransferRequestCount | Specifies the maximum number of simultaneous USB transfers used to stream data. Modify this value to affect performance under different combinations of operating system and device. |
| UsbTransferRequestSize | Specifies the maximum size of a USB transfer request in bytes. Modify this value to affect performance under different combinations of operating system and device. |
| UseOnlyOnBoardMemory | Specifies whether to write samples directly to the onboard memory of the device, bypassing the memory buffer. Generally, you cannot update onboard memory directly after you start the task. Onboard memory includes data FIFOs. |
| VoltageCurrentLimit | Specifies the current limit, in amperes, for the voltage channel. |
| VoltageUnits | Specifies in what units to generate voltage on the channel. Write data to the channel in the units you select. |

#### See Also

- AOChannelCollection

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannelcollection-all.html language=enus -->
## TOPIC 00733: All

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannelcollection-all.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannelcollection-all.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an AOChannel that operates on all of the channels in the task. SyntaxNamespace: NationalInstruments.DAQmxpublic AOChannel All { get; }RemarksAn AOChannel that operates on all of the channels in a task.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an

### All

Gets an [AOChannel](nationalinstruments-daqmx-aochannel.html) that operates on all of the channels in the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AOChannel](nationalinstruments-daqmx-aochannel.html) All { get; }

#### Remarks

An [AOChannel](nationalinstruments-daqmx-aochannel.html) that operates on all of the channels in a task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannelcollection-copyto__array-int.html language=enus -->
## TOPIC 00734: CopyTo(Array, int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannelcollection-copyto__array-int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannelcollection-copyto__array-int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Copies the collection to an array or a portion of an array. This operation is not supported for AOChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic void CopyTo(Array array, int index)ParametersNameTypeDescriptionarrayArrayDestination array for the collection.indexintThe index in th

### CopyTo(Array, int)

Copies the collection to an array or a portion of an array. This operation is not supported for [AOChannelCollection](nationalinstruments-daqmx-aochannelcollection.html).

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

AOChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannelcollection-count.html language=enus -->
## TOPIC 00735: Count

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannelcollection-count.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannelcollection-count.html
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

AOChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannelcollection-createcurrentchannel__string-string-double-double-aocurrentunits.html language=enus -->
## TOPIC 00736: CreateCurrentChannel(string, string, double, double, AOCurrentUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannelcollection-createcurrentchannel__string-string-double-double-aocurrentunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannelcollection-createcurrentchannel__string-string-double-double-aocurrentunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AOChannel to generate current. This method adds one or more channels to the AOChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AOChannel CreateCurrentChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AOCurrentUnits

### CreateCurrentChannel(string, string, double, double, AOCurrentUnits)

Creates an [AOChannel](nationalinstruments-daqmx-aochannel.html) to [generate current](/csh?context=nidaqmx_daqhelp_measuring_current). This method adds one or more channels to the [AOChannelCollection](nationalinstruments-daqmx-aochannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AOChannel](nationalinstruments-daqmx-aochannel.html) CreateCurrentChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AOCurrentUnits units)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateCurrentChannel(string, string, double, double, AOCurrentUnits) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value to generate, in units . |
| maximumValue | double | The maximum value to generate, in units . |
| units | AOCurrentUnits | The units to use to generate current. |

#### Returns

The newly created [AOChannel](nationalinstruments-daqmx-aochannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannelcollection-createcurrentchannel__string-string-double-double-string.html language=enus -->
## TOPIC 00737: CreateCurrentChannel(string, string, double, double, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannelcollection-createcurrentchannel__string-string-double-double-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannelcollection-createcurrentchannel__string-string-double-double-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AOChannel with the specified custom scale to generate current. This method adds one or more channels to the AOChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AOChannel CreateCurrentChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, dou

### CreateCurrentChannel(string, string, double, double, string)

Creates an [AOChannel](nationalinstruments-daqmx-aochannel.html) with the specified custom scale to [generate current](/csh?context=nidaqmx_daqhelp_measuring_current). This method adds one or more channels to the [AOChannelCollection](nationalinstruments-daqmx-aochannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AOChannel](nationalinstruments-daqmx-aochannel.html) CreateCurrentChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, string customScaleName)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateCurrentChannel(string, string, double, double, string) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value to generate, in units. |
| maximumValue | double | The maximum value to generate, in units. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |

#### Returns

The newly created [AOChannel](nationalinstruments-daqmx-aochannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannelcollection-createfunctiongenerationchannel__string-string-aofunctiongenerationtype-double-double-double.html language=enus -->
## TOPIC 00738: CreateFunctionGenerationChannel(string, string, AOFunctionGenerationType, double, double, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannelcollection-createfunctiongenerationchannel__string-string-aofunctiongenerationtype-double-double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannelcollection-createfunctiongenerationchannel__string-string-aofunctiongenerationtype-double-double-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AOChannel that continuously generates a waveform with the specificed waveform type, frequency, amplitude, and offset. This method adds one or more channels to the AOChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AOChannel CreateFunctionGenerationChannel(string physica

### CreateFunctionGenerationChannel(string, string, AOFunctionGenerationType, double, double, double)

Creates an [AOChannel](nationalinstruments-daqmx-aochannel.html) that continuously generates a waveform with the specificed waveform type, frequency, amplitude, and offset. This method adds one or more channels to the [AOChannelCollection](nationalinstruments-daqmx-aochannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AOChannel](nationalinstruments-daqmx-aochannel.html) CreateFunctionGenerationChannel(string physicalChannelName, string nameToAssignChannel, AOFunctionGenerationType waveformType, double frequency, double amplitude, double offset)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. [CreateCurrentChannel(string, string, double, double, string)](nationalinstruments-daqmx-aochannelcollection-createcurrentchannel__string-string-double-double-string.html) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| waveformType | AOFunctionGenerationType | The AOFunctionGenerationType to generate. |
| frequency | double | The desired frequency of the output waveformType . |
| amplitude | double | The desired amplitude of the output waveformType , in units of volts zero-to-peak. Zero and negative values are valid. |
| offset | double | The desired offset of the output waveformType . |

#### Returns

The newly created [AOChannel](nationalinstruments-daqmx-aochannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannelcollection-createfunctiongenerationchannel__string-string-aofunctiongenerationtype-double-double.html language=enus -->
## TOPIC 00739: CreateFunctionGenerationChannel(string, string, AOFunctionGenerationType, double, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannelcollection-createfunctiongenerationchannel__string-string-aofunctiongenerationtype-double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannelcollection-createfunctiongenerationchannel__string-string-aofunctiongenerationtype-double-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AOChannel that continuously generates a waveform with the specificed waveform type, frequency, and amplitude. This method adds one or more channels to the AOChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AOChannel CreateFunctionGenerationChannel(string physicalChannel

### CreateFunctionGenerationChannel(string, string, AOFunctionGenerationType, double, double)

Creates an [AOChannel](nationalinstruments-daqmx-aochannel.html) that continuously generates a waveform with the specificed waveform type, frequency, and amplitude. This method adds one or more channels to the [AOChannelCollection](nationalinstruments-daqmx-aochannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AOChannel](nationalinstruments-daqmx-aochannel.html) CreateFunctionGenerationChannel(string physicalChannelName, string nameToAssignChannel, AOFunctionGenerationType waveformType, double frequency, double amplitude)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. [CreateCurrentChannel(string, string, double, double, string)](nationalinstruments-daqmx-aochannelcollection-createcurrentchannel__string-string-double-double-string.html) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| waveformType | AOFunctionGenerationType | The AOFunctionGenerationType to generate. |
| frequency | double | The desired frequency of the output waveformType . |
| amplitude | double | The desired amplitude of the output waveformType , in units of volts zero-to-peak. Zero and negative values are valid. |

#### Returns

The newly created [AOChannel](nationalinstruments-daqmx-aochannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannelcollection-createvoltagechannel__string-string-double-double-aovoltageunits.html language=enus -->
## TOPIC 00740: CreateVoltageChannel(string, string, double, double, AOVoltageUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannelcollection-createvoltagechannel__string-string-double-double-aovoltageunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannelcollection-createvoltagechannel__string-string-double-double-aovoltageunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AOChannel to generate voltage. This method adds one or more channels to the AOChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AOChannel CreateVoltageChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AOVoltageUnits

### CreateVoltageChannel(string, string, double, double, AOVoltageUnits)

Creates an [AOChannel](nationalinstruments-daqmx-aochannel.html) to [generate voltage](/csh?context=nidaqmx_daqhelp_genvolt). This method adds one or more channels to the [AOChannelCollection](nationalinstruments-daqmx-aochannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AOChannel](nationalinstruments-daqmx-aochannel.html) CreateVoltageChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AOVoltageUnits units)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateVoltageChannel(string, string, double, double, AOVoltageUnits) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value to generate, in units . |
| maximumValue | double | The maximum value to generate, in units . |
| units | AOVoltageUnits | The units to use to generate voltage. |

#### Returns

The newly created [AOChannel](nationalinstruments-daqmx-aochannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannelcollection-createvoltagechannel__string-string-double-double-string.html language=enus -->
## TOPIC 00741: CreateVoltageChannel(string, string, double, double, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannelcollection-createvoltagechannel__string-string-double-double-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannelcollection-createvoltagechannel__string-string-double-double-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AOChannel with the specified custom scale to generate voltage. This method adds one or more channels to the AOChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AOChannel CreateVoltageChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, dou

### CreateVoltageChannel(string, string, double, double, string)

Creates an [AOChannel](nationalinstruments-daqmx-aochannel.html) with the specified custom scale to [generate voltage](/csh?context=nidaqmx_daqhelp_genvolt). This method adds one or more channels to the [AOChannelCollection](nationalinstruments-daqmx-aochannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AOChannel](nationalinstruments-daqmx-aochannel.html) CreateVoltageChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, string customScaleName)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateVoltageChannel(string, string, double, double, string) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value to generate. |
| maximumValue | double | The maximum value to generate. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |

#### Returns

The newly created [AOChannel](nationalinstruments-daqmx-aochannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AOChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannelcollection-getenumerator.html language=enus -->
## TOPIC 00742: GetEnumerator()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannelcollection-getenumerator.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannelcollection-getenumerator.html
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

AOChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannelcollection-this__long.html language=enus -->
## TOPIC 00743: this[long index]

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannelcollection-this__long.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannelcollection-this__long.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the AOChannel at the specified index. In Visual C#, this property is the indexer. SyntaxNamespace: NationalInstruments.DAQmxpublic AOChannel this[long index] { get; }RemarksThe AOChannel at the specified index. ChannelsParametersNameTypeDescriptionindexlongThe zero-based index of the entry to l

### this[long index]

Gets the [AOChannel](nationalinstruments-daqmx-aochannel.html) at the specified index. In Visual C#, this property is the indexer.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AOChannel](nationalinstruments-daqmx-aochannel.html) this[long index] { get; }

#### Remarks

The [AOChannel](nationalinstruments-daqmx-aochannel.html) at the specified index.

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

- AOChannel

Parent topic:

AOChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannelcollection-this__string.html language=enus -->
## TOPIC 00744: this[string virtualChannelName]

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannelcollection-this__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannelcollection-this__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the AOChannel with the specified virtual channel name. In Visual C#, this property is the indexer. SyntaxNamespace: NationalInstruments.DAQmxpublic AOChannel this[string virtualChannelName] { get; }RemarksThe specified AOChannel.By using a comma or colon in virtualChannelName , you can retrieve

### this[string virtualChannelName]

Gets the [AOChannel](nationalinstruments-daqmx-aochannel.html) with the specified virtual channel name. In Visual C#, this property is the indexer.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AOChannel](nationalinstruments-daqmx-aochannel.html) this[string virtualChannelName] { get; }

#### Remarks

The specified [AOChannel](nationalinstruments-daqmx-aochannel.html).

By using a comma or colon in *virtualChannelName* , you can retrieve more than one channel at a time. For more information refer to [Channels](https://#).

Channels

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| virtualChannelName | string | One or more virtual channel names that the retrieved AOChannel operates on. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

#### See Also

- AOChannel

Parent topic:

AOChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannelcollection-tostring.html language=enus -->
## TOPIC 00745: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannelcollection-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannelcollection-tostring.html
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

AOChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aochannelcollection.html language=enus -->
## TOPIC 00746: AOChannelCollection Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aochannelcollection.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aochannelcollection.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains the collection of analog output channels for a Task. Derives fromMarshalByRefObjectICollectionSyntaxNamespace: NationalInstruments.DAQmxpublic class AOChannelCollection : MarshalByRefObject, ICollectionRemarksExample applications are located in the <Public Documents>\National Instruments\NI

### AOChannelCollection Class

Contains the collection of analog output channels for a [Task](nationalinstruments-daqmx-task.html).

#### Derives from

- MarshalByRefObject
- ICollection

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class AOChannelCollection : MarshalByRefObject, ICollection

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| All | Gets an AOChannel that operates on all of the channels in the task. |
| Count | Gets the number of elements in the collection. |
| this[long index] | Gets the AOChannel at the specified index. In Visual C#, this property is the indexer. |
| this[string virtualChannelName] | Gets the AOChannel with the specified virtual channel name. In Visual C#, this property is the indexer. |

#### Methods

| Name | Description |
| --- | --- |
| CopyTo(Array, int) | Copies the collection to an array or a portion of an array. This operation is not supported for AOChannelCollection. |
| CreateCurrentChannel(string, string, double, double, string) | Creates an AOChannel with the specified custom scale to generate current. This method adds one or more channels to the AOChannelCollection. |
| CreateCurrentChannel(string, string, double, double, AOCurrentUnits) | Creates an AOChannel to generate current. This method adds one or more channels to the AOChannelCollection. |
| CreateFunctionGenerationChannel(string, string, AOFunctionGenerationType, double, double) | Creates an AOChannel that continuously generates a waveform with the specificed waveform type, frequency, and amplitude. This method adds one or more channels to the AOChannelCollection. |
| CreateFunctionGenerationChannel(string, string, AOFunctionGenerationType, double, double, double) | Creates an AOChannel that continuously generates a waveform with the specificed waveform type, frequency, amplitude, and offset. This method adds one or more channels to the AOChannelCollection. |
| CreateVoltageChannel(string, string, double, double, AOVoltageUnits) | Creates an AOChannel to generate voltage. This method adds one or more channels to the AOChannelCollection. |
| CreateVoltageChannel(string, string, double, double, string) | Creates an AOChannel with the specified custom scale to generate voltage. This method adds one or more channels to the AOChannelCollection. |
| GetEnumerator() | Returns an enumerator that you can use to iterate through the collection. |
| ToString() | Returns a string representation of the object. |

#### See Also

- Task
- AOChannels
- AOChannel

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aocurrentunits.html language=enus -->
## TOPIC 00747: AOCurrentUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aocurrentunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aocurrentunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in what units to generate current on the channel. Write data to the channel in the units you select. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AOCurrentUnitsRemarksSpecifies in what units to generate current on the channel. Write data to the channel in the units you select. Use

### AOCurrentUnits Enumeration

Specifies in what units to generate current on the channel. Write data to the channel in the units you select.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AOCurrentUnits

#### Remarks

Specifies in what units to generate current on the channel. Write data to the channel in the units you select. Use this enumeration to get or set the value of [CurrentUnits](nationalinstruments-daqmx-aochannel-currentunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Amps | 10342 | Amperes. |
| FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |
| FromTeds | 12516 | Units defined by TEDS information associated with the channel. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aodacoffsetsource.html language=enus -->
## TOPIC 00748: AODacOffsetSource Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aodacoffsetsource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aodacoffsetsource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source of the DAC offset voltage. The value of this voltage source determines the full-scale value of the DAC. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AODacOffsetSourceRemarksSpecifies the source of the DAC offset voltage. The value of this voltage source determines the f

### AODacOffsetSource Enumeration

Specifies the source of the DAC offset voltage. The value of this voltage source determines the full-scale value of the DAC.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AODacOffsetSource

#### Remarks

Specifies the source of the DAC offset voltage. The value of this voltage source determines the full-scale value of the DAC. Use this enumeration to get or set the value of [DacOffsetSource](nationalinstruments-daqmx-aochannel-dacoffsetsource.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Internal | 10200 | Internal to the device. |
| External | 10167 | External to the device. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aodacreferencesource.html language=enus -->
## TOPIC 00749: AODacReferenceSource Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aodacreferencesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aodacreferencesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source of the DAC reference voltage. The value of this voltage source determines the full-scale value of the DAC. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AODacReferenceSourceRemarksSpecifies the source of the DAC reference voltage. The value of this voltage source determi

### AODacReferenceSource Enumeration

Specifies the source of the DAC reference voltage. The value of this voltage source determines the full-scale value of the DAC.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AODacReferenceSource

#### Remarks

Specifies the source of the DAC reference voltage. The value of this voltage source determines the full-scale value of the DAC. Use this enumeration to get or set the value of [DacReferenceSource](nationalinstruments-daqmx-aochannel-dacreferencesource.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Internal | 10200 | Internal to the device. |
| External | 10167 | External to the device. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aodatatransfermechanism.html language=enus -->
## TOPIC 00750: AODataTransferMechanism Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aodatatransfermechanism.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aodatatransfermechanism.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the data transfer mode for the device. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AODataTransferMechanismRemarksSpecifies the data transfer mode for the device. Use this enumeration to get or set the value of DataTransferMechanism.MembersNameValueDescriptionDma10054Direct Memory

### AODataTransferMechanism Enumeration

Specifies the data transfer mode for the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AODataTransferMechanism

#### Remarks

Specifies the data transfer mode for the device. Use this enumeration to get or set the value of [DataTransferMechanism](nationalinstruments-daqmx-aochannel-datatransfermechanism.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Dma | 10054 | Direct Memory Access. Data transfers take place independently from the application. |
| Interrupts | 10204 | Data transfers take place independently from the application. Using interrupts increases CPU usage because the CPU must service interrupt requests. Typically, you should use interrupts if the device is out of DMA channels. |
| ProgrammedIO | 10264 | Data transfers take place when you call reading from the task or writing to the task. |
| UsbBulk | 12590 | Data transfers take place independently from the application using a USB bulk pipe. |

Parent topic:

NationalInstruments.DAQmx
