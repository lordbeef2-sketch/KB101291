# NI DOCUMENT BUNDLE: ni-daqmx-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-daqmx-labview-api-ref start=1501 end=1750 -->
<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr1308.html language=enus -->
## TOPIC 01501: Sample Clock:Timebase:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr1308.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr1308.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the Sample Clock Timebase. Remarks The following table lists the characteristics of this property. Short Name SampClk.Timebase.Src Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available

### Sample Clock:Timebase:Source

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 of the signal to use as the Sample Clock Timebase.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SampClk.Timebase.Src |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr1310.html language=enus -->
## TOPIC 01502: Sample Quantity:Samples Per Channel

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr1310.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr1310.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of samples to acquire or generate for each channel if SampQuant.SampMode is Finite Samples. If SampQuant.SampMode is Continuous Samples, NI-DAQmx uses this value to determine the buffer size . To configure an analog output task to generate a finite number of cycles of a waveform

### Sample Quantity:Samples Per Channel

Specifies the number of samples to acquire or generate for each channel if 
 [SampQuant.SampMode](/csh?context=nidaqmx_daqmxprop_attr1300)
 is Finite Samples. If 
 [SampQuant.SampMode](/csh?context=nidaqmx_daqmxprop_attr1300)
 is Continuous Samples, NI-DAQmx uses this value to 
 [determine the buffer size](/csh?context=nidaqmx_mxcncpts_buffersize)
 .

To configure an analog output task to generate a finite number of cycles of a waveform, set this property to 
(desired number of cycles) * (number of samples per cycle).

This property affects the
 [buffer allocation](/csh?context=nidaqmx_mxcncpts_buffersize)
 for the task.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SampQuant.SampPerChan |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr1315.html language=enus -->
## TOPIC 01503: More:Reference Clock:Rate

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr1315.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr1315.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency of the Reference Clock. Remarks The following table lists the characteristics of this property. Short Name RefClk.Rate Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True

### More:Reference Clock:Rate

Specifies the frequency of the Reference Clock.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | RefClk.Rate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr1316.html language=enus -->
## TOPIC 01504: More:Reference Clock:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr1316.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr1316.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the Reference Clock. Remarks The following table lists the characteristics of this property. Short Name RefClk.Src Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engi

### More:Reference Clock:Source

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 of the signal to use as the Reference Clock.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | RefClk.Src |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr1317.html language=enus -->
## TOPIC 01505: More:AI Convert:Delay From Sample Clock:Delay

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr1317.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr1317.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the amount of time to wait after receiving a Sample Clock edge before beginning to acquire the sample. This value is in the units you specify with DelayFromSampClk.DelayUnits . Remarks The following table lists the characteristics of this property. Short Name DelayFromSampClk.Delay Data ty

### More:AI Convert:Delay From Sample Clock:Delay

Specifies the amount of time to wait after receiving a Sample Clock edge before beginning to acquire the sample. This value is in the units you specify with 
 [DelayFromSampClk.DelayUnits](/csh?context=nidaqmx_daqmxprop_attr1304)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DelayFromSampClk.Delay |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr1335.html language=enus -->
## TOPIC 01506: More:AI Convert:Timebase Divisor

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr1335.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr1335.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of AI Convert Clock Timebase pulses needed to produce a single AI Convert Clock pulse. Remarks The following table lists the characteristics of this property. Short Name AIConv.TimebaseDiv Data type cu32.png Permissions Read/Write Resettable True Settable While Task Is Running d

### More:AI Convert:Timebase Divisor

Specifies the number of AI Convert Clock Timebase pulses needed to produce a single AI Convert Clock pulse.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AIConv.TimebaseDiv |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr1339.html language=enus -->
## TOPIC 01507: More:AI Convert:Timebase:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr1339.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr1339.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the AI Convert Clock Timebase. Remarks The following table lists the characteristics of this property. Short Name AIConv.Timebase.Src Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in R

### More:AI Convert:Timebase:Source

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 of the signal to use as the AI Convert Clock Timebase.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AIConv.Timebase.Src |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Same as Sample Timebase | 10284 | Use the same source as Sample Clock timebase. |
| --- | --- | --- |
| Same as Master Timebase | 10282 | Use the same source as the Master Timebase. |
| 100 MHz Timebase | 15857 | Use the onboard 100 MHz timebase. |
| 80 MHz Timebase | 14636 | Use the onboard 80 MHz timebase. |
| 20 MHz Timebase | 12537 | Use the onboard 20 MHz timebase. |
| 8 MHz Timebase | 16023 | Use the onboard 8 MHz timebase. |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr1343.html language=enus -->
## TOPIC 01508: More:Master Timebase:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr1343.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr1343.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the Master Timebase. On an E Series device, you can choose only between the onboard 20MHz Timebase or the RTSI7 terminal. Remarks The following table lists the characteristics of this property. Short Name MasterTimebase.Src Data type cdaqmxscale.png Per

### More:Master Timebase:Source

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 of the signal to use as the Master Timebase. On an E Series device, you can choose only between the onboard 20MHz Timebase or the RTSI7 terminal.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | MasterTimebase.Src |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr1344.html language=enus -->
## TOPIC 01509: Sample Clock:Rate

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr1344.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr1344.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sampling rate in samples per channel per second. If you use an external source for the Sample Clock, set this input to the maximum expected rate of that clock. Remarks The following table lists the characteristics of this property. Short Name SampClk.Rate Data type cdbl.png Permissions

### Sample Clock:Rate

Specifies the sampling rate in samples per channel per second. If you use an external source for the Sample Clock, set this input to the maximum expected rate of that clock.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SampClk.Rate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr1347.html language=enus -->
## TOPIC 01510: Sample Timing Type

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr1347.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr1347.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of sample timing to use for the task. Select Sample Clock when a hardware signal (usually a clock) must acquire or produce samples. To perform buffered edge counting, for example, select Sample Clock and use SampClk.Src to specify the source of the Sample clock. Select Handshake t

### Sample Timing Type

Specifies the 
 [type of sample timing](/csh?context=nidaqmx_mxcncpts_smpletimingtype)
 to use for the task.

Select Sample Clock when a hardware signal (usually a clock) must acquire or produce samples. To perform buffered edge 
counting, for example, select Sample Clock and use 
 [SampClk.Src](/csh?context=nidaqmx_daqmxprop_attr1852)
 to specify the source of the Sample clock.

Select Handshake to use bidirectional hardware signals to time the exchange of digital data between two devices.

Select Burst Handshake to run at a slower rate but with the capability for per sample evaluation of triggers and events to pause the operation.

Select Pipelined Sample Clock on supported devices to run at the maximum sample rate with a few Sample clock cycles delay before the device can respond to triggers and events.

Select On Demand to acquire data only when 
 [DAQmx Read](/csh?context=nidaqmx_lvdaqmx_mxread)
 executes or to generate data only when 
 [DAQmx Write](/csh?context=nidaqmx_lvdaqmx_mxwrite)
executes.

Select Implicit to perform a buffered period or frequency counter measurement or to generate a finite pulse train.

Select Change Detection to capture data only when certain digital lines change states and without continuously transferring unnecessary data during periods of inactivity.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SampTimingType |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Sample Clock | 10388 | Acquire or generate samples on the specified edge of the sample clock. |
| --- | --- | --- |
| Burst Handshake | 12548 | Determine sample timing using burst handshaking between the device and a peripheral device. |
| Handshake | 10389 | Determine sample timing by using digital handshaking between the device and a peripheral device. |
| Implicit | 10451 | Configure only the duration of the task. |
| On Demand | 10390 | Acquire or generate a sample on each read or write operation. This timing type is also referred to as static or software-timed. |
| Change Detection | 12504 | Acquire samples when a change occurs in the state of one or more digital input lines. The lines must be contained within a digital input channel. |
| Pipelined Sample Clock | 14668 | Device acquires or generates samples on each sample clock edge, but does not respond to certain triggers until a few sample clock edges later. Pipelining allows higher data transfer rates at the cost of increased trigger response latency. Refer to the device documentation for information about which triggers pipelining affects. This timing type allows handshaking with some devices using the Pause trigger, the Ready for Transfer event, or the Data Active event. Refer to the device documentation for more information. |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr1495.html language=enus -->
## TOPIC 01511: More:Master Timebase:Rate

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr1495.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr1495.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the rate of the Master Timebase. This property is useful only when the source of the Master Timebase is not the onboard 20 MHz timebase. NI-DAQmx requires the Master Timebase rate to calculate other timing parameters. Remarks The following table lists the characteristics of this property.

### More:Master Timebase:Rate

Specifies the rate of the Master Timebase.

This property is useful only when the source of the Master Timebase is not the onboard 20 MHz timebase. NI-DAQmx requires the Master Timebase
rate to calculate other timing parameters.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | MasterTimebase.Rate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr1502.html language=enus -->
## TOPIC 01512: More:AI Convert:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr1502.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr1502.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the AI Convert Clock. Remarks The following table lists the characteristics of this property. Short Name AIConv.Src Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Eng

### More:AI Convert:Source

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 of the signal to use as the AI Convert Clock.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AIConv.Src |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr1848.html language=enus -->
## TOPIC 01513: More:AI Convert:Rate

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr1848.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr1848.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in Hertz the rate at which to clock the analog-to-digital converter. This clock is specific to the analog input section of multiplexed devices . By default, NI-DAQmx selects the maximum convert rate supported by the device, plus up to 10 microseconds per channel settling time. Other task s

### More:AI Convert:Rate

Specifies in Hertz the rate at which to clock the analog-to-digital converter. This clock is specific to the analog input section of 
 [multiplexed devices](/csh?context=nidaqmx_mxcncpts_multisimulsamp)
 .

By default, NI-DAQmx selects the maximum convert rate supported by the device, plus up to 10 microseconds per channel settling time. 
Other task settings, such as high channel counts or setting 
 [DelayFromSampClk.Delay](/csh?context=nidaqmx_daqmxprop_attr1317)
 , can result in a faster default convert rate.

CompactDAQ applies up to 10 microseconds of settling time for all C Series devices even if the maximum convert rates of the devices differ.

If you connect signal conditioning accessories with track and hold capabilities, such as an SCXI module, to the device, NI-DAQmx uses the fastest
convert rate possible that meets the settling requirements for the slowest module sampled. Refer to the device documentation for the signal conditioning accessory 
for more information.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AIConv.Rate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr1852.html language=enus -->
## TOPIC 01514: Sample Clock:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr1852.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr1852.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the Sample Clock. Remarks The following table lists the characteristics of this property. Short Name SampClk.Src Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine

### Sample Clock:Source

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 of the signal to use as the Sample Clock.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SampClk.Src |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr1853.html language=enus -->
## TOPIC 01515: More:AI Convert:Active Edge

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr1853.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr1853.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge of the clock pulse an analog-to-digital conversion takes place. This property is useful primarily when the signal you use as the AI Convert Clock is not a periodic clock. For example, set this property to Rising to perform an analog to digital conversion on each rising edge o

### More:AI Convert:Active Edge

Specifies on which edge of the clock pulse an analog-to-digital conversion takes place.

This property is useful primarily when the signal you use as the AI Convert Clock is not a periodic clock. For example, set this property 
to Rising to perform an analog to digital conversion on each rising edge of an aperiodic signal.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AIConv.ActiveEdge |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Rising | 10280 | Rising edge(s). |
| --- | --- | --- |
| Falling | 10171 | Falling edge(s). |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr18eb.html language=enus -->
## TOPIC 01516: Sample Clock:Timebase Divisor

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr18eb.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr18eb.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of Sample Clock Timebase pulses needed to produce a single Sample Clock pulse. The rate of the Sample Clock is equal to (frequency of Sample Clock Timebase) / (value of this property). If the Sample Clock Timebase is not a periodic clock, the value of this property determines th

### Sample Clock:Timebase Divisor

Specifies the number of Sample Clock Timebase pulses needed to produce a single Sample Clock pulse.

The rate of the Sample Clock is equal to (frequency of Sample Clock Timebase) / (value of this property).

If the Sample Clock Timebase is not a periodic clock, the value of this property determines the number 
of Sample Clock Timebase edges that the device must receive before producing each Sample Clock pulse. Use 
 [SampClk.Timebase.ActiveEdge](/csh?context=nidaqmx_daqmxprop_attr18ec)
 to specify
the polarity of these edges.

Setting this property has a similar effect to setting 
 [SampClk.Rate](/csh?context=nidaqmx_daqmxprop_attr1344)
 . Use 
 [SampClk.Rate](/csh?context=nidaqmx_daqmxprop_attr1344)
 when you know the rate of the Sample Clock Timebase 
and you want to acquire or generate samples at the specified rate. Use this property when you have an external timebase that 
you want to divide down and use as the Sample Clock, but you do not know rate of the external timebase.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SampClk.TimebaseDiv |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr18ec.html language=enus -->
## TOPIC 01517: Sample Clock:Timebase:Active Edge

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr18ec.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr18ec.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge to recognize a Sample Clock Timebase pulse. This property is useful primarily when the signal you use as the Sample Clock Timebase is not a periodic clock. Remarks The following table lists the characteristics of this property. Short Name SampClk.Timebase.ActiveEdge Data type

### Sample Clock:Timebase:Active Edge

Specifies on which edge to recognize a Sample Clock Timebase pulse. This property is useful primarily when the signal you use as the Sample Clock Timebase is not a periodic clock.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SampClk.Timebase.ActiveEdge |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Rising | 10280 | Rising edge(s). |
| --- | --- | --- |
| Falling | 10171 | Falling edge(s). |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr2195.html language=enus -->
## TOPIC 01518: Change Detection:Digital Input:Rising Edge Physical Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr2195.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr2195.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the names of the digital lines or ports on which to detect rising edges. The lines or ports must be used by virtual channels in the task. You also can specify a string that contains a list or range of digital lines or ports. Remarks The following table lists the characteristics of this pro

### Change Detection:Digital Input:Rising Edge Physical Channels

Specifies the names of the digital lines or ports on which to detect rising edges. The lines or ports must be used by virtual channels in the task. You also can specify a string that contains a 
 [list or range](/csh?context=nidaqmx_mxcncpts_physchannames)
 of digital lines or ports.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ChangeDetect.DI.RisingEdgePhysicalChans |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr2196.html language=enus -->
## TOPIC 01519: Change Detection:Digital Input:Falling Edge Physical Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr2196.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr2196.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the names of the digital lines or ports on which to detect falling edges. The lines or ports must be used by virtual channels in the task. You also can specify a string that contains a list or range of digital lines or ports. Remarks The following table lists the characteristics of this pr

### Change Detection:Digital Input:Falling Edge Physical Channels

Specifies the names of the digital lines or ports on which to detect falling edges. The lines or ports must be used by virtual channels in the task. You also can specify a string that contains a 
 [list or range](/csh?context=nidaqmx_mxcncpts_physchannames)
 of digital lines or ports.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ChangeDetect.DI.FallingEdgePhysicalChans |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr21a0.html language=enus -->
## TOPIC 01520: On Demand:Simultaneous Analog Output Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr21a0.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr21a0.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to update all channels in the task simultaneously, rather than updating channels independently when you write a sample to that channel. Remarks The following table lists the characteristics of this property. Short Name SimultaneousAOEnable Data type cbool.png Permissions Read/Write

### On Demand:Simultaneous Analog Output Enable

Specifies whether to update all channels in the task simultaneously, rather than updating channels independently when you write a sample to that channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SimultaneousAOEnable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr221e.html language=enus -->
## TOPIC 01521: Sample Clock:Digital Filter:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr221e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr221e.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply the pulse width filter to the signal. Remarks The following table lists the characteristics of this property. Short Name SampClk.DigFltr.Enable Data type cbool.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time E

### Sample Clock:Digital Filter:Enable

Specifies whether to apply the pulse width 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 to the signal.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SampClk.DigFltr.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr221f.html language=enus -->
## TOPIC 01522: Sample Clock:Digital Filter:Minimum Pulse Width

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr221f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr221f.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. Remarks The following table lists the characteristics of this property. Short Name SampClk.DigFltr.MinPulseWidth Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in R

### Sample Clock:Digital Filter:Minimum Pulse Width

Specifies in seconds the minimum pulse width the 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 recognizes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SampClk.DigFltr.MinPulseWidth |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr2220.html language=enus -->
## TOPIC 01523: Sample Clock:Digital Filter:Timebase:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr2220.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr2220.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to use as the timebase of the pulse width filter. Remarks The following table lists the characteristics of this property. Short Name SampClk.DigFltr.TimebaseSrc Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running

### Sample Clock:Digital Filter:Timebase:Source

Specifies the input 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 of the signal to use as the timebase of the pulse width filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SampClk.DigFltr.TimebaseSrc |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr2221.html language=enus -->
## TOPIC 01524: Sample Clock:Digital Filter:Timebase:Rate

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr2221.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr2221.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. Remarks The following table lists the characteristics of this property. Short Name SampClk.DigFltr.TimebaseRate Data type cdbl.png Permissions Read/Write Resettable True Setta

### Sample Clock:Digital Filter:Timebase:Rate

Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SampClk.DigFltr.TimebaseRate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr2222.html language=enus -->
## TOPIC 01525: Sample Clock:Digital Synchronization:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr2222.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr2222.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. This property does not affect the minimum pulse width recognized by the device, but setting this property to TRUE does limit the speed at which the device recognizes transitions to less

### Sample Clock:Digital Synchronization:Enable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

This property does not affect the minimum pulse width recognized by the device, 
but setting this property to TRUE does limit the speed at which the device recognizes transitions 
to less than the frequency of the internal timebase.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SampClk.DigSync.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr223d.html language=enus -->
## TOPIC 01526: More:Synchronization Pulse:Digital Edge:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr223d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr223d.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the synchronization pulse. The synchronization pulse resets the clock dividers and the ADCs/DACs on the device. Remarks The following table lists the characteristics of this property. Short Name SyncPulse.Src Data type cdaqmxscale.png Permissions Read/W

### More:Synchronization Pulse:Digital Edge:Source

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 of the signal to use as the synchronization pulse. The synchronization pulse resets the clock dividers and the ADCs/DACs on the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SyncPulse.Src |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr223e.html language=enus -->
## TOPIC 01527: More:Synchronization Pulse:Synchronization Time

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr223e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr223e.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in seconds the delay required to reset the ADCs/DACs after the device receives the synchronization pulse. This time is the minimum delay required by the device between the receipt of the synchronization pulse and the start of the acquisition. Read this property for all slave devices and se

### More:Synchronization Pulse:Synchronization Time

Indicates in seconds the delay required to reset the ADCs/DACs after the device receives the synchronization pulse.

This time is the minimum delay required by the device between the receipt of the synchronization pulse and the start of the acquisition. Read this 
property for all slave devices and set 
 [SyncPulse.MinDelayToStart](/csh?context=nidaqmx_daqmxprop_attr223f)
 for the master device to the maximum of these delays.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SyncPulse.SyncTime |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr223f.html language=enus -->
## TOPIC 01528: More:Synchronization Pulse:Minimum Delay To Start

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr223f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr223f.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the amount of time that elapses after the master device issues the synchronization pulse before the task starts. Read SyncPulse.SyncTime for all slave devices, and set this property for the master device to the maximum of those values. Remarks The following table lists the chara

### More:Synchronization Pulse:Minimum Delay To Start

Specifies in seconds the amount of time that elapses after the master device issues the synchronization pulse before the task starts.

Read 
 [SyncPulse.SyncTime](/csh?context=nidaqmx_daqmxprop_attr223e)
 for all slave devices, and set this property for the master device to the maximum of those values.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SyncPulse.MinDelayToStart |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr22c2.html language=enus -->
## TOPIC 01529: Handshake:Delay After Transfer

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr22c2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr22c2.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of seconds to wait after a handshake cycle before starting a new handshake cycle. Remarks The following table lists the characteristics of this property. Short Name Hshk.DelayAfterXfer Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running devic

### Handshake:Delay After Transfer

Specifies the number of seconds to wait after a handshake cycle before starting a new handshake cycle.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Hshk.DelayAfterXfer |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr22c3.html language=enus -->
## TOPIC 01530: Handshake:Start Condition

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr22c3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr22c3.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the point in the handshake cycle that the device is in when the task starts. Remarks The following table lists the characteristics of this property. Short Name Hshk.StartCond Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available

### Handshake:Start Condition

Specifies the point in the handshake cycle that the device is in when the task starts.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Hshk.StartCond |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Immediate | 10198 | Device is waiting for space in the FIFO (for acquisition) or waiting for samples (for generation). |
| --- | --- | --- |
| Wait For Handshake Trigger Assert | 12550 | Device is waiting for the Handshake Trigger to assert. |
| Wait For Handshake Trigger Deassert | 12551 | Device is waiting for the Handshake Trigger to deassert. |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr22c4.html language=enus -->
## TOPIC 01531: Handshake:Sample Input Data When

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr22c4.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr22c4.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge of the Handshake Trigger an input task latches the data from the peripheral device. Remarks The following table lists the characteristics of this property. Short Name Hshk.SampleInputDataWhen Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Run

### Handshake:Sample Input Data When

Specifies on which edge of the Handshake Trigger an input task latches the data from the peripheral device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Hshk.SampleInputDataWhen |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Handshake Trigger Asserts | 12552 | Latch data when the Handshake Trigger asserts. |
| --- | --- | --- |
| Handshake Trigger Deasserts | 12553 | Latch data when the Handshake Trigger deasserts. |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr22c8.html language=enus -->
## TOPIC 01532: Sample Clock:Maximum Rate

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr22c8.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr22c8.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the maximum Sample Clock rate supported by the task, based on other timing settings. For output tasks, the maximum Sample Clock rate is the maximum rate of the DAC. For input tasks, NI-DAQmx calculates the maximum sampling rate differently for multiplexed devices than simultaneous sampling

### Sample Clock:Maximum Rate

Indicates the maximum Sample Clock rate supported by the task, based on other timing settings. For output tasks, the maximum Sample Clock rate is the maximum rate of the DAC. For input tasks, NI-DAQmx calculates the maximum sampling rate differently for 
 [multiplexed devices than simultaneous sampling devices](/csh?context=nidaqmx_mxcncpts_multisimulsamp)
 .

For multiplexed devices, NI-DAQmx calculates the maximum sample clock rate based on the maximum AI Convert Clock rate unless you set 
 [AIConv.Rate](/csh?context=nidaqmx_daqmxprop_attr1848)
 . If you set that property, 
NI-DAQmx calculates the maximum sample clock rate based on that setting. Use 
 [AIConv.MaxRate](/csh?context=nidaqmx_daqmxprop_attr22c9)
 to query the maximum AI Convert Clock rate.
NI-DAQmx also uses the minimum sample clock delay to calculate the maximum sample clock rate unless you set 
 [DelayFromSampClk.Delay](/csh?context=nidaqmx_daqmxprop_attr1317)
 .

For simultaneous sampling devices, the maximum Sample Clock rate is the maximum rate of the ADC.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SampClk.MaxRate |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr22c9.html language=enus -->
## TOPIC 01533: More:AI Convert:Maximum Rate

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr22c9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr22c9.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the maximum convert rate supported by the task, given the current devices and channel count. This rate is generally faster than the default AI Convert Clock rate selected by NI-DAQmx, because NI-DAQmx adds in an additional 10 microseconds per channel settling time to compensate for most po

