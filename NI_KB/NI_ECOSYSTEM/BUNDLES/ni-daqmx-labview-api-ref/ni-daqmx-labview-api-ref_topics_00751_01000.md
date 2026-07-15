# NI DOCUMENT BUNDLE: ni-daqmx-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-daqmx-labview-api-ref start=751 end=1000 -->
<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2202.html language=enus -->
## TOPIC 00751: Counter Input:Position:B Input:Digital Filter:Timebase:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2202.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2202.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to use as the timebase of the pulse width filter. Remarks The following table lists the characteristics of this property. Short Name CI.Encoder.BInput.DigFltr.TimebaseSrc Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task I

### Counter Input:Position:B Input:Digital Filter:Timebase:Source

Specifies the input 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 of the signal to use as the timebase of the pulse width filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Encoder.BInput.DigFltr.TimebaseSrc |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2203.html language=enus -->
## TOPIC 00752: Counter Input:Position:B Input:Digital Filter:Timebase:Rate

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2203.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2203.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. Remarks The following table lists the characteristics of this property. Short Name CI.Encoder.BInput.DigFltr.TimebaseRate Data type cdbl.png Permissions Read/Write Resettable

### Counter Input:Position:B Input:Digital Filter:Timebase:Rate

Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Encoder.BInput.DigFltr.TimebaseRate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2204.html language=enus -->
## TOPIC 00753: Counter Input:Position:B Input:Digital Synchronization:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2204.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2204.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. This property does not affect the minimum pulse width recognized by the device, but setting this property to TRUE does limit the speed at which the device recognizes transitions to less

### Counter Input:Position:B Input:Digital Synchronization:Enable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

This property does not affect the minimum pulse width recognized by the device, 
but setting this property to TRUE does limit the speed at which the device recognizes transitions 
to less than the frequency of the internal timebase.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Encoder.BInput.DigSync.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2205.html language=enus -->
## TOPIC 00754: Counter Input:Position:Z Input:Digital Filter:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2205.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2205.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply the pulse width filter to the signal. Remarks The following table lists the characteristics of this property. Short Name CI.Encoder.ZInput.DigFltr.Enable Data type cbool.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in

### Counter Input:Position:Z Input:Digital Filter:Enable

Specifies whether to apply the pulse width 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 to the signal.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Encoder.ZInput.DigFltr.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2206.html language=enus -->
## TOPIC 00755: Counter Input:Position:Z Input:Digital Filter:Minimum Pulse Width

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2206.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2206.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. Remarks The following table lists the characteristics of this property. Short Name CI.Encoder.ZInput.DigFltr.MinPulseWidth Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Avai

### Counter Input:Position:Z Input:Digital Filter:Minimum Pulse Width

Specifies in seconds the minimum pulse width the 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 recognizes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Encoder.ZInput.DigFltr.MinPulseWidth |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2207.html language=enus -->
## TOPIC 00756: Counter Input:Position:Z Input:Digital Filter:Timebase:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2207.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2207.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to use as the timebase of the pulse width filter. Remarks The following table lists the characteristics of this property. Short Name CI.Encoder.ZInput.DigFltr.TimebaseSrc Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task I

### Counter Input:Position:Z Input:Digital Filter:Timebase:Source

Specifies the input 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 of the signal to use as the timebase of the pulse width filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Encoder.ZInput.DigFltr.TimebaseSrc |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2208.html language=enus -->
## TOPIC 00757: Counter Input:Position:Z Input:Digital Filter:Timebase:Rate

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2208.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2208.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. Remarks The following table lists the characteristics of this property. Short Name CI.Encoder.ZInput.DigFltr.TimebaseRate Data type cdbl.png Permissions Read/Write Resettable

### Counter Input:Position:Z Input:Digital Filter:Timebase:Rate

Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Encoder.ZInput.DigFltr.TimebaseRate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2209.html language=enus -->
## TOPIC 00758: Counter Input:Position:Z Input:Digital Synchronization:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2209.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2209.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. This property does not affect the minimum pulse width recognized by the device, but setting this property to TRUE does limit the speed at which the device recognizes transitions to less

### Counter Input:Position:Z Input:Digital Synchronization:Enable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

This property does not affect the minimum pulse width recognized by the device, 
but setting this property to TRUE does limit the speed at which the device recognizes transitions 
to less than the frequency of the internal timebase.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Encoder.ZInput.DigSync.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr220a.html language=enus -->
## TOPIC 00759: Counter Input:Pulse Width:Input:Digital Filter:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr220a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr220a.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply the pulse width filter to the signal. Remarks The following table lists the characteristics of this property. Short Name CI.PulseWidth.DigFltr.Enable Data type cbool.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-

### Counter Input:Pulse Width:Input:Digital Filter:Enable

Specifies whether to apply the pulse width 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 to the signal.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.PulseWidth.DigFltr.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr220b.html language=enus -->
## TOPIC 00760: Counter Input:Pulse Width:Input:Digital Filter:Minimum Pulse Width

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr220b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr220b.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. Remarks The following table lists the characteristics of this property. Short Name CI.PulseWidth.DigFltr.MinPulseWidth Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Availabl

### Counter Input:Pulse Width:Input:Digital Filter:Minimum Pulse Width

Specifies in seconds the minimum pulse width the 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 recognizes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.PulseWidth.DigFltr.MinPulseWidth |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr220c.html language=enus -->
## TOPIC 00761: Counter Input:Pulse Width:Input:Digital Filter:Timebase:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr220c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr220c.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to use as the timebase of the pulse width filter. Remarks The following table lists the characteristics of this property. Short Name CI.PulseWidth.DigFltr.TimebaseSrc Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Ru

### Counter Input:Pulse Width:Input:Digital Filter:Timebase:Source

Specifies the input 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 of the signal to use as the timebase of the pulse width filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.PulseWidth.DigFltr.TimebaseSrc |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr220d.html language=enus -->
## TOPIC 00762: Counter Input:Pulse Width:Input:Digital Filter:Timebase:Rate

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr220d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr220d.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. Remarks The following table lists the characteristics of this property. Short Name CI.PulseWidth.DigFltr.TimebaseRate Data type cdbl.png Permissions Read/Write Resettable True

### Counter Input:Pulse Width:Input:Digital Filter:Timebase:Rate

Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.PulseWidth.DigFltr.TimebaseRate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr220e.html language=enus -->
## TOPIC 00763: Counter Input:Pulse Width:Input:Digital Synchronization:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr220e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr220e.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. This property does not affect the minimum pulse width recognized by the device, but setting this property to TRUE does limit the speed at which the device recognizes transitions to less

### Counter Input:Pulse Width:Input:Digital Synchronization:Enable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

This property does not affect the minimum pulse width recognized by the device, 
but setting this property to TRUE does limit the speed at which the device recognizes transitions 
to less than the frequency of the internal timebase.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.PulseWidth.DigSync.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr220f.html language=enus -->
## TOPIC 00764: Counter Input:Two Edge Separation:First:Input:Digital Filter:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr220f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr220f.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply the pulse width filter to the signal. Remarks The following table lists the characteristics of this property. Short Name CI.TwoEdgeSep.First.DigFltr.Enable Data type cbool.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available i

### Counter Input:Two Edge Separation:First:Input:Digital Filter:Enable

Specifies whether to apply the pulse width 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 to the signal.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.TwoEdgeSep.First.DigFltr.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2210.html language=enus -->
## TOPIC 00765: Counter Input:Two Edge Separation:First:Input:Digital Filter:Minimum Pulse Width

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2210.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2210.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. Remarks The following table lists the characteristics of this property. Short Name CI.TwoEdgeSep.First.DigFltr.MinPulseWidth Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Av

### Counter Input:Two Edge Separation:First:Input:Digital Filter:Minimum Pulse Width

Specifies in seconds the minimum pulse width the 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 recognizes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.TwoEdgeSep.First.DigFltr.MinPulseWidth |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2211.html language=enus -->
## TOPIC 00766: Counter Input:Two Edge Separation:First:Input:Digital Filter:Timebase:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2211.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2211.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to use as the timebase of the pulse width filter. Remarks The following table lists the characteristics of this property. Short Name CI.TwoEdgeSep.First.DigFltr.TimebaseSrc Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task

### Counter Input:Two Edge Separation:First:Input:Digital Filter:Timebase:Source

Specifies the input 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 of the signal to use as the timebase of the pulse width filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.TwoEdgeSep.First.DigFltr.TimebaseSrc |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2212.html language=enus -->
## TOPIC 00767: Counter Input:Two Edge Separation:First:Input:Digital Filter:Timebase:Rate

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2212.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2212.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. Remarks The following table lists the characteristics of this property. Short Name CI.TwoEdgeSep.First.DigFltr.TimebaseRate Data type cdbl.png Permissions Read/Write Resettabl

### Counter Input:Two Edge Separation:First:Input:Digital Filter:Timebase:Rate

Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.TwoEdgeSep.First.DigFltr.TimebaseRate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2213.html language=enus -->
## TOPIC 00768: Counter Input:Two Edge Separation:First:Input:Digital Synchronization:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2213.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2213.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. This property does not affect the minimum pulse width recognized by the device, but setting this property to TRUE does limit the speed at which the device recognizes transitions to less

### Counter Input:Two Edge Separation:First:Input:Digital Synchronization:Enable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

This property does not affect the minimum pulse width recognized by the device, 
but setting this property to TRUE does limit the speed at which the device recognizes transitions 
to less than the frequency of the internal timebase.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.TwoEdgeSep.First.DigSync.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2214.html language=enus -->
## TOPIC 00769: Counter Input:Two Edge Separation:Second:Input:Digital Filter:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2214.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2214.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply the pulse width filter to the signal. Remarks The following table lists the characteristics of this property. Short Name CI.TwoEdgeSep.Second.DigFltr.Enable Data type cbool.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available

### Counter Input:Two Edge Separation:Second:Input:Digital Filter:Enable

Specifies whether to apply the pulse width 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 to the signal.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.TwoEdgeSep.Second.DigFltr.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2215.html language=enus -->
## TOPIC 00770: Counter Input:Two Edge Separation:Second:Input:Digital Filter:Minimum Pulse Width

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2215.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2215.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. Remarks The following table lists the characteristics of this property. Short Name CI.TwoEdgeSep.Second.DigFltr.MinPulseWidth Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific A

### Counter Input:Two Edge Separation:Second:Input:Digital Filter:Minimum Pulse Width

Specifies in seconds the minimum pulse width the 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 recognizes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.TwoEdgeSep.Second.DigFltr.MinPulseWidth |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2216.html language=enus -->
## TOPIC 00771: Counter Input:Two Edge Separation:Second:Input:Digital Filter:Timebase:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2216.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2216.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to use as the timebase of the pulse width filter. Remarks The following table lists the characteristics of this property. Short Name CI.TwoEdgeSep.Second.DigFltr.TimebaseSrc Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Tas

### Counter Input:Two Edge Separation:Second:Input:Digital Filter:Timebase:Source

Specifies the input 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 of the signal to use as the timebase of the pulse width filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.TwoEdgeSep.Second.DigFltr.TimebaseSrc |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2217.html language=enus -->
## TOPIC 00772: Counter Input:Two Edge Separation:Second:Input:Digital Filter:Timebase:Rate

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2217.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2217.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. Remarks The following table lists the characteristics of this property. Short Name CI.TwoEdgeSep.Second.DigFltr.TimebaseRate Data type cdbl.png Permissions Read/Write Resettab

### Counter Input:Two Edge Separation:Second:Input:Digital Filter:Timebase:Rate

Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.TwoEdgeSep.Second.DigFltr.TimebaseRate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2218.html language=enus -->
## TOPIC 00773: Counter Input:Two Edge Separation:Second:Input:Digital Synchronization:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2218.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2218.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. This property does not affect the minimum pulse width recognized by the device, but setting this property to TRUE does limit the speed at which the device recognizes transitions to less

### Counter Input:Two Edge Separation:Second:Input:Digital Synchronization:Enable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

This property does not affect the minimum pulse width recognized by the device, 
but setting this property to TRUE does limit the speed at which the device recognizes transitions 
to less than the frequency of the internal timebase.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.TwoEdgeSep.Second.DigSync.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2219.html language=enus -->
## TOPIC 00774: Counter Input:Semi-Period:Input:Digital Filter:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2219.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2219.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply the pulse width filter to the signal. Remarks The following table lists the characteristics of this property. Short Name CI.SemiPeriod.DigFltr.Enable Data type cbool.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-

### Counter Input:Semi-Period:Input:Digital Filter:Enable

Specifies whether to apply the pulse width 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 to the signal.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.SemiPeriod.DigFltr.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr221a.html language=enus -->
## TOPIC 00775: Counter Input:Semi-Period:Input:Digital Filter:Minimum Pulse Width

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr221a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr221a.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. Remarks The following table lists the characteristics of this property. Short Name CI.SemiPeriod.DigFltr.MinPulseWidth Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Availabl

### Counter Input:Semi-Period:Input:Digital Filter:Minimum Pulse Width

Specifies in seconds the minimum pulse width the 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 recognizes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.SemiPeriod.DigFltr.MinPulseWidth |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr221b.html language=enus -->
## TOPIC 00776: Counter Input:Semi-Period:Input:Digital Filter:Timebase:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr221b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr221b.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to use as the timebase of the pulse width filter. Remarks The following table lists the characteristics of this property. Short Name CI.SemiPeriod.DigFltr.TimebaseSrc Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Ru

### Counter Input:Semi-Period:Input:Digital Filter:Timebase:Source

Specifies the input 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 of the signal to use as the timebase of the pulse width filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.SemiPeriod.DigFltr.TimebaseSrc |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr221c.html language=enus -->
## TOPIC 00777: Counter Input:Semi-Period:Input:Digital Filter:Timebase:Rate

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr221c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr221c.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. Remarks The following table lists the characteristics of this property. Short Name CI.SemiPeriod.DigFltr.TimebaseRate Data type cdbl.png Permissions Read/Write Resettable True

### Counter Input:Semi-Period:Input:Digital Filter:Timebase:Rate

Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.SemiPeriod.DigFltr.TimebaseRate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr221d.html language=enus -->
## TOPIC 00778: Counter Input:Semi-Period:Input:Digital Synchronization:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr221d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr221d.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. This property does not affect the minimum pulse width recognized by the device, but setting this property to TRUE does limit the speed at which the device recognizes transitions to less

### Counter Input:Semi-Period:Input:Digital Synchronization:Enable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

This property does not affect the minimum pulse width recognized by the device, 
but setting this property to TRUE does limit the speed at which the device recognizes transitions 
to less than the frequency of the internal timebase.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.SemiPeriod.DigSync.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2239.html language=enus -->
## TOPIC 00779: Counter Input:General Properties:More:Advanced:Prescaler

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2239.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2239.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the divisor to apply to the signal you connect to the counter source terminal. Scaled data that you read takes this setting into account. You should use a prescaler only when you connect an external signal to the counter source terminal and when that signal has a higher frequency than the

### Counter Input:General Properties:More:Advanced:Prescaler

Specifies the divisor to apply to the signal you connect to the counter source terminal. Scaled data that you read takes this setting into account. You should use a prescaler only when you connect an external signal to the counter source terminal and when that signal has a higher frequency than the fastest onboard timebase. Setting this value disables duplicate count prevention unless you explicitly set 
 [CI.DupCountPrevention](/csh?context=nidaqmx_daqmxprop_attr21ac)
 to TRUE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Prescaler |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr223a.html language=enus -->
## TOPIC 00780: Analog Input:Sound Pressure:Maximum Sound Pressure Level

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr223a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr223a.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum instantaneous sound pressure level you expect to measure. This value is in decibels, referenced to 20 micropascals. NI-DAQmx uses the maximum sound pressure level to calculate values in pascals for AI.Max and AI.Min for the channel. Remarks The following table lists the charact

### Analog Input:Sound Pressure:Maximum Sound Pressure Level

Specifies the maximum instantaneous sound pressure level you expect to measure. This value is in decibels, referenced to 20 micropascals. NI-DAQmx uses the maximum sound pressure level to calculate values in pascals for 
 [AI.Max](/csh?context=nidaqmx_daqmxprop_attr17dd)
 and 
 [AI.Min](/csh?context=nidaqmx_daqmxprop_attr17de)
 for the channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.SoundPressure.MaxSoundPressureLvl |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2240.html language=enus -->
## TOPIC 00781: Analog Output:General Properties:Output Configuration:Idle Output Behavior

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2240.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2240.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the state of the channel when no generation is in progress. Remarks The following table lists the characteristics of this property. Short Name AO.IdleOutputBehavior Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Tim

### Analog Output:General Properties:Output Configuration:Idle Output Behavior

Specifies the state of the channel when no generation is in progress.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO.IdleOutputBehavior |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Zero Volts | 12526 | Generate 0 V. |
| --- | --- | --- |
| High-Impedance | 12527 | Set the channel to high-impedance, effectively disconnecting the analog output circuitry from the I/O connector. |
| Maintain Existing Value | 12528 | Continue generating the current value. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2241.html language=enus -->
## TOPIC 00782: Analog Output:General Properties:Advanced:Enhanced Image Rejection Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2241.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2241.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the DAC interpolation filter. Disable the interpolation filter to improve DAC signal-to-noise ratio at the expense of degraded image rejection. Remarks The following table lists the characteristics of this property. Short Name AO.EnhancedImageRejectionEnable Data type cbo

### Analog Output:General Properties:Advanced:Enhanced Image Rejection Enable

Specifies whether to enable the DAC interpolation filter. Disable the interpolation filter to improve DAC signal-to-noise ratio at the expense of degraded image rejection.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO.EnhancedImageRejectionEnable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2252.html language=enus -->
## TOPIC 00783: Analog Output:General Properties:DAC:Reference Voltage:External Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2252.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2252.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source of the DAC reference voltage if AO.DAC.Ref.Src is External. The valid sources for this signal vary by device . Remarks The following table lists the characteristics of this property. Short Name AO.DAC.Ref.ExtSrc Data type cstr.png Permissions Read/Write Resettable True Settable

### Analog Output:General Properties:DAC:Reference Voltage:External Source

Specifies the source of the DAC reference voltage if 
 [AO.DAC.Ref.Src](/csh?context=nidaqmx_daqmxprop_attr132)
 is External. The valid sources for this signal 
 [vary by device](/csh?context=nidaqmx_mxdevconsid_mseriesextrefsrc)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO.DAC.Ref.ExtSrc |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2253.html language=enus -->
## TOPIC 00784: Analog Output:General Properties:DAC:Offset Voltage:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2253.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2253.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source of the DAC offset voltage. The value of this voltage source determines the full-scale value of the DAC. Remarks The following table lists the characteristics of this property. Short Name AO.DAC.Offset.Src Data type ci32.png Permissions Read/Write Resettable True Settable While T

### Analog Output:General Properties:DAC:Offset Voltage:Source

Specifies the source of the DAC offset voltage. The value of this voltage source determines the full-scale value of the DAC.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO.DAC.Offset.Src |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Internal | 10200 | Internal to the device. |
| --- | --- | --- |
| External | 10167 | External to the device. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2254.html language=enus -->
## TOPIC 00785: Analog Output:General Properties:DAC:Offset Voltage:External Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2254.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2254.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source of the DAC offset voltage if AO.DAC.Offset.Src is External. The valid sources for this signal vary by device . Remarks The following table lists the characteristics of this property. Short Name AO.DAC.Offset.ExtSrc Data type cstr.png Permissions Read/Write Resettable True Settab

