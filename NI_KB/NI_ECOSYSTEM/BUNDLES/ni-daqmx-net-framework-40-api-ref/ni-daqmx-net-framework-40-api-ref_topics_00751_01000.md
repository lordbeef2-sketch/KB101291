# NI DOCUMENT BUNDLE: ni-daqmx-net-framework-40-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-daqmx-net-framework-40-api-ref start=751 end=1000 -->
<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_outputtype.htm language=enus -->
## TOPIC 00751: COChannelOutputType Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_outputtype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_outputtype.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

COChannel.OutputType Property

### COChannelOutputType Property

Indicates how to define pulses generated on the channel.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public COOutputType OutputType { get; }
```

```text
Public ReadOnly Property OutputType As COOutputType
	Get
```

###### Property Value

COOutputType

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

COChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_prescaler.htm language=enus -->
## TOPIC 00752: COChannelPrescaler Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_prescaler.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_prescaler.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

COChannel.Prescaler Property

### COChannelPrescaler Property

Specifies the divisor to apply to the signal you connect to the counter source terminal. Pulse generations defined by frequency or time take this setting into account, but pulse generations defined by ticks do not. You should use a prescaler only when you connect an external signal to the counter source terminal and when that signal has a higher frequency than the fastest onboard timebase.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public long Prescaler { get; set; }
```

```text
Public Property Prescaler As Long
	Get
	Set
```

###### Property Value

Int64

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

COChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_pulsedone.htm language=enus -->
## TOPIC 00753: COChannelPulseDone Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_pulsedone.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_pulsedone.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

COChannel.PulseDone Property

### COChannelPulseDone Property

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool PulseDone { get; }
```

```text
Public ReadOnly Property PulseDone As Boolean
	Get
```

###### Property Value

Boolean

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

COChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_pulsedutycycle.htm language=enus -->
## TOPIC 00754: COChannelPulseDutyCycle Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_pulsedutycycle.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_pulsedutycycle.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

COChannel.PulseDutyCycle Property

### COChannelPulseDutyCycle Property

Specifies the duty cycle of the pulses. The duty cycle of a signal is the width of the pulse divided by period. NI-DAQmx uses this ratio and the pulse frequency to determine the width of the pulses and the delay between pulses.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double PulseDutyCycle { get; set; }
```

```text
Public Property PulseDutyCycle As Double
	Get
	Set
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

COChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_pulsefrequency.htm language=enus -->
## TOPIC 00755: COChannelPulseFrequency Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_pulsefrequency.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_pulsefrequency.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

COChannel.PulseFrequency Property

### COChannelPulseFrequency Property

PulseFrequencyUnits

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double PulseFrequency { get; set; }
```

```text
Public Property PulseFrequency As Double
	Get
	Set
```

###### Property Value

Double

PulseFrequencyUnits

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

COChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_pulsefrequencyinitialdelay.htm language=enus -->
## TOPIC 00756: COChannelPulseFrequencyInitialDelay Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_pulsefrequencyinitialdelay.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_pulsefrequencyinitialdelay.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

COChannel.PulseFrequencyInitialDelay Property

### COChannelPulseFrequencyInitialDelay Property

Specifies in seconds the amount of time to wait before generating the first pulse.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double PulseFrequencyInitialDelay { get; set; }
```

```text
Public Property PulseFrequencyInitialDelay As Double
	Get
	Set
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

COChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_pulselowticks.htm language=enus -->
## TOPIC 00757: COChannelPulseLowTicks Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_pulselowticks.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_pulselowticks.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

COChannel.PulseLowTicks Property

### COChannelPulseLowTicks Property

Specifies the number of ticks the pulse is low.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public long PulseLowTicks { get; set; }
```

```text
Public Property PulseLowTicks As Long
	Get
	Set
```

###### Property Value

Int64

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

COChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_pulselowtime.htm language=enus -->
## TOPIC 00758: COChannelPulseLowTime Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_pulselowtime.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_pulselowtime.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

COChannel.PulseLowTime Property

### COChannelPulseLowTime Property

PulseTimeUnits

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double PulseLowTime { get; set; }
```

```text
Public Property PulseLowTime As Double
	Get
	Set
```

###### Property Value

Double

PulseTimeUnits

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

COChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_pulseterminal.htm language=enus -->
## TOPIC 00759: COChannelPulseTerminal Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_pulseterminal.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_pulseterminal.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

COChannel.PulseTerminal Property

### COChannelPulseTerminal Property

terminal

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string PulseTerminal { get; set; }
```

```text
Public Property PulseTerminal As String
	Get
	Set
```

###### Property Value

String

terminal

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

COChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_pulseticksinitialdelay.htm language=enus -->
## TOPIC 00760: COChannelPulseTicksInitialDelay Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_pulseticksinitialdelay.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_pulseticksinitialdelay.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

COChannel.PulseTicksInitialDelay Property

### COChannelPulseTicksInitialDelay Property

Specifies the number of ticks to wait before generating the first pulse.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public long PulseTicksInitialDelay { get; set; }
```

```text
Public Property PulseTicksInitialDelay As Long
	Get
	Set
```

###### Property Value

Int64

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

COChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_pulsetimeinitialdelay.htm language=enus -->
## TOPIC 00761: COChannelPulseTimeInitialDelay Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_pulsetimeinitialdelay.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_pulsetimeinitialdelay.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

COChannel.PulseTimeInitialDelay Property

### COChannelPulseTimeInitialDelay Property

Specifies in seconds the amount of time to wait before generating the first pulse.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double PulseTimeInitialDelay { get; set; }
```

```text
Public Property PulseTimeInitialDelay As Double
	Get
	Set
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

COChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_pulsetimeunits.htm language=enus -->
## TOPIC 00762: COChannelPulseTimeUnits Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_pulsetimeunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_cochannel_pulsetimeunits.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

COChannel.PulseTimeUnits Property

### COChannelPulseTimeUnits Property

Specifies the units in which to define high and low pulse time.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public COPulseTimeUnits PulseTimeUnits { get; set; }
```

```text
Public Property PulseTimeUnits As COPulseTimeUnits
	Get
	Set
```

###### Property Value

COPulseTimeUnits

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

COChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_buffer.htm language=enus -->
## TOPIC 00763: DaqStreamBuffer Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_buffer.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_buffer.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream.Buffer Property

### DaqStreamBuffer Property

buffer

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public DaqBuffer Buffer { get; }
```

```text
Public ReadOnly Property Buffer As DaqBuffer
	Get
```

###### Property Value

DaqBuffer

DaqBuffer

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_channelstoread.htm language=enus -->
## TOPIC 00764: DaqStreamChannelsToRead Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_channelstoread.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_channelstoread.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream.ChannelsToRead Property

### DaqStreamChannelsToRead Property

Sets a subset of channels in the task from which to read.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string ChannelsToRead { get; set; }
```

```text
Public Property ChannelsToRead As String
	Get
	Set
```

###### Property Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_loggingfilepath.htm language=enus -->
## TOPIC 00765: DaqStreamLoggingFilePath Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_loggingfilepath.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_loggingfilepath.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream.LoggingFilePath Property

### DaqStreamLoggingFilePath Property

log

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string LoggingFilePath { get; set; }
```

```text
Public Property LoggingFilePath As String
	Get
	Set
```

###### Property Value

String

log

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_readopencurrentloopchannels.htm language=enus -->
## TOPIC 00766: DaqStreamReadOpenCurrentLoopChannels Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_readopencurrentloopchannels.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_readopencurrentloopchannels.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream.ReadOpenCurrentLoopChannels Property

### DaqStreamReadOpenCurrentLoopChannels Property

list of names

open current loop

ReadOpenCurrentLoopChannelsExist

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string[] ReadOpenCurrentLoopChannels { get; }
```

```text
Public ReadOnly Property ReadOpenCurrentLoopChannels As String()
	Get
```

###### Property Value

String

list of names

open current loop

ReadOpenCurrentLoopChannelsExist

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_readovercurrentchannels.htm language=enus -->
## TOPIC 00767: DaqStreamReadOvercurrentChannels Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_readovercurrentchannels.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_readovercurrentchannels.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream.ReadOvercurrentChannels Property

### DaqStreamReadOvercurrentChannels Property

list of names

overcurrent condition

ReadOvercurrentChannelsExist

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string[] ReadOvercurrentChannels { get; }
```

```text
Public ReadOnly Property ReadOvercurrentChannels As String()
	Get
```

###### Property Value

String

list of names

overcurrent condition

ReadOvercurrentChannelsExist

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_readovercurrentchannelsexist.htm language=enus -->
## TOPIC 00768: DaqStreamReadOvercurrentChannelsExist Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_readovercurrentchannelsexist.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_readovercurrentchannelsexist.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream.ReadOvercurrentChannelsExist Property

### DaqStreamReadOvercurrentChannelsExist Property

overcurrent condition

ReadOvercurrentChannels

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool ReadOvercurrentChannelsExist { get; }
```

```text
Public ReadOnly Property ReadOvercurrentChannelsExist As Boolean
	Get
```

###### Property Value

Boolean

overcurrent condition

ReadOvercurrentChannels

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_readovertemperaturechannels.htm language=enus -->
## TOPIC 00769: DaqStreamReadOvertemperatureChannels Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_readovertemperaturechannels.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_readovertemperaturechannels.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream.ReadOvertemperatureChannels Property

### DaqStreamReadOvertemperatureChannels Property

ReadOvertemperatureChannelsExist

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string[] ReadOvertemperatureChannels { get; }
```

```text
Public ReadOnly Property ReadOvertemperatureChannels As String()
	Get
```

###### Property Value

String

ReadOvertemperatureChannelsExist

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_readsynchronizationunlockedchannels.htm language=enus -->
## TOPIC 00770: DaqStreamReadSynchronizationUnlockedChannels Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_readsynchronizationunlockedchannels.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_readsynchronizationunlockedchannels.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream.ReadSynchronizationUnlockedChannels Property

### DaqStreamReadSynchronizationUnlockedChannels Property

Indicates the channels from devices in an unlocked target.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string[] ReadSynchronizationUnlockedChannels { get; }
```

```text
Public ReadOnly Property ReadSynchronizationUnlockedChannels As String()
	Get
```

###### Property Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_readsynchronizationunlockedchannelsexist.htm language=enus -->
## TOPIC 00771: DaqStreamReadSynchronizationUnlockedChannelsExist Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_readsynchronizationunlockedchannelsexist.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_readsynchronizationunlockedchannelsexist.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream.ReadSynchronizationUnlockedChannelsExist Property

### DaqStreamReadSynchronizationUnlockedChannelsExist Property

Indicates whether the target is currently locked to the grand master. Devices may report PLL Unlock either during acquisition or after acquisition.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool ReadSynchronizationUnlockedChannelsExist { get; }
```

```text
Public ReadOnly Property ReadSynchronizationUnlockedChannelsExist As Boolean
	Get
```

###### Property Value

Boolean

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_totalsamplesgeneratedperchannel.htm language=enus -->
## TOPIC 00772: DaqStreamTotalSamplesGeneratedPerChannel Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_totalsamplesgeneratedperchannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_totalsamplesgeneratedperchannel.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream.TotalSamplesGeneratedPerChannel Property

### DaqStreamTotalSamplesGeneratedPerChannel Property

Indicates the total number of samples generated by each channel in the task. This value is identical for all channels in the task.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public long TotalSamplesGeneratedPerChannel { get; }
```

```text
Public ReadOnly Property TotalSamplesGeneratedPerChannel As Long
	Get
```

###### Property Value

Int64

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_writeexternalovervoltagechannels.htm language=enus -->
## TOPIC 00773: DaqStreamWriteExternalOvervoltageChannels Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_writeexternalovervoltagechannels.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_writeexternalovervoltagechannels.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream.WriteExternalOvervoltageChannels Property

### DaqStreamWriteExternalOvervoltageChannels Property

Indicates a list of names of any virtual channels in the task for which an External Overvoltage condition has been detected. You must read External OvervoltageChansExist before you read this property. Otherwise, you will receive an error.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string[] WriteExternalOvervoltageChannels { get; }
```

```text
Public ReadOnly Property WriteExternalOvervoltageChannels As String()
	Get
```

###### Property Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_writeoffset.htm language=enus -->
## TOPIC 00774: DaqStreamWriteOffset Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_writeoffset.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_writeoffset.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream.WriteOffset Property

### DaqStreamWriteOffset Property

WriteRelativeTo

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public int WriteOffset { get; set; }
```

```text
Public Property WriteOffset As Integer
	Get
	Set
```

###### Property Value

Int32

WriteRelativeTo

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_writeovertemperaturechannels.htm language=enus -->
## TOPIC 00775: DaqStreamWriteOvertemperatureChannels Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_writeovertemperaturechannels.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_writeovertemperaturechannels.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream.WriteOvertemperatureChannels Property

### DaqStreamWriteOvertemperatureChannels Property

WriteOvertemperatureChannelsExist

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string[] WriteOvertemperatureChannels { get; }
```

```text
Public ReadOnly Property WriteOvertemperatureChannels As String()
	Get
```

###### Property Value

String

WriteOvertemperatureChannelsExist

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_writeovertemperaturechannelsexist.htm language=enus -->
## TOPIC 00776: DaqStreamWriteOvertemperatureChannelsExist Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_writeovertemperaturechannelsexist.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_writeovertemperaturechannelsexist.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream.WriteOvertemperatureChannelsExist Property

### DaqStreamWriteOvertemperatureChannelsExist Property

WriteOvertemperatureChannels

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool WriteOvertemperatureChannelsExist { get; }
```

```text
Public ReadOnly Property WriteOvertemperatureChannelsExist As Boolean
	Get
```

###### Property Value

Boolean

WriteOvertemperatureChannels

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_writepowersupplyfaultchannelsexist.htm language=enus -->
## TOPIC 00777: DaqStreamWritePowerSupplyFaultChannelsExist Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_writepowersupplyfaultchannelsexist.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_writepowersupplyfaultchannelsexist.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream.WritePowerSupplyFaultChannelsExist Property

### DaqStreamWritePowerSupplyFaultChannelsExist Property

power supply fault

WritePowerSupplyFaultChannels

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool WritePowerSupplyFaultChannelsExist { get; }
```

```text
Public ReadOnly Property WritePowerSupplyFaultChannelsExist As Boolean
	Get
```

###### Property Value

Boolean

power supply fault

WritePowerSupplyFaultChannels

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_writesleeptime.htm language=enus -->
## TOPIC 00778: DaqStreamWriteSleepTime Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_writesleeptime.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_writesleeptime.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream.WriteSleepTime Property

### DaqStreamWriteSleepTime Property

WriteWaitMode

Sleep

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double WriteSleepTime { get; set; }
```

```text
Public Property WriteSleepTime As Double
	Get
	Set
```

###### Property Value

Double

WriteWaitMode

Sleep

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_writesynchronizationunlockedchannels.htm language=enus -->
## TOPIC 00779: DaqStreamWriteSynchronizationUnlockedChannels Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_writesynchronizationunlockedchannels.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_writesynchronizationunlockedchannels.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream.WriteSynchronizationUnlockedChannels Property

### DaqStreamWriteSynchronizationUnlockedChannels Property

Indicates the channels from devices in an unlocked target.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string[] WriteSynchronizationUnlockedChannels { get; }
```

```text
Public ReadOnly Property WriteSynchronizationUnlockedChannels As String()
	Get
```

###### Property Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_writesynchronizationunlockedchannelsexist.htm language=enus -->
## TOPIC 00780: DaqStreamWriteSynchronizationUnlockedChannelsExist Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_writesynchronizationunlockedchannelsexist.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_writesynchronizationunlockedchannelsexist.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream.WriteSynchronizationUnlockedChannelsExist Property

### DaqStreamWriteSynchronizationUnlockedChannelsExist Property

Indicates whether the target is currently locked to the grand master. Devices may report PLL Unlock either during acquisition or after acquisition.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool WriteSynchronizationUnlockedChannelsExist { get; }
```

```text
Public ReadOnly Property WriteSynchronizationUnlockedChannelsExist As Boolean
	Get
```

###### Property Value

Boolean

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_writewaitmode.htm language=enus -->
## TOPIC 00781: DaqStreamWriteWaitMode Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_writewaitmode.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqstream_writewaitmode.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream.WriteWaitMode Property

### DaqStreamWriteWaitMode Property

Specifies how writing to the task waits for space to become available in the buffer.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public WriteWaitMode WriteWaitMode { get; set; }
```

```text
Public Property WriteWaitMode As WriteWaitMode
	Get
	Set
```

###### Property Value

WriteWaitMode

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqsystem_devices.htm language=enus -->
## TOPIC 00782: DaqSystemDevices Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqsystem_devices.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqsystem_devices.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.Devices Property

### DaqSystemDevices Property

Indicates the names of all devices installed in the system.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string[] Devices { get; }
```

```text
Public ReadOnly Property Devices As String()
	Get
```

###### Property Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

DaqSystem Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqsystem_drivermajorversion.htm language=enus -->
## TOPIC 00783: DaqSystemDriverMajorVersion Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqsystem_drivermajorversion.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqsystem_drivermajorversion.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.DriverMajorVersion Property

### DaqSystemDriverMajorVersion Property

Indicates the major portion of the installed version of NI-DAQmx, such as 7 for version 7.0.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public long DriverMajorVersion { get; }
```

```text
Public ReadOnly Property DriverMajorVersion As Long
	Get
```

###### Property Value

Int64

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqSystem Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqsystem_driverminorversion.htm language=enus -->
## TOPIC 00784: DaqSystemDriverMinorVersion Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqsystem_driverminorversion.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqsystem_driverminorversion.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.DriverMinorVersion Property

### DaqSystemDriverMinorVersion Property

Indicates the minor portion of the installed version of NI-DAQmx, such as 0 for version 7.0.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public long DriverMinorVersion { get; }
```

```text
Public ReadOnly Property DriverMinorVersion As Long
	Get
```

###### Property Value

Int64

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqSystem Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqsystem_driverupdateversion.htm language=enus -->
## TOPIC 00785: DaqSystemDriverUpdateVersion Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqsystem_driverupdateversion.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqsystem_driverupdateversion.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.DriverUpdateVersion Property

### DaqSystemDriverUpdateVersion Property

Indicates the update portion of the installed version of NI-DAQmx, such as 1 for version 9.0.1.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public long DriverUpdateVersion { get; }
```

```text
Public ReadOnly Property DriverUpdateVersion As Long
	Get
```

###### Property Value

Int64

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqSystem Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqsystem_globalchannels.htm language=enus -->
## TOPIC 00786: DaqSystemGlobalChannels Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqsystem_globalchannels.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqsystem_globalchannels.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.GlobalChannels Property

### DaqSystemGlobalChannels Property

Indicates an array that contains the names of all global channels saved on the system.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string[] GlobalChannels { get; }
```

```text
Public ReadOnly Property GlobalChannels As String()
	Get
```

###### Property Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

DaqSystem Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqsystem_isreadorwritelate.htm language=enus -->
## TOPIC 00787: DaqSystemIsReadOrWriteLate Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqsystem_isreadorwritelate.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqsystem_isreadorwritelate.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.IsReadOrWriteLate Property

### DaqSystemIsReadOrWriteLate Property

**Note: This API is now obsolete.**

IsReadOrWriteLate

WaitForNextSampleClock(Double)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("The IsReadOrWriteLate property is deprecated. Please use the Timing.SinglePoint.WaitForNextSampleClock method instead.")]
public bool IsReadOrWriteLate { get; }
```

```text
<ObsoleteAttribute("The IsReadOrWriteLate property is deprecated. Please use the Timing.SinglePoint.WaitForNextSampleClock method instead.")>
Public ReadOnly Property IsReadOrWriteLate As Boolean
	Get
```

###### Property Value

Boolean

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

The value of this property is not meaningful unless reading or writing a task that has [SampleQuantityMode](p_nationalinstruments_daqmx_timing_samplequantitymode.htm) set to
[HardwareTimedSinglePoint](t_nationalinstruments_daqmx_samplequantitymode.htm).

This property returns information only about warnings that occur in the thread from which the property is accessed. This behavior distinguishes warnings that are caused by actions in one thread from warnings that are caused by independent actions that occur at the same time in another thread.

##### See Also

###### Reference

DaqSystem Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqsystem_lastdaqwarning.htm language=enus -->
## TOPIC 00788: DaqSystemLastDaqWarning Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqsystem_lastdaqwarning.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqsystem_lastdaqwarning.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.LastDaqWarning Property

### DaqSystemLastDaqWarning Property

DaqWarningEventArgs

DaqWarning

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public DaqWarningEventArgs LastDaqWarning { get; }
```

```text
Public ReadOnly Property LastDaqWarning As DaqWarningEventArgs
	Get
```

###### Property Value

DaqWarningEventArgs

DaqWarningEventArgs

DaqWarning

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns information only about warnings that occur in the thread from which the property is accessed. This behavior distinguishes warnings that are caused by actions in one thread from warnings that are caused by independent actions that occur at the same time in another thread.

##### See Also

###### Reference

DaqSystem Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqsystem_scales.htm language=enus -->
## TOPIC 00789: DaqSystemScales Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqsystem_scales.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqsystem_scales.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.Scales Property

### DaqSystemScales Property

Indicates an array that contains the names of all custom scales saved on the system.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string[] Scales { get; }
```

```text
Public ReadOnly Property Scales As String()
	Get
```

###### Property Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

DaqSystem Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqsystem_switchrelays.htm language=enus -->
## TOPIC 00790: DaqSystemSwitchRelays Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqsystem_switchrelays.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqsystem_switchrelays.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.SwitchRelays Property

### DaqSystemSwitchRelays Property

**Note: This API is now obsolete.**

switch relay names

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("This property is obsolete.")]
public string[] SwitchRelays { get; }
```

```text
<ObsoleteAttribute("This property is obsolete.")>
Public ReadOnly Property SwitchRelays As String()
	Get
```

###### Property Value

String

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqSystem Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqsystem_switchtopologies.htm language=enus -->
## TOPIC 00791: DaqSystemSwitchTopologies Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqsystem_switchtopologies.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqsystem_switchtopologies.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.SwitchTopologies Property

### DaqSystemSwitchTopologies Property

**Note: This API is now obsolete.**

switch topologies

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("This property is obsolete.")]
public string[] SwitchTopologies { get; }
```

```text
<ObsoleteAttribute("This property is obsolete.")>
Public ReadOnly Property SwitchTopologies As String()
	Get
```

###### Property Value

String

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqSystem Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqwarningeventargs_error.htm language=enus -->
## TOPIC 00792: DaqWarningEventArgsError Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqwarningeventargs_error.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqwarningeventargs_error.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqWarningEventArgs.Error Property

### DaqWarningEventArgsError Property

Gets the NI-DAQmx driver code for the warning that occurred. Zero means no warning occurred.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public int Error { get; }
```

```text
Public ReadOnly Property Error As Integer
	Get
```

###### Property Value

Int32

##### Remarks

NI-DAQmx Driver Error Codes

##### See Also

###### Reference

DaqWarningEventArgs Class

NationalInstruments.DAQmx Namespace

###### Other Resources

NI-DAQmx Driver Error Codes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqwarningeventargs_message.htm language=enus -->
## TOPIC 00793: DaqWarningEventArgsMessage Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqwarningeventargs_message.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_daqwarningeventargs_message.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqWarningEventArgs.Message Property

### DaqWarningEventArgsMessage Property

Gets a message that describes the warning.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string Message { get; }
```

```text
Public ReadOnly Property Message As String
	Get
```

###### Property Value

String

##### See Also

###### Reference

DaqWarningEventArgs Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_accessoryproductnumbers.htm language=enus -->
## TOPIC 00794: DeviceAccessoryProductNumbers Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_accessoryproductnumbers.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_accessoryproductnumbers.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.AccessoryProductNumbers Property

### DeviceAccessoryProductNumbers Property

Indicates the unique hardware identification number for accessories connected to the device. Each array element corresponds to a connector. For example, index 0 corresponds to connector 0. The array contains 0 for each connector with no accessory connected.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public long[] AccessoryProductNumbers { get; }
```

```text
Public ReadOnly Property AccessoryProductNumbers As Long()
	Get
```

###### Property Value

Int64

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aifrequencyranges.htm language=enus -->
## TOPIC 00795: DeviceAIFrequencyRanges Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aifrequencyranges.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aifrequencyranges.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.AIFrequencyRanges Property

### DeviceAIFrequencyRanges Property

Indicates the pairs of frequency input ranges supported by this device. Each pair consists of the low value, followed by the high value.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] AIFrequencyRanges { get; }
```

```text
Public ReadOnly Property AIFrequencyRanges As Double()
	Get
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aigains.htm language=enus -->
## TOPIC 00796: DeviceAIGains Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aigains.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aigains.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.AIGains Property

### DeviceAIGains Property

Indicates the input gain settings supported by this device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] AIGains { get; }
```

```text
Public ReadOnly Property AIGains As Double()
	Get
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aimaximummultichannelrate.htm language=enus -->
## TOPIC 00797: DeviceAIMaximumMultiChannelRate Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aimaximummultichannelrate.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aimaximummultichannelrate.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.AIMaximumMultiChannelRate Property

### DeviceAIMaximumMultiChannelRate Property

AIMaximumSingleChannelRate

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double AIMaximumMultiChannelRate { get; }
```

```text
Public ReadOnly Property AIMaximumMultiChannelRate As Double
	Get
```

###### Property Value

Double

AIMaximumSingleChannelRate

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aimaximumsinglechannelrate.htm language=enus -->
## TOPIC 00798: DeviceAIMaximumSingleChannelRate Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aimaximumsinglechannelrate.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aimaximumsinglechannelrate.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.AIMaximumSingleChannelRate Property

### DeviceAIMaximumSingleChannelRate Property

Indicates the maximum rate for an analog input task if the task contains only a single channel from this device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double AIMaximumSingleChannelRate { get; }
```

```text
Public ReadOnly Property AIMaximumSingleChannelRate As Double
	Get
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_ainumberofsampletimingengines.htm language=enus -->
## TOPIC 00799: DeviceAINumberOfSampleTimingEngines Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_ainumberofsampletimingengines.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_ainumberofsampletimingengines.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.AINumberOfSampleTimingEngines Property

### DeviceAINumberOfSampleTimingEngines Property

Indicates the number of Analog Input sample timing engines supported by the device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public long AINumberOfSampleTimingEngines { get; }
```

```text
Public ReadOnly Property AINumberOfSampleTimingEngines As Long
	Get
```

###### Property Value

Int64

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aiphysicalchannels.htm language=enus -->
## TOPIC 00800: DeviceAIPhysicalChannels Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aiphysicalchannels.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aiphysicalchannels.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.AIPhysicalChannels Property

### DeviceAIPhysicalChannels Property

Indicates an array containing the names of the analog input physical channels available on the device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string[] AIPhysicalChannels { get; }
```

```text
Public ReadOnly Property AIPhysicalChannels As String()
	Get
```

###### Property Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aisimultaneoussamplingsupported.htm language=enus -->
## TOPIC 00801: DeviceAISimultaneousSamplingSupported Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aisimultaneoussamplingsupported.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aisimultaneoussamplingsupported.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.AISimultaneousSamplingSupported Property

### DeviceAISimultaneousSamplingSupported Property

Indicates if the device supports simultaneous sampling.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool AISimultaneousSamplingSupported { get; }
```

```text
Public ReadOnly Property AISimultaneousSamplingSupported As Boolean
	Get
```

###### Property Value

Boolean

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aisupportedmeasurementtypes.htm language=enus -->
## TOPIC 00802: DeviceAISupportedMeasurementTypes Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aisupportedmeasurementtypes.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aisupportedmeasurementtypes.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.AISupportedMeasurementTypes Property

### DeviceAISupportedMeasurementTypes Property

Gets the measurement types supported by the physical channels of the device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIMeasurementType[] AISupportedMeasurementTypes { get; }
```

```text
Public ReadOnly Property AISupportedMeasurementTypes As AIMeasurementType()
	Get
```

###### Property Value

AIMeasurementType

AIMeasurementType

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aitriggerusage.htm language=enus -->
## TOPIC 00803: DeviceAITriggerUsage Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aitriggerusage.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aitriggerusage.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.AITriggerUsage Property

### DeviceAITriggerUsage Property

Indicates the analog input trigger types supported by this device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public TriggerUsageTypes AITriggerUsage { get; }
```

```text
Public ReadOnly Property AITriggerUsage As TriggerUsageTypes
	Get
```

###### Property Value

TriggerUsageTypes

TriggerUsageTypes

Advance

ArmStart

Handshake

None

Pause

Reference

Start

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aivoltageinternalexcitationdiscretevalues.htm language=enus -->
## TOPIC 00804: DeviceAIVoltageInternalExcitationDiscreteValues Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aivoltageinternalexcitationdiscretevalues.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aivoltageinternalexcitationdiscretevalues.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.AIVoltageInternalExcitationDiscreteValues Property

### DeviceAIVoltageInternalExcitationDiscreteValues Property

AIVoltageInternalExcitationRangeValues

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] AIVoltageInternalExcitationDiscreteValues { get; }
```

```text
Public ReadOnly Property AIVoltageInternalExcitationDiscreteValues As Double()
	Get
```

###### Property Value

Double

AIVoltageInternalExcitationRangeValues

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_analogtriggersupported.htm language=enus -->
## TOPIC 00805: DeviceAnalogTriggerSupported Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_analogtriggersupported.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_analogtriggersupported.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.AnalogTriggerSupported Property

### DeviceAnalogTriggerSupported Property

Indicates if the device supports analog triggering.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool AnalogTriggerSupported { get; }
```

```text
Public ReadOnly Property AnalogTriggerSupported As Boolean
	Get
```

###### Property Value

Boolean

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aocurrentranges.htm language=enus -->
## TOPIC 00806: DeviceAOCurrentRanges Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aocurrentranges.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aocurrentranges.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.AOCurrentRanges Property

### DeviceAOCurrentRanges Property

Indicates pairs of output current ranges supported by this device. Each pair consists of the low value, followed by the high value.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] AOCurrentRanges { get; }
```

```text
Public ReadOnly Property AOCurrentRanges As Double()
	Get
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aophysicalchannels.htm language=enus -->
## TOPIC 00807: DeviceAOPhysicalChannels Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aophysicalchannels.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aophysicalchannels.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.AOPhysicalChannels Property

### DeviceAOPhysicalChannels Property

Indicates an array containing the names of the analog output physical channels available on the device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string[] AOPhysicalChannels { get; }
```

```text
Public ReadOnly Property AOPhysicalChannels As String()
	Get
```

###### Property Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aotriggerusage.htm language=enus -->
## TOPIC 00808: DeviceAOTriggerUsage Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aotriggerusage.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_aotriggerusage.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.AOTriggerUsage Property

### DeviceAOTriggerUsage Property

Indicates the analog output trigger types supported by this device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public TriggerUsageTypes AOTriggerUsage { get; }
```

```text
Public ReadOnly Property AOTriggerUsage As TriggerUsageTypes
	Get
```

###### Property Value

TriggerUsageTypes

TriggerUsageTypes

Advance

ArmStart

Handshake

None

Pause

Reference

Start

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_cisupportedmeasurementtypes.htm language=enus -->
## TOPIC 00809: DeviceCISupportedMeasurementTypes Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_cisupportedmeasurementtypes.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_cisupportedmeasurementtypes.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.CISupportedMeasurementTypes Property

### DeviceCISupportedMeasurementTypes Property

Gets the measurement types supported by the physical channels of the device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public CIMeasurementType[] CISupportedMeasurementTypes { get; }
```

```text
Public ReadOnly Property CISupportedMeasurementTypes As CIMeasurementType()
	Get
```

###### Property Value

CIMeasurementType

CIMeasurementType

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_citriggerusage.htm language=enus -->
## TOPIC 00810: DeviceCITriggerUsage Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_citriggerusage.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_citriggerusage.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.CITriggerUsage Property