### More:AI Convert:Maximum Rate

Indicates the maximum convert rate supported by the task, given the current devices and channel count.

This rate is generally faster than the default AI Convert Clock rate selected by NI-DAQmx, because NI-DAQmx adds in an additional 10 microseconds per channel settling time to 
compensate for most potential system settling constraints.

For single channel tasks, the maximum AI Convert Clock rate is the maximum rate of the ADC. 
For multiple channel tasks, the maximum AI Convert Clock rate is the maximum convert rate of the analog hardware, including the ADC, filters, multiplexers, and amplifiers.
Signal conditioning accessories can further constrain the maximum AI Convert Clock based on timing and settling requirements.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AIConv.MaxRate |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr2961.html language=enus -->
## TOPIC 01534: Sample Clock:Underflow Behavior

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr2961.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr2961.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the action to take when the onboard memory of the device becomes empty. In either case, the sample clock does not stop. Remarks The following table lists the characteristics of this property. Short Name SampClk.UnderflowBehavior Data type ci32.png Permissions Read/Write Resettable True Set

### Sample Clock:Underflow Behavior

Specifies the action to take when the onboard memory of the device becomes empty. In either case, the sample clock does not stop.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SampClk.UnderflowBehavior |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Halt Output and Error | 14615 | Stop generating samples and return an error. |
| --- | --- | --- |
| Pause until Data Available | 14616 | Pause the task until samples are available in the FIFO. |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr2970.html language=enus -->
## TOPIC 01535: More:AI Convert:Active Devices

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr2970.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr2970.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a subset of devices in the task to configure. NI-DAQmx configures all devices in the task if you do not set this property. Remarks The following table lists the characteristics of this property. Short Name ActiveDevs Data type cdaqmxscale.png Permissions Write Only Resettable False Settabl

### More:AI Convert:Active Devices

Specifies a subset of devices in the task to configure. NI-DAQmx configures all devices in the task if you do not set this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ActiveDevs |
| --- | --- |
| Data type |  |
| Permissions | Write Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr2a26.html language=enus -->
## TOPIC 01536: Advanced:Sample Timing Engine

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr2a26.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr2a26.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies which timing engine to use for the task. Remarks The following table lists the characteristics of this property. Short Name SampTimingEngine Data type cu32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True

### Advanced:Sample Timing Engine

Specifies which 
 [timing engine](/csh?context=nidaqmx_mxdevconsid_multitimingengines)
 to use for the task.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SampTimingEngine |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr2edc.html language=enus -->
## TOPIC 01537: More:AI Convert:Digital Filter:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr2edc.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr2edc.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply a digital filter to the AI Convert Clock. Remarks The following table lists the characteristics of this property. Short Name AIConv.DigFltr.Enable Data type cbool.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Tim

### More:AI Convert:Digital Filter:Enable

Specifies whether to apply a digital 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 to the AI Convert Clock.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AIConv.DigFltr.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr2edd.html language=enus -->
## TOPIC 01538: More:AI Convert:Digital Filter:Minimum Pulse Width

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr2edd.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr2edd.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. Remarks The following table lists the characteristics of this property. Short Name AIConv.DigFltr.MinPulseWidth Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Ru

### More:AI Convert:Digital Filter:Minimum Pulse Width

Specifies in seconds the minimum pulse width the 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 recognizes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AIConv.DigFltr.MinPulseWidth |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr2ede.html language=enus -->
## TOPIC 01539: More:AI Convert:Digital Filter:Timebase:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr2ede.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr2ede.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the timebase of the digital filter. Remarks The following table lists the characteristics of this property. Short Name AIConv.DigFltr.TimebaseSrc Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running device-spec

### More:AI Convert:Digital Filter:Timebase:Source

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 of the signal to use as the timebase of the digital filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AIConv.DigFltr.TimebaseSrc |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr2edf.html language=enus -->
## TOPIC 01540: More:AI Convert:Digital Filter:Timebase:Rate

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr2edf.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr2edf.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. Remarks The following table lists the characteristics of this property. Short Name AIConv.DigFltr.TimebaseRate Data type cdbl.png Permissions Read/Write Resettable True Settable W

### More:AI Convert:Digital Filter:Timebase:Rate

Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AIConv.DigFltr.TimebaseRate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr2ee0.html language=enus -->
## TOPIC 01541: More:AI Convert:Digital Synchronization:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr2ee0.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr2ee0.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. Remarks The following table lists the characteristics of this property. Short Name AIConv.DigSync.Enable Data type cbool.png Permissions Read/Write Resettable True Settable While Task Is

### More:AI Convert:Digital Synchronization:Enable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AIConv.DigSync.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr2efa.html language=enus -->
## TOPIC 01542: Change Detection:Digital Input:Tristate

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr2efa.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr2efa.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to tristate lines specified with ChangeDetect.DI.RisingEdgePhysicalChans and ChangeDetect.DI.FallingEdgePhysicalChans that are not in a virtual channel in the task. If you set this property to TRUE, NI-DAQmx tristates rising/falling edge lines that are not in a virtual channel in t

### Change Detection:Digital Input:Tristate

Specifies whether to tristate lines specified with 
 [ChangeDetect.DI.RisingEdgePhysicalChans](/csh?context=nidaqmx_daqmxprop_attr2195)
 and 
 [ChangeDetect.DI.FallingEdgePhysicalChans](/csh?context=nidaqmx_daqmxprop_attr2196)
 that are not in a virtual channel in the task. If you set this property to TRUE, NI-DAQmx tristates rising/falling edge lines that are not in a virtual channel in the task. If you set this property to FALSE, NI-DAQmx does not modify the configuration of rising/falling edge lines that are not in a virtual channel in the task, even if the lines were previously tristated. Set this property to FALSE to detect changes on lines in other tasks or to detect changes on output-only lines.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ChangeDetect.DI.Tristate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr2efc.html language=enus -->
## TOPIC 01543: Sample Clock:Overrun Behavior

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr2efc.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr2efc.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the action to take if Sample Clock edges occur faster than the device can handle them. Remarks The following table lists the characteristics of this property. Short Name SampClk.OverrunBehavior Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-

### Sample Clock:Overrun Behavior

Specifies the action to take if Sample Clock edges occur faster than the device can handle them.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SampClk.OverrunBehavior |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Stop Task And Error | 15862 | Stop task and return an error. |
| --- | --- | --- |
| Ignore Overruns | 15863 | NI-DAQmx ignores Sample Clock overruns, and the task continues to run. |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr2efd.html language=enus -->
## TOPIC 01544: Implicit:Underflow Behavior

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr2efd.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr2efd.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the action to take when the onboard memory of the device becomes empty. Remarks The following table lists the characteristics of this property. Short Name Implicit.UnderflowBehavior Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Ava

### Implicit:Underflow Behavior

Specifies the action to take when the onboard memory of the device becomes empty.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Implicit.UnderflowBehavior |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Halt Output and Error | 14615 | Stop generating samples and return an error. |
| --- | --- | --- |
| Pause until Data Available | 14616 | Pause the task until samples are available in the FIFO. |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr2f1b.html language=enus -->
## TOPIC 01545: Sample Clock:Terminal

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr2f1b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr2f1b.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the name of the internal Sample Clock terminal for the task. This property does not return the name of the Sample Clock source terminal specified with SampClk.Src . Remarks The following table lists the characteristics of this property. Short Name SampClk.Term Data type cdaqmxscale.png Per

### Sample Clock:Terminal

Indicates the name of the internal Sample Clock terminal for the task. This property does not return the name of the Sample Clock source terminal specified with 
 [SampClk.Src](/csh?context=nidaqmx_daqmxprop_attr1852)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SampClk.Term |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr2f1c.html language=enus -->
## TOPIC 01546: Sample Clock:Timebase:Terminal

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr2f1c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr2f1c.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the name of the internal Sample Clock Timebase terminal for the task. This property does not return the name of the Sample Clock Timebase source terminal specified with SampClk.Timebase.Src . Remarks The following table lists the characteristics of this property. Short Name SampClk.Timebas

### Sample Clock:Timebase:Terminal

Indicates the name of the internal Sample Clock Timebase terminal for the task. This property does not return the name of the Sample Clock Timebase source terminal specified with 
 [SampClk.Timebase.Src](/csh?context=nidaqmx_daqmxprop_attr1308)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SampClk.Timebase.Term |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr2f7c.html language=enus -->
## TOPIC 01547: More:Synchronization Pulse:Reset Time

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr2f7c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr2f7c.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in seconds the amount of time required for the ADCs or DACs on the device to reset. When synchronizing devices, query this property on all devices and note the largest reset time. Then, for each device, subtract the value of this property from the largest reset time and set SyncPulse.Reset

### More:Synchronization Pulse:Reset Time

Indicates in seconds the amount of time required for the ADCs or DACs on the device to reset. When synchronizing devices, query this property on all devices and note the largest reset time. Then, for each device, subtract the value of this property from the largest reset time and set 
 [SyncPulse.ResetDelay](/csh?context=nidaqmx_daqmxprop_attr2f7d)
 to the resulting value.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SyncPulse.ResetTime |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr2f7d.html language=enus -->
## TOPIC 01548: More:Synchronization Pulse:Reset Delay

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr2f7d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr2f7d.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the amount of time to wait after the Synchronization Pulse before resetting the ADCs or DACs on the device. When synchronizing devices, query SyncPulse.ResetTime on all devices and note the largest reset time. Then, for each device, subtract the reset time from the largest reset

### More:Synchronization Pulse:Reset Delay

Specifies in seconds the amount of time to wait after the Synchronization Pulse before resetting the ADCs or DACs on the device. When synchronizing devices, query 
 [SyncPulse.ResetTime](/csh?context=nidaqmx_daqmxprop_attr2f7c)
 on all devices and note the largest reset time. Then, for each device, subtract the reset time from the largest reset time and set this property to the resulting value.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SyncPulse.ResetDelay |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr2f7e.html language=enus -->
## TOPIC 01549: More:Synchronization Clock:Interval

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr2f7e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr2f7e.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the interval, in Sample Clock periods, between each internal Synchronization Clock pulse. NI-DAQmx uses this pulse for synchronization of triggers between multiple devices at different rates. Refer to device documentation for information about how to calculate this value. Remarks The follo

### More:Synchronization Clock:Interval

Specifies the interval, in Sample Clock periods, between each internal Synchronization Clock pulse. NI-DAQmx uses this pulse for synchronization of triggers between multiple devices at different rates. Refer to device documentation for information about how to calculate this value.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SyncClk.Interval |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr2f85.html language=enus -->
## TOPIC 01550: More:Synchronization Pulse:Terminal

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr2f85.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr2f85.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the name of the internal Synchronization Pulse terminal for the task. This property does not return the name of the source terminal. Remarks The following table lists the characteristics of this property. Short Name SyncPulse.Term Data type cdaqmxscale.png Permissions Read Only Resettable

### More:Synchronization Pulse:Terminal

Indicates the name of the internal Synchronization Pulse terminal for the task. This property does not return the name of the source terminal.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SyncPulse.Term |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr30fc.html language=enus -->
## TOPIC 01551: Sample Clock:Write Waveform:Use Initial Waveform dt

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr30fc.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr30fc.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies that the value of SampClk.Rate will be determined by the dt component of the initial DAQmx Write waveform input for Output tasks. Remarks The following table lists the characteristics of this property. Short Name SampClk.WriteWfm.UseInitialWfmDT Data type cbool.png Permissions Read/Write R

### Sample Clock:Write Waveform:Use Initial Waveform dt

Specifies that the value of 
 [SampClk.Rate](/csh?context=nidaqmx_daqmxprop_attr1344)
 will be determined by the dt component of the initial DAQmx Write waveform input for Output tasks.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SampClk.WriteWfm.UseInitialWfmDT |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr3136.html language=enus -->
## TOPIC 01552: More:Synchronization Pulse:Type

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr3136.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr3136.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of sync pulse used in the task. Remarks The following table lists the characteristics of this property. Short Name SyncPulse.Type Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True Onboard 1612

### More:Synchronization Pulse:Type

Specifies the type of sync pulse used in the task.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SyncPulse.Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Onboard | 16128 | Use the synchronization pulse type specified by the device. |
| --- | --- | --- |
| Digital Edge | 10150 | Digital Edge synchronization. |
| Time | 15996 | Time synchronization. |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr3137.html language=enus -->
## TOPIC 01553: More:Synchronization Pulse:Time:When

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr3137.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr3137.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the start time of the sync pulse. Remarks The following table lists the characteristics of this property. Short Name SyncPulse.Time.When Data type catrn.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True

### More:Synchronization Pulse:Time:When

Specifies the start time of the sync pulse.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SyncPulse.Time.When |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr3138.html language=enus -->
## TOPIC 01554: More:Synchronization Pulse:Time:Timescale

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr3138.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr3138.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the timescale to be used for timestamps for a sync pulse. Remarks The following table lists the characteristics of this property. Short Name SyncPulse.Time.Timescale Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Ti

### More:Synchronization Pulse:Time:Timescale

Specifies the timescale to be used for timestamps for a sync pulse.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SyncPulse.Time.Timescale |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Host Time | 16126 | Use the host device. |
| --- | --- | --- |
| I/O Device Time | 16127 | Use the I/O device. |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr3139.html language=enus -->
## TOPIC 01555: Advanced:First Sample Timestamp:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr3139.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr3139.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the first sample timestamp. Remarks The following table lists the characteristics of this property. Short Name FirstSampTimestamp.Enable Data type cbool.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine

### Advanced:First Sample Timestamp:Enable

Specifies whether to enable the first sample timestamp.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FirstSampTimestamp.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr313a.html language=enus -->
## TOPIC 01556: Advanced:First Sample Timestamp:Value

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr313a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr313a.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the timestamp of the first sample. Remarks The following table lists the characteristics of this property. Short Name FirstSampTimestamp.Val Data type catrn.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### Advanced:First Sample Timestamp:Value

Indicates the timestamp of the first sample.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FirstSampTimestamp.Val |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr313b.html language=enus -->
## TOPIC 01557: Advanced:First Sample Timestamp:Timescale

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr313b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr313b.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the timescale to be used for the first sample timestamp. Remarks The following table lists the characteristics of this property. Short Name FirstSampTimestamp.Timescale Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run

### Advanced:First Sample Timestamp:Timescale

Specifies the timescale to be used for the first sample timestamp.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FirstSampTimestamp.Timescale |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Host Time | 16126 | Use the host device. |
| --- | --- | --- |
| I/O Device Time | 16127 | Use the I/O device. |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr3182.html language=enus -->
## TOPIC 01558: Advanced:First Sample Clock Time:When

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr3182.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr3182.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the time of the first sample clock pulse. Remarks The following table lists the characteristics of this property. Short Name FirstSampClk.When Data type catrn.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True

### Advanced:First Sample Clock Time:When

Specifies the time of the first sample clock pulse.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FirstSampClk.When |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr3183.html language=enus -->
## TOPIC 01559: Advanced:First Sample Clock Time:Timescale

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr3183.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr3183.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the timescale to be used for the value of FirstSampClk.When . Remarks The following table lists the characteristics of this property. Short Name FirstSampClk.Timescale Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-

### Advanced:First Sample Clock Time:Timescale

Specifies the timescale to be used for the value of 
 [FirstSampClk.When](/csh?context=nidaqmx_daqmxprop_attr3182)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FirstSampClk.Timescale |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Host Time | 16126 | Use the host device. |
| --- | --- | --- |
| I/O Device Time | 16127 | Use the I/O device. |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr31aa.html language=enus -->
## TOPIC 01560: Advanced:First Sample Clock Time:Offset

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr31aa.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr31aa.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies, in seconds, the offset to apply to the FirstSampClk.When value. This offset modifies when the first sample clock occurs and is used to account for known delays in the signal path. Remarks The following table lists the characteristics of this property. Short Name FirstSampClk.Offset Data t

### Advanced:First Sample Clock Time:Offset

Specifies, in seconds, the offset to apply to the 
 [FirstSampClk.When](/csh?context=nidaqmx_daqmxprop_attr3182)
 value. This offset modifies when the first sample clock occurs and is used to account for known delays in the signal path.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FirstSampClk.Offset |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger-p.html language=enus -->
## TOPIC 01561: DAQmx Trigger Properties

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger-p.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger-p.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the DAQmx Trigger properties to configure triggering for a task.

### DAQmx Trigger Properties

Use the DAQmx Trigger properties to configure triggering for a task.