### Analog Output:General Properties:DAC:Offset Voltage:External Source

Specifies the source of the DAC offset voltage if 
 [AO.DAC.Offset.Src](/csh?context=nidaqmx_daqmxprop_attr2253)
 is External. The valid sources for this signal 
 [vary by device](/csh?context=nidaqmx_mxdevconsid_mseriesextrefsrc)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO.DAC.Offset.ExtSrc |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2255.html language=enus -->
## TOPIC 00786: Analog Output:General Properties:DAC:Offset Voltage:Value

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2255.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2255.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in volts the value of the DAC offset voltage. To achieve best accuracy, the DAC offset value should be hand calibrated. Remarks The following table lists the characteristics of this property. Short Name AO.DAC.Offset.Val Data type cdbl.png Permissions Read/Write Resettable True Settable Wh

### Analog Output:General Properties:DAC:Offset Voltage:Value

Specifies in volts the value of the DAC offset voltage. To achieve best accuracy, the DAC offset value should be hand calibrated.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO.DAC.Offset.Val |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2263.html language=enus -->
## TOPIC 00787: Digital Input:General Properties:Advanced:Data Transfer and Memory:Data Transfer Mechanism

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2263.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2263.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the data transfer mode for the device. Remarks The following table lists the characteristics of this property. Short Name DI.DataXferMech Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True DMA 10054 Dir

### Digital Input:General Properties:Advanced:Data Transfer and Memory:Data Transfer Mechanism

Specifies the data transfer mode for the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DI.DataXferMech |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| DMA | 10054 | Direct Memory Access. Data transfers take place independently from the application. |
| --- | --- | --- |
| Interrupts | 10204 | Data transfers take place independently from the application. Using interrupts increases CPU usage because the CPU must service interrupt requests. Typically, you should use interrupts if the device is out of DMA channels. |
| Programmed I/O | 10264 | Data transfers take place when you call DAQmx Read or DAQmx Write . |
| USB Bulk | 12590 | Data transfers take place independently from the application using a USB bulk pipe. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2264.html language=enus -->
## TOPIC 00788: Digital Input:General Properties:Advanced:Data Transfer and Memory:Data Transfer Request Condition

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2264.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2264.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies under what condition to transfer data from the onboard memory of the device to the buffer. Remarks The following table lists the characteristics of this property. Short Name DI.DataXferReqCond Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-s

### Digital Input:General Properties:Advanced:Data Transfer and Memory:Data Transfer Request Condition

Specifies under what condition to transfer data from the onboard memory of the device to the buffer.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DI.DataXferReqCond |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Onboard Memory More than Half Full | 10237 | Transfer data from the device when more than half of the onboard memory of the device fills. |
| --- | --- | --- |
| Onboard Memory Not Empty | 10241 | Transfer data from the device when there is data in the onboard memory. |
| Onboard Memory Custom Threshold | 12577 | Transfer data from the device when the number of samples specified with AI.DataXferCustomThreshold are in the device FIFO. |
| When Acquisition Complete | 12546 | Transfer data when the acquisition is complete. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2265.html language=enus -->
## TOPIC 00789: Digital Output:General Properties:Advanced:Data Transfer and Memory:Use Only Onboard Memory

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2265.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2265.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to write samples directly to the onboard memory of the device, bypassing the memory buffer. Generally, you cannot update onboard memory after you start the task. Onboard memory includes data FIFOs. Remarks The following table lists the characteristics of this property. Short Name D

### Digital Output:General Properties:Advanced:Data Transfer and Memory:Use Only Onboard Memory

Specifies whether to write samples directly to the onboard memory of the device, bypassing the memory buffer. Generally, you cannot update onboard memory after you start the task. Onboard memory includes data FIFOs.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DO.UseOnlyOnBrdMem |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2266.html language=enus -->
## TOPIC 00790: Digital Output:General Properties:Advanced:Data Transfer and Memory:Data Transfer Mechanism

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2266.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2266.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the data transfer mode for the device. Remarks The following table lists the characteristics of this property. Short Name DO.DataXferMech Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True DMA 10054 Dir

### Digital Output:General Properties:Advanced:Data Transfer and Memory:Data Transfer Mechanism

Specifies the data transfer mode for the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DO.DataXferMech |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| DMA | 10054 | Direct Memory Access. Data transfers take place independently from the application. |
| --- | --- | --- |
| Interrupts | 10204 | Data transfers take place independently from the application. Using interrupts increases CPU usage because the CPU must service interrupt requests. Typically, you should use interrupts if the device is out of DMA channels. |
| Programmed I/O | 10264 | Data transfers take place when you call DAQmx Read or DAQmx Write . |
| USB Bulk | 12590 | Data transfers take place independently from the application using a USB bulk pipe. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2267.html language=enus -->
## TOPIC 00791: Digital Output:General Properties:Advanced:Data Transfer and Memory:Data Transfer Request Condition

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2267.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2267.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies under what condition to transfer data from the buffer to the onboard memory of the device. Remarks The following table lists the characteristics of this property. Short Name DO.DataXferReqCond Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-s

### Digital Output:General Properties:Advanced:Data Transfer and Memory:Data Transfer Request Condition

Specifies under what condition to transfer data from the buffer to the onboard memory of the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DO.DataXferReqCond |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Onboard Memory Empty | 10235 | Transfer data to the device only when there is no data in the onboard memory of the device. |
| --- | --- | --- |
| Onboard Memory Half Full or Less | 10239 | Transfer data to the device any time the onboard memory is less than half full. |
| Onboard Memory Less than Full | 10242 | Transfer data to the device any time the onboard memory of the device is not full. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr226d.html language=enus -->
## TOPIC 00792: Counter Output:General Properties:More:Advanced:Prescaler

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr226d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr226d.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the divisor to apply to the signal you connect to the counter source terminal. Pulse generations defined by frequency or time take this setting into account, but pulse generations defined by ticks do not. You should use a prescaler only when you connect an external signal to the counter so

### Counter Output:General Properties:More:Advanced:Prescaler

Specifies the divisor to apply to the signal you connect to the counter source terminal. Pulse generations defined by frequency or time take this setting into account, but pulse generations defined by ticks do not. You should use a prescaler only when you connect an external signal to the counter source terminal and when that signal has a higher frequency than the fastest onboard timebase.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CO.Prescaler |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2271.html language=enus -->
## TOPIC 00793: Counter Input:General Properties:Counter Timebase:Digital Filter:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2271.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2271.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply the pulse width filter to the signal. Remarks The following table lists the characteristics of this property. Short Name CI.CtrTimebase.DigFltr.Enable Data type cbool.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run

### Counter Input:General Properties:Counter Timebase:Digital Filter:Enable

Specifies whether to apply the pulse width 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 to the signal.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.CtrTimebase.DigFltr.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2272.html language=enus -->
## TOPIC 00794: Counter Input:General Properties:Counter Timebase:Digital Filter:Minimum Pulse Width

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2272.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2272.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. Remarks The following table lists the characteristics of this property. Short Name CI.CtrTimebase.DigFltr.MinPulseWidth Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Availab

### Counter Input:General Properties:Counter Timebase:Digital Filter:Minimum Pulse Width

Specifies in seconds the minimum pulse width the 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 recognizes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.CtrTimebase.DigFltr.MinPulseWidth |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2273.html language=enus -->
## TOPIC 00795: Counter Input:General Properties:Counter Timebase:Digital Filter:Timebase:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2273.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2273.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to use as the timebase of the pulse width filter. Remarks The following table lists the characteristics of this property. Short Name CI.CtrTimebase.DigFltr.TimebaseSrc Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is R

### Counter Input:General Properties:Counter Timebase:Digital Filter:Timebase:Source

Specifies the input 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 of the signal to use as the timebase of the pulse width filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.CtrTimebase.DigFltr.TimebaseSrc |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2274.html language=enus -->
## TOPIC 00796: Counter Input:General Properties:Counter Timebase:Digital Filter:Timebase:Rate

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2274.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2274.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. Remarks The following table lists the characteristics of this property. Short Name CI.CtrTimebase.DigFltr.TimebaseRate Data type cdbl.png Permissions Read/Write Resettable Tru

### Counter Input:General Properties:Counter Timebase:Digital Filter:Timebase:Rate

Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.CtrTimebase.DigFltr.TimebaseRate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2275.html language=enus -->
## TOPIC 00797: Counter Input:General Properties:Counter Timebase:Digital Synchronization:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2275.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2275.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. This property does not affect the minimum pulse width recognized by the device, but setting this property to TRUE does limit the speed at which the device recognizes transitions to less

### Counter Input:General Properties:Counter Timebase:Digital Synchronization:Enable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

This property does not affect the minimum pulse width recognized by the device, 
but setting this property to TRUE does limit the speed at which the device recognizes transitions 
to less than the frequency of the internal timebase.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.CtrTimebase.DigSync.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2276.html language=enus -->
## TOPIC 00798: Counter Output:General Properties:Counter Timebase:Digital Filter:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2276.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2276.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply the pulse width filter to the signal. Remarks The following table lists the characteristics of this property. Short Name CO.CtrTimebase.DigFltr.Enable Data type cbool.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run

### Counter Output:General Properties:Counter Timebase:Digital Filter:Enable

Specifies whether to apply the pulse width 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 to the signal.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CO.CtrTimebase.DigFltr.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2277.html language=enus -->
## TOPIC 00799: Counter Output:General Properties:Counter Timebase:Digital Filter:Minimum Pulse Width

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2277.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2277.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. Remarks The following table lists the characteristics of this property. Short Name CO.CtrTimebase.DigFltr.MinPulseWidth Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Availab

### Counter Output:General Properties:Counter Timebase:Digital Filter:Minimum Pulse Width

Specifies in seconds the minimum pulse width the 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 recognizes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CO.CtrTimebase.DigFltr.MinPulseWidth |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2278.html language=enus -->
## TOPIC 00800: Counter Output:General Properties:Counter Timebase:Digital Filter:Timebase:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2278.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2278.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to use as the timebase of the pulse width filter. Remarks The following table lists the characteristics of this property. Short Name CO.CtrTimebase.DigFltr.TimebaseSrc Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is R

### Counter Output:General Properties:Counter Timebase:Digital Filter:Timebase:Source

Specifies the input 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 of the signal to use as the timebase of the pulse width filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CO.CtrTimebase.DigFltr.TimebaseSrc |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2279.html language=enus -->
## TOPIC 00801: Counter Output:General Properties:Counter Timebase:Digital Filter:Timebase:Rate

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2279.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2279.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. Remarks The following table lists the characteristics of this property. Short Name CO.CtrTimebase.DigFltr.TimebaseRate Data type cdbl.png Permissions Read/Write Resettable Tru

### Counter Output:General Properties:Counter Timebase:Digital Filter:Timebase:Rate

Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CO.CtrTimebase.DigFltr.TimebaseRate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr227a.html language=enus -->
## TOPIC 00802: Counter Output:General Properties:Counter Timebase:Digital Synchronization:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr227a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr227a.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. This property does not affect the minimum pulse width recognized by the device, but setting this property to TRUE does limit the speed at which the device recognizes transitions to less

### Counter Output:General Properties:Counter Timebase:Digital Synchronization:Enable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

This property does not affect the minimum pulse width recognized by the device, 
but setting this property to TRUE does limit the speed at which the device recognizes transitions 
to less than the frequency of the internal timebase.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CO.CtrTimebase.DigSync.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2294.html language=enus -->
## TOPIC 00803: Analog Input:General Properties:Advanced:Enhanced Alias Rejection Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2294.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2294.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable enhanced alias rejection . Leave this property set to the default value for most applications. Remarks The following table lists the characteristics of this property. Short Name AI.EnhancedAliasRejectionEnable Data type cbool.png Permissions Read/Write Resettable True Set

### Analog Input:General Properties:Advanced:Enhanced Alias Rejection Enable

Specifies whether to enable 
 [enhanced alias rejection](/csh?context=nidaqmx_mxdevconsid_enhancedaliasrej)
 . Leave this property set to the default value for most applications.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.EnhancedAliasRejectionEnable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2297.html language=enus -->
## TOPIC 00804: Analog Input:General Properties:Channel Calibration:Has Valid Calibration Information

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2297.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2297.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the channel has calibration information. Remarks The following table lists the characteristics of this property. Short Name AI.ChanCal.HasValidCalInfo Data type cbool.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine T

### Analog Input:General Properties:Channel Calibration:Has Valid Calibration Information

Indicates if the channel has calibration information.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.ChanCal.HasValidCalInfo |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2298.html language=enus -->
## TOPIC 00805: Analog Input:General Properties:Channel Calibration:Enable Calibration

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2298.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2298.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the channel calibration associated with the channel. Remarks The following table lists the characteristics of this property. Short Name AI.ChanCal.EnableCal Data type cbool.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available

### Analog Input:General Properties:Channel Calibration:Enable Calibration

Specifies whether to enable the channel calibration associated with the channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.ChanCal.EnableCal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2299.html language=enus -->
## TOPIC 00806: Analog Input:General Properties:Channel Calibration:Apply Calibration If Expired

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2299.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2299.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply the channel calibration to the channel after the expiration date has passed. Remarks The following table lists the characteristics of this property. Short Name AI.ChanCal.ApplyCalIfExp Data type cbool.png Permissions Read/Write Resettable True Settable While Task Is Runnin

### Analog Input:General Properties:Channel Calibration:Apply Calibration If Expired

Specifies whether to apply the channel calibration to the channel after the expiration date has passed.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.ChanCal.ApplyCalIfExp |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr229a.html language=enus -->
## TOPIC 00807: Analog Input:General Properties:Channel Calibration:Calibration Date

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr229a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr229a.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the last date and time that the channel underwent a channel calibration. Remarks The following table lists the characteristics of this property. Short Name AI.ChanCal.CalDate Data type catrn.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available

### Analog Input:General Properties:Channel Calibration:Calibration Date

Specifies the last date and time that the channel underwent a channel calibration.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.ChanCal.CalDate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr229b.html language=enus -->
## TOPIC 00808: Analog Input:General Properties:Channel Calibration:Expiration Date

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr229b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr229b.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the date and time that the channel calibration expires. Remarks The following table lists the characteristics of this property. Short Name AI.ChanCal.ExpDate Data type catrn.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engi

### Analog Input:General Properties:Channel Calibration:Expiration Date

Specifies the date and time that the channel calibration expires.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.ChanCal.ExpDate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr229c.html language=enus -->
## TOPIC 00809: Analog Input:General Properties:Channel Calibration:Scaling Parameters:Scale Type

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr229c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr229c.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the method or equation form that the calibration scale uses. Remarks The following table lists the characteristics of this property. Short Name AI.ChanCal.ScaleType Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Tim

### Analog Input:General Properties:Channel Calibration:Scaling Parameters:Scale Type

Specifies the method or equation form that the calibration scale uses.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.ChanCal.ScaleType |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Polynomial | 10449 | Scale values by using an Nth order polynomial equation. |
| --- | --- | --- |
| Table | 10450 | Map an array of prescaled values to an array of corresponding scaled values, with all other values scaled proportionally. |
| None | 10230 |  |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr229d.html language=enus -->
## TOPIC 00810: Analog Input:General Properties:Channel Calibration:Scaling Parameters:Table:Pre-Scaled Values

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr229d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr229d.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference values collected when calibrating the channel. Remarks The following table lists the characteristics of this property. Short Name AI.ChanCal.Table.PreScaledVals Data type c1ddbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Availabl

### Analog Input:General Properties:Channel Calibration:Scaling Parameters:Table:Pre-Scaled Values

Specifies the reference values collected when calibrating the channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.ChanCal.Table.PreScaledVals |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr229e.html language=enus -->
## TOPIC 00811: Analog Input:General Properties:Channel Calibration:Scaling Parameters:Table:Scaled Values

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr229e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr229e.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the acquired values collected when calibrating the channel. Remarks The following table lists the characteristics of this property. Short Name AI.ChanCal.Table.ScaledVals Data type c1ddbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in

### Analog Input:General Properties:Channel Calibration:Scaling Parameters:Table:Scaled Values

Specifies the acquired values collected when calibrating the channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.ChanCal.Table.ScaledVals |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr229f.html language=enus -->
## TOPIC 00812: Analog Input:General Properties:Channel Calibration:Scaling Parameters:Polynomial:Forward Coefficients

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr229f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr229f.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the forward polynomial values used for calibrating the channel. Remarks The following table lists the characteristics of this property. Short Name AI.ChanCal.Poly.ForwardCoeff Data type c1ddbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Availab

### Analog Input:General Properties:Channel Calibration:Scaling Parameters:Polynomial:Forward Coefficients

Specifies the forward polynomial values used for calibrating the channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.ChanCal.Poly.ForwardCoeff |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr22a0.html language=enus -->
## TOPIC 00813: Analog Input:General Properties:Channel Calibration:Scaling Parameters:Polynomial:Reverse Coefficients

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr22a0.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr22a0.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reverse polynomial values used for calibrating the channel. Remarks The following table lists the characteristics of this property. Short Name AI.ChanCal.Poly.ReverseCoeff Data type c1ddbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Availab

### Analog Input:General Properties:Channel Calibration:Scaling Parameters:Polynomial:Reverse Coefficients

Specifies the reverse polynomial values used for calibrating the channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.ChanCal.Poly.ReverseCoeff |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr22a1.html language=enus -->
## TOPIC 00814: Analog Input:General Properties:Channel Calibration:Verification:Reference Values

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr22a1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr22a1.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference values collected when verifying the calibration. NI-DAQmx stores these values as a record of calibration accuracy and does not use them in the scaling process. Remarks The following table lists the characteristics of this property. Short Name AI.ChanCal.Verif.RefVals Data typ

### Analog Input:General Properties:Channel Calibration:Verification:Reference Values

Specifies the reference values collected when verifying the calibration. NI-DAQmx stores these values as a record of calibration accuracy and does not use them in the scaling process.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.ChanCal.Verif.RefVals |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr22a2.html language=enus -->
## TOPIC 00815: Analog Input:General Properties:Channel Calibration:Verification:Acquired Values

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr22a2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr22a2.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the acquired values collected when verifying the calibration. NI-DAQmx stores these values as a record of calibration accuracy and does not use them in the scaling process. Remarks The following table lists the characteristics of this property. Short Name AI.ChanCal.Verif.AcqVals Data type

### Analog Input:General Properties:Channel Calibration:Verification:Acquired Values

Specifies the acquired values collected when verifying the calibration. NI-DAQmx stores these values as a record of calibration accuracy and does not use them in the scaling process.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.ChanCal.Verif.AcqVals |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr22a3.html language=enus -->
## TOPIC 00816: Analog Input:General Properties:Channel Calibration:Operator Name

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr22a3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr22a3.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of the operator who performed the channel calibration. Remarks The following table lists the characteristics of this property. Short Name AI.ChanCal.OperatorName Data type cstr.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in R

### Analog Input:General Properties:Channel Calibration:Operator Name