### DeviceCITriggerUsage Property

Indicates the counter input trigger types supported by this device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public TriggerUsageTypes CITriggerUsage { get; }
```

```text
Public ReadOnly Property CITriggerUsage As TriggerUsageTypes
	Get
```

###### Property Value

TriggerUsageTypes

TriggerUsageTypes

Advance

ArmStart

Handshake

None

Pause

Reference

Start

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_compactdaqchassisdevicename.htm language=enus -->
## TOPIC 00811: DeviceCompactDaqChassisDeviceName Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_compactdaqchassisdevicename.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_compactdaqchassisdevicename.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.CompactDaqChassisDeviceName Property

### DeviceCompactDaqChassisDeviceName Property

Indicates the name of the CompactDAQ chassis that contains this module.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string CompactDaqChassisDeviceName { get; }
```

```text
Public ReadOnly Property CompactDaqChassisDeviceName As String
	Get
```

###### Property Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_fielddaqbankdevicenames.htm language=enus -->
## TOPIC 00812: DeviceFieldDaqBankDeviceNames Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_fielddaqbankdevicenames.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_fielddaqbankdevicenames.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.FieldDaqBankDeviceNames Property

### DeviceFieldDaqBankDeviceNames Property

Indicates an array containing the names of the banks in the FieldDAQ.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string[] FieldDaqBankDeviceNames { get; }
```

```text
Public ReadOnly Property FieldDaqBankDeviceNames As String()
	Get
```

###### Property Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_isselfcalibrationsupported.htm language=enus -->
## TOPIC 00813: DeviceIsSelfCalibrationSupported Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_isselfcalibrationsupported.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_isselfcalibrationsupported.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.IsSelfCalibrationSupported Property

### DeviceIsSelfCalibrationSupported Property

Indicates whether the device supports self-calibration.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool IsSelfCalibrationSupported { get; }
```

```text
Public ReadOnly Property IsSelfCalibrationSupported As Boolean
	Get
```

###### Property Value

Boolean

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_maxuserdefinedcalibrationinfosize.htm language=enus -->
## TOPIC 00814: DeviceMaxUserDefinedCalibrationInfoSize Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_maxuserdefinedcalibrationinfosize.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_maxuserdefinedcalibrationinfosize.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.MaxUserDefinedCalibrationInfoSize Property

### DeviceMaxUserDefinedCalibrationInfoSize Property

UserDefinedCalibrationInfo

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public long MaxUserDefinedCalibrationInfoSize { get; }
```

```text
Public ReadOnly Property MaxUserDefinedCalibrationInfoSize As Long
	Get
```

###### Property Value

Int64

UserDefinedCalibrationInfo

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_pcidevicenumber.htm language=enus -->
## TOPIC 00815: DevicePciDeviceNumber Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_pcidevicenumber.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_pcidevicenumber.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.PciDeviceNumber Property

### DevicePciDeviceNumber Property

Indicates the PCI slot number of the device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public long PciDeviceNumber { get; }
```

```text
Public ReadOnly Property PciDeviceNumber As Long
	Get
```

###### Property Value

Int64

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_pxichassisnumber.htm language=enus -->
## TOPIC 00816: DevicePxiChassisNumber Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_pxichassisnumber.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_pxichassisnumber.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.PxiChassisNumber Property

### DevicePxiChassisNumber Property

Indicates the PXI chassis number of the device, as identified in MAX.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public long PxiChassisNumber { get; }
```

```text
Public ReadOnly Property PxiChassisNumber As Long
	Get
```

###### Property Value

Int64

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_pxislotnumber.htm language=enus -->
## TOPIC 00817: DevicePxiSlotNumber Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_pxislotnumber.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_pxislotnumber.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.PxiSlotNumber Property

### DevicePxiSlotNumber Property

Indicates the PXI slot number of the device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public long PxiSlotNumber { get; }
```

```text
Public ReadOnly Property PxiSlotNumber As Long
	Get
```

###### Property Value

Int64

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_recommendedaccessoryconnectioncountlimit.htm language=enus -->
## TOPIC 00818: DeviceRecommendedAccessoryConnectionCountLimit Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_recommendedaccessoryconnectioncountlimit.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_recommendedaccessoryconnectioncountlimit.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.RecommendedAccessoryConnectionCountLimit Property

### DeviceRecommendedAccessoryConnectionCountLimit Property

Indicates the recommended connection count limit for an accessory. If the accessory connection count exceeds this limit, the accessory could require maintenance.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public long RecommendedAccessoryConnectionCountLimit { get; }
```

```text
Public ReadOnly Property RecommendedAccessoryConnectionCountLimit As Long
	Get
```

###### Property Value

Int64

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_selfcalibrationdatetime.htm language=enus -->
## TOPIC 00819: DeviceSelfCalibrationDateTime Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_selfcalibrationdatetime.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_selfcalibrationdatetime.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.SelfCalibrationDateTime Property

### DeviceSelfCalibrationDateTime Property

Gets the last date and time that the device underwent a self-calibration.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public DateTime SelfCalibrationDateTime { get; }
```

```text
Public ReadOnly Property SelfCalibrationDateTime As DateTime
	Get
```

###### Property Value

DateTime

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_selfcalibrationtemperature.htm language=enus -->
## TOPIC 00820: DeviceSelfCalibrationTemperature Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_selfcalibrationtemperature.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_selfcalibrationtemperature.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.SelfCalibrationTemperature Property

### DeviceSelfCalibrationTemperature Property

Indicates in degrees Celsius the temperature of the device at the time of the last self-calibration. Compare this temperature to the current onboard temperature to determine if you should perform another calibration.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double SelfCalibrationTemperature { get; }
```

```text
Public ReadOnly Property SelfCalibrationTemperature As Double
	Get
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

The temperature returned by this property is the calibration temperature as measured by an onboard temperature sensor and may differ from the temperature displayed 
on a printed calibration certificate. Calibration certificates usually display the ambient temperature rather than the onboard 
temperature.

Using Traditional NI-DAQ (Legacy) to perform calibration does not update this property. This property is updated only when you use NI-DAQmx 
to perform calibration.

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_serialnumber.htm language=enus -->
## TOPIC 00821: DeviceSerialNumber Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_serialnumber.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_serialnumber.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.SerialNumber Property

### DeviceSerialNumber Property

Indicates the serial number of the device. This value is zero if the device does not have a serial number.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public long SerialNumber { get; }
```

```text
Public ReadOnly Property SerialNumber As Long
	Get
```

###### Property Value

Int64

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_switch.htm language=enus -->
## TOPIC 00822: DeviceSwitch Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_switch.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_switch.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.Switch Property

### DeviceSwitch Property

**Note: This API is now obsolete.**

Switch

switch devices

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("This property is obsolete.")]
public Switch Switch { get; }
```

```text
<ObsoleteAttribute("This property is obsolete.")>
Public ReadOnly Property Switch As Switch
	Get
```

###### Property Value

Switch

Switch

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_tcpipethernetip.htm language=enus -->
## TOPIC 00823: DeviceTcpipEthernetIP Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_tcpipethernetip.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_device_tcpipethernetip.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.TcpipEthernetIP Property

### DeviceTcpipEthernetIP Property

Indicates the IPv4 address of the Ethernet interface in dotted decimal format. This property returns 0.0.0.0 if the Ethernet interface cannot acquire an address.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string TcpipEthernetIP { get; }
```

```text
Public ReadOnly Property TcpipEthernetIP As String
	Get
```

###### Property Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_dichannel_digitalfilterenablebusmode.htm language=enus -->
## TOPIC 00824: DIChannelDigitalFilterEnableBusMode Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_dichannel_digitalfilterenablebusmode.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_dichannel_digitalfilterenablebusmode.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DIChannel.DigitalFilterEnableBusMode Property

### DIChannelDigitalFilterEnableBusMode Property

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool DigitalFilterEnableBusMode { get; set; }
```

```text
Public Property DigitalFilterEnableBusMode As Boolean
	Get
	Set
```

###### Property Value

Boolean

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_dichannel_digitalfiltertimebaserate.htm language=enus -->
## TOPIC 00825: DIChannelDigitalFilterTimebaseRate Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_dichannel_digitalfiltertimebaserate.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_dichannel_digitalfiltertimebaserate.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DIChannel.DigitalFilterTimebaseRate Property

### DIChannelDigitalFilterTimebaseRate Property

Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double DigitalFilterTimebaseRate { get; set; }
```

```text
Public Property DigitalFilterTimebaseRate As Double
	Get
	Set
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_dichannel_tristate.htm language=enus -->
## TOPIC 00826: DIChannelTristate Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_dichannel_tristate.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_dichannel_tristate.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DIChannel.Tristate Property

### DIChannelTristate Property

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool Tristate { get; set; }
```

```text
Public Property Tristate As Boolean
	Get
	Set
```

###### Property Value

Boolean

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_dichannel_usbtransferrequestsize.htm language=enus -->
## TOPIC 00827: DIChannelUsbTransferRequestSize Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_dichannel_usbtransferrequestsize.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_dichannel_usbtransferrequestsize.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DIChannel.UsbTransferRequestSize Property

### DIChannelUsbTransferRequestSize Property

Specifies the maximum size of a USB transfer request in bytes. Modify this value to affect performance under different combinations of operating system and device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public long UsbTransferRequestSize { get; set; }
```

```text
Public Property UsbTransferRequestSize As Long
	Get
	Set
```

###### Property Value

Int64

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_digitaledgeadvancetrigger_digitalfilterenable.htm language=enus -->
## TOPIC 00828: DigitalEdgeAdvanceTriggerDigitalFilterEnable Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_digitaledgeadvancetrigger_digitalfilterenable.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_digitaledgeadvancetrigger_digitalfilterenable.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalEdgeAdvanceTrigger.DigitalFilterEnable Property

### DigitalEdgeAdvanceTriggerDigitalFilterEnable Property

**Note: This API is now obsolete.**

(Deprecated) Specifies whether to apply the pulse width filter to the signal.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("This property is obsolete.")]
public bool DigitalFilterEnable { get; set; }
```

```text
<ObsoleteAttribute("This property is obsolete.")>
Public Property DigitalFilterEnable As Boolean
	Get
	Set
```

###### Property Value

Boolean

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DigitalEdgeAdvanceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_digitaledgearmstarttrigger_digitalfilterminimumpulsewidth.htm language=enus -->
## TOPIC 00829: DigitalEdgeArmStartTriggerDigitalFilterMinimumPulseWidth Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_digitaledgearmstarttrigger_digitalfilterminimumpulsewidth.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_digitaledgearmstarttrigger_digitalfilterminimumpulsewidth.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalEdgeArmStartTrigger.DigitalFilterMinimumPulseWidth Property

### DigitalEdgeArmStartTriggerDigitalFilterMinimumPulseWidth Property

filter

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double DigitalFilterMinimumPulseWidth { get; set; }
```

```text
Public Property DigitalFilterMinimumPulseWidth As Double
	Get
	Set
```

###### Property Value

Double

filter

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DigitalEdgeArmStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_digitaledgearmstarttrigger_edge.htm language=enus -->
## TOPIC 00830: DigitalEdgeArmStartTriggerEdge Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_digitaledgearmstarttrigger_edge.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_digitaledgearmstarttrigger_edge.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalEdgeArmStartTrigger.Edge Property

### DigitalEdgeArmStartTriggerEdge Property

Specifies on which edge of a digital signal to arm the task for a Start Trigger.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public DigitalEdgeArmStartTriggerEdge Edge { get; set; }
```

```text
Public Property Edge As DigitalEdgeArmStartTriggerEdge
	Get
	Set
```

###### Property Value

DigitalEdgeArmStartTriggerEdge

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DigitalEdgeArmStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_digitaledgearmstarttrigger_source.htm language=enus -->
## TOPIC 00831: DigitalEdgeArmStartTriggerSource Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_digitaledgearmstarttrigger_source.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_digitaledgearmstarttrigger_source.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalEdgeArmStartTrigger.Source Property

### DigitalEdgeArmStartTriggerSource Property

terminal

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string Source { get; set; }
```

```text
Public Property Source As String
	Get
	Set
```

###### Property Value

String

terminal

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DigitalEdgeArmStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_digitaledgereferencetrigger_digitalsynchronizationenable.htm language=enus -->
## TOPIC 00832: DigitalEdgeReferenceTriggerDigitalSynchronizationEnable Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_digitaledgereferencetrigger_digitalsynchronizationenable.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_digitaledgereferencetrigger_digitalsynchronizationenable.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalEdgeReferenceTrigger.DigitalSynchronizationEnable Property

### DigitalEdgeReferenceTriggerDigitalSynchronizationEnable Property

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool DigitalSynchronizationEnable { get; set; }
```

```text
Public Property DigitalSynchronizationEnable As Boolean
	Get
	Set
```

###### Property Value

Boolean

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DigitalEdgeReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_digitaledgereferencetrigger_source.htm language=enus -->
## TOPIC 00833: DigitalEdgeReferenceTriggerSource Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_digitaledgereferencetrigger_source.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_digitaledgereferencetrigger_source.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalEdgeReferenceTrigger.Source Property

### DigitalEdgeReferenceTriggerSource Property

terminal

Reference Trigger

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string Source { get; set; }
```

```text
Public Property Source As String
	Get
	Set
```

###### Property Value

String

terminal

Reference Trigger

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DigitalEdgeReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_digitaledgestarttrigger_digitalfiltertimebaserate.htm language=enus -->
## TOPIC 00834: DigitalEdgeStartTriggerDigitalFilterTimebaseRate Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_digitaledgestarttrigger_digitalfiltertimebaserate.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_digitaledgestarttrigger_digitalfiltertimebaserate.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalEdgeStartTrigger.DigitalFilterTimebaseRate Property

### DigitalEdgeStartTriggerDigitalFilterTimebaseRate Property

Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double DigitalFilterTimebaseRate { get; set; }
```

```text
Public Property DigitalFilterTimebaseRate As Double
	Get
	Set
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DigitalEdgeStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_digitalsinglechannelwriter_synchronizecallbacks.htm language=enus -->
## TOPIC 00835: DigitalSingleChannelWriterSynchronizeCallbacks Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_digitalsinglechannelwriter_synchronizecallbacks.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_digitalsinglechannelwriter_synchronizecallbacks.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelWriter.SynchronizeCallbacks Property

### DigitalSingleChannelWriterSynchronizeCallbacks Property

Specifies how events and callback delegates are invoked.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public virtual bool SynchronizeCallbacks { get; set; }
```

```text
Public Overridable Property SynchronizeCallbacks As Boolean
	Get
	Set
```

###### Property Value

Boolean

Send(SendOrPostCallback, Object)

Post(SendOrPostCallback, Object)

###### Implements

##### Remarks

In some cases, callbacks and event handlers are executed in a different thread than the rest of the program. 
Therefore, you must take special care when accessing objects that have thread affinity, such as UI controls, 
from these callbacks and event handlers. For more information, refer to 
Events, Callbacks, and Thread Safety in Measurement Studio .NET Class Libraries.

##### See Also

###### Reference

DigitalSingleChannelWriter Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Reading and Writing with NI-DAQmx Streams

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_dochannel_linestatesdonestate.htm language=enus -->
## TOPIC 00836: DOChannelLineStatesDoneState Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_dochannel_linestatesdonestate.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_dochannel_linestatesdonestate.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DOChannel.LineStatesDoneState Property

### DOChannelLineStatesDoneState Property

completes execution

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public DOLineStatesDoneState LineStatesDoneState { get; set; }
```

```text
Public Property LineStatesDoneState As DOLineStatesDoneState
	Get
	Set
```

###### Property Value

DOLineStatesDoneState

completes execution

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DOChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_dochannelcollection_count.htm language=enus -->
## TOPIC 00837: DOChannelCollectionCount Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_dochannelcollection_count.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_dochannelcollection_count.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DOChannelCollection.Count Property

### DOChannelCollectionCount Property

Gets the number of elements in the collection.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public virtual int Count { get; }
```

```text
Public Overridable ReadOnly Property Count As Integer
	Get
```

###### Property Value

Int32

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DOChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_dochannelcollection_item.htm language=enus -->
## TOPIC 00838: DOChannelCollectionItem Property (Int64)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_dochannelcollection_item.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_dochannelcollection_item.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DOChannelCollection.Item Property (Int64)

### DOChannelCollectionItem Property (Int64)

DOChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public virtual DOChannel this[
	long index
] { get; }
```

```text
Public Overridable ReadOnly Default Property Item ( 
	index As Long
) As DOChannel
	Get
```

###### Parameters

- **index**
  - Type: SystemInt64The zero-based index of the entry to locate in the collection.

###### Property Value

DOChannel

DOChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DOChannelCollection Class

Item Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Channels

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_everynsampleswritteneventargs_error.htm language=enus -->
## TOPIC 00839: EveryNSamplesWrittenEventArgsError Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_everynsampleswritteneventargs_error.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_everynsampleswritteneventargs_error.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

EveryNSamplesWrittenEventArgs.Error Property

### EveryNSamplesWrittenEventArgsError Property

Exception

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public Exception Error { get; }
```

```text
Public ReadOnly Property Error As Exception
	Get
```

###### Property Value

Exception

Exception

##### Remarks

##### See Also

###### Reference

EveryNSamplesWrittenEventArgs Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_exportsignals_advancecompleteeventdelay.htm language=enus -->
## TOPIC 00840: ExportSignalsAdvanceCompleteEventDelay Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_exportsignals_advancecompleteeventdelay.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_exportsignals_advancecompleteeventdelay.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExportSignals.AdvanceCompleteEventDelay Property

### ExportSignalsAdvanceCompleteEventDelay Property

Specifies the output signal delay in periods of the sample clock.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double AdvanceCompleteEventDelay { get; set; }
```

```text
Public Property AdvanceCompleteEventDelay As Double
	Get
	Set
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

ExportSignals Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_exportsignals_advancetriggerpulsewidthunits.htm language=enus -->
## TOPIC 00841: ExportSignalsAdvanceTriggerPulseWidthUnits Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_exportsignals_advancetriggerpulsewidthunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_exportsignals_advancetriggerpulsewidthunits.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ExportSignals.AdvanceTriggerPulseWidthUnits Property

### ExportSignalsAdvanceTriggerPulseWidthUnits Property

AdvanceTriggerPulseWidth

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AdvanceTriggerPulseWidthUnits AdvanceTriggerPulseWidthUnits { get; set; }
```

```text
Public Property AdvanceTriggerPulseWidthUnits As AdvanceTriggerPulseWidthUnits
	Get
	Set
```

###### Property Value

AdvanceTriggerPulseWidthUnits

AdvanceTriggerPulseWidth

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

ExportSignals Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_referencetrigger_type.htm language=enus -->
## TOPIC 00842: ReferenceTriggerType Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_referencetrigger_type.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_referencetrigger_type.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ReferenceTrigger.Type Property

### ReferenceTriggerType Property

type

reference

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public ReferenceTriggerType Type { get; set; }
```

```text
Public Property Type As ReferenceTriggerType
	Get
	Set
```

###### Property Value

ReferenceTriggerType

type

reference

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

ReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_savedscaleinfo_allowinteractivedeletion.htm language=enus -->
## TOPIC 00843: SavedScaleInfoAllowInteractiveDeletion Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_savedscaleinfo_allowinteractivedeletion.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_savedscaleinfo_allowinteractivedeletion.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SavedScaleInfo.AllowInteractiveDeletion Property

### SavedScaleInfoAllowInteractiveDeletion Property

Indicates whether the custom scale can be deleted through MAX.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool AllowInteractiveDeletion { get; }
```

```text
Public ReadOnly Property AllowInteractiveDeletion As Boolean
	Get
```

###### Property Value

Boolean

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

SavedScaleInfo Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_savedtaskinfo_name.htm language=enus -->
## TOPIC 00844: SavedTaskInfoName Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_savedtaskinfo_name.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_savedtaskinfo_name.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SavedTaskInfo.Name Property

### SavedTaskInfoName Property

Gets the name of the task.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string Name { get; }
```

```text
Public ReadOnly Property Name As String
	Get
```

###### Property Value

String

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

SavedTaskInfo Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_scale_description.htm language=enus -->
## TOPIC 00845: ScaleDescription Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_scale_description.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_scale_description.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Scale.Description Property

### ScaleDescription Property

Specifies a description for the scale.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string Description { get; set; }
```

```text
Public Property Description As String
	Get
	Set
```

###### Property Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Scale Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_singlepoint_writerecoverymode.htm language=enus -->
## TOPIC 00846: SinglePointWriteRecoveryMode Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_singlepoint_writerecoverymode.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_singlepoint_writerecoverymode.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SinglePoint.WriteRecoveryMode Property

### SinglePointWriteRecoveryMode Property

Specifies how NI-DAQmx attempts to recover after missing a Sample Clock pulse when performing counter writes.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public WriteRecoveryMode WriteRecoveryMode { get; set; }
```

```text
Public Property WriteRecoveryMode As WriteRecoveryMode
	Get
	Set
```

###### Property Value

WriteRecoveryMode

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

SinglePoint Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_starttrigger_delay.htm language=enus -->
## TOPIC 00847: StartTriggerDelay Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_starttrigger_delay.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_starttrigger_delay.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

StartTrigger.Delay Property

### StartTriggerDelay Property

DelayUnits

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double Delay { get; set; }
```

```text
Public Property Delay As Double
	Get
	Set
```

###### Property Value

Double

DelayUnits

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

StartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_task_accessoryinsertionorremovaldetected.htm language=enus -->
## TOPIC 00848: TaskAccessoryInsertionOrRemovalDetected Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_task_accessoryinsertionorremovaldetected.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_task_accessoryinsertionorremovaldetected.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Task.AccessoryInsertionOrRemovalDetected Property

### TaskAccessoryInsertionOrRemovalDetected Property

DevicesWithInsertedOrRemovedAccessories

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool AccessoryInsertionOrRemovalDetected { get; }
```

```text
Public ReadOnly Property AccessoryInsertionOrRemovalDetected As Boolean
	Get
```

###### Property Value

Boolean

DevicesWithInsertedOrRemovedAccessories

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Task Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_task_aochannels.htm language=enus -->
## TOPIC 00849: TaskAOChannels Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_task_aochannels.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_task_aochannels.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Task.AOChannels Property

### TaskAOChannels Property

Gets the collection of analog output channels in the task.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AOChannelCollection AOChannels { get; }
```

```text
Public ReadOnly Property AOChannels As AOChannelCollection
	Get
```

###### Property Value

AOChannelCollection

AIChannelCollection

AOChannel

##### Remarks

Each task can contain
only one type of channel. You must use the channels property that corresponds to the type of channels in the task to access the channels in the task.

##### See Also

###### Reference

Task Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_task_cichannels.htm language=enus -->
## TOPIC 00850: TaskCIChannels Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_task_cichannels.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_task_cichannels.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Task.CIChannels Property

### TaskCIChannels Property

Gets the collection of counter input channels in the task.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public CIChannelCollection CIChannels { get; }
```

```text
Public ReadOnly Property CIChannels As CIChannelCollection
	Get
```

###### Property Value

CIChannelCollection

CIChannelCollection

CIChannel

##### Remarks

Each task can contain
only one type of channel. You must use the channels property that corresponds to the type of channels in the task to access the channels in the task.

##### See Also

###### Reference

Task Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_task_switchscan.htm language=enus -->
## TOPIC 00851: TaskSwitchScan Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_task_switchscan.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_task_switchscan.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Task.SwitchScan Property

### TaskSwitchScan Property

Gets the switch scan configuration for the task.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public SwitchScan SwitchScan { get; }
```

```text
Public ReadOnly Property SwitchScan As SwitchScan
	Get
```

###### Property Value

SwitchScan

SwitchScan

##### See Also

###### Reference

Task Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_task_synchronizecallbacks.htm language=enus -->
## TOPIC 00852: TaskSynchronizeCallbacks Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_task_synchronizecallbacks.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_task_synchronizecallbacks.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Task.SynchronizeCallbacks Property

### TaskSynchronizeCallbacks Property

Specifies how events and callback delegates are invoked.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public virtual bool SynchronizeCallbacks { get; set; }
```

```text
Public Overridable Property SynchronizeCallbacks As Boolean
	Get
	Set
```

###### Property Value

Boolean

Send(SendOrPostCallback, Object)

Post(SendOrPostCallback, Object)

###### Implements

##### Remarks

In some cases, callbacks and event handlers are executed in a different thread than the rest of the program. 
Therefore, you must take special care when accessing objects that have thread affinity, such as UI controls, 
from these callbacks and event handlers. For more information, refer to 
Events, Callbacks, and Thread Safety in Measurement Studio .NET Class Libraries.

##### See Also

###### Reference

Task Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Reading and Writing with NI-DAQmx Streams

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_timing_aiconvertactiveedge.htm language=enus -->
## TOPIC 00853: TimingAIConvertActiveEdge Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_timing_aiconvertactiveedge.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_timing_aiconvertactiveedge.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.AIConvertActiveEdge Property

### TimingAIConvertActiveEdge Property

Specifies on which edge of the clock pulse an analog-to-digital conversion takes place.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIConvertActiveEdge AIConvertActiveEdge { get; set; }
```

```text
Public Property AIConvertActiveEdge As AIConvertActiveEdge
	Get
	Set
```

###### Property Value

AIConvertActiveEdge

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property is useful primarily when the signal you use as the AI Convert Clock is not a periodic clock. For example, set this property 
to [Rising](t_nationalinstruments_daqmx_aiconvertactiveedge.htm) to perform an analog to digital conversion on each rising edge of an aperiodic signal.

##### See Also

###### Reference

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_timing_referenceclockrate.htm language=enus -->
## TOPIC 00854: TimingReferenceClockRate Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_timing_referenceclockrate.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_timing_referenceclockrate.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.ReferenceClockRate Property

### TimingReferenceClockRate Property

Specifies the frequency of the Reference Clock.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double ReferenceClockRate { get; set; }
```

```text
Public Property ReferenceClockRate As Double
	Get
	Set
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_timing_referenceclocksource.htm language=enus -->
## TOPIC 00855: TimingReferenceClockSource Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_timing_referenceclocksource.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_timing_referenceclocksource.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.ReferenceClockSource Property

### TimingReferenceClockSource Property

terminal

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string ReferenceClockSource { get; set; }
```

```text
Public Property ReferenceClockSource As String
	Get
	Set
```

###### Property Value

String

terminal

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_timing_sampleclockactiveedge.htm language=enus -->
## TOPIC 00856: TimingSampleClockActiveEdge Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_timing_sampleclockactiveedge.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_timing_sampleclockactiveedge.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.SampleClockActiveEdge Property

### TimingSampleClockActiveEdge Property

Specifies on which edge of a clock pulse sampling takes place. This property is useful primarily when the signal you use as the Sample Clock is not a periodic clock.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public SampleClockActiveEdge SampleClockActiveEdge { get; set; }
```

```text
Public Property SampleClockActiveEdge As SampleClockActiveEdge
	Get
	Set
```

###### Property Value

SampleClockActiveEdge

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_timing_sampleclockdigitalfiltertimebasesource.htm language=enus -->
## TOPIC 00857: TimingSampleClockDigitalFilterTimebaseSource Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_timing_sampleclockdigitalfiltertimebasesource.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_timing_sampleclockdigitalfiltertimebasesource.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.SampleClockDigitalFilterTimebaseSource Property

### TimingSampleClockDigitalFilterTimebaseSource Property

terminal

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string SampleClockDigitalFilterTimebaseSource { get; set; }
```

```text
Public Property SampleClockDigitalFilterTimebaseSource As String
	Get
	Set
```

###### Property Value

String

terminal

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_timing_sampleclockdigitalsynchronizationenable.htm language=enus -->
## TOPIC 00858: TimingSampleClockDigitalSynchronizationEnable Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_timing_sampleclockdigitalsynchronizationenable.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_timing_sampleclockdigitalsynchronizationenable.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.SampleClockDigitalSynchronizationEnable Property

### TimingSampleClockDigitalSynchronizationEnable Property

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool SampleClockDigitalSynchronizationEnable { get; set; }
```

```text
Public Property SampleClockDigitalSynchronizationEnable As Boolean
	Get
	Set
```

###### Property Value

Boolean

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property does not affect the minimum pulse width recognized by the device, 
but setting this property to does limit the speed at which the device recognizes transitions 
to less than the frequency of the internal timebase.

##### See Also

###### Reference

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_timing_sampleclockmaximumrate.htm language=enus -->
## TOPIC 00859: TimingSampleClockMaximumRate Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_timing_sampleclockmaximumrate.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_timing_sampleclockmaximumrate.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.SampleClockMaximumRate Property

### TimingSampleClockMaximumRate Property

multiplexed devices than simultaneous sampling devices

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double SampleClockMaximumRate { get; }
```

```text
Public ReadOnly Property SampleClockMaximumRate As Double
	Get
```

###### Property Value

Double

multiplexed devices than simultaneous sampling devices

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

For multiplexed devices, NI-DAQmx calculates the maximum sample clock rate based on the maximum AI Convert Clock rate unless you set [AIConvertRate](p_nationalinstruments_daqmx_timing_aiconvertrate.htm). If you set that property, 
NI-DAQmx calculates the maximum sample clock rate based on that setting. Use [AIConvertMaximumRate](p_nationalinstruments_daqmx_timing_aiconvertmaximumrate.htm) to query the maximum AI Convert Clock rate.
NI-DAQmx also uses the minimum sample clock delay to calculate the maximum sample clock rate unless you set [DelayFromSampleClock](p_nationalinstruments_daqmx_timing_delayfromsampleclock.htm).

For simultaneous sampling devices, the maximum Sample Clock rate is the maximum rate of the ADC.

##### See Also

###### Reference

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_timing_sampleclockoverrunbehavior.htm language=enus -->
## TOPIC 00860: TimingSampleClockOverrunBehavior Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_timing_sampleclockoverrunbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_timing_sampleclockoverrunbehavior.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.SampleClockOverrunBehavior Property

### TimingSampleClockOverrunBehavior Property

Specifies the action to take if Sample Clock edges occur faster than the device can handle them.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public SampleClockOverrunBehavior SampleClockOverrunBehavior { get; set; }
```

```text
Public Property SampleClockOverrunBehavior As SampleClockOverrunBehavior
	Get
	Set
```

###### Property Value

SampleClockOverrunBehavior

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_timing_sampleclockrate.htm language=enus -->
## TOPIC 00861: TimingSampleClockRate Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_timing_sampleclockrate.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_timing_sampleclockrate.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.SampleClockRate Property

### TimingSampleClockRate Property

Specifies the sampling rate in samples per channel per second. If you use an external source for the Sample Clock, set this input to the maximum expected rate of that clock.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double SampleClockRate { get; set; }
```

```text
Public Property SampleClockRate As Double
	Get
	Set
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_timing_sampleclockterminal.htm language=enus -->
## TOPIC 00862: TimingSampleClockTerminal Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_timing_sampleclockterminal.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_timing_sampleclockterminal.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.SampleClockTerminal Property

### TimingSampleClockTerminal Property

SampleClockSource

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string SampleClockTerminal { get; }
```

```text
Public ReadOnly Property SampleClockTerminal As String
	Get
```

###### Property Value

String

SampleClockSource

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_timing_sampleclocktimebaseactiveedge.htm language=enus -->
## TOPIC 00863: TimingSampleClockTimebaseActiveEdge Property

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_timing_sampleclocktimebaseactiveedge.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/p_nationalinstruments_daqmx_timing_sampleclocktimebaseactiveedge.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.SampleClockTimebaseActiveEdge Property

### TimingSampleClockTimebaseActiveEdge Property

Specifies on which edge to recognize a Sample Clock Timebase pulse. This property is useful primarily when the signal you use as the Sample Clock Timebase is not a periodic clock.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public SampleClockTimebaseActiveEdge SampleClockTimebaseActiveEdge { get; set; }
```

```text
Public Property SampleClockTimebaseActiveEdge As SampleClockTimebaseActiveEdge
	Get
	Set
```

###### Property Value