- [Advanced:Synchronization Type](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2f80.html) Specifies the role of the device in a synchronized system. Setting this value to Master or Slave enables trigger skew correction . If you enable trigger skew correction, set this property to Master on only one device, and set this property to Slave on the other devices.
- [Deprecated:More:Advance:Digital Edge:Digital Filter:Enable](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2238.html) (Deprecated) Specifies whether to apply the pulse width filter to the signal.
- [Deprecated:More:Advance:Digital Edge:Edge](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1360.html) (Deprecated) Specifies on which edge of a digital signal to advance to the next entry in a scan list.
- [Deprecated:More:Advance:Digital Edge:Source](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1362.html) (Deprecated) Specifies the name of a terminal where there is a digital signal to use as the source of the Advance Trigger.
- [Deprecated:More:Advance:Trigger Type](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1365.html) (Deprecated) Specifies the type of trigger to use to advance to the next entry in a switch scan list.
- [More:Arm Start:Digital Edge:Digital Filter:Enable](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr222d.html) Specifies whether to apply the pulse width filter to the signal.
- [More:Arm Start:Digital Edge:Digital Filter:Minimum Pulse Width](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr222e.html) Specifies in seconds the minimum pulse width the filter recognizes.
- [More:Arm Start:Digital Edge:Digital Filter:Timebase:Rate](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2230.html) Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.
- [More:Arm Start:Digital Edge:Digital Filter:Timebase:Source](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr222f.html) Specifies the input terminal of the signal to use as the timebase of the pulse width filter.
- [More:Arm Start:Digital Edge:Digital Synchronization:Enable](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2231.html) Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.
- [More:Arm Start:Digital Edge:Edge](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1415.html) Specifies on which edge of a digital signal to arm the task for a Start Trigger.
- [More:Arm Start:Digital Edge:Source](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1417.html) Specifies the name of a terminal where there is a digital signal to use as the source of the Arm Start Trigger.
- [More:Arm Start:Terminal](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2f7f.html) Indicates the name of the internal Arm Start Trigger terminal for the task. This property does not return the name of the trigger source terminal.
- [More:Arm Start:Time:Timescale](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr3132.html) Specifies the timescale to be used for timestamps used in an arm start time trigger.
- [More:Arm Start:Time:When](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr3131.html) Specifies when to trigger the arm start trigger.
- [More:Arm Start:Timestamp:Enable](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr3133.html) Specifies whether the arm start trigger timestamp is enabled. If the timestamp is enabled but no resources are available, an error will be returned at run time.
- [More:Arm Start:Timestamp:Timescale](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr3135.html) Specifies the arm start trigger timestamp timescale.
- [More:Arm Start:Timestamp:Value](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr3134.html) Indicates the arm start trigger timestamp value.
- [More:Arm Start:Trigger Type](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1414.html) Specifies the type of trigger to use to arm the task for a Start Trigger. If you configure an Arm Start Trigger, the task does not respond to a Start Trigger until the device receives the Arm Start Trigger.
- [More:Handshake:Interlocked:Asserted Level](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr22b9.html) Specifies the asserted level of the Handshake Trigger .
- [More:Handshake:Interlocked:Source](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr22b8.html) Specifies the source terminal of the Handshake Trigger .
- [More:Handshake:Trigger Type](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr22b7.html) Specifies the type of Handshake Trigger to use.
- [More:Pause:Analog Level:Coupling](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2236.html) Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel .
- [More:Pause:Analog Level:Digital Filter:Enable](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef0.html) Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay above or below the trigger level for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the hysteresis window rapidly.
- [More:Pause:Analog Level:Digital Filter:Minimum Pulse Width](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef1.html) Specifies in seconds the minimum pulse width the filter recognizes.
- [More:Pause:Analog Level:Digital Filter:Timebase:Rate](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef3.html) Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.
- [More:Pause:Analog Level:Digital Filter:Timebase:Source](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef2.html) Specifies the terminal of the signal to use as the timebase of the digital filter.
- [More:Pause:Analog Level:Digital Synchronization:Enable](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef4.html) Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.
- [More:Pause:Analog Level:Hysteresis](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1368.html) Specifies a hysteresis level in the units of the measurement or generation. If Pause.AnlgLvl.When is Above Level, the trigger does not deassert until the source signal passes below Pause.AnlgLvl.Lvl minus the hysteresis. If Pause.AnlgLvl.When is Below Level, the trigger does not deassert until the source signal passes above Pause.AnlgLvl.Lvl plus the hysteresis. Hysteresis is always enabled. Set this property to a non-zero value to use hysteresis.
- [More:Pause:Analog Level:Level](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1369.html) Specifies the threshold at which to pause the task. Specify this value in the units of the measurement or generation. Use Pause.AnlgLvl.When to specify whether the task pauses above or below this threshold.
- [More:Pause:Analog Level:Pause When](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1371.html) Specifies whether the task pauses above or below the threshold you specify with Pause.AnlgLvl.Lvl .
- [More:Pause:Analog Level:Source](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1370.html) Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the trigger.
- [More:Pause:Analog Window:Bottom](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1375.html) Specifies the lower limit of the window. Specify this value in the units of the measurement or generation.
- [More:Pause:Analog Window:Coupling](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2237.html) Specifies the coupling for the source signal of the terminal if the source is a terminal rather than a virtual channel .
- [More:Pause:Analog Window:Digital Filter:Enable](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef5.html) Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay within the trigger window for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the window rapidly.
- [More:Pause:Analog Window:Digital Filter:Minimum Pulse Width](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef6.html) Specifies in seconds the minimum pulse width the filter recognizes.
- [More:Pause:Analog Window:Digital Filter:Timebase:Rate](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef8.html) Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.
- [More:Pause:Analog Window:Digital Filter:Timebase:Source](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef7.html) Specifies the terminal of the signal to use as the timebase of the digital filter.
- [More:Pause:Analog Window:Digital Synchronization:Enable](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef9.html) Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.
- [More:Pause:Analog Window:Pause When](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1374.html) Specifies whether the task pauses while the trigger signal is inside or outside the window you specify with Pause.AnlgWin.Btm and Pause.AnlgWin.Top .
- [More:Pause:Analog Window:Source](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1373.html) Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the trigger.
- [More:Pause:Analog Window:Top](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1376.html) Specifies the upper limit of the window. Specify this value in the units of the measurement or generation.
- [More:Pause:Digital Level:Digital Filter:Enable](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2228.html) Specifies whether to apply a digital filter to the trigger signal.
- [More:Pause:Digital Level:Digital Filter:Minimum Pulse Width](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2229.html) Specifies in seconds the minimum pulse width the filter recognizes.
- [More:Pause:Digital Level:Digital Filter:Timebase:Rate](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr222b.html) Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.
- [More:Pause:Digital Level:Digital Filter:Timebase:Source](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr222a.html) Specifies the input terminal of the signal to use as the timebase of the pulse width filter.
- [More:Pause:Digital Level:Digital Synchronization:Enable](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr222c.html) Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.
- [More:Pause:Digital Level:Pause When](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1380.html) Specifies whether the task pauses while the signal is high or low.
- [More:Pause:Digital Level:Source](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1379.html) Specifies the name of a terminal where there is a digital signal to use as the source of the Pause Trigger.
- [More:Pause:Digital Pattern:Pattern](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2188.html) Specifies the digital pattern that must be met for the Pause Trigger to occur.
- [More:Pause:Digital Pattern:Pause When](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2170.html) Specifies if the Pause Trigger occurs when the physical channels specified with Pause.DigPattern.Src match or differ from the digital pattern specified with Pause.DigPattern.Pattern .
- [More:Pause:Digital Pattern:Source](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr216f.html) Specifies the physical channels to use for pattern matching. The order of the physical channels determines the order of the pattern. If a port is included, the lines within the port are in ascending order.
- [More:Pause:Terminal](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2f20.html) Indicates the name of the internal Pause Trigger terminal for the task. This property does not return the name of the trigger source terminal.
- [More:Pause:Trigger Type](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1366.html) Specifies the type of trigger to use to pause a task.
- [Reference:Analog Edge:Coupling](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2235.html) Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel .
- [Reference:Analog Edge:Digital Filter:Enable](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee6.html) Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay above or below the trigger level for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the hysteresis window rapidly.
- [Reference:Analog Edge:Digital Filter:Minimum Pulse Width](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee7.html) Specifies in seconds the minimum pulse width the filter recognizes.
- [Reference:Analog Edge:Digital Filter:Timebase:Rate](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee9.html) Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.
- [Reference:Analog Edge:Digital Filter:Timebase:Source](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee8.html) Specifies the terminal of the signal to use as the timebase of the digital filter.
- [Reference:Analog Edge:Digital Synchronization:Enable](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2eea.html) Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.
- [Reference:Analog Edge:Hysteresis](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1421.html) Specifies a hysteresis level in the units of the measurement. If Ref.AnlgEdge.Slope is Rising, the trigger does not deassert until the source signal passes below Ref.AnlgEdge.Lvl minus the hysteresis. If Ref.AnlgEdge.Slope is Falling, the trigger does not deassert until the source signal passes above Ref.AnlgEdge.Lvl plus the hysteresis. Hysteresis is always enabled. Set this property to a non-zero value to use hysteresis.
- [Reference:Analog Edge:Level](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1422.html) Specifies in the units of the measurement the threshold at which the Reference Trigger occurs. Use Ref.AnlgEdge.Slope to specify on which slope to trigger at this threshold.
- [Reference:Analog Edge:Slope](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1423.html) Specifies on which slope of the source signal the Reference Trigger occurs.
- [Reference:Analog Edge:Source](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1424.html) Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the Reference Trigger .
- [Reference:Analog Multiple Edge:Couplings](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr312a.html) Specifies an array that describes the couplings for the corresponding source signal of the trigger if the source is a terminal rather than a virtual channel. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.
- [Reference:Analog Multiple Edge:Hystereses](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr3129.html) Specifies an array of hysteresis levels in the units of the measurement or generation. If the corresponding element of Ref.AnlgMultiEdge.Slopes is Rising, the trigger does not deassert until the source signal passes below the corresponding element of Ref.AnlgMultiEdge.Lvls minus the hysteresis. If Ref.AnlgEdge.Slope is Falling, the trigger does not deassert until the source signal passes above Ref.AnlgEdge.Lvl plus the hysteresis. Hysteresis is always enabled. Set this property to a non-zero value to use hysteresis. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.
- [Reference:Analog Multiple Edge:Levels](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr3128.html) Specifies an array of thresholds in the units of the measurement or generation to start acquiring or generating samples. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.
- [Reference:Analog Multiple Edge:Slopes](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr3127.html) Specifies an array of slopes on which to trigger task to start generating or acquiring samples. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.
- [Reference:Analog Multiple Edge:Sources](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr3126.html) Specifies a List and/or range of analog sources that are going to be used for Analog triggering. Each source corresponds to an element in each of the Analog Multi Edge property arrays, if they are not empty.
- [Reference:Analog Window:Bottom](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1428.html) Specifies the lower limit of the window . Specify this value in the units of the measurement.
- [Reference:Analog Window:Coupling](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1857.html) Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel .
- [Reference:Analog Window:Digital Filter:Enable](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2eeb.html) Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay within the trigger window for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the window rapidly.
- [Reference:Analog Window:Digital Filter:Minimum Pulse Width](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2eec.html) Specifies in seconds the minimum pulse width the filter recognizes.
- [Reference:Analog Window:Digital Filter:Timebase:Rate](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2eee.html) Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.
- [Reference:Analog Window:Digital Filter:Timebase:Source](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2eed.html) Specifies the terminal of the signal to use as the timebase of the digital filter.
- [Reference:Analog Window:Digital Synchronization:Enable](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2eef.html) Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.
- [Reference:Analog Window:Source](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1426.html) Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the Reference Trigger .
- [Reference:Analog Window:Top](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1429.html) Specifies the upper limit of the window . Specify this value in the units of the measurement.
- [Reference:Analog Window:Trigger When](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1427.html) Specifies whether the Reference Trigger occurs when the source signal enters the window or when it leaves the window. Use Ref.AnlgWin.Btm and Ref.AnlgWin.Top to specify the window.
- [Reference:Auto Trigger:Enable](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2ec1.html) Specifies whether to send a software trigger to the device when a hardware trigger is no longer active in order to prevent a timeout.
- [Reference:Auto Triggered](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2ec2.html) Indicates whether a completed acquisition was triggered by the auto trigger. If an acquisition has not completed after the task starts, this property returns FALSE. This property is only applicable when Ref.AutoTrig.Enable is TRUE.
- [Reference:Digital Edge:Digital Filter:Enable](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2ed7.html) Specifies whether to apply a digital filter to the trigger signal.
- [Reference:Digital Edge:Digital Filter:Minimum Pulse Width](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2ed8.html) Specifies in seconds the minimum pulse width the filter recognizes.
- [Reference:Digital Edge:Digital Filter:Timebase:Rate](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2eda.html) Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.
- [Reference:Digital Edge:Digital Filter:Timebase:Source](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2ed9.html) Specifies the terminal of the signal to use as the timebase of the digital filter.
- [Reference:Digital Edge:Digital Synchronization:Enable](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2edb.html) Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.
- [Reference:Digital Edge:Edge](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1430.html) Specifies on what edge of a digital pulse the Reference Trigger occurs.
- [Reference:Digital Edge:Source](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1434.html) Specifies the name of a terminal where there is a digital signal to use as the source of the Reference Trigger .
- [Reference:Digital Pattern:Pattern](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2187.html) Specifies the digital pattern that must be met for the Reference Trigger to occur.
- [Reference:Digital Pattern:Source](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1437.html) Specifies the physical channels to use for pattern matching. The order of the physical channels determines the order of the pattern. If a port is included, the order of the physical channels within the port is in ascending order.
- [Reference:Digital Pattern:Trigger When](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1438.html) Specifies whether the Reference Trigger occurs when the physical channels specified with Ref.DigPattern.Src match or differ from the digital pattern specified with Ref.DigPattern.Pattern .
- [Reference:More:Delay](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1483.html) Specifies in seconds the time to wait after the device receives the Reference Trigger before switching from pretrigger to posttrigger samples.
- [Reference:More:Maximum Number of Triggers to Detect](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr3120.html) Specifies the maximum number of times the task will detect a reference trigger during the task. The number of times a trigger is detected and acted upon by the module may be less than the specified amount if the task stops early because of trigger/retrigger window expiration. Specifying the Maximum Number of Triggers to Detect to be 0 causes the driver to automatically set this value to the maximum possible number of triggers detectable by the device and configuration combination. Note: The number of detected triggers may be less than number of trigger events occurring, because the devices were unable to respond to the trigger.
- [Reference:More:Retrigger Window](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr311f.html) Specifies the duration in seconds after each trigger during which the device may trigger. Once the window has passed, the device stops detecting triggers, and the task will stop after the device finishes acquiring post-trigger samples that it already started. Specifying a Retrigger Window of -1 causes the window to be infinite.
- [Reference:More:Retriggerable](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr311d.html) Specifies whether a finite task resets, acquires pretrigger samples, and waits for another Reference Trigger after the task completes. When you set this property to TRUE, the device will acquire post-trigger samples, reset, and acquire pretrigger samples each time the Reference Trigger occurs until the task stops. The device ignores a trigger if it is in the process of acquiring signals.
- [Reference:More:Trigger Window](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr311e.html) Specifies the duration in seconds after the task starts during which the device may trigger. Once the window has passed, the device stops detecting triggers, and the task will stop after the device finishes acquiring post-trigger samples that it already started. If no triggers are detected during the entire period, then no data will be returned. Specifying a Trigger Window of -1 causes the window to be infinite.
- [Reference:Pretrigger Samples per Channel](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1445.html) Specifies the minimum number of pretrigger samples to acquire from each channel before recognizing the reference trigger . Post-trigger samples per channel are equal to SampQuant.SampPerChan minus the number of pretrigger samples per channel.
- [Reference:Terminal](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2f1f.html) Indicates the name of the internal Reference Trigger terminal for the task. This property does not return the name of the trigger source terminal.
- [Reference:Timestamp:Enable](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr312e.html) Specifies whether the reference trigger timestamp is enabled. If the timestamp is enabled but no resources are available, an error will be returned at run time.
- [Reference:Timestamp:Timescale](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr3130.html) Specifies the reference trigger timestamp timescale.
- [Reference:Timestamp:Value](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr312f.html) Indicates the reference trigger timestamp value.
- [Reference:Trigger Type](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1419.html) Specifies the type of trigger to use to mark a reference point for the measurement.
- [Start:Analog Edge:Coupling](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2233.html) Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel .
- [Start:Analog Edge:Digital Filter:Enable](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee1.html) Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay above or below the trigger level for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the hysteresis window rapidly.
- [Start:Analog Edge:Digital Filter:Minimum Pulse Width](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee2.html) Specifies in seconds the minimum pulse width the filter recognizes.
- [Start:Analog Edge:Digital Filter:Timebase:Rate](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee4.html) Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.
- [Start:Analog Edge:Digital Filter:Timebase:Source](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee3.html) Specifies the terminal of the signal to use as the timebase of the digital filter.
- [Start:Analog Edge:Digital Synchronization:Enable](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee5.html) Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.
- [Start:Analog Edge:Hysteresis](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1395.html) Specifies a hysteresis level in the units of the measurement or generation. If Start.AnlgEdge.Slope is Rising, the trigger does not deassert until the source signal passes below Start.AnlgEdge.Lvl minus the hysteresis. If Start.AnlgEdge.Slope is Falling, the trigger does not deassert until the source signal passes above Start.AnlgEdge.Lvl plus the hysteresis. Hysteresis is always enabled. Set this property to a non-zero value to use hysteresis.
- [Start:Analog Edge:Level](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1396.html) Specifies at what threshold in the units of the measurement or generation to start acquiring or generating samples. Use Start.AnlgEdge.Slope to specify on which slope to trigger on this threshold.
- [Start:Analog Edge:Slope](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1397.html) Specifies on which slope of the trigger signal to start acquiring or generating samples.
- [Start:Analog Edge:Source](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1398.html) Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the Start Trigger.
- [Start:Analog Multiple Edge:Couplings](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr3125.html) Specifies an array that describes the couplings for the corresponding source signal of the trigger if the source is a terminal rather than a virtual channel. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.
- [Start:Analog Multiple Edge:Hystereses](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr3124.html) Specifies an array of hysteresis levels in the units of the measurement or generation. If the corresponding element of Start.AnlgMultiEdge.Slopes is Rising, the trigger does not deassert until the source signal passes below the corresponding element of Start.AnlgMultiEdge.Lvls minus the hysteresis. If Start.AnlgEdge.Slope is Falling, the trigger does not deassert until the source signal passes above Start.AnlgEdge.Lvl plus the hysteresis. Hysteresis is always enabled. Set this property to a non-zero value to use hysteresis. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.
- [Start:Analog Multiple Edge:Levels](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr3123.html) Specifies an array of thresholds in the units of the measurement or generation to start acquiring or generating samples. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.
- [Start:Analog Multiple Edge:Slopes](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr3122.html) Specifies an array of slopes on which to trigger task to start generating or acquiring samples. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.
- [Start:Analog Multiple Edge:Sources](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr3121.html) Specifies a list and/or range of analog sources that are going to be used for Analog triggering. Each source corresponds to an element in each of the Analog Multi Edge property arrays, if they are not empty.
- [Start:Analog Window:Bottom](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1402.html) Specifies the lower limit of the window . Specify this value in the units of the measurement or generation.
- [Start:Analog Window:Coupling](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2234.html) Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel .
- [Start:Analog Window:Digital Filter:Enable](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2eff.html) Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay within the trigger window for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the window rapidly.
- [Start:Analog Window:Digital Filter:Minimum Pulse Width](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2f00.html) Specifies in seconds the minimum pulse width the filter recognizes.
- [Start:Analog Window:Digital Filter:Timebase:Rate](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2f02.html) Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.
- [Start:Analog Window:Digital Filter:Timebase:Source](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2f01.html) Specifies the terminal of the signal to use as the timebase of the digital filter.
- [Start:Analog Window:Digital Synchronization:Enable](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2f03.html) Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.
- [Start:Analog Window:Source](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1400.html) Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the Start Trigger.
- [Start:Analog Window:Top](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1403.html) Specifies the upper limit of the window . Specify this value in the units of the measurement or generation.
- [Start:Analog Window:Trigger When](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1401.html) Specifies whether the task starts acquiring or generating samples when the signal enters or leaves the window you specify with Start.AnlgWin.Btm and Start.AnlgWin.Top .
- [Start:Digital Edge:Digital Filter:Enable](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2223.html) Specifies whether to apply a digital filter to the trigger signal.
- [Start:Digital Edge:Digital Filter:Minimum Pulse Width](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2224.html) Specifies in seconds the minimum pulse width the filter recognizes.
- [Start:Digital Edge:Digital Filter:Timebase:Rate](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2226.html) Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.
- [Start:Digital Edge:Digital Filter:Timebase:Source](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2225.html) Specifies the input terminal of the signal to use as the timebase of the pulse width filter.
- [Start:Digital Edge:Digital Synchronization:Enable](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2227.html) Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. If you set this property to TRUE, the device does not recognize and act upon the trigger until the next pulse of the internal timebase.
- [Start:Digital Edge:Edge](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1404.html) Specifies on which edge of a digital pulse to start acquiring or generating samples.
- [Start:Digital Edge:Source](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1407.html) Specifies the name of a terminal where there is a digital signal to use as the source of the Start Trigger.
- [Start:Digital Pattern:Pattern](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2186.html) Specifies the digital pattern that must be met for the Start Trigger to occur.
- [Start:Digital Pattern:Source](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1410.html) Specifies the physical channels to use for pattern matching. The order of the physical channels determines the order of the pattern. If a port is included, the order of the physical channels within the port is in ascending order.
- [Start:Digital Pattern:Trigger When](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1411.html) Specifies whether the Start Trigger occurs when the physical channels specified with Start.DigPattern.Src match or differ from the digital pattern specified with Start.DigPattern.Pattern .
- [Start:More:Delay](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1856.html) Specifies an amount of time to wait after the Start Trigger is received before acquiring or generating the first sample. This value is in the units you specify with Start.DelayUnits .
- [Start:More:Delay Units](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr18c8.html) Specifies the units of Start.Delay .
- [Start:More:Maximum Number of Triggers to Detect](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr311c.html) Specifies the maximum number of times the task will detect a start trigger during the task. The number of times a trigger is detected and acted upon by the module may be less than the specified amount if the task stops early because of trigger/retrigger window expiration. Specifying the Maximum Number of Triggers to Detect to be 0 causes the driver to automatically set this value to the maximum possible number of triggers detectable by the device and configuration combination. Note: The number of detected triggers may be less than number of trigger events occurring, because the devices were unable to respond to the trigger.
- [Start:More:Retrigger Window](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr311b.html) Specifies the period of time in seconds after each trigger during which the device may trigger. Once the window has expired, the device stops detecting triggers, and the task will finish after the device finishes acquiring post-trigger samples that it already started. Ensure the period of time specified covers the entire time span desired for retrigger detection to avoid missed triggers. Specifying a Retrigger Window of -1 causes the window to be infinite.
- [Start:More:Retriggerable](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr190f.html) Specifies whether a finite task resets and waits for another Start Trigger after the task completes. When you set this property to TRUE, the device performs a finite acquisition or generation each time the Start Trigger occurs until the task stops. The device ignores a trigger if it is in the process of acquiring or generating signals.
- [Start:More:Trigger Window](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr311a.html) Specifies the period of time in seconds after the task starts during which the device may trigger. Once the window has expired, the device stops detecting triggers, and the task will finish after the device finishes acquiring post-trigger samples for any triggers detected. If no triggers are detected during the entire period, then no data will be returned. Ensure the period of time specified covers the entire time span desired for trigger detection to avoid missed triggers. Specifying a Trigger Window of -1 causes the window to be infinite.
- [Start:Terminal](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr2f1e.html) Indicates the name of the internal Start Trigger terminal for the task. This property does not return the name of the trigger source terminal.
- [Start:Time:Timescale](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr3036.html) Specifies the timescale to be used for timestamps used in a time trigger.
- [Start:Time:When](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr304d.html) Specifies when to trigger the start trigger.
- [Start:Timestamp:Enable](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr314a.html) Specifies whether the start trigger timestamp is enabled. If the timestamp is enabled but no resources are available, an error will be returned at run time.
- [Start:Timestamp:Timescale](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr312d.html) Specifies the start trigger timestamp timescale.
- [Start:Timestamp:Value](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr314b.html) Indicates the start trigger timestamp value.
- [Start:Trigger Type](../../../resource/objmgr/daqmx-rc/daqmx-trigger/attr1393.html) Specifies the type of trigger to use to start a task.

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1360.html language=enus -->
## TOPIC 01562: Deprecated:More:Advance:Digital Edge:Edge

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1360.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1360.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (Deprecated) Specifies on which edge of a digital signal to advance to the next entry in a scan list. Remarks The following table lists the characteristics of this property. Short Name Adv.DigEdge.Edge Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-sp

### Deprecated:More:Advance:Digital Edge:Edge

(Deprecated) Specifies on which edge of a digital signal to advance to the next entry in a scan list.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Adv.DigEdge.Edge |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Rising | 10280 | Rising edge(s). |
| --- | --- | --- |
| Falling | 10171 | Falling edge(s). |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1362.html language=enus -->
## TOPIC 01563: Deprecated:More:Advance:Digital Edge:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1362.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1362.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (Deprecated) Specifies the name of a terminal where there is a digital signal to use as the source of the Advance Trigger. Remarks The following table lists the characteristics of this property. Short Name Adv.DigEdge.Src Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable Whil

### Deprecated:More:Advance:Digital Edge:Source

(Deprecated) Specifies the name of a 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 where there is a digital signal to use as the source of the Advance Trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Adv.DigEdge.Src |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1365.html language=enus -->
## TOPIC 01564: Deprecated:More:Advance:Trigger Type

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1365.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1365.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (Deprecated) Specifies the type of trigger to use to advance to the next entry in a switch scan list. Remarks The following table lists the characteristics of this property. Short Name Adv.TrigType Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specif

### Deprecated:More:Advance:Trigger Type

(Deprecated) Specifies the 
 [type](/csh?context=nidaqmx_mxcncpts_analogtriggering)
 of trigger to use to advance to the next entry in a switch scan list.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Adv.TrigType |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Digital Edge | 10150 | Advance to the next entry in a scan list on the rising or falling edge of a digital signal. |
| --- | --- | --- |
| Software | 10292 | Advance to the next entry in a scan list when you call DAQmx Send Software Trigger . |
| None | 10230 | Advance through all entries in the scan list as fast as possible. |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1366.html language=enus -->
## TOPIC 01565: More:Pause:Trigger Type

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1366.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1366.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of trigger to use to pause a task. Remarks The following table lists the characteristics of this property. Short Name Pause.TrigType Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True Analog Le

### More:Pause:Trigger Type

Specifies the 
 [type](/csh?context=nidaqmx_mxcncpts_analogtriggering)
 of trigger to use to pause a task.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pause.TrigType |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Analog Level | 10101 | Pause the measurement or generation while an analog signal is above or below a level. |
| --- | --- | --- |
| Analog Window | 10103 | Pause the measurement or generation while an analog signal is either inside or outside of a range of values. |
| Digital Level | 10152 | Pause the measurement or generation while a digital signal is at either a high or low state. |
| Digital Pattern | 10398 | Pause the measurement or generation while digital physical channels either match or do not match a digital pattern. |
| None | 10230 | Do not pause the measurement or generation. |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1368.html language=enus -->
## TOPIC 01566: More:Pause:Analog Level:Hysteresis

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1368.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1368.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a hysteresis level in the units of the measurement or generation. If Pause.AnlgLvl.When is Above Level, the trigger does not deassert until the source signal passes below Pause.AnlgLvl.Lvl minus the hysteresis. If Pause.AnlgLvl.When is Below Level, the trigger does not deassert until the s

### More:Pause:Analog Level:Hysteresis

Specifies a 
 [hysteresis level](/csh?context=nidaqmx_mxcncpts_analogtriggering)
 in the units of the measurement or generation. If 
 [Pause.AnlgLvl.When](/csh?context=nidaqmx_daqmxprop_attr1371)
 is Above Level, the trigger does not deassert until the source signal passes below 
 [Pause.AnlgLvl.Lvl](/csh?context=nidaqmx_daqmxprop_attr1369)
 minus the hysteresis. If 
 [Pause.AnlgLvl.When](/csh?context=nidaqmx_daqmxprop_attr1371)
 is Below Level, the trigger does not deassert until the source signal passes above 
 [Pause.AnlgLvl.Lvl](/csh?context=nidaqmx_daqmxprop_attr1369)
 plus the hysteresis. Hysteresis is always enabled. Set this property to a non-zero value to use hysteresis.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pause.AnlgLvl.Hyst |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1369.html language=enus -->
## TOPIC 01567: More:Pause:Analog Level:Level

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1369.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1369.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the threshold at which to pause the task. Specify this value in the units of the measurement or generation. Use Pause.AnlgLvl.When to specify whether the task pauses above or below this threshold. Remarks The following table lists the characteristics of this property. Short Name Pause.Anlg

### More:Pause:Analog Level:Level

Specifies the threshold at which to pause the task. Specify this value in the units of the measurement or generation. Use 
 [Pause.AnlgLvl.When](/csh?context=nidaqmx_daqmxprop_attr1371)
 to specify whether the task pauses above or below this threshold.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pause.AnlgLvl.Lvl |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1370.html language=enus -->
## TOPIC 01568: More:Pause:Analog Level:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1370.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1370.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the trigger. For E Series devices, if you use a channel name, the channel must be the only channel in the task. The only terminal you can use for E Series devices is PFI0. Remarks The followin

### More:Pause:Analog Level:Source

Specifies the name of a 
 [virtual channel](/csh?context=nidaqmx_mxcncpts_chans)
 or 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 where there is an analog signal to use as the source of the trigger.