Specifies the name of the operator who performed the channel calibration.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.ChanCal.OperatorName |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr22a4.html language=enus -->
## TOPIC 00817: Analog Input:General Properties:Channel Calibration:Description

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr22a4.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr22a4.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the description entered for the calibration of the channel. Remarks The following table lists the characteristics of this property. Short Name AI.ChanCal.Desc Data type cstr.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engi

### Analog Input:General Properties:Channel Calibration:Description

Specifies the description entered for the calibration of the channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.ChanCal.Desc |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr22b3.html language=enus -->
## TOPIC 00818: Counter Input:Timestamp:Units

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr22b3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr22b3.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return timestamp measurements. Remarks The following table lists the characteristics of this property. Short Name CI.Timestamp.Units Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine Tru

### Counter Input:Timestamp:Units

Specifies the units to use to return timestamp measurements.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Timestamp.Units |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Seconds | 10364 | Seconds. |
| --- | --- | --- |
| From Custom Scale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr22b4.html language=enus -->
## TOPIC 00819: Counter Input:Timestamp:Initial Seconds

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr22b4.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr22b4.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of seconds that elapsed since the beginning of the current year. This value is ignored if CI.GPS.SyncMethod is IRIG-B. Remarks The following table lists the characteristics of this property. Short Name CI.Timestamp.InitialSeconds Data type cu32.png Permissions Read/Write Resetta

### Counter Input:Timestamp:Initial Seconds

Specifies the number of seconds that elapsed since the beginning of the current year. This value is ignored if 
 [CI.GPS.SyncMethod](/csh?context=nidaqmx_daqmxprop_attr1092)
 is IRIG-B.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Timestamp.InitialSeconds |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr22d8.html language=enus -->
## TOPIC 00820: Analog Input:General Properties:Advanced:Data Transfer and Memory:Compression:Raw Data Compression Type

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr22d8.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr22d8.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of compression to apply to raw samples returned from the device. Remarks The following table lists the characteristics of this property. Short Name AI.RawDataCompressionType Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Av

### Analog Input:General Properties:Advanced:Data Transfer and Memory:Compression:Raw Data Compression Type

Specifies the type of compression to apply to 
 [raw samples](/csh?context=nidaqmx_mxcncpts_rawdata)
 returned from the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.RawDataCompressionType |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| None | 10230 | Do not compress samples. |
| --- | --- | --- |
| Lossless Packing | 12555 | Remove unused bits from samples. No resolution is lost. |
| Lossy LSB Removal | 12556 | Remove unused bits from samples. Then, if necessary, remove bits from samples until the samples are the size specified with AI.LossyLSBRemoval.CompressedSampSize . This compression type limits resolution to the specified sample size. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr22d9.html language=enus -->
## TOPIC 00821: Analog Input:General Properties:Advanced:Data Transfer and Memory:Compression:Lossy LSB Removal:Compressed Sample Size

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr22d9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr22d9.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of bits to return in a raw sample when AI.RawDataCompressionType is set to Lossy LSB Removal. Remarks The following table lists the characteristics of this property. Short Name AI.LossyLSBRemoval.CompressedSampSize Data type cu32.png Permissions Read/Write Resettable True Settab

### Analog Input:General Properties:Advanced:Data Transfer and Memory:Compression:Lossy LSB Removal:Compressed Sample Size

Specifies the number of bits to return in a 
 [raw sample](/csh?context=nidaqmx_mxcncpts_rawdata)
 when 
 [AI.RawDataCompressionType](/csh?context=nidaqmx_daqmxprop_attr22d8)
 is set to Lossy LSB Removal.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.LossyLSBRemoval.CompressedSampSize |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr22da.html language=enus -->
## TOPIC 00822: Analog Input:General Properties:Digitizer/ADC:Raw Sample Size

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr22da.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr22da.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in bits the size of a raw sample from the device. Remarks The following table lists the characteristics of this property. Short Name AI.RawSampSize Data type cu32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### Analog Input:General Properties:Digitizer/ADC:Raw Sample Size

Indicates in bits the size of a 
 [raw sample](/csh?context=nidaqmx_mxcncpts_rawdata)
 from the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.RawSampSize |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr22fe.html language=enus -->
## TOPIC 00823: Counter Input:Semi-Period:Starting Edge

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr22fe.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr22fe.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge of the input signal to begin semi-period measurement. Semi-period measurements alternate between high time and low time, starting on this edge. Remarks The following table lists the characteristics of this property. Short Name CI.SemiPeriod.StartingEdge Data type ci32.png Per

### Counter Input:Semi-Period:Starting Edge

Specifies on which edge of the input signal to begin semi-period measurement. Semi-period measurements alternate between high time and low time, starting on this edge.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.SemiPeriod.StartingEdge |
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

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr22ff.html language=enus -->
## TOPIC 00824: Counter Output:General Properties:More:Advanced:Ready For New Value

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr22ff.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr22ff.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the counter is ready for new continuous pulse train values. Remarks The following table lists the characteristics of this property. Short Name CO.RdyForNewVal Data type cbool.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-

### Counter Output:General Properties:More:Advanced:Ready For New Value

Indicates whether the counter is ready for new continuous pulse train values.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CO.RdyForNewVal |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2304.html language=enus -->
## TOPIC 00825: General Properties:Is Global

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2304.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2304.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the channel is a global channel . Remarks The following table lists the characteristics of this property. Short Name IsGlobal Data type cbool.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### General Properties:Is Global

Indicates whether the channel is a 
 [global channel](/csh?context=nidaqmx_mxcncpts_chans)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IsGlobal |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr230c.html language=enus -->
## TOPIC 00826: Analog Input:General Properties:Advanced:Data Transfer and Memory:Data Transfer Custom Threshold

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr230c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr230c.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of samples that must be in the FIFO to transfer data from the device if AI.DataXferReqCond is Onboard Memory Custom Threshold. Remarks The following table lists the characteristics of this property. Short Name AI.DataXferCustomThreshold Data type cu32.png Permissions Read/Write

### Analog Input:General Properties:Advanced:Data Transfer and Memory:Data Transfer Custom Threshold

Specifies the number of samples that must be in the FIFO to transfer data from the device if 
 [AI.DataXferReqCond](/csh?context=nidaqmx_daqmxprop_attr188b)
 is Onboard Memory Custom Threshold.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.DataXferCustomThreshold |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr293.html language=enus -->
## TOPIC 00827: Counter Output:General Properties:More:Count

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr293.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr293.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the current value of the count register. Remarks The following table lists the characteristics of this property. Short Name CO.Count Data type cu32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### Counter Output:General Properties:More:Count

Indicates the current value of the count register.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CO.Count |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr294.html language=enus -->
## TOPIC 00828: Counter Output:General Properties:More:Output State

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr294.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr294.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the current state of the output terminal of the counter. Remarks The following table lists the characteristics of this property. Short Name CO.OutputState Data type ci32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine T

### Counter Output:General Properties:More:Output State

Indicates the current state of the output terminal of the counter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CO.OutputState |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| High | 10192 | High state. |
| --- | --- | --- |
| Low | 10214 | Low state. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr295.html language=enus -->
## TOPIC 00829: Counter Output:General Properties:More:Auto Increment Count

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr295.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr295.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a number of timebase ticks by which to increase the time spent in the idle state for each successive pulse. When this value is greater than 0, NI-DAQmx generates progressively longer pulses until the count register rolls over. At that point, the generated pulses return to the original puls

### Counter Output:General Properties:More:Auto Increment Count

Specifies a number of timebase ticks by which to increase the time spent in the idle state for each successive pulse.

When this value is greater than 0, NI-DAQmx generates progressively longer pulses until the count register rolls over. At that point, the generated 
pulses return to the original pulse width and grow progressively longer until the count register rolls over again.

Use this property to provide a clock to an analog input channel for equivalent time sampling (ETS). ETS is a data acquisition technique in which 
data on a periodic waveform with a frequency higher than the Nyquist frequency of the system is obtained by sampling the waveform at instants in 
time skewed in relation to the beginning of each period of the waveform.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CO.AutoIncrCnt |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2966.html language=enus -->
## TOPIC 00830: Digital Input:General Properties:Advanced:Acquire On

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2966.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2966.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge of the sample clock to acquire samples. Remarks The following table lists the characteristics of this property. Short Name DI.AcquireOn Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True S

### Digital Input:General Properties:Advanced:Acquire On

Specifies on which edge of the sample clock to acquire samples.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DI.AcquireOn |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Sample Clock Active Edge | 14617 | Active edges. |
| --- | --- | --- |
| Sample Clock Inactive Edge | 14618 | Inactive edges. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2967.html language=enus -->
## TOPIC 00831: Digital Output:Line States:Paused State

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2967.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2967.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the state of the lines in a digital output task when the task pauses. Remarks The following table lists the characteristics of this property. Short Name DO.LineStates.PausedState Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Availa

### Digital Output:Line States:Paused State

Specifies the state of the lines in a digital output task when the task pauses.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DO.LineStates.PausedState |
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

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2968.html language=enus -->
## TOPIC 00832: Digital Output:Line States:Done State

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2968.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2968.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the state of the lines in a digital output task when the task completes execution . Remarks The following table lists the characteristics of this property. Short Name DO.LineStates.DoneState Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-spe

### Digital Output:Line States:Done State

Specifies the state of the lines in a digital output task when the task 
 [completes execution](/csh?context=nidaqmx_mxcncpts_whentaskdone)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DO.LineStates.DoneState |
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

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2969.html language=enus -->
## TOPIC 00833: Digital Output:General Properties:Advanced:Generate On

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2969.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2969.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge of the sample clock to generate samples. Remarks The following table lists the characteristics of this property. Short Name DO.GenerateOn Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True

### Digital Output:General Properties:Advanced:Generate On

Specifies on which edge of the sample clock to generate samples.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DO.GenerateOn |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Sample Clock Active Edge | 14617 | Active edges. |
| --- | --- | --- |
| Sample Clock Inactive Edge | 14618 | Inactive edges. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr296a.html language=enus -->
## TOPIC 00834: Digital Input:General Properties:Advanced:Data Transfer and Memory:Memory Mapping for Programmed IO Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr296a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr296a.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies for NI-DAQmx to map hardware registers to the memory space of the application, if possible. Normally, NI-DAQmx maps hardware registers to memory accessible only to the kernel. Mapping the registers to the memory space of the application increases performance. However, if the application ac

### Digital Input:General Properties:Advanced:Data Transfer and Memory:Memory Mapping for Programmed IO Enable

Specifies for NI-DAQmx to map hardware registers to the memory space of the application, if possible. Normally, NI-DAQmx maps hardware registers to memory accessible only to the kernel. Mapping the registers to the memory space of the application increases performance. However, if the application accesses the memory space mapped to the registers, it can adversely affect the operation of the device and possibly result in a system crash.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DI.MemMapEnable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr296b.html language=enus -->
## TOPIC 00835: Digital Output:General Properties:Advanced:Data Transfer and Memory:Memory Mapping for Programmed IO Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr296b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr296b.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies for NI-DAQmx to map hardware registers to the memory space of the application, if possible. Normally, NI-DAQmx maps hardware registers to memory accessible only to the kernel. Mapping the registers to the memory space of the application increases performance. However, if the application ac

### Digital Output:General Properties:Advanced:Data Transfer and Memory:Memory Mapping for Programmed IO Enable

Specifies for NI-DAQmx to map hardware registers to the memory space of the application, if possible. Normally, NI-DAQmx maps hardware registers to memory accessible only to the kernel. Mapping the registers to the memory space of the application increases performance. However, if the application accesses the memory space mapped to the registers, it can adversely affect the operation of the device and possibly result in a system crash.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DO.MemMapEnable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr296d.html language=enus -->
## TOPIC 00836: Digital Input:Logic Family

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr296d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr296d.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic family to use for acquisition. A logic family corresponds to voltage thresholds that are compatible with a group of voltage standards. Refer to the device documentation for information on the logic high and logic low voltages for these logic families. Remarks The following table

### Digital Input:Logic Family

Specifies the logic family to use for acquisition. A logic family corresponds to voltage thresholds that are compatible with a group of voltage standards. Refer to the device documentation for information on the logic high and logic low voltages for these logic families.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DI.LogicFamily |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| 1.8 V | 16184 | Compatible with 1.8 V CMOS signals. |
| --- | --- | --- |
| 2.5 V | 14620 | Compatible with 2.5 V CMOS signals. |
| 3.3 V | 14621 | Compatible with LVTTL signals. |
| 5.0 V | 14619 | Compatible with TTL and 5 V CMOS signals. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr296e.html language=enus -->
## TOPIC 00837: Digital Output:Logic Family

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr296e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr296e.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic family to use for generation. A logic family corresponds to voltage thresholds that are compatible with a group of voltage standards. Refer to the device documentation for information on the logic high and logic low voltages for these logic families. Remarks The following table l

### Digital Output:Logic Family

Specifies the logic family to use for generation. A logic family corresponds to voltage thresholds that are compatible with a group of voltage standards. Refer to the device documentation for information on the logic high and logic low voltages for these logic families.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DO.LogicFamily |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| 1.8 V | 16184 | Compatible with 1.8 V CMOS signals. |
| --- | --- | --- |
| 2.5 V | 14620 | Compatible with 2.5 V CMOS signals. |
| 3.3 V | 14621 | Compatible with LVTTL signals. |
| 5.0 V | 14619 | Compatible with TTL and 5 V CMOS signals. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2972.html language=enus -->
## TOPIC 00838: Digital Output:Line States:Start State

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2972.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2972.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the state of the lines in a digital output task when the task starts. Remarks The following table lists the characteristics of this property. Short Name DO.LineStates.StartState Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Availab

### Digital Output:Line States:Start State

Specifies the state of the lines in a digital output task when the task starts.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DO.LineStates.StartState |
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

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr298.html language=enus -->
## TOPIC 00839: Counter Output:Pulse:Ticks:Initial Delay

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr298.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr298.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of ticks to wait before generating the first pulse. Remarks The following table lists the characteristics of this property. Short Name CO.Pulse.Ticks.InitialDelay Data type cu32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available i

### Counter Output:Pulse:Ticks:Initial Delay

Specifies the number of ticks to wait before generating the first pulse.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CO.Pulse.Ticks.InitialDelay |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2983.html language=enus -->
## TOPIC 00840: Analog Input:TEDS:Is TEDS

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2983.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2983.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the virtual channel was initialized using a TEDS bitstream from the corresponding physical channel. Remarks The following table lists the characteristics of this property. Short Name AI.TEDS.IsTEDS Data type cbool.png Permissions Read Only Resettable False Settable While Task Is Running

### Analog Input:TEDS:Is TEDS

Indicates if the virtual channel was initialized using a TEDS bitstream from the corresponding physical channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.TEDS.IsTEDS |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr299.html language=enus -->
## TOPIC 00841: Counter Output:Pulse:Frequency:Initial Delay

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr299.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr299.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the amount of time to wait before generating the first pulse. Remarks The following table lists the characteristics of this property. Short Name CO.Pulse.Freq.InitialDelay Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Av

### Counter Output:Pulse:Frequency:Initial Delay

Specifies in seconds the amount of time to wait before generating the first pulse.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CO.Pulse.Freq.InitialDelay |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr29b0.html language=enus -->
## TOPIC 00842: Analog Input:Voltage:dB Reference

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr29b0.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr29b0.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the decibel reference level in the units of the channel. When you read samples as a waveform, the decibel reference level is included in the waveform attributes. Remarks The following table lists the characteristics of this property. Short Name AI.Voltage.dBRef Data type cdbl.png Permissio

### Analog Input:Voltage:dB Reference

Specifies the decibel reference level in the units of the channel. When you read samples as a waveform, the decibel reference level is included in the waveform attributes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.Voltage.dBRef |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr29b1.html language=enus -->
## TOPIC 00843: Analog Input:Sound Pressure:dB Reference

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr29b1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr29b1.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the decibel reference level in the units of the channel. When you read samples as a waveform, the decibel reference level is included in the waveform attributes. NI-DAQmx also uses the decibel reference level when converting AI.SoundPressure.MaxSoundPressureLvl to a voltage level. Remarks

### Analog Input:Sound Pressure:dB Reference

Specifies the decibel reference level in the units of the channel. When you read samples as a waveform, the decibel reference level is included in the waveform attributes. NI-DAQmx also uses the decibel reference level when converting 
 [AI.SoundPressure.MaxSoundPressureLvl](/csh?context=nidaqmx_daqmxprop_attr223a)
 to a voltage level.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.SoundPressure.dBRef |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr29b2.html language=enus -->
## TOPIC 00844: Analog Input:Acceleration:dB Reference

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr29b2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr29b2.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the decibel reference level in the units of the channel. When you read samples as a waveform, the decibel reference level is included in the waveform attributes. Remarks The following table lists the characteristics of this property. Short Name AI.Accel.dBRef Data type cdbl.png Permissions

### Analog Input:Acceleration:dB Reference

Specifies the decibel reference level in the units of the channel. When you read samples as a waveform, the decibel reference level is included in the waveform attributes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.Accel.dBRef |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr29d0.html language=enus -->
## TOPIC 00845: Analog Input:Temperature:Thermocouple:Scale Type

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr29d0.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr29d0.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the method or equation form that the thermocouple scale uses. Remarks The following table lists the characteristics of this property. Short Name AI.Thrmcpl.ScaleType Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Ti

### Analog Input:Temperature:Thermocouple:Scale Type

Specifies the method or equation form that the thermocouple scale uses.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.Thrmcpl.ScaleType |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Polynomial | 10449 | Scale values by using an Nth order polynomial equation. |
| --- | --- | --- |
| Table | 10450 | Map an array of prescaled values to an array of corresponding scaled values, with all other values scaled proportionally. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr29f2.html language=enus -->
## TOPIC 00846: Counter Output:General Properties:More:Advanced:Constrained Generation Mode

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr29f2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr29f2.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies constraints to apply when the counter generates pulses. Constraining the counter reduces the device resources required for counter operation. Constraining the counter can also allow additional analog or counter tasks on the device to run concurrently. For continuous counter tasks, NI-DAQmx

### Counter Output:General Properties:More:Advanced:Constrained Generation Mode

Specifies constraints to apply when the counter generates pulses. Constraining the counter reduces the device resources required for counter operation. Constraining the counter can also allow additional analog or counter tasks on the device to run concurrently. For continuous counter tasks, NI-DAQmx consumes no device resources when the counter is constrained. For finite counter tasks, resource use increases with the frequency regardless of the constraint mode. However, fixed frequency constraints significantly reduce resource usage, and fixed duty cycle constraint marginally reduces it.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CO.ConstrainedGenMode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Unconstrained | 14708 | Counter has no restrictions on pulse generation. |
| --- | --- | --- |
| Fixed High Frequency | 14709 | Pulse frequency must be above 7.63 Hz and cannot change while the task runs. In this mode, the duty cycle has 8 bits of resolution. |
| Fixed Low Frequency | 14710 | Pulse frequency must be below 366.21 Hz and cannot change while the task runs. In this mode, the duty cycle has 16 bits of resolution. |
| Fixed 50 Percent Duty Cycle | 14711 | Pulse duty cycle must be 50 percent. The frequency can change while the task runs. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr29f9.html language=enus -->
## TOPIC 00847: Analog Input:General Properties:Digitizer/ADC:Timing Mode

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr29f9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr29f9.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the ADC timing mode , controlling the tradeoff between speed and effective resolution. Some ADC timing modes provide increased powerline noise rejection. On devices that have an AI Convert clock, this setting affects both the maximum and default values for AIConv.Rate . You must use the sa