SampleClockTimebaseActiveEdge

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_analogmultiedgestarttrigger.htm language=enus -->
## TOPIC 00864: AnalogMultiEdgeStartTrigger Properties

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_analogmultiedgestarttrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_analogmultiedgestarttrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiEdgeStartTrigger Properties

### AnalogMultiEdgeStartTrigger Properties

The [AnalogMultiEdgeStartTrigger](t_nationalinstruments_daqmx_analogmultiedgestarttrigger.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Couplings | Specifies an array that describes the couplings for the corresponding source signal of the trigger if the source is a terminal rather than a virtual channel. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty. |
|  | Hystereses | Specifies an array of hysteresis levels in the units of the measurement or generation. If the corresponding element of Start.AnlgMultiEdge.Slopes is Rising, the trigger does not deassert until the source signal passes below the corresponding element of Start.AnlgMultiEdge.Lvls minus the hysteresis. If Start.AnlgEdge.Slope is Falling, the trigger does not deassert until the source signal passes above Start.AnlgEdge.Lvl plus the hysteresis. Hysteresis is always enabled. Set this property to a non-zero value to use hysteresis. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty. |
|  | Levels | Specifies an array of thresholds in the units of the measurement or generation to start acquiring or generating samples. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty. |
|  | Slopes | Specifies an array of slopes on which to trigger task to start generating or acquiring samples. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty. |
|  | Sources | Specifies a list and/or range of analog sources that are going to be used for Analog triggering. Each source corresponds to an element in each of the Analog Multi Edge property arrays, if they are not empty. |

Top

##### See Also

###### Reference

AnalogMultiEdgeStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_analogsinglechannelreader.htm language=enus -->
## TOPIC 00865: AnalogSingleChannelReader Properties

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_analogsinglechannelreader.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_analogsinglechannelreader.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogSingleChannelReader Properties

### AnalogSingleChannelReader Properties

The [AnalogSingleChannelReader](t_nationalinstruments_daqmx_analogsinglechannelreader.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |

Top

##### See Also

###### Reference

AnalogSingleChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_analogsinglechannelwriter.htm language=enus -->
## TOPIC 00866: AnalogSingleChannelWriter Properties

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_analogsinglechannelwriter.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_analogsinglechannelwriter.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogSingleChannelWriter Properties

### AnalogSingleChannelWriter Properties

The [AnalogSingleChannelWriter](t_nationalinstruments_daqmx_analogsinglechannelwriter.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |

Top

##### See Also

###### Reference

AnalogSingleChannelWriter Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_analogunscaledreader.htm language=enus -->
## TOPIC 00867: AnalogUnscaledReader Properties

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_analogunscaledreader.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_analogunscaledreader.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogUnscaledReader Properties

### AnalogUnscaledReader Properties

The [AnalogUnscaledReader](t_nationalinstruments_daqmx_analogunscaledreader.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |

Top

##### See Also

###### Reference

AnalogUnscaledReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_analogunscaledwriter.htm language=enus -->
## TOPIC 00868: AnalogUnscaledWriter Properties

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_analogunscaledwriter.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_analogunscaledwriter.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogUnscaledWriter Properties

### AnalogUnscaledWriter Properties

The [AnalogUnscaledWriter](t_nationalinstruments_daqmx_analogunscaledwriter.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |

Top

##### See Also

###### Reference

AnalogUnscaledWriter Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_analogwindowpausetrigger.htm language=enus -->
## TOPIC 00869: AnalogWindowPauseTrigger Properties

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_analogwindowpausetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_analogwindowpausetrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogWindowPauseTrigger Properties

### AnalogWindowPauseTrigger Properties

The [AnalogWindowPauseTrigger](t_nationalinstruments_daqmx_analogwindowpausetrigger.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Condition | Specifies whether the task pauses while the trigger signal is inside or outside the window you specify with WindowBottom and WindowTop. |
|  | Coupling | Specifies the coupling for the source signal of the terminal if the source is a terminal rather than a virtual channel. |
|  | DigitalFilterEnable | Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay within the trigger window for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the window rapidly. |
|  | DigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | DigitalFilterTimebaseRate | Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | DigitalFilterTimebaseSource | Specifies the terminal of the signal to use as the timebase of the digital filter. |
|  | DigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | Source | Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the trigger. |
|  | WindowBottom | Specifies the lower limit of the window. Specify this value in the units of the measurement or generation. |
|  | WindowTop | Specifies the upper limit of the window. Specify this value in the units of the measurement or generation. |

Top

##### See Also

###### Reference

AnalogWindowPauseTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_analogwindowreferencetrigger.htm language=enus -->
## TOPIC 00870: AnalogWindowReferenceTrigger Properties

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_analogwindowreferencetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_analogwindowreferencetrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogWindowReferenceTrigger Properties

### AnalogWindowReferenceTrigger Properties

The [AnalogWindowReferenceTrigger](t_nationalinstruments_daqmx_analogwindowreferencetrigger.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Condition | Specifies whether the Reference Trigger occurs when the source signal enters the window or when it leaves the window. Use WindowBottom and WindowTop to specify the window. |
|  | Coupling | Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel. |
|  | DigitalFilterEnable | Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay within the trigger window for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the window rapidly. |
|  | DigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | DigitalFilterTimebaseRate | Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | DigitalFilterTimebaseSource | Specifies the terminal of the signal to use as the timebase of the digital filter. |
|  | DigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | Source | Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the Reference Trigger. |
|  | WindowBottom | Specifies the lower limit of the window. Specify this value in the units of the measurement. |
|  | WindowTop | Specifies the upper limit of the window. Specify this value in the units of the measurement. |

Top

##### See Also

###### Reference

AnalogWindowReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_analogwindowstarttrigger.htm language=enus -->
## TOPIC 00871: AnalogWindowStartTrigger Properties

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_analogwindowstarttrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_analogwindowstarttrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogWindowStartTrigger Properties

### AnalogWindowStartTrigger Properties

The [AnalogWindowStartTrigger](t_nationalinstruments_daqmx_analogwindowstarttrigger.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Condition | Specifies whether the task starts acquiring or generating samples when the signal enters or leaves the window you specify with WindowBottom and WindowTop. |
|  | Coupling | Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel. |
|  | DigitalFilterEnable | Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay within the trigger window for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the window rapidly. |
|  | DigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | DigitalFilterTimebaseRate | Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | DigitalFilterTimebaseSource | Specifies the terminal of the signal to use as the timebase of the digital filter. |
|  | DigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | Source | Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the Start Trigger. |
|  | WindowBottom | Specifies the lower limit of the window. Specify this value in the units of the measurement or generation. |
|  | WindowTop | Specifies the upper limit of the window. Specify this value in the units of the measurement or generation. |

Top

##### See Also

###### Reference

AnalogWindowStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_aochannel.htm language=enus -->
## TOPIC 00872: AOChannel Properties

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_aochannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_aochannel.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AOChannel Properties

### AOChannel Properties

The [AOChannel](t_nationalinstruments_daqmx_aochannel.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | CommonModeOffset | Specifies the common-mode offset of the AO channel. Use the property only when Terminal Configuration is set to Differential. |
|  | CurrentUnits | Specifies in what units to generate current on the channel. Write data to the channel in the units you select. |
|  | CustomScaleName | Specifies the name of a custom scale for the channel. |
|  | DacAllowConnectReferenceToGround | Specifies whether to allow grounding the internal DAC reference at run time. You must set this property to and set DacReferenceSource to Internal before you can set DacConnectReferenceToGround to . |
|  | DacConnectReferenceToGround | Specifies whether to ground the internal DAC reference. Grounding the internal DAC reference has the effect of grounding all analog output channels and stopping waveform generation across all analog output channels regardless of whether the channels belong to the current task. You can ground the internal DAC reference only when DacReferenceSource is Internal and DacAllowConnectReferenceToGround is . |
|  | DacOffsetExternalSource | Specifies the source of the DAC offset voltage if DacOffsetSource is External. The valid sources for this signal vary by device. |
|  | DacOffsetSource | Specifies the source of the DAC offset voltage. The value of this voltage source determines the full-scale value of the DAC. |
|  | DacOffsetValue | Specifies in volts the value of the DAC offset voltage. To achieve best accuracy, the DAC offset value should be hand calibrated. |
|  | DacRangeHigh | Specifies the upper limit of the output range of the device. This value is in the native units of the device. On E Series devices, for example, the native units is volts. |
|  | DacRangeLow | Specifies the lower limit of the output range of the device. This value is in the native units of the device. On E Series devices, for example, the native units is volts. |
|  | DacReferenceExternalSource | Specifies the source of the DAC reference voltage if DacReferenceSource is External. The valid sources for this signal vary by device. |
|  | DacReferenceSource | Specifies the source of the DAC reference voltage. The value of this voltage source determines the full-scale value of the DAC. |
|  | DacReferenceValue | Specifies in volts the value of the DAC reference voltage. This voltage determines the full-scale range of the DAC. Smaller reference voltages result in smaller ranges, but increased resolution. |
|  | DataTransferMechanism | Specifies the data transfer mode for the device. |
|  | DataTransferRequestCondition | Specifies under what condition to transfer data from the buffer to the onboard memory of the device. |
|  | Description | Specifies a user-defined description for the channel. (Inherited from Channel.) |
|  | DeviceScalingCoefficients | Indicates the coefficients of a linear equation that NI-DAQmx uses to scale values from a voltage to the native format of the device. Each element of the array corresponds to a term of the equation. The first element of the array corresponds to the y-intercept, and the second element corresponds to the slope. Scaling coefficients do not account for any custom scales that may be applied to the channel. |
|  | EnhancedImageRejectionEnable | Specifies whether to enable the DAC interpolation filter. Disable the interpolation filter to improve DAC signal-to-noise ratio at the expense of degraded image rejection. |
|  | FilterDelay | Specifies the amount of time between when the sample is written by the host device and when the sample is output by the DAC. This value is in the units you specify with FilterDelayUnits. |
|  | FilterDelayAdjustment | Specifies an additional amount of time to wait between when the sample is written by the host device and when the sample is output by the DAC. This delay adjustment is in addition to the value indicated by FilterDelay. This delay adjustment is in the units you specify with FilterDelayUnits. |
|  | FilterDelayUnits | Specifies the units of FilterDelay and FilterDelayAdjustment. |
|  | FunctionGenerationAmplitude | Specifies the zero-to-peak amplitude of the waveform to generate in volts. Zero and negative values are valid. |
|  | FunctionGenerationFMDeviation | Specifies the FM deviation in hertz per volt when FunctionGenerationModulationType is FM. |
|  | FunctionGenerationFrequency | Specifies the frequency of the waveform to generate in hertz. |
|  | FunctionGenerationModulationType | Specifies if the device generates a modulated version of the waveform using the original waveform as a carrier and input from an external terminal as the signal. |
|  | FunctionGenerationOffset | Specifies the voltage offset of the waveform to generate. |
|  | FunctionGenerationSquareDutyCycle | Specifies the square wave duty cycle of the waveform to generate. |
|  | FunctionGenerationType | Specifies the kind of the waveform to generate. |
|  | Gain | Specifies in decibels the gain factor to apply to the channel. |
|  | IdleOutputBehavior | Specifies the state of the channel when no generation is in progress. |
|  | IsGlobal | Indicates whether the channel is a global channel. (Inherited from Channel.) |
|  | LoadImpedance | Specifies in ohms the load impedance connected to the analog output channel. |
|  | Maximum | Specifies the maximum value you expect to generate. The value is in the units you specify with a units property. If you try to write a value larger than the maximum value, NI-DAQmx generates an error. NI-DAQmx might coerce this value to a smaller value if other task settings restrict the device from generating the desired maximum. |
|  | MemoryMappingEnable | Specifies for NI-DAQmx to map hardware registers to the memory space of the application, if possible. Normally, NI-DAQmx maps hardware registers to memory accessible only to the kernel. Mapping the registers to the memory space of the application increases performance. However, if the application accesses the memory space mapped to the registers, it can adversely affect the operation of the device and possibly result in a system crash. |
|  | Minimum | Specifies the minimum value you expect to generate. The value is in the units you specify with a units property. If you try to write a value smaller than the minimum value, NI-DAQmx generates an error. NI-DAQmx might coerce this value to a larger value if other task settings restrict the device from generating the desired minimum. |
|  | OutputImpedance | Specifies in ohms the impedance of the analog output stage of the device. |
|  | OutputType | Indicates whether the channel generates voltage, current, or a waveform. |
|  | PhysicalName | Specifies the name of the physical channel upon which this virtual channel is based. (Inherited from Channel.) |
|  | ReglitchEnable | Specifies whether to enable reglitching. The output of a DAC normally glitches whenever the DAC is updated with a new value. The amount of glitching differs from code to code and is generally largest at major code transitions. Reglitching generates uniform glitch energy at each code transition and provides for more uniform glitches. Uniform glitch energy makes it easier to filter out the noise introduced from glitching during spectrum analysis. |
|  | Resolution | Indicates the resolution of the digital-to-analog converter of the channel. This value is in the units you specify with ResolutionUnits. |
|  | ResolutionUnits | Specifies the units of Resolution. |
|  | SynchronizationUnlockBehavior | Specifies the action to take if the target loses its synchronization to the grand master. (Inherited from Channel.) |
|  | TerminalConfiguration | Specifies the terminal configuration of the channel. |
|  | Type | Indicates the type of the virtual channel. (Inherited from Channel.) |
|  | UsbTransferRequestCount | Specifies the maximum number of simultaneous USB transfers used to stream data. Modify this value to affect performance under different combinations of operating system and device. |
|  | UsbTransferRequestSize | Specifies the maximum size of a USB transfer request in bytes. Modify this value to affect performance under different combinations of operating system and device. |
|  | UseOnlyOnBoardMemory | Specifies whether to write samples directly to the onboard memory of the device, bypassing the memory buffer. Generally, you cannot update onboard memory directly after you start the task. Onboard memory includes data FIFOs. |
|  | VirtualName | Gets the name of the virtual channel. (Inherited from Channel.) |
|  | VoltageCurrentLimit | Specifies the current limit, in amperes, for the voltage channel. |
|  | VoltageUnits | Specifies in what units to generate voltage on the channel. Write data to the channel in the units you select. |

Top

##### See Also

###### Reference

AOChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_aochannelcollection.htm language=enus -->
## TOPIC 00873: AOChannelCollection Properties

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_aochannelcollection.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_aochannelcollection.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AOChannelCollection Properties

### AOChannelCollection Properties

The [AOChannelCollection](t_nationalinstruments_daqmx_aochannelcollection.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | All | Gets an AOChannel that operates on all of the channels in the task. |
|  | Count | Gets the number of elements in the collection. |
|  | ItemInt64 | Gets the AOChannel at the specified index. In Visual C#, this property is the indexer. |
|  | ItemString | Gets the AOChannel with the specified virtual channel name. In Visual C#, this property is the indexer. |

Top

##### See Also

###### Reference

AOChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_armstarttrigger.htm language=enus -->
## TOPIC 00874: ArmStartTrigger Properties

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_armstarttrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_armstarttrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ArmStartTrigger Properties

### ArmStartTrigger Properties

The [ArmStartTrigger](t_nationalinstruments_daqmx_armstarttrigger.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | DigitalEdge | Gets the DigitalEdgeArmStartTrigger. |
|  | Terminal | Indicates the name of the internal Arm Start Trigger terminal for the task. This property does not return the name of the trigger source terminal. |
|  | Time | Gets the TimeArmStartTrigger. |
|  | Timestamp | Gets the arm start trigger timestamp. |
|  | TimestampEnable | Specifies whether the arm start trigger timestamp is enabled. If the timestamp is enabled but no resources are available, an error will be returned at run time. |
|  | TimestampTimescale | Specifies the arm start trigger timestamp timescale. |
|  | Type | Specifies the type of trigger to use to arm the task for a Start Trigger. If you configure an Arm Start Trigger, the task does not respond to a Start Trigger until the device receives the Arm Start Trigger. |

Top

##### See Also

###### Reference

ArmStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_channel.htm language=enus -->
## TOPIC 00875: Channel Properties

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_channel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_channel.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Channel Properties

### Channel Properties

The [Channel](t_nationalinstruments_daqmx_channel.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Description | Specifies a user-defined description for the channel. |
|  | IsGlobal | Indicates whether the channel is a global channel. |
|  | PhysicalName | Specifies the name of the physical channel upon which this virtual channel is based. |
|  | SynchronizationUnlockBehavior | Specifies the action to take if the target loses its synchronization to the grand master. |
|  | Type | Indicates the type of the virtual channel. |
|  | VirtualName | Gets the name of the virtual channel. |

Top

##### See Also

###### Reference

Channel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_cichannel.htm language=enus -->
## TOPIC 00876: CIChannel Properties

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_cichannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_cichannel.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannel Properties

### CIChannel Properties

The [CIChannel](t_nationalinstruments_daqmx_cichannel.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | AngularEncoderInitialAngle | Specifies the starting angle of the encoder. This value is in the units you specify with AngularEncoderUnits. |
|  | AngularEncoderPulsesPerRevolution | Specifies the number of pulses the encoder generates per revolution. This value is the number of pulses on either signal A or signal B, not the total number of pulses on both signal A and signal B. |
|  | AngularEncoderUnits | Specifies the units to use to return angular position measurements from the channel. |
|  | Count | Indicates the current value of the count register. |
|  | CountEdgesActiveEdge | Specifies on which edges to increment or decrement the counter. |
|  | CountEdgesCountDirection | Specifies whether to increment or decrement the counter on each edge. |
|  | CountEdgesCountDirectionDigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
|  | CountEdgesCountDirectionDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | CountEdgesCountDirectionDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | CountEdgesCountDirectionDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | CountEdgesCountDirectionDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | CountEdgesCountDirectionHysteresis | Specifies a hysteresis level applied to the CountEdgesCountDirectionThresholdVoltage. The source signal must fall below CountEdgesCountDirectionThresholdVoltage minus the hysteresis before a change in count direction occurs. |
|  | CountEdgesCountDirectionLogicLevelBehavior | Specifies the logic level behavior on the count reset line. |
|  | CountEdgesCountDirectionTerminal | Specifies the source terminal of the digital signal that controls the count direction if CountEdgesCountDirection is ExternallyControlled. |
|  | CountEdgesCountDirectionTerminalConfiguration | Specifies the input terminal configuration. |
|  | CountEdgesCountDirectionThresholdVoltage | Specifies the voltage level applied to the Count Direction terminal. When the signal is above this threshold, the counter counts up. When the signal is below this threshold, the counter counts down. |
|  | CountEdgesCountResetActiveEdge | Specifies on which edge of the signal to reset the count. |
|  | CountEdgesCountResetDigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
|  | CountEdgesCountResetDigitalFilterMinimumPulseWidth | Specifies the minimum pulse width the filter recognizes. |
|  | CountEdgesCountResetDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | CountEdgesCountResetDigitalFilterTimebaseSource | Specifies the input of the signal to use as the timebase of the pulse width filter. |
|  | CountEdgesCountResetDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | CountEdgesCountResetEnable | Specifies whether to reset the count on the active edge specified with CountEdgesCountResetTerminal. |
|  | CountEdgesCountResetHysteresis | Specifies a hysteresis level applied to CountEdgesCountResetThresholdVoltage. When CountEdgesCountResetActiveEdge is rising, the source signal must first fall below CountEdgesCountResetThresholdVoltage minus the hysteresis before a rising edge is detected at CountEdgesCountResetThresholdVoltage. When CountEdgesCountResetActiveEdge is falling, the source signal must first rise above CountEdgesCountResetThresholdVoltage plus the hysteresis before a falling edge is detected at CountEdgesCountResetThresholdVoltage. |
|  | CountEdgesCountResetLogicLevelBehavior | Specifies the logic level behavior on the count reset line. |
|  | CountEdgesCountResetResetCount | Specifies the value to reset the count to. |
|  | CountEdgesCountResetTerminal | Specifies the input terminal of the signal to reset the count. |
|  | CountEdgesCountResetTerminalConfiguration | Specifies the input terminal configuration. |
|  | CountEdgesCountResetThresholdVoltage | Specifies the voltage level at which to recognize the counter reset event. |
|  | CountEdgesDigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
|  | CountEdgesDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | CountEdgesDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | CountEdgesDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | CountEdgesDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | CountEdgesGateDigitalFilterEnable | Specifies whether to apply the pulse width filter to the gate input signal. |
|  | CountEdgesGateDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the digital filter recognizes. |
|  | CountEdgesGateDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | CountEdgesGateDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | CountEdgesGateEnable | Specifies whether to enable the functionality to gate the counter input signal for a count edges measurement. |
|  | CountEdgesGateHysteresis | Specifies a hysteresis level applied to the CountEdgesGateThresholdVoltage. When CountEdgesGatePauseState is High, the source signal must fall below CountEdgesGateThresholdVoltage minus the hysteresis before the counter resumes counting. When CountEdgesGatePauseState is Low, the source signal must rise above CountEdgesGateThresholdVoltage plus the hysteresis before the counter resumes counting. |
|  | CountEdgesGateLogicLevelBehavior | Specifies the logic level behavior on the gate input line. |
|  | CountEdgesGatePauseState | Specifies whether the counter gates input pulses while the signal is high or low. |
|  | CountEdgesGateTerminal | Specifies the gate terminal. |
|  | CountEdgesGateTerminalConfiguration | Specifies the gate terminal configuration. |
|  | CountEdgesGateThresholdVoltage | Specifies the voltage level at which to recognize the counter gate signal. |
|  | CountEdgesHysteresis | Specifies a hysteresis level to apply to CountEdgesThresholdVoltage. When CountEdgesActiveEdge is rising, the source signal must first fall below CountEdgesThresholdVoltage minus the hysteresis before a rising edge is detected at CountEdgesThresholdVoltage. When CountEdgesActiveEdge is falling, the source signal must first rise above CountEdgesThresholdVoltage plus the hysteresis before a falling edge is detected at CountEdgesThresholdVoltage. |
|  | CountEdgesInitialCount | Specifies the starting value from which to count. |
|  | CountEdgesLogicLevelBehavior | Specifies the logic level behavior on the input line. |
|  | CountEdgesTerminal | Specifies the input terminal of the signal to measure. |
|  | CountEdgesTerminalConfiguration | Specifies the input terminal configuration. |
|  | CountEdgesThresholdVoltage | Specifies the voltage level at which to recognize waveform repetitions. Select a voltage level that occurs only once within the entire period of a waveform. You also can select a voltage that occurs only once while the voltage rises or falls. |
|  | CounterTimebaseActiveEdge | Specifies whether a timebase cycle is from rising edge to rising edge or from falling edge to falling edge. |
|  | CounterTimebaseDigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
|  | CounterTimebaseDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | CounterTimebaseDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | CounterTimebaseDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | CounterTimebaseDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | CounterTimebaseMasterTimebaseDivisor | Specifies the divisor for an external counter timebase. You can divide the counter timebase in order to measure slower signals without causing the count register to roll over. |
|  | CounterTimebaseRate | Specifies in Hertz the frequency of the counter timebase. Specifying the rate of a counter timebase allows you to take measurements in terms of time or frequency rather than in ticks of the timebase. If you use an external timebase and do not specify the rate, you can take measurements only in terms of ticks of the timebase. |
|  | CounterTimebaseSource | Specifies the terminal of the timebase to use for the counter. |
|  | CustomScaleName | Specifies the name of a custom scale for the channel. |
|  | DataTransferMechanism | Specifies the data transfer mode for the channel. |
|  | DataTransferRequestCondition | Specifies under what condition to transfer data from the onboard memory of the device to the buffer. |
|  | Description | Specifies a user-defined description for the channel. (Inherited from Channel.) |
|  | DuplicateCountPrevention | Specifies whether to enable duplicate count prevention for the channel. Duplicate count prevention is enabled by default. Setting Prescaler disables duplicate count prevention unless you explicitly enable it. |
|  | DutyCycleDigitalFilterEnabled | Specifies whether to apply the pulse width filter to the signal. |
|  | DutyCycleDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the digital filter recognizes. |
|  | DutyCycleDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | DutyCycleDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | DutyCycleLogicLevelBehavior | Specifies the logic level behavior on the input line. |
|  | DutyCycleStartingEdge | Specifies which edge of the input signal to begin the duty cycle measurement. |
|  | DutyCycleTerminal | Specifies the input terminal of the signal to measure. |
|  | DutyCycleTerminalConfiguration | Specifies the input terminal configuration. |
|  | EncoderAInputDigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
|  | EncoderAInputDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | EncoderAInputDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | EncoderAInputDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | EncoderAInputDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | EncoderAInputLogicLevelBehavior | Specifies the logic level behavior on the input line. |
|  | EncoderAInputTerminal | Specifies the terminal to which signal A is connected. |
|  | EncoderAInputTerminalConfiguration | Specifies the input terminal configuration. |
|  | EncoderBInputDigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
|  | EncoderBInputDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | EncoderBInputDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | EncoderBInputDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | EncoderBInputDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | EncoderBInputLogicLevelBehavior | Specifies the logic level behavior on the input line. |
|  | EncoderBInputTerminal | Specifies the terminal to which signal B is connected. |
|  | EncoderBInputTerminalConfiguration | Specifies the input terminal configuration. |
|  | EncoderDecodingType | Specifies how to count and interpret the pulses the encoder generates on signal A and signal B. X1, X2, and X4 are valid for quadrature encoders only. TwoPulseCounting is valid for two-pulse encoders only. |
|  | EncoderZIndexEnable | Specifies whether to use Z indexing for the channel. |
|  | EncoderZIndexPhase | Specifies the states at which signal A and signal B must be while signal Z is high for NI-DAQmx to reset the measurement. If signal Z is never high while signal A and signal B are high, for example, you must choose a phase other than AHighBHigh. |
|  | EncoderZIndexValue | Specifies the value to which to reset the measurement when signal Z is high and signal A and signal B are at the states you specify with EncoderZIndexPhase. Specify this value in the units of the measurement. |
|  | EncoderZInputDigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
|  | EncoderZInputDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | EncoderZInputDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | EncoderZInputDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | EncoderZInputDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | EncoderZInputLogicLevelBehavior | Specifies the logic level behavior on the input line. |
|  | EncoderZInputTerminal | Specifies the terminal to which signal Z is connected. |
|  | EncoderZInputTerminalConfiguration | Specifies the input terminal configuration. |
|  | FilterDelay | Indicates the amount of time between when the input signal transitions and when the filtered sample is read by the host device. This value is in the units specified with FilterDelayUnits. |
|  | FilterDelayUnits | Specifies the units of FilterDelay. |
|  | FilterEnabled | Specifies the corresponding filter enable/disable state. |
|  | FilterFrequency | Specifies the corresponding filter frequency (cutoff or center) of the filter response. |
|  | FilterOrder | Specifies the corresponding filter order and defines the slope of the filter response. |
|  | FilterResponse | Specifies the corresponding filter response and defines the shape of the filter response. |
|  | FrequencyDigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
|  | FrequencyDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | FrequencyDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | FrequencyDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | FrequencyDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | FrequencyDivisor | Specifies the value by which to divide the input signal if FrequencyMeasurementMethod is LargeRangeTwoCounter. The larger the divisor, the more accurate the measurement. However, too large a value could cause the count register to roll over, which results in an incorrect measurement. |
|  | FrequencyEnableAveraging | Specifies whether to enable averaging mode for Sample Clock-timed frequency measurements. |
|  | FrequencyHysteresis | Specifies a hysteresis level to apply to FrequencyThresholdVoltage. When FrequencyStartingEdge is rising, the source signal must first fall below FrequencyThresholdVoltage minus the hysteresis before a rising edge is detected at FrequencyThresholdVoltage. When FrequencyStartingEdge is falling, the source signal must first rise above FrequencyThresholdVoltage plus the hysteresis before a falling edge is detected at FrequencyThresholdVoltage. |
|  | FrequencyLogicalLevelBehavior | Specifies the logic level behavior on the input line. |
|  | FrequencyMeasurementMethod | Specifies the method to use to measure the frequency of the signal. |
|  | FrequencyMeasurementTime | Specifies in seconds the length of time to measure the frequency of the signal if FrequencyMeasurementMethod is HighFrequencyTwoCounter. Measurement accuracy increases with increased measurement time and with increased signal frequency. If you measure a high-frequency signal for too long, however, the count register could roll over, which results in an incorrect measurement. |
|  | FrequencyStartingEdge | Specifies between which edges to measure the frequency of the signal. |
|  | FrequencyTerminal | Specifies the input terminal of the signal to measure. |
|  | FrequencyTerminalConfiguration | Specifies the input terminal configuration. |
|  | FrequencyThresholdVoltage | Specifies the voltage level at which to recognize waveform repetitions. Select a voltage level that occurs only once within the entire period of a waveform. You also can select a voltage that occurs only once while the voltage rises or falls. |
|  | FrequencyUnits | Specifies the units to use to return frequency measurements. |
|  | GpsSyncMethod | Specifies the method to use to synchronize the counter to a GPS receiver. |
|  | GpsSyncSource | Specifies the terminal to which the GPS synchronization signal is connected. |
|  | IsGlobal | Indicates whether the channel is a global channel. (Inherited from Channel.) |
|  | LinearEncoderDistancePerPulse | Specifies the distance to measure for each pulse the encoder generates on signal A or signal B. This value is in the units you specify with LinearEncoderUnits. |
|  | LinearEncoderInitialPosition | Specifies the position of the encoder when the measurement begins. This value is in the units you specify with LinearEncoderUnits. |
|  | LinearEncoderUnits | Specifies the units to use to return linear encoder measurements from the channel. |
|  | Maximum | Specifies the maximum value you expect to measure. This value is in the units you specify with a units property. When you query this property, it returns the coerced maximum value that the hardware can measure with the current settings. |
|  | MaximumMeasurementPeriod | Specifies the maximum period (in seconds) in which the device will recognize signals. For frequency measurements, a signal with a higher period than the one set in this property will return 0 Hz. For duty cycle, the device will return 0 or 1 depending on the state of the line during the max defined period of time. Period measurements will return NaN. Pulse width measurement will return zero. |
|  | MeasurementType | Indicates the measurement to take with the channel. |
|  | MemoryMappingEnable | Specifies for NI-DAQmx to map hardware registers to the memory space of the application, if possible. Normally, NI-DAQmx maps hardware registers to memory accessible only to the kernel. Mapping the registers to the memory space of the application increases performance. However, if the application accesses the memory space mapped to the registers, it can adversely affect the operation of the device and possibly result in a system crash. |
|  | Minimum | Specifies the minimum value you expect to measure. This value is in the units you specify with a units property. When you query this property, it returns the coerced minimum value that the hardware can measure with the current settings. |
|  | NumberPossiblyInvalidSamples | Indicates the number of samples that the device might have overwritten before it could transfer them to the buffer. |
|  | OutputState | Indicates the current state of the out terminal of the counter. |
|  | PeriodDigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
|  | PeriodDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | PeriodDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | PeriodDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | PeriodDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | PeriodDivisor | Specifies the value by which to divide the input signal if PeriodMeasurementMethod is LargeRangeTwoCounter. The larger the divisor, the more accurate the measurement. However, too large a value could cause the count register to roll over, which results in an incorrect measurement. |
|  | PeriodEnableAveraging | Specifies whether to enable averaging mode for Sample Clock-timed period measurements. |
|  | PeriodHysteresis | Specifies a hysteresis level to apply to PeriodThresholdVoltage. When PeriodStartingEdge is rising, the source signal must first fall below PeriodThresholdVoltage minus the hysteresis before a rising edge is detected at PeriodThresholdVoltage. When PeriodStartingEdge is falling, the source signal must first rise above PeriodThresholdVoltage plus the hysteresis before a falling edge is detected at PeriodThresholdVoltage. |
|  | PeriodLogicLevelBehavior | Specifies the logic level behavior on the input line. |
|  | PeriodMeasurementMethod | Specifies the method to use to measure the period of the signal. |
|  | PeriodMeasurementTime | Specifies in seconds the length of time to measure the period of the signal if PeriodMeasurementMethod is HighFrequencyTwoCounter. Measurement accuracy increases with increased measurement time and with increased signal frequency. If you measure a high-frequency signal for too long, however, the count register could roll over, which results in an incorrect measurement. |
|  | PeriodStartingEdge | Specifies between which edges to measure the period of the signal. |
|  | PeriodTerminal | Specifies the input terminal of the signal to measure. |
|  | PeriodTerminalConfiguration | Specifies the input terminal configuration. |
|  | PeriodThresholdVoltage | Specifies the voltage level at which to recognize waveform repetitions. Select a voltage level that occurs only once within the entire period of a waveform. You also can select a voltage that occurs only once while the voltage rises or falls. |
|  | PeriodUnits | Specifies the unit to use to return period measurements. |
|  | PhysicalName | Specifies the name of the physical channel upon which this virtual channel is based. (Inherited from Channel.) |
|  | Prescaler | Specifies the divisor to apply to the signal you connect to the counter source terminal. Scaled data that you read takes this setting into account. You should use a prescaler only when you connect an external signal to the counter source terminal and when that signal has a higher frequency than the fastest onboard timebase. Setting this value disables duplicate count prevention unless you explicitly set DuplicateCountPrevention to . |
|  | PulseFrequencyDigitalFilterEnable | Specifies whether to apply a digital filter to the signal to measure. |
|  | PulseFrequencyDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | PulseFrequencyDigitalFilterTimebaseRate | Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | PulseFrequencyDigitalFilterTimebaseSource | Specifies the terminal of the signal to use as the timebase of the digital filter. |
|  | PulseFrequencyDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | PulseFrequencyLogicLevelBehavior | Specifies the logic level behavior on the count reset line. |
|  | PulseFrequencyStartingEdge | Specifies on which edge of the input signal to begin pulse measurement. |
|  | PulseFrequencyTerminal | Specifies the input terminal of the signal to measure. |
|  | PulseFrequencyTerminalConfiguration | Specifies the input terminal configuration. |
|  | PulseFrequencyUnits | Specifies the units to use to return pulse specifications in terms of frequency. |
|  | PulseTicksDigitalFilterEnable | Specifies whether to apply a digital filter to the signal to measure. |
|  | PulseTicksDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | PulseTicksDigitalFilterTimebaseRate | Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | PulseTicksDigitalFilterTimebaseSource | Specifies the terminal of the signal to use as the timebase of the digital filter. |
|  | PulseTicksDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | PulseTicksLogicLevelBehavior | Specifies the logic level behavior on the count reset line. |
|  | PulseTicksStartingEdge | Specifies on which edge of the input signal to begin pulse measurement. |
|  | PulseTicksTerminal | Specifies the input terminal of the signal to measure. |
|  | PulseTicksTerminalConfiguration | Specifies the input terminal configuration. |
|  | PulseTimeDigitalFilterEnable | Specifies whether to apply a digital filter to the signal to measure. |
|  | PulseTimeDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | PulseTimeDigitalFilterTimebaseRate | Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | PulseTimeDigitalFilterTimebaseSource | Specifies the terminal of the signal to use as the timebase of the digital filter. |
|  | PulseTimeDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | PulseTimeLogicLevelBehavior | Specifies the logic level behavior on the count reset line. |
|  | PulseTimeStartingEdge | Specifies on which edge of the input signal to begin pulse measurement. |
|  | PulseTimeTerminal | Specifies the input terminal of the signal to measure. |
|  | PulseTimeTerminalConfiguration | Specifies the input terminal configuration. |
|  | PulseTimeUnits | Specifies the units to use to return pulse specifications in terms of high time and low time. |
|  | PulseWidthDigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
|  | PulseWidthDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | PulseWidthDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | PulseWidthDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | PulseWidthDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | PulseWidthLogicLevelBehavior | Specifies the logic level behavior on the input line. |
|  | PulseWidthStartingEdge | Specifies on which edge of the input signal to begin each pulse width measurement. |
|  | PulseWidthTerminal | Specifies the input terminal of the signal to measure. |
|  | PulseWidthTerminalConfiguration | Specifies the input terminal configuration. |
|  | PulseWidthUnits | Specifies the units to use to return pulse width measurements. |
|  | SampleClockOverrunBehavior | Specifies the counter behavior when data is read but a new value was not detected during a sample clock. |
|  | SampleClockOverrunSentinelValue | Specifies the sentinel value returned when the No New Sample Behavior is set to Sentinel Value. |
|  | SemiPeriodDigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
|  | SemiPeriodDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | SemiPeriodDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | SemiPeriodDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | SemiPeriodDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | SemiPeriodLogicLevelBehavior | Specifies the logic level behavior on the count reset line. |
|  | SemiPeriodStartingEdge | Specifies on which edge of the input signal to begin semi-period measurement. Semi-period measurements alternate between high time and low time, starting on this edge. |
|  | SemiPeriodTerminal | Specifies the input terminal of the signal to measure. |
|  | SemiPeriodTerminalConfiguration | Specifies the input terminal configuration. |
|  | SemiPeriodUnits | Specifies the units to use to return semi-period measurements. |
|  | SynchronizationUnlockBehavior | Specifies the action to take if the target loses its synchronization to the grand master. (Inherited from Channel.) |
|  | TerminalCountReached | Indicates whether the counter rolled over. When you query this property, NI-DAQmx resets it to . |
|  | TimestampInitialSeconds | Specifies the number of seconds that elapsed since the beginning of the current year. This value is ignored if GpsSyncMethod is IrigB. |
|  | TimestampUnits | Specifies the units to use to return timestamp measurements. |
|  | TwoEdgeSeparationFirstEdge | Specifies on which edge of the first signal to start each measurement. |
|  | TwoEdgeSeparationFirstEdgeDigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
|  | TwoEdgeSeparationFirstEdgeDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | TwoEdgeSeparationFirstEdgeDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | TwoEdgeSeparationFirstEdgeDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | TwoEdgeSeparationFirstEdgeDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | TwoEdgeSeparationFirstLogicLevelBehavior | Specifies the logic level behavior on the input line. |
|  | TwoEdgeSeparationFirstTerminal | Specifies the source terminal of the digital signal that starts each measurement. |
|  | TwoEdgeSeparationFirstTerminalConfiguration | Specifies the input terminal configuration. |
|  | TwoEdgeSeparationSecondEdge | Specifies on which edge of the second signal to stop each measurement. |
|  | TwoEdgeSeparationSecondEdgeDigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
|  | TwoEdgeSeparationSecondEdgeDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | TwoEdgeSeparationSecondEdgeDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | TwoEdgeSeparationSecondEdgeDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | TwoEdgeSeparationSecondEdgeDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | TwoEdgeSeparationSecondLogicLevelBehavior | Specifies the logic level behavior on the count reset line. |
|  | TwoEdgeSeparationSecondTerminal | Specifies the source terminal of the digital signal that stops each measurement. |
|  | TwoEdgeSeparationSecondTerminalConfiguration | Specifies the input terminal configuration. |
|  | TwoEdgeSeparationUnits | Specifies the units to use to return two-edge separation measurements from the channel. |
|  | Type | Indicates the type of the virtual channel. (Inherited from Channel.) |
|  | UsbTransferRequestCount | Specifies the maximum number of simultaneous USB transfers used to stream data. Modify this value to affect performance under different combinations of operating system and device. |
|  | UsbTransferRequestSize | Specifies the maximum size of a USB transfer request in bytes. Modify this value to affect performance under different combinations of operating system and device. |
|  | VelocityAInputDigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
|  | VelocityAInputDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the digital filter recognizes. |
|  | VelocityAInputDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | VelocityAInputDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | VelocityAInputLogicLevelBehavior | Specifies the logic level behavior of the input terminal. |
|  | VelocityAInputTerminal | Specifies the terminal to which signal A is connected. |
|  | VelocityAInputTerminalConfiguration | Specifies the input terminal configuration. |
|  | VelocityAngularEncoderPulsesPerRevolution | Specifies the number of pulses the encoder generates per revolution. This value is the number of pulses on either signal A or signal B, not the total number of pulses on both signal A and signal B. |
|  | VelocityAngularEncoderUnits | Specifies the units to use to return angular velocity counter measurements. |
|  | VelocityBInputDigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
|  | VelocityBInputDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the digital filter recognizes. |
|  | VelocityBInputDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | VelocityBInputDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | VelocityBInputLogicLevelBehavior | Specifies the logic level behavior of the input terminal. |
|  | VelocityBInputTerminal | Specifies the terminal to which signal B is connected. |
|  | VelocityBInputTerminalConfiguration | Specifies the input terminal configuration. |
|  | VelocityDecodingType | Specifies how to count and interpret the pulses the encoder generates on signal A and signal B. X1, X2, and X4 are valid for quadrature encoders only. Two Pulse Counting is valid for two-pulse encoders only. |
|  | VelocityDivisor | Specifies the value by which to divide the input signal. |
|  | VelocityLinearEncoderDistancePerPulse | Specifies the distance to measure for each pulse the encoder generates on signal A or signal B. This value is in the units you specify in CI.Velocity.LinEncoder.DistUnits. |
|  | VelocityLinearEncoderUnits | Specifies the units to use to return linear encoder velocity measurements from the channel. |
|  | VelocityMeasurementTime | Specifies in seconds the length of time to measure the velocity of the signal. |
|  | VirtualName | Gets the name of the virtual channel. (Inherited from Channel.) |
|  | VoltageThresholdLevel | Specifies the digital threshold value in Volts for high and low input transitions. Some devices do not support this for differential channels. |

Top

##### See Also

###### Reference

CIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_cichannelcollection.htm language=enus -->
## TOPIC 00877: CIChannelCollection Properties

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_cichannelcollection.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_cichannelcollection.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannelCollection Properties

### CIChannelCollection Properties

The [CIChannelCollection](t_nationalinstruments_daqmx_cichannelcollection.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | All | Gets a CIChannel that operates on all of the channels in the task. |
|  | Count | Gets the number of elements in the collection. |
|  | ItemInt64 | Gets the CIChannel at the specified index in the collection. In Visual C#, this property is the indexer. |
|  | ItemString | Gets the CIChannel with the specified virtual channel name. In Visual C#, this property is the indexer. |

Top

##### See Also

###### Reference

CIChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_cidatafrequency.htm language=enus -->
## TOPIC 00878: CIDataFrequency Properties

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_cidatafrequency.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_cidatafrequency.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CIDataFrequency Properties

### CIDataFrequency Properties

The [CIDataFrequency](t_nationalinstruments_daqmx_cidatafrequency.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | DutyCycle | Gets or sets the duty cycle of the pulse. |
|  | Frequency | Gets or sets the frequency of the pulse. |

Top

##### See Also

###### Reference

CIDataFrequency Structure

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_cidataticks.htm language=enus -->
## TOPIC 00879: CIDataTicks Properties

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_cidataticks.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_cidataticks.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CIDataTicks Properties

### CIDataTicks Properties

The [CIDataTicks](t_nationalinstruments_daqmx_cidataticks.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | HighTicksInt32 | Gets or sets the number of timebase ticks the pulse is high. |
|  | HighTicksUInt32 | Gets or sets the number of timebase ticks the pulse is high. |
|  | LowTicksInt32 | Gets or sets the number of timebase ticks the pulse is low. |
|  | LowTicksUInt32 | Gets or sets the number of timebase ticks the pulse is low. |

Top

##### See Also

###### Reference

CIDataTicks Structure

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_cidatatime.htm language=enus -->
## TOPIC 00880: CIDataTime Properties

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_cidatatime.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_cidatatime.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CIDataTime Properties

### CIDataTime Properties

The [CIDataTime](t_nationalinstruments_daqmx_cidatatime.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | HighTime | Gets or sets the amount of time the pulse is high. |
|  | LowTime | Gets or sets the amount of time the pulse is low. |

Top

##### See Also

###### Reference

CIDataTime Structure

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_cochannelcollection.htm language=enus -->
## TOPIC 00881: COChannelCollection Properties

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_cochannelcollection.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_cochannelcollection.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

COChannelCollection Properties

### COChannelCollection Properties

The [COChannelCollection](t_nationalinstruments_daqmx_cochannelcollection.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | All | Gets a COChannel that operates on all of the channels in the task. |
|  | Count | Gets the number of elements in the collection. |
|  | ItemInt64 | Gets the COChannel at the specified index. In Visual C#, this property is the indexer. |
|  | ItemString | Gets the COChannel with the specified virtual channel name. In Visual C#, this property is the indexer. |

Top

##### See Also

###### Reference

COChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_codatafrequency.htm language=enus -->
## TOPIC 00882: CODataFrequency Properties

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_codatafrequency.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_codatafrequency.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CODataFrequency Properties

### CODataFrequency Properties

The [CODataFrequency](t_nationalinstruments_daqmx_codatafrequency.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | DutyCycle | Gets or sets the duty cycle of the pulse. |
|  | Frequency | Gets or sets the frequency of the pulse. |

Top

##### See Also

###### Reference

CODataFrequency Structure

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_codatatime.htm language=enus -->
## TOPIC 00883: CODataTime Properties

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_codatatime.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_codatatime.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CODataTime Properties

### CODataTime Properties

The [CODataTime](t_nationalinstruments_daqmx_codatatime.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | HighTime | Gets or sets the amount of time the pulse is high. |
|  | LowTime | Gets or sets the amount of time the pulse is low. |

Top

##### See Also

###### Reference

CODataTime Structure

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_countermultichannelreader.htm language=enus -->
## TOPIC 00884: CounterMultiChannelReader Properties

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_countermultichannelreader.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_countermultichannelreader.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterMultiChannelReader Properties

### CounterMultiChannelReader Properties

The [CounterMultiChannelReader](t_nationalinstruments_daqmx_countermultichannelreader.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |

Top

##### See Also

###### Reference

CounterMultiChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_countersinglechannelreader.htm language=enus -->
## TOPIC 00885: CounterSingleChannelReader Properties

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_countersinglechannelreader.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_countersinglechannelreader.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelReader Properties

### CounterSingleChannelReader Properties

The [CounterSingleChannelReader](t_nationalinstruments_daqmx_countersinglechannelreader.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |

Top

##### See Also

###### Reference

CounterSingleChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_countersinglechannelwriter.htm language=enus -->
## TOPIC 00886: CounterSingleChannelWriter Properties

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_countersinglechannelwriter.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_countersinglechannelwriter.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelWriter Properties

### CounterSingleChannelWriter Properties

The [CounterSingleChannelWriter](t_nationalinstruments_daqmx_countersinglechannelwriter.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |

Top

##### See Also

###### Reference

CounterSingleChannelWriter Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_daqbuffer.htm language=enus -->
## TOPIC 00887: DaqBuffer Properties

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_daqbuffer.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_daqbuffer.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqBuffer Properties

### DaqBuffer Properties

The [DaqBuffer](t_nationalinstruments_daqmx_daqbuffer.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | InputBufferSize | Specifies the number of samples the input buffer can hold for each channel in the task. Zero indicates to allocate no buffer. Use a buffer size of 0 to perform a hardware-timed operation without using a buffer. Setting this property overrides the automatic input buffer allocation that NI-DAQmx performs. |
|  | InputOnBoardBufferSize | Indicates in samples per channel the size of the onboard input buffer of the device. |
|  | OutputBufferSize | Specifies the number of samples the output buffer can hold for each channel in the task. Zero indicates to allocate no buffer. Use a buffer size of 0 to perform a hardware-timed operation without using a buffer. Setting this property overrides the automatic output buffer allocation that NI-DAQmx performs. |
|  | OutputOnBoardBufferSize | Specifies in samples per channel the size of the onboard output buffer of the device. |

Top

##### See Also

###### Reference

DaqBuffer Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_daqexception.htm language=enus -->
## TOPIC 00888: DaqException Properties

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_daqexception.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_daqexception.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqException Properties

### DaqException Properties

The [DaqException](t_nationalinstruments_daqmx_daqexception.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Data | Gets a collection of key/value pairs that provide additional user-defined information about the exception. (Inherited from Exception.) |
|  | Error | Gets the NI-DAQmx driver code for the error that occurred. |
|  | HelpLink | Gets or sets a link to the help file associated with this exception. (Inherited from Exception.) |
|  | HResult | Gets or sets HRESULT, a coded numerical value that is assigned to a specific exception. (Inherited from Exception.) |
|  | InnerException | Gets the Exception instance that caused the current exception. (Inherited from Exception.) |
|  | Message | Gets a message that describes the current exception. (Inherited from Exception.) |
|  | Source | Gets or sets the name of the application or the object that causes the error. (Inherited from Exception.) |
|  | StackTrace | Gets a string representation of the immediate frames on the call stack. (Inherited from Exception.) |
|  | TargetSite | Gets the method that throws the current exception. (Inherited from Exception.) |

Top

##### See Also

###### Reference

DaqException Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_daqstream.htm language=enus -->
## TOPIC 00889: DaqStream Properties

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_daqstream.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_daqstream.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream Properties

### DaqStream Properties

The [DaqStream](t_nationalinstruments_daqmx_daqstream.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | AccessoryInsertionOrRemovalDetected | Indicates if any device(s) in the task detected the insertion or removal of an accessory since the task started. Reading this property clears the accessory change status for all channels in the task. You must read this property before you read DevicesWithInsertedOrRemovedAccessories. Otherwise, you will receive an error. |
|  | AvailableSamplesPerChannel | Indicates the number of samples available to read per channel. This value is the same for all channels in the task. |
|  | Buffer | Gets the buffer for the task. |
|  | ChannelsToRead | Sets a subset of channels in the task from which to read. |
|  | CommonModeRangeErrorChannels | Indicates a list of names of any virtual channels in the task for which the device(s) detected a common mode range violation. You must read CommonModeRangeErrorChannelsExist before you read this property. Otherwise, you will receive an error. |
|  | CommonModeRangeErrorChannelsExist | Indicates if the device(s) detected a common mode range violation for any virtual channel in the task. Common mode range violation occurs when the voltage of either the positive terminal or negative terminal to ground are out of range. Reading this property clears the common mode range violation status for all channels in the task. You must read this property before you read CommonModeRangeErrorChannels. Otherwise, you will receive an error. |
|  | CurrentReadPosition | Indicates in samples per channel the current position in the buffer. |
|  | CurrentWritePosition | Indicates the position in the buffer of the next sample to generate. This value is identical for all channels in the task. |
|  | DevicesWithInsertedOrRemovedAccessories | Indicates the names of any devices that detected the insertion or removal of an accessory since the task started. You must read AccessoryInsertionOrRemovalDetected before you read this property. Otherwise, you will receive an error. |
|  | DigitalLinesPerInputChannel | Indicates the number of lines per channel that NI-DAQmx returns in a sample for line-based reads. If a channel has fewer lines than this number, the extra lines are . |
|  | DigitalLinesPerOutputChannel | Indicates the number of Boolean values expected per channel in a sample for line-based writes. This property is determined by the channel in the task with the most digital lines. If a channel has fewer lines than this number, NI-DAQmx ignores the extra Boolean values. |
|  | LoggingFilePath | Specifies the path to the TDMS file to which you want to log data. If the file path is changed while the task is running, this takes effect on the next sample interval (if Logging.SampsPerFile has been set) or when DAQmx Start New File is called. New file paths can be specified by ending with "\\" or "/". Files created after specifying a new file path retain the same name and numbering sequence. |
|  | LoggingFilePreallocationSize | Specifies a size in samples to be used to pre-allocate space on disk. Pre-allocation can improve file I/O performance, especially in situations where multiple files are being written to disk. For finite tasks, the default behavior is to pre-allocate the file based on the number of samples you configure the task to acquire. |
|  | LoggingFileWriteSize | Specifies the size, in samples, in which data will be written to disk. The size must be evenly divisible by the volume sector size, in bytes. |
|  | LoggingMode | Specifies whether to enable logging and whether to allow reading data while logging. Log mode allows for the best performance. However, you cannot read data while logging if you specify this mode. If you want to read data while logging, specify Log and Read mode. |
|  | LoggingPause | Specifies whether logging is paused while a task is executing. If LoggingMode is set to Log and Read mode, this value is taken into consideration on the next call to DAQmx Read, where data is written to disk. If LoggingMode is set to Log Only mode, this value is taken into consideration the next time that data is written to disk. A new TDMS group is written when logging is resumed from a paused state. |
|  | LoggingSamplesPerFile | Specifies how many samples to write to each file. When the file reaches the number of samples specified, a new file is created with the naming convention of <filename>_####.tdms, where #### starts at 0001 and increments automatically with each new file. For example, if the file specified is C:\\data.tdms, the next file name used is C:\\data_0001.tdms. To disable file spanning behavior, set this attribute to 0. If LoggingFilePath is changed while this attribute is set, the new file path takes effect on the next file created. |
|  | NumberOfInputChannels | Indicates the number of channels that reading from the task reads from the task. This value is the number of channels in the task or the number of channels you specify with ChannelsToRead. |
|  | NumberOfOutputChannels | Indicates the number of channels that writing to the task writes to the task. This value is the number of channels in the task. |
|  | OpenThermocoupleChannels | Indicates a list of names of any virtual channels in the task for which the device(s) detected an open thermcouple. You must read OpenThermocoupleChannelsExist before you read this property. Otherwise, you will receive an error. |
|  | OpenThermocoupleChannelsExist | Indicates if the device(s) detected an open thermocouple connected to any virtual channel in the task. Reading this property clears the open thermocouple status for all channels in the task. You must read this property before you read OpenThermocoupleChannels. Otherwise, you will receive an error. |
|  | OutputBufferSpaceAvailable | Indicates in samples per channel the amount of available space in the buffer. |
|  | OverloadedInputChannels | Indicates a list of names of any overloaded virtual channels in the task. You must read OverloadedInputChannelsExist before you read this property. Otherwise, you will receive an error. |
|  | OverloadedInputChannelsExist | Indicates if the device(s) detected an overload in any virtual channel in the task. Reading this property clears the overload status for all channels in the task. You must read this property before you read OverloadedInputChannels. Otherwise, you will receive an error. |
|  | PhaseLockedLoopUnlockedChannels | Indicates the channels that had their PLLs unlock. |
|  | PhaseLockedLoopUnlockedChannelsExist | Indicates whether the PLL is currently locked, or whether it became unlocked during the previous acquisition. Devices may report PLL Unlock either during acquisition or after acquisition. |
|  | ReadAllAvailableSamples | Specifies whether subsequent read operations read all samples currently available in the buffer or wait for the buffer to become full before reading. NI-DAQmx uses this setting for finite acquisitions and only when the number of samples to read is -1. For continuous acquisitions when the number of samples to read is -1, a read operation always reads all samples currently available in the buffer. |
|  | ReadAutoStart | Specifies if reading from the task automatically starts the task if you did not start the task explicitly by using starting the task. The default value is . When reading from the task starts a finite acquisition task, it also stops the task after reading the last sample. |
|  | ReadExcitationFaultChannels | Indicates a list of names of any virtual channels in the task for which the device(s) detected an excitation fault condition. You must read ReadExcitationFaultChannelsExist before you read this property. Otherwise, you will receive an error. |
|  | ReadExcitationFaultChannelsExist | Indicates if the device(s) detected an excitation fault condition for any virtual channel in the task. Reading this property clears the excitation fault status for all channels in the task. You must read this property before you read ReadExcitationFaultChannels. Otherwise, you will receive an error. |
|  | ReadInputLimitsFaultChannels | Indicates the virtual channels that have detected samples outside the upper or lower limits configured for each channel in the task. You must read ReadInputLimitsFaultChannelsExist before you read this property. Otherwise, you will receive an error. |
|  | ReadInputLimitsFaultChannelsExist | Indicates if the device or devices detected a sample that was outside the upper or lower limits configured for each channel in the task. Reading this property clears the input limits fault channel status for all channels in the task. You must read this property before you read ReadInputLimitsFaultChannels. Otherwise, you will receive an error. Note: Fault detection applies to both positive and negative inputs. For instance, if you specify a lower limit of 2 mA and an upper limit of 12 mA, NI-DAQmx detects a fault at 15 mA and -15 mA, but not at -6 mA because it is in the range of -12 mA to -2 mA. |
|  | ReadOffset | Specifies an offset in samples per channel at which to begin a read operation. This offset is relative to the location you specify with ReadRelativeTo. |
|  | ReadOpenCurrentLoopChannels | Indicates a list of names of any virtual channels in the task for which the device(s) detected an open current loop. You must read ReadOpenCurrentLoopChannelsExist before you read this property. Otherwise, you will receive an error. |
|  | ReadOpenCurrentLoopChannelsExist | Indicates if the device(s) detected an open current loop for any virtual channel in the task. Reading this property clears the open current loop status for all channels in the task. You must read this property before you read ReadOpenCurrentLoopChannels. Otherwise, you will receive an error. |
|  | ReadOvercurrentChannels | Indicates a list of names of any virtual channels in the task for which the device(s) detected an overcurrent condition. You must read ReadOvercurrentChannelsExist before you read this property. Otherwise, you will receive an error. On some devices, you must restart the task for all overcurrent channels to recover. |
|  | ReadOvercurrentChannelsExist | Indicates if the device(s) detected an overcurrent condition for any virtual channel in the task. Reading this property clears the overcurrent status for all channels in the task. You must read this property before you read ReadOvercurrentChannels. Otherwise, you will receive an error. |
|  | ReadOvertemperatureChannels | Indicates a list of names of any overtemperature virtual channels. You must read ReadOvertemperatureChannelsExist before you read this property. Otherwise, you will receive an error. |
|  | ReadOvertemperatureChannelsExist | Indicates if the device(s) detected an overtemperature condition in any virtual channel in the task. Reading this property clears the overtemperature status for all channels in the task. You must read this property before you read ReadOvertemperatureChannels. Otherwise, you will receive an error. |
|  | ReadOverwriteMode | Specifies whether to overwrite samples in the buffer that you have not yet read. |
|  | ReadPowerSupplyFaultChannels | Indicates the virtual channels that have detected a power supply fault. You must read WritePowerSupplyFaultChannelsExist before you read this property. Otherwise, you will receive an error. |
|  | ReadPowerSupplyFaultChannelsExist | Indicates if the device or devices detected a power supply fault condition in any virtual channel in the task. Reading this property clears the power supply fault status for all channels in this task. You must read this property before you read ReadPowerSupplyFaultChannels. Otherwise, you will receive an error. |
|  | ReadRawDataWidth | Indicates in bytes the size of a raw sample from the task. |
|  | ReadRelativeTo | Specifies the point in the buffer at which to begin a read operation. If you also specify an offset with ReadOffset, the read operation begins at that offset relative to the point you select with this property. The default value is CurrentReadPosition unless you configure a Reference Trigger for the task. If you configure a Reference Trigger, the default value is FirstPretriggerSample. |
|  | ReadSleepTime | Specifies in seconds the amount of time to sleep after checking for available samples if ReadWaitMode is Sleep. |
|  | ReadSynchronizationUnlockedChannels | Indicates the channels from devices in an unlocked target. |
|  | ReadSynchronizationUnlockedChannelsExist | Indicates whether the target is currently locked to the grand master. Devices may report PLL Unlock either during acquisition or after acquisition. |
|  | ReadWaitMode | Specifies how reading from the task waits for samples to become available. |
|  | TdmsLoggingGroupName | Specifies the name of the group to create within the TDMS file for data from this task. If you append data to an existing file and the specified group already exists, NI-DAQmx appends a number symbol and a number to the group name, incrementing that number until finding a group name that does not exist. For example, if you specify a group name of Voltage Task, and that group already exists, NI-DAQmx assigns the group name Voltage Task #1, then Voltage Task #2. |
|  | TdmsLoggingOperation | Specifies how to open the TDMS file. |
|  | Timeout | Gets or sets the amount of time in milliseconds to wait for reads or writes to complete. |
|  | TotalSamplesAcquiredPerChannel | Indicates the total number of samples acquired by each channel. NI-DAQmx returns a single value because this value is the same for all channels. For retriggered acquisitions, this value is the cumulative number of samples across all retriggered acquisitions. |
|  | TotalSamplesGeneratedPerChannel | Indicates the total number of samples generated by each channel in the task. This value is identical for all channels in the task. |
|  | WaveformAttributeMode | Gets or sets the type of information returned from a waveform read. |
|  | WriteExternalOvervoltageChannels | Indicates a list of names of any virtual channels in the task for which an External Overvoltage condition has been detected. You must read External OvervoltageChansExist before you read this property. Otherwise, you will receive an error. |
|  | WriteExternalOvervoltageChannelsExist | Indicates if the device(s) detected an External Overvoltage condition for any channel in the task. Reading this property clears the External Overvoltage status for all channels in the task. You must read this property before you read External OvervoltageChans. Otherwise, you will receive an error. |
|  | WriteOffset | Specifies in samples per channel an offset at which a write operation begins. This offset is relative to the location you specify with WriteRelativeTo. |
|  | WriteOpenCurrentLoopChannels | Indicates a list of names of any virtual channels in the task for which the device(s) detected an open current loop. You must read WriteOpenCurrentLoopChannelsExist before you read this property. Otherwise, you will receive an error. |
|  | WriteOpenCurrentLoopChannelsExist | Indicates if the device(s) detected an open current loop for any channel in the task. Reading this property clears the open current loop status for all channels in the task. You must read this property before you read WriteOpenCurrentLoopChannels. Otherwise, you will receive an error. |
|  | WriteOvercurrentChannels | Indicates a list of names of any virtual channels in the task for which an overcurrent condition has been detected. You must read WriteOvercurrentChannelsExist before you read this property. Otherwise, you will receive an error. |
|  | WriteOvercurrentChannelsExist | Indicates if the device(s) detected an overcurrent condition for any channel in the task. Reading this property clears the overcurrent status for all channels in the task. You must read this property before you read WriteOvercurrentChannels. Otherwise, you will receive an error. |
|  | WriteOverloadedChannels | Indicates a list of names of any overloaded virtual channels in the task. You must read WriteOverloadedChannelsExist before you read this property. Otherwise, you will receive an error. |
|  | WriteOverloadedChannelsExist | Indicates if the device(s) detected an overload in any virtual channel in the task. Reading this property clears the overload status for all channels in the task. You must read this property before you read WriteOverloadedChannels. Otherwise, you will receive an error. |
|  | WriteOvertemperatureChannels | Indicates a list of names of any overtemperature virtual channels. You must read WriteOvertemperatureChannelsExist before you read this property. Otherwise, you will receive an error. The list of names may be empty if the device cannot determine the source of the overtemperature. |
|  | WriteOvertemperatureChannelsExist | Indicates if the device(s) detected an overtemperature condition in any virtual channel in the task. Reading this property clears the overtemperature status for all channels in the task. You must read this property before you read WriteOvertemperatureChannels. Otherwise, you will receive an error. |
|  | WritePowerSupplyFaultChannels | Indicates a list of names of any virtual channels in the task that have a power supply fault. You must read WritePowerSupplyFaultChannelsExist before you read this property. Otherwise, you will receive an error. |
|  | WritePowerSupplyFaultChannelsExist | Indicates if the device(s) detected a power supply fault for any channel in the task. Reading this property clears the power supply fault status for all channels in the task. You must read this property before you read WritePowerSupplyFaultChannels. Otherwise, you will receive an error. |
|  | WriteRawDataWidth | Indicates in bytes the required size of a raw sample to write to the task. |
|  | WriteRegenerationMode | Specifies whether to allow NI-DAQmx to generate the same data multiple times. |
|  | WriteRelativeTo | Specifies the point in the buffer at which to write data. If you also specify an offset with WriteOffset, the write operation begins at that offset relative to this point you select with this property. |
|  | WriteSleepTime | Specifies in seconds the amount of time to sleep after checking for available buffer space if WriteWaitMode is Sleep. |
|  | WriteSynchronizationUnlockedChannels | Indicates the channels from devices in an unlocked target. |
|  | WriteSynchronizationUnlockedChannelsExist | Indicates whether the target is currently locked to the grand master. Devices may report PLL Unlock either during acquisition or after acquisition. |
|  | WriteWaitMode | Specifies how writing to the task waits for space to become available in the buffer. |

Top

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_triggers.htm language=enus -->
## TOPIC 00890: Triggers Properties

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_triggers.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/properties_t_nationalinstruments_daqmx_triggers.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Triggers Properties

### Triggers Properties

The [Triggers](t_nationalinstruments_daqmx_triggers.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | AdvanceTrigger | Gets the AdvanceTrigger. |
|  | ArmStartTrigger | Gets the ArmStartTrigger. |
|  | HandshakeTrigger | Gets the HandshakeTrigger. |
|  | PauseTrigger | Gets the PauseTrigger. |
|  | ReferenceTrigger | Gets the ReferenceTrigger. |
|  | StartTrigger | Gets the StartTrigger. |
|  | SynchronizationType | Specifies the role of the device in a synchronized system. Setting this value to Master or Slave enables trigger skew correction. If you enable trigger skew correction, set this property to Master on only one device, and set this property to Slave on the other devices. |
|  | WatchdogExpirationTrigger | Gets the WatchdogExpirationTrigger. |

Top

##### See Also

###### Reference

Triggers Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_advancetrigger.htm language=enus -->
## TOPIC 00891: AdvanceTrigger Class

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_advancetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_advancetrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AdvanceTrigger Class

### AdvanceTrigger Class

switch task advances to the next entry in the scan list

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class AdvanceTrigger : MarshalByRefObject, 
	IFilteredTypeDescriptor
```

```text
Public Class AdvanceTrigger
	Inherits MarshalByRefObject
	Implements IFilteredTypeDescriptor
```

The AdvanceTrigger type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | DigitalEdge | Gets the DigitalEdgeAdvanceTrigger. |
|  | Type | Obsolete. (Deprecated) Specifies the type of trigger to use to advance to the next entry in a switch scan list. |

Top

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

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_advancetriggerpulsepolarity.htm language=enus -->
## TOPIC 00892: AdvanceTriggerPulsePolarity Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_advancetriggerpulsepolarity.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_advancetriggerpulsepolarity.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AdvanceTriggerPulsePolarity Enumeration

### AdvanceTriggerPulsePolarity Enumeration

Indicates the polarity of the exported Advance Trigger.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AdvanceTriggerPulsePolarity
```

```text
Public Enumeration AdvanceTriggerPulsePolarity
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | ActiveHigh | 10095 | High state is the active state. |
|  | ActiveLow | 10096 | Low state is the active state. |

##### Remarks

AdvanceTriggerPulsePolarity

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aiaccelerationchargesensitivityunits.htm language=enus -->
## TOPIC 00893: AIAccelerationChargeSensitivityUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aiaccelerationchargesensitivityunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aiaccelerationchargesensitivityunits.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIAccelerationChargeSensitivityUnits Enumeration

### AIAccelerationChargeSensitivityUnits Enumeration

Specifies the units of AI.Accel.Charge.Sensitivity.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AIAccelerationChargeSensitivityUnits
```

```text
Public Enumeration AIAccelerationChargeSensitivityUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | PicoCoulombsPerG | 16099 | PicoCoulombs per g. |
|  | PicoCoulombsPerMetersPerSecondSquared | 16100 | PicoCoulombs per m/s^2. |
|  | PicoCoulombsPerInchesPerSecondSquared | 16101 | PicoCoulombs per in/s^2. |

##### Remarks

AccelerationChargeSensitivityUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aiaccelerationfourwiredcvoltagesensitivityunits.htm language=enus -->
## TOPIC 00894: AIAccelerationFourWireDCVoltageSensitivityUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aiaccelerationfourwiredcvoltagesensitivityunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aiaccelerationfourwiredcvoltagesensitivityunits.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIAccelerationFourWireDCVoltageSensitivityUnits Enumeration

### AIAccelerationFourWireDCVoltageSensitivityUnits Enumeration

Specifies the units of AI.Accel.4WireDCVoltage.Sensitivity.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AIAccelerationFourWireDCVoltageSensitivityUnits
```

```text
Public Enumeration AIAccelerationFourWireDCVoltageSensitivityUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | MillivoltsPerG | 12509 | mVolts/g. |
|  | VoltsPerG | 12510 | Volts/g. |

##### Remarks

AccelerationFourWireDCVoltageSensitivityUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aiacexcitationwiremode.htm language=enus -->
## TOPIC 00895: AIACExcitationWireMode Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aiacexcitationwiremode.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aiacexcitationwiremode.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIACExcitationWireMode Enumeration

### AIACExcitationWireMode Enumeration

Specifies the number of leads on the LVDT or RVDT. Some sensors require you to tie leads together to create a four- or five- wire sensor. Refer to the sensor documentation for more information.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AIACExcitationWireMode
```

```text
Public Enumeration AIACExcitationWireMode
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | FourWire | 4 | 4-wire. |
|  | FiveWire | 5 | 5-wire. |
|  | SixWire | 6 | 6-wire. |

##### Remarks

ACExcitationWireMode

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aiautozeromode.htm language=enus -->
## TOPIC 00896: AIAutoZeroMode Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aiautozeromode.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aiautozeromode.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIAutoZeroMode Enumeration

### AIAutoZeroMode Enumeration

Specifies how often to measure ground. NI-DAQmx subtracts the measured ground voltage from every sample.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AIAutoZeroMode
```

```text
Public Enumeration AIAutoZeroMode
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | None | 10230 | Do not perform an autozero. |
|  | Once | 10244 | Perform an auto zero at the beginning of the acquisition. This auto zero task might not run if you have used DAQmx Control Task previously in your task. |
|  | EverySample | 10164 | Perform an auto zero at every sample of the acquisition. |

##### Remarks

AutoZeroMode

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aibridgeconfiguration.htm language=enus -->
## TOPIC 00897: AIBridgeConfiguration Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aibridgeconfiguration.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aibridgeconfiguration.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIBridgeConfiguration Enumeration

### AIBridgeConfiguration Enumeration

Specifies the type of Wheatstone bridge connected to the channel.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AIBridgeConfiguration
```

```text
Public Enumeration AIBridgeConfiguration
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | FullBridge | 10182 | Sensor is a full bridge. If you set UseExcitationForScaling to , NI-DAQmx divides the measurement by the excitation value. Many sensors scale data to native units using scaling of volts per excitation. |
|  | HalfBridge | 10187 | Sensor is a half bridge. If you set UseExcitationForScaling to , NI-DAQmx divides the measurement by the excitation value. Many sensors scale data to native units using scaling of volts per excitation. |
|  | QuarterBridge | 10270 | Sensor is a quarter bridge. If you set UseExcitationForScaling to , NI-DAQmx divides the measurement by the excitation value. Many sensors scale data to native units using scaling of volts per excitation. |
|  | NoBridge | 10228 | Sensor is not a Wheatstone bridge. |

##### Remarks

BridgeConfiguration

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aibridgescaletype.htm language=enus -->
## TOPIC 00898: AIBridgeScaleType Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aibridgescaletype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aibridgescaletype.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIBridgeScaleType Enumeration

### AIBridgeScaleType Enumeration

scaling type

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AIBridgeScaleType
```

```text
Public Enumeration AIBridgeScaleType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | None | 10230 | Do not scale electrical values to physical units. |
|  | TwoPointLinear | 15898 | You provide two pairs of electrical values and their corresponding physical values. NI-DAQmx uses those values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values. |
|  | Table | 10450 | Map an array of electrical values to an array of corresponding physical values, with all other values scaled proportionally. If you specify this scaling type, Maximum and Minimum must be within the smallest and largest physical values. For any data outside those endpoints, NI-DAQmx coerces that data to the endpoints. |
|  | Polynomial | 10449 | Scale values by using an Nth order polynomial equation. |

##### Remarks

scaling type

BridgeScaleType

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aichannelcalibrationscaletype.htm language=enus -->
## TOPIC 00899: AIChannelCalibrationScaleType Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aichannelcalibrationscaletype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aichannelcalibrationscaletype.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCalibrationScaleType Enumeration

### AIChannelCalibrationScaleType Enumeration

Specifies the method or equation form that the calibration scale uses.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AIChannelCalibrationScaleType
```

```text
Public Enumeration AIChannelCalibrationScaleType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Polynomial | 10449 | Scale values by using an Nth order polynomial equation. |
|  | Table | 10450 | Map an array of prescaled values to an array of corresponding scaled values, with all other values scaled proportionally. |
|  | None | 10230 |  |

##### Remarks

CalibrationScaleType

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aichannelcollection.htm language=enus -->
## TOPIC 00900: AIChannelCollection Class

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aichannelcollection.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aichannelcollection.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection Class

### AIChannelCollection Class

Task

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class AIChannelCollection : MarshalByRefObject, 
	ICollection
```

```text
Public Class AIChannelCollection
	Inherits MarshalByRefObject
	Implements ICollection
```

The AIChannelCollection type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | All | Gets an AIChannel that operates on all of the channels in the task. |
|  | Count | Gets the number of elements in the collection. |
|  | ItemInt64 | Gets the AIChannel at the specified index. In Visual C#, this property is the indexer. |
|  | ItemString | Gets the AIChannel with the specified virtual channel name. In Visual C#, this property is the indexer. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateAccelerationChargeChannel(String, String, AITerminalConfiguration, Double, Double, AIAccelerationUnits, Double, AIAccelerationChargeSensitivityUnits) | Creates channel(s) that use an accelerometer to measure acceleration and adds the channel(s) to the task you specify with taskHandle. |
|  | CreateAccelerationChargeChannel(String, String, AITerminalConfiguration, Double, Double, String, Double, AIAccelerationChargeSensitivityUnits) | Creates channel(s) that use an accelerometer to measure acceleration and adds the channel(s) to the task you specify with taskHandle. |
|  | CreateAccelerationFourWireDCVoltageChannel(String, String, AITerminalConfiguration, Double, Double, AIAccelerationUnits, Double, AIAccelerationFourWireDCVoltageSensitivityUnits, AIExcitationSource, Double, Boolean) | Creates an AIChannel that measures acceleration using a 4-wire, DC voltage-based sensor connected to the channel. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateAccelerationFourWireDCVoltageChannel(String, String, AITerminalConfiguration, Double, Double, String, Double, AIAccelerationFourWireDCVoltageSensitivityUnits, AIExcitationSource, Double, Boolean) | Creates an AIChannel that specifies the sensitivity of the 4-wire, DC voltage-based sensor connected to the channel. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateAccelerometerChannel(String, String, AITerminalConfiguration, Double, Double, Double, AIAccelerometerSensitivityUnits, AIExcitationSource, Double, AIAccelerationUnits) | Creates an AIChannel that uses an accelerometer to measure acceleration. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateAccelerometerChannel(String, String, AITerminalConfiguration, Double, Double, Double, AIAccelerometerSensitivityUnits, AIExcitationSource, Double, String) | Creates an AIChannel with the specified custom scale that uses an accelerometer to measure acceleration. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateBridgeChannel(String, String, Double, Double, AIBridgeUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double) | Creates an AIChannel that measures voltage ratios from a Wheatstone bridge. Use this instance with bridge-based sensors that measure phenomena other than strain, force, pressure, or torque, or that scale data to physical units NI-DAQmx does not support. This method adds one or more physical channels to the AIChannelCollection. Use a custom scale or other scaling code to convert the voltage ratios to physical units. |
|  | CreateBridgeChannel(String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double) | Creates an AIChannel that measures voltage ratios from a Wheatstone bridge, with the specified custom scale. Use this instance with bridge-based sensors that measure phenomena other than strain, force, pressure, or torque, or that scale data to physical units NI-DAQmx does not support. This method adds one or more physical channels to the AIChannelCollection. Use a custom scale or other scaling code to convert the voltage ratios to physical units. |
|  | CreateBuiltInSensorTemperatureChannel | Creates an AIChannel to measure temperature with a built-in sensor of a terminal block or device. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateChargeChannel(String, String, AITerminalConfiguration, Double, Double, AIChargeUnits) | Creates an AIChannel to measure acceleration using a charge-based sensor. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateChargeChannel(String, String, AITerminalConfiguration, Double, Double, String) | Creates an AIChannel to measure acceleration using a charge-based sensor. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateCurrentChannel(String, String, AITerminalConfiguration, Double, Double, AICurrentUnits) | Creates an AIChannel with an internal shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateCurrentChannel(String, String, AITerminalConfiguration, Double, Double, String) | Creates an AIChannel with the specified custom scale and an internal shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateCurrentChannel(String, String, AITerminalConfiguration, Double, Double, Double, AICurrentUnits) | Creates an AIChannel with the specified external shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateCurrentChannel(String, String, AITerminalConfiguration, Double, Double, Double, String) | Creates an AIChannel with the specified custom scale and external shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateCurrentChannel(String, String, AITerminalConfiguration, Double, Double, AICurrentUnits, AICurrentShuntLocation, Double, String) | Creates an AIChannel with the specified custom scale and external shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateCurrentRmsChannel(String, String, AITerminalConfiguration, Double, Double, AICurrentAcrmsUnits) | Creates an AIChannel with an internal shunt resistor to measure AC current. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateCurrentRmsChannel(String, String, AITerminalConfiguration, Double, Double, String) | Creates an AIChannel with the specified custom scale and an internal shunt resistor to measure AC current. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateCurrentRmsChannel(String, String, AITerminalConfiguration, Double, Double, Double, AICurrentAcrmsUnits) | Creates an AIChannel with the specified external shunt resistor to measure AC current. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateCurrentRmsChannel(String, String, AITerminalConfiguration, Double, Double, Double, String) | Creates an AIChannel with the specified custom scale and external shunt resistor to measure AC current. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateDeviceTemperatureChannel | Obsolete. Creates an AIChannel to measure temperature with a built-in sensor of a terminal block or device. This method adds one or more physical channels to the AIChannelCollection. The CreateDeviceTemperatureChannel(String, String, AITemperatureUnits) method has been deprecated in favor of the CreateBuiltInSensorTemperatureChannel(String, String, AITemperatureUnits) method. |
|  | CreateEddyCurrentProximityProbeChannel(String, String, Double, Double, Double, AIEddyCurrentProximityProbeSensitivityUnits, AIEddyCurrentProximityProbeUnits) | Creates an AIChannel that uses an Eddy Current Proximity Probe to measure position. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateEddyCurrentProximityProbeChannel(String, String, Double, Double, Double, AIEddyCurrentProximityProbeSensitivityUnits, String) | Creates an AIChannel with the specified custom scale that uses an Eddy Current Proximity Probe to measure position. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateForceBridgePolynomialChannel(String, String, Double, Double, AIForceUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure force or load. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electrical values to physical values (forward), as well as coefficients for a polynomial that converts physical values to electrical values (reverse). If you only know one set of coefficients, use PolynomialScale to generate the other set. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateForceBridgePolynomialChannel(String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure force or load, with the specified custom scale. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electrical values to physical values (forward), as well as coefficients for a polynomial that converts physical values to electrical values (reverse). If you only know one set of coefficients, use PolynomialScale to generate the other set. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateForceBridgeTableChannel(String, String, Double, Double, AIForceUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, AIBridgeElectricalUnits, Double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure force or load. Use this instance with sensors whose specifications provide a table of electrical values and the corresponding physical values. When you use this scaling type, NI-DAQmx performs linear scaling between each pair of electrical and physical values. The input limits specified with the minimum value and maximum value parameters must fall within the smallest and largest physical values. For any data outside those endpoints, NI-DAQmx coerces that data to the endpoints. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateForceBridgeTableChannel(String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, AIBridgeElectricalUnits, Double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure force or load, with the specified custom scale. Use this instance with sensors whose specifications provide a table of electrical values and the corresponding physical values. When you use this scaling type, NI-DAQmx performs linear scaling between each pair of electrical and physical values. The input limits specified with the minimum value and maximum value parameters must fall within the smallest and largest physical values. For any data outside those endpoints, NI-DAQmx coerces that data to the endpoints. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateForceBridgeTwoPointLinearChannel(String, String, Double, Double, AIForceUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, Double, Double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure force or load. Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points of electrical and physical values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateForceBridgeTwoPointLinearChannel(String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, Double, Double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure force or load, with the specified custom scale. Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points of electrical and physical values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateForceIepeChannel(String, String, AITerminalConfiguration, Double, Double, AIForceUnits, Double, AIForceIepeSensorSensitivityUnits, AIExcitationSource, Double) | Creates an AIChannel that uses an IEPE force sensor to measure force or load. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateForceIepeChannel(String, String, AITerminalConfiguration, Double, Double, String, Double, AIForceIepeSensorSensitivityUnits, AIExcitationSource, Double) | Creates an AIChannel that uses an IEPE force sensor to measure force or load, with the specified custom scale. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateFrequencyVoltageChannel(String, String, Double, Double, Double, Double, AIFrequencyUnits) | Creates an AIChannel to measure frequency using a frequency-to-voltage converter. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateFrequencyVoltageChannel(String, String, Double, Double, Double, Double, String) | Creates an AIChannel with the specified custom scale to measure frequency using a frequency-to-voltage converter. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateLvdtChannel(String, String, Double, Double, Double, AILvdtSensitivityUnits, AIExcitationSource, Double, Double, AIACExcitationWireMode, AILvdtUnits) | Creates an AIChannel that uses an LVDT to measure linear position. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateLvdtChannel(String, String, Double, Double, Double, AILvdtSensitivityUnits, AIExcitationSource, Double, Double, AIACExcitationWireMode, String) | Creates an AIChannel with the specified custom scale that uses an LVDT to measure linear position. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateMicrophoneChannel(String, String, Double, Double, AITerminalConfiguration, AIExcitationSource, Double, AISoundPressureUnits) | Creates an AIChannel that uses a microphone to measure sound pressure. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateMicrophoneChannel(String, String, Double, Double, AITerminalConfiguration, AIExcitationSource, Double, String) | Creates an AIChannel with the specified custom scale that uses a microphone to measure sound pressure. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | CreatePressureBridgePolynomialChannel(String, String, Double, Double, AIPressureUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure pressure. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electrical values to physical values (forward), as well as coefficients for a polynomial that converts physical values to electrical values (reverse). If you only know one set of coefficients, use PolynomialScale to generate the other set. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreatePressureBridgePolynomialChannel(String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure pressure, with the specified custom scale. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electrical values to physical values (forward), as well as coefficients for a polynomial that converts physical values to electrical values (reverse). If you only know one set of coefficients, use PolynomialScale to generate the other set. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreatePressureBridgeTableChannel(String, String, Double, Double, AIPressureUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, AIBridgeElectricalUnits, Double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure pressure. Use this instance with sensors whose specifications provide a table of electrical values and the corresponding physical values. When you use this scaling type, NI-DAQmx performs linear scaling between each pair of electrical and physical values. The input limits specified with the minimum value and maximum value parameters must fall within the smallest and largest physical values. For any data outside those endpoints, NI-DAQmx coerces that data to the endpoints. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreatePressureBridgeTableChannel(String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, AIBridgeElectricalUnits, Double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure pressure, with the specified custom scale. Use this instance with sensors whose specifications provide a table of electrical values and the corresponding physical values. When you use this scaling type, NI-DAQmx performs linear scaling between each pair of electrical and physical values. The input limits specified with the minimum value and maximum value parameters must fall within the smallest and largest physical values. For any data outside those endpoints, NI-DAQmx coerces that data to the endpoints. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreatePressureBridgeTwoPointLinearChannel(String, String, Double, Double, AIPressureUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, Double, Double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure pressure. Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points of electrical and physical values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreatePressureBridgeTwoPointLinearChannel(String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, Double, Double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure pressure, with the specified custom scale. Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points of electrical and physical values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateResistanceChannel(String, String, Double, Double, AIResistanceConfiguration, AIExcitationSource, Double, AIResistanceUnits) | Creates an AIChannel to measure resistance. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateResistanceChannel(String, String, Double, Double, AIResistanceConfiguration, AIExcitationSource, Double, String) | Creates an AIChannel with the specified custom scale to measure resistance. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateRosetteStrainGageChannel | Creates an AIChannel to measure two-dimensional strain using a rosette strain gage. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateRtdChannel | Creates an AIChannel that uses an RTD to measure temperature. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateRvdtChannel(String, String, Double, Double, Double, AIRvdtSensitivityUnits, AIExcitationSource, Double, Double, AIACExcitationWireMode, AIRvdtUnits) | Creates an AIChannel that uses an RVDT to measure angular position. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateRvdtChannel(String, String, Double, Double, Double, AIRvdtSensitivityUnits, AIExcitationSource, Double, Double, AIACExcitationWireMode, String) | Creates an AIChannel with the specified custom scale that uses an RVDT to measure angular position. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateStrainGageChannel(String, String, Double, Double, AIStrainGageConfiguration, AIExcitationSource, Double, Double, Double, Double, Double, Double, AIStrainUnits) | Creates an AIChannel to measure strain. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateStrainGageChannel(String, String, Double, Double, AIStrainGageConfiguration, AIExcitationSource, Double, Double, Double, Double, Double, Double, String) | Creates an AIChannel with the specified custom scale to measure strain. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsAccelerometerChannel(String, String, Double, Double, AIExcitationSource, Double, AIAccelerationUnits) | Creates an AIChannel that uses an accelerometer to measure acceleration. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsAccelerometerChannel(String, String, Double, Double, AIExcitationSource, Double, String) | Creates an AIChannel with the specified custom scale that uses an accelerometer to measure acceleration. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsBridgeChannel(String, String, Double, Double, AIBridgeUnits, AIExcitationSource, Double) | Creates an AIChannel that measures a a Wheatstone bridge. You must configure the physical channel(s) with TEDS information to use this method. Use this instance with bridge-based sensors that measure phenomena other than strain, force, pressure, or torque, or that scale data to physical units NI-DAQmx does not support. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsBridgeChannel(String, String, Double, Double, String, AIExcitationSource, Double) | Creates an AIChannel that measures a a Wheatstone bridge, with the specified custom scale. You must configure the physical channel(s) with TEDS information to use this method. Use this instance with bridge-based sensors that measure phenomena other than strain, force, pressure, or torque, or that scale data to physical units NI-DAQmx does not support. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsCurrentChannel(String, String, AITerminalConfiguration, Double, Double, AICurrentUnits) | Creates an AIChannel with an internal shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsCurrentChannel(String, String, AITerminalConfiguration, Double, Double, String) | Creates an AIChannel with the specified custom scale and an internal shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsCurrentChannel(String, String, AITerminalConfiguration, Double, Double, Double, AICurrentUnits) | Creates an AIChannel with the specified external shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsCurrentChannel(String, String, AITerminalConfiguration, Double, Double, Double, String) | Creates an AIChannel with the specified custom scale and external shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsForceBridgeChannel(String, String, Double, Double, AIForceUnits, AIExcitationSource, Double) | Creates an AIChannel that uses a Wheatstone bridge to measure force or load. You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsForceBridgeChannel(String, String, Double, Double, String, AIExcitationSource, Double) | Creates an AIChannel that uses a Wheatstone bridge to measure force or load, with the specified custom scale. You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsForceIepeChannel(String, String, AITerminalConfiguration, Double, Double, AIForceUnits, AIExcitationSource, Double) | Creates an AIChannel that uses an IEPE force sensor to measure force or load. You must configure the physical channel(s) with TEDS information to use this method. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsForceIepeChannel(String, String, AITerminalConfiguration, Double, Double, String, AIExcitationSource, Double) | Creates an AIChannel that uses an IEPE force sensor to measure force or load, with the specified custom scale. You must configure the physical channel(s) with TEDS information to use this method. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsLvdtChannel(String, String, Double, Double, AIExcitationSource, Double, Double, AIACExcitationWireMode, AILvdtUnits) | Creates an AIChannel that uses an LVDT to measure linear position. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsLvdtChannel(String, String, Double, Double, AIExcitationSource, Double, Double, AIACExcitationWireMode, String) | Creates an AIChannel with the specified custom scale that uses an LVDT to measure linear position. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsMicrophoneChannel(String, String, Double, AITerminalConfiguration, AIExcitationSource, Double, AISoundPressureUnits) | Creates an AIChannel that uses a microphone to measure sound pressure. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsMicrophoneChannel(String, String, Double, AITerminalConfiguration, AIExcitationSource, Double, String) | Creates an AIChannel with the specified custom scale that uses a microphone to measure sound pressure. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsPressureBridgeChannel(String, String, Double, Double, AIPressureUnits, AIExcitationSource, Double) | Creates an AIChannel that uses a Wheatstone bridge to measure pressure. You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one or more physical channels to the AIChannelCollection. You must configure the physical channel(s) with TEDS information to use this method. |
|  | CreateTedsPressureBridgeChannel(String, String, Double, Double, String, AIExcitationSource, Double) | Creates an AIChannel that uses a Wheatstone bridge to measure pressure, with the specified custom scale. You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one or more physical channels to the AIChannelCollection. You must configure the physical channel(s) with TEDS information to use this method. |
|  | CreateTedsResistanceChannel(String, String, Double, Double, AIResistanceConfiguration, AIExcitationSource, Double, AIResistanceUnits) | Creates an AIChannel to measure resistance. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsResistanceChannel(String, String, Double, Double, AIResistanceConfiguration, AIExcitationSource, Double, String) | Creates an AIChannel with the specified custom scale to measure resistance. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsRtdChannel | Creates an AIChannel that uses an RTD to measure temperature. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsRvdtChannel(String, String, Double, Double, AIExcitationSource, Double, Double, AIACExcitationWireMode, AIRvdtUnits) | Creates an AIChannel that uses an RVDT to measure angular position. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsRvdtChannel(String, String, Double, Double, AIExcitationSource, Double, Double, AIACExcitationWireMode, String) | Creates an AIChannel that uses an RVDT to measure angular position. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsStrainGageChannel(String, String, Double, Double, AIExcitationSource, Double, Double, Double, AIStrainUnits) | Creates an AIChannel to measure strain. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsStrainGageChannel(String, String, Double, Double, AIExcitationSource, Double, Double, Double, String) | Creates an AIChannel with the specified custom scale to measure strain. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsThermistorIExChannel | Creates an AIChannel that uses a thermistor to measure temperature. Use this method when the thermistor uses current excitation. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsThermistorVExChannel | Creates an AIChannel that uses a thermistor to measure temperature. Use this method when the thermistor uses voltage excitation. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsThermocoupleChannel(String, String, Double, Double, AITemperatureUnits) | Creates an AIChannel that uses a thermocouple to measure temperature using a built-in cold-junction compensation source. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsThermocoupleChannel(String, String, Double, Double, AITemperatureUnits, Double) | Creates an AIChannel that uses a thermocouple to measure temperature using a constant value cold-junction compensation. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsThermocoupleChannel(String, String, Double, Double, AITemperatureUnits, String) | Creates an AIChannel that uses a thermocouple to measure temperature using a measurement on another channel for cold-junction compensation. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsTorqueBridgeChannel(String, String, Double, Double, AITorqueUnits, AIExcitationSource, Double) | Creates an AIChannel that uses a Wheatstone bridge to measure torque. You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsTorqueBridgeChannel(String, String, Double, Double, String, AIExcitationSource, Double) | Creates an AIChannel that uses a Wheatstone bridge to measure torque, with the specified custom scale. You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsVoltageChannel(String, String, AITerminalConfiguration, Double, Double, AIVoltageUnits) | Creates an AIChannel to measure voltage. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsVoltageChannel(String, String, AITerminalConfiguration, Double, Double, String) | Creates an AIChannel with the specified custom scale to measure voltage. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsVoltageChannelWithExcitation(String, String, AITerminalConfiguration, Double, Double, AIExcitationSource, Double, AIVoltageUnits) | Creates an AIChannel to measure voltage for custom sensors that require excitation. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsVoltageChannelWithExcitation(String, String, AITerminalConfiguration, Double, Double, AIExcitationSource, Double, String) | Creates an AIChannel with the specified custom scale to measure voltage for custom sensors that require excitation. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateThermistorIExChannel | Creates an AIChannel that uses a thermistor to measure temperature. Use this method when the thermistor uses current excitation. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateThermistorVExChannel | Creates an AIChannel that uses a thermistor to measure temperature. Use this method when the thermistor uses voltage excitation. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateThermocoupleChannel(String, String, Double, Double, AIThermocoupleType, AITemperatureUnits) | Creates an AIChannel that uses a thermocouple to measure temperature using a built-in cold-junction compensation source. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateThermocoupleChannel(String, String, Double, Double, AIThermocoupleType, AITemperatureUnits, Double) | Creates an AIChannel that uses a thermocouple to measure temperature using a constant value cold-junction compensation. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateThermocoupleChannel(String, String, Double, Double, AIThermocoupleType, AITemperatureUnits, String) | Creates an AIChannel that uses a thermocouple to measure temperature using a measurement on another channel for cold-junction compensation. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTorqueBridgePolynomialChannel(String, String, Double, Double, AITorqueUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure torque. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electrical values to physical values (forward), as well as coefficients for a polynomial that converts physical values to electrical values (reverse). If you only know one set of coefficients, use PolynomialScale to generate the other set. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTorqueBridgePolynomialChannel(String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure torque, with the specified custom scale. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electrical values to physical values (forward), as well as coefficients for a polynomial that converts physical values to electrical values (reverse). If you only know one set of coefficients, use PolynomialScale to generate the other set. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTorqueBridgeTableChannel(String, String, Double, Double, AITorqueUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, AIBridgeElectricalUnits, Double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure torque, with the specified custom scale. Use this instance with sensors whose specifications provide a table of electrical values and the corresponding physical values. When you use this scaling type, NI-DAQmx performs linear scaling between each pair of electrical and physical values. The input limits specified with the minimum value and maximum value parameters must fall within the smallest and largest physical values. For any data outside those endpoints, NI-DAQmx coerces that data to the endpoints. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTorqueBridgeTableChannel(String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, AIBridgeElectricalUnits, Double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure torque, with the specified custom scale. Use this instance with sensors whose specifications provide a table of electrical values and the corresponding physical values. When you use this scaling type, NI-DAQmx performs linear scaling between each pair of electrical and physical values. The input limits specified with the minimum value and maximum value parameters must fall within the smallest and largest physical values. For any data outside those endpoints, NI-DAQmx coerces that data to the endpoints. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTorqueBridgeTwoPointLinearChannel(String, String, Double, Double, AITorqueUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, Double, Double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure torque, with the specified custom scale. Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points of electrical and physical values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTorqueBridgeTwoPointLinearChannel(String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, Double, Double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure torque, with the specified custom scale. Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points of electrical and physical values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateVelocityIepeChannel(String, String, AITerminalConfiguration, Double, Double, AIVelocityUnits, Double, AIVelocityIepeSensorSensitivityUnits, AIExcitationSource, Double) | Creates an AIChannel that uses an IEPE velocity sensor to measure velocity. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateVelocityIepeChannel(String, String, AITerminalConfiguration, Double, Double, String, Double, AIVelocityIepeSensorSensitivityUnits, AIExcitationSource, Double) | Creates an AIChannel that uses an IEPE velocity sensor to measure velocity. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateVoltageChannel(String, String, AITerminalConfiguration, Double, Double, AIVoltageUnits) | Creates an AIChannel to measure voltage. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateVoltageChannel(String, String, AITerminalConfiguration, Double, Double, String) | Creates an AIChannel with the specified custom scale to measure voltage. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateVoltageChannelWithExcitation(String, String, AITerminalConfiguration, Double, Double, AIBridgeConfiguration, AIExcitationSource, Double, Boolean, AIVoltageUnits) | Creates an AIChannel to measure voltage for custom sensors that require excitation. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateVoltageChannelWithExcitation(String, String, AITerminalConfiguration, Double, Double, AIBridgeConfiguration, AIExcitationSource, Double, Boolean, String) | Creates an AIChannel with the specified custom scale to measure voltage for custom sensors that require excitation. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateVoltageRmsChannel(String, String, AITerminalConfiguration, Double, Double, AIVoltageAcrmsUnits) | Creates an AIChannel to measure AC voltage. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateVoltageRmsChannel(String, String, AITerminalConfiguration, Double, Double, String) | Creates an AIChannel with the specified custom scale to measure AC voltage. This method adds one or more physical channels to the AIChannelCollection. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetEnumerator | Returns an enumerator that you can use to iterate through the collection. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aipressureunits.htm language=enus -->
## TOPIC 00901: AIPressureUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aipressureunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aipressureunits.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIPressureUnits Enumeration

### AIPressureUnits Enumeration

Specifies in which unit to return pressure measurements from the channel.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AIPressureUnits
```

```text
Public Enumeration AIPressureUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Pascals | 10081 | Pascals. |
|  | PoundsPerSquareInch | 15879 | Pounds per square inch. |
|  | Bar | 15880 | Bar. |
|  | FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

##### Remarks

PressureUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_airawdatacompressiontype.htm language=enus -->
## TOPIC 00902: AIRawDataCompressionType Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_airawdatacompressiontype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_airawdatacompressiontype.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIRawDataCompressionType Enumeration

### AIRawDataCompressionType Enumeration

raw samples

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AIRawDataCompressionType
```

```text
Public Enumeration AIRawDataCompressionType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | None | 10230 | Do not compress samples. |
|  | LosslessPacking | 12555 | Remove unused bits from samples. No resolution is lost. |
|  | LossyLsbRemoval | 12556 | Remove unused bits from samples. Then, if necessary, remove bits from samples until the samples are the size specified with LossyLsbRemovalCompressedSampleSize. This compression type limits resolution to the specified sample size. |

##### Remarks

raw samples

RawDataCompressionType

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_airawsamplejustification.htm language=enus -->
## TOPIC 00903: AIRawSampleJustification Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_airawsamplejustification.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_airawsamplejustification.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIRawSampleJustification Enumeration

### AIRawSampleJustification Enumeration

raw sample

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AIRawSampleJustification
```

```text
Public Enumeration AIRawSampleJustification
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | RightJustified | 10279 | Samples occupy the lower bits of the integer. |
|  | LeftJustified | 10209 | Samples occupy the higher bits of the integer. |

##### Remarks

raw sample

RawSampleJustification

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_airesistanceconfiguration.htm language=enus -->
## TOPIC 00904: AIResistanceConfiguration Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_airesistanceconfiguration.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_airesistanceconfiguration.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIResistanceConfiguration Enumeration

### AIResistanceConfiguration Enumeration

Specifies the resistance configuration for the channel. NI-DAQmx uses this value for any resistance-based measurements, including temperature measurement using a thermistor or RTD.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AIResistanceConfiguration
```

```text
Public Enumeration AIResistanceConfiguration
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | TwoWire | 2 | 2-wire mode. |
|  | ThreeWire | 3 | 3-wire mode. |
|  | FourWire | 4 | 4-wire mode. |

##### Remarks

ResistanceConfiguration

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_airesolutionunits.htm language=enus -->
## TOPIC 00905: AIResolutionUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_airesolutionunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_airesolutionunits.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIResolutionUnits Enumeration

### AIResolutionUnits Enumeration

Resolution

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AIResolutionUnits
```

```text
Public Enumeration AIResolutionUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Bits | 10109 | Bits. |

##### Remarks

Resolution

ResolutionUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_airosettetype.htm language=enus -->
## TOPIC 00906: AIRosetteType Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_airosettetype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_airosettetype.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIRosetteType Enumeration

### AIRosetteType Enumeration

Indicates the type of rosette gage.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AIRosetteType
```

```text
Public Enumeration AIRosetteType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Rectangular | 15968 | A rectangular rosette consists of three strain gages, each separated by a 45 degree angle. |
|  | Delta | 15969 | A delta rosette consists of three strain gages, each separated by a 60 degree angle. |
|  | Tee | 15970 | A tee rosette consists of two gages oriented at 90 degrees with respect to each other. |

##### Remarks

RosetteType

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aivelocityiepesensorsensitivityunits.htm language=enus -->
## TOPIC 00907: AIVelocityIepeSensorSensitivityUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aivelocityiepesensorsensitivityunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aivelocityiepesensorsensitivityunits.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIVelocityIepeSensorSensitivityUnits Enumeration

### AIVelocityIepeSensorSensitivityUnits Enumeration

VelocityIepeSensorSensitivity

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AIVelocityIepeSensorSensitivityUnits
```

```text
Public Enumeration AIVelocityIepeSensorSensitivityUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | MillivoltsPerMillimeterPerSecond | 15963 | Millivolts per millimeter per second. |
|  | MillivoltsPerInchPerSecond | 15964 | Millivolts per inch per second. |

##### Remarks

VelocityIepeSensorSensitivity

VelocityIepeSensorSensitivityUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aivelocityunits.htm language=enus -->
## TOPIC 00908: AIVelocityUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aivelocityunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aivelocityunits.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIVelocityUnits Enumeration

### AIVelocityUnits Enumeration

Specifies in which unit to return velocity measurements from the channel.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AIVelocityUnits
```

```text
Public Enumeration AIVelocityUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | MetersPerSecond | 15959 | Meters per second. |
|  | InchesPerSecond | 15960 | Inches per second. |
|  | FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

##### Remarks

VelocityUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aivoltageacrmsunits.htm language=enus -->
## TOPIC 00909: AIVoltageAcrmsUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aivoltageacrmsunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aivoltageacrmsunits.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIVoltageAcrmsUnits Enumeration

### AIVoltageAcrmsUnits Enumeration

Specifies the units to use to return voltage RMS measurements from the channel.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AIVoltageAcrmsUnits
```

```text
Public Enumeration AIVoltageAcrmsUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Volts | 10348 | Volts. |
|  | FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |
|  | FromTeds | 12516 | Units defined by TEDS information associated with the channel. |

##### Remarks

VoltageAcrmsUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aivoltageunits.htm language=enus -->
## TOPIC 00910: AIVoltageUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aivoltageunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aivoltageunits.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIVoltageUnits Enumeration

### AIVoltageUnits Enumeration

Specifies the units to use to return voltage measurements from the channel.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AIVoltageUnits
```

```text
Public Enumeration AIVoltageUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Volts | 10348 | Volts. |
|  | FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |
|  | FromTeds | 12516 | Units defined by TEDS information associated with the channel. |

##### Remarks

VoltageUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_analogedgepausetriggercoupling.htm language=enus -->
## TOPIC 00911: AnalogEdgePauseTriggerCoupling Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_analogedgepausetriggercoupling.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_analogedgepausetriggercoupling.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogEdgePauseTriggerCoupling Enumeration

### AnalogEdgePauseTriggerCoupling Enumeration

terminal

virtual channel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AnalogEdgePauseTriggerCoupling
```

```text
Public Enumeration AnalogEdgePauseTriggerCoupling
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | AC | 10045 | Alternating Current. |
|  | DC | 10050 | Direct Current. |

##### Remarks

terminal

virtual channel

Coupling

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_analogedgereferencetrigger.htm language=enus -->
## TOPIC 00912: AnalogEdgeReferenceTrigger Class

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_analogedgereferencetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_analogedgereferencetrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogEdgeReferenceTrigger Class

### AnalogEdgeReferenceTrigger Class

analog edge

reference triggers

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class AnalogEdgeReferenceTrigger : MarshalByRefObject, 
	IFilteredTypeDescriptor
```

```text
Public Class AnalogEdgeReferenceTrigger
	Inherits MarshalByRefObject
	Implements IFilteredTypeDescriptor
```

The AnalogEdgeReferenceTrigger type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Coupling | Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel. |
|  | DigitalFilterEnable | Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay above or below the trigger level for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the hysteresis window rapidly. |
|  | DigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width thefilter recognizes. |
|  | DigitalFilterTimebaseRate | Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | DigitalFilterTimebaseSource | Specifies the terminal of the signal to use as the timebase of the digital filter. |
|  | DigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | Hysteresis | Specifies a hysteresis level in the units of the measurement. If Slope is Rising, the trigger does not deassert until the source signal passes below Level minus the hysteresis. If Slope is Falling, the trigger does not deassert until the source signal passes above Level plus the hysteresis. Hysteresis is always enabled. Set this property to a non-zero value to use hysteresis. |
|  | Level | Specifies in the units of the measurement the threshold at which the Reference Trigger occurs. Use Slope to specify on which slope to trigger at this threshold. |
|  | Slope | Specifies on which slope of the source signal the Reference Trigger occurs. |
|  | Source | Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the Reference Trigger. |

Top

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

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_analogedgereferencetriggercoupling.htm language=enus -->
## TOPIC 00913: AnalogEdgeReferenceTriggerCoupling Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_analogedgereferencetriggercoupling.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_analogedgereferencetriggercoupling.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogEdgeReferenceTriggerCoupling Enumeration

### AnalogEdgeReferenceTriggerCoupling Enumeration

terminal

virtual channel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AnalogEdgeReferenceTriggerCoupling
```

```text
Public Enumeration AnalogEdgeReferenceTriggerCoupling
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | AC | 10045 | Alternating Current. |
|  | DC | 10050 | Direct Current. |

##### Remarks

terminal

virtual channel

Coupling

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_analogedgereferencetriggerslope.htm language=enus -->
## TOPIC 00914: AnalogEdgeReferenceTriggerSlope Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_analogedgereferencetriggerslope.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_analogedgereferencetriggerslope.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogEdgeReferenceTriggerSlope Enumeration

### AnalogEdgeReferenceTriggerSlope Enumeration

Reference Trigger

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AnalogEdgeReferenceTriggerSlope
```

```text
Public Enumeration AnalogEdgeReferenceTriggerSlope
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Rising | 10280 | Trigger on the rising slope of the signal. |
|  | Falling | 10171 | Trigger on the falling slope of the signal. |

##### Remarks

Reference Trigger

Slope

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_analogedgestarttrigger.htm language=enus -->
## TOPIC 00915: AnalogEdgeStartTrigger Class

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_analogedgestarttrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_analogedgestarttrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogEdgeStartTrigger Class

### AnalogEdgeStartTrigger Class

analog edge

start triggers

StartTrigger

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class AnalogEdgeStartTrigger : MarshalByRefObject, 
	IFilteredTypeDescriptor
```

```text
Public Class AnalogEdgeStartTrigger
	Inherits MarshalByRefObject
	Implements IFilteredTypeDescriptor
```

The AnalogEdgeStartTrigger type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Coupling | Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel. |
|  | DigitalFilterEnable | Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay above or below the trigger level for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the hysteresis window rapidly. |
|  | DigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | DigitalFilterTimebaseRate | Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | DigitalFilterTimebaseSource | Specifies the terminal of the signal to use as the timebase of the digital filter. |
|  | DigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | Hysteresis | Specifies a hysteresis level in the units of the measurement or generation. If Slope is Rising, the trigger does not deassert until the source signal passes below Level minus the hysteresis. If Slope is Falling, the trigger does not deassert until the source signal passes above Level plus the hysteresis. Hysteresis is always enabled. Set this property to a non-zero value to use hysteresis. |
|  | Level | Specifies at what threshold in the units of the measurement or generation to start acquiring or generating samples. Use Slope to specify on which slope to trigger on this threshold. |
|  | Slope | Specifies on which slope of the trigger signal to start acquiring or generating samples. |
|  | Source | Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the Start Trigger. |

Top

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

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_analogedgestarttriggercoupling.htm language=enus -->
## TOPIC 00916: AnalogEdgeStartTriggerCoupling Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_analogedgestarttriggercoupling.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_analogedgestarttriggercoupling.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogEdgeStartTriggerCoupling Enumeration

### AnalogEdgeStartTriggerCoupling Enumeration

terminal

virtual channel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AnalogEdgeStartTriggerCoupling
```

```text
Public Enumeration AnalogEdgeStartTriggerCoupling
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | AC | 10045 | Alternating Current. |
|  | DC | 10050 | Direct Current. |

##### Remarks

terminal

virtual channel

Coupling

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_analogedgestarttriggerslope.htm language=enus -->
## TOPIC 00917: AnalogEdgeStartTriggerSlope Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_analogedgestarttriggerslope.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_analogedgestarttriggerslope.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogEdgeStartTriggerSlope Enumeration

### AnalogEdgeStartTriggerSlope Enumeration

Specifies on which slope of the trigger signal to start acquiring or generating samples.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AnalogEdgeStartTriggerSlope
```

```text
Public Enumeration AnalogEdgeStartTriggerSlope
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Rising | 10280 | Trigger on the rising slope of the signal. |
|  | Falling | 10171 | Trigger on the falling slope of the signal. |

##### Remarks

Slope

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_analogmultiedgereferencetriggerslope.htm language=enus -->
## TOPIC 00918: AnalogMultiEdgeReferenceTriggerSlope Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_analogmultiedgereferencetriggerslope.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_analogmultiedgereferencetriggerslope.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiEdgeReferenceTriggerSlope Enumeration

### AnalogMultiEdgeReferenceTriggerSlope Enumeration

Specifies an array of slopes on which to trigger task to start generating or acquiring samples. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AnalogMultiEdgeReferenceTriggerSlope
```

```text
Public Enumeration AnalogMultiEdgeReferenceTriggerSlope
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Rising | 10280 | Trigger on the rising slope of the signal. |
|  | Falling | 10171 | Trigger on the falling slope of the signal. |

##### Remarks

Slopes

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_analogmultiedgestarttriggerslope.htm language=enus -->
## TOPIC 00919: AnalogMultiEdgeStartTriggerSlope Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_analogmultiedgestarttriggerslope.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_analogmultiedgestarttriggerslope.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiEdgeStartTriggerSlope Enumeration

### AnalogMultiEdgeStartTriggerSlope Enumeration

Specifies an array of slopes on which to trigger task to start generating or acquiring samples. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AnalogMultiEdgeStartTriggerSlope
```

```text
Public Enumeration AnalogMultiEdgeStartTriggerSlope
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Rising | 10280 | Trigger on the rising slope of the signal. |
|  | Falling | 10171 | Trigger on the falling slope of the signal. |

##### Remarks

Slopes

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aodacreferencesource.htm language=enus -->
## TOPIC 00920: AODacReferenceSource Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aodacreferencesource.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aodacreferencesource.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AODacReferenceSource Enumeration

### AODacReferenceSource Enumeration

Specifies the source of the DAC reference voltage. The value of this voltage source determines the full-scale value of the DAC.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AODacReferenceSource
```

```text
Public Enumeration AODacReferenceSource
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Internal | 10200 | Internal to the device. |
|  | External | 10167 | External to the device. |

##### Remarks

DacReferenceSource

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aodatatransferrequestcondition.htm language=enus -->
## TOPIC 00921: AODataTransferRequestCondition Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aodatatransferrequestcondition.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aodatatransferrequestcondition.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AODataTransferRequestCondition Enumeration

### AODataTransferRequestCondition Enumeration

Specifies under what condition to transfer data from the buffer to the onboard memory of the device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AODataTransferRequestCondition
```

```text
Public Enumeration AODataTransferRequestCondition
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | OnBoardMemoryEmpty | 10235 | Transfer data to the device only when there is no data in the onboard memory of the device. |
|  | OnBoardMemoryHalfFullOrLess | 10239 | Transfer data to the device any time the onboard memory is less than half full. |
|  | OnBoardMemoryNotFull | 10242 | Transfer data to the device any time the onboard memory of the device is not full. |

##### Remarks

DataTransferRequestCondition

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aofilterdelayunits.htm language=enus -->
## TOPIC 00922: AOFilterDelayUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aofilterdelayunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aofilterdelayunits.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AOFilterDelayUnits Enumeration

### AOFilterDelayUnits Enumeration

FilterDelay

FilterDelayAdjustment

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AOFilterDelayUnits
```

```text
Public Enumeration AOFilterDelayUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Seconds | 10364 | Seconds. |
|  | SampleClockPeriods | 10286 | Sample Clock Periods. |

##### Remarks

FilterDelay

FilterDelayAdjustment

FilterDelayUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aofunctiongenerationmodulationtype.htm language=enus -->
## TOPIC 00923: AOFunctionGenerationModulationType Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aofunctiongenerationmodulationtype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aofunctiongenerationmodulationtype.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AOFunctionGenerationModulationType Enumeration

### AOFunctionGenerationModulationType Enumeration

Specifies if the device generates a modulated version of the waveform using the original waveform as a carrier and input from an external terminal as the signal.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AOFunctionGenerationModulationType
```

```text
Public Enumeration AOFunctionGenerationModulationType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | AM | 14756 | Amplitude modulation. |
|  | FM | 14757 | Frequency modulation. |
|  | None | 10230 | No modulation. |

##### Remarks

FunctionGenerationModulationType

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aofunctiongenerationtype.htm language=enus -->
## TOPIC 00924: AOFunctionGenerationType Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aofunctiongenerationtype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aofunctiongenerationtype.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AOFunctionGenerationType Enumeration

### AOFunctionGenerationType Enumeration

Specifies the kind of the waveform to generate.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AOFunctionGenerationType
```

```text
Public Enumeration AOFunctionGenerationType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Sine | 14751 | Sine wave. |
|  | Triangle | 14752 | Triangle wave. |
|  | Square | 14753 | Square wave. |
|  | Sawtooth | 14754 | Sawtooth wave. |

##### Remarks

FunctionGenerationType

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aoidleoutputbehavior.htm language=enus -->
## TOPIC 00925: AOIdleOutputBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aoidleoutputbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aoidleoutputbehavior.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AOIdleOutputBehavior Enumeration

### AOIdleOutputBehavior Enumeration

Specifies the state of the channel when no generation is in progress.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AOIdleOutputBehavior
```

```text
Public Enumeration AOIdleOutputBehavior
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | ZeroVolts | 12526 | Generate 0 V. |
|  | HighImpedance | 12527 | Set the channel to high-impedance, effectively disconnecting the analog output circuitry from the I/O connector. |
|  | MaintainExistingValue | 12528 | Continue generating the current value. |

##### Remarks

IdleOutputBehavior

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aoresolutionunits.htm language=enus -->
## TOPIC 00926: AOResolutionUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aoresolutionunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aoresolutionunits.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AOResolutionUnits Enumeration

### AOResolutionUnits Enumeration

Resolution

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AOResolutionUnits
```

```text
Public Enumeration AOResolutionUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Bits | 10109 | Bits. |

##### Remarks

Resolution

ResolutionUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aoterminalconfiguration.htm language=enus -->
## TOPIC 00927: AOTerminalConfiguration Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aoterminalconfiguration.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_aoterminalconfiguration.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AOTerminalConfiguration Enumeration

### AOTerminalConfiguration Enumeration

Specifies the terminal configuration of the channel.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AOTerminalConfiguration
```

```text
Public Enumeration AOTerminalConfiguration
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Rse | 10083 | Referenced Single-Ended. |
|  | Differential | 10106 | Differential. |
|  | Pseudodifferential | 12529 | Pseudodifferential. |

##### Remarks

TerminalConfiguration

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_armstarttrigger.htm language=enus -->
## TOPIC 00928: ArmStartTrigger Class

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_armstarttrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_armstarttrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ArmStartTrigger Class

### ArmStartTrigger Class

arms the task for a start trigger

StartTrigger

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class ArmStartTrigger : MarshalByRefObject, 
	IFilteredTypeDescriptor
```

```text
Public Class ArmStartTrigger
	Inherits MarshalByRefObject
	Implements IFilteredTypeDescriptor
```

The ArmStartTrigger type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | DigitalEdge | Gets the DigitalEdgeArmStartTrigger. |
|  | Terminal | Indicates the name of the internal Arm Start Trigger terminal for the task. This property does not return the name of the trigger source terminal. |
|  | Time | Gets the TimeArmStartTrigger. |
|  | Timestamp | Gets the arm start trigger timestamp. |
|  | TimestampEnable | Specifies whether the arm start trigger timestamp is enabled. If the timestamp is enabled but no resources are available, an error will be returned at run time. |
|  | TimestampTimescale | Specifies the arm start trigger timestamp timescale. |
|  | Type | Specifies the type of trigger to use to arm the task for a Start Trigger. If you configure an Arm Start Trigger, the task does not respond to a Start Trigger until the device receives the Arm Start Trigger. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureDigitalEdgeTrigger | Configures a task to arm for a start trigger upon a rising or falling edge of a digital signal. |
|  | ConfigureNone | Disables arm start triggering for the task. |
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

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_armstarttriggertype.htm language=enus -->
## TOPIC 00929: ArmStartTriggerType Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_armstarttriggertype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_armstarttriggertype.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ArmStartTriggerType Enumeration

### ArmStartTriggerType Enumeration

Specifies the type of trigger to use to arm the task for a Start Trigger. If you configure an Arm Start Trigger, the task does not respond to a Start Trigger until the device receives the Arm Start Trigger.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum ArmStartTriggerType
```

```text
Public Enumeration ArmStartTriggerType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | DigitalEdge | 10150 | Trigger on a rising or falling edge of a digital signal. |
|  | Time | 15996 | Trigger when a specified time is reached. |
|  | None | 10230 | Disable the trigger. |

##### Remarks

Type

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_basictedsdataoption.htm language=enus -->
## TOPIC 00930: BasicTedsDataOption Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_basictedsdataoption.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_basictedsdataoption.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

BasicTedsDataOption Enumeration

### BasicTedsDataOption Enumeration

basic TEDS data

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum BasicTedsDataOption
```

```text
Public Enumeration BasicTedsDataOption
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | WriteToEeprom | 12538 | Basic TEDS data is written to the EEPROM, even if the sensor includes a PROM. You cannot write basic TEDS data if the PROM contains data. |
|  | WriteToProm | 12539 | Basic TEDS data is written to the PROM. Any subsequent attempts to write basic TEDS data results in an error. |
|  | DoNotWrite | 12540 | Basic TEDS data is ignored. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_calibrationinputterminalconfiguration4463.htm language=enus -->
## TOPIC 00931: CalibrationInputTerminalConfiguration4463 Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_calibrationinputterminalconfiguration4463.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_calibrationinputterminalconfiguration4463.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CalibrationInputTerminalConfiguration4463 Enumeration

### CalibrationInputTerminalConfiguration4463 Enumeration

Specifies the input terminal configuration for the channel to calibrate on an NI PXIe 4463 device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CalibrationInputTerminalConfiguration4463
```

```text
Public Enumeration CalibrationInputTerminalConfiguration4463
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Differential | 10106 | A differential input terminal configuration. |
|  | Pseudodifferential | 12529 | A pseudodifferential input terminal configuration. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_calibrationinputterminalconfiguration9209.htm language=enus -->
## TOPIC 00932: CalibrationInputTerminalConfiguration9209 Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_calibrationinputterminalconfiguration9209.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_calibrationinputterminalconfiguration9209.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CalibrationInputTerminalConfiguration9209 Enumeration

### CalibrationInputTerminalConfiguration9209 Enumeration

Specifies the input terminal configuration for the channel to calibrate on an NI 9209 device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CalibrationInputTerminalConfiguration9209
```

```text
Public Enumeration CalibrationInputTerminalConfiguration9209
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Rse | 10083 | A referenced single-ended input terminal configuration. |
|  | Differential | 10106 | A differential input terminal configuration. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_calibrationmode4339.htm language=enus -->
## TOPIC 00933: CalibrationMode4339 Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_calibrationmode4339.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_calibrationmode4339.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CalibrationMode4339 Enumeration

### CalibrationMode4339 Enumeration

Specifies which measurements to use to calibrate an NI 4339 device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CalibrationMode4339
```

```text
Public Enumeration CalibrationMode4339
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Voltage | 10322 | Voltage mode. |
|  | Ratiometric | 15908 | Ratiometric mode. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_changedetectioneventpulsepolarity.htm language=enus -->
## TOPIC 00934: ChangeDetectionEventPulsePolarity Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_changedetectioneventpulsepolarity.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_changedetectioneventpulsepolarity.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ChangeDetectionEventPulsePolarity Enumeration

### ChangeDetectionEventPulsePolarity Enumeration

Specifies the polarity of an exported Change Detection Event pulse.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum ChangeDetectionEventPulsePolarity
```

```text
Public Enumeration ChangeDetectionEventPulsePolarity
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | ActiveHigh | 10095 | High state is the active state. |
|  | ActiveLow | 10096 | Low state is the active state. |

##### Remarks

ChangeDetectionEventPulsePolarity

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cicountedgesactiveedge.htm language=enus -->
## TOPIC 00935: CICountEdgesActiveEdge Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cicountedgesactiveedge.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cicountedgesactiveedge.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CICountEdgesActiveEdge Enumeration

### CICountEdgesActiveEdge Enumeration

Specifies on which edges to increment or decrement the counter.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CICountEdgesActiveEdge
```

```text
Public Enumeration CICountEdgesActiveEdge
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Rising | 10280 | Rising edge(s). |
|  | Falling | 10171 | Falling edge(s). |

##### Remarks

CountEdgesActiveEdge

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cicountedgescountdirection.htm language=enus -->
## TOPIC 00936: CICountEdgesCountDirection Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cicountedgescountdirection.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cicountedgescountdirection.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CICountEdgesCountDirection Enumeration

### CICountEdgesCountDirection Enumeration

Specifies whether to increment or decrement the counter on each edge.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CICountEdgesCountDirection
```

```text
Public Enumeration CICountEdgesCountDirection
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Up | 10128 | Increment counter. |
|  | Down | 10124 | Decrement counter. |
|  | ExternallyControlled | 10326 | The state of a digital line controls the count direction. Each counter has a default count direction terminal. |

##### Remarks

CountEdgesCountDirection

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cicountedgescountdirectionlogiclevelbehavior.htm language=enus -->
## TOPIC 00937: CICountEdgesCountDirectionLogicLevelBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cicountedgescountdirectionlogiclevelbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cicountedgescountdirectionlogiclevelbehavior.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CICountEdgesCountDirectionLogicLevelBehavior Enumeration

### CICountEdgesCountDirectionLogicLevelBehavior Enumeration

Specifies the logic level behavior on the count reset line.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CICountEdgesCountDirectionLogicLevelBehavior
```

```text
Public Enumeration CICountEdgesCountDirectionLogicLevelBehavior
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | LogicLevelPullUp | 16064 | High logic. |
|  | None | 10230 | Supply no excitation to the channel. |

##### Remarks

CountEdgesCountDirectionLogicLevelBehavior

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cicountedgescountresetlogiclevelbehavior.htm language=enus -->
## TOPIC 00938: CICountEdgesCountResetLogicLevelBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cicountedgescountresetlogiclevelbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cicountedgescountresetlogiclevelbehavior.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CICountEdgesCountResetLogicLevelBehavior Enumeration

### CICountEdgesCountResetLogicLevelBehavior Enumeration

Specifies the logic level behavior on the count reset line.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CICountEdgesCountResetLogicLevelBehavior
```

```text
Public Enumeration CICountEdgesCountResetLogicLevelBehavior
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | LogicLevelPullUp | 16064 | High logic. |
|  | None | 10230 | Supply no excitation to the channel. |

##### Remarks

CountEdgesCountResetLogicLevelBehavior

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cicountedgesgatelogiclevelbehavior.htm language=enus -->
## TOPIC 00939: CICountEdgesGateLogicLevelBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cicountedgesgatelogiclevelbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cicountedgesgatelogiclevelbehavior.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CICountEdgesGateLogicLevelBehavior Enumeration

### CICountEdgesGateLogicLevelBehavior Enumeration

Specifies the logic level behavior on the gate input line.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CICountEdgesGateLogicLevelBehavior
```

```text
Public Enumeration CICountEdgesGateLogicLevelBehavior
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | LogicLevelPullUp | 16064 | High logic. |
|  | None | 10230 | Supply no excitation to the channel. |

##### Remarks

CountEdgesGateLogicLevelBehavior

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cicountedgesgatepausestate.htm language=enus -->
## TOPIC 00940: CICountEdgesGatePauseState Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cicountedgesgatepausestate.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cicountedgesgatepausestate.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CICountEdgesGatePauseState Enumeration

### CICountEdgesGatePauseState Enumeration

Specifies whether the counter gates input pulses while the signal is high or low.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CICountEdgesGatePauseState
```

```text
Public Enumeration CICountEdgesGatePauseState
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | High | 10192 | High state. |
|  | Low | 10214 | Low state. |

##### Remarks

CountEdgesGatePauseState

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cicountedgesgateterminalconfiguration.htm language=enus -->
## TOPIC 00941: CICountEdgesGateTerminalConfiguration Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cicountedgesgateterminalconfiguration.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cicountedgesgateterminalconfiguration.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CICountEdgesGateTerminalConfiguration Enumeration

### CICountEdgesGateTerminalConfiguration Enumeration

Specifies the gate terminal configuration.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CICountEdgesGateTerminalConfiguration
```

```text
Public Enumeration CICountEdgesGateTerminalConfiguration
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Differential | 10106 | Differential. |
|  | Rse | 10083 | Referenced Single-Ended. |

##### Remarks

CountEdgesGateTerminalConfiguration

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cidatafrequency.htm language=enus -->
## TOPIC 00942: CIDataFrequency Structure

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cidatafrequency.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cidatafrequency.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CIDataFrequency Structure

### CIDataFrequency Structure

duty cycle

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[SerializableAttribute]
public struct CIDataFrequency : ISerializable
```

```text
<SerializableAttribute>
Public Structure CIDataFrequency
	Implements ISerializable
```

The CIDataFrequency type exposes the following members.

##### Constructors

|  | Name | Description |
| --- | --- | --- |
|  | CIDataFrequency | Initializes a new instance of the CIDataFrequency object with the specified frequency and duty cycle. |

Top

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | DutyCycle | Gets or sets the duty cycle of the pulse. |
|  | Frequency | Gets or sets the frequency of the pulse. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals(Object) | Returns a value indicating if this instance is equal to the specified object. (Overrides ValueTypeEquals(Object).) |
|  | Equals(CIDataFrequency) | Returns a value indicating if this instance is equal to the specified CIDataFrequency object. |
|  | Equals(CIDataFrequency, CIDataFrequency) | Returns a value indicating if two specified instances of CIDataFrequency are equal. |
|  | GetHashCode | Returns a hash code for the CIDataFrequency object. (Overrides ValueTypeGetHashCode.) |
|  | GetObjectData | Sets the SerializationInfo object with information about the exception. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns the fully qualified type name of this instance. (Inherited from ValueType.) |

Top

##### Operators

|  | Name | Description |
| --- | --- | --- |
|  | Equality | Returns if two CIDataFrequency objects are equal. |
|  | Inequality | Returns if two CIDataFrequency objects are not equal. |

Top

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cidataticks.htm language=enus -->
## TOPIC 00943: CIDataTicks Structure

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cidataticks.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cidataticks.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CIDataTicks Structure

### CIDataTicks Structure

Encapsulates a counter input specified in terms of timebase ticks.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[SerializableAttribute]
public struct CIDataTicks : ISerializable
```

```text
<SerializableAttribute>
Public Structure CIDataTicks
	Implements ISerializable
```

The CIDataTicks type exposes the following members.

##### Constructors

|  | Name | Description |
| --- | --- | --- |
|  | CIDataTicks(Int32, Int32) | Initializes a new instance of the CIDataTicks object with the specified initial values. |
|  | CIDataTicks(UInt32, UInt32) | Initializes a new instance of the CIDataTicks object with the specified unsigned initial values. |

Top

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | HighTicksInt32 | Gets or sets the number of timebase ticks the pulse is high. |
|  | HighTicksUInt32 | Gets or sets the number of timebase ticks the pulse is high. |
|  | LowTicksInt32 | Gets or sets the number of timebase ticks the pulse is low. |
|  | LowTicksUInt32 | Gets or sets the number of timebase ticks the pulse is low. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals(Object) | Returns a value indicating if this instance is equal to the specified object. (Overrides ValueTypeEquals(Object).) |
|  | Equals(CIDataTicks) | Returns a value indicating if this instance is equal to the specified CIDataTicks object. |
|  | Equals(CIDataTicks, CIDataTicks) | Returns a value indicating if two specified instances of CIDataTicks are equal. |
|  | GetHashCode | Returns a hash code for the CIDataTicks object. (Overrides ValueTypeGetHashCode.) |
|  | GetObjectData | Sets the SerializationInfo object with information about the exception. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns the fully qualified type name of this instance. (Inherited from ValueType.) |

Top

##### Operators

|  | Name | Description |
| --- | --- | --- |
|  | Equality | Returns if two CIDataTicks objects are equal. |
|  | Inequality | Returns if two CIDataTicks objects are not equal. |

Top

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cidatatime.htm language=enus -->
## TOPIC 00944: CIDataTime Structure

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cidatatime.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cidatatime.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CIDataTime Structure

### CIDataTime Structure

Encapsulates a counter input specified in terms of time.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[SerializableAttribute]
public struct CIDataTime : ISerializable
```

```text
<SerializableAttribute>
Public Structure CIDataTime
	Implements ISerializable
```

The CIDataTime type exposes the following members.

##### Constructors

|  | Name | Description |
| --- | --- | --- |
|  | CIDataTime | Initializes a new instance of the CIDataTime object with the specified time. |

Top

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | HighTime | Gets or sets the amount of time the pulse is high. |
|  | LowTime | Gets or sets the amount of time the pulse is low. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals(Object) | Returns a value indicating if this instance is equal to the specified object. (Overrides ValueTypeEquals(Object).) |
|  | Equals(CIDataTime) | Returns a value indicating if this instance is equal to the specified CIDataTime object. |
|  | Equals(CIDataTime, CIDataTime) | Returns a value indicating if two specified instances of CIDataTime are equal. |
|  | GetHashCode | Returns a hash code for the CIDataTime object. (Overrides ValueTypeGetHashCode.) |
|  | GetObjectData | Sets the SerializationInfo object with information about the exception. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns the fully qualified type name of this instance. (Inherited from ValueType.) |

Top

##### Operators

|  | Name | Description |
| --- | --- | --- |
|  | Equality | Returns if two CIDataTime objects are equal. |
|  | Inequality | Returns if two CIDataTime objects are not equal. |

Top

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_ciencoderainputterminalconfiguration.htm language=enus -->
## TOPIC 00945: CIEncoderAInputTerminalConfiguration Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_ciencoderainputterminalconfiguration.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_ciencoderainputterminalconfiguration.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CIEncoderAInputTerminalConfiguration Enumeration

### CIEncoderAInputTerminalConfiguration Enumeration

Specifies the input terminal configuration.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CIEncoderAInputTerminalConfiguration
```

```text
Public Enumeration CIEncoderAInputTerminalConfiguration
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Differential | 10106 | Differential. |
|  | Rse | 10083 | Referenced Single-Ended. |

##### Remarks

EncoderAInputTerminalConfiguration

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_ciencoderzinputterminalconfiguration.htm language=enus -->
## TOPIC 00946: CIEncoderZInputTerminalConfiguration Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_ciencoderzinputterminalconfiguration.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_ciencoderzinputterminalconfiguration.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CIEncoderZInputTerminalConfiguration Enumeration

### CIEncoderZInputTerminalConfiguration Enumeration

Specifies the input terminal configuration.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CIEncoderZInputTerminalConfiguration
```

```text
Public Enumeration CIEncoderZInputTerminalConfiguration
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Differential | 10106 | Differential. |
|  | Rse | 10083 | Referenced Single-Ended. |

##### Remarks

EncoderZInputTerminalConfiguration

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cifilterdelayunits.htm language=enus -->
## TOPIC 00947: CIFilterDelayUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cifilterdelayunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cifilterdelayunits.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CIFilterDelayUnits Enumeration

### CIFilterDelayUnits Enumeration

FilterDelay

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CIFilterDelayUnits
```

```text
Public Enumeration CIFilterDelayUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Seconds | 10364 | Seconds. |
|  | SampleClockPeriods | 10286 | Sample Clock Periods. |

##### Remarks

FilterDelay

FilterDelayUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cifilterresponse.htm language=enus -->
## TOPIC 00948: CIFilterResponse Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cifilterresponse.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cifilterresponse.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CIFilterResponse Enumeration

### CIFilterResponse Enumeration

Specifies the corresponding filter response and defines the shape of the filter response.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CIFilterResponse
```

```text
Public Enumeration CIFilterResponse
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Comb | 16152 | Comb filter response. |
|  | Bessel | 16153 | Bessel filter response. |
|  | Brickwall | 16155 | Brickwall filter response. |
|  | Butterworth | 16076 | Butterworth filter response. |

##### Remarks

FilterResponse

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cifrequencylogiclevelbehavior.htm language=enus -->
## TOPIC 00949: CIFrequencyLogicLevelBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cifrequencylogiclevelbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cifrequencylogiclevelbehavior.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CIFrequencyLogicLevelBehavior Enumeration

### CIFrequencyLogicLevelBehavior Enumeration

Specifies the logic level behavior on the input line.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CIFrequencyLogicLevelBehavior
```

```text
Public Enumeration CIFrequencyLogicLevelBehavior
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | LogicLevelPullUp | 16064 | High logic. |
|  | None | 10230 | Supply no excitation to the channel. |

##### Remarks

FrequencyLogicalLevelBehavior

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cifrequencyterminalconfiguration.htm language=enus -->
## TOPIC 00950: CIFrequencyTerminalConfiguration Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cifrequencyterminalconfiguration.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cifrequencyterminalconfiguration.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CIFrequencyTerminalConfiguration Enumeration

### CIFrequencyTerminalConfiguration Enumeration

Specifies the input terminal configuration.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CIFrequencyTerminalConfiguration
```

```text
Public Enumeration CIFrequencyTerminalConfiguration
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Differential | 10106 | Differential. |
|  | Rse | 10083 | Referenced Single-Ended. |

##### Remarks

FrequencyTerminalConfiguration

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cifrequencyunits.htm language=enus -->
## TOPIC 00951: CIFrequencyUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cifrequencyunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cifrequencyunits.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CIFrequencyUnits Enumeration

### CIFrequencyUnits Enumeration

Specifies the units to use to return frequency measurements.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CIFrequencyUnits
```

```text
Public Enumeration CIFrequencyUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Hertz | 10373 | Hertz. |
|  | Ticks | 10304 | Timebase ticks. |
|  | FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

##### Remarks

FrequencyUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cioutputstate.htm language=enus -->
## TOPIC 00952: CIOutputState Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cioutputstate.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cioutputstate.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CIOutputState Enumeration

### CIOutputState Enumeration

out terminal

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CIOutputState
```

```text
Public Enumeration CIOutputState
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | High | 10192 | High state. |
|  | Low | 10214 | Low state. |

##### Remarks

out terminal

OutputState

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cipulsefrequencystartingedge.htm language=enus -->
## TOPIC 00953: CIPulseFrequencyStartingEdge Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cipulsefrequencystartingedge.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cipulsefrequencystartingedge.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CIPulseFrequencyStartingEdge Enumeration

### CIPulseFrequencyStartingEdge Enumeration

Specifies on which edge of the input signal to begin pulse measurement.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CIPulseFrequencyStartingEdge
```

```text
Public Enumeration CIPulseFrequencyStartingEdge
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Rising | 10280 | Rising edge(s). |
|  | Falling | 10171 | Falling edge(s). |

##### Remarks

PulseFrequencyStartingEdge

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cipulsefrequencyterminalconfiguration.htm language=enus -->
## TOPIC 00954: CIPulseFrequencyTerminalConfiguration Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cipulsefrequencyterminalconfiguration.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cipulsefrequencyterminalconfiguration.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CIPulseFrequencyTerminalConfiguration Enumeration

### CIPulseFrequencyTerminalConfiguration Enumeration

Specifies the input terminal configuration.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CIPulseFrequencyTerminalConfiguration
```

```text
Public Enumeration CIPulseFrequencyTerminalConfiguration
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Differential | 10106 | Differential. |
|  | Rse | 10083 | Referenced Single-Ended. |

##### Remarks

PulseFrequencyTerminalConfiguration

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cipulsefrequencyunits.htm language=enus -->
## TOPIC 00955: CIPulseFrequencyUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cipulsefrequencyunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cipulsefrequencyunits.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CIPulseFrequencyUnits Enumeration

### CIPulseFrequencyUnits Enumeration

Specifies the units to use to return pulse specifications in terms of frequency.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CIPulseFrequencyUnits
```

```text
Public Enumeration CIPulseFrequencyUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Hertz | 10373 | Hertz. |

##### Remarks

PulseFrequencyUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cipulsetickslogiclevelbehavior.htm language=enus -->
## TOPIC 00956: CIPulseTicksLogicLevelBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cipulsetickslogiclevelbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cipulsetickslogiclevelbehavior.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CIPulseTicksLogicLevelBehavior Enumeration

### CIPulseTicksLogicLevelBehavior Enumeration

Specifies the logic level behavior on the count reset line.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CIPulseTicksLogicLevelBehavior
```

```text
Public Enumeration CIPulseTicksLogicLevelBehavior
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | LogicLevelPullUp | 16064 | High logic. |
|  | None | 10230 | Supply no excitation to the channel. |

##### Remarks

PulseTicksLogicLevelBehavior

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cipulseticksterminalconfiguration.htm language=enus -->
## TOPIC 00957: CIPulseTicksTerminalConfiguration Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cipulseticksterminalconfiguration.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cipulseticksterminalconfiguration.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CIPulseTicksTerminalConfiguration Enumeration

### CIPulseTicksTerminalConfiguration Enumeration

Specifies the input terminal configuration.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CIPulseTicksTerminalConfiguration
```

```text
Public Enumeration CIPulseTicksTerminalConfiguration
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Differential | 10106 | Differential. |
|  | Rse | 10083 | Referenced Single-Ended. |

##### Remarks

PulseTicksTerminalConfiguration

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cipulsetimelogiclevelbehavior.htm language=enus -->
## TOPIC 00958: CIPulseTimeLogicLevelBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cipulsetimelogiclevelbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cipulsetimelogiclevelbehavior.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CIPulseTimeLogicLevelBehavior Enumeration

### CIPulseTimeLogicLevelBehavior Enumeration

Specifies the logic level behavior on the count reset line.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CIPulseTimeLogicLevelBehavior
```

```text
Public Enumeration CIPulseTimeLogicLevelBehavior
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | LogicLevelPullUp | 16064 | High logic. |
|  | None | 10230 | Supply no excitation to the channel. |

##### Remarks

PulseTimeLogicLevelBehavior

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cipulsetimestartingedge.htm language=enus -->
## TOPIC 00959: CIPulseTimeStartingEdge Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cipulsetimestartingedge.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cipulsetimestartingedge.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CIPulseTimeStartingEdge Enumeration

### CIPulseTimeStartingEdge Enumeration

Specifies on which edge of the input signal to begin pulse measurement.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CIPulseTimeStartingEdge
```

```text
Public Enumeration CIPulseTimeStartingEdge
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Rising | 10280 | Rising edge(s). |
|  | Falling | 10171 | Falling edge(s). |

##### Remarks

PulseTimeStartingEdge

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cipulsetimeterminalconfiguration.htm language=enus -->
## TOPIC 00960: CIPulseTimeTerminalConfiguration Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cipulsetimeterminalconfiguration.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cipulsetimeterminalconfiguration.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CIPulseTimeTerminalConfiguration Enumeration

### CIPulseTimeTerminalConfiguration Enumeration

Specifies the input terminal configuration.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CIPulseTimeTerminalConfiguration
```

```text
Public Enumeration CIPulseTimeTerminalConfiguration
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Differential | 10106 | Differential. |
|  | Rse | 10083 | Referenced Single-Ended. |

##### Remarks

PulseTimeTerminalConfiguration

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cisemiperiodunits.htm language=enus -->
## TOPIC 00961: CISemiPeriodUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cisemiperiodunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cisemiperiodunits.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CISemiPeriodUnits Enumeration

### CISemiPeriodUnits Enumeration

Specifies the units to use to return semi-period measurements.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CISemiPeriodUnits
```

```text
Public Enumeration CISemiPeriodUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Seconds | 10364 | Seconds. |
|  | Ticks | 10304 | Timebase ticks. |
|  | FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

##### Remarks

SemiPeriodUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_citimestampunits.htm language=enus -->
## TOPIC 00962: CITimestampUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_citimestampunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_citimestampunits.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CITimestampUnits Enumeration

### CITimestampUnits Enumeration

Specifies the units to use to return timestamp measurements.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CITimestampUnits
```

```text
Public Enumeration CITimestampUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Seconds | 10364 | Seconds. |
|  | FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

##### Remarks

TimestampUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_citwoedgeseparationsecondedge.htm language=enus -->
## TOPIC 00963: CITwoEdgeSeparationSecondEdge Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_citwoedgeseparationsecondedge.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_citwoedgeseparationsecondedge.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CITwoEdgeSeparationSecondEdge Enumeration

### CITwoEdgeSeparationSecondEdge Enumeration

Specifies on which edge of the second signal to stop each measurement.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CITwoEdgeSeparationSecondEdge
```

```text
Public Enumeration CITwoEdgeSeparationSecondEdge
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Rising | 10280 | Rising edge(s). |
|  | Falling | 10171 | Falling edge(s). |

##### Remarks

TwoEdgeSeparationSecondEdge

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_citwoedgeseparationsecondlogiclevelbehavior.htm language=enus -->
## TOPIC 00964: CITwoEdgeSeparationSecondLogicLevelBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_citwoedgeseparationsecondlogiclevelbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_citwoedgeseparationsecondlogiclevelbehavior.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CITwoEdgeSeparationSecondLogicLevelBehavior Enumeration

### CITwoEdgeSeparationSecondLogicLevelBehavior Enumeration

Specifies the logic level behavior on the count reset line.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CITwoEdgeSeparationSecondLogicLevelBehavior
```

```text
Public Enumeration CITwoEdgeSeparationSecondLogicLevelBehavior
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | LogicLevelPullUp | 16064 | High logic. |
|  | None | 10230 | Supply no excitation to the channel. |

##### Remarks

TwoEdgeSeparationSecondLogicLevelBehavior

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_citwoedgeseparationsecondterminalconfiguration.htm language=enus -->
## TOPIC 00965: CITwoEdgeSeparationSecondTerminalConfiguration Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_citwoedgeseparationsecondterminalconfiguration.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_citwoedgeseparationsecondterminalconfiguration.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CITwoEdgeSeparationSecondTerminalConfiguration Enumeration

### CITwoEdgeSeparationSecondTerminalConfiguration Enumeration

Specifies the input terminal configuration.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CITwoEdgeSeparationSecondTerminalConfiguration
```

```text
Public Enumeration CITwoEdgeSeparationSecondTerminalConfiguration
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Differential | 10106 | Differential. |
|  | Rse | 10083 | Referenced Single-Ended. |

##### Remarks

TwoEdgeSeparationSecondTerminalConfiguration

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_civelocityainputlogiclevelbehavior.htm language=enus -->
## TOPIC 00966: CIVelocityAInputLogicLevelBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_civelocityainputlogiclevelbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_civelocityainputlogiclevelbehavior.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CIVelocityAInputLogicLevelBehavior Enumeration

### CIVelocityAInputLogicLevelBehavior Enumeration

Specifies the logic level behavior of the input terminal.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CIVelocityAInputLogicLevelBehavior
```

```text
Public Enumeration CIVelocityAInputLogicLevelBehavior
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | LogicLevelPullUp | 16064 | High logic. |
|  | None | 10230 | Supply no excitation to the channel. |

##### Remarks

VelocityAInputLogicLevelBehavior

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_civelocityainputterminalconfiguration.htm language=enus -->
## TOPIC 00967: CIVelocityAInputTerminalConfiguration Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_civelocityainputterminalconfiguration.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_civelocityainputterminalconfiguration.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CIVelocityAInputTerminalConfiguration Enumeration

### CIVelocityAInputTerminalConfiguration Enumeration

Specifies the input terminal configuration.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CIVelocityAInputTerminalConfiguration
```

```text
Public Enumeration CIVelocityAInputTerminalConfiguration
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Differential | 10106 | Differential. |
|  | Rse | 10083 | Referenced Single-Ended. |

##### Remarks

VelocityAInputTerminalConfiguration

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_civelocityangularencoderunits.htm language=enus -->
## TOPIC 00968: CIVelocityAngularEncoderUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_civelocityangularencoderunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_civelocityangularencoderunits.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CIVelocityAngularEncoderUnits Enumeration

### CIVelocityAngularEncoderUnits Enumeration

Specifies the units to use to return angular velocity counter measurements.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CIVelocityAngularEncoderUnits
```

```text
Public Enumeration CIVelocityAngularEncoderUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | RPM | 16080 | Revolutions per minute. |
|  | RadiansPerSecond | 16081 | Radians per second. |
|  | DegreesPerSecond | 16082 | Degrees per second. |
|  | FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

##### Remarks

VelocityAngularEncoderUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cochannel.htm language=enus -->
## TOPIC 00969: COChannel Class

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cochannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cochannel.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

COChannel Class

### COChannel Class

Encapsulates one or more counter/timer output channels and the properties for a counter/timer output channel.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class COChannel : Channel, IFilteredTypeDescriptor
```

```text
Public Class COChannel
	Inherits Channel
	Implements IFilteredTypeDescriptor
```

The COChannel type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | AutoIncrementCount | Specifies a number of timebase ticks by which to increase the time spent in the idle state for each successive pulse. |
|  | ConstrainedGenerationMode | Specifies constraints to apply when the counter generates pulses. Constraining the counter reduces the device resources required for counter operation. Constraining the counter can also allow additional analog or counter tasks on the device to run concurrently. For continuous counter tasks, NI-DAQmx consumes no device resources when the counter is constrained. For finite counter tasks, resource use increases with the frequency regardless of the constraint mode. However, fixed frequency constraints significantly reduce resource usage, and fixed duty cycle constraint marginally reduces it. |
|  | Count | Indicates the current value of the count register. |
|  | CounterTimebaseActiveEdge | Specifies whether a timebase cycle is from rising edge to rising edge or from falling edge to falling edge. |
|  | CounterTimebaseDigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
|  | CounterTimebaseDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | CounterTimebaseDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | CounterTimebaseDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | CounterTimebaseDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | CounterTimebaseMasterTimebaseDivisor | Specifies the divisor for an external counter timebase. You can divide the counter timebase in order to generate slower signals without causing the count register to roll over. |
|  | CounterTimebaseRate | Specifies in Hertz the frequency of the counter timebase. Specifying the rate of a counter timebase allows you to define output pulses in seconds rather than in ticks of the timebase. If you use an external timebase and do not specify the rate, you can define output pulses only in ticks of the timebase. |
|  | CounterTimebaseSource | Specifies the terminal of the timebase to use for the counter. Typically, NI-DAQmx uses one of the internal counter timebases when generating pulses. Use this property to specify an external timebase and produce custom pulse widths that are not possible using the internal timebases. |
|  | DataTransferMechanism | Specifies the data transfer mode for the device. For buffered operations, use DMA or USB Bulk. For non-buffered operations, use Polled. |
|  | DataTransferRequestCondition | Specifies under what condition to transfer data from the buffer to the onboard memory of the device. |
|  | Description | Specifies a user-defined description for the channel. (Inherited from Channel.) |
|  | EnableInitialDelayOnRetrigger | Specifies whether to apply the initial delay to retriggered pulse trains. |
|  | IsGlobal | Indicates whether the channel is a global channel. (Inherited from Channel.) |
|  | MemoryMappingEnable | Specifies for NI-DAQmx to map hardware registers to the memory space of the application, if possible. Normally, NI-DAQmx maps hardware registers to memory accessible only to the kernel. Mapping the registers to the memory space of the application increases performance. However, if the application accesses the memory space mapped to the registers, it can adversely affect the operation of the device and possibly result in a system crash. |
|  | OutputState | Indicates the current state of the output terminal of the counter. |
|  | OutputType | Indicates how to define pulses generated on the channel. |
|  | PhysicalName | Specifies the name of the physical channel upon which this virtual channel is based. (Inherited from Channel.) |
|  | Prescaler | Specifies the divisor to apply to the signal you connect to the counter source terminal. Pulse generations defined by frequency or time take this setting into account, but pulse generations defined by ticks do not. You should use a prescaler only when you connect an external signal to the counter source terminal and when that signal has a higher frequency than the fastest onboard timebase. |
|  | PulseDone | Indicates if the task completed pulse generation. Use this value for retriggerable pulse generation when you need to determine if the device generated the current pulse. For retriggerable tasks, when you query this property, NI-DAQmx resets it to . |
|  | PulseDutyCycle | Specifies the duty cycle of the pulses. The duty cycle of a signal is the width of the pulse divided by period. NI-DAQmx uses this ratio and the pulse frequency to determine the width of the pulses and the delay between pulses. |
|  | PulseFrequency | Specifies the frequency of the pulses to generate. This value is in the units you specify with PulseFrequencyUnits or when you create the channel. |
|  | PulseFrequencyInitialDelay | Specifies in seconds the amount of time to wait before generating the first pulse. |
|  | PulseFrequencyUnits | Specifies the units in which to define pulse frequency. |
|  | PulseHighTicks | Specifies the number of ticks the pulse is high. |
|  | PulseHighTime | Specifies the amount of time that the pulse is at a high voltage. This value is in the units you specify with PulseTimeUnits or when you create the channel. |
|  | PulseIdleState | Specifies the resting state of the output terminal. |
|  | PulseLowTicks | Specifies the number of ticks the pulse is low. |
|  | PulseLowTime | Specifies the amount of time that the pulse is at a low voltage. This value is in the units you specify with PulseTimeUnits or when you create the channel. |
|  | PulseTerminal | Specifies on which terminal to generate pulses. |
|  | PulseTicksInitialDelay | Specifies the number of ticks to wait before generating the first pulse. |
|  | PulseTimeInitialDelay | Specifies in seconds the amount of time to wait before generating the first pulse. |
|  | PulseTimeUnits | Specifies the units in which to define high and low pulse time. |
|  | ReadyForNewValue | Indicates whether the counter is ready for new continuous pulse train values. |
|  | SynchronizationUnlockBehavior | Specifies the action to take if the target loses its synchronization to the grand master. (Inherited from Channel.) |
|  | Type | Indicates the type of the virtual channel. (Inherited from Channel.) |
|  | UsbTransferRequestCount | Specifies the maximum number of simultaneous USB transfers used to stream data. Modify this value to affect performance under different combinations of operating system and device. |
|  | UsbTransferRequestSize | Specifies the maximum size of a USB transfer request in bytes. Modify this value to affect performance under different combinations of operating system and device. |
|  | UseOnlyOnBoardMemory | Specifies whether to write samples directly to the onboard memory of the device, bypassing the memory buffer. Generally, you cannot update onboard memory directly after you start the task. Onboard memory includes data FIFOs. |
|  | VirtualName | Gets the name of the virtual channel. (Inherited from Channel.) |

Top

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

##### Remarks

COChannels

COChannel

COChannel

COChannels

COChannelCollection

COChannel

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_coconstrainedgenerationmode.htm language=enus -->
## TOPIC 00970: COConstrainedGenerationMode Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_coconstrainedgenerationmode.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_coconstrainedgenerationmode.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

COConstrainedGenerationMode Enumeration

### COConstrainedGenerationMode Enumeration

Specifies constraints to apply when the counter generates pulses. Constraining the counter reduces the device resources required for counter operation. Constraining the counter can also allow additional analog or counter tasks on the device to run concurrently. For continuous counter tasks, NI-DAQmx consumes no device resources when the counter is constrained. For finite counter tasks, resource use increases with the frequency regardless of the constraint mode. However, fixed frequency constraints significantly reduce resource usage, and fixed duty cycle constraint marginally reduces it.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum COConstrainedGenerationMode
```

```text
Public Enumeration COConstrainedGenerationMode
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Unconstrained | 14708 | Counter has no restrictions on pulse generation. |
|  | FixedHighFrequency | 14709 | Pulse frequency must be above 7.63 Hz and cannot change while the task runs. In this mode, the duty cycle has 8 bits of resolution. |
|  | FixedLowFrequency | 14710 | Pulse frequency must be below 366.21 Hz and cannot change while the task runs. In this mode, the duty cycle has 16 bits of resolution. |
|  | Fixed50PercentDutyCycle | 14711 | Pulse duty cycle must be 50 percent. The frequency can change while the task runs. |

##### Remarks

ConstrainedGenerationMode

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_codatafrequency.htm language=enus -->
## TOPIC 00971: CODataFrequency Structure

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_codatafrequency.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_codatafrequency.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CODataFrequency Structure

### CODataFrequency Structure

Encapsulates a counter output specified in terms of frequency and duty cycle.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[SerializableAttribute]
public struct CODataFrequency : ISerializable
```

```text
<SerializableAttribute>
Public Structure CODataFrequency
	Implements ISerializable
```

The CODataFrequency type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | DutyCycle | Gets or sets the duty cycle of the pulse. |
|  | Frequency | Gets or sets the frequency of the pulse. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals(Object) | Returns a value indicating if this instance is equal to the specified object. (Overrides ValueTypeEquals(Object).) |
|  | Equals(CODataFrequency) | Returns a value indicating if this instance is equal to the specified CODataFrequency object. |
|  | Equals(CODataFrequency, CODataFrequency) | Returns a value indicating if two specified instances of CODataFrequency are equal. |
|  | GetHashCode | Returns a hash code for the CODataFrequency object. (Overrides ValueTypeGetHashCode.) |
|  | GetObjectData | Sets the SerializationInfo object with information about the exception. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns the fully qualified type name of this instance. (Inherited from ValueType.) |

Top

##### Operators

|  | Name | Description |
| --- | --- | --- |
|  | Equality | Returns true if two CODataFrequency objects are equal. |
|  | Inequality | Returns true if two CODataFrequency objects are not equal. |

Top

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_codatatransfermechanism.htm language=enus -->
## TOPIC 00972: CODataTransferMechanism Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_codatatransfermechanism.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_codatatransfermechanism.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CODataTransferMechanism Enumeration

### CODataTransferMechanism Enumeration

Specifies the data transfer mode for the device. For buffered operations, use DMA or USB Bulk. For non-buffered operations, use Polled.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CODataTransferMechanism
```

```text
Public Enumeration CODataTransferMechanism
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Dma | 10054 | Direct Memory Access. Data transfers take place independently from the application. |
|  | Interrupts | 10204 | Data transfers take place independently from the application. Using interrupts increases CPU usage because the CPU must service interrupt requests. Typically, you should use interrupts if the device is out of DMA channels. |
|  | ProgrammedIO | 10264 | Data transfers take place when you call reading from the task or writing to the task. |
|  | UsbBulk | 12590 | Data transfers take place independently from the application using a USB bulk pipe. |

##### Remarks

DataTransferMechanism

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cooutputtype.htm language=enus -->
## TOPIC 00973: COOutputType Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cooutputtype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_cooutputtype.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

COOutputType Enumeration

### COOutputType Enumeration

Indicates how to define pulses generated on the channel.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum COOutputType
```

```text
Public Enumeration COOutputType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | PulseTime | 10269 | Generate pulses defined by the time the pulse is at a low state and the time the pulse is at a high state. |
|  | PulseFrequency | 10119 | Generate digital pulses defined by frequency and duty cycle. |
|  | PulseTicks | 10268 | Generate digital pulses defined by the number of timebase ticks that the pulse is at a low state and the number of timebase ticks that the pulse is at a high state. |

##### Remarks

OutputType

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_counteroutputeventargs.htm language=enus -->
## TOPIC 00974: CounterOutputEventArgs Class

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_counteroutputeventargs.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_counteroutputeventargs.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterOutputEventArgs Class

### CounterOutputEventArgs Class

CounterOutput

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[SerializableAttribute]
public class CounterOutputEventArgs : EventArgs, 
	ISerializable
```

```text
<SerializableAttribute>
Public Class CounterOutputEventArgs
	Inherits EventArgs
	Implements ISerializable
```

The CounterOutputEventArgs type exposes the following members.

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

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_counteroutputeventhandler.htm language=enus -->
## TOPIC 00975: CounterOutputEventHandler Delegate

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_counteroutputeventhandler.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_counteroutputeventhandler.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterOutputEventHandler Delegate

### CounterOutputEventHandler Delegate

CounterOutput

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public delegate void CounterOutputEventHandler(
	Object sender,
	CounterOutputEventArgs e
)
```

```text
Public Delegate Sub CounterOutputEventHandler ( 
	sender As Object,
	e As CounterOutputEventArgs
)
```

###### Parameters

- **sender**
  - Type: SystemObject The Task that caused this event.
- **e**
  - Type: NationalInstruments.DAQmxCounterOutputEventArgs A CounterOutputEventArgs that contains the event data.

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_counteroutputeventidlestate.htm language=enus -->
## TOPIC 00976: CounterOutputEventIdleState Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_counteroutputeventidlestate.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_counteroutputeventidlestate.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterOutputEventIdleState Enumeration

### CounterOutputEventIdleState Enumeration

CounterOutputEventOutputBehavior

Toggle

commits

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CounterOutputEventIdleState
```

```text
Public Enumeration CounterOutputEventIdleState
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | High | 10192 | High state. |
|  | Low | 10214 | Low state. |

##### Remarks

CounterOutputEventOutputBehavior

Toggle

commits

CounterOutputEventIdleState

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_counteroutputeventoutputbehavior.htm language=enus -->
## TOPIC 00977: CounterOutputEventOutputBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_counteroutputeventoutputbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_counteroutputeventoutputbehavior.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterOutputEventOutputBehavior Enumeration

### CounterOutputEventOutputBehavior Enumeration

Specifies whether the exported Counter Output Event pulses or changes from one state to the other when the counter reaches terminal count.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CounterOutputEventOutputBehavior
```

```text
Public Enumeration CounterOutputEventOutputBehavior
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Pulse | 10265 | Send a pulse to the terminal. |
|  | Toggle | 10307 | Toggle the state of the terminal from low to high or from high to low. |

##### Remarks

CounterOutputEventOutputBehavior

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_counteroutputeventpulsepolarity.htm language=enus -->
## TOPIC 00978: CounterOutputEventPulsePolarity Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_counteroutputeventpulsepolarity.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_counteroutputeventpulsepolarity.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterOutputEventPulsePolarity Enumeration

### CounterOutputEventPulsePolarity Enumeration

CounterOutputEventOutputBehavior

Pulse

CounterOutputEventOutputBehavior

Toggle

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CounterOutputEventPulsePolarity
```

```text
Public Enumeration CounterOutputEventPulsePolarity
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | ActiveHigh | 10095 | High state is the active state. |
|  | ActiveLow | 10096 | Low state is the active state. |

##### Remarks

CounterOutputEventOutputBehavior

Pulse

CounterOutputEventOutputBehavior

Toggle

CounterOutputEventPulsePolarity

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_countersinglechannelreader.htm language=enus -->
## TOPIC 00979: CounterSingleChannelReader Class

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_countersinglechannelreader.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_countersinglechannelreader.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelReader Class

### CounterSingleChannelReader Class

Contains methods for reading samples from the counter input channel in a task.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class CounterSingleChannelReader : MarshalByRefObject, 
	ISynchronizeCallbacks, ISupportSynchronizationContext
```

```text
Public Class CounterSingleChannelReader
	Inherits MarshalByRefObject
	Implements ISynchronizeCallbacks, ISupportSynchronizationContext
```

The CounterSingleChannelReader type exposes the following members.

##### Constructors

|  | Name | Description |
| --- | --- | --- |
|  | CounterSingleChannelReader | Creates a new instance of the CounterSingleChannelReader class to read from the specified DaqStream. |

Top

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | BeginMemoryOptimizedReadMultiSampleDouble(Int32, AsyncCallback, Object, Double) | Begins an asynchronous memory-optimized read of one or more Double samples from a single CIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSampleDouble(Int32, AsyncCallback, Object, Double, ReallocationPolicy) | Begins an asynchronous memory-optimized read of one or more Double samples from a single CIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSampleInt32(Int32, AsyncCallback, Object, Int32) | Begins an asynchronous memory-optimized read of one or more Int32 samples from a single CIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSampleInt32(Int32, AsyncCallback, Object, Int32, ReallocationPolicy) | Begins an asynchronous memory-optimized read of one or more Int32 samples from a single CIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePulseFrequency(Int32, AsyncCallback, Object, CIDataFrequency) | Begins an asynchronous memory-optimized read of one or more CIDataFrequency samples from a single CIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePulseFrequency(Int32, AsyncCallback, Object, CIDataFrequency, ReallocationPolicy) | Begins an asynchronous memory-optimized read of one or more CIDataFrequency samples from a single CIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePulseTicks(Int32, AsyncCallback, Object, CIDataTicks) | Begins an asynchronous memory-optimized read of one or more CIDataTicks samples from a single CIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePulseTicks(Int32, AsyncCallback, Object, CIDataTicks, ReallocationPolicy) | Begins an asynchronous memory-optimized read of one or more CIDataTicks samples from a single CIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePulseTime(Int32, AsyncCallback, Object, CIDataTime) | Begins an asynchronous memory-optimized read of one or more CIDataTime samples from a single CIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePulseTime(Int32, AsyncCallback, Object, CIDataTime, ReallocationPolicy) | Begins an asynchronous memory-optimized read of one or more CIDataTime samples from a single CIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSampleUInt32(Int32, AsyncCallback, Object, UInt32) | Begins an asynchronous memory-optimized read of one or more UInt32 samples from a single CIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSampleUInt32(Int32, AsyncCallback, Object, UInt32, ReallocationPolicy) | Begins an asynchronous memory-optimized read of one or more UInt32 samples from a single CIChannel in a task. |
|  | BeginReadMultiSampleDouble | Begins an asynchronous read of one or more Double samples from a counter task. |
|  | BeginReadMultiSampleInt32 | Begins an asynchronous read of one or more Int32 samples from a counter task. |
|  | BeginReadMultiSamplePulseFrequency | Begins an asynchronous read of one or more pulse samples in terms of frequency from a counter task. |
|  | BeginReadMultiSamplePulseTicks | Begins an asynchronous read of one or more pulse samples in terms of ticks from a counter task. |
|  | BeginReadMultiSamplePulseTime | Begins an asynchronous read of one or more pulse samples in terms of time from a counter task. |
|  | BeginReadMultiSampleUInt32 | Begins an asynchronous read of one or more UInt32 samples from a counter task. |
|  | BeginReadSingleSampleDouble | Begins an asynchronous read of a Double sample from a counter task. |
|  | BeginReadSingleSampleInt32 | Begins an asynchronous read of a 32-bit integer sample from a counter task. |
|  | BeginReadSingleSamplePulseFrequency | Begins an asynchronous read of a single pulse sample in terms of frequency from a counter task. |
|  | BeginReadSingleSamplePulseTicks | Begins an asynchronous read of a single pulse sample in terms of ticks from a counter task. |
|  | BeginReadSingleSamplePulseTime | Begins an asynchronous read of a single pulse sample in terms of time from a counter task. |
|  | BeginReadSingleSampleUInt32 | Begins an asynchronous read of a UInt32 sample from a counter task. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | EndMemoryOptimizedReadMultiSampleDouble | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSampleDouble(Int32, AsyncCallback, Object, Double) and retrieves the read samples. |
|  | EndMemoryOptimizedReadMultiSampleInt32 | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSampleInt32(Int32, AsyncCallback, Object, Int32) and retrieves the read samples. |
|  | EndMemoryOptimizedReadMultiSamplePulseFrequency | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePulseFrequency(Int32, AsyncCallback, Object, CIDataFrequency) and retrieves the read samples. |
|  | EndMemoryOptimizedReadMultiSamplePulseTicks | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePulseTicks(Int32, AsyncCallback, Object, CIDataTicks) and retrieves the read samples. |
|  | EndMemoryOptimizedReadMultiSamplePulseTime | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePulseTime(Int32, AsyncCallback, Object, CIDataTime) and retrieves the read samples. |
|  | EndMemoryOptimizedReadMultiSampleUInt32 | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSampleUInt32(Int32, AsyncCallback, Object, UInt32) and retrieves the read samples. |
|  | EndReadMultiSampleDouble | Handles the end of an asynchronous read initiated with BeginReadMultiSampleDouble(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadMultiSampleInt32 | Handles the end of an asynchronous read initiated with BeginReadMultiSampleInt32(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadMultiSamplePulseFrequency | Handles the end of an asynchronous read initiated with BeginReadMultiSamplePulseFrequency(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadMultiSamplePulseTicks | Handles the end of an asynchronous read initiated with BeginReadMultiSamplePulseTicks(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadMultiSamplePulseTime | Handles the end of an asynchronous read initiated with BeginReadMultiSamplePulseTime(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadMultiSampleUInt32 | Handles the end of an asynchronous read initiated with BeginReadMultiSampleUInt32(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSampleDouble | Handles the end of an asynchronous read initiated with BeginReadSingleSampleDouble(AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSampleInt32 | Handles the end of an asynchronous read initiated with BeginReadSingleSampleInt32(AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSamplePulseFrequency | Handles the end of an asynchronous read initiated with BeginReadSingleSamplePulseFrequency(AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSamplePulseTicks | Handles the end of an asynchronous read initiated with BeginReadSingleSamplePulseTicks(AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSamplePulseTime | Handles the end of an asynchronous read initiated with BeginReadSingleSamplePulseTime(AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSampleUInt32 | Handles the end of an asynchronous read initiated with BeginReadSingleSampleUInt32(AsyncCallback, Object) and retrieves the read samples. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | MemoryOptimizedReadMultiSampleDouble(Int32, Double, Int32) | Reads one or more Double samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSampleDouble(Int32, Double, ReallocationPolicy, Int32) | Reads one or more Double samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSampleInt32(Int32, Int32, Int32) | Reads one or more Int32 samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSampleInt32(Int32, Int32, ReallocationPolicy, Int32) | Reads one or more Int32 samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSamplePulseFrequency(Int32, CIDataFrequency, Int32) | Reads one or more CIDataFrequency samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSamplePulseFrequency(Int32, CIDataFrequency, ReallocationPolicy, Int32) | Reads one or more CIDataFrequency samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSamplePulseTicks(Int32, CIDataTicks, Int32) | Reads one or more CIDataTicks samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSamplePulseTicks(Int32, CIDataTicks, ReallocationPolicy, Int32) | Reads one or more CIDataTicks samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSamplePulseTime(Int32, CIDataTime, Int32) | Reads one or more CIDataTime samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSamplePulseTime(Int32, CIDataTime, ReallocationPolicy, Int32) | Reads one or more CIDataTime samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSampleUInt32(Int32, UInt32, Int32) | Reads one or more UInt32 samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSampleUInt32(Int32, UInt32, ReallocationPolicy, Int32) | Reads one or more UInt32 samples from a single CIChannel in a task. |
|  | ReadMultiSampleDouble | Reads one or more Double samples from a counter task. |
|  | ReadMultiSampleInt32 | Reads one or more Int32 samples from a counter task. |
|  | ReadMultiSamplePulseFrequency | Reads one or more pulse samples in terms of frequency from a counter task. |
|  | ReadMultiSamplePulseTicks | Reads one or more pulse samples in terms of ticks from a counter task. |
|  | ReadMultiSamplePulseTime | Reads one or more pulse samples in terms of time from a counter task. |
|  | ReadMultiSampleUInt32 | Reads one or more UInt32 samples from a counter task. |
|  | ReadSingleSampleDouble | Reads a single Double sample from a counter task. |
|  | ReadSingleSampleInt32 | Reads a Int32 sample from a counter task. |
|  | ReadSingleSamplePulseFrequency | Reads a pulse sample in terms of frequency from a counter task. |
|  | ReadSingleSamplePulseTicks | Reads a pulse sample in terms of ticks from a counter task. |
|  | ReadSingleSamplePulseTime | Reads a pulse sample in terms of time from a counter task. |
|  | ReadSingleSampleUInt32 | Reads an UInt32 sample from a counter task. |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_countersinglechannelwriter.htm language=enus -->
## TOPIC 00980: CounterSingleChannelWriter Class

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_countersinglechannelwriter.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_countersinglechannelwriter.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelWriter Class

### CounterSingleChannelWriter Class

Contains methods for writing samples to a single counter output channel in a counter output task.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class CounterSingleChannelWriter : MarshalByRefObject, 
	ISynchronizeCallbacks, ISupportSynchronizationContext
```

```text
Public Class CounterSingleChannelWriter
	Inherits MarshalByRefObject
	Implements ISynchronizeCallbacks, ISupportSynchronizationContext
```

The CounterSingleChannelWriter type exposes the following members.

##### Constructors

|  | Name | Description |
| --- | --- | --- |
|  | CounterSingleChannelWriter | Initializes a new instance of the CounterSingleChannelWriter class to write to the specified DaqStream. |

Top

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |

Top

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

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_couplingtypes.htm language=enus -->
## TOPIC 00981: CouplingTypes Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_couplingtypes.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_couplingtypes.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CouplingTypes Enumeration

### CouplingTypes Enumeration

Specifies a set of coupling types a device may support.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[FlagsAttribute]
public enum CouplingTypes
```

```text
<FlagsAttribute>
Public Enumeration CouplingTypes
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | None | 0 | No coupling types supported by the device. |
|  | AC | 1 | Remove the DC offset from the signal. |
|  | DC | 2 | Allow NI-DAQmx to measure all of the signal. |
|  | Ground | 4 | Remove the signal from the measurement and measure only ground. |

##### Remarks

Specifies a set of coupling types a device may support.

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_daqbuffer.htm language=enus -->
## TOPIC 00982: DaqBuffer Class

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_daqbuffer.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_daqbuffer.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqBuffer Class

### DaqBuffer Class

buffer

Task

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class DaqBuffer : MarshalByRefObject, IFilteredTypeDescriptor
```

```text
Public Class DaqBuffer
	Inherits MarshalByRefObject
	Implements IFilteredTypeDescriptor
```

The DaqBuffer type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | InputBufferSize | Specifies the number of samples the input buffer can hold for each channel in the task. Zero indicates to allocate no buffer. Use a buffer size of 0 to perform a hardware-timed operation without using a buffer. Setting this property overrides the automatic input buffer allocation that NI-DAQmx performs. |
|  | InputOnBoardBufferSize | Indicates in samples per channel the size of the onboard input buffer of the device. |
|  | OutputBufferSize | Specifies the number of samples the output buffer can hold for each channel in the task. Zero indicates to allocate no buffer. Use a buffer size of 0 to perform a hardware-timed operation without using a buffer. Setting this property overrides the automatic output buffer allocation that NI-DAQmx performs. |
|  | OutputOnBoardBufferSize | Specifies in samples per channel the size of the onboard output buffer of the device. |

Top

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

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_daqexception.htm language=enus -->
## TOPIC 00983: DaqException Class

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_daqexception.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_daqexception.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqException Class

### DaqException Class

Represents the exception that is thrown when an NI-DAQmx driver error occurs.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[SerializableAttribute]
public class DaqException : SystemException, 
	ISerializable
```

```text
<SerializableAttribute>
Public Class DaqException
	Inherits SystemException
	Implements ISerializable
```

The DaqException type exposes the following members.

##### Constructors

|  | Name | Description |
| --- | --- | --- |
|  | DaqException | Initializes a new instance of the DaqException class. |
|  | DaqException(String) | Initializes a new instance of the DaqException class with the specified error message. |
|  | DaqException(SerializationInfo, StreamingContext) | Creates a new instance of the DaqException class with serialized data. |
|  | DaqException(String, Int32) | Initializes a new instance of the DaqException class with the specified error message and NI-DAQmx driver error code. |
|  | DaqException(String, Exception) | Initializes a new instance of the DaqException class with the specified error message and a reference to the inner exception that is the cause of the exception. |
|  | DaqException(String, Int32, Exception) | Initializes a new instance of the DaqException class with the specified error message, NI-DAQmx driver error code, and reference to the inner exception that is the cause of the exception. |

Top

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Data | Gets a collection of key/value pairs that provide additional user-defined information about the exception. (Inherited from Exception.) |
|  | Error | Gets the NI-DAQmx driver code for the error that occurred. |
|  | HelpLink | Gets or sets a link to the help file associated with this exception. (Inherited from Exception.) |
|  | HResult | Gets or sets HRESULT, a coded numerical value that is assigned to a specific exception. (Inherited from Exception.) |
|  | InnerException | Gets the Exception instance that caused the current exception. (Inherited from Exception.) |
|  | Message | Gets a message that describes the current exception. (Inherited from Exception.) |
|  | Source | Gets or sets the name of the application or the object that causes the error. (Inherited from Exception.) |
|  | StackTrace | Gets a string representation of the immediate frames on the call stack. (Inherited from Exception.) |
|  | TargetSite | Gets the method that throws the current exception. (Inherited from Exception.) |

Top

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

##### Events

|  | Name | Description |
| --- | --- | --- |
|  | SerializeObjectState | Occurs when an exception is serialized to create an exception state object that contains serialized data about the exception. (Inherited from Exception.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

###### Other Resources

NI-DAQmx Driver Error Codes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_daqwarningeventargs.htm language=enus -->
## TOPIC 00984: DaqWarningEventArgs Class

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_daqwarningeventargs.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_daqwarningeventargs.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqWarningEventArgs Class

### DaqWarningEventArgs Class

DaqWarning

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[SerializableAttribute]
public class DaqWarningEventArgs : EventArgs, 
	ISerializable
```

```text
<SerializableAttribute>
Public Class DaqWarningEventArgs
	Inherits EventArgs
	Implements ISerializable
```

The DaqWarningEventArgs type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Error | Gets the NI-DAQmx driver code for the warning that occurred. Zero means no warning occurred. |
|  | Message | Gets a message that describes the warning. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetObjectData | Sets the SerializationInfo object with information about the exception. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_diacquireon.htm language=enus -->
## TOPIC 00985: DIAcquireOn Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_diacquireon.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_diacquireon.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DIAcquireOn Enumeration

### DIAcquireOn Enumeration

Specifies on which edge of the sample clock to acquire samples.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum DIAcquireOn
```

```text
Public Enumeration DIAcquireOn
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | ActiveEdge | 14617 | Active edges. |
|  | InactiveEdge | 14618 | Inactive edges. |

##### Remarks

AcquireOn

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_dichannelcollection.htm language=enus -->
## TOPIC 00986: DIChannelCollection Class

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_dichannelcollection.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_dichannelcollection.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DIChannelCollection Class

### DIChannelCollection Class

Task

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class DIChannelCollection : MarshalByRefObject, 
	ICollection
```

```text
Public Class DIChannelCollection
	Inherits MarshalByRefObject
	Implements ICollection
```

The DIChannelCollection type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | All | Gets a DIChannel that operates on all of the channels in the task. |
|  | Count | Gets the number of elements in the collection. |
|  | ItemInt64 | Gets the DIChannel at the specified index. In Visual C#, this property is the indexer. |
|  | ItemString | Gets the DIChannel with the specified virtual channel name. In Visual C#, this property is the indexer. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateChannel | Creates a DIChannel to measure digital signals. This method adds one or more channels to the DIChannelCollection. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetEnumerator | Returns an enumerator that you can use to iterate through the collection. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_digitalchangedetectioneventhandler.htm language=enus -->
## TOPIC 00987: DigitalChangeDetectionEventHandler Delegate

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_digitalchangedetectioneventhandler.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_digitalchangedetectioneventhandler.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalChangeDetectionEventHandler Delegate

### DigitalChangeDetectionEventHandler Delegate

DigitalChangeDetection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public delegate void DigitalChangeDetectionEventHandler(
	Object sender,
	DigitalChangeDetectionEventArgs e
)
```

```text
Public Delegate Sub DigitalChangeDetectionEventHandler ( 
	sender As Object,
	e As DigitalChangeDetectionEventArgs
)
```

###### Parameters

- **sender**
  - Type: SystemObject The Task that caused this event.
- **e**
  - Type: NationalInstruments.DAQmxDigitalChangeDetectionEventArgs A DigitalChangeDetectionEventArgs that contains the event data.

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_digitaledgeadvancetrigger.htm language=enus -->
## TOPIC 00988: DigitalEdgeAdvanceTrigger Class

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_digitaledgeadvancetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_digitaledgeadvancetrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalEdgeAdvanceTrigger Class

### DigitalEdgeAdvanceTrigger Class

digital edge

advance triggers

AdvanceTrigger

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class DigitalEdgeAdvanceTrigger : MarshalByRefObject, 
	IFilteredTypeDescriptor
```

```text
Public Class DigitalEdgeAdvanceTrigger
	Inherits MarshalByRefObject
	Implements IFilteredTypeDescriptor
```

The DigitalEdgeAdvanceTrigger type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | DigitalFilterEnable | Obsolete. (Deprecated) Specifies whether to apply the pulse width filter to the signal. |
|  | Edge | Obsolete. (Deprecated) Specifies on which edge of a digital signal to advance to the next entry in a scan list. |
|  | Source | Obsolete. (Deprecated) Specifies the name of a terminal where there is a digital signal to use as the source of the Advance Trigger. |

Top

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

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_digitaledgeadvancetriggeredge.htm language=enus -->
## TOPIC 00989: DigitalEdgeAdvanceTriggerEdge Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_digitaledgeadvancetriggeredge.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_digitaledgeadvancetriggeredge.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalEdgeAdvanceTriggerEdge Enumeration

### DigitalEdgeAdvanceTriggerEdge Enumeration

**Note: This API is now obsolete.**

(Deprecated) Specifies on which edge of a digital signal to advance to the next entry in a scan list.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("This enum is obsolete.")]
public enum DigitalEdgeAdvanceTriggerEdge
```

```text
<ObsoleteAttribute("This enum is obsolete.")>
Public Enumeration DigitalEdgeAdvanceTriggerEdge
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Rising | 10280 | Rising edge(s). |
|  | Falling | 10171 | Falling edge(s). |

##### Remarks

Edge

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_digitaledgearmstarttrigger.htm language=enus -->
## TOPIC 00990: DigitalEdgeArmStartTrigger Class

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_digitaledgearmstarttrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_digitaledgearmstarttrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalEdgeArmStartTrigger Class

### DigitalEdgeArmStartTrigger Class

digital edge

arm start triggers

ArmStartTrigger

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class DigitalEdgeArmStartTrigger : MarshalByRefObject, 
	IFilteredTypeDescriptor
```

```text
Public Class DigitalEdgeArmStartTrigger
	Inherits MarshalByRefObject
	Implements IFilteredTypeDescriptor
```

The DigitalEdgeArmStartTrigger type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | DigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
|  | DigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | DigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | DigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | DigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | Edge | Specifies on which edge of a digital signal to arm the task for a Start Trigger. |
|  | Source | Specifies the name of a terminal where there is a digital signal to use as the source of the Arm Start Trigger. |

Top

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

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_digitallevelpausetrigger.htm language=enus -->
## TOPIC 00991: DigitalLevelPauseTrigger Class

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_digitallevelpausetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_digitallevelpausetrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalLevelPauseTrigger Class

### DigitalLevelPauseTrigger Class

digital level

pause triggers

PauseTrigger

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class DigitalLevelPauseTrigger : MarshalByRefObject, 
	IFilteredTypeDescriptor
```

```text
Public Class DigitalLevelPauseTrigger
	Inherits MarshalByRefObject
	Implements IFilteredTypeDescriptor
```

The DigitalLevelPauseTrigger type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Condition | Specifies whether the task pauses while the signal is high or low. |
|  | DigitalFilterEnable | Specifies whether to apply a digital filter to the trigger signal. |
|  | DigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | DigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | DigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | DigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | Source | Specifies the name of a terminal where there is a digital signal to use as the source of the Pause Trigger. |

Top

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

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_dolinestatesdonestate.htm language=enus -->
## TOPIC 00992: DOLineStatesDoneState Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_dolinestatesdonestate.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_dolinestatesdonestate.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DOLineStatesDoneState Enumeration

### DOLineStatesDoneState Enumeration

completes execution

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum DOLineStatesDoneState
```

```text
Public Enumeration DOLineStatesDoneState
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | High | 10192 | Logic high. |
|  | Low | 10214 | Logic low. |
|  | Tristate | 10310 | High-impedance state. You can select this state only on devices with bidirectional lines. You cannot select this state for dedicated digital output lines. On some devices, you can select this value only for entire ports. |
|  | NoChange | 10160 | Do not change the state of the lines. On some devices, you can select this value only for entire ports. |

##### Remarks

completes execution

LineStatesDoneState

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_dologicfamily.htm language=enus -->
## TOPIC 00993: DOLogicFamily Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_dologicfamily.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_dologicfamily.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DOLogicFamily Enumeration

### DOLogicFamily Enumeration

Specifies the logic family to use for generation. A logic family corresponds to voltage thresholds that are compatible with a group of voltage standards. Refer to the device documentation for information on the logic high and logic low voltages for these logic families.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum DOLogicFamily
```

```text
Public Enumeration DOLogicFamily
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | TwoPointFiveVolts | 14620 | Compatible with 2.5 V CMOS signals. |
|  | ThreePointThreeVolts | 14621 | Compatible with LVTTL signals. |
|  | FiveVolts | 14619 | Compatible with TTL and 5 V CMOS signals. |

##### Remarks

LogicFamily

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_dooutputdrivetype.htm language=enus -->
## TOPIC 00994: DOOutputDriveType Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_dooutputdrivetype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_dooutputdrivetype.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DOOutputDriveType Enumeration

### DOOutputDriveType Enumeration

Specifies the drive type for digital output channels.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum DOOutputDriveType
```

```text
Public Enumeration DOOutputDriveType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | ActiveDrive | 12573 | Drive the output pin to approximately 0 V for logic low and +3.3 V or +5 V, depending on the device, for logic high. |
|  | OpenCollector | 12574 | Drive the output pin to 0 V for logic low. For logic high, the output driver assumes a high-impedance state and does not drive a voltage. |

##### Remarks

OutputDriveType

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_everynsamplesreadeventargs.htm language=enus -->
## TOPIC 00995: EveryNSamplesReadEventArgs Class

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_everynsamplesreadeventargs.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_everynsamplesreadeventargs.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

EveryNSamplesReadEventArgs Class

### EveryNSamplesReadEventArgs Class

EveryNSamplesRead

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[SerializableAttribute]
public class EveryNSamplesReadEventArgs : EventArgs, 
	ISerializable
```

```text
<SerializableAttribute>
Public Class EveryNSamplesReadEventArgs
	Inherits EventArgs
	Implements ISerializable
```

The EveryNSamplesReadEventArgs type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Error | Gets the Exception that occurred, if any. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CheckForException | Throws the Exception that occurred, if any exists. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetObjectData | Sets the SerializationInfo object with information about the exception. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_everynsamplesreadeventhandler.htm language=enus -->
## TOPIC 00996: EveryNSamplesReadEventHandler Delegate

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_everynsamplesreadeventhandler.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_everynsamplesreadeventhandler.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

EveryNSamplesReadEventHandler Delegate

### EveryNSamplesReadEventHandler Delegate

EveryNSamplesRead

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public delegate void EveryNSamplesReadEventHandler(
	Object sender,
	EveryNSamplesReadEventArgs e
)
```

```text
Public Delegate Sub EveryNSamplesReadEventHandler ( 
	sender As Object,
	e As EveryNSamplesReadEventArgs
)
```

###### Parameters

- **sender**
  - Type: SystemObject The Task that caused this event.
- **e**
  - Type: NationalInstruments.DAQmxEveryNSamplesReadEventArgs An EveryNSamplesReadEventArgs that contains the event data.

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_everynsampleswritteneventargs.htm language=enus -->
## TOPIC 00997: EveryNSamplesWrittenEventArgs Class

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_everynsampleswritteneventargs.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_everynsampleswritteneventargs.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

EveryNSamplesWrittenEventArgs Class

### EveryNSamplesWrittenEventArgs Class

EveryNSamplesWritten

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[SerializableAttribute]
public class EveryNSamplesWrittenEventArgs : EventArgs, 
	ISerializable
```

```text
<SerializableAttribute>
Public Class EveryNSamplesWrittenEventArgs
	Inherits EventArgs
	Implements ISerializable
```

The EveryNSamplesWrittenEventArgs type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Error | Gets the Exception that occurred, if any. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CheckForException | Throws the Exception that occurred, if any exists. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetObjectData | Sets the SerializationInfo object with information about the exception. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_handshakestartcondition.htm language=enus -->
## TOPIC 00998: HandshakeStartCondition Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_handshakestartcondition.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_handshakestartcondition.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

HandshakeStartCondition Enumeration

### HandshakeStartCondition Enumeration

Specifies the point in the handshake cycle that the device is in when the task starts.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum HandshakeStartCondition
```

```text
Public Enumeration HandshakeStartCondition
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Immediate | 10198 | Device is waiting for space in the FIFO (for acquisition) or waiting for samples (for generation). |
|  | WaitForHandshakeTriggerAssert | 12550 | Device is waiting for the Handshake Trigger to assert. |
|  | WaitForHandshakeTriggerDeassert | 12551 | Device is waiting for the Handshake Trigger to deassert. |

##### Remarks

HandshakeStartCondition

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_physicalchannel.htm language=enus -->
## TOPIC 00999: PhysicalChannel Class

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_physicalchannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_physicalchannel.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

PhysicalChannel Class

### PhysicalChannel Class

channel

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class PhysicalChannel : MarshalByRefObject, 
	IDisposable
```

```text
Public Class PhysicalChannel
	Inherits MarshalByRefObject
	Implements IDisposable
```

The PhysicalChannel type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | AIInputSources | Indicates the list of input sources supported by the channel. Channels may support using the signal from the I/O connector or one of several calibration signals. |
|  | AISupportedMeasurementTypes | Gets the measurement types supported by the physical channels of the device. |
|  | AITerminalConfigurations | Indicates the list of input terminal configurations supported by the channel. |
|  | AOManualControlAmplitude | Indicates the current value of the front panel amplitude control for the physical channel in volts. |
|  | AOManualControlEnable | Specifies if you can control the physical channel externally via a manual control located on the device. You cannot simultaneously control a channel manually and with NI-DAQmx. |
|  | AOManualControlFrequency | Indicates the current value of the front panel frequency control for the physical channel in hertz. |
|  | AOManualControlShortDetected | Indicates whether the physical channel is currently disabled due to a short detected on the channel. |
|  | AOPowerAmplifierChannelEnable | Specifies whether to enable or disable a channel for amplification. This property can also be used to check if a channel is enabled. |
|  | AOPowerAmplifierGain | Indicates the calibrated gain of the channel. |
|  | AOPowerAmplifierOffset | Indicates the calibrated offset of the channel in volts. |
|  | AOPowerAmplifierOvercurrent | Indicates if the channel detected an overcurrent condition. |
|  | AOPowerAmplifierScalingCoefficients | Indicates the coefficients of a polynomial equation used to scale from pre-amplified values. |
|  | AOSupportedOutputTypes | Gets the generation types supported by the physical channels of the device. |
|  | AOTerminalConfigurations | Indicates the list of output terminal configurations supported by the channel. |
|  | CISupportedMeasurementTypes | Gets the measurement types supported by the physical channels of the device. |
|  | COSupportedOutputTypes | Gets the generation types supported by the physical channels of the device |
|  | DIChangeDetectionSupported | Indicates if the change detection timing type is supported for the digital input physical channel. |
|  | DIPortWidth | Indicates in bits the width of digital input port. |
|  | DISampleClockSupported | Indicates if the sample clock timing type is supported for the digital input physical channel. |
|  | DISampleModes | Gets the sample modes supported by the physical channels that support sample clocked digital input. |
|  | DOPortWidth | Indicates in bits the width of digital output port. |
|  | DOSampleClockSupported | Indicates if the sample clock timing type is supported for the digital output physical channel. |
|  | DOSampleModes | Gets the sample modes supported by physical channels that support sample clocked digital output. |
|  | PhysicalChannelName | Gets the name of the physical channel. |
|  | PowerControlEnable | Specifies whether to turn on the sensor's power supply. |
|  | PowerControlType | Specifies the type of power supplied to the sensor. |
|  | PowerControlVoltage | Specifies the voltage level for the sensor's power supply. |
|  | SensorPowerOpenChannel | Indicates whether there is an open channel or undercurrent condition on the channel. |
|  | SensorPowerOvercurrent | Indicates whether there is an overcurrent condition on the channel. |
|  | SensorPowerTypes | Indicates the types of power supplied to the sensor supported by this channel. |
|  | SensorPowerVoltageRangeValues | Indicates pairs of sensor power voltage ranges supported by this channel. Each pair consists of the low value followed by the high value. |
|  | TedsBitStream | Indicates the TEDS binary bitstream without checksums. |
|  | TedsManufacturerID | Indicates the manufacturer ID of the sensor. |
|  | TedsModelNumber | Indicates the model number of the sensor. |
|  | TedsSerialNumber | Indicates the serial number of the sensor. |
|  | TedsTemplateIDs | Indicates the IDs of the templates in the bitstream in TedsBitStream. |
|  | TedsVersionLetter | Indicates the version letter of the sensor. |
|  | TedsVersionNumber | Indicates the version number of the sensor. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ClearTeds | Removes TEDS information from the physical channel you specify. |
|  | ConfigureTeds | Associates TEDS information with the physical channel you specify, using a TEDS sensor connected to the physical channel. |
|  | ConfigureTeds(String) | Associates TEDS information with the physical channel you specify. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Dispose | Releases all resources used by PhysicalChannel. |
|  | Dispose(Boolean) | Releases the managed and unmanaged resources used by PhysicalChannel or optionally releases only the unmanaged resources. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |
|  | WriteTedsData(Byte, BasicTedsDataOption) | Write TEDS data from a Byte array to a sensor on the physical channel you specify. |
|  | WriteTedsData(String, BasicTedsDataOption) | Write TEDS data from a virtual TEDS file to a sensor on the physical channel you specify. |

Top

##### Remarks

LoadPhysicalChannel(String)

Local

DaqSystem

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_physicalchannelaisensorpowertype.htm language=enus -->
## TOPIC 01000: PhysicalChannelAISensorPowerType Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_physicalchannelaisensorpowertype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_physicalchannelaisensorpowertype.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

PhysicalChannelAISensorPowerType Enumeration

### PhysicalChannelAISensorPowerType Enumeration

Indicates the types of power supplied to the sensor supported by this channel.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum PhysicalChannelAISensorPowerType
```

```text
Public Enumeration PhysicalChannelAISensorPowerType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | DC | 10050 | Sensor power supply generates a single DC voltage level. |
|  | AC | 10045 | Sensor power supply generates an AC voltage. |
|  | BipolarDC | 16147 | Sensor power supply generates a pair of DC voltage levels. |

##### Remarks

SensorPowerTypes

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.