For E Series devices, if you use a channel name, the channel must be the only channel in the task. The only terminal you can use for 
E Series devices is PFI0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pause.AnlgLvl.Src |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1371.html language=enus -->
## TOPIC 01569: More:Pause:Analog Level:Pause When

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1371.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1371.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the task pauses above or below the threshold you specify with Pause.AnlgLvl.Lvl . Remarks The following table lists the characteristics of this property. Short Name Pause.AnlgLvl.When Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-sp

### More:Pause:Analog Level:Pause When

Specifies whether the task pauses above or below the threshold you specify with 
 [Pause.AnlgLvl.Lvl](/csh?context=nidaqmx_daqmxprop_attr1369)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pause.AnlgLvl.When |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Above Level | 10093 | Pause the measurement or generation while the signal is above the threshold. |
| --- | --- | --- |
| Below Level | 10107 | Pause the measurement or generation while the signal is below the threshold. |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1373.html language=enus -->
## TOPIC 01570: More:Pause:Analog Window:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1373.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1373.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the trigger. For E Series devices, if you use a channel name, the channel must be the only channel in the task. The only terminal you can use for E Series devices is PFI0. Remarks The followin

### More:Pause:Analog Window:Source

Specifies the name of a 
 [virtual channel](/csh?context=nidaqmx_mxcncpts_chans)
 or 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 where there is an analog signal to use as the source of the trigger.

For E Series devices, if you use a channel name, the channel must be the only channel in the task. The only terminal you can use for 
E Series devices is PFI0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pause.AnlgWin.Src |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1374.html language=enus -->
## TOPIC 01571: More:Pause:Analog Window:Pause When

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1374.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1374.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the task pauses while the trigger signal is inside or outside the window you specify with Pause.AnlgWin.Btm and Pause.AnlgWin.Top . Remarks The following table lists the characteristics of this property. Short Name Pause.AnlgWin.When Data type ci32.png Permissions Read/Write Resett

### More:Pause:Analog Window:Pause When

Specifies whether the task pauses while the trigger signal is inside or outside the window you specify with 
 [Pause.AnlgWin.Btm](/csh?context=nidaqmx_daqmxprop_attr1375)
 and 
 [Pause.AnlgWin.Top](/csh?context=nidaqmx_daqmxprop_attr1376)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pause.AnlgWin.When |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Inside Window | 10199 | Pause the measurement or generation while the trigger is inside the window. |
| --- | --- | --- |
| Outside Window | 10251 | Pause the measurement or generation while the signal is outside the window. |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1375.html language=enus -->
## TOPIC 01572: More:Pause:Analog Window:Bottom

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1375.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1375.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the lower limit of the window. Specify this value in the units of the measurement or generation. Remarks The following table lists the characteristics of this property. Short Name Pause.AnlgWin.Btm Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running dev

### More:Pause:Analog Window:Bottom

Specifies the lower limit of the window. Specify this value in the units of the measurement or generation.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pause.AnlgWin.Btm |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1376.html language=enus -->
## TOPIC 01573: More:Pause:Analog Window:Top

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1376.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1376.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the upper limit of the window. Specify this value in the units of the measurement or generation. Remarks The following table lists the characteristics of this property. Short Name Pause.AnlgWin.Top Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running dev

### More:Pause:Analog Window:Top

Specifies the upper limit of the window. Specify this value in the units of the measurement or generation.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pause.AnlgWin.Top |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1379.html language=enus -->
## TOPIC 01574: More:Pause:Digital Level:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1379.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1379.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of a terminal where there is a digital signal to use as the source of the Pause Trigger. Remarks The following table lists the characteristics of this property. Short Name Pause.DigLvl.Src Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Runn

### More:Pause:Digital Level:Source

Specifies the name of a 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 where there is a digital signal to use as the source of the Pause Trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pause.DigLvl.Src |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1380.html language=enus -->
## TOPIC 01575: More:Pause:Digital Level:Pause When

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1380.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1380.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the task pauses while the signal is high or low. Remarks The following table lists the characteristics of this property. Short Name Pause.DigLvl.When Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engin

### More:Pause:Digital Level:Pause When

Specifies whether the task pauses while the signal is high or low.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pause.DigLvl.When |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| High | 10192 | High state. |
| --- | --- | --- |
| Low | 10214 | Low state. |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1393.html language=enus -->
## TOPIC 01576: Start:Trigger Type

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1393.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1393.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of trigger to use to start a task. Remarks The following table lists the characteristics of this property. Short Name Start.TrigType Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True Analog Ed

### Start:Trigger Type

Specifies the 
 [type](/csh?context=nidaqmx_mxcncpts_triggertypes)
 of trigger to use to start a task.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.TrigType |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Analog Edge | 10099 | Trigger when an analog signal signal crosses a threshold. |
| --- | --- | --- |
| Analog Multi Edge | 16108 | Trigger when any of the configured analog signals cross their respective thresholds. |
| Digital Edge | 10150 | Trigger on the rising or falling edge of a digital signal. |
| Digital Pattern | 10398 | Trigger when digital physical channels match a digital pattern. |
| Analog Window | 10103 | Trigger when an analog signal enters or leaves a range of values. The range is in the units of the measurement. |
| Time | 15996 | Trigger when a specified time is reached. |
| None | 10230 | Disable triggering for the task. |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1395.html language=enus -->
## TOPIC 01577: Start:Analog Edge:Hysteresis

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1395.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1395.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a hysteresis level in the units of the measurement or generation. If Start.AnlgEdge.Slope is Rising, the trigger does not deassert until the source signal passes below Start.AnlgEdge.Lvl minus the hysteresis. If Start.AnlgEdge.Slope is Falling, the trigger does not deassert until the sourc

### Start:Analog Edge:Hysteresis

Specifies a 
 [hysteresis level](/csh?context=nidaqmx_mxcncpts_analogtriggering)
 in the units of the measurement or generation. If 
 [Start.AnlgEdge.Slope](/csh?context=nidaqmx_daqmxprop_attr1397)
 is Rising, the trigger does not deassert until the source signal passes below 
 [Start.AnlgEdge.Lvl](/csh?context=nidaqmx_daqmxprop_attr1396)
 minus the hysteresis. If 
 [Start.AnlgEdge.Slope](/csh?context=nidaqmx_daqmxprop_attr1397)
 is Falling, the trigger does not deassert until the source signal passes above 
 [Start.AnlgEdge.Lvl](/csh?context=nidaqmx_daqmxprop_attr1396)
 plus the hysteresis. Hysteresis is always enabled. Set this property to a non-zero value to use hysteresis.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.AnlgEdge.Hyst |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1396.html language=enus -->
## TOPIC 01578: Start:Analog Edge:Level

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1396.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1396.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies at what threshold in the units of the measurement or generation to start acquiring or generating samples. Use Start.AnlgEdge.Slope to specify on which slope to trigger on this threshold. Remarks The following table lists the characteristics of this property. Short Name Start.AnlgEdge.Lvl D

### Start:Analog Edge:Level

Specifies at what threshold in the units of the measurement or generation to start acquiring or generating samples. Use 
 [Start.AnlgEdge.Slope](/csh?context=nidaqmx_daqmxprop_attr1397)
 to specify on which slope to trigger on this threshold.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.AnlgEdge.Lvl |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1397.html language=enus -->
## TOPIC 01579: Start:Analog Edge:Slope

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1397.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1397.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which slope of the trigger signal to start acquiring or generating samples. Remarks The following table lists the characteristics of this property. Short Name Start.AnlgEdge.Slope Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Av

### Start:Analog Edge:Slope

Specifies on which slope of the trigger signal to start acquiring or generating samples.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.AnlgEdge.Slope |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Rising | 10280 | Trigger on the rising slope of the signal. |
| --- | --- | --- |
| Falling | 10171 | Trigger on the falling slope of the signal. |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1398.html language=enus -->
## TOPIC 01580: Start:Analog Edge:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1398.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1398.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the Start Trigger. For E Series devices, if you use a channel name, the channel must be the first one in the task. The only terminal you can use for E Series devices is PFI0. Remarks The follo

### Start:Analog Edge:Source

Specifies the name of a 
 [virtual channel](/csh?context=nidaqmx_mxcncpts_chans)
 or 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 where there is an analog signal to use as the 
 [source](/csh?context=nidaqmx_mxdevconsid_analogtrig)
 of the Start Trigger.

For E Series devices, if you use a channel name, the channel must be the first one in the task. The only terminal you can use for 
E Series devices is PFI0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.AnlgEdge.Src |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1400.html language=enus -->
## TOPIC 01581: Start:Analog Window:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1400.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1400.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the Start Trigger. For E Series devices, if you use a channel name, the channel must be the first one in the task. The only terminal you can use for E Series devices is PFI0. Remarks The follo

### Start:Analog Window:Source

Specifies the name of a 
 [virtual channel](/csh?context=nidaqmx_mxcncpts_chans)
 or 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 where there is an analog signal to use as the source of the Start Trigger.

For E Series devices, if you use a channel name, the channel must be the first one in the task. The only terminal you can use for 
E Series devices is PFI0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.AnlgWin.Src |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1401.html language=enus -->
## TOPIC 01582: Start:Analog Window:Trigger When

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1401.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1401.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the task starts acquiring or generating samples when the signal enters or leaves the window you specify with Start.AnlgWin.Btm and Start.AnlgWin.Top . Remarks The following table lists the characteristics of this property. Short Name Start.AnlgWin.TrigWhen Data type ci32.png Permis

### Start:Analog Window:Trigger When

Specifies whether the task starts acquiring or generating samples when the signal enters or leaves the window you specify with 
 [Start.AnlgWin.Btm](/csh?context=nidaqmx_daqmxprop_attr1402)
 and 
 [Start.AnlgWin.Top](/csh?context=nidaqmx_daqmxprop_attr1403)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.AnlgWin.TrigWhen |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Entering Window | 10163 | Trigger when the signal enters the window. |
| --- | --- | --- |
| Leaving Window | 10208 | Trigger when the signal leaves the window. |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1402.html language=enus -->
## TOPIC 01583: Start:Analog Window:Bottom

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1402.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1402.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the lower limit of the window . Specify this value in the units of the measurement or generation. Remarks The following table lists the characteristics of this property. Short Name Start.AnlgWin.Btm Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running de

### Start:Analog Window:Bottom

Specifies the lower limit of the 
 [window](/csh?context=nidaqmx_mxcncpts_algwindowtrig)
 . Specify this value in the units of the measurement or generation.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.AnlgWin.Btm |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1403.html language=enus -->
## TOPIC 01584: Start:Analog Window:Top

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1403.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1403.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the upper limit of the window . Specify this value in the units of the measurement or generation. Remarks The following table lists the characteristics of this property. Short Name Start.AnlgWin.Top Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running de

### Start:Analog Window:Top

Specifies the upper limit of the 
 [window](/csh?context=nidaqmx_mxcncpts_algwindowtrig)
 . Specify this value in the units of the measurement or generation.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.AnlgWin.Top |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1404.html language=enus -->
## TOPIC 01585: Start:Digital Edge:Edge

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1404.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1404.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge of a digital pulse to start acquiring or generating samples. Remarks The following table lists the characteristics of this property. Short Name Start.DigEdge.Edge Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Availabl

### Start:Digital Edge:Edge

Specifies on which edge of a digital pulse to start acquiring or generating samples.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.DigEdge.Edge |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Rising | 10280 | Rising edge(s). |
| --- | --- | --- |
| Falling | 10171 | Falling edge(s). |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1407.html language=enus -->
## TOPIC 01586: Start:Digital Edge:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1407.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1407.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of a terminal where there is a digital signal to use as the source of the Start Trigger. Remarks The following table lists the characteristics of this property. Short Name Start.DigEdge.Src Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Run

### Start:Digital Edge:Source

Specifies the name of a 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 where there is a digital signal to use as the source of the Start Trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.DigEdge.Src |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1410.html language=enus -->
## TOPIC 01587: Start:Digital Pattern:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1410.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1410.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the physical channels to use for pattern matching. The order of the physical channels determines the order of the pattern. If a port is included, the order of the physical channels within the port is in ascending order. Remarks The following table lists the characteristics of this property

### Start:Digital Pattern:Source

Specifies the 
 [physical channels](/csh?context=nidaqmx_mxcncpts_chans)
 to use for pattern matching. The order of the physical channels determines the order of the pattern. If a 
 [port](/csh?context=nidaqmx_mxcncpts_linesports)
 is included, the order of the physical channels within the port is in ascending order.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.DigPattern.Src |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1411.html language=enus -->
## TOPIC 01588: Start:Digital Pattern:Trigger When

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1411.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1411.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the Start Trigger occurs when the physical channels specified with Start.DigPattern.Src match or differ from the digital pattern specified with Start.DigPattern.Pattern . Remarks The following table lists the characteristics of this property. Short Name Start.DigPattern.TrigWhen Da

### Start:Digital Pattern:Trigger When

Specifies whether the Start Trigger occurs when the 
 [physical channels](/csh?context=nidaqmx_mxcncpts_chans)
 specified with 
 [Start.DigPattern.Src](/csh?context=nidaqmx_daqmxprop_attr1410)
 match or differ from the 
 [digital pattern](/csh?context=nidaqmx_mxcncpts_digpattern)
 specified with 
 [Start.DigPattern.Pattern](/csh?context=nidaqmx_daqmxprop_attr2186)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.DigPattern.TrigWhen |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Pattern Matches | 10254 | Trigger when the physical channels match the specified pattern. |
| --- | --- | --- |
| Pattern Does Not Match | 10253 | Trigger when the physical channels do not match the specified pattern. |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1414.html language=enus -->
## TOPIC 01589: More:Arm Start:Trigger Type

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1414.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1414.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of trigger to use to arm the task for a Start Trigger. If you configure an Arm Start Trigger, the task does not respond to a Start Trigger until the device receives the Arm Start Trigger. Remarks The following table lists the characteristics of this property. Short Name ArmStart.T

### More:Arm Start:Trigger Type

Specifies the type of trigger to use to arm the task for a Start Trigger. If you configure an Arm Start Trigger, the task does not respond to a Start Trigger until the device receives the Arm Start Trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ArmStart.TrigType |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Digital Edge | 10150 | Trigger on a rising or falling edge of a digital signal. |
| --- | --- | --- |
| Time | 15996 | Trigger when a specified time is reached. |
| None | 10230 | Disable the trigger. |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1415.html language=enus -->
## TOPIC 01590: More:Arm Start:Digital Edge:Edge

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1415.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1415.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge of a digital signal to arm the task for a Start Trigger. Remarks The following table lists the characteristics of this property. Short Name ArmStart.DigEdge.Edge Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available

### More:Arm Start:Digital Edge:Edge

Specifies on which edge of a digital signal to arm the task for a Start Trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ArmStart.DigEdge.Edge |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Rising | 10280 | Rising edge(s). |
| --- | --- | --- |
| Falling | 10171 | Falling edge(s). |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1417.html language=enus -->
## TOPIC 01591: More:Arm Start:Digital Edge:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1417.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1417.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of a terminal where there is a digital signal to use as the source of the Arm Start Trigger. Remarks The following table lists the characteristics of this property. Short Name ArmStart.DigEdge.Src Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task

### More:Arm Start:Digital Edge:Source

Specifies the name of a 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 where there is a digital signal to use as the source of the Arm Start Trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ArmStart.DigEdge.Src |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1419.html language=enus -->
## TOPIC 01592: Reference:Trigger Type

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1419.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1419.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of trigger to use to mark a reference point for the measurement. Remarks The following table lists the characteristics of this property. Short Name Ref.TrigType Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Ru

### Reference:Trigger Type

Specifies the 
 [type](/csh?context=nidaqmx_mxcncpts_triggertypes)
 of trigger to use to mark a 
 [reference](/csh?context=nidaqmx_mxcncpts_referencetrigger)
 point for the measurement.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.TrigType |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Analog Edge | 10099 | Trigger when an analog signal signal crosses a threshold. |
| --- | --- | --- |
| Analog Multi Edge | 16108 | Trigger when any of the configured analog signals cross their respective thresholds. |
| Digital Edge | 10150 | Trigger on the rising or falling edge of a digital signal. |
| Digital Pattern | 10398 | Trigger when digital physical channels match a digital pattern. |
| Analog Window | 10103 | Trigger when an analog signal enters or leaves a range of values. The range is in the units of the measurement. |
| Time | 15996 | Trigger when a specified time is reached. |
| None | 10230 | Disable triggering for the task. |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1421.html language=enus -->
## TOPIC 01593: Reference:Analog Edge:Hysteresis

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1421.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1421.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a hysteresis level in the units of the measurement. If Ref.AnlgEdge.Slope is Rising, the trigger does not deassert until the source signal passes below Ref.AnlgEdge.Lvl minus the hysteresis. If Ref.AnlgEdge.Slope is Falling, the trigger does not deassert until the source signal passes abov

### Reference:Analog Edge:Hysteresis

Specifies a 
 [hysteresis level](/csh?context=nidaqmx_mxcncpts_analogtriggering)
 in the units of the measurement. If 
 [Ref.AnlgEdge.Slope](/csh?context=nidaqmx_daqmxprop_attr1423)
 is Rising, the trigger does not deassert until the source signal passes below 
 [Ref.AnlgEdge.Lvl](/csh?context=nidaqmx_daqmxprop_attr1422)
 minus the hysteresis. If 
 [Ref.AnlgEdge.Slope](/csh?context=nidaqmx_daqmxprop_attr1423)
 is Falling, the trigger does not deassert until the source signal passes above 
 [Ref.AnlgEdge.Lvl](/csh?context=nidaqmx_daqmxprop_attr1422)
 plus the hysteresis. Hysteresis is always enabled. Set this property to a non-zero value to use hysteresis.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.AnlgEdge.Hyst |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1422.html language=enus -->
## TOPIC 01594: Reference:Analog Edge:Level

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1422.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1422.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in the units of the measurement the threshold at which the Reference Trigger occurs. Use Ref.AnlgEdge.Slope to specify on which slope to trigger at this threshold. Remarks The following table lists the characteristics of this property. Short Name Ref.AnlgEdge.Lvl Data type cdbl.png Permiss

### Reference:Analog Edge:Level

Specifies in the units of the measurement the threshold at which the 
 [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger)
 occurs. Use 
 [Ref.AnlgEdge.Slope](/csh?context=nidaqmx_daqmxprop_attr1423)
 to specify on which slope to trigger at this threshold.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.AnlgEdge.Lvl |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1423.html language=enus -->
## TOPIC 01595: Reference:Analog Edge:Slope

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1423.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1423.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which slope of the source signal the Reference Trigger occurs. Remarks The following table lists the characteristics of this property. Short Name Ref.AnlgEdge.Slope Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-

### Reference:Analog Edge:Slope

Specifies on which slope of the source signal the 
 [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger)
 occurs.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.AnlgEdge.Slope |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Rising | 10280 | Trigger on the rising slope of the signal. |
| --- | --- | --- |
| Falling | 10171 | Trigger on the falling slope of the signal. |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1424.html language=enus -->
## TOPIC 01596: Reference:Analog Edge:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1424.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1424.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the Reference Trigger . For E Series devices, if you use a channel name, the channel must be the only channel in the task. The only terminal you can use for E Series devices is PFI0. Remarks T

### Reference:Analog Edge:Source

Specifies the name of a 
 [virtual channel](/csh?context=nidaqmx_mxcncpts_chans)
 or 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 where there is an analog signal to use as the source of the 
 [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger)
 .

For E Series devices, if you use a channel name, the channel must be the only channel in the task. The only terminal you can use for 
E Series devices is PFI0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.AnlgEdge.Src |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1426.html language=enus -->
## TOPIC 01597: Reference:Analog Window:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1426.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1426.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the Reference Trigger . For E Series devices, if you use a channel name, the channel must be the only channel in the task. The only terminal you can use for E Series devices is PFI0. Remarks T

### Reference:Analog Window:Source

Specifies the name of a 
 [virtual channel](/csh?context=nidaqmx_mxcncpts_chans)
 or 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 where there is an analog signal to use as the source of the 
 [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger)
 .

For E Series devices, if you use a channel name, the channel must be the only channel in the task. The only terminal you can use for 
E Series devices is PFI0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.AnlgWin.Src |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1427.html language=enus -->
## TOPIC 01598: Reference:Analog Window:Trigger When

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1427.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1427.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the Reference Trigger occurs when the source signal enters the window or when it leaves the window. Use Ref.AnlgWin.Btm and Ref.AnlgWin.Top to specify the window. Remarks The following table lists the characteristics of this property. Short Name Ref.AnlgWin.TrigWhen Data type ci32.

### Reference:Analog Window:Trigger When

Specifies whether the 
 [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger)
 occurs when the source signal enters the window or when it leaves the window. Use 
 [Ref.AnlgWin.Btm](/csh?context=nidaqmx_daqmxprop_attr1428)
 and 
 [Ref.AnlgWin.Top](/csh?context=nidaqmx_daqmxprop_attr1429)
 to specify the window.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.AnlgWin.TrigWhen |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Entering Window | 10163 | Trigger when the signal enters the window. |
| --- | --- | --- |
| Leaving Window | 10208 | Trigger when the signal leaves the window. |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1428.html language=enus -->
## TOPIC 01599: Reference:Analog Window:Bottom

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1428.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1428.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the lower limit of the window . Specify this value in the units of the measurement. Remarks The following table lists the characteristics of this property. Short Name Ref.AnlgWin.Btm Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Av

### Reference:Analog Window:Bottom

Specifies the lower limit of the 
 [window](/csh?context=nidaqmx_mxcncpts_algwindowtrig)
 . Specify this value in the units of the measurement.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.AnlgWin.Btm |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1429.html language=enus -->
## TOPIC 01600: Reference:Analog Window:Top

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1429.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1429.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the upper limit of the window . Specify this value in the units of the measurement. Remarks The following table lists the characteristics of this property. Short Name Ref.AnlgWin.Top Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Av

### Reference:Analog Window:Top

Specifies the upper limit of the 
 [window](/csh?context=nidaqmx_mxcncpts_algwindowtrig)
 . Specify this value in the units of the measurement.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.AnlgWin.Top |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1430.html language=enus -->
## TOPIC 01601: Reference:Digital Edge:Edge

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1430.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1430.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on what edge of a digital pulse the Reference Trigger occurs. Remarks The following table lists the characteristics of this property. Short Name Ref.DigEdge.Edge Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time E

### Reference:Digital Edge:Edge

Specifies on what edge of a digital pulse the 
 [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger)
 occurs.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.DigEdge.Edge |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Rising | 10280 | Rising edge(s). |
| --- | --- | --- |
| Falling | 10171 | Falling edge(s). |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1434.html language=enus -->
## TOPIC 01602: Reference:Digital Edge:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1434.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1434.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of a terminal where there is a digital signal to use as the source of the Reference Trigger . Remarks The following table lists the characteristics of this property. Short Name Ref.DigEdge.Src Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is

### Reference:Digital Edge:Source