### Analog Input:General Properties:Digitizer/ADC:Timing Mode

Specifies the 
 [ADC timing mode](/csh?context=nidaqmx_mxdevconsid_configadctiming)
 , controlling the tradeoff between speed and effective resolution. Some ADC timing modes provide increased powerline noise rejection. On devices that have an AI Convert clock, this setting affects both the maximum and default values for 
 [AIConv.Rate](/csh?context=nidaqmx_daqmxprop_attr1848)
 . You must use the same ADC timing mode for all channels on a device, but you can use different ADC timing modes for different devices in the same task.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.ADCTimingMode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Automatic | 16097 | Uses the most appropriate supported timing mode based on the Sample Clock Rate. |
| --- | --- | --- |
| High Resolution | 10195 | Increases resolution and noise rejection while decreasing conversion rate. |
| High Speed | 14712 | Increases conversion rate while decreasing resolution. |
| Best 50 Hz Rejection | 14713 | Improves 50 Hz noise rejection while decreasing noise rejection at other frequencies. |
| Best 60 Hz Rejection | 14714 | Improves 60 Hz noise rejection while decreasing noise rejection at other frequencies. |
| Custom | 10137 | Use AI.ADCCustomTimingMode to specify a custom value controlling the tradeoff between speed and resolution. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2a18.html language=enus -->
## TOPIC 00848: Analog Output:Function Generation:Type

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2a18.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2a18.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the kind of the waveform to generate. Remarks The following table lists the characteristics of this property. Short Name AO.FuncGen.Type Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True Sine 14751 Sin

### Analog Output:Function Generation:Type

Specifies the kind of the waveform to generate.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO.FuncGen.Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Sine | 14751 | Sine wave. |
| --- | --- | --- |
| Triangle | 14752 | Triangle wave. |
| Square | 14753 | Square wave. |
| Sawtooth | 14754 | Sawtooth wave. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2a19.html language=enus -->
## TOPIC 00849: Analog Output:Function Generation:Frequency

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2a19.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2a19.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency of the waveform to generate in hertz. Remarks The following table lists the characteristics of this property. Short Name AO.FuncGen.Freq Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True

### Analog Output:Function Generation:Frequency

Specifies the frequency of the waveform to generate in hertz.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO.FuncGen.Freq |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2a1a.html language=enus -->
## TOPIC 00850: Analog Output:Function Generation:Amplitude

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2a1a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2a1a.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the zero-to-peak amplitude of the waveform to generate in volts. Zero and negative values are valid. Remarks The following table lists the characteristics of this property. Short Name AO.FuncGen.Amplitude Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Runn

### Analog Output:Function Generation:Amplitude

Specifies the zero-to-peak amplitude of the waveform to generate in volts. Zero and negative values are valid.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO.FuncGen.Amplitude |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2a1b.html language=enus -->
## TOPIC 00851: Analog Output:Function Generation:Offset

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2a1b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2a1b.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the voltage offset of the waveform to generate. Remarks The following table lists the characteristics of this property. Short Name AO.FuncGen.Offset Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True

### Analog Output:Function Generation:Offset

Specifies the voltage offset of the waveform to generate.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO.FuncGen.Offset |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2a1c.html language=enus -->
## TOPIC 00852: Analog Output:Function Generation:Square:DutyCycle

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2a1c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2a1c.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the square wave duty cycle of the waveform to generate. Remarks The following table lists the characteristics of this property. Short Name AO.FuncGen.Square.DutyCycle Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-T

### Analog Output:Function Generation:Square:DutyCycle

Specifies the square wave duty cycle of the waveform to generate.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO.FuncGen.Square.DutyCycle |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2a1d.html language=enus -->
## TOPIC 00853: Analog Output:Voltage:Current Limit

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2a1d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2a1d.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the current limit, in amperes, for the voltage channel. Remarks The following table lists the characteristics of this property. Short Name AO.Voltage.CurrentLimit Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time

### Analog Output:Voltage:Current Limit

Specifies the current limit, in amperes, for the voltage channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO.Voltage.CurrentLimit |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2a22.html language=enus -->
## TOPIC 00854: Analog Output:Function Generation:Modulation:Type

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2a22.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2a22.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies if the device generates a modulated version of the waveform using the original waveform as a carrier and input from an external terminal as the signal. Remarks The following table lists the characteristics of this property. Short Name AO.FuncGen.ModulationType Data type ci32.png Permission

### Analog Output:Function Generation:Modulation:Type

Specifies if the device generates a modulated version of the waveform using the original waveform as a carrier and input from an external terminal as the signal.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO.FuncGen.ModulationType |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| AM | 14756 | Amplitude modulation. |
| --- | --- | --- |
| FM | 14757 | Frequency modulation. |
| None | 10230 | No modulation. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2a23.html language=enus -->
## TOPIC 00855: Analog Output:Function Generation:Modulation:FM Deviation

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2a23.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2a23.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the FM deviation in hertz per volt when AO.FuncGen.ModulationType is FM. Remarks The following table lists the characteristics of this property. Short Name AO.FuncGen.FMDeviation Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Availa

### Analog Output:Function Generation:Modulation:FM Deviation

Specifies the FM deviation in hertz per volt when 
 [AO.FuncGen.ModulationType](/csh?context=nidaqmx_daqmxprop_attr2a22)
 is FM.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO.FuncGen.FMDeviation |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2a85.html language=enus -->
## TOPIC 00856: Digital Output:Overcurrent:Current Limit

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2a85.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2a85.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the current threshold in Amperes for the channel. A value of 0 means the channel observes no limit. Devices can monitor only a finite number of current thresholds simultaneously. If you attempt to monitor additional thresholds, NI-DAQmx returns an error. Remarks The following table lists t

### Digital Output:Overcurrent:Current Limit

Specifies the current threshold in Amperes for the channel. A value of 0 means the channel observes no limit. Devices can monitor only a finite number of current thresholds simultaneously. If you attempt to monitor additional thresholds, NI-DAQmx returns an error.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DO.Overcurrent.Limit |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2a86.html language=enus -->
## TOPIC 00857: Digital Output:Overcurrent:Automatic Re-enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2a86.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2a86.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to automatically reenable channels after they no longer exceed the current limit specified by DO.Overcurrent.Limit . Remarks The following table lists the characteristics of this property. Short Name DO.Overcurrent.AutoReenable Data type cbool.png Permissions Read/Write Resettable

### Digital Output:Overcurrent:Automatic Re-enable

Specifies whether to automatically reenable channels after they no longer exceed the current limit specified by 
 [DO.Overcurrent.Limit](/csh?context=nidaqmx_daqmxprop_attr2a85)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DO.Overcurrent.AutoReenable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2a87.html language=enus -->
## TOPIC 00858: Digital Output:Overcurrent:Re-enable Period

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2a87.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2a87.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the delay in seconds between the time a channel no longer exceeds the current limit and the reactivation of that channel, if DO.Overcurrent.AutoReenable is TRUE. Remarks The following table lists the characteristics of this property. Short Name DO.Overcurrent.ReenablePeriod Data type cdbl.

### Digital Output:Overcurrent:Re-enable Period

Specifies the delay in seconds between the time a channel no longer exceeds the current limit and the reactivation of that channel, if 
 [DO.Overcurrent.AutoReenable](/csh?context=nidaqmx_daqmxprop_attr2a86)
 is TRUE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DO.Overcurrent.ReenablePeriod |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2a88.html language=enus -->
## TOPIC 00859: Analog Input:General Properties:Signal Conditioning:Probe Attenuation

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2a88.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2a88.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the amount of attenuation provided by the probe connected to the channel. Specify this attenuation as a ratio. Remarks The following table lists the characteristics of this property. Short Name AI.ProbeAtten Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is R

### Analog Input:General Properties:Signal Conditioning:Probe Attenuation

Specifies the amount of attenuation provided by the probe connected to the channel. Specify this attenuation as a ratio.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.ProbeAtten |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2a89.html language=enus -->
## TOPIC 00860: Analog Input:General Properties:Advanced:DC Offset

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2a89.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2a89.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the DC value to add to the input range of the device. Use AI.Rng.High and AI.Rng.Low to specify the input range. This offset is in the native units of the device . Remarks The following table lists the characteristics of this property. Short Name AI.DCOffset Data type cdbl.png Permissions

### Analog Input:General Properties:Advanced:DC Offset

Specifies the DC value to add to the input range of the device. Use 
 [AI.Rng.High](/csh?context=nidaqmx_daqmxprop_attr1815)
 and 
 [AI.Rng.Low](/csh?context=nidaqmx_daqmxprop_attr1816)
 to specify the input range. This offset is in the native units of the device .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.DCOffset |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2a8e.html language=enus -->
## TOPIC 00861: Analog Input:General Properties:Advanced:Data Transfer and Memory:USB Transfer Request Size

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2a8e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2a8e.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum size of a USB transfer request in bytes. Modify this value to affect performance under different combinations of operating system and device. Remarks The following table lists the characteristics of this property. Short Name AI.UsbXferReqSize Data type cu32.png Permissions Read

### Analog Input:General Properties:Advanced:Data Transfer and Memory:USB Transfer Request Size

Specifies the maximum size of a USB transfer request in bytes. Modify this value to affect performance under different combinations of operating system and device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.UsbXferReqSize |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2a8f.html language=enus -->
## TOPIC 00862: Analog Output:General Properties:Advanced:Data Transfer and Memory:USB Transfer Request Size

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2a8f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2a8f.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum size of a USB transfer request in bytes. Modify this value to affect performance under different combinations of operating system and device. Remarks The following table lists the characteristics of this property. Short Name AO.UsbXferReqSize Data type cu32.png Permissions Read

### Analog Output:General Properties:Advanced:Data Transfer and Memory:USB Transfer Request Size

Specifies the maximum size of a USB transfer request in bytes. Modify this value to affect performance under different combinations of operating system and device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO.UsbXferReqSize |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2a90.html language=enus -->
## TOPIC 00863: Digital Input:General Properties:Advanced:Data Transfer and Memory:USB Transfer Request Size

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2a90.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2a90.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum size of a USB transfer request in bytes. Modify this value to affect performance under different combinations of operating system and device. Remarks The following table lists the characteristics of this property. Short Name DI.UsbXferReqSize Data type cu32.png Permissions Read

### Digital Input:General Properties:Advanced:Data Transfer and Memory:USB Transfer Request Size

Specifies the maximum size of a USB transfer request in bytes. Modify this value to affect performance under different combinations of operating system and device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DI.UsbXferReqSize |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2a91.html language=enus -->
## TOPIC 00864: Digital Output:General Properties:Advanced:Data Transfer and Memory:USB Transfer Request Size

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2a91.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2a91.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum size of a USB transfer request in bytes. Modify this value to affect performance under different combinations of operating system and device. Remarks The following table lists the characteristics of this property. Short Name DO.UsbXferReqSize Data type cu32.png Permissions Read

### Digital Output:General Properties:Advanced:Data Transfer and Memory:USB Transfer Request Size

Specifies the maximum size of a USB transfer request in bytes. Modify this value to affect performance under different combinations of operating system and device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DO.UsbXferReqSize |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2a92.html language=enus -->
## TOPIC 00865: Counter Input:General Properties:More:Advanced:Data Transfer and Memory:USB Transfer Request Size

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2a92.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2a92.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum size of a USB transfer request in bytes. Modify this value to affect performance under different combinations of operating system and device. Remarks The following table lists the characteristics of this property. Short Name CI.UsbXferReqSize Data type cu32.png Permissions Read

### Counter Input:General Properties:More:Advanced:Data Transfer and Memory:USB Transfer Request Size

Specifies the maximum size of a USB transfer request in bytes. Modify this value to affect performance under different combinations of operating system and device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.UsbXferReqSize |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2a93.html language=enus -->
## TOPIC 00866: Counter Output:General Properties:More:Advanced:Data Transfer and Memory:USB Transfer Request Size

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2a93.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2a93.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum size of a USB transfer request in bytes. Modify this value to affect performance under different combinations of operating system and device. Remarks The following table lists the characteristics of this property. Short Name CO.UsbXferReqSize Data type cu32.png Permissions Read

### Counter Output:General Properties:More:Advanced:Data Transfer and Memory:USB Transfer Request Size

Specifies the maximum size of a USB transfer request in bytes. Modify this value to affect performance under different combinations of operating system and device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CO.UsbXferReqSize |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2abe.html language=enus -->
## TOPIC 00867: Analog Input:Position:Eddy Current Proximity Probe:Sensitivity

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2abe.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2abe.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sensitivity of the eddy current proximity probe . This value is in the units you specify with AI.EddyCurrentProx.SensitivityUnits . Refer to the sensor documentation to determine this value. Remarks The following table lists the characteristics of this property. Short Name AI.EddyCurre

### Analog Input:Position:Eddy Current Proximity Probe:Sensitivity

Specifies the sensitivity of the 
 [eddy current proximity probe](/csh?context=nidaqmx_measfunds_eddycurrentproximityprobe)
 . This value is in the units you specify with 
 [AI.EddyCurrentProx.SensitivityUnits](/csh?context=nidaqmx_daqmxprop_attr2abf)
 . Refer to the sensor documentation to determine this value.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.EddyCurrentProx.Sensitivity |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2abf.html language=enus -->
## TOPIC 00868: Analog Input:Position:Eddy Current Proximity Probe:Sensitivity Units

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2abf.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2abf.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of AI.EddyCurrentProx.Sensitivity . Remarks The following table lists the characteristics of this property. Short Name AI.EddyCurrentProx.SensitivityUnits Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Tim

### Analog Input:Position:Eddy Current Proximity Probe:Sensitivity Units

Specifies the units of 
 [AI.EddyCurrentProx.Sensitivity](/csh?context=nidaqmx_daqmxprop_attr2abe)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.EddyCurrentProx.SensitivityUnits |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| mVolts/mil | 14836 | mVolts/mil. |
| --- | --- | --- |
| Volts/mil | 14837 | Volts/mil. |
| mVolts/mMeter | 14838 | mVolts/mMeter. |
| Volts/mMeter | 14839 | Volts/mMeter. |
| mVolts/micron | 14840 | mVolts/micron. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2ac0.html language=enus -->
## TOPIC 00869: Analog Input:Position:Eddy Current Proximity Probe:Units

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2ac0.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2ac0.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return proximity measurements from the channel. Remarks The following table lists the characteristics of this property. Short Name AI.EddyCurrentProx.Units Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available

### Analog Input:Position:Eddy Current Proximity Probe:Units

Specifies the units to use to return proximity measurements from the channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.EddyCurrentProx.Units |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Meters | 10219 | Meters. |
| --- | --- | --- |
| Inches | 10379 | Inches. |
| From Custom Scale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2ec9.html language=enus -->
## TOPIC 00870: Counter Output:General Properties:More:Enable Initial Delay on Retrigger

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2ec9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2ec9.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply the initial delay to retriggered pulse trains. Remarks The following table lists the characteristics of this property. Short Name CO.EnableInitialDelayOnRetrigger Data type cbool.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Avai

### Counter Output:General Properties:More:Enable Initial Delay on Retrigger

Specifies whether to apply the 
 [initial delay](/csh?context=nidaqmx_mxcncpts_pulsetrainpolarity)
 to retriggered pulse trains.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CO.EnableInitialDelayOnRetrigger |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2ecb.html language=enus -->
## TOPIC 00871: Counter Output:General Properties:More:Advanced:Data Transfer and Memory:Use Only Onboard Memory

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2ecb.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2ecb.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to write samples directly to the onboard memory of the device, bypassing the memory buffer. Generally, you cannot update onboard memory directly after you start the task. Onboard memory includes data FIFOs. Remarks The following table lists the characteristics of this property. Sho

### Counter Output:General Properties:More:Advanced:Data Transfer and Memory:Use Only Onboard Memory

Specifies whether to write samples directly to the onboard memory of the device, bypassing the memory buffer. Generally, you cannot update onboard memory directly after you start the task. Onboard memory includes data FIFOs.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CO.UseOnlyOnBrdMem |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2ecc.html language=enus -->
## TOPIC 00872: Counter Output:General Properties:More:Advanced:Data Transfer and Memory:Data Transfer Mechanism

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2ecc.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2ecc.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the data transfer mode for the device. For buffered operations, use DMA or USB Bulk. For non-buffered operations, use Polled. Remarks The following table lists the characteristics of this property. Short Name CO.DataXferMech Data type ci32.png Permissions Read/Write Resettable True Settabl

### Counter Output:General Properties:More:Advanced:Data Transfer and Memory:Data Transfer Mechanism

Specifies the data transfer mode for the device. For buffered operations, use DMA or USB Bulk. For non-buffered operations, use Polled.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CO.DataXferMech |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| DMA | 10054 | Direct Memory Access. Data transfers take place independently from the application. |
| --- | --- | --- |
| Interrupts | 10204 | Data transfers take place independently from the application. Using interrupts increases CPU usage because the CPU must service interrupt requests. Typically, you should use interrupts if the device is out of DMA channels. |
| Programmed I/O | 10264 | Data transfers take place when you call DAQmx Read or DAQmx Write . |
| USB Bulk | 12590 | Data transfers take place independently from the application using a USB bulk pipe. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2ecd.html language=enus -->
## TOPIC 00873: Counter Output:General Properties:More:Advanced:Data Transfer and Memory:Data Transfer Request Condition

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2ecd.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2ecd.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies under what condition to transfer data from the buffer to the onboard memory of the device. Remarks The following table lists the characteristics of this property. Short Name CO.DataXferReqCond Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-s

### Counter Output:General Properties:More:Advanced:Data Transfer and Memory:Data Transfer Request Condition

Specifies under what condition to transfer data from the buffer to the onboard memory of the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CO.DataXferReqCond |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Onboard Memory Empty | 10235 | Transfer data to the device only when there is no data in the onboard memory of the device. |
| --- | --- | --- |
| Onboard Memory Half Full or Less | 10239 | Transfer data to the device any time the onboard memory is less than half full. |
| Onboard Memory Less than Full | 10242 | Transfer data to the device any time the onboard memory of the device is not full. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2ed0.html language=enus -->
## TOPIC 00874: Counter Input:Frequency:Measurement Specifications:Enable Averaging

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2ed0.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2ed0.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging mode for Sample Clock-timed frequency measurements. Remarks The following table lists the characteristics of this property. Short Name CI.Freq.EnableAveraging Data type cbool.png Permissions Read/Write Resettable True Settable While Task Is Running device-specif

### Counter Input:Frequency:Measurement Specifications:Enable Averaging

Specifies whether to enable 
 [averaging mode](/csh?context=nidaqmx_mxcncpts_configtimemeas)
 for Sample Clock-timed frequency measurements.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Freq.EnableAveraging |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2ed1.html language=enus -->
## TOPIC 00875: Counter Input:Period:Measurement Specifications:Enable Averaging

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2ed1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2ed1.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging mode for Sample Clock-timed period measurements. Remarks The following table lists the characteristics of this property. Short Name CI.Period.EnableAveraging Data type cbool.png Permissions Read/Write Resettable True Settable While Task Is Running device-specifi

### Counter Input:Period:Measurement Specifications:Enable Averaging

Specifies whether to enable 
 [averaging mode](/csh?context=nidaqmx_mxcncpts_configtimemeas)
 for Sample Clock-timed period measurements.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Period.EnableAveraging |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2ed2.html language=enus -->
## TOPIC 00876: Counter Input:General Properties:More:Advanced:Data Transfer and Memory:Memory Mapping for Programmed IO Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2ed2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2ed2.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies for NI-DAQmx to map hardware registers to the memory space of the application, if possible. Normally, NI-DAQmx maps hardware registers to memory accessible only to the kernel. Mapping the registers to the memory space of the application increases performance. However, if the application ac

### Counter Input:General Properties:More:Advanced:Data Transfer and Memory:Memory Mapping for Programmed IO Enable

Specifies for NI-DAQmx to map hardware registers to the memory space of the application, if possible. Normally, NI-DAQmx maps hardware registers to memory accessible only to the kernel. Mapping the registers to the memory space of the application increases performance. However, if the application accesses the memory space mapped to the registers, it can adversely affect the operation of the device and possibly result in a system crash.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.MemMapEnable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2ed3.html language=enus -->
## TOPIC 00877: Counter Output:General Properties:More:Advanced:Data Transfer and Memory:Memory Mapping for Programmed IO Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2ed3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2ed3.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies for NI-DAQmx to map hardware registers to the memory space of the application, if possible. Normally, NI-DAQmx maps hardware registers to memory accessible only to the kernel. Mapping the registers to the memory space of the application increases performance. However, if the application ac

### Counter Output:General Properties:More:Advanced:Data Transfer and Memory:Memory Mapping for Programmed IO Enable

Specifies for NI-DAQmx to map hardware registers to the memory space of the application, if possible. Normally, NI-DAQmx maps hardware registers to memory accessible only to the kernel. Mapping the registers to the memory space of the application increases performance. However, if the application accesses the memory space mapped to the registers, it can adversely affect the operation of the device and possibly result in a system crash.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CO.MemMapEnable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2ed4.html language=enus -->
## TOPIC 00878: Digital Input:Digital Filter:Timebase:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2ed4.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2ed4.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the timebase of the digital filter. Remarks The following table lists the characteristics of this property. Short Name DI.DigFltr.TimebaseSrc Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific

### Digital Input:Digital Filter:Timebase:Source

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 of the signal to use as the timebase of the digital filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DI.DigFltr.TimebaseSrc |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2ed5.html language=enus -->
## TOPIC 00879: Digital Input:Digital Filter:Timebase:Rate

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2ed5.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2ed5.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. Remarks The following table lists the characteristics of this property. Short Name DI.DigFltr.TimebaseRate Data type cdbl.png Permissions Read/Write Resettable True Settable While

### Digital Input:Digital Filter:Timebase:Rate

Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DI.DigFltr.TimebaseRate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2ed6.html language=enus -->
## TOPIC 00880: Digital Input:Digital Synchronization:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2ed6.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2ed6.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. Remarks The following table lists the characteristics of this property. Short Name DI.DigSync.Enable Data type cbool.png Permissions Read/Write Resettable True Settable While Task Is Run

### Digital Input:Digital Synchronization:Enable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DI.DigSync.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2efb.html language=enus -->
## TOPIC 00881: Counter Input:General Properties:More:Advanced:Data Transfer and Memory:Data Transfer Request Condition

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2efb.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2efb.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies under what condition to transfer data from the onboard memory of the device to the buffer. Remarks The following table lists the characteristics of this property. Short Name CI.DataXferReqCond Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-s

### Counter Input:General Properties:More:Advanced:Data Transfer and Memory:Data Transfer Request Condition

Specifies under what condition to transfer data from the onboard memory of the device to the buffer.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.DataXferReqCond |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Onboard Memory More than Half Full | 10237 | Transfer data from the device when more than half of the onboard memory of the device fills. |
| --- | --- | --- |
| Onboard Memory Not Empty | 10241 | Transfer data from the device when there is data in the onboard memory. |
| Onboard Memory Custom Threshold | 12577 | Transfer data from the device when the number of samples specified with AI.DataXferCustomThreshold are in the device FIFO. |
| When Acquisition Complete | 12546 | Transfer data when the acquisition is complete. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2efe.html language=enus -->
## TOPIC 00882: Digital Input:Digital Filter:Enable Bus Mode

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2efe.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2efe.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable bus mode for digital filtering. If you set this property to TRUE, NI-DAQmx treats all lines that use common filtering settings as a bus. If any line in the bus has jitter, all lines in the bus hold state until the entire bus stabilizes, or until 2 times the minimum pulse

### Digital Input:Digital Filter:Enable Bus Mode

Specifies whether to enable bus mode for digital filtering. If you set this property to TRUE, NI-DAQmx treats all lines that use common filtering settings as a bus. If any line in the bus has jitter, all lines in the bus hold state until the entire bus stabilizes, or until 2 times the minimum pulse width elapses. If you set this property to FALSE, NI-DAQmx filters all lines individually. Jitter in one line does not affect other lines.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DI.DigFltr.EnableBusMode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f04.html language=enus -->
## TOPIC 00883: Counter Input:Pulse:Frequency:Input:Terminal

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f04.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f04.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the connectCounter of the signal to measure. Remarks The following table lists the characteristics of this property. Short Name CI.Pulse.Freq.Term Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine Tr

### Counter Input:Pulse:Frequency:Input:Terminal

Specifies the 
 [connectCounter](/csh?context=nidaqmx__daqhelp)
 of the signal to measure.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Pulse.Freq.Term |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f05.html language=enus -->
## TOPIC 00884: Counter Input:Pulse:Frequency:Starting Edge

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f05.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f05.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge of the input signal to begin pulse measurement. Remarks The following table lists the characteristics of this property. Short Name CI.Pulse.Freq.StartingEdge Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in

### Counter Input:Pulse:Frequency:Starting Edge

Specifies on which edge of the input signal to begin pulse measurement.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Pulse.Freq.StartingEdge |
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

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f06.html language=enus -->
## TOPIC 00885: Counter Input:Pulse:Frequency:Input:Digital Filter:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f06.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f06.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply a digital filter to the signal to measure. Remarks The following table lists the characteristics of this property. Short Name CI.Pulse.Freq.DigFltr.Enable Data type cbool.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in

### Counter Input:Pulse:Frequency:Input:Digital Filter:Enable

Specifies whether to apply a digital 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 to the signal to measure.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Pulse.Freq.DigFltr.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f07.html language=enus -->
## TOPIC 00886: Counter Input:Pulse:Frequency:Input:Digital Filter:Minimum Pulse Width

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f07.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f07.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. Remarks The following table lists the characteristics of this property. Short Name CI.Pulse.Freq.DigFltr.MinPulseWidth Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Availabl

### Counter Input:Pulse:Frequency:Input:Digital Filter:Minimum Pulse Width

Specifies in seconds the minimum pulse width the 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 recognizes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Pulse.Freq.DigFltr.MinPulseWidth |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f08.html language=enus -->
## TOPIC 00887: Counter Input:Pulse:Frequency:Input:Digital Filter:Timebase:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f08.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f08.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the timebase of the digital filter. Remarks The following table lists the characteristics of this property. Short Name CI.Pulse.Freq.DigFltr.TimebaseSrc Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running devi

### Counter Input:Pulse:Frequency:Input:Digital Filter:Timebase:Source

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 of the signal to use as the timebase of the digital filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Pulse.Freq.DigFltr.TimebaseSrc |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f09.html language=enus -->
## TOPIC 00888: Counter Input:Pulse:Frequency:Input:Digital Filter:Timebase:Rate

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f09.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f09.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. Remarks The following table lists the characteristics of this property. Short Name CI.Pulse.Freq.DigFltr.TimebaseRate Data type cdbl.png Permissions Read/Write Resettable True Set

### Counter Input:Pulse:Frequency:Input:Digital Filter:Timebase:Rate

Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Pulse.Freq.DigFltr.TimebaseRate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f0a.html language=enus -->
## TOPIC 00889: Counter Input:Pulse:Frequency:Input:Digital Synchronization:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f0a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f0a.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. Remarks The following table lists the characteristics of this property. Short Name CI.Pulse.Freq.DigSync.Enable Data type cbool.png Permissions Read/Write Resettable True Settable While

### Counter Input:Pulse:Frequency:Input:Digital Synchronization:Enable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Pulse.Freq.DigSync.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f0b.html language=enus -->
## TOPIC 00890: Counter Input:Pulse:Frequency:Units

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f0b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f0b.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return pulse specifications in terms of frequency. Remarks The following table lists the characteristics of this property. Short Name CI.Pulse.Freq.Units Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available i

### Counter Input:Pulse:Frequency:Units

Specifies the units to use to return pulse specifications in terms of frequency.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Pulse.Freq.Units |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Hz | 10373 | Hertz. |
| --- | --- | --- |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f0c.html language=enus -->
## TOPIC 00891: Counter Input:Pulse:Time:Input:Terminal

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f0c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f0c.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the connectCounter of the signal to measure. Remarks The following table lists the characteristics of this property. Short Name CI.Pulse.Time.Term Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine Tr

### Counter Input:Pulse:Time:Input:Terminal

Specifies the 
 [connectCounter](/csh?context=nidaqmx__daqhelp)
 of the signal to measure.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Pulse.Time.Term |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f0d.html language=enus -->
## TOPIC 00892: Counter Input:Pulse:Time:Starting Edge

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f0d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f0d.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge of the input signal to begin pulse measurement. Remarks The following table lists the characteristics of this property. Short Name CI.Pulse.Time.StartingEdge Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in

### Counter Input:Pulse:Time:Starting Edge

Specifies on which edge of the input signal to begin pulse measurement.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Pulse.Time.StartingEdge |
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

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f0e.html language=enus -->
## TOPIC 00893: Counter Input:Pulse:Time:Input:Digital Filter:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f0e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f0e.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply a digital filter to the signal to measure. Remarks The following table lists the characteristics of this property. Short Name CI.Pulse.Time.DigFltr.Enable Data type cbool.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in

### Counter Input:Pulse:Time:Input:Digital Filter:Enable

Specifies whether to apply a digital 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 to the signal to measure.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Pulse.Time.DigFltr.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f0f.html language=enus -->
## TOPIC 00894: Counter Input:Pulse:Time:Input:Digital Filter:Minimum Pulse Width

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f0f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f0f.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. Remarks The following table lists the characteristics of this property. Short Name CI.Pulse.Time.DigFltr.MinPulseWidth Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Availabl

### Counter Input:Pulse:Time:Input:Digital Filter:Minimum Pulse Width

Specifies in seconds the minimum pulse width the 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 recognizes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Pulse.Time.DigFltr.MinPulseWidth |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f10.html language=enus -->
## TOPIC 00895: Counter Input:Pulse:Time:Input:Digital Filter:Timebase:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f10.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f10.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the timebase of the digital filter. Remarks The following table lists the characteristics of this property. Short Name CI.Pulse.Time.DigFltr.TimebaseSrc Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running devi

### Counter Input:Pulse:Time:Input:Digital Filter:Timebase:Source

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 of the signal to use as the timebase of the digital filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Pulse.Time.DigFltr.TimebaseSrc |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f11.html language=enus -->
## TOPIC 00896: Counter Input:Pulse:Time:Input:Digital Filter:Timebase:Rate

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f11.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f11.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. Remarks The following table lists the characteristics of this property. Short Name CI.Pulse.Time.DigFltr.TimebaseRate Data type cdbl.png Permissions Read/Write Resettable True Set

### Counter Input:Pulse:Time:Input:Digital Filter:Timebase:Rate

Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Pulse.Time.DigFltr.TimebaseRate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f12.html language=enus -->
## TOPIC 00897: Counter Input:Pulse:Time:Input:Digital Synchronization:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f12.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f12.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. Remarks The following table lists the characteristics of this property. Short Name CI.Pulse.Time.DigSync.Enable Data type cbool.png Permissions Read/Write Resettable True Settable While

### Counter Input:Pulse:Time:Input:Digital Synchronization:Enable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Pulse.Time.DigSync.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f13.html language=enus -->
## TOPIC 00898: Counter Input:Pulse:Time:Units

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f13.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f13.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return pulse specifications in terms of high time and low time. Remarks The following table lists the characteristics of this property. Short Name CI.Pulse.Time.Units Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specifi

### Counter Input:Pulse:Time:Units

Specifies the units to use to return pulse specifications in terms of high time and low time.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Pulse.Time.Units |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Seconds | 10364 | Seconds. |
| --- | --- | --- |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f14.html language=enus -->
## TOPIC 00899: Counter Input:Pulse:Ticks:Input:Terminal

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f14.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f14.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the connectCounter of the signal to measure. Remarks The following table lists the characteristics of this property. Short Name CI.Pulse.Ticks.Term Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine T

### Counter Input:Pulse:Ticks:Input:Terminal

Specifies the 
 [connectCounter](/csh?context=nidaqmx__daqhelp)
 of the signal to measure.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Pulse.Ticks.Term |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f15.html language=enus -->
## TOPIC 00900: Counter Input:Pulse:Ticks:Starting Edge

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f15.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f15.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge of the input signal to begin pulse measurement. Remarks The following table lists the characteristics of this property. Short Name CI.Pulse.Ticks.StartingEdge Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in

### Counter Input:Pulse:Ticks:Starting Edge

Specifies on which edge of the input signal to begin pulse measurement.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Pulse.Ticks.StartingEdge |
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

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f16.html language=enus -->
## TOPIC 00901: Counter Input:Pulse:Ticks:Input:Digital Filter:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f16.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f16.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply a digital filter to the signal to measure. Remarks The following table lists the characteristics of this property. Short Name CI.Pulse.Ticks.DigFltr.Enable Data type cbool.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available i

### Counter Input:Pulse:Ticks:Input:Digital Filter:Enable

Specifies whether to apply a digital 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 to the signal to measure.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Pulse.Ticks.DigFltr.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f17.html language=enus -->
## TOPIC 00902: Counter Input:Pulse:Ticks:Input:Digital Filter:Minimum Pulse Width

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f17.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f17.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. Remarks The following table lists the characteristics of this property. Short Name CI.Pulse.Ticks.DigFltr.MinPulseWidth Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Availab

### Counter Input:Pulse:Ticks:Input:Digital Filter:Minimum Pulse Width

Specifies in seconds the minimum pulse width the 
 [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering)
 recognizes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Pulse.Ticks.DigFltr.MinPulseWidth |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f18.html language=enus -->
## TOPIC 00903: Counter Input:Pulse:Ticks:Input:Digital Filter:Timebase:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f18.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f18.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the timebase of the digital filter. Remarks The following table lists the characteristics of this property. Short Name CI.Pulse.Ticks.DigFltr.TimebaseSrc Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running dev

### Counter Input:Pulse:Ticks:Input:Digital Filter:Timebase:Source

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 of the signal to use as the timebase of the digital filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Pulse.Ticks.DigFltr.TimebaseSrc |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f19.html language=enus -->
## TOPIC 00904: Counter Input:Pulse:Ticks:Input:Digital Filter:Timebase:Rate

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f19.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f19.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. Remarks The following table lists the characteristics of this property. Short Name CI.Pulse.Ticks.DigFltr.TimebaseRate Data type cdbl.png Permissions Read/Write Resettable True Se

### Counter Input:Pulse:Ticks:Input:Digital Filter:Timebase:Rate

Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Pulse.Ticks.DigFltr.TimebaseRate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f1a.html language=enus -->
## TOPIC 00905: Counter Input:Pulse:Ticks:Input:Digital Synchronization:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f1a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f1a.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. Remarks The following table lists the characteristics of this property. Short Name CI.Pulse.Ticks.DigSync.Enable Data type cbool.png Permissions Read/Write Resettable True Settable While

### Counter Input:Pulse:Ticks:Input:Digital Synchronization:Enable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Pulse.Ticks.DigSync.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f6b.html language=enus -->
## TOPIC 00906: Analog Input:General Properties:Digitizer/ADC:Custom Timing Mode

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f6b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f6b.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the timing mode of the ADC when AI.ADCTimingMode is Custom. Remarks The following table lists the characteristics of this property. Short Name AI.ADCCustomTimingMode Data type cu32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Ti

### Analog Input:General Properties:Digitizer/ADC:Custom Timing Mode

Specifies the 
 [timing mode of the ADC](/csh?context=nidaqmx_mxdevconsid_configadctiming)
 when 
 [AI.ADCTimingMode](/csh?context=nidaqmx_daqmxprop_attr29f9)
 is Custom.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.ADCCustomTimingMode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f72.html language=enus -->
## TOPIC 00907: Analog Input:General Properties:Signal Conditioning:Thermocouple:Open Thermocouple Detection Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f72.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f72.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply the open thermocouple detection bias voltage to the channel. Changing the value of this property on a channel may require settling time before the data returned is valid. To compensate for this settling time, discard unsettled data or add a delay between committing and sta

### Analog Input:General Properties:Signal Conditioning:Thermocouple:Open Thermocouple Detection Enable

Specifies whether to apply the 
 [open thermocouple detection bias voltage](/csh?context=nidaqmx_mxdevconsid_openthermdet)
 to the channel. Changing the value of this property on a channel may require settling time before the data returned is valid. To compensate for this settling time, discard unsettled data or add a delay between committing and starting the task. Refer to your device specifications for the required settling time. When open thermocouple detection is enabled, use 
 [OpenThrmcplChansExist](/csh?context=nidaqmx_daqmxprop_attr2a96)
 to determine if any channels were open.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.OpenThrmcplDetectEnable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f75.html language=enus -->
## TOPIC 00908: Analog Input:Force:Units

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f75.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f75.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in which unit to return force or load measurements from the channel. Remarks The following table lists the characteristics of this property. Short Name AI.Force.Units Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-T

### Analog Input:Force:Units

Specifies in which unit to return force or load measurements from the channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.Force.Units |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Newtons | 15875 | Newtons. |
| --- | --- | --- |
| Pounds | 15876 | Pounds. |
| kgf | 15877 | Kilograms-force. |
| From Custom Scale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f76.html language=enus -->
## TOPIC 00909: Analog Input:Pressure:Units

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f76.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f76.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in which unit to return pressure measurements from the channel. Remarks The following table lists the characteristics of this property. Short Name AI.Pressure.Units Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Tim

### Analog Input:Pressure:Units

Specifies in which unit to return pressure measurements from the channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.Pressure.Units |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Pascals | 10081 | Pascals. |
| --- | --- | --- |
| psi | 15879 | Pounds per square inch. |
| bar | 15880 | Bar. |
| From Custom Scale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f77.html language=enus -->
## TOPIC 00910: Analog Input:Torque:Units

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f77.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f77.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in which unit to return torque measurements from the channel. Remarks The following table lists the characteristics of this property. Short Name AI.Torque.Units Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time En

### Analog Input:Torque:Units

Specifies in which unit to return torque measurements from the channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.Torque.Units |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Nm | 15881 | Newton meters. |
| --- | --- | --- |
| oz-in | 15882 | Ounce-inches. |
| lb-in | 15883 | Pound-inches. |
| lb-ft | 15884 | Pound-feet. |
| From Custom Scale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f78.html language=enus -->
## TOPIC 00911: Analog Input:General Properties:Signal Conditioning:Bridge:Shunt Cal:Shunt Cal A Resistor Value

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f78.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f78.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in ohms the desired value of the internal shunt calibration A resistor. Remarks The following table lists the characteristics of this property. Short Name AI.Bridge.ShuntCal.ShuntCalAResistance Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-