Specifies the name of a 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 where there is a digital signal to use as the source of the 
 [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.DigEdge.Src |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1437.html language=enus -->
## TOPIC 01603: Reference:Digital Pattern:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1437.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1437.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the physical channels to use for pattern matching. The order of the physical channels determines the order of the pattern. If a port is included, the order of the physical channels within the port is in ascending order. Remarks The following table lists the characteristics of this property

### Reference:Digital Pattern:Source

Specifies the 
 [physical channels](/csh?context=nidaqmx_mxcncpts_chans)
 to use for pattern matching. The order of the physical channels determines the order of the pattern. If a 
 [port](/csh?context=nidaqmx_mxcncpts_linesports)
 is included, the order of the physical channels within the port is in ascending order.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.DigPattern.Src |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1438.html language=enus -->
## TOPIC 01604: Reference:Digital Pattern:Trigger When

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1438.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1438.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the Reference Trigger occurs when the physical channels specified with Ref.DigPattern.Src match or differ from the digital pattern specified with Ref.DigPattern.Pattern . Remarks The following table lists the characteristics of this property. Short Name Ref.DigPattern.TrigWhen Data

### Reference:Digital Pattern:Trigger When

Specifies whether the 
 [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger)
 occurs when the 
 [physical channels](/csh?context=nidaqmx_mxcncpts_chans)
 specified with 
 [Ref.DigPattern.Src](/csh?context=nidaqmx_daqmxprop_attr1437)
 match or differ from the 
 [digital pattern](/csh?context=nidaqmx_mxcncpts_digpattern)
 specified with 
 [Ref.DigPattern.Pattern](/csh?context=nidaqmx_daqmxprop_attr2187)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.DigPattern.TrigWhen |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Pattern Matches | 10254 | Trigger when the physical channels match the specified pattern. |
| --- | --- | --- |
| Pattern Does Not Match | 10253 | Trigger when the physical channels do not match the specified pattern. |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1445.html language=enus -->
## TOPIC 01605: Reference:Pretrigger Samples per Channel

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1445.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1445.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the minimum number of pretrigger samples to acquire from each channel before recognizing the reference trigger . Post-trigger samples per channel are equal to SampQuant.SampPerChan minus the number of pretrigger samples per channel. Remarks The following table lists the characteristics of

### Reference:Pretrigger Samples per Channel

Specifies the minimum number of pretrigger samples to acquire from each channel before recognizing the 
 [reference trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger)
 . Post-trigger samples per channel are equal to 
 [SampQuant.SampPerChan](/csh?context=nidaqmx_daqmxprop_attr1310)
 minus the number of pretrigger samples per channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.PretrigSamples |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1483.html language=enus -->
## TOPIC 01606: Reference:More:Delay

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1483.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1483.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the time to wait after the device receives the Reference Trigger before switching from pretrigger to posttrigger samples. Remarks The following table lists the characteristics of this property. Short Name Ref.Delay Data type cdbl.png Permissions Read/Write Resettable True Settab

### Reference:More:Delay

Specifies in seconds the time to wait after the device receives the Reference Trigger before switching from pretrigger to posttrigger samples.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.Delay |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1856.html language=enus -->
## TOPIC 01607: Start:More:Delay

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1856.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1856.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an amount of time to wait after the Start Trigger is received before acquiring or generating the first sample. This value is in the units you specify with Start.DelayUnits . Remarks The following table lists the characteristics of this property. Short Name Start.Delay Data type cdbl.png Pe

### Start:More:Delay

Specifies an amount of time to wait after the Start Trigger is received before acquiring or generating the first sample. This value is in the units you specify with 
 [Start.DelayUnits](/csh?context=nidaqmx_daqmxprop_attr18c8)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.Delay |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr1857.html language=enus -->
## TOPIC 01608: Reference:Analog Window:Coupling

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr1857.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr1857.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel . Remarks The following table lists the characteristics of this property. Short Name Ref.AnlgWin.Coupling Data type ci32.png Permissions Read/Write Resettable True Settable While Tas

### Reference:Analog Window:Coupling

Specifies the coupling for the source signal of the trigger if the source is a 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 rather than a 
 [virtual channel](/csh?context=nidaqmx_mxcncpts_chans)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.AnlgWin.Coupling |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| AC | 10045 | Alternating Current. |
| --- | --- | --- |
| DC | 10050 | Direct Current. |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr18c8.html language=enus -->
## TOPIC 01609: Start:More:Delay Units

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr18c8.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr18c8.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of Start.Delay . Remarks The following table lists the characteristics of this property. Short Name Start.DelayUnits Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True Sample Clock Periods 102

### Start:More:Delay Units

Specifies the units of 
 [Start.Delay](/csh?context=nidaqmx_daqmxprop_attr1856)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.DelayUnits |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Sample Clock Periods | 10286 | Complete periods of the Sample Clock. |
| --- | --- | --- |
| Seconds | 10364 | Seconds. |
| Ticks | 10304 | Timebase ticks. |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr190f.html language=enus -->
## TOPIC 01610: Start:More:Retriggerable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr190f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr190f.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether a finite task resets and waits for another Start Trigger after the task completes. When you set this property to TRUE, the device performs a finite acquisition or generation each time the Start Trigger occurs until the task stops. The device ignores a trigger if it is in the proces

### Start:More:Retriggerable

Specifies whether a finite task resets and waits for another Start Trigger after the task completes. When you set this property to TRUE, the device performs a finite acquisition or generation each time the Start Trigger occurs until the task stops. The device ignores a trigger if it is in the process of acquiring or generating signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.Retriggerable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr216f.html language=enus -->
## TOPIC 01611: More:Pause:Digital Pattern:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr216f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr216f.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the physical channels to use for pattern matching. The order of the physical channels determines the order of the pattern. If a port is included, the lines within the port are in ascending order. Remarks The following table lists the characteristics of this property. Short Name Pause.DigPa

### More:Pause:Digital Pattern:Source

Specifies the physical channels to use for pattern matching. The order of the physical channels determines the order of the pattern. If a port is included, the lines within the port are in ascending order.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pause.DigPattern.Src |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2170.html language=enus -->
## TOPIC 01612: More:Pause:Digital Pattern:Pause When

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2170.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2170.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies if the Pause Trigger occurs when the physical channels specified with Pause.DigPattern.Src match or differ from the digital pattern specified with Pause.DigPattern.Pattern . Remarks The following table lists the characteristics of this property. Short Name Pause.DigPattern.When Data type c

### More:Pause:Digital Pattern:Pause When

Specifies if the Pause Trigger occurs when the physical channels specified with 
 [Pause.DigPattern.Src](/csh?context=nidaqmx_daqmxprop_attr216f)
 match or differ from the digital pattern specified with 
 [Pause.DigPattern.Pattern](/csh?context=nidaqmx_daqmxprop_attr2188)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pause.DigPattern.When |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Pattern Matches | 10254 | Trigger when the physical channels match the specified pattern. |
| --- | --- | --- |
| Pattern Does Not Match | 10253 | Trigger when the physical channels do not match the specified pattern. |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2186.html language=enus -->
## TOPIC 01613: Start:Digital Pattern:Pattern

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2186.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2186.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the digital pattern that must be met for the Start Trigger to occur. Remarks The following table lists the characteristics of this property. Short Name Start.DigPattern.Pattern Data type cstr.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Availabl

### Start:Digital Pattern:Pattern

Specifies the 
 [digital pattern](/csh?context=nidaqmx_mxcncpts_digpattern)
 that must be met for the Start Trigger to occur.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.DigPattern.Pattern |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2187.html language=enus -->
## TOPIC 01614: Reference:Digital Pattern:Pattern

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2187.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2187.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the digital pattern that must be met for the Reference Trigger to occur. Remarks The following table lists the characteristics of this property. Short Name Ref.DigPattern.Pattern Data type cstr.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Availa

### Reference:Digital Pattern:Pattern

Specifies the 
 [digital pattern](/csh?context=nidaqmx_mxcncpts_digpattern)
 that must be met for the 
 [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger)
 to occur.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.DigPattern.Pattern |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2188.html language=enus -->
## TOPIC 01615: More:Pause:Digital Pattern:Pattern

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2188.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2188.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the digital pattern that must be met for the Pause Trigger to occur. Remarks The following table lists the characteristics of this property. Short Name Pause.DigPattern.Pattern Data type cstr.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Availabl

### More:Pause:Digital Pattern:Pattern

Specifies the 
 [digital pattern](/csh?context=nidaqmx_mxcncpts_digpattern)
 that must be met for the Pause Trigger to occur.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pause.DigPattern.Pattern |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2223.html language=enus -->
## TOPIC 01616: Start:Digital Edge:Digital Filter:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2223.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2223.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply a digital filter to the trigger signal. Remarks The following table lists the characteristics of this property. Short Name Start.DigEdge.DigFltr.Enable Data type cbool.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Ru

### Start:Digital Edge:Digital Filter:Enable

Specifies whether to apply a digital 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 to the trigger signal.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.DigEdge.DigFltr.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2224.html language=enus -->
## TOPIC 01617: Start:Digital Edge:Digital Filter:Minimum Pulse Width

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2224.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2224.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. Remarks The following table lists the characteristics of this property. Short Name Start.DigEdge.DigFltr.MinPulseWidth Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Availabl

### Start:Digital Edge:Digital Filter:Minimum Pulse Width

Specifies in seconds the minimum pulse width the 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 recognizes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.DigEdge.DigFltr.MinPulseWidth |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2225.html language=enus -->
## TOPIC 01618: Start:Digital Edge:Digital Filter:Timebase:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2225.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2225.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to use as the timebase of the pulse width filter. Remarks The following table lists the characteristics of this property. Short Name Start.DigEdge.DigFltr.TimebaseSrc Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Ru

### Start:Digital Edge:Digital Filter:Timebase:Source

Specifies the input 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 of the signal to use as the timebase of the pulse width filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.DigEdge.DigFltr.TimebaseSrc |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2226.html language=enus -->
## TOPIC 01619: Start:Digital Edge:Digital Filter:Timebase:Rate

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2226.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2226.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. Remarks The following table lists the characteristics of this property. Short Name Start.DigEdge.DigFltr.TimebaseRate Data type cdbl.png Permissions Read/Write Resettable True

### Start:Digital Edge:Digital Filter:Timebase:Rate

Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.DigEdge.DigFltr.TimebaseRate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2227.html language=enus -->
## TOPIC 01620: Start:Digital Edge:Digital Synchronization:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2227.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2227.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. If you set this property to TRUE, the device does not recognize and act upon the trigger until the next pulse of the internal timebase. This property does not affect the minimum pulse wi

### Start:Digital Edge:Digital Synchronization:Enable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. If you set this property to TRUE, the device does not recognize and act upon the trigger until the next pulse of the internal timebase.

This property does not affect the minimum pulse width recognized by the device, 
but setting this property to TRUE does limit the speed at which the device recognizes transitions 
to less than the frequency of the internal timebase.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.DigEdge.DigSync.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2228.html language=enus -->
## TOPIC 01621: More:Pause:Digital Level:Digital Filter:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2228.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2228.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply a digital filter to the trigger signal. Remarks The following table lists the characteristics of this property. Short Name Pause.DigLvl.DigFltr.Enable Data type cbool.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run

### More:Pause:Digital Level:Digital Filter:Enable

Specifies whether to apply a digital 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 to the trigger signal.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pause.DigLvl.DigFltr.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2229.html language=enus -->
## TOPIC 01622: More:Pause:Digital Level:Digital Filter:Minimum Pulse Width

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2229.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2229.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. Remarks The following table lists the characteristics of this property. Short Name Pause.DigLvl.DigFltr.MinPulseWidth Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available

### More:Pause:Digital Level:Digital Filter:Minimum Pulse Width

Specifies in seconds the minimum pulse width the 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 recognizes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pause.DigLvl.DigFltr.MinPulseWidth |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr222a.html language=enus -->
## TOPIC 01623: More:Pause:Digital Level:Digital Filter:Timebase:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr222a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr222a.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to use as the timebase of the pulse width filter. Remarks The following table lists the characteristics of this property. Short Name Pause.DigLvl.DigFltr.TimebaseSrc Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Run

### More:Pause:Digital Level:Digital Filter:Timebase:Source

Specifies the input 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 of the signal to use as the timebase of the pulse width filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pause.DigLvl.DigFltr.TimebaseSrc |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr222b.html language=enus -->
## TOPIC 01624: More:Pause:Digital Level:Digital Filter:Timebase:Rate

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr222b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr222b.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. Remarks The following table lists the characteristics of this property. Short Name Pause.DigLvl.DigFltr.TimebaseRate Data type cdbl.png Permissions Read/Write Resettable True

### More:Pause:Digital Level:Digital Filter:Timebase:Rate

Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pause.DigLvl.DigFltr.TimebaseRate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr222c.html language=enus -->
## TOPIC 01625: More:Pause:Digital Level:Digital Synchronization:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr222c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr222c.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. This property does not affect the minimum pulse width recognized by the device, but setting this property to TRUE does limit the speed at which the device recognizes transitions to less

### More:Pause:Digital Level:Digital Synchronization:Enable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

This property does not affect the minimum pulse width recognized by the device, 
but setting this property to TRUE does limit the speed at which the device recognizes transitions 
to less than the frequency of the internal timebase.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pause.DigLvl.DigSync.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr222d.html language=enus -->
## TOPIC 01626: More:Arm Start:Digital Edge:Digital Filter:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr222d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr222d.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply the pulse width filter to the signal. Remarks The following table lists the characteristics of this property. Short Name ArmStart.DigEdge.DigFltr.Enable Data type cbool.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in R

### More:Arm Start:Digital Edge:Digital Filter:Enable

Specifies whether to apply the pulse width 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 to the signal.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ArmStart.DigEdge.DigFltr.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr222e.html language=enus -->
## TOPIC 01627: More:Arm Start:Digital Edge:Digital Filter:Minimum Pulse Width

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr222e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr222e.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. Remarks The following table lists the characteristics of this property. Short Name ArmStart.DigEdge.DigFltr.MinPulseWidth Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Avail

### More:Arm Start:Digital Edge:Digital Filter:Minimum Pulse Width

Specifies in seconds the minimum pulse width the 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 recognizes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ArmStart.DigEdge.DigFltr.MinPulseWidth |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr222f.html language=enus -->
## TOPIC 01628: More:Arm Start:Digital Edge:Digital Filter:Timebase:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr222f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr222f.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to use as the timebase of the pulse width filter. Remarks The following table lists the characteristics of this property. Short Name ArmStart.DigEdge.DigFltr.TimebaseSrc Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is

### More:Arm Start:Digital Edge:Digital Filter:Timebase:Source

Specifies the input 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 of the signal to use as the timebase of the pulse width filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ArmStart.DigEdge.DigFltr.TimebaseSrc |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2230.html language=enus -->
## TOPIC 01629: More:Arm Start:Digital Edge:Digital Filter:Timebase:Rate

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2230.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2230.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. Remarks The following table lists the characteristics of this property. Short Name ArmStart.DigEdge.DigFltr.TimebaseRate Data type cdbl.png Permissions Read/Write Resettable T

### More:Arm Start:Digital Edge:Digital Filter:Timebase:Rate

Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ArmStart.DigEdge.DigFltr.TimebaseRate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2231.html language=enus -->
## TOPIC 01630: More:Arm Start:Digital Edge:Digital Synchronization:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2231.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2231.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. This property does not affect the minimum pulse width recognized by the device, but setting this property to TRUE does limit the speed at which the device recognizes transitions to less

### More:Arm Start:Digital Edge:Digital Synchronization:Enable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

This property does not affect the minimum pulse width recognized by the device, 
but setting this property to TRUE does limit the speed at which the device recognizes transitions 
to less than the frequency of the internal timebase.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ArmStart.DigEdge.DigSync.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2233.html language=enus -->
## TOPIC 01631: Start:Analog Edge:Coupling

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2233.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2233.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel . Remarks The following table lists the characteristics of this property. Short Name Start.AnlgEdge.Coupling Data type ci32.png Permissions Read/Write Resettable True Settable While

### Start:Analog Edge:Coupling

Specifies the coupling for the source signal of the trigger if the source is a 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 rather than a 
 [virtual channel](/csh?context=nidaqmx_mxcncpts_chans)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.AnlgEdge.Coupling |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| AC | 10045 | Alternating Current. |
| --- | --- | --- |
| DC | 10050 | Direct Current. |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2234.html language=enus -->
## TOPIC 01632: Start:Analog Window:Coupling

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2234.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2234.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel . Remarks The following table lists the characteristics of this property. Short Name Start.AnlgWin.Coupling Data type ci32.png Permissions Read/Write Resettable True Settable While T

### Start:Analog Window:Coupling

Specifies the coupling for the source signal of the trigger if the source is a 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 rather than a 
 [virtual channel](/csh?context=nidaqmx_mxcncpts_chans)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.AnlgWin.Coupling |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| AC | 10045 | Alternating Current. |
| --- | --- | --- |
| DC | 10050 | Direct Current. |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2235.html language=enus -->
## TOPIC 01633: Reference:Analog Edge:Coupling

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2235.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2235.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel . Remarks The following table lists the characteristics of this property. Short Name Ref.AnlgEdge.Coupling Data type ci32.png Permissions Read/Write Resettable True Settable While Ta

### Reference:Analog Edge:Coupling

Specifies the coupling for the source signal of the trigger if the source is a 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 rather than a 
 [virtual channel](/csh?context=nidaqmx_mxcncpts_chans)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.AnlgEdge.Coupling |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| AC | 10045 | Alternating Current. |
| --- | --- | --- |
| DC | 10050 | Direct Current. |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2236.html language=enus -->
## TOPIC 01634: More:Pause:Analog Level:Coupling

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2236.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2236.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel . Remarks The following table lists the characteristics of this property. Short Name Pause.AnlgLvl.Coupling Data type ci32.png Permissions Read/Write Resettable True Settable While T

### More:Pause:Analog Level:Coupling

Specifies the coupling for the source signal of the trigger if the source is a 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 rather than a 
 [virtual channel](/csh?context=nidaqmx_mxcncpts_chans)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pause.AnlgLvl.Coupling |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| AC | 10045 | Alternating Current. |
| --- | --- | --- |
| DC | 10050 | Direct Current. |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2237.html language=enus -->
## TOPIC 01635: More:Pause:Analog Window:Coupling

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2237.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2237.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the coupling for the source signal of the terminal if the source is a terminal rather than a virtual channel . Remarks The following table lists the characteristics of this property. Short Name Pause.AnlgWin.Coupling Data type ci32.png Permissions Read/Write Resettable True Settable While

### More:Pause:Analog Window:Coupling

Specifies the coupling for the source signal of the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 if the source is a terminal rather than a 
 [virtual channel](/csh?context=nidaqmx_mxcncpts_chans)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pause.AnlgWin.Coupling |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| AC | 10045 | Alternating Current. |
| --- | --- | --- |
| DC | 10050 | Direct Current. |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2238.html language=enus -->
## TOPIC 01636: Deprecated:More:Advance:Digital Edge:Digital Filter:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2238.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2238.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (Deprecated) Specifies whether to apply the pulse width filter to the signal. Remarks The following table lists the characteristics of this property. Short Name Adv.DigEdge.DigFltr.Enable Data type cbool.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Availa

### Deprecated:More:Advance:Digital Edge:Digital Filter:Enable

(Deprecated) Specifies whether to apply the pulse width filter to the signal.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Adv.DigEdge.DigFltr.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr22b7.html language=enus -->
## TOPIC 01637: More:Handshake:Trigger Type

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr22b7.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr22b7.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of Handshake Trigger to use. Remarks The following table lists the characteristics of this property. Short Name Hshk.TrigType Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True Interlocked 1254

### More:Handshake:Trigger Type

Specifies the type of 
 [Handshake Trigger](/csh?context=nidaqmx_mxcncpts_handtrig)
 to use.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Hshk.TrigType |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Interlocked | 12549 | Use the Handshake Trigger as a control signal for asynchronous handshaking, such as 8255 handshaking. |
| --- | --- | --- |
| None | 10230 | Start the measurement or generation immediately when you start the task. |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr22b8.html language=enus -->
## TOPIC 01638: More:Handshake:Interlocked:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr22b8.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr22b8.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source terminal of the Handshake Trigger . Remarks The following table lists the characteristics of this property. Short Name Hshk.Interlocked.Src Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engin

### More:Handshake:Interlocked:Source

Specifies the source 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 of the 
 [Handshake Trigger](/csh?context=nidaqmx_mxcncpts_handtrig)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Hshk.Interlocked.Src |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr22b9.html language=enus -->
## TOPIC 01639: More:Handshake:Interlocked:Asserted Level

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr22b9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr22b9.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the asserted level of the Handshake Trigger . Remarks The following table lists the characteristics of this property. Short Name Hshk.Interlocked.AssertedLvl Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engin

### More:Handshake:Interlocked:Asserted Level

Specifies the asserted level of the 
 [Handshake Trigger](/csh?context=nidaqmx_mxcncpts_handtrig)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Hshk.Interlocked.AssertedLvl |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| High | 10192 | High state. |
| --- | --- | --- |
| Low | 10214 | Low state. |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2ec1.html language=enus -->
## TOPIC 01640: Reference:Auto Trigger:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2ec1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2ec1.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to send a software trigger to the device when a hardware trigger is no longer active in order to prevent a timeout. Remarks The following table lists the characteristics of this property. Short Name Ref.AutoTrig.Enable Data type cbool.png Permissions Read/Write Resettable True Sett

### Reference:Auto Trigger:Enable

Specifies whether to send a software trigger to the device when a hardware trigger is no longer active in order to prevent a timeout.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.AutoTrig.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2ec2.html language=enus -->
## TOPIC 01641: Reference:Auto Triggered

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2ec2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2ec2.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether a completed acquisition was triggered by the auto trigger. If an acquisition has not completed after the task starts, this property returns FALSE. This property is only applicable when Ref.AutoTrig.Enable is TRUE. Remarks The following table lists the characteristics of this proper

### Reference:Auto Triggered

Indicates whether a completed acquisition was triggered by the auto trigger. If an acquisition has not completed after the task starts, this property returns FALSE. This property is only applicable when 
 [Ref.AutoTrig.Enable](/csh?context=nidaqmx_daqmxprop_attr2ec1)
 is TRUE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.AutoTriggered |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2ed7.html language=enus -->
## TOPIC 01642: Reference:Digital Edge:Digital Filter:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2ed7.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2ed7.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply a digital filter to the trigger signal. Remarks The following table lists the characteristics of this property. Short Name Ref.DigEdge.DigFltr.Enable Data type cbool.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-

### Reference:Digital Edge:Digital Filter:Enable

Specifies whether to apply a digital 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 to the trigger signal.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.DigEdge.DigFltr.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2ed8.html language=enus -->
## TOPIC 01643: Reference:Digital Edge:Digital Filter:Minimum Pulse Width

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2ed8.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2ed8.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. Remarks The following table lists the characteristics of this property. Short Name Ref.DigEdge.DigFltr.MinPulseWidth Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available

### Reference:Digital Edge:Digital Filter:Minimum Pulse Width

Specifies in seconds the minimum pulse width the 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 recognizes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.DigEdge.DigFltr.MinPulseWidth |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2ed9.html language=enus -->
## TOPIC 01644: Reference:Digital Edge:Digital Filter:Timebase:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2ed9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2ed9.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the timebase of the digital filter. Remarks The following table lists the characteristics of this property. Short Name Ref.DigEdge.DigFltr.TimebaseSrc Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running device

### Reference:Digital Edge:Digital Filter:Timebase:Source

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 of the signal to use as the timebase of the digital filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.DigEdge.DigFltr.TimebaseSrc |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2eda.html language=enus -->
## TOPIC 01645: Reference:Digital Edge:Digital Filter:Timebase:Rate

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2eda.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2eda.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. Remarks The following table lists the characteristics of this property. Short Name Ref.DigEdge.DigFltr.TimebaseRate Data type cdbl.png Permissions Read/Write Resettable True Setta

### Reference:Digital Edge:Digital Filter:Timebase:Rate

Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.DigEdge.DigFltr.TimebaseRate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2edb.html language=enus -->
## TOPIC 01646: Reference:Digital Edge:Digital Synchronization:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2edb.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2edb.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. Remarks The following table lists the characteristics of this property. Short Name Ref.DigEdge.DigSync.Enable Data type cbool.png Permissions Read/Write Resettable True Settable While Ta

### Reference:Digital Edge:Digital Synchronization:Enable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.DigEdge.DigSync.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee1.html language=enus -->
## TOPIC 01647: Start:Analog Edge:Digital Filter:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee1.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay above or below the trigger level for the minimum pulse width before being recognized. Use filtering for noisy trigger signals

### Start:Analog Edge:Digital Filter:Enable

Specifies whether to apply a digital 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay above or below the trigger level for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the hysteresis window rapidly.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.AnlgEdge.DigFltr.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee2.html language=enus -->
## TOPIC 01648: Start:Analog Edge:Digital Filter:Minimum Pulse Width

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee2.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. Remarks The following table lists the characteristics of this property. Short Name Start.AnlgEdge.DigFltr.MinPulseWidth Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Availab

### Start:Analog Edge:Digital Filter:Minimum Pulse Width

Specifies in seconds the minimum pulse width the 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 recognizes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.AnlgEdge.DigFltr.MinPulseWidth |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee3.html language=enus -->
## TOPIC 01649: Start:Analog Edge:Digital Filter:Timebase:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee3.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the timebase of the digital filter. Remarks The following table lists the characteristics of this property. Short Name Start.AnlgEdge.DigFltr.TimebaseSrc Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running dev

### Start:Analog Edge:Digital Filter:Timebase:Source

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 of the signal to use as the timebase of the digital filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.AnlgEdge.DigFltr.TimebaseSrc |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee4.html language=enus -->
## TOPIC 01650: Start:Analog Edge:Digital Filter:Timebase:Rate

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee4.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee4.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. Remarks The following table lists the characteristics of this property. Short Name Start.AnlgEdge.DigFltr.TimebaseRate Data type cdbl.png Permissions Read/Write Resettable True Se

### Start:Analog Edge:Digital Filter:Timebase:Rate

Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.AnlgEdge.DigFltr.TimebaseRate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee5.html language=enus -->
## TOPIC 01651: Start:Analog Edge:Digital Synchronization:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee5.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee5.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. Remarks The following table lists the characteristics of this property. Short Name Start.AnlgEdge.DigSync.Enable Data type cbool.png Permissions Read/Write Resettable True Settable While

### Start:Analog Edge:Digital Synchronization:Enable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.AnlgEdge.DigSync.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee6.html language=enus -->
## TOPIC 01652: Reference:Analog Edge:Digital Filter:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee6.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee6.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay above or below the trigger level for the minimum pulse width before being recognized. Use filtering for noisy trigger signals

### Reference:Analog Edge:Digital Filter:Enable

Specifies whether to apply a digital 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay above or below the trigger level for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the hysteresis window rapidly.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.AnlgEdge.DigFltr.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee7.html language=enus -->
## TOPIC 01653: Reference:Analog Edge:Digital Filter:Minimum Pulse Width

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee7.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee7.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. Remarks The following table lists the characteristics of this property. Short Name Ref.AnlgEdge.DigFltr.MinPulseWidth Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available

### Reference:Analog Edge:Digital Filter:Minimum Pulse Width

Specifies in seconds the minimum pulse width the
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 recognizes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.AnlgEdge.DigFltr.MinPulseWidth |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee8.html language=enus -->
## TOPIC 01654: Reference:Analog Edge:Digital Filter:Timebase:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee8.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee8.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the timebase of the digital filter. Remarks The following table lists the characteristics of this property. Short Name Ref.AnlgEdge.DigFltr.TimebaseSrc Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running devic

### Reference:Analog Edge:Digital Filter:Timebase:Source

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 of the signal to use as the timebase of the digital filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.AnlgEdge.DigFltr.TimebaseSrc |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee9.html language=enus -->
## TOPIC 01655: Reference:Analog Edge:Digital Filter:Timebase:Rate

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2ee9.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. Remarks The following table lists the characteristics of this property. Short Name Ref.AnlgEdge.DigFltr.TimebaseRate Data type cdbl.png Permissions Read/Write Resettable True Sett

### Reference:Analog Edge:Digital Filter:Timebase:Rate

Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.AnlgEdge.DigFltr.TimebaseRate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2eea.html language=enus -->
## TOPIC 01656: Reference:Analog Edge:Digital Synchronization:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2eea.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2eea.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. Remarks The following table lists the characteristics of this property. Short Name Ref.AnlgEdge.DigSync.Enable Data type cbool.png Permissions Read/Write Resettable True Settable While T

### Reference:Analog Edge:Digital Synchronization:Enable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.AnlgEdge.DigSync.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2eeb.html language=enus -->
## TOPIC 01657: Reference:Analog Window:Digital Filter:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2eeb.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2eeb.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay within the trigger window for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that tr

### Reference:Analog Window:Digital Filter:Enable

Specifies whether to apply a digital 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay within the trigger window for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the window rapidly.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.AnlgWin.DigFltr.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2eec.html language=enus -->
## TOPIC 01658: Reference:Analog Window:Digital Filter:Minimum Pulse Width

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2eec.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2eec.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. Remarks The following table lists the characteristics of this property. Short Name Ref.AnlgWin.DigFltr.MinPulseWidth Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available

### Reference:Analog Window:Digital Filter:Minimum Pulse Width

Specifies in seconds the minimum pulse width the 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 recognizes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.AnlgWin.DigFltr.MinPulseWidth |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2eed.html language=enus -->
## TOPIC 01659: Reference:Analog Window:Digital Filter:Timebase:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2eed.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2eed.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the timebase of the digital filter. Remarks The following table lists the characteristics of this property. Short Name Ref.AnlgWin.DigFltr.TimebaseSrc Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running device

### Reference:Analog Window:Digital Filter:Timebase:Source

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 of the signal to use as the timebase of the digital filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.AnlgWin.DigFltr.TimebaseSrc |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2eee.html language=enus -->
## TOPIC 01660: Reference:Analog Window:Digital Filter:Timebase:Rate

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2eee.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2eee.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. Remarks The following table lists the characteristics of this property. Short Name Ref.AnlgWin.DigFltr.TimebaseRate Data type cdbl.png Permissions Read/Write Resettable True Setta

### Reference:Analog Window:Digital Filter:Timebase:Rate

Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.AnlgWin.DigFltr.TimebaseRate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2eef.html language=enus -->
## TOPIC 01661: Reference:Analog Window:Digital Synchronization:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2eef.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2eef.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. Remarks The following table lists the characteristics of this property. Short Name Ref.AnlgWin.DigSync.Enable Data type cbool.png Permissions Read/Write Resettable True Settable While Ta

### Reference:Analog Window:Digital Synchronization:Enable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.AnlgWin.DigSync.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef0.html language=enus -->
## TOPIC 01662: More:Pause:Analog Level:Digital Filter:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef0.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef0.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay above or below the trigger level for the minimum pulse width before being recognized. Use filtering for noisy trigger signals

### More:Pause:Analog Level:Digital Filter:Enable

Specifies whether to apply a digital 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay above or below the trigger level for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the hysteresis window rapidly.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pause.AnlgLvl.DigFltr.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef1.html language=enus -->
## TOPIC 01663: More:Pause:Analog Level:Digital Filter:Minimum Pulse Width

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef1.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. Remarks The following table lists the characteristics of this property. Short Name Pause.AnlgLvl.DigFltr.MinPulseWidth Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Availabl

### More:Pause:Analog Level:Digital Filter:Minimum Pulse Width

Specifies in seconds the minimum pulse width the 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 recognizes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pause.AnlgLvl.DigFltr.MinPulseWidth |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef2.html language=enus -->
## TOPIC 01664: More:Pause:Analog Level:Digital Filter:Timebase:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef2.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the timebase of the digital filter. Remarks The following table lists the characteristics of this property. Short Name Pause.AnlgLvl.DigFltr.TimebaseSrc Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running devi

### More:Pause:Analog Level:Digital Filter:Timebase:Source

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 of the signal to use as the timebase of the digital filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pause.AnlgLvl.DigFltr.TimebaseSrc |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef3.html language=enus -->
## TOPIC 01665: More:Pause:Analog Level:Digital Filter:Timebase:Rate

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef3.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. Remarks The following table lists the characteristics of this property. Short Name Pause.AnlgLvl.DigFltr.TimebaseRate Data type cdbl.png Permissions Read/Write Resettable True Set

### More:Pause:Analog Level:Digital Filter:Timebase:Rate

Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pause.AnlgLvl.DigFltr.TimebaseRate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef4.html language=enus -->
## TOPIC 01666: More:Pause:Analog Level:Digital Synchronization:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef4.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef4.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. Remarks The following table lists the characteristics of this property. Short Name Pause.AnlgLvl.DigSync.Enable Data type cbool.png Permissions Read/Write Resettable True Settable While

### More:Pause:Analog Level:Digital Synchronization:Enable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pause.AnlgLvl.DigSync.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef5.html language=enus -->
## TOPIC 01667: More:Pause:Analog Window:Digital Filter:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef5.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef5.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay within the trigger window for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that tr

### More:Pause:Analog Window:Digital Filter:Enable

Specifies whether to apply a digital 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay within the trigger window for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the window rapidly.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pause.AnlgWin.DigFltr.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef6.html language=enus -->
## TOPIC 01668: More:Pause:Analog Window:Digital Filter:Minimum Pulse Width

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef6.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef6.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. Remarks The following table lists the characteristics of this property. Short Name Pause.AnlgWin.DigFltr.MinPulseWidth Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Availabl

### More:Pause:Analog Window:Digital Filter:Minimum Pulse Width

Specifies in seconds the minimum pulse width the 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 recognizes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pause.AnlgWin.DigFltr.MinPulseWidth |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef7.html language=enus -->
## TOPIC 01669: More:Pause:Analog Window:Digital Filter:Timebase:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef7.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef7.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the timebase of the digital filter. Remarks The following table lists the characteristics of this property. Short Name Pause.AnlgWin.DigFltr.TimebaseSrc Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running devi

### More:Pause:Analog Window:Digital Filter:Timebase:Source

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 of the signal to use as the timebase of the digital filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pause.AnlgWin.DigFltr.TimebaseSrc |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef8.html language=enus -->
## TOPIC 01670: More:Pause:Analog Window:Digital Filter:Timebase:Rate

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef8.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef8.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. Remarks The following table lists the characteristics of this property. Short Name Pause.AnlgWin.DigFltr.TimebaseRate Data type cdbl.png Permissions Read/Write Resettable True Set

### More:Pause:Analog Window:Digital Filter:Timebase:Rate

Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pause.AnlgWin.DigFltr.TimebaseRate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef9.html language=enus -->
## TOPIC 01671: More:Pause:Analog Window:Digital Synchronization:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2ef9.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. Remarks The following table lists the characteristics of this property. Short Name Pause.AnlgWin.DigSync.Enable Data type cbool.png Permissions Read/Write Resettable True Settable While

### More:Pause:Analog Window:Digital Synchronization:Enable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pause.AnlgWin.DigSync.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2eff.html language=enus -->
## TOPIC 01672: Start:Analog Window:Digital Filter:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2eff.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2eff.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay within the trigger window for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that tr

### Start:Analog Window:Digital Filter:Enable

Specifies whether to apply a digital 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay within the trigger window for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the window rapidly.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.AnlgWin.DigFltr.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2f00.html language=enus -->
## TOPIC 01673: Start:Analog Window:Digital Filter:Minimum Pulse Width

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2f00.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2f00.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. Remarks The following table lists the characteristics of this property. Short Name Start.AnlgWin.DigFltr.MinPulseWidth Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Availabl

### Start:Analog Window:Digital Filter:Minimum Pulse Width

Specifies in seconds the minimum pulse width the 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 recognizes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.AnlgWin.DigFltr.MinPulseWidth |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2f01.html language=enus -->
## TOPIC 01674: Start:Analog Window:Digital Filter:Timebase:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2f01.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2f01.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the timebase of the digital filter. Remarks The following table lists the characteristics of this property. Short Name Start.AnlgWin.DigFltr.TimebaseSrc Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running devi

### Start:Analog Window:Digital Filter:Timebase:Source

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 of the signal to use as the timebase of the digital filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.AnlgWin.DigFltr.TimebaseSrc |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2f02.html language=enus -->
## TOPIC 01675: Start:Analog Window:Digital Filter:Timebase:Rate

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2f02.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2f02.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. Remarks The following table lists the characteristics of this property. Short Name Start.AnlgWin.DigFltr.TimebaseRate Data type cdbl.png Permissions Read/Write Resettable True Set

### Start:Analog Window:Digital Filter:Timebase:Rate

Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.AnlgWin.DigFltr.TimebaseRate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2f03.html language=enus -->
## TOPIC 01676: Start:Analog Window:Digital Synchronization:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2f03.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2f03.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. Remarks The following table lists the characteristics of this property. Short Name Start.AnlgWin.DigSync.Enable Data type cbool.png Permissions Read/Write Resettable True Settable While

### Start:Analog Window:Digital Synchronization:Enable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.AnlgWin.DigSync.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2f1e.html language=enus -->
## TOPIC 01677: Start:Terminal

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2f1e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2f1e.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the name of the internal Start Trigger terminal for the task. This property does not return the name of the trigger source terminal. Remarks The following table lists the characteristics of this property. Short Name Start.Term Data type cdaqmxscale.png Permissions Read Only Resettable Fals

### Start:Terminal

Indicates the name of the internal Start Trigger terminal for the task. This property does not return the name of the trigger source terminal.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.Term |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2f1f.html language=enus -->
## TOPIC 01678: Reference:Terminal

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2f1f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2f1f.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the name of the internal Reference Trigger terminal for the task. This property does not return the name of the trigger source terminal. Remarks The following table lists the characteristics of this property. Short Name Ref.Term Data type cdaqmxscale.png Permissions Read Only Resettable Fa

### Reference:Terminal

Indicates the name of the internal Reference Trigger terminal for the task. This property does not return the name of the trigger source terminal.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.Term |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2f20.html language=enus -->
## TOPIC 01679: More:Pause:Terminal

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2f20.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2f20.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the name of the internal Pause Trigger terminal for the task. This property does not return the name of the trigger source terminal. Remarks The following table lists the characteristics of this property. Short Name Pause.Term Data type cdaqmxscale.png Permissions Read Only Resettable Fals

### More:Pause:Terminal

Indicates the name of the internal Pause Trigger terminal for the task. This property does not return the name of the trigger source terminal.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pause.Term |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2f7f.html language=enus -->
## TOPIC 01680: More:Arm Start:Terminal

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2f7f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2f7f.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the name of the internal Arm Start Trigger terminal for the task. This property does not return the name of the trigger source terminal. Remarks The following table lists the characteristics of this property. Short Name ArmStart.Term Data type cdaqmxscale.png Permissions Read Only Resettab

### More:Arm Start:Terminal

Indicates the name of the internal Arm Start Trigger terminal for the task. This property does not return the name of the trigger source terminal.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ArmStart.Term |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr2f80.html language=enus -->
## TOPIC 01681: Advanced:Synchronization Type

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr2f80.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr2f80.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the role of the device in a synchronized system. Setting this value to Master or Slave enables trigger skew correction . If you enable trigger skew correction, set this property to Master on only one device, and set this property to Slave on the other devices. Remarks The following table l

### Advanced:Synchronization Type

Specifies the role of the device in a synchronized system. Setting this value to Master or Slave enables 
 [trigger skew correction](/csh?context=nidaqmx_mxcncpts_synctriggerskewcorrect)
 . If you enable trigger skew correction, set this property to Master on only one device, and set this property to Slave on the other devices.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SyncType |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| None | 10230 | Disables trigger skew correction. |
| --- | --- | --- |
| Master | 15888 | Device is the source for shared clocks and triggers. |
| Slave | 15889 | Device uses clocks and triggers from the master device. |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr3036.html language=enus -->
## TOPIC 01682: Start:Time:Timescale

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr3036.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr3036.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the timescale to be used for timestamps used in a time trigger. Remarks The following table lists the characteristics of this property. Short Name Start.Time.Timescale Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-

### Start:Time:Timescale

Specifies the timescale to be used for timestamps used in a time trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.Time.Timescale |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Host Time | 16126 | Use the host device. |
| --- | --- | --- |
| I/O Device Time | 16127 | Use the I/O device. |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr304d.html language=enus -->
## TOPIC 01683: Start:Time:When

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr304d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr304d.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies when to trigger the start trigger. Remarks The following table lists the characteristics of this property. Short Name Start.Time.When Data type catrn.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True

### Start:Time:When

Specifies when to trigger the start trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.Time.When |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr311a.html language=enus -->
## TOPIC 01684: Start:More:Trigger Window

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr311a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr311a.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the period of time in seconds after the task starts during which the device may trigger. Once the window has expired, the device stops detecting triggers, and the task will finish after the device finishes acquiring post-trigger samples for any triggers detected. If no triggers are detecte

### Start:More:Trigger Window

Specifies the period of time in seconds after the task starts during which the device may trigger. Once the window has expired, the device stops detecting triggers, and the task will finish after the device finishes acquiring post-trigger samples for any triggers detected. If no triggers are detected during the entire period, then no data will be returned. Ensure the period of time specified covers the entire time span desired for trigger detection to avoid missed triggers. Specifying a Trigger Window of -1 causes the window to be infinite.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.TrigWin |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr311b.html language=enus -->
## TOPIC 01685: Start:More:Retrigger Window

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr311b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr311b.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the period of time in seconds after each trigger during which the device may trigger. Once the window has expired, the device stops detecting triggers, and the task will finish after the device finishes acquiring post-trigger samples that it already started. Ensure the period of time speci

### Start:More:Retrigger Window

Specifies the period of time in seconds after each trigger during which the device may trigger. Once the window has expired, the device stops detecting triggers, and the task will finish after the device finishes acquiring post-trigger samples that it already started. Ensure the period of time specified covers the entire time span desired for retrigger detection to avoid missed triggers. Specifying a Retrigger Window of -1 causes the window to be infinite.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.RetriggerWin |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr311c.html language=enus -->
## TOPIC 01686: Start:More:Maximum Number of Triggers to Detect

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr311c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr311c.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of times the task will detect a start trigger during the task. The number of times a trigger is detected and acted upon by the module may be less than the specified amount if the task stops early because of trigger/retrigger window expiration. Specifying the Maximum Numb

### Start:More:Maximum Number of Triggers to Detect

Specifies the maximum number of times the task will detect a start trigger during the task. The number of times a trigger is detected and acted upon by the module may be less than the specified amount if the task stops early because of trigger/retrigger window expiration. Specifying the Maximum Number of Triggers to Detect to be 0 causes the driver to automatically set this value to the maximum possible number of triggers detectable by the device and configuration combination. Note: The number of detected triggers may be less than number of trigger events occurring, because the devices were unable to respond to the trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.MaxNumTrigsToDetect |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr311d.html language=enus -->
## TOPIC 01687: Reference:More:Retriggerable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr311d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr311d.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether a finite task resets, acquires pretrigger samples, and waits for another Reference Trigger after the task completes. When you set this property to TRUE, the device will acquire post-trigger samples, reset, and acquire pretrigger samples each time the Reference Trigger occurs until

### Reference:More:Retriggerable

Specifies whether a finite task resets, acquires pretrigger samples, and waits for another Reference Trigger after the task completes. When you set this property to TRUE, the device will acquire post-trigger samples, reset, and acquire pretrigger samples each time the Reference Trigger occurs until the task stops. The device ignores a trigger if it is in the process of acquiring signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.Retriggerable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr311e.html language=enus -->
## TOPIC 01688: Reference:More:Trigger Window

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr311e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr311e.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the duration in seconds after the task starts during which the device may trigger. Once the window has passed, the device stops detecting triggers, and the task will stop after the device finishes acquiring post-trigger samples that it already started. If no triggers are detected during th

### Reference:More:Trigger Window

Specifies the duration in seconds after the task starts during which the device may trigger. Once the window has passed, the device stops detecting triggers, and the task will stop after the device finishes acquiring post-trigger samples that it already started. If no triggers are detected during the entire period, then no data will be returned. Specifying a Trigger Window of -1 causes the window to be infinite.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.TrigWin |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr311f.html language=enus -->
## TOPIC 01689: Reference:More:Retrigger Window

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr311f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr311f.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the duration in seconds after each trigger during which the device may trigger. Once the window has passed, the device stops detecting triggers, and the task will stop after the device finishes acquiring post-trigger samples that it already started. Specifying a Retrigger Window of -1 caus

### Reference:More:Retrigger Window

Specifies the duration in seconds after each trigger during which the device may trigger. Once the window has passed, the device stops detecting triggers, and the task will stop after the device finishes acquiring post-trigger samples that it already started. Specifying a Retrigger Window of -1 causes the window to be infinite.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.RetriggerWin |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr3120.html language=enus -->
## TOPIC 01690: Reference:More:Maximum Number of Triggers to Detect

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr3120.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr3120.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of times the task will detect a reference trigger during the task. The number of times a trigger is detected and acted upon by the module may be less than the specified amount if the task stops early because of trigger/retrigger window expiration. Specifying the Maximum

### Reference:More:Maximum Number of Triggers to Detect

Specifies the maximum number of times the task will detect a reference trigger during the task. The number of times a trigger is detected and acted upon by the module may be less than the specified amount if the task stops early because of trigger/retrigger window expiration. Specifying the Maximum Number of Triggers to Detect to be 0 causes the driver to automatically set this value to the maximum possible number of triggers detectable by the device and configuration combination. Note: The number of detected triggers may be less than number of trigger events occurring, because the devices were unable to respond to the trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.MaxNumTrigsToDetect |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr3121.html language=enus -->
## TOPIC 01691: Start:Analog Multiple Edge:Sources

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr3121.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr3121.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a list and/or range of analog sources that are going to be used for Analog triggering. Each source corresponds to an element in each of the Analog Multi Edge property arrays, if they are not empty. Remarks The following table lists the characteristics of this property. Short Name Start.Anl

### Start:Analog Multiple Edge:Sources

Specifies a list and/or range of analog sources that are going to be used for Analog triggering. Each source corresponds to an element in each of the Analog Multi Edge property arrays, if they are not empty.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.AnlgMultiEdge.Srcs |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr3122.html language=enus -->
## TOPIC 01692: Start:Analog Multiple Edge:Slopes

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr3122.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr3122.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of slopes on which to trigger task to start generating or acquiring samples. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty. Remarks The following table list

### Start:Analog Multiple Edge:Slopes

Specifies an array of slopes on which to trigger task to start generating or acquiring samples. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.AnlgMultiEdge.Slopes |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Rising | 10280 | Trigger on the rising slope of the signal. |
| --- | --- | --- |
| Falling | 10171 | Trigger on the falling slope of the signal. |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr3123.html language=enus -->
## TOPIC 01693: Start:Analog Multiple Edge:Levels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr3123.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr3123.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of thresholds in the units of the measurement or generation to start acquiring or generating samples. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty. Remarks

### Start:Analog Multiple Edge:Levels

Specifies an array of thresholds in the units of the measurement or generation to start acquiring or generating samples. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.AnlgMultiEdge.Lvls |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr3124.html language=enus -->
## TOPIC 01694: Start:Analog Multiple Edge:Hystereses

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr3124.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr3124.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of hysteresis levels in the units of the measurement or generation. If the corresponding element of Start.AnlgMultiEdge.Slopes is Rising, the trigger does not deassert until the source signal passes below the corresponding element of Start.AnlgMultiEdge.Lvls minus the hysteresis.

### Start:Analog Multiple Edge:Hystereses

Specifies an array of hysteresis levels in the units of the measurement or generation. If the corresponding element of Start.AnlgMultiEdge.Slopes is Rising, the trigger does not deassert until the source signal passes below the corresponding element of Start.AnlgMultiEdge.Lvls minus the hysteresis. If Start.AnlgEdge.Slope is Falling, the trigger does not deassert until the source signal passes above Start.AnlgEdge.Lvl plus the hysteresis. Hysteresis is always enabled. Set this property to a non-zero value to use hysteresis. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.AnlgMultiEdge.Hysts |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr3125.html language=enus -->
## TOPIC 01695: Start:Analog Multiple Edge:Couplings

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr3125.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr3125.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array that describes the couplings for the corresponding source signal of the trigger if the source is a terminal rather than a virtual channel. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property a

### Start:Analog Multiple Edge:Couplings

Specifies an array that describes the couplings for the corresponding source signal of the trigger if the source is a terminal rather than a virtual channel. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.AnlgMultiEdge.Couplings |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| AC | 10045 | Alternating Current. |
| --- | --- | --- |
| DC | 10050 | Direct Current. |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr3126.html language=enus -->
## TOPIC 01696: Reference:Analog Multiple Edge:Sources

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr3126.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr3126.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a List and/or range of analog sources that are going to be used for Analog triggering. Each source corresponds to an element in each of the Analog Multi Edge property arrays, if they are not empty. Remarks The following table lists the characteristics of this property. Short Name Ref.AnlgM

### Reference:Analog Multiple Edge:Sources

Specifies a List and/or range of analog sources that are going to be used for Analog triggering. Each source corresponds to an element in each of the Analog Multi Edge property arrays, if they are not empty.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.AnlgMultiEdge.Srcs |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr3127.html language=enus -->
## TOPIC 01697: Reference:Analog Multiple Edge:Slopes

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr3127.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr3127.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of slopes on which to trigger task to start generating or acquiring samples. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty. Remarks The following table lists

### Reference:Analog Multiple Edge:Slopes

Specifies an array of slopes on which to trigger task to start generating or acquiring samples. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.AnlgMultiEdge.Slopes |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Rising | 10280 | Trigger on the rising slope of the signal. |
| --- | --- | --- |
| Falling | 10171 | Trigger on the falling slope of the signal. |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr3128.html language=enus -->
## TOPIC 01698: Reference:Analog Multiple Edge:Levels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr3128.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr3128.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of thresholds in the units of the measurement or generation to start acquiring or generating samples. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty. Remarks T

### Reference:Analog Multiple Edge:Levels

Specifies an array of thresholds in the units of the measurement or generation to start acquiring or generating samples. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.AnlgMultiEdge.Lvls |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr3129.html language=enus -->
## TOPIC 01699: Reference:Analog Multiple Edge:Hystereses

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr3129.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr3129.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of hysteresis levels in the units of the measurement or generation. If the corresponding element of Ref.AnlgMultiEdge.Slopes is Rising, the trigger does not deassert until the source signal passes below the corresponding element of Ref.AnlgMultiEdge.Lvls minus the hysteresis. If R

### Reference:Analog Multiple Edge:Hystereses

Specifies an array of hysteresis levels in the units of the measurement or generation. If the corresponding element of Ref.AnlgMultiEdge.Slopes is Rising, the trigger does not deassert until the source signal passes below the corresponding element of Ref.AnlgMultiEdge.Lvls minus the hysteresis. If Ref.AnlgEdge.Slope is Falling, the trigger does not deassert until the source signal passes above Ref.AnlgEdge.Lvl plus the hysteresis. Hysteresis is always enabled. Set this property to a non-zero value to use hysteresis. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.AnlgMultiEdge.Hysts |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr312a.html language=enus -->
## TOPIC 01700: Reference:Analog Multiple Edge:Couplings

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr312a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr312a.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array that describes the couplings for the corresponding source signal of the trigger if the source is a terminal rather than a virtual channel. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arr

### Reference:Analog Multiple Edge:Couplings

Specifies an array that describes the couplings for the corresponding source signal of the trigger if the source is a terminal rather than a virtual channel. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.AnlgMultiEdge.Couplings |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| AC | 10045 | Alternating Current. |
| --- | --- | --- |
| DC | 10050 | Direct Current. |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr312d.html language=enus -->
## TOPIC 01701: Start:Timestamp:Timescale

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr312d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr312d.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the start trigger timestamp timescale. Remarks The following table lists the characteristics of this property. Short Name Start.Timestamp.Timescale Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True Hos

### Start:Timestamp:Timescale

Specifies the start trigger timestamp timescale.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.Timestamp.Timescale |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Host Time | 16126 | Use the host device. |
| --- | --- | --- |
| I/O Device Time | 16127 | Use the I/O device. |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr312e.html language=enus -->
## TOPIC 01702: Reference:Timestamp:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr312e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr312e.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the reference trigger timestamp is enabled. If the timestamp is enabled but no resources are available, an error will be returned at run time. Remarks The following table lists the characteristics of this property. Short Name Ref.Timestamp.Enable Data type cbool.png Permissions Rea

### Reference:Timestamp:Enable

Specifies whether the reference trigger timestamp is enabled. If the timestamp is enabled but no resources are available, an error will be returned at run time.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.Timestamp.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr312f.html language=enus -->
## TOPIC 01703: Reference:Timestamp:Value

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr312f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr312f.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the reference trigger timestamp value. Remarks The following table lists the characteristics of this property. Short Name Ref.Timestamp.Val Data type catrn.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### Reference:Timestamp:Value

Indicates the reference trigger timestamp value.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.Timestamp.Val |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr3130.html language=enus -->
## TOPIC 01704: Reference:Timestamp:Timescale

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr3130.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr3130.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference trigger timestamp timescale. Remarks The following table lists the characteristics of this property. Short Name Ref.Timestamp.Timescale Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True H

### Reference:Timestamp:Timescale

Specifies the reference trigger timestamp timescale.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref.Timestamp.Timescale |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Host Time | 16126 | Use the host device. |
| --- | --- | --- |
| I/O Device Time | 16127 | Use the I/O device. |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr3131.html language=enus -->
## TOPIC 01705: More:Arm Start:Time:When

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr3131.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr3131.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies when to trigger the arm start trigger. Remarks The following table lists the characteristics of this property. Short Name ArmStart.Time.When Data type catrn.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True

### More:Arm Start:Time:When

Specifies when to trigger the arm start trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ArmStart.Time.When |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr3132.html language=enus -->
## TOPIC 01706: More:Arm Start:Time:Timescale

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr3132.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr3132.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the timescale to be used for timestamps used in an arm start time trigger. Remarks The following table lists the characteristics of this property. Short Name ArmStart.Time.Timescale Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Ava

### More:Arm Start:Time:Timescale

Specifies the timescale to be used for timestamps used in an arm start time trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ArmStart.Time.Timescale |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Host Time | 16126 | Use the host device. |
| --- | --- | --- |
| I/O Device Time | 16127 | Use the I/O device. |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr3133.html language=enus -->
## TOPIC 01707: More:Arm Start:Timestamp:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr3133.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr3133.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the arm start trigger timestamp is enabled. If the timestamp is enabled but no resources are available, an error will be returned at run time. Remarks The following table lists the characteristics of this property. Short Name ArmStart.Timestamp.Enable Data type cbool.png Permission

### More:Arm Start:Timestamp:Enable

Specifies whether the arm start trigger timestamp is enabled. If the timestamp is enabled but no resources are available, an error will be returned at run time.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ArmStart.Timestamp.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr3134.html language=enus -->
## TOPIC 01708: More:Arm Start:Timestamp:Value

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr3134.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr3134.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the arm start trigger timestamp value. Remarks The following table lists the characteristics of this property. Short Name ArmStart.Timestamp.Val Data type catrn.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### More:Arm Start:Timestamp:Value

Indicates the arm start trigger timestamp value.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ArmStart.Timestamp.Val |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr3135.html language=enus -->
## TOPIC 01709: More:Arm Start:Timestamp:Timescale

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr3135.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr3135.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the arm start trigger timestamp timescale. Remarks The following table lists the characteristics of this property. Short Name ArmStart.Timestamp.Timescale Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine T

### More:Arm Start:Timestamp:Timescale

Specifies the arm start trigger timestamp timescale.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ArmStart.Timestamp.Timescale |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Host Time | 16126 | Use the host device. |
| --- | --- | --- |
| I/O Device Time | 16127 | Use the I/O device. |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr314a.html language=enus -->
## TOPIC 01710: Start:Timestamp:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr314a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr314a.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the start trigger timestamp is enabled. If the timestamp is enabled but no resources are available, an error will be returned at run time. Remarks The following table lists the characteristics of this property. Short Name Start.Timestamp.Enable Data type cbool.png Permissions Read/

### Start:Timestamp:Enable

Specifies whether the start trigger timestamp is enabled. If the timestamp is enabled but no resources are available, an error will be returned at run time.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.Timestamp.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-trigger/attr314b.html language=enus -->
## TOPIC 01711: Start:Timestamp:Value

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-trigger/attr314b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-trigger/attr314b.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the start trigger timestamp value. Remarks The following table lists the characteristics of this property. Short Name Start.Timestamp.Val Data type catrn.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### Start:Timestamp:Value

Indicates the start trigger timestamp value.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start.Timestamp.Val |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Trigger Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-watchdog-p.html language=enus -->
## TOPIC 01712: DAQmx Watchdog Properties

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-watchdog-p.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-watchdog-p.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the DAQmx Watchdog properties to configure the watchdog timer of a device.

### DAQmx Watchdog Properties

Use the DAQmx Watchdog properties to configure the watchdog timer of a device.

- [Expiration States:Active Physical Channels](../../../resource/objmgr/daqmx-rc/daqmx-watchdog/attr21a6.html) Specifies a physical channel or list of physical channels to modify. You cannot modify the expiration state of dedicated digital input physical channels.
- [Expiration States:Analog Output:Expiration State](../../../resource/objmgr/daqmx-rc/daqmx-watchdog/attr305f.html) Specifies the state to set the analog output physical channels when the watchdog task expires.
- [Expiration States:Analog Output:Output Type](../../../resource/objmgr/daqmx-rc/daqmx-watchdog/attr305e.html) Specifies the output type of the analog output physical channels when the watchdog task expires.
- [Expiration States:Counter Output:Expiration State](../../../resource/objmgr/daqmx-rc/daqmx-watchdog/attr3060.html) Specifies the state to set the counter output channel terminal when the watchdog task expires.
- [Expiration States:Digital Output:Expiration State](../../../resource/objmgr/daqmx-rc/daqmx-watchdog/attr21a7.html) Specifies the state to which to set the digital physical channels when the watchdog task expires. You cannot modify the expiration state of dedicated digital input physical channels.
- [Expiration Trigger:Digital Edge:Edge](../../../resource/objmgr/daqmx-rc/daqmx-watchdog/attr21a5.html) Specifies on which edge of a digital signal to expire the watchdog task.
- [Expiration Trigger:Digital Edge:Source](../../../resource/objmgr/daqmx-rc/daqmx-watchdog/attr21a4.html) Specifies the name of a terminal where a digital signal exists to use as the source of the Expiration Trigger.
- [Expiration Trigger:Trigger On Network Connection Loss](../../../resource/objmgr/daqmx-rc/daqmx-watchdog/attr305d.html) Specifies the watchdog timer behavior when the network connection is lost between the host and the chassis. If set to true, the watchdog timer expires when the chassis detects the loss of network connection.
- [Expiration Trigger:Trigger Type](../../../resource/objmgr/daqmx-rc/daqmx-watchdog/attr21a3.html) Specifies the type of trigger to use to expire a watchdog task.
- [Status:Expired](../../../resource/objmgr/daqmx-rc/daqmx-watchdog/attr21a8.html) Indicates if the watchdog timer expired. You can read this property only while the task is running.
- [Timeout](../../../resource/objmgr/daqmx-rc/daqmx-watchdog/attr21a9.html) Specifies in seconds the amount of time until the watchdog timer expires. A value of -1 means the internal timer never expires. Set this input to -1 if you use an Expiration Trigger to expire the watchdog task.

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-watchdog/attr21a3.html language=enus -->
## TOPIC 01713: Expiration Trigger:Trigger Type

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-watchdog/attr21a3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-watchdog/attr21a3.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of trigger to use to expire a watchdog task. Remarks The following table lists the characteristics of this property. Short Name ExpirTrig.TrigType Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine

### Expiration Trigger:Trigger Type

Specifies the type of trigger to use to expire a watchdog task.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ExpirTrig.TrigType |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Digital Edge | 10150 | Trigger on a rising or falling edge of a digital signal. |
| --- | --- | --- |
| Time | 15996 | Trigger when a specified time is reached. |
| None | 10230 | Disable the trigger. |

Parent topic:

DAQmx Watchdog Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-watchdog/attr21a4.html language=enus -->
## TOPIC 01714: Expiration Trigger:Digital Edge:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-watchdog/attr21a4.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-watchdog/attr21a4.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of a terminal where a digital signal exists to use as the source of the Expiration Trigger. Remarks The following table lists the characteristics of this property. Short Name ExpirTrig.DigEdge.Src Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task

### Expiration Trigger:Digital Edge:Source

Specifies the name of a 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 where a digital signal exists to use as the source of the Expiration Trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ExpirTrig.DigEdge.Src |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Watchdog Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-watchdog/attr21a5.html language=enus -->
## TOPIC 01715: Expiration Trigger:Digital Edge:Edge

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-watchdog/attr21a5.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-watchdog/attr21a5.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge of a digital signal to expire the watchdog task. Remarks The following table lists the characteristics of this property. Short Name ExpirTrig.DigEdge.Edge Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run

### Expiration Trigger:Digital Edge:Edge

Specifies on which edge of a digital signal to expire the watchdog task.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ExpirTrig.DigEdge.Edge |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Rising | 10280 | Rising edge(s). |
| --- | --- | --- |
| Falling | 10171 | Falling edge(s). |

Parent topic:

DAQmx Watchdog Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-watchdog/attr21a6.html language=enus -->
## TOPIC 01716: Expiration States:Active Physical Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-watchdog/attr21a6.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-watchdog/attr21a6.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a physical channel or list of physical channels to modify. You cannot modify the expiration state of dedicated digital input physical channels. Remarks The following table lists the characteristics of this property. Short Name ExpirStates.ActivePhysicalChans Data type cdaqmxscale.png Permi

### Expiration States:Active Physical Channels

Specifies a 
 [physical channel](/csh?context=nidaqmx_mxcncpts_chans)
 or list of physical channels to modify. You cannot modify the expiration state of dedicated digital input physical channels.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ExpirStates.ActivePhysicalChans |
| --- | --- |
| Data type |  |
| Permissions | Write Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Watchdog Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-watchdog/attr21a7.html language=enus -->
## TOPIC 01717: Expiration States:Digital Output:Expiration State

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-watchdog/attr21a7.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-watchdog/attr21a7.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the state to which to set the digital physical channels when the watchdog task expires. You cannot modify the expiration state of dedicated digital input physical channels. Remarks The following table lists the characteristics of this property. Short Name ExpirStates.DO.State Data type ci3

### Expiration States:Digital Output:Expiration State

Specifies the state to which to set the digital physical channels when the watchdog task expires. You cannot modify the expiration state of dedicated digital input physical channels.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ExpirStates.DO.State |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| High | 10192 | Logic high. |
| --- | --- | --- |
| Low | 10214 | Logic low. |
| Tristate | 10310 | High-impedance state. You can select this state only on devices with bidirectional lines. You cannot select this state for dedicated digital output lines. On some devices, you can select this value only for entire ports. |
| No Change | 10160 | Do not change the state of the lines. On some devices, you can select this value only for entire ports. |

Parent topic:

DAQmx Watchdog Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-watchdog/attr21a8.html language=enus -->
## TOPIC 01718: Status:Expired

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-watchdog/attr21a8.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-watchdog/attr21a8.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the watchdog timer expired. You can read this property only while the task is running. Remarks The following table lists the characteristics of this property. Short Name Expired Data type cbool.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Ava

### Status:Expired

Indicates if the watchdog timer expired. You can read this property only while the task is running.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Expired |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Watchdog Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-watchdog/attr21a9.html language=enus -->
## TOPIC 01719: Timeout

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-watchdog/attr21a9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-watchdog/attr21a9.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the amount of time until the watchdog timer expires. A value of -1 means the internal timer never expires. Set this input to -1 if you use an Expiration Trigger to expire the watchdog task. Remarks The following table lists the characteristics of this property. Short Name Timeou

### Timeout

Specifies in seconds the amount of time until the watchdog timer expires. A value of -1 means the internal timer never expires. Set this input to -1 if you use an Expiration Trigger to expire the watchdog task.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Timeout |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Watchdog Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-watchdog/attr305d.html language=enus -->
## TOPIC 01720: Expiration Trigger:Trigger On Network Connection Loss

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-watchdog/attr305d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-watchdog/attr305d.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the watchdog timer behavior when the network connection is lost between the host and the chassis. If set to true, the watchdog timer expires when the chassis detects the loss of network connection. Remarks The following table lists the characteristics of this property. Short Name ExpirTrig

### Expiration Trigger:Trigger On Network Connection Loss

Specifies the watchdog timer behavior when the network connection is lost between the host and the chassis. If set to true, the watchdog timer expires when the chassis detects the loss of network connection.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ExpirTrig.TrigOnNetworkConnLoss |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Watchdog Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-watchdog/attr305e.html language=enus -->
## TOPIC 01721: Expiration States:Analog Output:Output Type

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-watchdog/attr305e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-watchdog/attr305e.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output type of the analog output physical channels when the watchdog task expires. Remarks The following table lists the characteristics of this property. Short Name ExpirStates.AO.Type Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-spec

### Expiration States:Analog Output:Output Type

Specifies the output type of the analog output physical channels when the watchdog task expires.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ExpirStates.AO.Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Voltage | 10322 | Voltage output. |
| --- | --- | --- |
| Current | 10134 | Current output. |
| No Change | 10160 | Expiration does not affect the port. Do not change the state of any lines in the port, and do not lock the port. |

Parent topic:

DAQmx Watchdog Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-watchdog/attr305f.html language=enus -->
## TOPIC 01722: Expiration States:Analog Output:Expiration State

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-watchdog/attr305f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-watchdog/attr305f.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the state to set the analog output physical channels when the watchdog task expires. Remarks The following table lists the characteristics of this property. Short Name ExpirStates.AO.State Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-speci

### Expiration States:Analog Output:Expiration State

Specifies the state to set the analog output physical channels when the watchdog task expires.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ExpirStates.AO.State |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Watchdog Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-watchdog/attr3060.html language=enus -->
## TOPIC 01723: Expiration States:Counter Output:Expiration State

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-watchdog/attr3060.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-watchdog/attr3060.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the state to set the counter output channel terminal when the watchdog task expires. Remarks The following table lists the characteristics of this property. Short Name ExpirStates.CO.State Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-speci

### Expiration States:Counter Output:Expiration State

Specifies the state to set the counter output channel terminal when the watchdog task expires.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ExpirStates.CO.State |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Low | 10214 | Low logic. |
| --- | --- | --- |
| High | 10192 | High logic. |
| No Change | 10160 | Expiration does not affect the state of the counter output. The channels retain their states at the time of the watchdog timer expiration, and no further counter generation runs. |

Parent topic:

DAQmx Watchdog Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-write-p.html language=enus -->
## TOPIC 01724: DAQmx Write Properties

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-write-p.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-write-p.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the DAQmx Write properties to configure write options, such as to what position in a buffer you want to write, and to query the current status of write operations.

### DAQmx Write Properties

Use the DAQmx Write properties to configure write options, such as to what 
 [position in a buffer](/csh?context=nidaqmx_mxcncpts_controlwherebufferwrite)
 you want to write, and to 
 [query the current status](/csh?context=nidaqmx_mxcncpts_writestatus)
 of write operations.

- [Advanced:Digital Output:Number of Booleans Per Channel](../../../resource/objmgr/daqmx-rc/daqmx-write/attr217f.html) Indicates the number of Boolean values expected per channel in a sample for line-based writes. This property is determined by the channel in the task with the most digital lines. If a channel has fewer lines than this number, NI-DAQmx ignores the extra Boolean values.
- [Advanced:Number of Channels](../../../resource/objmgr/daqmx-rc/daqmx-write/attr217e.html) Indicates the number of channels that DAQmx Write writes to the task. This value is the number of channels in the task.
- [Advanced:Raw Data Width](../../../resource/objmgr/daqmx-rc/daqmx-write/attr217d.html) Indicates in bytes the required size of a raw sample to write to the task.
- [Advanced:Sleep Time](../../../resource/objmgr/daqmx-rc/daqmx-write/attr22b2.html) Specifies in seconds the amount of time to sleep after checking for available buffer space if WaitMode is Sleep.
- [Advanced:Wait Mode](../../../resource/objmgr/daqmx-rc/daqmx-write/attr22b1.html) Specifies how DAQmx Write waits for space to become available in the buffer.
- [Offset](../../../resource/objmgr/daqmx-rc/daqmx-write/attr190d.html) Specifies in samples per channel an offset at which a write operation begins. This offset is relative to the location you specify with RelativeTo .
- [Regeneration Mode](../../../resource/objmgr/daqmx-rc/daqmx-write/attr1453.html) Specifies whether to allow NI-DAQmx to generate the same data multiple times.
- [Relative To](../../../resource/objmgr/daqmx-rc/daqmx-write/attr190c.html) Specifies the point in the buffer at which to write data. If you also specify an offset with Offset , the write operation begins at that offset relative to this point you select with this property.
- [Status:Accessory:Accessory Insertion or Removal Detected](../../../resource/objmgr/daqmx-rc/daqmx-write/attr3053.html) Indicates if any devices in the task detected the insertion or removal of an accessory since the task started. Reading this property clears the accessory change status for all channels in the task. You must read this property before you read DevsWithInsertedOrRemovedAccessories . Otherwise, you will receive an error.
- [Status:Accessory:Devices with Inserted or Removed Accessories](../../../resource/objmgr/daqmx-rc/daqmx-write/attr3054.html) Indicates the names of any devices that detected the insertion or removal of an accessory since the task started. You must read AccessoryInsertionOrRemovalDetected before you read this property. Otherwise, you will receive an error.
- [Status:Current Write Position](../../../resource/objmgr/daqmx-rc/daqmx-write/attr1458.html) Indicates the position in the buffer of the next sample to generate. This value is identical for all channels in the task.
- [Status:External Overvoltage:External Overvoltage Channels](../../../resource/objmgr/daqmx-rc/daqmx-write/attr30bc.html) Indicates a list of names of any virtual channels in the task for which an External Overvoltage condition has been detected. You must read External OvervoltageChansExist before you read this property. Otherwise, you will receive an error.
- [Status:External Overvoltage:External Overvoltage Channels Exist](../../../resource/objmgr/daqmx-rc/daqmx-write/attr30bb.html) Indicates if the device(s) detected an External Overvoltage condition for any channel in the task. Reading this property clears the External Overvoltage status for all channels in the task. You must read this property before you read External OvervoltageChans. Otherwise, you will receive an error.
- [Status:Open Current Loop:Open Current Loop Channels](../../../resource/objmgr/daqmx-rc/daqmx-write/attr29eb.html) Indicates a list of names of any virtual channels in the task for which the device(s) detected an open current loop . You must read OpenCurrentLoopChansExist before you read this property. Otherwise, you will receive an error.
- [Status:Open Current Loop:Open Current Loop Channels Exist](../../../resource/objmgr/daqmx-rc/daqmx-write/attr29ea.html) Indicates if the device(s) detected an open current loop for any channel in the task. Reading this property clears the open current loop status for all channels in the task. You must read this property before you read OpenCurrentLoopChans . Otherwise, you will receive an error.
- [Status:Overcurrent:Overcurrent Channels](../../../resource/objmgr/daqmx-rc/daqmx-write/attr29e9.html) Indicates a list of names of any virtual channels in the task for which an overcurrent condition has been detected. You must read OvercurrentChansExist before you read this property. Otherwise, you will receive an error.
- [Status:Overcurrent:Overcurrent Channels Exist](../../../resource/objmgr/daqmx-rc/daqmx-write/attr29e8.html) Indicates if the device(s) detected an overcurrent condition for any channel in the task. Reading this property clears the overcurrent status for all channels in the task. You must read this property before you read OvercurrentChans . Otherwise, you will receive an error.
- [Status:Overload:Overloaded Channels](../../../resource/objmgr/daqmx-rc/daqmx-write/attr3085.html) Indicates a list of names of any overloaded virtual channels in the task. You must read OverloadedChansExist before you read this property. Otherwise, you will receive an error.
- [Status:Overload:Overloaded Channels Exist](../../../resource/objmgr/daqmx-rc/daqmx-write/attr3084.html) Indicates if the device(s) detected an overload in any virtual channel in the task. Reading this property clears the overload status for all channels in the task. You must read this property before you read OverloadedChans . Otherwise, you will receive an error.
- [Status:Overtemperature:Overtemperature Channels](../../../resource/objmgr/daqmx-rc/daqmx-write/attr3083.html) Indicates a list of names of any overtemperature virtual channels. You must read OvertemperatureChansExist before you read this property. Otherwise, you will receive an error. The list of names may be empty if the device cannot determine the source of the overtemperature.
- [Status:Overtemperature:Overtemperature Channels Exist](../../../resource/objmgr/daqmx-rc/daqmx-write/attr2a84.html) Indicates if the device(s) detected an overtemperature condition in any virtual channel in the task. Reading this property clears the overtemperature status for all channels in the task. You must read this property before you read OvertemperatureChans . Otherwise, you will receive an error.
- [Status:Power Supply Fault:Power Supply Fault Channels](../../../resource/objmgr/daqmx-rc/daqmx-write/attr29ed.html) Indicates a list of names of any virtual channels in the task that have a power supply fault . You must read PowerSupplyFaultChansExist before you read this property. Otherwise, you will receive an error.
- [Status:Power Supply Fault:Power Supply Fault Channels Exist](../../../resource/objmgr/daqmx-rc/daqmx-write/attr29ec.html) Indicates if the device(s) detected a power supply fault for any channel in the task. Reading this property clears the power supply fault status for all channels in the task. You must read this property before you read PowerSupplyFaultChans . Otherwise, you will receive an error.
- [Status:Space Available in Buffer](../../../resource/objmgr/daqmx-rc/daqmx-write/attr1460.html) Indicates in samples per channel the amount of available space in the buffer.
- [Status:Synchronization:Unlocked Channels](../../../resource/objmgr/daqmx-rc/daqmx-write/attr3140.html) Indicates the channels from devices in an unlocked target.
- [Status:Synchronization:Unlocked Channels Exist](../../../resource/objmgr/daqmx-rc/daqmx-write/attr313f.html) Indicates whether the target is currently locked to the grand master. Devices may report PLL Unlock either during acquisition or after acquisition.
- [Status:Total Samples Per Channel Generated](../../../resource/objmgr/daqmx-rc/daqmx-write/attr192b.html) Indicates the total number of samples generated by each channel in the task. This value is identical for all channels in the task.

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-write/attr1453.html language=enus -->
## TOPIC 01725: Regeneration Mode

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-write/attr1453.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-write/attr1453.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to allow NI-DAQmx to generate the same data multiple times. If you enable regeneration and write new data to the buffer, NI-DAQmx can generate a combination of old and new data, a phenomenon called glitching . Remarks The following table lists the characteristics of this property.

### Regeneration Mode

Specifies whether to allow NI-DAQmx to generate the same data multiple times.

If you enable regeneration and write new data to the buffer, NI-DAQmx can generate a combination of old and new data, a phenomenon 
called 
 [glitching](/csh?context=nidaqmx_mxcncpts_glitching)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | RegenMode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Allow Regeneration | 10097 | Allow NI-DAQmx to regenerate samples that the device previously generated. When you choose this value, the write marker returns to the beginning of the buffer after the device generates all samples currently in the buffer. |
| --- | --- | --- |
| Do Not Allow Regeneration | 10158 | Do not allow NI-DAQmx to regenerate samples the device previously generated. When you choose this value, NI-DAQmx waits for you to write more samples to the buffer or until the timeout expires. |

Parent topic:

DAQmx Write Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-write/attr1458.html language=enus -->
## TOPIC 01726: Status:Current Write Position

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-write/attr1458.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-write/attr1458.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the position in the buffer of the next sample to generate. This value is identical for all channels in the task. Remarks The following table lists the characteristics of this property. Short Name CurrWritePos Data type cdbl.png Permissions Read Only Resettable False Settable While Task Is

### Status:Current Write Position

Indicates the position in the buffer of the next sample to generate. This value is identical for all channels in the task.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CurrWritePos |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Write Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-write/attr1460.html language=enus -->
## TOPIC 01727: Status:Space Available in Buffer

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-write/attr1460.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-write/attr1460.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in samples per channel the amount of available space in the buffer. Remarks The following table lists the characteristics of this property. Short Name SpaceAvail Data type cu32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time E

### Status:Space Available in Buffer

Indicates in samples per channel the amount of available space in the buffer.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SpaceAvail |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Write Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-write/attr190c.html language=enus -->
## TOPIC 01728: Relative To

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-write/attr190c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-write/attr190c.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the point in the buffer at which to write data. If you also specify an offset with Offset , the write operation begins at that offset relative to this point you select with this property. Remarks The following table lists the characteristics of this property. Short Name RelativeTo Data typ

### Relative To

Specifies the point in the buffer at which to write data. If you also specify an offset with 
 [Offset](/csh?context=nidaqmx_daqmxprop_attr190d)
 , the write operation begins at that offset relative to this point you select with this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | RelativeTo |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| First Sample | 10424 | Write samples relative to the first sample. |
| --- | --- | --- |
| Current Write Position | 10430 | Write samples relative to the current position in the buffer. |

Parent topic:

DAQmx Write Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-write/attr190d.html language=enus -->
## TOPIC 01729: Offset

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-write/attr190d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-write/attr190d.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in samples per channel an offset at which a write operation begins. This offset is relative to the location you specify with RelativeTo . Remarks The following table lists the characteristics of this property. Short Name Offset Data type ci32.png Permissions Read/Write Resettable True Sett

### Offset

Specifies in samples per channel an offset at which a write operation begins. This offset is relative to the location you specify with 
 [RelativeTo](/csh?context=nidaqmx_daqmxprop_attr190c)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Offset |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Write Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-write/attr192b.html language=enus -->
## TOPIC 01730: Status:Total Samples Per Channel Generated

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-write/attr192b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-write/attr192b.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the total number of samples generated by each channel in the task. This value is identical for all channels in the task. Remarks The following table lists the characteristics of this property. Short Name TotalSampPerChanGenerated Data type cdbl.png Permissions Read Only Resettable False Se

### Status:Total Samples Per Channel Generated

Indicates the total number of samples generated by each channel in the task. This value is identical for all channels in the task.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | TotalSampPerChanGenerated |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Write Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-write/attr217d.html language=enus -->
## TOPIC 01731: Advanced:Raw Data Width

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-write/attr217d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-write/attr217d.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in bytes the required size of a raw sample to write to the task. Remarks The following table lists the characteristics of this property. Short Name RawDataWidth Data type cu32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time En

### Advanced:Raw Data Width

Indicates in bytes the required size of a raw sample to write to the task.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | RawDataWidth |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Write Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-write/attr217e.html language=enus -->
## TOPIC 01732: Advanced:Number of Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-write/attr217e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-write/attr217e.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of channels that DAQmx Write writes to the task. This value is the number of channels in the task. Remarks The following table lists the characteristics of this property. Short Name NumChans Data type cu32.png Permissions Read Only Resettable False Settable While Task Is Running

### Advanced:Number of Channels

Indicates the number of channels that 
 [DAQmx Write](/csh?context=nidaqmx_lvdaqmx_mxwrite)
 writes to the task. This value is the number of channels in the task.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | NumChans |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Write Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-write/attr217f.html language=enus -->
## TOPIC 01733: Advanced:Digital Output:Number of Booleans Per Channel

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-write/attr217f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-write/attr217f.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of Boolean values expected per channel in a sample for line-based writes. This property is determined by the channel in the task with the most digital lines. If a channel has fewer lines than this number, NI-DAQmx ignores the extra Boolean values. Remarks The following table lis

### Advanced:Digital Output:Number of Booleans Per Channel

Indicates the number of Boolean values expected per channel in a sample for line-based writes. This property is determined by the channel in the task with the most digital lines. If a channel has fewer lines than this number, NI-DAQmx ignores the extra Boolean values.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DO.NumBooleansPerChan |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Write Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-write/attr22b1.html language=enus -->
## TOPIC 01734: Advanced:Wait Mode

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-write/attr22b1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-write/attr22b1.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how DAQmx Write waits for space to become available in the buffer. Remarks The following table lists the characteristics of this property. Short Name WaitMode Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engi

### Advanced:Wait Mode

Specifies how 
 [DAQmx Write](/csh?context=nidaqmx_lvdaqmx_mxwrite)
 waits for space to become available in the buffer.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | WaitMode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Poll | 12524 | Repeatedly check for available buffer space as fast as possible. This mode allows for the highest sampling rates at the expense of CPU efficiency. |
| --- | --- | --- |
| Yield | 12525 | Repeatedly check for available buffer space, but yield control to other threads after each check. This mode offers a balance between sampling rate and CPU efficiency. |
| Sleep | 12547 | Check for available buffer space once per the amount of time specified in SleepTime . |

Parent topic:

DAQmx Write Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-write/attr22b2.html language=enus -->
## TOPIC 01735: Advanced:Sleep Time

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-write/attr22b2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-write/attr22b2.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the amount of time to sleep after checking for available buffer space if WaitMode is Sleep. Remarks The following table lists the characteristics of this property. Short Name SleepTime Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running devic

### Advanced:Sleep Time

Specifies in seconds the amount of time to sleep after checking for available buffer space if 
 [WaitMode](/csh?context=nidaqmx_daqmxprop_attr22b1)
 is Sleep.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SleepTime |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Write Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-write/attr29e8.html language=enus -->
## TOPIC 01736: Status:Overcurrent:Overcurrent Channels Exist

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-write/attr29e8.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-write/attr29e8.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device(s) detected an overcurrent condition for any channel in the task. Reading this property clears the overcurrent status for all channels in the task. You must read this property before you read OvercurrentChans . Otherwise, you will receive an error. Remarks The following table

### Status:Overcurrent:Overcurrent Channels Exist

Indicates if the device(s) detected an 
 [overcurrent condition](/csh?context=nidaqmx_mxdevconsid_overcurrentdet)
 for any channel in the task. Reading this property clears the overcurrent status for all channels in the task. You must read this property before you read 
 [OvercurrentChans](/csh?context=nidaqmx_daqmxprop_attr29e9)
 . Otherwise, you will receive an error.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OvercurrentChansExist |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Write Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-write/attr29e9.html language=enus -->
## TOPIC 01737: Status:Overcurrent:Overcurrent Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-write/attr29e9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-write/attr29e9.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of names of any virtual channels in the task for which an overcurrent condition has been detected. You must read OvercurrentChansExist before you read this property. Otherwise, you will receive an error. Remarks The following table lists the characteristics of this property. Short N

### Status:Overcurrent:Overcurrent Channels

Indicates a 
 [list of names](/csh?context=nidaqmx_mxcncpts_physchannames)
 of any virtual channels in the task for which an 
 [overcurrent condition](/csh?context=nidaqmx_mxdevconsid_overcurrentdet)
 has been detected. You must read 
 [OvercurrentChansExist](/csh?context=nidaqmx_daqmxprop_attr29e8)
 before you read this property. Otherwise, you will receive an error.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OvercurrentChans |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Write Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-write/attr29ea.html language=enus -->
## TOPIC 01738: Status:Open Current Loop:Open Current Loop Channels Exist

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-write/attr29ea.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-write/attr29ea.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device(s) detected an open current loop for any channel in the task. Reading this property clears the open current loop status for all channels in the task. You must read this property before you read OpenCurrentLoopChans . Otherwise, you will receive an error. Remarks The following

### Status:Open Current Loop:Open Current Loop Channels Exist

Indicates if the device(s) detected an 
 [open current loop](/csh?context=nidaqmx_mxdevconsid_opencurrent)
 for any channel in the task. Reading this property clears the open current loop status for all channels in the task. You must read this property before you read 
 [OpenCurrentLoopChans](/csh?context=nidaqmx_daqmxprop_attr29eb)
 . Otherwise, you will receive an error.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OpenCurrentLoopChansExist |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Write Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-write/attr29eb.html language=enus -->
## TOPIC 01739: Status:Open Current Loop:Open Current Loop Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-write/attr29eb.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-write/attr29eb.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of names of any virtual channels in the task for which the device(s) detected an open current loop . You must read OpenCurrentLoopChansExist before you read this property. Otherwise, you will receive an error. Remarks The following table lists the characteristics of this property. S

### Status:Open Current Loop:Open Current Loop Channels

Indicates a 
 [list of names](/csh?context=nidaqmx_mxcncpts_physchannames)
 of any virtual channels in the task for which the device(s) detected an 
 [open current loop](/csh?context=nidaqmx_mxdevconsid_opencurrent)
 . You must read 
 [OpenCurrentLoopChansExist](/csh?context=nidaqmx_daqmxprop_attr29ea)
 before you read this property. Otherwise, you will receive an error.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OpenCurrentLoopChans |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Write Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-write/attr29ec.html language=enus -->
## TOPIC 01740: Status:Power Supply Fault:Power Supply Fault Channels Exist

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-write/attr29ec.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-write/attr29ec.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device(s) detected a power supply fault for any channel in the task. Reading this property clears the power supply fault status for all channels in the task. You must read this property before you read PowerSupplyFaultChans . Otherwise, you will receive an error. Remarks The followi

### Status:Power Supply Fault:Power Supply Fault Channels Exist

Indicates if the device(s) detected a 
 [power supply fault](/csh?context=nidaqmx_mxdevconsid_pwrsupfault)
 for any channel in the task. Reading this property clears the power supply fault status for all channels in the task. You must read this property before you read 
 [PowerSupplyFaultChans](/csh?context=nidaqmx_daqmxprop_attr29ed)
 . Otherwise, you will receive an error.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PowerSupplyFaultChansExist |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Write Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-write/attr29ed.html language=enus -->
## TOPIC 01741: Status:Power Supply Fault:Power Supply Fault Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-write/attr29ed.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-write/attr29ed.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of names of any virtual channels in the task that have a power supply fault . You must read PowerSupplyFaultChansExist before you read this property. Otherwise, you will receive an error. Remarks The following table lists the characteristics of this property. Short Name PowerSupplyF

### Status:Power Supply Fault:Power Supply Fault Channels

Indicates a 
 [list of names](/csh?context=nidaqmx_mxcncpts_physchannames)
 of any virtual channels in the task that have a 
 [power supply fault](/csh?context=nidaqmx_mxdevconsid_pwrsupfault)
 . You must read 
 [PowerSupplyFaultChansExist](/csh?context=nidaqmx_daqmxprop_attr29ec)
 before you read this property. Otherwise, you will receive an error.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PowerSupplyFaultChans |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Write Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-write/attr2a84.html language=enus -->
## TOPIC 01742: Status:Overtemperature:Overtemperature Channels Exist

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-write/attr2a84.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-write/attr2a84.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device(s) detected an overtemperature condition in any virtual channel in the task. Reading this property clears the overtemperature status for all channels in the task. You must read this property before you read OvertemperatureChans . Otherwise, you will receive an error. Remarks

### Status:Overtemperature:Overtemperature Channels Exist

Indicates if the device(s) detected an overtemperature condition in any virtual channel in the task. Reading this property clears the overtemperature status for all channels in the task. You must read this property before you read 
 [OvertemperatureChans](/csh?context=nidaqmx_daqmxprop_attr3083)
 . Otherwise, you will receive an error.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OvertemperatureChansExist |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Write Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-write/attr3053.html language=enus -->
## TOPIC 01743: Status:Accessory:Accessory Insertion or Removal Detected

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-write/attr3053.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-write/attr3053.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if any devices in the task detected the insertion or removal of an accessory since the task started. Reading this property clears the accessory change status for all channels in the task. You must read this property before you read DevsWithInsertedOrRemovedAccessories . Otherwise, you will

### Status:Accessory:Accessory Insertion or Removal Detected

Indicates if any devices in the task detected the insertion or removal of an accessory since the task started. Reading this property clears the accessory change status for all channels in the task. You must read this property before you read 
 [DevsWithInsertedOrRemovedAccessories](/csh?context=nidaqmx_daqmxprop_attr3054)
 . Otherwise, you will receive an error.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AccessoryInsertionOrRemovalDetected |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Write Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-write/attr3054.html language=enus -->
## TOPIC 01744: Status:Accessory:Devices with Inserted or Removed Accessories

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-write/attr3054.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-write/attr3054.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the names of any devices that detected the insertion or removal of an accessory since the task started. You must read AccessoryInsertionOrRemovalDetected before you read this property. Otherwise, you will receive an error. Remarks The following table lists the characteristics of this prope

### Status:Accessory:Devices with Inserted or Removed Accessories

Indicates the names of any devices that detected the insertion or removal of an accessory since the task started. You must read 
 [AccessoryInsertionOrRemovalDetected](/csh?context=nidaqmx_daqmxprop_attr3053)
 before you read this property. Otherwise, you will receive an error.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DevsWithInsertedOrRemovedAccessories |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Write Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-write/attr3083.html language=enus -->
## TOPIC 01745: Status:Overtemperature:Overtemperature Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-write/attr3083.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-write/attr3083.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of names of any overtemperature virtual channels. You must read OvertemperatureChansExist before you read this property. Otherwise, you will receive an error. The list of names may be empty if the device cannot determine the source of the overtemperature. Remarks The following table

### Status:Overtemperature:Overtemperature Channels

Indicates a list of names of any overtemperature virtual channels. You must read 
 [OvertemperatureChansExist](/csh?context=nidaqmx_daqmxprop_attr2a84)
 before you read this property. Otherwise, you will receive an error. The list of names may be empty if the device cannot determine the source of the overtemperature.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OvertemperatureChans |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Write Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-write/attr3084.html language=enus -->
## TOPIC 01746: Status:Overload:Overloaded Channels Exist

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-write/attr3084.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-write/attr3084.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device(s) detected an overload in any virtual channel in the task. Reading this property clears the overload status for all channels in the task. You must read this property before you read OverloadedChans . Otherwise, you will receive an error. Remarks The following table lists the

### Status:Overload:Overloaded Channels Exist

Indicates if the device(s) detected an overload in any virtual channel in the task. Reading this property clears the overload status for all channels in the task. You must read this property before you read 
 [OverloadedChans](/csh?context=nidaqmx_daqmxprop_attr3085)
 . Otherwise, you will receive an error.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OverloadedChansExist |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Write Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-write/attr3085.html language=enus -->
## TOPIC 01747: Status:Overload:Overloaded Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-write/attr3085.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-write/attr3085.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of names of any overloaded virtual channels in the task. You must read OverloadedChansExist before you read this property. Otherwise, you will receive an error. Remarks The following table lists the characteristics of this property. Short Name OverloadedChans Data type c1dstr.png Pe

### Status:Overload:Overloaded Channels

Indicates a list of names of any overloaded virtual channels in the task. You must read 
 [OverloadedChansExist](/csh?context=nidaqmx_daqmxprop_attr3084)
 before you read this property. Otherwise, you will receive an error.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OverloadedChans |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Write Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-write/attr30bb.html language=enus -->
## TOPIC 01748: Status:External Overvoltage:External Overvoltage Channels Exist

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-write/attr30bb.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-write/attr30bb.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device(s) detected an External Overvoltage condition for any channel in the task. Reading this property clears the External Overvoltage status for all channels in the task. You must read this property before you read External OvervoltageChans. Otherwise, you will receive an error. R

### Status:External Overvoltage:External Overvoltage Channels Exist

Indicates if the device(s) detected an External Overvoltage condition for any channel in the task. Reading this property clears the External Overvoltage status for all channels in the task. You must read this property before you read External OvervoltageChans. Otherwise, you will receive an error.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ExternalOvervoltageChansExist |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Write Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-write/attr30bc.html language=enus -->
## TOPIC 01749: Status:External Overvoltage:External Overvoltage Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-write/attr30bc.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-write/attr30bc.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of names of any virtual channels in the task for which an External Overvoltage condition has been detected. You must read External OvervoltageChansExist before you read this property. Otherwise, you will receive an error. Remarks The following table lists the characteristics of this

### Status:External Overvoltage:External Overvoltage Channels

Indicates a list of names of any virtual channels in the task for which an External Overvoltage condition has been detected. You must read External OvervoltageChansExist before you read this property. Otherwise, you will receive an error.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ExternalOvervoltageChans |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Write Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-write/attr313f.html language=enus -->
## TOPIC 01750: Status:Synchronization:Unlocked Channels Exist

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-write/attr313f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-write/attr313f.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the target is currently locked to the grand master. Devices may report PLL Unlock either during acquisition or after acquisition. Remarks The following table lists the characteristics of this property. Short Name Sync.UnlockedChansExist Data type cbool.png Permissions Read Only Res

### Status:Synchronization:Unlocked Channels Exist

Indicates whether the target is currently locked to the grand master. Devices may report PLL Unlock either during acquisition or after acquisition.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sync.UnlockedChansExist |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Write Properties