### Analog Input:General Properties:Signal Conditioning:Bridge:Shunt Cal:Shunt Cal A Resistor Value

Specifies in ohms the desired value of the internal shunt calibration A resistor.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.Bridge.ShuntCal.ShuntCalAResistance |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f79.html language=enus -->
## TOPIC 00912: Analog Input:General Properties:Signal Conditioning:Bridge:Shunt Cal:Shunt Cal A Actual Resistor Value

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f79.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f79.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in ohms the actual value of the internal shunt calibration A resistor. Remarks The following table lists the characteristics of this property. Short Name AI.Bridge.ShuntCal.ShuntCalAActualResistance Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running de

### Analog Input:General Properties:Signal Conditioning:Bridge:Shunt Cal:Shunt Cal A Actual Resistor Value

Specifies in ohms the actual value of the internal shunt calibration A resistor.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.Bridge.ShuntCal.ShuntCalAActualResistance |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f7a.html language=enus -->
## TOPIC 00913: Analog Input:General Properties:Signal Conditioning:Bridge:Shunt Cal:Shunt Cal B Resistor Value

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f7a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f7a.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in ohms the desired value of the internal shunt calibration B resistor. Remarks The following table lists the characteristics of this property. Short Name AI.Bridge.ShuntCal.ShuntCalBResistance Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-

### Analog Input:General Properties:Signal Conditioning:Bridge:Shunt Cal:Shunt Cal B Resistor Value

Specifies in ohms the desired value of the internal shunt calibration B resistor.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.Bridge.ShuntCal.ShuntCalBResistance |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f7b.html language=enus -->
## TOPIC 00914: Analog Input:General Properties:Signal Conditioning:Bridge:Shunt Cal:Shunt Cal B Actual Resistor Value

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f7b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f7b.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in ohms the actual value of the internal shunt calibration B resistor. Remarks The following table lists the characteristics of this property. Short Name AI.Bridge.ShuntCal.ShuntCalBActualResistance Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running de

### Analog Input:General Properties:Signal Conditioning:Bridge:Shunt Cal:Shunt Cal B Actual Resistor Value

Specifies in ohms the actual value of the internal shunt calibration B resistor.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.Bridge.ShuntCal.ShuntCalBActualResistance |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f81.html language=enus -->
## TOPIC 00915: Analog Input:Force:IEPE Sensor:Sensitivity

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f81.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f81.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sensitivity of the IEPE force sensor connected to the channel. Specify this value in the unit indicated by AI.Force.IEPESensor.SensitivityUnits . Remarks The following table lists the characteristics of this property. Short Name AI.Force.IEPESensor.Sensitivity Data type cdbl.png Permis

### Analog Input:Force:IEPE Sensor:Sensitivity

Specifies the sensitivity of the IEPE force sensor connected to the channel. Specify this value in the unit indicated by 
 [AI.Force.IEPESensor.SensitivityUnits](/csh?context=nidaqmx_daqmxprop_attr2f82)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.Force.IEPESensor.Sensitivity |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f82.html language=enus -->
## TOPIC 00916: Analog Input:Force:IEPE Sensor:Sensitivity Units

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f82.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f82.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units for AI.Force.IEPESensor.Sensitivity . Remarks The following table lists the characteristics of this property. Short Name AI.Force.IEPESensor.SensitivityUnits Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-

### Analog Input:Force:IEPE Sensor:Sensitivity Units

Specifies the units for 
 [AI.Force.IEPESensor.Sensitivity](/csh?context=nidaqmx_daqmxprop_attr2f81)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.Force.IEPESensor.SensitivityUnits |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| mVolts/N | 15891 | Millivolts per newton. |
| --- | --- | --- |
| mVolts/lb | 15892 | Millivolts per pound. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f86.html language=enus -->
## TOPIC 00917: Analog Input:General Properties:Signal Conditioning:Bridge:Initial Bridge Ratio

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f86.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f86.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in volts per volt the ratio of output voltage from the bridge to excitation voltage supplied to the bridge while not under load. NI-DAQmx subtracts this value from any measurements before applying scaling equations. If you set AI.Bridge.InitialVoltage , NI-DAQmx coerces this property to AI

### Analog Input:General Properties:Signal Conditioning:Bridge:Initial Bridge Ratio

Specifies in volts per volt the ratio of output voltage from the bridge to excitation voltage supplied to the bridge while not under load. NI-DAQmx subtracts this value from any measurements before applying scaling equations. If you set 
 [AI.Bridge.InitialVoltage](/csh?context=nidaqmx_daqmxprop_attr17ed)
 , NI-DAQmx coerces this property to 
 [AI.Bridge.InitialVoltage](/csh?context=nidaqmx_daqmxprop_attr17ed)
 divided by 
 [AI.Excit.ActualVal](/csh?context=nidaqmx_daqmxprop_attr1883)
 . If you set this property, NI-DAQmx coerces 
 [AI.Bridge.InitialVoltage](/csh?context=nidaqmx_daqmxprop_attr17ed)
 to the value of this property times 
 [AI.Excit.ActualVal](/csh?context=nidaqmx_daqmxprop_attr1883)
 . If you set both this property and 
 [AI.Bridge.InitialVoltage](/csh?context=nidaqmx_daqmxprop_attr17ed)
 , and their values conflict, NI-DAQmx returns an error. To avoid this error, reset one property to its default value before setting the other.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.Bridge.InitialRatio |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f87.html language=enus -->
## TOPIC 00918: Analog Input:Bridge:Scaling Parameters:Electrical Units

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f87.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f87.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies from which electrical unit to scale data. Select the same unit that the sensor data sheet or calibration certificate uses for electrical values. Remarks The following table lists the characteristics of this property. Short Name AI.Bridge.ElectricalUnits Data type ci32.png Permissions Read/

### Analog Input:Bridge:Scaling Parameters:Electrical Units

Specifies from which electrical unit to scale data. Select the same unit that the sensor data sheet or calibration certificate uses for electrical values.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.Bridge.ElectricalUnits |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Volts/Volt | 15896 | Volts per volt. |
| --- | --- | --- |
| mVolts/Volt | 15897 | Millivolts per volt. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f88.html language=enus -->
## TOPIC 00919: Analog Input:Bridge:Scaling Parameters:Physical Units

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f88.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f88.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies to which physical unit to scale electrical data. Select the same unit that the sensor data sheet or calibration certificate uses for physical values. Remarks The following table lists the characteristics of this property. Short Name AI.Bridge.PhysicalUnits Data type ci32.png Permissions Re

### Analog Input:Bridge:Scaling Parameters:Physical Units

Specifies to which physical unit to scale electrical data. Select the same unit that the sensor data sheet or calibration certificate uses for physical values.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.Bridge.PhysicalUnits |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Newtons | 15875 | Newtons. |
| --- | --- | --- |
| Pounds | 15876 | Pounds. |
| kgf | 15877 | kilograms-force. |
| Pascals | 10081 | Pascals. |
| psi | 15879 | Pounds per square inch. |
| bar | 15880 | Bar. |
| Nm | 15881 | Newton metres. |
| oz-in | 15882 | Ounce-inches. |
| lb-in | 15883 | Pound-inches. |
| lb-ft | 15884 | Pound-feet. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f89.html language=enus -->
## TOPIC 00920: Analog Input:Bridge:Scaling Parameters:Scale Type

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f89.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f89.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the scaling type to use when scaling electrical values from the sensor to physical units. Remarks The following table lists the characteristics of this property. Short Name AI.Bridge.ScaleType Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-s

### Analog Input:Bridge:Scaling Parameters:Scale Type

Specifies the 
 [scaling type](/csh?context=nidaqmx_measfunds_bridgescalingtypes)
 to use when scaling electrical values from the sensor to physical units.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.Bridge.ScaleType |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| None | 10230 | Do not scale electrical values to physical units. |
| --- | --- | --- |
| Two-Point Linear | 15898 | You provide two pairs of electrical values and their corresponding physical values. NI-DAQmx uses those values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values. |
| Table | 10450 | Map an array of electrical values to an array of corresponding physical values, with all other values scaled proportionally. If you specify this scaling type, AI.Max and AI.Min must be within the smallest and largest physical values. For any data outside those endpoints, NI-DAQmx coerces that data to the endpoints. |
| Polynomial | 10449 | Scale values by using an Nth order polynomial equation. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f8a.html language=enus -->
## TOPIC 00921: Analog Input:Bridge:Scaling Parameters:Two-Point Linear:First:Electrical Value

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f8a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f8a.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the first electrical value, corresponding to AI.Bridge.TwoPointLin.First.PhysicalVal . Specify this value in the unit indicated by AI.Bridge.ElectricalUnits . Remarks The following table lists the characteristics of this property. Short Name AI.Bridge.TwoPointLin.First.ElectricalVal Data t

### Analog Input:Bridge:Scaling Parameters:Two-Point Linear:First:Electrical Value

Specifies the first electrical value, corresponding to 
 [AI.Bridge.TwoPointLin.First.PhysicalVal](/csh?context=nidaqmx_daqmxprop_attr2f8b)
 . Specify this value in the unit indicated by 
 [AI.Bridge.ElectricalUnits](/csh?context=nidaqmx_daqmxprop_attr2f87)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.Bridge.TwoPointLin.First.ElectricalVal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f8b.html language=enus -->
## TOPIC 00922: Analog Input:Bridge:Scaling Parameters:Two-Point Linear:First:Physical Value

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f8b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f8b.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the first physical value, corresponding to AI.Bridge.TwoPointLin.First.ElectricalVal . Specify this value in the unit indicated by AI.Bridge.PhysicalUnits . Remarks The following table lists the characteristics of this property. Short Name AI.Bridge.TwoPointLin.First.PhysicalVal Data type

### Analog Input:Bridge:Scaling Parameters:Two-Point Linear:First:Physical Value

Specifies the first physical value, corresponding to 
 [AI.Bridge.TwoPointLin.First.ElectricalVal](/csh?context=nidaqmx_daqmxprop_attr2f8a)
 . Specify this value in the unit indicated by 
 [AI.Bridge.PhysicalUnits](/csh?context=nidaqmx_daqmxprop_attr2f88)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.Bridge.TwoPointLin.First.PhysicalVal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f8c.html language=enus -->
## TOPIC 00923: Analog Input:Bridge:Scaling Parameters:Two-Point Linear:Second:Electrical Value

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f8c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f8c.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the second electrical value, corresponding to AI.Bridge.TwoPointLin.Second.PhysicalVal . Specify this value in the unit indicated by AI.Bridge.ElectricalUnits . Remarks The following table lists the characteristics of this property. Short Name AI.Bridge.TwoPointLin.Second.ElectricalVal Dat

### Analog Input:Bridge:Scaling Parameters:Two-Point Linear:Second:Electrical Value

Specifies the second electrical value, corresponding to 
 [AI.Bridge.TwoPointLin.Second.PhysicalVal](/csh?context=nidaqmx_daqmxprop_attr2f8d)
 . Specify this value in the unit indicated by 
 [AI.Bridge.ElectricalUnits](/csh?context=nidaqmx_daqmxprop_attr2f87)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.Bridge.TwoPointLin.Second.ElectricalVal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f8d.html language=enus -->
## TOPIC 00924: Analog Input:Bridge:Scaling Parameters:Two-Point Linear:Second:Physical Value

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f8d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f8d.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the second physical value, corresponding to AI.Bridge.TwoPointLin.Second.ElectricalVal . Specify this value in the unit indicated by AI.Bridge.PhysicalUnits . Remarks The following table lists the characteristics of this property. Short Name AI.Bridge.TwoPointLin.Second.PhysicalVal Data ty

### Analog Input:Bridge:Scaling Parameters:Two-Point Linear:Second:Physical Value

Specifies the second physical value, corresponding to 
 [AI.Bridge.TwoPointLin.Second.ElectricalVal](/csh?context=nidaqmx_daqmxprop_attr2f8c)
 . Specify this value in the unit indicated by 
 [AI.Bridge.PhysicalUnits](/csh?context=nidaqmx_daqmxprop_attr2f88)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.Bridge.TwoPointLin.Second.PhysicalVal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f8e.html language=enus -->
## TOPIC 00925: Analog Input:Bridge:Scaling Parameters:Table:Electrical Values

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f8e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f8e.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the array of electrical values that map to the values in AI.Bridge.Table.PhysicalVals . Specify this value in the unit indicated by AI.Bridge.ElectricalUnits . Remarks The following table lists the characteristics of this property. Short Name AI.Bridge.Table.ElectricalVals Data type c1ddbl

### Analog Input:Bridge:Scaling Parameters:Table:Electrical Values

Specifies the array of electrical values that map to the values in 
 [AI.Bridge.Table.PhysicalVals](/csh?context=nidaqmx_daqmxprop_attr2f8f)
 . Specify this value in the unit indicated by 
 [AI.Bridge.ElectricalUnits](/csh?context=nidaqmx_daqmxprop_attr2f87)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.Bridge.Table.ElectricalVals |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f8f.html language=enus -->
## TOPIC 00926: Analog Input:Bridge:Scaling Parameters:Table:Physical Values

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f8f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f8f.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the array of physical values that map to the values in AI.Bridge.Table.ElectricalVals . Specify this value in the unit indicated by AI.Bridge.PhysicalUnits . Remarks The following table lists the characteristics of this property. Short Name AI.Bridge.Table.PhysicalVals Data type c1ddbl.png

### Analog Input:Bridge:Scaling Parameters:Table:Physical Values

Specifies the array of physical values that map to the values in 
 [AI.Bridge.Table.ElectricalVals](/csh?context=nidaqmx_daqmxprop_attr2f8e)
 . Specify this value in the unit indicated by 
 [AI.Bridge.PhysicalUnits](/csh?context=nidaqmx_daqmxprop_attr2f88)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.Bridge.Table.PhysicalVals |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f90.html language=enus -->
## TOPIC 00927: Analog Input:Bridge:Scaling Parameters:Polynomial:Forward Coefficients

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f90.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f90.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of coefficients for the polynomial that converts electrical values to physical values. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9x^3. Remarks The following table lists the cha

### Analog Input:Bridge:Scaling Parameters:Polynomial:Forward Coefficients

Specifies an array of coefficients for the polynomial that converts electrical values to physical values. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9x^3.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.Bridge.Poly.ForwardCoeff |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f91.html language=enus -->
## TOPIC 00928: Analog Input:Bridge:Scaling Parameters:Polynomial:Reverse Coefficients

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f91.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f91.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of coefficients for the polynomial that converts physical values to electrical values. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9x^3. Remarks The following table lists the cha

### Analog Input:Bridge:Scaling Parameters:Polynomial:Reverse Coefficients

Specifies an array of coefficients for the polynomial that converts physical values to electrical values. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9x^3.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.Bridge.Poly.ReverseCoeff |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2f92.html language=enus -->
## TOPIC 00929: Analog Input:Bridge:Units

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2f92.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2f92.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in which unit to return voltage ratios from the channel. Remarks The following table lists the characteristics of this property. Short Name AI.Bridge.Units Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine

### Analog Input:Bridge:Units

Specifies in which unit to return 
 [voltage ratios](/csh?context=nidaqmx_measfunds_bridgescaling)
 from the channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.Bridge.Units |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Volts/Volt | 15896 | Volts per volt. |
| --- | --- | --- |
| mVolts/Volt | 15897 | Millivolts per volt. |
| From Custom Scale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |
| From TEDS | 12516 | Units defined by TEDS information associated with the channel. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2faf.html language=enus -->
## TOPIC 00930: Counter Input:Count Edges:Count Reset:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2faf.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2faf.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to reset the count on the active edge specified with CI.CountEdges.CountReset.Term . Remarks The following table lists the characteristics of this property. Short Name CI.CountEdges.CountReset.Enable Data type cbool.png Permissions Read/Write Resettable True Settable While Task Is

### Counter Input:Count Edges:Count Reset:Enable

Specifies whether to reset the count on the active edge specified with 
 [CI.CountEdges.CountReset.Term](/csh?context=nidaqmx_daqmxprop_attr2fb1)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.CountEdges.CountReset.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2fb0.html language=enus -->
## TOPIC 00931: Counter Input:Count Edges:Count Reset:Reset Count

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2fb0.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2fb0.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value to reset the count to. Remarks The following table lists the characteristics of this property. Short Name CI.CountEdges.CountReset.ResetCnt Data type cu32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True

### Counter Input:Count Edges:Count Reset:Reset Count

Specifies the value to reset the count to.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.CountEdges.CountReset.ResetCnt |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2fb1.html language=enus -->
## TOPIC 00932: Counter Input:Count Edges:Count Reset:Input:Terminal

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2fb1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2fb1.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to reset the count. Remarks The following table lists the characteristics of this property. Short Name CI.CountEdges.CountReset.Term Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in

### Counter Input:Count Edges:Count Reset:Input:Terminal

Specifies the input terminal of the signal to reset the count.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.CountEdges.CountReset.Term |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2fb2.html language=enus -->
## TOPIC 00933: Counter Input:Count Edges:Count Reset:Active Edge

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2fb2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2fb2.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge of the signal to reset the count. Remarks The following table lists the characteristics of this property. Short Name CI.CountEdges.CountReset.ActiveEdge Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-T

### Counter Input:Count Edges:Count Reset:Active Edge

Specifies on which edge of the signal to reset the count.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.CountEdges.CountReset.ActiveEdge |
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

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2fb3.html language=enus -->
## TOPIC 00934: Counter Input:Count Edges:Count Reset:Input:Digital Filter:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2fb3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2fb3.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply the pulse width filter to the signal. Remarks The following table lists the characteristics of this property. Short Name CI.CountEdges.CountReset.DigFltr.Enable Data type cbool.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Availa

### Counter Input:Count Edges:Count Reset:Input:Digital Filter:Enable

Specifies whether to apply the pulse width filter to the signal.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.CountEdges.CountReset.DigFltr.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2fb4.html language=enus -->
## TOPIC 00935: Counter Input:Count Edges:Count Reset:Input:Digital Filter:Minimum Pulse Width

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2fb4.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2fb4.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the minimum pulse width the filter recognizes. Remarks The following table lists the characteristics of this property. Short Name CI.CountEdges.CountReset.DigFltr.MinPulseWidth Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Availabl

### Counter Input:Count Edges:Count Reset:Input:Digital Filter:Minimum Pulse Width

Specifies the minimum pulse width the filter recognizes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.CountEdges.CountReset.DigFltr.MinPulseWidth |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2fb5.html language=enus -->
## TOPIC 00936: Counter Input:Count Edges:Count Reset:Input:Digital Filter:Timebase:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2fb5.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2fb5.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input of the signal to use as the timebase of the pulse width filter. Remarks The following table lists the characteristics of this property. Short Name CI.CountEdges.CountReset.DigFltr.TimebaseSrc Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is

### Counter Input:Count Edges:Count Reset:Input:Digital Filter:Timebase:Source

Specifies the input of the signal to use as the timebase of the pulse width filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.CountEdges.CountReset.DigFltr.TimebaseSrc |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2fb6.html language=enus -->
## TOPIC 00937: Counter Input:Count Edges:Count Reset:Input:Digital Filter:Timebase:Rate

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2fb6.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2fb6.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. Remarks The following table lists the characteristics of this property. Short Name CI.CountEdges.CountReset.DigFltr.TimebaseRate Data type cdbl.png Permissions Read/Write Rese

### Counter Input:Count Edges:Count Reset:Input:Digital Filter:Timebase:Rate

Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.CountEdges.CountReset.DigFltr.TimebaseRate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2fb7.html language=enus -->
## TOPIC 00938: Counter Input:Count Edges:Count Reset:Input:Digital Synchronization:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2fb7.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2fb7.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. Remarks The following table lists the characteristics of this property. Short Name CI.CountEdges.CountReset.DigSync.Enable Data type cbool.png Permissions Read/Write Resettable True Sett

### Counter Input:Count Edges:Count Reset:Input:Digital Synchronization:Enable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.CountEdges.CountReset.DigSync.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2fb8.html language=enus -->
## TOPIC 00939: Analog Input:General Properties:Signal Conditioning:Thermocouple:Lead Offset Voltage

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2fb8.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2fb8.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the lead offset nulling voltage to subtract from measurements on a device. This property is ignored if open thermocouple detection is disabled. Remarks The following table lists the characteristics of this property. Short Name AI.Thrmcpl.LeadOffsetVoltage Data type cdbl.png Permissions Rea

### Analog Input:General Properties:Signal Conditioning:Thermocouple:Lead Offset Voltage

Specifies the 
 [lead offset nulling](/csh?context=nidaqmx_mxdevconsid_openthermdet)
 voltage to subtract from measurements on a device. This property is ignored if open thermocouple detection is disabled.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.Thrmcpl.LeadOffsetVoltage |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2fbd.html language=enus -->
## TOPIC 00940: Analog Input:General Properties:Filter:Remove Filter Delay

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2fbd.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2fbd.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies if filter delay removal is enabled on the device. Remarks The following table lists the characteristics of this property. Short Name AI.RemoveFilterDelay Data type cbool.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine T

### Analog Input:General Properties:Filter:Remove Filter Delay

Specifies if filter delay removal is enabled on the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.RemoveFilterDelay |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2fed.html language=enus -->
## TOPIC 00941: Analog Input:General Properties:Filter:Filter Delay

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2fed.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2fed.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the amount of time between when the ADC samples data and when the sample is read by the host device. This value is in the units you specify with AI.FilterDelayUnits . You can adjust this amount of time using AI.FilterDelayAdjustment . Remarks The following table lists the characteristics o

### Analog Input:General Properties:Filter:Filter Delay

Indicates the amount of time between when the ADC samples data and when the sample is read by the host device. This value is in the units you specify with 
 [AI.FilterDelayUnits](/csh?context=nidaqmx_daqmxprop_attr3071)
 . You can adjust this amount of time using 
 [AI.FilterDelayAdjustment](/csh?context=nidaqmx_daqmxprop_attr3074)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.FilterDelay |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2fee.html language=enus -->
## TOPIC 00942: Analog Input:General Properties:Filter:Averaging Window Size

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2fee.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2fee.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of samples to average while acquiring data. Increasing the number of samples to average reduces noise in your measurement. Remarks The following table lists the characteristics of this property. Short Name AI.AveragingWinSize Data type cu32.png Permissions Read/Write Resettable

### Analog Input:General Properties:Filter:Averaging Window Size

Specifies the number of samples to average while acquiring data. Increasing the number of samples to average reduces noise in your measurement.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.AveragingWinSize |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2ff4.html language=enus -->
## TOPIC 00943: Analog Input:Velocity:Units

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2ff4.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2ff4.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in which unit to return velocity measurements from the channel. Remarks The following table lists the characteristics of this property. Short Name AI.Velocity.Units Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Tim

### Analog Input:Velocity:Units

Specifies in which unit to return velocity measurements from the channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.Velocity.Units |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| m/s | 15959 | Meters per second. |
| --- | --- | --- |
| in/s | 15960 | Inches per second. |
| From Custom Scale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2ff5.html language=enus -->
## TOPIC 00944: Analog Input:Velocity:IEPE Sensor:dB Reference

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2ff5.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2ff5.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the decibel reference level in the units of the channel. When you read samples as a waveform, the decibel reference level is included in the waveform attributes. Remarks The following table lists the characteristics of this property. Short Name AI.Velocity.IEPESensor.dBRef Data type cdbl.p

### Analog Input:Velocity:IEPE Sensor:dB Reference

Specifies the decibel reference level in the units of the channel. When you read samples as a waveform, the decibel reference level is included in the waveform attributes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.Velocity.IEPESensor.dBRef |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2ff6.html language=enus -->
## TOPIC 00945: Analog Input:Velocity:IEPE Sensor:Sensitivity

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2ff6.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2ff6.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sensitivity of the IEPE velocity sensor connected to the channel. Specify this value in the unit indicated by AI.Velocity.IEPESensor.SensitivityUnits . Remarks The following table lists the characteristics of this property. Short Name AI.Velocity.IEPESensor.Sensitivity Data type cdbl.p

### Analog Input:Velocity:IEPE Sensor:Sensitivity

Specifies the sensitivity of the IEPE velocity sensor connected to the channel. Specify this value in the unit indicated by 
 [AI.Velocity.IEPESensor.SensitivityUnits](/csh?context=nidaqmx_daqmxprop_attr2ff7)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.Velocity.IEPESensor.Sensitivity |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2ff7.html language=enus -->
## TOPIC 00946: Analog Input:Velocity:IEPE Sensor:Sensitivity Units

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2ff7.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2ff7.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units for AI.Velocity.IEPESensor.Sensitivity . Remarks The following table lists the characteristics of this property. Short Name AI.Velocity.IEPESensor.SensitivityUnits Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available i

### Analog Input:Velocity:IEPE Sensor:Sensitivity Units

Specifies the units for 
 [AI.Velocity.IEPESensor.Sensitivity](/csh?context=nidaqmx_daqmxprop_attr2ff6)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.Velocity.IEPESensor.SensitivityUnits |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| mVolts/mm/s | 15963 | Millivolts per millimeter per second. |
| --- | --- | --- |
| mVolts/in/s | 15964 | Millivolts per inch per second. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2ffa.html language=enus -->
## TOPIC 00947: Analog Input:Strain:Force Read From Channel

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2ffa.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2ffa.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the data is returned by DAQmx Read when set on a raw strain channel that is part of a rosette configuration. Remarks The following table lists the characteristics of this property. Short Name AI.Strain.ForceReadFromChan Data type cbool.png Permissions Read/Write Resettable True Set

### Analog Input:Strain:Force Read From Channel

Specifies whether the data is returned by 
 [DAQmx Read](/csh?context=nidaqmx_lvdaqmx_mxread)
 when set on a raw strain channel that is part of a rosette configuration.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.Strain.ForceReadFromChan |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2ffb.html language=enus -->
## TOPIC 00948: Analog Input:Rosette Strain Gage:Strain Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2ffb.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2ffb.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the raw strain channels that comprise the strain rosette. Remarks The following table lists the characteristics of this property. Short Name AI.RosetteStrainGage.StrainChans Data type c1dstr.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available

### Analog Input:Rosette Strain Gage:Strain Channels

Indicates the raw strain channels that comprise the strain rosette.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.RosetteStrainGage.StrainChans |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2ffc.html language=enus -->
## TOPIC 00949: Analog Input:Rosette Strain Gage:Gage Orientation

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2ffc.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2ffc.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies gage orientation in degrees with respect to the X axis. Remarks The following table lists the characteristics of this property. Short Name AI.RosetteStrainGage.GageOrientation Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available

### Analog Input:Rosette Strain Gage:Gage Orientation

Specifies gage orientation in degrees with respect to the X axis.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.RosetteStrainGage.GageOrientation |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2ffd.html language=enus -->
## TOPIC 00950: Analog Input:Rosette Strain Gage:Rosette Measurement Type

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2ffd.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2ffd.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of rosette measurement. Remarks The following table lists the characteristics of this property. Short Name AI.RosetteStrainGage.RosetteMeasType Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine Tru

### Analog Input:Rosette Strain Gage:Rosette Measurement Type

Specifies the type of rosette measurement.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.RosetteStrainGage.RosetteMeasType |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Principal Strain 1 | 15971 | The maximum tensile strain coplanar to the surface of the material under stress. |
| --- | --- | --- |
| Principal Strain 2 | 15972 | The minimum tensile strain coplanar to the surface of the material under stress. |
| Principal Strain Angle | 15973 | The angle at which the principal strains of the rosette occur. |
| Cartesian Strain X | 15974 | The tensile strain coplanar to the surface of the material under stress in the X coordinate direction. |
| Cartesian Strain Y | 15975 | The tensile strain coplanar to the surface of the material under stress in the Y coordinate direction. |
| Cartesian Shear Strain XY | 15976 | The tensile strain coplanar to the surface of the material under stress in the XY coordinate direction. |
| Maximum Shear Strain | 15977 | The maximum strain coplanar to the cross section of the material under stress. |
| Maximum Shear Strain Angle | 15978 | The angle at which the maximum shear strain of the rosette occurs. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr2ffe.html language=enus -->
## TOPIC 00951: Analog Input:Rosette Strain Gage:Rosette Type

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr2ffe.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr2ffe.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the type of rosette gage. Remarks The following table lists the characteristics of this property. Short Name AI.RosetteStrainGage.RosetteType Data type ci32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True Rectangul

### Analog Input:Rosette Strain Gage:Rosette Type

Indicates the type of rosette gage.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.RosetteStrainGage.RosetteType |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Rectangular Rosette | 15968 | A rectangular rosette consists of three strain gages, each separated by a 45 degree angle. |
| --- | --- | --- |
| Delta Rosette | 15969 | A delta rosette consists of three strain gages, each separated by a 60 degree angle. |
| Tee Rosette | 15970 | A tee rosette consists of two gages oriented at 90 degrees with respect to each other. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr3000.html language=enus -->
## TOPIC 00952: Analog Input:General Properties:Advanced:Data Transfer and Memory:USB Transfer Request Count

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr3000.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr3000.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of simultaneous USB transfers used to stream data. Modify this value to affect performance under different combinations of operating system and device. Remarks The following table lists the characteristics of this property. Short Name AI.UsbXferReqCount Data type cu32.pn

### Analog Input:General Properties:Advanced:Data Transfer and Memory:USB Transfer Request Count

Specifies the maximum number of simultaneous USB transfers used to stream data. Modify this value to affect performance under different combinations of operating system and device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.UsbXferReqCount |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr3001.html language=enus -->
## TOPIC 00953: Analog Output:General Properties:Advanced:Data Transfer and Memory:USB Transfer Request Count

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr3001.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr3001.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of simultaneous USB transfers used to stream data. Modify this value to affect performance under different combinations of operating system and device. Remarks The following table lists the characteristics of this property. Short Name AO.UsbXferReqCount Data type cu32.pn

### Analog Output:General Properties:Advanced:Data Transfer and Memory:USB Transfer Request Count

Specifies the maximum number of simultaneous USB transfers used to stream data. Modify this value to affect performance under different combinations of operating system and device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO.UsbXferReqCount |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr3002.html language=enus -->
## TOPIC 00954: Digital Input:General Properties:Advanced:Data Transfer and Memory:USB Transfer Request Count

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr3002.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr3002.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of simultaneous USB transfers used to stream data. Modify this value to affect performance under different combinations of operating system and device. Remarks The following table lists the characteristics of this property. Short Name DI.UsbXferReqCount Data type cu32.pn

### Digital Input:General Properties:Advanced:Data Transfer and Memory:USB Transfer Request Count

Specifies the maximum number of simultaneous USB transfers used to stream data. Modify this value to affect performance under different combinations of operating system and device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DI.UsbXferReqCount |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr3003.html language=enus -->
## TOPIC 00955: Digital Output:General Properties:Advanced:Data Transfer and Memory:USB Transfer Request Count

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr3003.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr3003.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of simultaneous USB transfers used to stream data. Modify this value to affect performance under different combinations of operating system and device. Remarks The following table lists the characteristics of this property. Short Name DO.UsbXferReqCount Data type cu32.pn

### Digital Output:General Properties:Advanced:Data Transfer and Memory:USB Transfer Request Count

Specifies the maximum number of simultaneous USB transfers used to stream data. Modify this value to affect performance under different combinations of operating system and device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DO.UsbXferReqCount |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr3004.html language=enus -->
## TOPIC 00956: Counter Input:General Properties:More:Advanced:Data Transfer and Memory:USB Transfer Request Count

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr3004.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr3004.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of simultaneous USB transfers used to stream data. Modify this value to affect performance under different combinations of operating system and device. Remarks The following table lists the characteristics of this property. Short Name CI.UsbXferReqCount Data type cu32.pn

### Counter Input:General Properties:More:Advanced:Data Transfer and Memory:USB Transfer Request Count

Specifies the maximum number of simultaneous USB transfers used to stream data. Modify this value to affect performance under different combinations of operating system and device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.UsbXferReqCount |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr3005.html language=enus -->
## TOPIC 00957: Counter Output:General Properties:More:Advanced:Data Transfer and Memory:USB Transfer Request Count

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr3005.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr3005.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of simultaneous USB transfers used to stream data. Modify this value to affect performance under different combinations of operating system and device. Remarks The following table lists the characteristics of this property. Short Name CO.UsbXferReqCount Data type cu32.pn

### Counter Output:General Properties:More:Advanced:Data Transfer and Memory:USB Transfer Request Count

Specifies the maximum number of simultaneous USB transfers used to stream data. Modify this value to affect performance under different combinations of operating system and device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CO.UsbXferReqCount |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr3071.html language=enus -->
## TOPIC 00958: Analog Input:General Properties:Filter:Filter Delay Units

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr3071.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr3071.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of AI.FilterDelay and AI.FilterDelayAdjustment . Remarks The following table lists the characteristics of this property. Short Name AI.FilterDelayUnits Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time E

### Analog Input:General Properties:Filter:Filter Delay Units

Specifies the units of 
 [AI.FilterDelay](/csh?context=nidaqmx_daqmxprop_attr2fed)
 and 
 [AI.FilterDelayAdjustment](/csh?context=nidaqmx_daqmxprop_attr3074)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.FilterDelayUnits |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Seconds | 10364 | Seconds. |
| --- | --- | --- |
| Sample Clock Periods | 10286 | Sample Clock Periods. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr3072.html language=enus -->
## TOPIC 00959: Analog Output:General Properties:Filter:Filter Delay Adjustment

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr3072.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr3072.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an additional amount of time to wait between when the sample is written by the host device and when the sample is output by the DAC. This delay adjustment is in addition to the value indicated by AO.FilterDelay . This delay adjustment is in the units you specify with AO.FilterDelayUnits .

### Analog Output:General Properties:Filter:Filter Delay Adjustment

Specifies an additional amount of time to wait between when the sample is written by the host device and when the sample is output by the DAC. This delay adjustment is in addition to the value indicated by 
 [AO.FilterDelay](/csh?context=nidaqmx_daqmxprop_attr3075)
 . This delay adjustment is in the units you specify with 
 [AO.FilterDelayUnits](/csh?context=nidaqmx_daqmxprop_attr3076)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO.FilterDelayAdjustment |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr3074.html language=enus -->
## TOPIC 00960: Analog Input:General Properties:Filter:Filter Delay Adjustment

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr3074.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr3074.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the amount of filter delay that gets removed if AI.RemoveFilterDelay is enabled. This delay adjustment is in addition to the value indicated by AI.FilterDelay . This delay adjustment is in the units you specify with AI.FilterDelayUnits . Remarks The following table lists the characteristic

### Analog Input:General Properties:Filter:Filter Delay Adjustment

Specifies the amount of filter delay that gets removed if 
 [AI.RemoveFilterDelay](/csh?context=nidaqmx_daqmxprop_attr2fbd)
 is enabled. This delay adjustment is in addition to the value indicated by 
 [AI.FilterDelay](/csh?context=nidaqmx_daqmxprop_attr2fed)
 . This delay adjustment is in the units you specify with 
 [AI.FilterDelayUnits](/csh?context=nidaqmx_daqmxprop_attr3071)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.FilterDelayAdjustment |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr3075.html language=enus -->
## TOPIC 00961: Analog Output:General Properties:Filter:Filter Delay

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr3075.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr3075.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the amount of time between when the sample is written by the host device and when the sample is output by the DAC. This value is in the units you specify with AO.FilterDelayUnits . Remarks The following table lists the characteristics of this property. Short Name AO.FilterDelay Data type c

### Analog Output:General Properties:Filter:Filter Delay

Specifies the amount of time between when the sample is written by the host device and when the sample is output by the DAC. This value is in the units you specify with 
 [AO.FilterDelayUnits](/csh?context=nidaqmx_daqmxprop_attr3076)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO.FilterDelay |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr3076.html language=enus -->
## TOPIC 00962: Analog Output:General Properties:Filter:Filter Delay Units

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr3076.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr3076.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of AO.FilterDelay and AO.FilterDelayAdjustment . Remarks The following table lists the characteristics of this property. Short Name AO.FilterDelayUnits Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time E

### Analog Output:General Properties:Filter:Filter Delay Units

Specifies the units of 
 [AO.FilterDelay](/csh?context=nidaqmx_daqmxprop_attr3075)
 and 
 [AO.FilterDelayAdjustment](/csh?context=nidaqmx_daqmxprop_attr3072)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO.FilterDelayUnits |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Seconds | 10364 | Seconds. |
| --- | --- | --- |
| Sample Clock Periods | 10286 | Sample Clock Periods. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr308d.html language=enus -->
## TOPIC 00963: Counter Input:Duty Cycle:Input:Terminal

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr308d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr308d.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to measure. Remarks The following table lists the characteristics of this property. Short Name CI.DutyCycle.Term Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine Tru

### Counter Input:Duty Cycle:Input:Terminal

Specifies the input terminal of the signal to measure.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.DutyCycle.Term |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr308e.html language=enus -->
## TOPIC 00964: Counter Input:Duty Cycle:Input:Digital Filter:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr308e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr308e.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply the pulse width filter to the signal. Remarks The following table lists the characteristics of this property. Short Name CI.DutyCycle.DigFltr.Enable Data type cbool.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-T

### Counter Input:Duty Cycle:Input:Digital Filter:Enable

Specifies whether to apply the pulse width filter to the signal.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.DutyCycle.DigFltr.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr308f.html language=enus -->
## TOPIC 00965: Counter Input:Duty Cycle:Input:Digital Filter:Minimum Pulse Width

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr308f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr308f.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the digital filter recognizes. Remarks The following table lists the characteristics of this property. Short Name CI.DutyCycle.DigFltr.MinPulseWidth Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific A

### Counter Input:Duty Cycle:Input:Digital Filter:Minimum Pulse Width

Specifies in seconds the minimum pulse width the digital filter recognizes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.DutyCycle.DigFltr.MinPulseWidth |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr3090.html language=enus -->
## TOPIC 00966: Counter Input:Duty Cycle:Input:Digital Filter:Timebase:Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr3090.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr3090.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to use as the timebase of the pulse width filter. Remarks The following table lists the characteristics of this property. Short Name CI.DutyCycle.DigFltr.TimebaseSrc Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Run

### Counter Input:Duty Cycle:Input:Digital Filter:Timebase:Source

Specifies the input terminal of the signal to use as the timebase of the pulse width filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.DutyCycle.DigFltr.TimebaseSrc |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr3091.html language=enus -->
## TOPIC 00967: Counter Input:Duty Cycle:Input:Digital Filter:Timebase:Rate

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr3091.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr3091.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. Remarks The following table lists the characteristics of this property. Short Name CI.DutyCycle.DigFltr.TimebaseRate Data type cdbl.png Permissions Read/Write Resettable True

### Counter Input:Duty Cycle:Input:Digital Filter:Timebase:Rate

Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.DutyCycle.DigFltr.TimebaseRate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr3092.html language=enus -->
## TOPIC 00968: Counter Input:Duty Cycle:StartingEdge

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr3092.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr3092.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies which edge of the input signal to begin the duty cycle measurement. Remarks The following table lists the characteristics of this property. Short Name CI.DutyCycle.StartingEdge Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Availabl

### Counter Input:Duty Cycle:StartingEdge

Specifies which edge of the input signal to begin the duty cycle measurement.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.DutyCycle.StartingEdge |
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

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr3093.html language=enus -->
## TOPIC 00969: Counter Input:General Properties:More:Sample Clock Overrun Behavior

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr3093.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr3093.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the counter behavior when data is read but a new value was not detected during a sample clock. Remarks The following table lists the characteristics of this property. Short Name CI.SampClkOverrunBehavior Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Runni

### Counter Input:General Properties:More:Sample Clock Overrun Behavior

Specifies the counter behavior when data is read but a new value was not detected during a sample clock.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.SampClkOverrunBehavior |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Repeated Data | 16062 | Repeat the last sample. |
| --- | --- | --- |
| Sentinel Value | 16063 | Return the sentinel value. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr3094.html language=enus -->
## TOPIC 00970: Counter Input:General Properties:More:Sample Clock Overrun Sentinel Value

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr3094.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr3094.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sentinel value returned when the No New Sample Behavior is set to Sentinel Value. Remarks The following table lists the characteristics of this property. Short Name CI.SampClkOverrunSentinelVal Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running dev

### Counter Input:General Properties:More:Sample Clock Overrun Sentinel Value

Specifies the sentinel value returned when the No New Sample Behavior is set to Sentinel Value.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.SampClkOverrunSentinelVal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr3095.html language=enus -->
## TOPIC 00971: Counter Input:General Properties:More:Advanced:Maximum Measurable Period

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr3095.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr3095.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum period (in seconds) in which the device will recognize signals. For frequency measurements, a signal with a higher period than the one set in this property will return 0 Hz. For duty cycle, the device will return 0 or 1 depending on the state of the line during the max defined

### Counter Input:General Properties:More:Advanced:Maximum Measurable Period

Specifies the maximum period (in seconds) in which the device will recognize signals. For frequency measurements, a signal with a higher period than the one set in this property will return 0 Hz. For duty cycle, the device will return 0 or 1 depending on the state of the line during the max defined period of time. Period measurements will return NaN. Pulse width measurement will return zero.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.MaxMeasPeriod |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr3097.html language=enus -->
## TOPIC 00972: Counter Input:Frequency:Input:Terminal Configuration

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr3097.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr3097.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal configuration. Remarks The following table lists the characteristics of this property. Short Name CI.Freq.TermCfg Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True Differential 10106

### Counter Input:Frequency:Input:Terminal Configuration

Specifies the input terminal configuration.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Freq.TermCfg |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Differential | 10106 | Differential. |
| --- | --- | --- |
| RSE | 10083 | Referenced Single-Ended. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr3098.html language=enus -->
## TOPIC 00973: Counter Input:Frequency:Input:Logic Level Behavior

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr3098.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr3098.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic level behavior on the input line. Remarks The following table lists the characteristics of this property. Short Name CI.Freq.LogicLvlBehavior Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True

### Counter Input:Frequency:Input:Logic Level Behavior

Specifies the logic level behavior on the input line.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Freq.LogicLvlBehavior |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Logic Level Pull-up | 16064 | High logic. |
| --- | --- | --- |
| None | 10230 | Supply no excitation to the channel. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr3099.html language=enus -->
## TOPIC 00974: Counter Input:Period:Input:Terminal Configuration

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr3099.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr3099.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal configuration. Remarks The following table lists the characteristics of this property. Short Name CI.Period.TermCfg Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True Differential 101

### Counter Input:Period:Input:Terminal Configuration

Specifies the input terminal configuration.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Period.TermCfg |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Differential | 10106 | Differential. |
| --- | --- | --- |
| RSE | 10083 | Referenced Single-Ended. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr309a.html language=enus -->
## TOPIC 00975: Counter Input:Period:Input:Logic Level Behavior

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr309a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr309a.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic level behavior on the input line. Remarks The following table lists the characteristics of this property. Short Name CI.Period.LogicLvlBehavior Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine Tr

### Counter Input:Period:Input:Logic Level Behavior

Specifies the logic level behavior on the input line.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Period.LogicLvlBehavior |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Logic Level Pull-up | 16064 | High logic. |
| --- | --- | --- |
| None | 10230 | Supply no excitation to the channel. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr309b.html language=enus -->
## TOPIC 00976: Counter Input:Count Edges:Input:Terminal Configuration

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr309b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr309b.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal configuration. Remarks The following table lists the characteristics of this property. Short Name CI.CountEdges.TermCfg Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True Differential

### Counter Input:Count Edges:Input:Terminal Configuration

Specifies the input terminal configuration.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.CountEdges.TermCfg |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Differential | 10106 | Differential. |
| --- | --- | --- |
| RSE | 10083 | Referenced Single-Ended. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr309c.html language=enus -->
## TOPIC 00977: Counter Input:Count Edges:Input:Logic Level Behavior

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr309c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr309c.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic level behavior on the input line. Remarks The following table lists the characteristics of this property. Short Name CI.CountEdges.LogicLvlBehavior Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engin

### Counter Input:Count Edges:Input:Logic Level Behavior

Specifies the logic level behavior on the input line.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.CountEdges.LogicLvlBehavior |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Logic Level Pull-up | 16064 | High logic. |
| --- | --- | --- |
| None | 10230 | Supply no excitation to the channel. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr309d.html language=enus -->
## TOPIC 00978: Counter Input:Count Edges:Count Direction:Input:Terminal Configuration

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr309d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr309d.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal configuration. Remarks The following table lists the characteristics of this property. Short Name CI.CountEdges.CountDir.TermCfg Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True Dif

### Counter Input:Count Edges:Count Direction:Input:Terminal Configuration

Specifies the input terminal configuration.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.CountEdges.CountDir.TermCfg |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Differential | 10106 | Differential. |
| --- | --- | --- |
| RSE | 10083 | Referenced Single-Ended. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr309e.html language=enus -->
## TOPIC 00979: Counter Input:Count Edges:Count Direction:Input:Logic Level Behavior

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr309e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr309e.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic level behavior on the count reset line. Remarks The following table lists the characteristics of this property. Short Name CI.CountEdges.CountDir.LogicLvlBehavior Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in

### Counter Input:Count Edges:Count Direction:Input:Logic Level Behavior

Specifies the logic level behavior on the count reset line.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.CountEdges.CountDir.LogicLvlBehavior |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Logic Level Pull-up | 16064 | High logic. |
| --- | --- | --- |
| None | 10230 | Supply no excitation to the channel. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr309f.html language=enus -->
## TOPIC 00980: Counter Input:Count Edges:Count Reset:Input:Terminal Configuration

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr309f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr309f.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal configuration. Remarks The following table lists the characteristics of this property. Short Name CI.CountEdges.CountReset.TermCfg Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True D

### Counter Input:Count Edges:Count Reset:Input:Terminal Configuration

Specifies the input terminal configuration.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.CountEdges.CountReset.TermCfg |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Differential | 10106 | Differential. |
| --- | --- | --- |
| RSE | 10083 | Referenced Single-Ended. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr30a0.html language=enus -->
## TOPIC 00981: Counter Input:Count Edges:Count Reset:Input:Logic Level Behavior

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr30a0.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr30a0.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic level behavior on the count reset line. Remarks The following table lists the characteristics of this property. Short Name CI.CountEdges.CountReset.LogicLvlBehavior Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available

### Counter Input:Count Edges:Count Reset:Input:Logic Level Behavior

Specifies the logic level behavior on the count reset line.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.CountEdges.CountReset.LogicLvlBehavior |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Logic Level Pull-up | 16064 | High logic. |
| --- | --- | --- |
| None | 10230 | Supply no excitation to the channel. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr30a1.html language=enus -->
## TOPIC 00982: Counter Input:Duty Cycle:Input:Terminal Configuration

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr30a1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr30a1.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal configuration. Remarks The following table lists the characteristics of this property. Short Name CI.DutyCycle.TermCfg Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True Differential

### Counter Input:Duty Cycle:Input:Terminal Configuration

Specifies the input terminal configuration.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.DutyCycle.TermCfg |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Differential | 10106 | Differential. |
| --- | --- | --- |
| RSE | 10083 | Referenced Single-Ended. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr30a2.html language=enus -->
## TOPIC 00983: Counter Input:Duty Cycle:Input:Logic Level Behavior

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr30a2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr30a2.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic level behavior on the input line. Remarks The following table lists the characteristics of this property. Short Name CI.DutyCycle.LogicLvlBehavior Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine

### Counter Input:Duty Cycle:Input:Logic Level Behavior

Specifies the logic level behavior on the input line.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.DutyCycle.LogicLvlBehavior |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Logic Level Pull-up | 16064 | High logic. |
| --- | --- | --- |
| None | 10230 | Supply no excitation to the channel. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr30a3.html language=enus -->
## TOPIC 00984: Counter Input:Position:A Input:Terminal Configuration

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr30a3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr30a3.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal configuration. Remarks The following table lists the characteristics of this property. Short Name CI.Encoder.AInput.TermCfg Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True Differen

### Counter Input:Position:A Input:Terminal Configuration

Specifies the input terminal configuration.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Encoder.AInput.TermCfg |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Differential | 10106 | Differential. |
| --- | --- | --- |
| RSE | 10083 | Referenced Single-Ended. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr30a4.html language=enus -->
## TOPIC 00985: Counter Input:Position:A Input:Logic Level Behavior

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr30a4.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr30a4.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic level behavior on the input line. Remarks The following table lists the characteristics of this property. Short Name CI.Encoder.AInput.LogicLvlBehavior Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time E

### Counter Input:Position:A Input:Logic Level Behavior

Specifies the logic level behavior on the input line.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Encoder.AInput.LogicLvlBehavior |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Logic Level Pull-up | 16064 | High logic. |
| --- | --- | --- |
| None | 10230 | Supply no excitation to the channel. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr30a5.html language=enus -->
## TOPIC 00986: Counter Input:Position:B Input:Terminal Configuration

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr30a5.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr30a5.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal configuration. Remarks The following table lists the characteristics of this property. Short Name CI.Encoder.BInput.TermCfg Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True Differen

### Counter Input:Position:B Input:Terminal Configuration

Specifies the input terminal configuration.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Encoder.BInput.TermCfg |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Differential | 10106 | Differential. |
| --- | --- | --- |
| RSE | 10083 | Referenced Single-Ended. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr30a6.html language=enus -->
## TOPIC 00987: Counter Input:Position:B Input:Logic Level Behavior

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr30a6.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr30a6.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic level behavior on the input line. Remarks The following table lists the characteristics of this property. Short Name CI.Encoder.BInput.LogicLvlBehavior Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time E

### Counter Input:Position:B Input:Logic Level Behavior

Specifies the logic level behavior on the input line.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Encoder.BInput.LogicLvlBehavior |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Logic Level Pull-up | 16064 | High logic. |
| --- | --- | --- |
| None | 10230 | Supply no excitation to the channel. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr30a7.html language=enus -->
## TOPIC 00988: Counter Input:Position:Z Input:Terminal Configuration

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr30a7.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr30a7.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal configuration. Remarks The following table lists the characteristics of this property. Short Name CI.Encoder.ZInput.TermCfg Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True Differen

### Counter Input:Position:Z Input:Terminal Configuration

Specifies the input terminal configuration.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Encoder.ZInput.TermCfg |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Differential | 10106 | Differential. |
| --- | --- | --- |
| RSE | 10083 | Referenced Single-Ended. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr30a8.html language=enus -->
## TOPIC 00989: Counter Input:Position:Z Input:Logic Level Behavior

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr30a8.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr30a8.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic level behavior on the input line. Remarks The following table lists the characteristics of this property. Short Name CI.Encoder.ZInput.LogicLvlBehavior Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time E

### Counter Input:Position:Z Input:Logic Level Behavior

Specifies the logic level behavior on the input line.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Encoder.ZInput.LogicLvlBehavior |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Logic Level Pull-up | 16064 | High logic. |
| --- | --- | --- |
| None | 10230 | Supply no excitation to the channel. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr30a9.html language=enus -->
## TOPIC 00990: Counter Input:Pulse Width:Input:Terminal Configuration

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr30a9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr30a9.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal configuration. Remarks The following table lists the characteristics of this property. Short Name CI.PulseWidth.TermCfg Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True Differential

### Counter Input:Pulse Width:Input:Terminal Configuration

Specifies the input terminal configuration.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.PulseWidth.TermCfg |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Differential | 10106 | Differential. |
| --- | --- | --- |
| RSE | 10083 | Referenced Single-Ended. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr30aa.html language=enus -->
## TOPIC 00991: Counter Input:Pulse Width:Input:Logic Level Behavior

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr30aa.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr30aa.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic level behavior on the input line. Remarks The following table lists the characteristics of this property. Short Name CI.PulseWidth.LogicLvlBehavior Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engin

### Counter Input:Pulse Width:Input:Logic Level Behavior

Specifies the logic level behavior on the input line.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.PulseWidth.LogicLvlBehavior |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Logic Level Pull-up | 16064 | High logic. |
| --- | --- | --- |
| None | 10230 | Supply no excitation to the channel. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr30ab.html language=enus -->
## TOPIC 00992: Counter Input:Two Edge Separation:First:Input:Terminal Configuration

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr30ab.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr30ab.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal configuration. Remarks The following table lists the characteristics of this property. Short Name CI.TwoEdgeSep.First.TermCfg Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True Differ

### Counter Input:Two Edge Separation:First:Input:Terminal Configuration

Specifies the input terminal configuration.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.TwoEdgeSep.First.TermCfg |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Differential | 10106 | Differential. |
| --- | --- | --- |
| RSE | 10083 | Referenced Single-Ended. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr30ac.html language=enus -->
## TOPIC 00993: Counter Input:Two Edge Separation:First:Input:Logic Level Behavior

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr30ac.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr30ac.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic level behavior on the input line. Remarks The following table lists the characteristics of this property. Short Name CI.TwoEdgeSep.First.LogicLvlBehavior Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time

### Counter Input:Two Edge Separation:First:Input:Logic Level Behavior

Specifies the logic level behavior on the input line.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.TwoEdgeSep.First.LogicLvlBehavior |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Logic Level Pull-up | 16064 | High logic. |
| --- | --- | --- |
| None | 10230 | Supply no excitation to the channel. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr30ad.html language=enus -->
## TOPIC 00994: Counter Input:Two Edge Separation:Second:Input:Terminal Configuration

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr30ad.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr30ad.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal configuration. Remarks The following table lists the characteristics of this property. Short Name CI.TwoEdgeSep.Second.TermCfg Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True Diffe

### Counter Input:Two Edge Separation:Second:Input:Terminal Configuration

Specifies the input terminal configuration.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.TwoEdgeSep.Second.TermCfg |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Differential | 10106 | Differential. |
| --- | --- | --- |
| RSE | 10083 | Referenced Single-Ended. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr30ae.html language=enus -->
## TOPIC 00995: Counter Input:Two Edge Separation:Second:Input:Logic Level Behavior

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr30ae.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr30ae.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic level behavior on the count reset line. Remarks The following table lists the characteristics of this property. Short Name CI.TwoEdgeSep.Second.LogicLvlBehavior Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in R

### Counter Input:Two Edge Separation:Second:Input:Logic Level Behavior

Specifies the logic level behavior on the count reset line.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.TwoEdgeSep.Second.LogicLvlBehavior |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Logic Level Pull-up | 16064 | High logic. |
| --- | --- | --- |
| None | 10230 | Supply no excitation to the channel. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr30af.html language=enus -->
## TOPIC 00996: Counter Input:Semi-Period:Input:Terminal Configuration

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr30af.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr30af.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal configuration. Remarks The following table lists the characteristics of this property. Short Name CI.SemiPeriod.TermCfg Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True Differential

### Counter Input:Semi-Period:Input:Terminal Configuration

Specifies the input terminal configuration.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.SemiPeriod.TermCfg |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Differential | 10106 | Differential. |
| --- | --- | --- |
| RSE | 10083 | Referenced Single-Ended. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr30b0.html language=enus -->
## TOPIC 00997: Counter Input:Semi-Period:Input:Logic Level Behavior

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr30b0.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr30b0.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic level behavior on the count reset line. Remarks The following table lists the characteristics of this property. Short Name CI.SemiPeriod.LogicLvlBehavior Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time

### Counter Input:Semi-Period:Input:Logic Level Behavior

Specifies the logic level behavior on the count reset line.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.SemiPeriod.LogicLvlBehavior |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Logic Level Pull-up | 16064 | High logic. |
| --- | --- | --- |
| None | 10230 | Supply no excitation to the channel. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr30b1.html language=enus -->
## TOPIC 00998: Counter Input:Pulse:Frequency:Input:Terminal Configuration

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr30b1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr30b1.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal configuration. Remarks The following table lists the characteristics of this property. Short Name CI.Pulse.Freq.TermCfg Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True Differential

### Counter Input:Pulse:Frequency:Input:Terminal Configuration

Specifies the input terminal configuration.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Pulse.Freq.TermCfg |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Differential | 10106 | Differential. |
| --- | --- | --- |
| RSE | 10083 | Referenced Single-Ended. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr30b2.html language=enus -->
## TOPIC 00999: Counter Input:Pulse:Frequency:Input:Logic Level Behavior

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr30b2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr30b2.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic level behavior on the count reset line. Remarks The following table lists the characteristics of this property. Short Name CI.Pulse.Freq.LogicLvlBehavior Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time

### Counter Input:Pulse:Frequency:Input:Logic Level Behavior

Specifies the logic level behavior on the count reset line.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Pulse.Freq.LogicLvlBehavior |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Logic Level Pull-up | 16064 | High logic. |
| --- | --- | --- |
| None | 10230 | Supply no excitation to the channel. |

Parent topic:

DAQmx Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-channel/attr30b3.html language=enus -->
## TOPIC 01000: Counter Input:Pulse:Time:Input:Terminal Configuration

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-channel/attr30b3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-channel/attr30b3.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal configuration. Remarks The following table lists the characteristics of this property. Short Name CI.Pulse.Time.TermCfg Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True Differential

### Counter Input:Pulse:Time:Input:Terminal Configuration

Specifies the input terminal configuration.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.Pulse.Time.TermCfg |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Differential | 10106 | Differential. |
| --- | --- | --- |
| RSE | 10083 | Referenced Single-Ended. |

Parent topic:

DAQmx Channel Properties
